#!/usr/bin/env python3
"""Diagnose a small HTTPS sample through newly appended LAN VLESS proxies."""

import argparse
import json
import os
import socket
import ssl
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import build_subscription as builder


HTTPS_TARGETS = (
    ("cp.cloudflare.com", "/generate_204", 204),
    ("www.gstatic.com", "/generate_204", 204),
)


def free_local_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.bind(("127.0.0.1", 0))
        return int(listener.getsockname()[1])


def wait_for_port(port: int, process: subprocess.Popen, timeout: float = 6.0) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError(f"mihomo exited with code {process.returncode}")
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.25):
                return
        except OSError:
            time.sleep(0.1)
    raise TimeoutError("mihomo did not open its local proxy port")


def receive_exact(connection: socket.socket, length: int) -> bytes:
    chunks = bytearray()
    while len(chunks) < length:
        chunk = connection.recv(length - len(chunks))
        if not chunk:
            raise ConnectionError("SOCKS5 connection closed during handshake")
        chunks.extend(chunk)
    return bytes(chunks)


def socks5_connect(port: int, host: str, target_port: int, timeout: float) -> socket.socket:
    target = host.encode("idna")
    connection = socket.create_connection(("127.0.0.1", port), timeout=timeout)
    try:
        connection.settimeout(timeout)
        connection.sendall(b"\x05\x01\x00")
        if receive_exact(connection, 2) != b"\x05\x00":
            raise RuntimeError("SOCKS5 authentication negotiation failed")
        request = (
            b"\x05\x01\x00\x03"
            + bytes([len(target)])
            + target
            + target_port.to_bytes(2, "big")
        )
        connection.sendall(request)
        header = receive_exact(connection, 4)
        if header[0] != 5 or header[1] != 0:
            raise RuntimeError(f"SOCKS5 CONNECT failed with reply {header[1]}")
        address_type = header[3]
        if address_type == 1:
            receive_exact(connection, 4)
        elif address_type == 3:
            receive_exact(connection, receive_exact(connection, 1)[0])
        elif address_type == 4:
            receive_exact(connection, 16)
        else:
            raise RuntimeError(f"SOCKS5 returned unknown address type {address_type}")
        receive_exact(connection, 2)
        return connection
    except Exception:
        connection.close()
        raise


def resolve_addresses(host: str, port: int) -> list[str]:
    addresses = {
        item[4][0]
        for item in socket.getaddrinfo(
            host, port, family=socket.AF_UNSPEC, type=socket.SOCK_STREAM
        )
    }
    return sorted(addresses)


def read_http_response(
    secure: ssl.SSLSocket,
    host: str,
    path: str,
    body_limit: int,
) -> tuple[int, bytes]:
    secure.sendall(
        f"GET {path} HTTP/1.1\r\nHost: {host}\r\n"
        "User-Agent: pale-signal-lan-health-check/2.0\r\n"
        "Accept: */*\r\nConnection: close\r\n\r\n".encode("ascii")
    )
    payload = bytearray()
    header_end = -1
    while header_end < 0:
        chunk = secure.recv(4096)
        if not chunk:
            raise ConnectionError("HTTPS response ended before headers")
        payload.extend(chunk)
        if len(payload) > 65536:
            raise RuntimeError("HTTPS response headers are too large")
        header_end = payload.find(b"\r\n\r\n")
    status_line = bytes(payload[:header_end]).decode(
        "iso-8859-1", errors="replace"
    ).splitlines()[0]
    parts = status_line.split()
    if len(parts) < 2 or not parts[1].isdigit():
        raise RuntimeError(f"invalid HTTPS status line: {status_line}")
    status = int(parts[1])
    body = bytearray(payload[header_end + 4 :])
    while body_limit and len(body) < body_limit:
        chunk = secure.recv(min(65536, body_limit - len(body)))
        if not chunk:
            break
        body.extend(chunk)
    return status, bytes(body)


def direct_https_probe(host: str, path: str, expected: int, timeout: float) -> dict:
    result = {
        "url": f"https://{host}{path}",
        "dns": False,
        "addresses": [],
        "tcp": False,
        "tls": False,
        "https": False,
        "http_status": None,
        "error_phase": "",
        "error": "",
    }
    connection = None
    try:
        result["addresses"] = resolve_addresses(host, 443)
        result["dns"] = bool(result["addresses"])
        connection = socket.create_connection((host, 443), timeout=timeout)
        result["tcp"] = True
        context = ssl.create_default_context()
        with context.wrap_socket(connection, server_hostname=host) as secure:
            connection = None
            secure.settimeout(timeout)
            result["tls"] = True
            status, _body = read_http_response(secure, host, path, 0)
            result["http_status"] = status
            result["https"] = status == expected
            if status != expected:
                raise RuntimeError(f"expected HTTP {expected}, got HTTP {status}")
    except Exception as exc:
        if not result["dns"]:
            result["error_phase"] = "dns"
        elif not result["tcp"]:
            result["error_phase"] = "tcp"
        elif not result["tls"]:
            result["error_phase"] = "tls"
        else:
            result["error_phase"] = "https"
        result["error"] = f"{type(exc).__name__}: {exc}"
    finally:
        if connection is not None:
            connection.close()
    return result


def https_probe_via_socks(
    port: int,
    host: str,
    path: str,
    expected: int,
    timeout: float,
    body_limit: int = 0,
) -> dict:
    result = {
        "url": f"https://{host}{path}",
        "socks_accepted": False,
        "tls": False,
        "https": False,
        "http_status": None,
        "bytes": 0,
        "latency_ms": None,
        "error_phase": "",
        "error": "",
    }
    connection = None
    started = time.monotonic()
    try:
        connection = socks5_connect(port, host, 443, timeout)
        result["socks_accepted"] = True
        context = ssl.create_default_context()
        with context.wrap_socket(connection, server_hostname=host) as secure:
            connection = None
            secure.settimeout(timeout)
            result["tls"] = True
            status, body = read_http_response(secure, host, path, body_limit)
            result["http_status"] = status
            result["bytes"] = len(body)
            result["https"] = status == expected
            if status != expected:
                raise RuntimeError(f"expected HTTP {expected}, got HTTP {status}")
            result["latency_ms"] = round((time.monotonic() - started) * 1000)
    except Exception as exc:
        if not result["socks_accepted"]:
            result["error_phase"] = "socks_connect"
        elif not result["tls"]:
            result["error_phase"] = "tls"
        else:
            result["error_phase"] = "https"
        result["error"] = f"{type(exc).__name__}: {exc}"
    finally:
        if connection is not None:
            connection.close()
    return result


def proxy_server_diagnostics(proxy: dict, timeout: float) -> dict:
    host = str(proxy.get("server", ""))
    port = int(proxy.get("port", 0) or 0)
    result = {
        "server": host,
        "port": port,
        "dns": False,
        "addresses": [],
        "tcp": False,
        "error": "",
    }
    try:
        result["addresses"] = resolve_addresses(host, port)
        result["dns"] = bool(result["addresses"])
        with socket.create_connection((host, port), timeout=timeout):
            result["tcp"] = True
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
    return result


def test_proxy(mihomo: Path, proxy: dict, timeout: float) -> dict:
    port = free_local_port()
    config = builder.build_config([proxy])
    config["mixed-port"] = port
    config["log-level"] = "debug"
    started = time.monotonic()
    result = {
        "name": proxy.get("name", "unnamed"),
        "route_enforcement": "single VLESS proxy with MATCH,PROXY; HTTPS sent to its local SOCKS5 port",
        "proxy_server": proxy_server_diagnostics(proxy, timeout),
        "mihomo_ready": False,
        "socks_accepted": False,
        "tls": False,
        "https": False,
        "transfer": False,
        "latency_ms": None,
        "verification_status": "не проверено",
        "probes": [],
        "transfer_probe": None,
        "error": "",
        "mihomo_log_tail": [],
    }
    with tempfile.TemporaryDirectory(prefix="pale-signal-lan-check-") as temp_dir:
        root = Path(temp_dir)
        config_path = root / "config.yaml"
        log_path = root / "mihomo.log"
        config_path.write_text(
            "\n".join(builder.dump_yaml(config)) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (root / "home").mkdir()
        with log_path.open("wb") as log_file:
            process = subprocess.Popen(
                [str(mihomo), "-d", str(root / "home"), "-f", str(config_path)],
                stdout=log_file,
                stderr=subprocess.STDOUT,
            )
            try:
                wait_for_port(port, process)
                result["mihomo_ready"] = True
                for host, path, expected in HTTPS_TARGETS:
                    result["probes"].append(
                        https_probe_via_socks(port, host, path, expected, timeout)
                    )
                result["socks_accepted"] = any(
                    probe["socks_accepted"] for probe in result["probes"]
                )
                result["tls"] = any(probe["tls"] for probe in result["probes"])
                result["https"] = any(probe["https"] for probe in result["probes"])
                latencies = [
                    probe["latency_ms"]
                    for probe in result["probes"]
                    if probe["https"] and probe["latency_ms"] is not None
                ]
                result["latency_ms"] = min(latencies) if latencies else None
                if result["https"]:
                    transfer = https_probe_via_socks(
                        port,
                        "speed.cloudflare.com",
                        "/__down?bytes=65536",
                        200,
                        timeout,
                        body_limit=65536,
                    )
                    result["transfer_probe"] = transfer
                    result["transfer"] = transfer["https"] and transfer["bytes"] >= 65536
                    result["verification_status"] = "проверено"
                failures = [
                    f"{probe['url']} [{probe['error_phase']}]: {probe['error']}"
                    for probe in result["probes"]
                    if not probe["https"]
                ]
                if result["transfer_probe"] and not result["transfer"]:
                    transfer = result["transfer_probe"]
                    transfer_error = transfer["error"] or f"bytes={transfer['bytes']}"
                    failures.append(
                        f"{transfer['url']} [{transfer['error_phase']}]: {transfer_error}"
                    )
                result["error"] = "; ".join(failures)
            except Exception as exc:
                result["error"] = f"mihomo_startup: {type(exc).__name__}: {exc}"
            finally:
                if process.poll() is None:
                    process.terminate()
                    try:
                        process.wait(timeout=3)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait(timeout=3)
        log_lines = log_path.read_text(encoding="utf-8", errors="replace").splitlines()
        result["mihomo_log_tail"] = log_lines[-30:]
    result["elapsed_ms"] = round((time.monotonic() - started) * 1000)
    return result


def diagnose_environment(timeout: float) -> dict:
    return {
        "direct_targets": [
            direct_https_probe(host, path, expected, timeout)
            for host, path, expected in HTTPS_TARGETS
        ]
    }


def assess_environment(
    diagnostics: dict,
    new_results: dict[str, list[dict]],
    legacy_results: list[dict],
) -> None:
    direct_ok = all(item["https"] for item in diagnostics["direct_targets"])
    new_success = sum(
        bool(result["https"])
        for source_results in new_results.values()
        for result in source_results
    )
    legacy_success = sum(bool(result["https"]) for result in legacy_results)
    if not direct_ok:
        code = "local_https_unavailable"
        text = "не проверено: тестовые HTTPS URL недоступны напрямую из локального окружения"
    elif new_success:
        code = "new_https_confirmed"
        text = f"HTTPS через VLESS подтверждён для {new_success} новых образцов"
    elif legacy_results and legacy_success:
        code = "new_candidates_failed_controls_passed"
        text = (
            "новые образцы не подтвердили HTTPS, тогда как старый контрольный узел прошёл; "
            "вероятнее проблема новых серверов"
        )
    elif legacy_results:
        code = "vless_path_inconclusive"
        text = (
            "не проверено: прямой HTTPS работает, но одинаковый сбой есть у новых и старых "
            "контрольных VLESS; отделить неисправность серверов от ограничения общего "
            "VLESS-пути в этом окружении нельзя"
        )
    else:
        code = "new_candidates_unverified"
        text = (
            "не проверено: прямой HTTPS работает, но новые VLESS не подтвердили HTTPS; "
            "контроль старого пула не выполнялся"
        )
    diagnostics.update(
        {
            "assessment_code": code,
            "assessment": text,
            "new_https_success": new_success,
            "legacy_https_success": legacy_success,
            "legacy_controls_tested": len(legacy_results),
        }
    )


def update_stats(
    stats: dict,
    results: dict[str, list[dict]],
    diagnostics: dict,
    legacy_results: list[dict],
) -> None:
    for source_id, source_results in results.items():
        item = stats.get("sources", {}).get(source_id)
        if not isinstance(item, dict):
            continue
        latencies = [
            result["latency_ms"]
            for result in source_results
            if result.get("https") and isinstance(result.get("latency_ms"), int)
        ]
        item["socks_accepted_tested"] = len(source_results)
        item["socks_accepted_success"] = sum(
            bool(result.get("socks_accepted")) for result in source_results
        )
        item["https_tested"] = len(source_results)
        item["https_success"] = sum(
            bool(result.get("https")) for result in source_results
        )
        item["https_failed"] = len(source_results) - item["https_success"]
        item["transfer_tested"] = sum(
            bool(result.get("https")) for result in source_results
        )
        item["transfer_success"] = sum(
            bool(result.get("transfer")) for result in source_results
        )
        item["median_latency_ms"] = (
            round(statistics.median(latencies)) if latencies else None
        )
        item["verification_status"] = (
            "проверено" if item["https_success"] else "не проверено"
        )
        item["health_errors"] = [
            f"{result['name']}: {result['error']}"
            for result in source_results
            if result.get("error")
        ]
        item["health_results"] = source_results
    stats["health_diagnostics"] = {
        **diagnostics,
        "legacy_controls": legacy_results,
    }


def summary_lines(stats: dict) -> list[str]:
    lines = [
        "### New LAN source HTTPS sample",
        "",
        "| Source | SOCKS accepted | HTTPS | 64 KiB | Status |",
        "|---|---:|---:|---:|---|",
    ]
    for source in builder.SOURCES:
        source_id = source["id"]
        if source_id not in builder.NEW_LAN_SOURCE_IDS:
            continue
        item = stats.get("sources", {}).get(source_id, {})
        lines.append(
            f"| {source['name']} | "
            f"{item.get('socks_accepted_success', 0)}/{item.get('socks_accepted_tested', 0)} | "
            f"{item.get('https_success', 0)}/{item.get('https_tested', 0)} | "
            f"{item.get('transfer_success', 0)}/{item.get('transfer_tested', 0)} | "
            f"{item.get('verification_status', 'не проверено')} |"
        )
    diagnostics = stats.get("health_diagnostics", {})
    lines.extend(["", f"Assessment: {diagnostics.get('assessment', 'не проверено')}"])
    return lines


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(errors="backslashreplace")
    parser = argparse.ArgumentParser()
    parser.add_argument("--mihomo", type=Path, required=True)
    parser.add_argument(
        "--candidates", type=Path, default=builder.LAN_HEALTH_CANDIDATES_FILE
    )
    parser.add_argument("--stats", type=Path, default=builder.LAN_SOURCE_STATS_FILE)
    parser.add_argument("--readme", type=Path, default=builder.README_FILE)
    parser.add_argument(
        "--legacy-baseline", type=Path, default=builder.LAN_GLOBAL_OUTPUT_FILE
    )
    parser.add_argument("--legacy-controls", type=int, default=3)
    parser.add_argument("--max-per-source", type=int, default=3)
    parser.add_argument("--timeout", type=float, default=12.0)
    args = parser.parse_args()

    if not args.mihomo.is_file():
        raise RuntimeError(f"mihomo executable not found: {args.mihomo}")
    stats = json.loads(args.stats.read_text(encoding="utf-8"))
    candidates = json.loads(args.candidates.read_text(encoding="utf-8"))
    results: dict[str, list[dict]] = {}
    for source in builder.SOURCES:
        source_id = source["id"]
        if source_id not in builder.NEW_LAN_SOURCE_IDS:
            continue
        source_candidates = candidates.get(source_id, [])[: max(0, args.max_per_source)]
        results[source_id] = []
        for proxy in source_candidates:
            result = test_proxy(args.mihomo.resolve(), proxy, args.timeout)
            results[source_id].append(result)
            if result["https"]:
                outcome = "HTTPS подтверждён"
            else:
                outcome = f"не проверено: {result['error']}"
            print(f"{source['name']} / {result['name']}: {outcome}")

    legacy_baseline = builder.load_lan_legacy_baseline(args.legacy_baseline)
    legacy_results = [
        test_proxy(args.mihomo.resolve(), proxy, args.timeout)
        for proxy in legacy_baseline[: max(0, args.legacy_controls)]
    ]
    diagnostics = diagnose_environment(args.timeout)
    assess_environment(diagnostics, results, legacy_results)
    update_stats(stats, results, diagnostics, legacy_results)
    builder.write_lan_source_stats(stats, args.stats)
    builder.refresh_readme_lan_source_stats(stats, args.readme)
    lines = summary_lines(stats)
    print("\n".join(lines))
    github_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if github_summary:
        with Path(github_summary).open("a", encoding="utf-8", newline="\n") as summary:
            summary.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)

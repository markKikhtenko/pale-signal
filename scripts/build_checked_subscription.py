#!/usr/bin/env python3
import concurrent.futures
import gzip
import ipaddress
import json
import math
import os
import platform
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

from build_subscription import (
    OUTPUT_FILE,
    ROOT,
    URL_TEST,
    dump_yaml,
    resolve_server_ip,
    split_by_country,
)


CHECKED_OUTPUT_FILE = ROOT / "subscription-global-checked.yaml"
MIHOMO_TOOLS_DIR = ROOT / ".tools" / "mihomo"
MIHOMO_LATEST_RELEASE_API = "https://api.github.com/repos/MetaCubeX/mihomo/releases/latest"
CHECKED_BATCH_SIZE = 2000
CHECKED_CONCURRENCY = 40
CHECKED_PROXY_TIMEOUT_MS = 5000
CHECKED_TOTAL_TIMEOUT_SECONDS = int(os.environ.get("CHECKED_TOTAL_TIMEOUT_SECONDS", "2400"))
MIN_CHECKED_PROXIES = 50
MAX_DROP_RATIO = 0.70


class CheckedAbort(RuntimeError):
    pass


def parse_scalar(value: str):
    value = value.strip()
    if value == "true":
        return True
    if value == "false":
        return False
    if value == "null":
        return None
    if value and value[0] == '"':
        return json.loads(value)
    if value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
        return int(value)
    return value


def line_indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def load_generated_yaml(path: Path):
    lines = [line.rstrip("\n") for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    index = 0

    def parse_block(indent: int):
        nonlocal index
        if index >= len(lines):
            return None
        current = lines[index]
        if line_indent(current) < indent:
            return None
        if current[indent:].startswith("-"):
            return parse_list(indent)
        return parse_dict(indent)

    def parse_list(indent: int) -> list:
        nonlocal index
        values = []
        while index < len(lines):
            line = lines[index]
            if line_indent(line) != indent or not line[indent:].startswith("-"):
                break
            rest = line[indent + 1 :].strip()
            index += 1
            values.append(parse_scalar(rest) if rest else parse_block(indent + 2))
        return values

    def parse_dict(indent: int) -> dict:
        nonlocal index
        values = {}
        while index < len(lines):
            line = lines[index]
            if line_indent(line) != indent or line[indent:].startswith("-"):
                break
            key, separator, rest = line[indent:].partition(":")
            if not separator:
                raise CheckedAbort(f"invalid generated YAML line: {line}")
            index += 1
            values[key] = parse_scalar(rest.strip()) if rest.strip() else parse_block(indent + 2)
        return values

    return parse_block(0)


def load_full_subscription_proxies() -> list[dict]:
    if not OUTPUT_FILE.exists():
        raise CheckedAbort(f"source full subscription does not exist: {OUTPUT_FILE.name}")
    config = load_generated_yaml(OUTPUT_FILE)
    proxies = config.get("proxies") if isinstance(config, dict) else None
    if not isinstance(proxies, list) or not proxies:
        raise CheckedAbort(f"source full subscription has no proxies: {OUTPUT_FILE.name}")
    clean_proxies = [dict(proxy) for proxy in proxies if isinstance(proxy, dict)]
    if not clean_proxies:
        raise CheckedAbort(f"source full subscription has no readable proxies: {OUTPUT_FILE.name}")
    return clean_proxies


def is_local_or_private_server(server: str) -> bool:
    ip = resolve_server_ip(server)
    if not ip:
        return False
    try:
        return not ipaddress.ip_address(ip).is_global
    except ValueError:
        return False


def select_foreign_proxies(proxies: list[dict]) -> tuple[list[dict], dict[str, int]]:
    public_proxies = []
    local_private = 0
    for proxy in proxies:
        server = str(proxy.get("server", ""))
        if server and is_local_or_private_server(server):
            local_private += 1
            continue
        public_proxies.append(dict(proxy))

    ru_proxies, foreign_proxies = split_by_country(public_proxies)
    stats = {
        "source_total": len(proxies),
        "local_private": local_private,
        "ru": len(ru_proxies),
        "foreign": len(foreign_proxies),
        "unknown": sum(1 for proxy in foreign_proxies if proxy.get("_country") == "UNKNOWN"),
    }
    return foreign_proxies, stats


def build_checked_config(proxies: list[dict]) -> dict:
    names = [proxy["name"] for proxy in proxies]
    export_proxies = [{key: value for key, value in proxy.items() if not key.startswith("_")} for proxy in proxies]
    return {
        "mixed-port": 7890,
        "allow-lan": True,
        "mode": "rule",
        "log-level": "info",
        "ipv6": False,
        "proxies": export_proxies,
        "proxy-groups": [
            {
                "name": "AUTO",
                "type": "url-test",
                "proxies": names,
                "url": URL_TEST,
                "interval": 3600,
                "timeout": 5000,
                "tolerance": 150,
                "lazy": True,
                "expected-status": 204,
            },
            {
                "name": "PROXY",
                "type": "select",
                "proxies": ["AUTO"],
            },
        ],
        "rules": ["MATCH,PROXY"],
    }


def validate_checked_config(config: dict) -> None:
    proxies = config.get("proxies")
    groups = config.get("proxy-groups")
    rules = config.get("rules")
    if not isinstance(proxies, list) or not proxies:
        raise CheckedAbort("checked config has no proxies")
    if not isinstance(groups, list) or len(groups) != 2:
        raise CheckedAbort("checked config must contain only AUTO and PROXY groups")
    group_names = [group.get("name") for group in groups]
    if group_names != ["AUTO", "PROXY"]:
        raise CheckedAbort(f"unexpected checked groups: {group_names}")
    if any(group.get("name") == "MANUAL" for group in groups):
        raise CheckedAbort("checked config must not contain MANUAL group")
    if rules != ["MATCH,PROXY"]:
        raise CheckedAbort("checked config rules are invalid")

    proxy_names = {proxy.get("name") for proxy in proxies}
    if len(proxy_names) != len(proxies):
        raise CheckedAbort("checked proxy names are not unique")

    available = proxy_names | set(group_names)
    for group in groups:
        refs = group.get("proxies")
        if not isinstance(refs, list) or not refs:
            raise CheckedAbort(f"checked group {group.get('name')} has no proxies")
        missing = [name for name in refs if name not in available or name == group.get("name")]
        if missing:
            raise CheckedAbort(f"checked group {group.get('name')} references missing proxies: {missing[:5]}")


def existing_checked_count() -> int:
    if not CHECKED_OUTPUT_FILE.exists():
        return 0
    try:
        config = load_generated_yaml(CHECKED_OUTPUT_FILE)
    except Exception:
        return 0
    proxies = config.get("proxies") if isinstance(config, dict) else None
    return len(proxies) if isinstance(proxies, list) else 0


def request_json(url: str, timeout: int = 45):
    request = urllib.request.Request(url, headers={"User-Agent": "pale-signal-checked-builder/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8", errors="replace"))


def download_file(url: str, target: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": "pale-signal-checked-builder/1.0"})
    with urllib.request.urlopen(request, timeout=120) as response:
        target.write_bytes(response.read())


def mihomo_target_name() -> str:
    return "mihomo.exe" if platform.system().lower().startswith("win") else "mihomo"


def mihomo_asset_score(name: str) -> int | None:
    lowered = name.lower()
    if not lowered.startswith("mihomo-") or lowered.endswith((".deb", ".rpm", ".pkg.tar.zst")):
        return None
    if platform.system().lower() == "windows":
        if "windows-amd64" not in lowered or not lowered.endswith(".zip"):
            return None
    else:
        if "linux-amd64" not in lowered or not lowered.endswith((".gz", ".zip")):
            return None
    score = 0
    if "compatible" in lowered:
        score += 10
    if "go120" in lowered:
        score += 20
    return score


def download_mihomo() -> Path:
    MIHOMO_TOOLS_DIR.mkdir(parents=True, exist_ok=True)
    target = MIHOMO_TOOLS_DIR / mihomo_target_name()
    if target.exists():
        return target

    release = request_json(MIHOMO_LATEST_RELEASE_API)
    assets = release.get("assets") if isinstance(release, dict) else None
    if not isinstance(assets, list):
        raise CheckedAbort("mihomo latest release has no assets")

    candidates = []
    for asset in assets:
        if not isinstance(asset, dict):
            continue
        name = str(asset.get("name", ""))
        url = str(asset.get("browser_download_url", ""))
        score = mihomo_asset_score(name)
        if score is not None and url:
            candidates.append((score, name, url))
    if not candidates:
        raise CheckedAbort("no suitable mihomo asset was found")

    _, name, url = sorted(candidates, key=lambda item: item[0])[0]
    archive = MIHOMO_TOOLS_DIR / name
    print(f"mihomo: downloading {name}")
    download_file(url, archive)

    if archive.suffix == ".gz":
        with gzip.open(archive, "rb") as source:
            target.write_bytes(source.read())
    elif archive.suffix == ".zip":
        with zipfile.ZipFile(archive) as zip_file:
            member = next(
                item
                for item in zip_file.namelist()
                if Path(item).name.lower().startswith("mihomo")
            )
            target.write_bytes(zip_file.read(member))
    else:
        raise CheckedAbort(f"unsupported mihomo archive: {archive.name}")

    if not platform.system().lower().startswith("win"):
        target.chmod(0o755)
    return target


def find_mihomo() -> Path:
    env_path = os.environ.get("MIHOMO_BIN")
    if env_path and Path(env_path).exists():
        return Path(env_path)
    path_binary = shutil.which("mihomo")
    if path_binary:
        return Path(path_binary)
    return download_mihomo()


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def write_batch_config(path: Path, proxies: list[dict], api_port: int, mixed_port: int) -> None:
    names = [proxy["name"] for proxy in proxies]
    export_proxies = [{key: value for key, value in proxy.items() if not key.startswith("_")} for proxy in proxies]
    config = {
        "mixed-port": mixed_port,
        "allow-lan": False,
        "mode": "rule",
        "log-level": "warning",
        "ipv6": False,
        "external-controller": f"127.0.0.1:{api_port}",
        "proxies": export_proxies,
        "proxy-groups": [
            {
                "name": "CHECK",
                "type": "select",
                "proxies": names,
            }
        ],
        "rules": ["MATCH,CHECK"],
    }
    path.write_text("\n".join(dump_yaml(config)) + "\n", encoding="utf-8", newline="\n")


def read_log_tail(path: Path, lines: int = 30) -> str:
    if not path.exists():
        return ""
    content = path.read_text(encoding="utf-8", errors="replace").splitlines()
    return "\n".join(content[-lines:])


def start_mihomo(mihomo_bin: Path, config_path: Path, data_dir: Path, log_path: Path) -> tuple[subprocess.Popen, object]:
    log_file = log_path.open("w", encoding="utf-8", errors="replace")
    proc = subprocess.Popen(
        [str(mihomo_bin), "-f", str(config_path), "-d", str(data_dir)],
        stdout=log_file,
        stderr=subprocess.STDOUT,
        cwd=str(ROOT),
    )
    return proc, log_file


def stop_mihomo(proc: subprocess.Popen, log_file) -> None:
    if proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=10)
    log_file.close()


def wait_for_mihomo_api(port: int, proc: subprocess.Popen, log_path: Path) -> None:
    deadline = time.monotonic() + 20
    url = f"http://127.0.0.1:{port}/version"
    while time.monotonic() < deadline:
        if proc.poll() is not None:
            raise CheckedAbort(f"mihomo exited before API became ready:\n{read_log_tail(log_path)}")
        try:
            request_json(url, timeout=2)
            return
        except Exception:
            time.sleep(0.5)
    raise CheckedAbort(f"mihomo API did not become ready:\n{read_log_tail(log_path)}")


def check_proxy(api_port: int, name: str) -> str:
    encoded_name = urllib.parse.quote(name, safe="")
    encoded_url = urllib.parse.quote(URL_TEST, safe="")
    url = (
        f"http://127.0.0.1:{api_port}/proxies/{encoded_name}/delay"
        f"?timeout={CHECKED_PROXY_TIMEOUT_MS}&url={encoded_url}"
    )
    try:
        payload = request_json(url, timeout=(CHECKED_PROXY_TIMEOUT_MS / 1000) + 2)
    except (TimeoutError, socket.timeout):
        return "timeout"
    except urllib.error.URLError as exc:
        reason = getattr(exc, "reason", None)
        return "timeout" if isinstance(reason, TimeoutError) else "error"
    except Exception:
        return "error"
    delay = payload.get("delay") if isinstance(payload, dict) else None
    return "success" if isinstance(delay, int) and delay >= 0 else "error"


def check_batch(
    mihomo_bin: Path,
    batch: list[dict],
    batch_number: int,
    total_batches: int,
    total_deadline: float,
) -> tuple[list[dict], dict[str, int]]:
    api_port = free_port()
    mixed_port = free_port()
    with tempfile.TemporaryDirectory(prefix="pale-signal-mihomo-") as temp_name:
        temp_dir = Path(temp_name)
        config_path = temp_dir / "config.yaml"
        log_path = temp_dir / "mihomo.log"
        write_batch_config(config_path, batch, api_port, mixed_port)
        proc, log_file = start_mihomo(mihomo_bin, config_path, temp_dir, log_path)
        try:
            wait_for_mihomo_api(api_port, proc, log_path)
            print(f"checked: batch {batch_number}/{total_batches}, proxies={len(batch)}")
            statuses: dict[int, str] = {}
            with concurrent.futures.ThreadPoolExecutor(max_workers=CHECKED_CONCURRENCY) as executor:
                future_map = {
                    executor.submit(check_proxy, api_port, proxy["name"]): index
                    for index, proxy in enumerate(batch)
                }
                for future in concurrent.futures.as_completed(future_map):
                    if time.monotonic() > total_deadline:
                        executor.shutdown(wait=False, cancel_futures=True)
                        raise CheckedAbort("total check timeout exceeded")
                    index = future_map[future]
                    try:
                        statuses[index] = future.result()
                    except Exception:
                        statuses[index] = "error"
        finally:
            stop_mihomo(proc, log_file)

    success = [proxy for index, proxy in enumerate(batch) if statuses.get(index) == "success"]
    counters = {
        "checked": len(batch),
        "success": len(success),
        "timeout": sum(1 for status in statuses.values() if status == "timeout"),
        "error": sum(1 for status in statuses.values() if status == "error"),
    }
    return success, counters


def check_foreign_proxies(proxies: list[dict]) -> tuple[list[dict], dict[str, int]]:
    mihomo_bin = find_mihomo()
    total_batches = math.ceil(len(proxies) / CHECKED_BATCH_SIZE)
    deadline = time.monotonic() + CHECKED_TOTAL_TIMEOUT_SECONDS
    successful: list[dict] = []
    counters = {"checked": 0, "success": 0, "timeout": 0, "error": 0, "batches": total_batches}

    for batch_index in range(0, len(proxies), CHECKED_BATCH_SIZE):
        if time.monotonic() > deadline:
            raise CheckedAbort("total check timeout exceeded before all batches completed")
        batch_number = batch_index // CHECKED_BATCH_SIZE + 1
        batch = proxies[batch_index : batch_index + CHECKED_BATCH_SIZE]
        batch_success, batch_counters = check_batch(mihomo_bin, batch, batch_number, total_batches, deadline)
        successful.extend(batch_success)
        for key in ("checked", "success", "timeout", "error"):
            counters[key] += batch_counters[key]
        print(
            "checked: "
            f"batch={batch_number}/{total_batches}, "
            f"success={batch_counters['success']}, "
            f"timeout={batch_counters['timeout']}, "
            f"error={batch_counters['error']}"
        )

    return successful, counters


def should_replace(new_count: int, old_count: int) -> tuple[bool, str]:
    if new_count < MIN_CHECKED_PROXIES:
        return False, f"only {new_count} checked proxies passed, minimum is {MIN_CHECKED_PROXIES}"
    if old_count and new_count < old_count * (1 - MAX_DROP_RATIO):
        return False, f"checked proxy count dropped from {old_count} to {new_count} by more than 70%"
    return True, ""


def write_checked_subscription(proxies: list[dict]) -> int:
    config = build_checked_config(proxies)
    validate_checked_config(config)
    yaml_text = "\n".join(dump_yaml(config)) + "\n"
    if not yaml_text.strip():
        raise CheckedAbort("checked YAML output is empty")

    old_count = existing_checked_count()
    replace, reason = should_replace(len(proxies), old_count)
    if not replace:
        raise CheckedAbort(reason)

    CHECKED_OUTPUT_FILE.write_text(yaml_text, encoding="utf-8", newline="\n")
    print(
        f"checked: wrote {CHECKED_OUTPUT_FILE.name}, "
        f"proxies={len(proxies)}, bytes={len(yaml_text.encode('utf-8'))}, old={old_count}"
    )
    return len(proxies)


def main(argv: list[str]) -> int:
    started = time.monotonic()
    filter_only = "--filter-only" in argv
    try:
        print(f"checked: source full subscription file: {OUTPUT_FILE.name}")
        proxies = load_full_subscription_proxies()
        foreign_proxies, filter_stats = select_foreign_proxies(proxies)
        total_batches = math.ceil(len(foreign_proxies) / CHECKED_BATCH_SIZE) if foreign_proxies else 0
        print(
            "checked: filter stats: "
            f"source={filter_stats['source_total']}, "
            f"local_private={filter_stats['local_private']}, "
            f"ru={filter_stats['ru']}, "
            f"foreign={filter_stats['foreign']}, "
            f"unknown={filter_stats['unknown']}, "
            f"batches={total_batches}"
        )
        if filter_only:
            print("checked: filter-only mode, Mihomo checks were not started")
            return 0
        if not foreign_proxies:
            raise CheckedAbort("no foreign proxies were selected from full subscription")

        checked_proxies, check_stats = check_foreign_proxies(foreign_proxies)
        written_count = write_checked_subscription(checked_proxies)
        elapsed = time.monotonic() - started
        print(
            "checked: complete: "
            f"checked={check_stats['checked']}, "
            f"success={check_stats['success']}, "
            f"timeout={check_stats['timeout']}, "
            f"error={check_stats['error']}, "
            f"written={written_count}, "
            f"elapsed={elapsed:.1f}s"
        )
        return 0
    except CheckedAbort as exc:
        print(f"checked: skipped replacing {CHECKED_OUTPUT_FILE.name}: {exc}", file=sys.stderr)
        return 0
    except Exception as exc:
        print(f"checked: unexpected error, keeping previous {CHECKED_OUTPUT_FILE.name}: {exc}", file=sys.stderr)
        return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

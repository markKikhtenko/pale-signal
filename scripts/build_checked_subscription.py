#!/usr/bin/env python3
import concurrent.futures
import gzip
import hashlib
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
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

from build_subscription import (
    GLOBAL_OUTPUT_FILE,
    OUTPUT_FILE,
    ROOT,
    URL_TEST,
    country_from_name,
    dump_yaml,
    ensure_unique_names,
    geoip_lookup,
    resolve_server_ip,
)


CHECKED_OUTPUT_FILE = ROOT / "subscription-global-checked.yaml"
MIHOMO_TOOLS_DIR = ROOT / ".tools" / "mihomo"
MIHOMO_LATEST_RELEASE_API = "https://api.github.com/repos/MetaCubeX/mihomo/releases/latest"
CHECK_GROUP_NAME = "CHECK"
HEALTHCHECK_FILE = ROOT / "healthcheck.txt"
HEALTHCHECK_URL = os.environ.get(
    "CHECKED_HEALTHCHECK_URL",
    "https://markkikhtenko.github.io/pale-signal/healthcheck.txt",
)
HEALTHCHECK_EXPECTED_BYTES = 64 * 1024
MIN_CHECKED_PROXIES = 50
MAX_DROP_RATIO = 0.70
CHECK_COUNTER_KEYS = (
    "checked",
    "success",
    "timeout",
    "error",
    "first_http_passed",
    "file_download_passed",
    "repeat_passed",
    "xudp_http_passed",
    "xudp_http_failed",
    "high_latency",
)
PRINT_LOCK = threading.Lock()
ENV_ERRORS: list[str] = []


def read_int_env(name: str, default: int, minimum: int = 1) -> int:
    raw = os.environ.get(name)
    if raw is None:
        return default
    try:
        value = int(raw)
    except ValueError:
        ENV_ERRORS.append(f"{name} must be an integer, got {raw!r}")
        return default
    if value < minimum:
        ENV_ERRORS.append(f"{name} must be >= {minimum}, got {value}")
        return default
    return value


def read_float_env(name: str, default: float, minimum: float = 0.0) -> float:
    raw = os.environ.get(name)
    if raw is None:
        return default
    try:
        value = float(raw)
    except ValueError:
        ENV_ERRORS.append(f"{name} must be a number, got {raw!r}")
        return default
    if value < minimum:
        ENV_ERRORS.append(f"{name} must be >= {minimum}, got {value}")
        return default
    return value


CHECKED_BATCH_SIZE = read_int_env("CHECKED_BATCH_SIZE", 2000)
CHECKED_WORKERS = read_int_env("CHECKED_WORKERS", 4)
CHECKED_MAX_DELAY_MS = read_int_env("CHECKED_MAX_DELAY_MS", 1500)
CHECKED_TOTAL_TIMEOUT_SECONDS = read_int_env("CHECKED_TOTAL_TIMEOUT_SECONDS", 16200)
CHECKED_LIMIT = read_int_env("CHECKED_LIMIT", 0, minimum=0)
CHECKED_PILOT_SCAN_LIMIT = read_int_env("CHECKED_PILOT_SCAN_LIMIT", 80)
CHECKED_REPEAT_PAUSE_SECONDS = read_float_env("CHECKED_REPEAT_PAUSE_SECONDS", 0.75)
WORST_CASE_STAGE_TIMEOUT_SECONDS = 5
HEALTHCHECK_PRECHECK_RETRIES = read_int_env("HEALTHCHECK_PRECHECK_RETRIES", 4)
HEALTHCHECK_PRECHECK_RETRY_PAUSE_SECONDS = read_float_env(
    "HEALTHCHECK_PRECHECK_RETRY_PAUSE_SECONDS",
    2.0,
)


class CheckedAbort(RuntimeError):
    pass


def log_line(message: str) -> None:
    with PRINT_LOCK:
        print(message, flush=True)


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


def load_full_subscription_proxies() -> list:
    if not OUTPUT_FILE.exists():
        raise CheckedAbort(f"source full subscription does not exist: {OUTPUT_FILE.name}")
    config = load_generated_yaml(OUTPUT_FILE)
    proxies = config.get("proxies") if isinstance(config, dict) else None
    if not isinstance(proxies, list) or not proxies:
        raise CheckedAbort(f"source full subscription has no proxies: {OUTPUT_FILE.name}")
    return proxies


def proxy_signature(proxy: dict) -> str:
    comparable = {
        key: value
        for key, value in proxy.items()
        if key != "name" and not key.startswith("_")
    }
    return json.dumps(comparable, sort_keys=True, ensure_ascii=False)


def load_curated_global_priority() -> dict[str, int]:
    if not GLOBAL_OUTPUT_FILE.exists():
        return {}
    try:
        config = load_generated_yaml(GLOBAL_OUTPUT_FILE)
    except Exception as exc:
        print(f"warning: could not read {GLOBAL_OUTPUT_FILE.name} for checked priority: {exc}", file=sys.stderr)
        return {}
    proxies = config.get("proxies") if isinstance(config, dict) else None
    if not isinstance(proxies, list):
        return {}

    priority: dict[str, int] = {}
    for index, proxy in enumerate(proxies):
        if isinstance(proxy, dict):
            priority.setdefault(proxy_signature(proxy), index)
    return priority


def prioritize_curated_global(proxies: list[dict]) -> dict[str, int]:
    priority = load_curated_global_priority()
    if not priority:
        return {"curated_priority": 0, "other_priority": len(proxies)}

    fallback_rank = len(priority) + 1
    matched = sum(1 for proxy in proxies if proxy_signature(proxy) in priority)
    proxies.sort(key=lambda proxy: priority.get(proxy_signature(proxy), fallback_rank))
    return {"curated_priority": matched, "other_priority": len(proxies) - matched}


def is_local_or_private_server(server: str) -> bool:
    ip = resolve_server_ip(server)
    if not ip:
        return False
    try:
        return not ipaddress.ip_address(ip).is_global
    except ValueError:
        return False


def select_foreign_proxies(proxies: list) -> tuple[list[dict], dict[str, int]]:
    pending_geo: dict[int, str | None] = {}
    pending_proxies: dict[int, dict] = {}
    ips: set[str] = set()
    ru_proxies: list[dict] = []
    unknown_proxies: list[dict] = []
    foreign_proxies: list[dict] = []
    stats = {
        "source_total": len(proxies),
        "invalid": 0,
        "local_private": 0,
        "ru": 0,
        "unknown_excluded": 0,
        "foreign": 0,
    }

    for index, raw_proxy in enumerate(proxies):
        if not isinstance(raw_proxy, dict):
            stats["invalid"] += 1
            continue
        name = raw_proxy.get("name")
        server = raw_proxy.get("server")
        if not isinstance(name, str) or not name or not isinstance(server, str) or not server:
            stats["invalid"] += 1
            continue

        proxy = dict(raw_proxy)
        if is_local_or_private_server(server):
            stats["local_private"] += 1
            continue

        name_country = country_from_name(name)
        if name_country == "RU":
            proxy["_country"] = "RU"
            ru_proxies.append(proxy)
            stats["ru"] += 1
            continue
        if name_country:
            proxy["_country"] = name_country
            foreign_proxies.append(proxy)
            stats["foreign"] += 1
            continue

        ip = resolve_server_ip(server)
        pending_geo[index] = ip
        pending_proxies[index] = proxy
        if ip:
            ips.add(ip)

    geoip = geoip_lookup(ips)
    for index, ip in pending_geo.items():
        proxy = pending_proxies[index]
        country = geoip.get(ip or "")
        if country == "RU":
            proxy["_country"] = "RU"
            ru_proxies.append(proxy)
            stats["ru"] += 1
        elif country:
            proxy["_country"] = country
            foreign_proxies.append(proxy)
            stats["foreign"] += 1
        else:
            proxy["_country"] = "UNKNOWN"
            if "[UNKNOWN]" not in proxy["name"]:
                proxy["name"] = f"{proxy['name']} [UNKNOWN]"
            unknown_proxies.append(proxy)
            stats["unknown_excluded"] += 1

    ensure_unique_names(ru_proxies + unknown_proxies + foreign_proxies)
    classified_total = (
        stats["invalid"]
        + stats["local_private"]
        + stats["ru"]
        + stats["unknown_excluded"]
        + stats["foreign"]
    )
    stats["classified_total"] = classified_total
    stats["classification_delta"] = classified_total - stats["source_total"]
    if stats["classification_delta"] != 0:
        raise CheckedAbort(
            "checked classification counters do not match source: "
            f"source={stats['source_total']}, "
            f"invalid={stats['invalid']}, "
            f"local_private={stats['local_private']}, "
            f"ru={stats['ru']}, "
            f"unknown_excluded={stats['unknown_excluded']}, "
            f"foreign={stats['foreign']}, "
            f"classified_total={classified_total}, "
            f"classification_delta={stats['classification_delta']}"
        )
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
                "timeout": CHECKED_MAX_DELAY_MS,
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


def existing_checked_names() -> list[str]:
    if not CHECKED_OUTPUT_FILE.exists():
        return []
    try:
        config = load_generated_yaml(CHECKED_OUTPUT_FILE)
    except Exception:
        return []
    proxies = config.get("proxies") if isinstance(config, dict) else None
    if not isinstance(proxies, list):
        return []
    return [str(proxy.get("name", "")) for proxy in proxies if isinstance(proxy, dict) and proxy.get("name")]


def healthcheck_local_stats() -> tuple[int, str]:
    if not HEALTHCHECK_FILE.exists():
        raise CheckedAbort(f"healthcheck file does not exist: {HEALTHCHECK_FILE.name}")
    body = HEALTHCHECK_FILE.read_bytes()
    size = len(body)
    if size != HEALTHCHECK_EXPECTED_BYTES:
        raise CheckedAbort(f"healthcheck file must be exactly 65536 bytes, got {size}: {HEALTHCHECK_FILE.name}")
    return size, hashlib.sha256(body).hexdigest()


def fetch_published_healthcheck() -> tuple[int, bytes]:
    request = urllib.request.Request(
        HEALTHCHECK_URL,
        headers={
            "User-Agent": "pale-signal-checked-builder/1.0",
            "Cache-Control": "no-cache",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        status = int(getattr(response, "status", response.getcode()))
        return status, response.read()


def verify_published_healthcheck(expected_size: int, expected_sha256: str) -> None:
    last_error = ""
    attempts = max(1, HEALTHCHECK_PRECHECK_RETRIES)
    for attempt in range(1, attempts + 1):
        try:
            status, body = fetch_published_healthcheck()
            actual_size = len(body)
            actual_sha256 = hashlib.sha256(body).hexdigest()
            if status != 200:
                last_error = f"expected HTTP 200, got HTTP {status}"
            elif actual_size != expected_size:
                last_error = f"expected {expected_size} bytes, got {actual_size} bytes"
            elif actual_sha256 != expected_sha256:
                last_error = f"expected sha256 {expected_sha256}, got {actual_sha256}"
            else:
                if attempt > 1:
                    print(f"checked: healthcheck precheck passed on retry {attempt}/{attempts}")
                return
        except urllib.error.HTTPError as exc:
            last_error = f"returned HTTP {exc.code}"
        except urllib.error.URLError as exc:
            last_error = f"is not reachable: {exc}"
        except Exception as exc:
            last_error = f"check failed: {exc}"

        if attempt < attempts:
            print(
                "checked: healthcheck precheck retry: "
                f"attempt={attempt}/{attempts}, "
                f"reason={last_error}"
            )
            time.sleep(HEALTHCHECK_PRECHECK_RETRY_PAUSE_SECONDS)
    raise CheckedAbort(f"published healthcheck is not ready: {HEALTHCHECK_URL}: {last_error}")


def empty_check_counters() -> dict[str, int]:
    return {key: 0 for key in CHECK_COUNTER_KEYS}


def merge_check_counters(target: dict[str, int], source: dict[str, int]) -> None:
    for key in CHECK_COUNTER_KEYS:
        target[key] = target.get(key, 0) + source.get(key, 0)


def safe_log_text(value: object) -> str:
    encoding = sys.stdout.encoding or "utf-8"
    return str(value).encode(encoding, errors="replace").decode(encoding, errors="replace")


def validate_worker_count() -> None:
    if ENV_ERRORS:
        raise CheckedAbort("; ".join(ENV_ERRORS))
    if CHECKED_WORKERS < 1:
        raise CheckedAbort(f"CHECKED_WORKERS must be at least 1, got {CHECKED_WORKERS}")
    if CHECKED_TOTAL_TIMEOUT_SECONDS < 1:
        raise CheckedAbort(
            f"CHECKED_TOTAL_TIMEOUT_SECONDS must be >= 1, got {CHECKED_TOTAL_TIMEOUT_SECONDS}"
        )
    if CHECKED_MAX_DELAY_MS > WORST_CASE_STAGE_TIMEOUT_SECONDS * 1000:
        raise CheckedAbort(
            f"CHECKED_MAX_DELAY_MS must be <= {WORST_CASE_STAGE_TIMEOUT_SECONDS * 1000}, "
            f"got {CHECKED_MAX_DELAY_MS}"
        )


def request_json(url: str, timeout: int = 45, method: str = "GET", payload: dict | None = None):
    data = None
    headers = {"User-Agent": "pale-signal-checked-builder/1.0"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read()
        if not body:
            return {}
        return json.loads(body.decode("utf-8", errors="replace"))


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


def allocate_worker_port_pairs(worker_count: int) -> list[tuple[int, int]]:
    needed_ports = worker_count * 2
    ports: list[int] = []
    used: set[int] = set()
    attempts = 0
    max_attempts = max(100, needed_ports * 20)

    while len(ports) < needed_ports:
        attempts += 1
        if attempts > max_attempts:
            raise CheckedAbort(f"could not allocate {needed_ports} unique local ports")
        port = free_port()
        if port in used:
            continue
        used.add(port)
        ports.append(port)

    return [(ports[index], ports[index + 1]) for index in range(0, needed_ports, 2)]


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
                "name": CHECK_GROUP_NAME,
                "type": "select",
                "proxies": names,
            }
        ],
        "rules": [f"MATCH,{CHECK_GROUP_NAME}"],
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


def network_error_status(exc: BaseException) -> str:
    if isinstance(exc, (TimeoutError, socket.timeout)):
        return "timeout"
    reason = getattr(exc, "reason", None)
    if isinstance(reason, (TimeoutError, socket.timeout)):
        return "timeout"
    message = str(exc).lower()
    return "timeout" if "timed out" in message or "timeout" in message else "error"


def is_xudp_proxy(proxy: dict) -> bool:
    return str(proxy.get("packet-encoding", "")).lower() == "xudp"


def select_proxy_for_mixed_port(api_port: int, name: str) -> str:
    encoded_group = urllib.parse.quote(CHECK_GROUP_NAME, safe="")
    url = f"http://127.0.0.1:{api_port}/proxies/{encoded_group}"
    try:
        request_json(url, timeout=3, method="PUT", payload={"name": name})
    except urllib.error.URLError as exc:
        return network_error_status(exc)
    except Exception as exc:
        return network_error_status(exc)
    return "success"


def http_get_via_mihomo(
    mixed_port: int,
    target_url: str,
    expected_status: int,
    expected_size: int | None = None,
    expected_sha256: str | None = None,
) -> str:
    proxy_url = f"http://127.0.0.1:{mixed_port}"
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({"http": proxy_url, "https": proxy_url})
    )
    request = urllib.request.Request(
        target_url,
        headers={
            "User-Agent": "pale-signal-checked-builder/1.0",
            "Cache-Control": "no-cache",
            "Connection": "close",
        },
    )
    started = time.monotonic()
    try:
        with opener.open(request, timeout=(CHECKED_MAX_DELAY_MS / 1000) + 2) as response:
            status = int(getattr(response, "status", response.getcode()))
            body = response.read()
    except urllib.error.HTTPError as exc:
        elapsed_ms = int((time.monotonic() - started) * 1000)
        try:
            exc.read()
        except Exception:
            pass
        return "high_latency" if elapsed_ms > CHECKED_MAX_DELAY_MS else "error"
    except urllib.error.URLError as exc:
        return network_error_status(exc)
    except Exception as exc:
        return network_error_status(exc)

    elapsed_ms = int((time.monotonic() - started) * 1000)
    if elapsed_ms > CHECKED_MAX_DELAY_MS:
        return "high_latency"
    if status != expected_status:
        return "error"
    if expected_size is not None:
        if not body or len(body) != expected_size:
            return "error"
    if expected_sha256 is not None:
        if hashlib.sha256(body).hexdigest() != expected_sha256:
            return "error"
    return "success"


def run_proxy_stages(
    api_port: int,
    mixed_port: int,
    name: str,
    expected_healthcheck_size: int,
    expected_healthcheck_sha256: str,
) -> tuple[str, bool, bool, bool]:
    # A worker checks proxies sequentially, so this selector binding cannot race with another request.
    selector_status = select_proxy_for_mixed_port(api_port, name)
    if selector_status != "success":
        return selector_status, False, False, False
    first_status = http_get_via_mihomo(mixed_port, URL_TEST, 204)
    if first_status != "success":
        return first_status, False, False, False
    file_status = http_get_via_mihomo(
        mixed_port,
        HEALTHCHECK_URL,
        200,
        expected_healthcheck_size,
        expected_healthcheck_sha256,
    )
    if file_status != "success":
        return file_status, True, False, False
    time.sleep(CHECKED_REPEAT_PAUSE_SECONDS)
    repeat_status = http_get_via_mihomo(mixed_port, URL_TEST, 204)
    if repeat_status != "success":
        return repeat_status, True, True, False
    return "success", True, True, True


def check_proxy(
    api_port: int,
    mixed_port: int,
    proxy: dict,
    expected_healthcheck_size: int,
    expected_healthcheck_sha256: str,
) -> tuple[str, dict[str, int]]:
    counters = empty_check_counters()
    name = proxy["name"]
    xudp = is_xudp_proxy(proxy)
    status, first_http_ok, file_ok, repeat_ok = run_proxy_stages(
        api_port,
        mixed_port,
        name,
        expected_healthcheck_size,
        expected_healthcheck_sha256,
    )
    if first_http_ok:
        counters["first_http_passed"] += 1
    if file_ok:
        counters["file_download_passed"] += 1
    if repeat_ok:
        counters["repeat_passed"] += 1
    if xudp:
        counters["xudp_http_passed" if status == "success" else "xudp_http_failed"] += 1
    if status != "success":
        return status, counters
    return "success", counters


def split_worker_items(batch: list[dict], worker_count: int) -> list[list[tuple[int, dict]]]:
    indexed = list(enumerate(batch))
    active_workers = min(max(1, worker_count), len(indexed))
    base_size, remainder = divmod(len(indexed), active_workers)
    chunks = []
    offset = 0
    for worker_index in range(active_workers):
        size = base_size + (1 if worker_index < remainder else 0)
        chunks.append(indexed[offset : offset + size])
        offset += size
    return chunks


def check_worker(
    mihomo_bin: Path,
    worker_number: int,
    worker_total: int,
    batch_number: int,
    api_port: int,
    mixed_port: int,
    worker_items: list[tuple[int, dict]],
    total_deadline: float,
    stop_event: threading.Event,
    expected_healthcheck_size: int,
    expected_healthcheck_sha256: str,
) -> tuple[int, list[tuple[int, dict]], dict[str, int]]:
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix=f"pale-signal-mihomo-worker-{worker_number}-") as temp_name:
        temp_dir = Path(temp_name)
        config_path = temp_dir / "config.yaml"
        log_path = temp_dir / "mihomo.log"
        worker_proxies = [proxy for _index, proxy in worker_items]
        write_batch_config(config_path, worker_proxies, api_port, mixed_port)
        log_line(
            "checked: worker start: "
            f"batch={batch_number}, "
            f"worker={worker_number}/{worker_total}, "
            f"queue={len(worker_items)}, "
            f"api_port={api_port}, "
            f"mixed_port={mixed_port}"
        )
        proc, log_file = start_mihomo(mihomo_bin, config_path, temp_dir, log_path)
        statuses: dict[int, str] = {}
        counters = empty_check_counters()
        counters["checked"] = len(worker_items)
        try:
            wait_for_mihomo_api(api_port, proc, log_path)
            for index, proxy in worker_items:
                if stop_event.is_set():
                    raise CheckedAbort("worker cancelled after another worker failed")
                if time.monotonic() > total_deadline:
                    stop_event.set()
                    raise CheckedAbort("checked build exceeded total timeout")
                try:
                    status, proxy_counters = check_proxy(
                        api_port,
                        mixed_port,
                        proxy,
                        expected_healthcheck_size,
                        expected_healthcheck_sha256,
                    )
                    statuses[index] = status
                    merge_check_counters(counters, proxy_counters)
                except Exception:
                    statuses[index] = "error"
        finally:
            stop_mihomo(proc, log_file)

    success = [(index, proxy) for index, proxy in worker_items if statuses.get(index) == "success"]
    counters["success"] = len(success)
    counters["timeout"] = sum(1 for status in statuses.values() if status == "timeout")
    counters["error"] = sum(1 for status in statuses.values() if status == "error")
    counters["high_latency"] = sum(1 for status in statuses.values() if status == "high_latency")
    elapsed = time.monotonic() - started
    log_line(
        "checked: worker complete: "
        f"batch={batch_number}, "
        f"worker={worker_number}/{worker_total}, "
        f"queue={len(worker_items)}, "
        f"success={counters['success']}, "
        f"timeout={counters['timeout']}, "
        f"error={counters['error']}, "
        f"first_http_passed={counters['first_http_passed']}, "
        f"file_download_passed={counters['file_download_passed']}, "
        f"repeat_passed={counters['repeat_passed']}, "
        f"xudp_http_passed={counters['xudp_http_passed']}, "
        f"xudp_http_failed={counters['xudp_http_failed']}, "
        f"high_latency={counters['high_latency']}, "
        f"elapsed={elapsed:.1f}s"
    )
    return worker_number, success, counters


def check_batch(
    mihomo_bin: Path,
    batch: list[dict],
    batch_number: int,
    total_batches: int,
    total_deadline: float,
    expected_healthcheck_size: int,
    expected_healthcheck_sha256: str,
) -> tuple[list[dict], dict[str, int]]:
    worker_batches = split_worker_items(batch, CHECKED_WORKERS)
    worker_total = len(worker_batches)
    queue_sizes = ", ".join(
        f"{worker_number}:{len(worker_items)}"
        for worker_number, worker_items in enumerate(worker_batches, start=1)
    )
    log_line(
        "checked: batch start: "
        f"batch={batch_number}/{total_batches}, "
        f"proxies={len(batch)}, "
        f"workers={worker_total}, "
        f"queues=[{queue_sizes}]"
    )
    success_items: list[tuple[int, dict]] = []
    counters = empty_check_counters()
    stop_event = threading.Event()
    worker_port_pairs = allocate_worker_port_pairs(worker_total)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=worker_total)
    try:
        futures = [
            executor.submit(
                check_worker,
                mihomo_bin,
                worker_number,
                worker_total,
                batch_number,
                api_port,
                mixed_port,
                worker_items,
                total_deadline,
                stop_event,
                expected_healthcheck_size,
                expected_healthcheck_sha256,
            )
            for worker_number, (worker_items, (api_port, mixed_port)) in enumerate(
                zip(worker_batches, worker_port_pairs),
                start=1,
            )
        ]
        for future in concurrent.futures.as_completed(futures):
            if time.monotonic() > total_deadline:
                stop_event.set()
                executor.shutdown(wait=False, cancel_futures=True)
                raise CheckedAbort("checked build exceeded total timeout")
            try:
                _worker_number, worker_success, worker_counters = future.result()
            except Exception:
                stop_event.set()
                executor.shutdown(wait=True, cancel_futures=True)
                raise
            success_items.extend(worker_success)
            merge_check_counters(counters, worker_counters)
    finally:
        executor.shutdown(wait=True, cancel_futures=True)

    success = [proxy for _index, proxy in sorted(success_items, key=lambda item: item[0])]
    return success, counters


def check_single_proxy_with_mihomo(
    mihomo_bin: Path,
    proxy: dict,
    expected_healthcheck_size: int,
    expected_healthcheck_sha256: str,
) -> tuple[str, dict[str, int]]:
    api_port = free_port()
    mixed_port = free_port()
    with tempfile.TemporaryDirectory(prefix="pale-signal-mihomo-pilot-") as temp_name:
        temp_dir = Path(temp_name)
        config_path = temp_dir / "config.yaml"
        log_path = temp_dir / "mihomo.log"
        write_batch_config(config_path, [proxy], api_port, mixed_port)
        proc, log_file = start_mihomo(mihomo_bin, config_path, temp_dir, log_path)
        try:
            wait_for_mihomo_api(api_port, proc, log_path)
            return check_proxy(
                api_port,
                mixed_port,
                proxy,
                expected_healthcheck_size,
                expected_healthcheck_sha256,
            )
        finally:
            stop_mihomo(proc, log_file)


def pilot_candidates(proxies: list[dict]) -> list[dict]:
    by_name = {str(proxy.get("name")): proxy for proxy in proxies if proxy.get("name")}
    candidates = []
    seen = set()
    for name in existing_checked_names():
        proxy = by_name.get(name)
        if proxy and name not in seen:
            candidates.append(proxy)
            seen.add(name)
        if len(candidates) >= CHECKED_PILOT_SCAN_LIMIT:
            return candidates
    for proxy in proxies:
        name = str(proxy.get("name", ""))
        if name and name not in seen:
            candidates.append(proxy)
            seen.add(name)
        if len(candidates) >= CHECKED_PILOT_SCAN_LIMIT:
            break
    return candidates


def run_pilot_proxy_check(
    mihomo_bin: Path,
    proxies: list[dict],
    total_deadline: float,
    expected_healthcheck_size: int,
    expected_healthcheck_sha256: str,
) -> None:
    candidates = pilot_candidates(proxies)
    if not candidates:
        raise CheckedAbort("pilot proxy check has no candidates")
    print(f"checked: pilot proxy check: candidates={len(candidates)}")
    pilot_success, counters = check_batch(
        mihomo_bin,
        candidates,
        1,
        1,
        total_deadline,
        expected_healthcheck_size,
        expected_healthcheck_sha256,
    )
    if pilot_success:
        print(
            "checked: pilot proxy passed: "
            f"name={safe_log_text(pilot_success[0]['name'])}, "
            f"success={len(pilot_success)}, "
            f"first_http_passed={counters['first_http_passed']}, "
            f"file_download_passed={counters['file_download_passed']}, "
            f"repeat_passed={counters['repeat_passed']}"
        )
        return
    raise CheckedAbort(
        "pilot proxy check failed: "
        f"candidates={len(candidates)}, "
        f"timeout={counters['timeout']}, "
        f"error={counters['error']}, "
        f"high_latency={counters['high_latency']}; "
        "full proxy check was not started"
    )


def check_foreign_proxies(
    mihomo_bin: Path,
    proxies: list[dict],
    deadline: float,
    expected_healthcheck_size: int,
    expected_healthcheck_sha256: str,
) -> tuple[list[dict], dict[str, int]]:
    total_batches = math.ceil(len(proxies) / CHECKED_BATCH_SIZE)
    successful: list[dict] = []
    counters = empty_check_counters()
    counters["batches"] = total_batches

    for batch_index in range(0, len(proxies), CHECKED_BATCH_SIZE):
        if time.monotonic() > deadline:
            raise CheckedAbort("checked build exceeded total timeout")
        batch_number = batch_index // CHECKED_BATCH_SIZE + 1
        batch = proxies[batch_index : batch_index + CHECKED_BATCH_SIZE]
        batch_success, batch_counters = check_batch(
            mihomo_bin,
            batch,
            batch_number,
            total_batches,
            deadline,
            expected_healthcheck_size,
            expected_healthcheck_sha256,
        )
        successful.extend(batch_success)
        merge_check_counters(counters, batch_counters)
        print(
            "checked: "
            f"batch={batch_number}/{total_batches}, "
            f"success={batch_counters['success']}, "
            f"timeout={batch_counters['timeout']}, "
            f"error={batch_counters['error']}, "
            f"first_http_passed={batch_counters['first_http_passed']}, "
            f"file_download_passed={batch_counters['file_download_passed']}, "
            f"repeat_passed={batch_counters['repeat_passed']}, "
            f"xudp_http_passed={batch_counters['xudp_http_passed']}, "
            f"xudp_http_failed={batch_counters['xudp_http_failed']}, "
            f"high_latency={batch_counters['high_latency']}"
        )

    return successful, counters


def estimate_worst_case_seconds(proxy_count: int) -> int:
    per_proxy_seconds = (WORST_CASE_STAGE_TIMEOUT_SECONDS * 3) + CHECKED_REPEAT_PAUSE_SECONDS
    total = 0.0
    for batch_index in range(0, proxy_count, CHECKED_BATCH_SIZE):
        batch_size = min(CHECKED_BATCH_SIZE, proxy_count - batch_index)
        worker_count = min(CHECKED_WORKERS, batch_size) if batch_size else 1
        max_worker_queue = math.ceil(batch_size / worker_count) if worker_count else 0
        total += max_worker_queue * per_proxy_seconds
    return math.ceil(total)


def log_check_plan(foreign_count: int, total_batches: int) -> None:
    print(
        "checked: check plan: "
        f"workers={CHECKED_WORKERS}, "
        f"total_timeout_seconds={CHECKED_TOTAL_TIMEOUT_SECONDS}, "
        f"foreign={foreign_count}, "
        f"batch_size={CHECKED_BATCH_SIZE}, "
        f"batches={total_batches}, "
        f"worst_case_seconds_at_5s={estimate_worst_case_seconds(foreign_count)}"
    )


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
    pilot_only = "--pilot-only" in argv
    try:
        print(f"checked: source full subscription file: {OUTPUT_FILE.name}")
        expected_healthcheck_size, expected_healthcheck_sha256 = healthcheck_local_stats()
        print(
            "checked: healthcheck local: "
            f"bytes={expected_healthcheck_size}, "
            f"sha256={expected_healthcheck_sha256}"
        )
        if not filter_only:
            validate_worker_count()
            verify_published_healthcheck(expected_healthcheck_size, expected_healthcheck_sha256)
            print(
                "checked: healthcheck published: "
                f"url={HEALTHCHECK_URL}, "
                f"http=200, "
                f"bytes={expected_healthcheck_size}, "
                f"sha256={expected_healthcheck_sha256}"
            )
        proxies = load_full_subscription_proxies()
        foreign_proxies, filter_stats = select_foreign_proxies(proxies)
        priority_stats = prioritize_curated_global(foreign_proxies)
        total_batches = math.ceil(len(foreign_proxies) / CHECKED_BATCH_SIZE) if foreign_proxies else 0
        print(
            "checked: filter stats: "
            "source_scope=subscription.yaml proxies after existing deduplication, "
            f"source={filter_stats['source_total']}, "
            f"invalid={filter_stats['invalid']}, "
            f"local_private={filter_stats['local_private']}, "
            f"ru={filter_stats['ru']}, "
            f"unknown_excluded={filter_stats['unknown_excluded']}, "
            f"foreign={filter_stats['foreign']}, "
            f"classified_total={filter_stats['classified_total']}, "
            f"classification_delta={filter_stats['classification_delta']}, "
            f"batches={total_batches}"
        )
        print(
            "checked: priority stats: "
            f"priority_source={GLOBAL_OUTPUT_FILE.name}, "
            f"curated_bypass_first={priority_stats['curated_priority']}, "
            f"other_after={priority_stats['other_priority']}"
        )
        if filter_only:
            print("checked: filter-only mode, Mihomo checks were not started")
            return 0
        if CHECKED_LIMIT > 0:
            original_count = len(foreign_proxies)
            foreign_proxies = foreign_proxies[:CHECKED_LIMIT]
            total_batches = math.ceil(len(foreign_proxies) / CHECKED_BATCH_SIZE) if foreign_proxies else 0
            print(f"checked: local limit enabled: {len(foreign_proxies)}/{original_count} proxies")
        if not foreign_proxies:
            raise CheckedAbort("no foreign proxies were selected from full subscription")

        log_check_plan(len(foreign_proxies), total_batches)
        print(
            "checked: healthcheck: "
            f"url={HEALTHCHECK_URL}, "
            f"bytes={expected_healthcheck_size}, "
            f"sha256={expected_healthcheck_sha256}, "
            f"max_delay_ms={CHECKED_MAX_DELAY_MS}, "
            f"repeat_pause_s={CHECKED_REPEAT_PAUSE_SECONDS:.2f}, "
            f"workers={CHECKED_WORKERS}"
        )
        mihomo_bin = find_mihomo()
        check_started = time.monotonic()
        check_deadline = check_started + CHECKED_TOTAL_TIMEOUT_SECONDS
        run_pilot_proxy_check(
            mihomo_bin,
            foreign_proxies,
            check_deadline,
            expected_healthcheck_size,
            expected_healthcheck_sha256,
        )
        if pilot_only:
            print("checked: pilot-only mode, full proxy check was not started")
            return 0
        checked_proxies, check_stats = check_foreign_proxies(
            mihomo_bin,
            foreign_proxies,
            check_deadline,
            expected_healthcheck_size,
            expected_healthcheck_sha256,
        )
        check_elapsed = time.monotonic() - check_started
        written_count = write_checked_subscription(checked_proxies)
        elapsed = time.monotonic() - started
        print(
            "checked: complete: "
            f"checked={check_stats['checked']}, "
            f"success={check_stats['success']}, "
            f"timeout={check_stats['timeout']}, "
            f"error={check_stats['error']}, "
            f"first_http_passed={check_stats['first_http_passed']}, "
            f"file_download_passed={check_stats['file_download_passed']}, "
            f"repeat_passed={check_stats['repeat_passed']}, "
            f"xudp_http_passed={check_stats['xudp_http_passed']}, "
            f"xudp_http_failed={check_stats['xudp_http_failed']}, "
            f"high_latency={check_stats['high_latency']}, "
            f"written={written_count}, "
            f"check_elapsed={check_elapsed:.1f}s, "
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

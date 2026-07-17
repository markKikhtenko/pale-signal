#!/usr/bin/env python3
import hashlib
import ipaddress
import json
import re
import sys
import urllib.parse
import urllib.request
import uuid
from pathlib import Path


SOURCE_URL = "https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt"
OUTPUT_FILE = Path(__file__).resolve().parents[1] / "subscription.yaml"
URL_TEST = "https://www.gstatic.com/generate_204"

SUPPORTED_NETWORKS = {"tcp", "ws", "grpc", "xhttp"}
TRUE_VALUES = {"1", "true", "yes", "on"}


def fetch_source() -> str:
    request = urllib.request.Request(
        SOURCE_URL,
        headers={"User-Agent": "pale-signal-subscription-builder/1.0"},
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        if response.status != 200:
            raise RuntimeError(f"source returned HTTP {response.status}")
        return response.read().decode("utf-8", errors="replace")


def first_param(params: dict[str, list[str]], *names: str) -> str:
    for name in names:
        values = params.get(name.lower())
        if values:
            return values[-1].strip()
    return ""


def is_truthy(value: str) -> bool:
    return value.strip().lower() in TRUE_VALUES


def clean_name(value: str, fallback: str) -> str:
    value = urllib.parse.unquote(value or "").strip()
    value = re.sub(r"\s+", " ", value)
    value = "".join(ch for ch in value if ch.isprintable())
    return value[:96] or fallback


def parse_query(query: str) -> dict[str, list[str]]:
    params: dict[str, list[str]] = {}
    for key, value in urllib.parse.parse_qsl(query, keep_blank_values=True):
        params.setdefault(key.lower(), []).append(value)
    return params


def normalize_network(raw_network: str) -> str:
    network = (raw_network or "tcp").strip().lower()
    if network in {"raw"}:
        return "tcp"
    if network in {"splithttp", "split-http"}:
        return "xhttp"
    return network


def valid_server(server: str) -> bool:
    try:
        address = ipaddress.ip_address(server)
        return not (address.is_unspecified or address.is_multicast)
    except ValueError:
        return bool(re.fullmatch(r"[A-Za-z0-9.-]+", server)) and "." in server


def parse_vless(line: str) -> dict | None:
    line = line.strip()
    if not line.startswith("vless://"):
        return None

    try:
        parsed = urllib.parse.urlsplit(line)
        if parsed.scheme != "vless":
            return None

        user = urllib.parse.unquote(parsed.username or "")
        parsed_uuid = uuid.UUID(user)
        if parsed_uuid.int == 0:
            return None

        server = parsed.hostname
        port = parsed.port
        if not server or not valid_server(server) or not port or not (1 <= port <= 65535):
            return None

        params = parse_query(parsed.query)
        network = normalize_network(first_param(params, "type", "network"))
        if network not in SUPPORTED_NETWORKS:
            return None

        security = first_param(params, "security", "tls").lower()
        if security in {"", "none"}:
            security = "none"
        if security not in {"none", "tls", "reality"}:
            return None

        proxy: dict = {
            "type": "vless",
            "server": server,
            "port": port,
            "uuid": user,
            "udp": True,
            "encryption": first_param(params, "encryption") or "none",
        }

        flow = first_param(params, "flow")
        if flow:
            proxy["flow"] = flow

        if security in {"tls", "reality"}:
            proxy["tls"] = True
            servername = first_param(params, "sni", "servername", "serverName")
            if servername:
                proxy["servername"] = servername

            fingerprint = first_param(params, "fp", "fingerprint", "client-fingerprint")
            if fingerprint:
                proxy["client-fingerprint"] = fingerprint

            alpn = first_param(params, "alpn")
            if alpn:
                proxy["alpn"] = [item.strip() for item in alpn.split(",") if item.strip()]

            if is_truthy(first_param(params, "allowInsecure", "skip-cert-verify", "insecure")):
                proxy["skip-cert-verify"] = True

        if security == "reality":
            public_key = first_param(params, "pbk", "public-key", "publicKey")
            if not public_key:
                return None
            reality_opts = {"public-key": public_key}
            short_id = first_param(params, "sid", "short-id", "shortId")
            if short_id:
                reality_opts["short-id"] = short_id
            spider_x = first_param(params, "spx", "spider-x", "spiderX")
            if spider_x:
                reality_opts["spider-x"] = spider_x
            proxy["reality-opts"] = reality_opts

        path = first_param(params, "path")
        host = first_param(params, "host", "authority")

        if network != "tcp":
            proxy["network"] = network

        if network == "ws":
            ws_opts: dict = {"path": path or "/"}
            if host:
                ws_opts["headers"] = {"Host": host}
            proxy["ws-opts"] = ws_opts
        elif network == "grpc":
            grpc_opts: dict = {}
            service_name = first_param(params, "serviceName", "service-name", "grpc-service-name")
            if service_name:
                grpc_opts["grpc-service-name"] = service_name
            if grpc_opts:
                proxy["grpc-opts"] = grpc_opts
        elif network == "xhttp":
            xhttp_opts: dict = {"path": path or "/"}
            if host:
                xhttp_opts["host"] = host
            mode = first_param(params, "mode")
            if mode:
                xhttp_opts["mode"] = mode
            proxy["xhttp-opts"] = xhttp_opts

        fallback_name = f"{server}:{port}"
        proxy["_source_name"] = clean_name(parsed.fragment, fallback_name)
        return proxy
    except Exception:
        return None


def dedupe_and_name(proxies: list[dict]) -> list[dict]:
    seen_keys: set[str] = set()
    used_names: dict[str, int] = {}
    result: list[dict] = []

    for proxy in proxies:
        source_name = proxy.pop("_source_name")
        key = json.dumps(proxy, sort_keys=True, ensure_ascii=False)
        digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
        if digest in seen_keys:
            continue
        seen_keys.add(digest)

        count = used_names.get(source_name, 0) + 1
        used_names[source_name] = count
        proxy["name"] = source_name if count == 1 else f"{source_name} {count}"
        result.append({"name": proxy.pop("name"), **proxy})

    return result


def build_config(proxies: list[dict]) -> dict:
    names = [proxy["name"] for proxy in proxies]
    return {
        "mixed-port": 7890,
        "allow-lan": True,
        "mode": "rule",
        "log-level": "info",
        "ipv6": True,
        "proxies": proxies,
        "proxy-groups": [
            {
                "name": "AUTO",
                "type": "url-test",
                "proxies": names,
                "url": URL_TEST,
                "interval": 300,
                "tolerance": 50,
            },
            {
                "name": "FALLBACK",
                "type": "fallback",
                "proxies": names,
                "url": URL_TEST,
                "interval": 300,
            },
            {
                "name": "PROXY",
                "type": "select",
                "proxies": ["AUTO", "FALLBACK", *names],
            },
        ],
        "rules": ["MATCH,PROXY"],
    }


def quote_scalar(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def yaml_scalar(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if value is None:
        return "null"
    return quote_scalar(str(value))


def dump_yaml(value, indent: int = 0) -> list[str]:
    spaces = " " * indent
    lines: list[str] = []

    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(item, (dict, list)):
                lines.append(f"{spaces}{key}:")
                lines.extend(dump_yaml(item, indent + 2))
            else:
                lines.append(f"{spaces}{key}: {yaml_scalar(item)}")
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, dict):
                lines.append(f"{spaces}-")
                lines.extend(dump_yaml(item, indent + 2))
            elif isinstance(item, list):
                lines.append(f"{spaces}-")
                lines.extend(dump_yaml(item, indent + 2))
            else:
                lines.append(f"{spaces}- {yaml_scalar(item)}")
    else:
        lines.append(f"{spaces}{yaml_scalar(value)}")

    return lines


def validate_config(config: dict) -> None:
    proxies = config.get("proxies")
    groups = config.get("proxy-groups")
    rules = config.get("rules")
    if not isinstance(proxies, list) or not proxies:
        raise RuntimeError("no valid proxies were produced")
    if not isinstance(groups, list) or len(groups) != 3:
        raise RuntimeError("proxy groups are missing")
    if rules != ["MATCH,PROXY"]:
        raise RuntimeError("rules are invalid")

    proxy_names = {proxy.get("name") for proxy in proxies}
    if len(proxy_names) != len(proxies):
        raise RuntimeError("proxy names are not unique")

    group_names = {group.get("name") for group in groups}
    available = proxy_names | group_names
    for group in groups:
        refs = group.get("proxies")
        if not isinstance(refs, list) or not refs:
            raise RuntimeError(f"group {group.get('name')} has no proxies")
        missing = [name for name in refs if name not in available or name == group.get("name")]
        if missing:
            raise RuntimeError(f"group {group.get('name')} references missing proxies: {missing}")


def main() -> int:
    source = fetch_source()
    parsed = [proxy for line in source.splitlines() if (proxy := parse_vless(line))]
    proxies = dedupe_and_name(parsed)
    config = build_config(proxies)
    validate_config(config)

    yaml_text = "\n".join(dump_yaml(config)) + "\n"
    if not yaml_text.strip():
        raise RuntimeError("empty YAML output")

    OUTPUT_FILE.write_text(yaml_text, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_FILE} with {len(proxies)} proxies")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)

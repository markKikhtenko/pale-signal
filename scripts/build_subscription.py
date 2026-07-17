#!/usr/bin/env python3
import datetime as dt
import hashlib
import ipaddress
import json
import re
import socket
import sys
import urllib.parse
import urllib.request
import uuid
from pathlib import Path


SOURCES = [
    {
        "id": "FULL",
        "name": "zieng2 vless_universal.txt",
        "url": "https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt",
    },
    {
        "id": "LITE",
        "name": "zieng2 vless_lite.txt",
        "url": "https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt",
    },
    {
        "id": "RADIKAL_LIGHT",
        "name": "0xRadikal light/configs.txt",
        "url": "https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt",
    },
    {
        "id": "KIRYA_26",
        "name": "KiryaScript source/githubmirror/26.txt",
        "url": "https://raw.githubusercontent.com/KiryaScript/white-lists/main/source/githubmirror/26.txt",
    },
    {
        "id": "MAHAN_VLESS",
        "name": "MahanKenway configs/vless.txt",
        "url": "https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt",
    },
    {
        "id": "EPODONIOS_26",
        "name": "Epodonios Sub26.txt",
        "url": "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt",
    },
    {
        "id": "AVEN_26",
        "name": "AvenCores 26_urls.json",
        "url": "https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json",
        "type": "url_list_json",
    },
]
ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = ROOT / "subscription.yaml"
RU_OUTPUT_FILE = ROOT / "subscription-ru.yaml"
GLOBAL_OUTPUT_FILE = ROOT / "subscription-global.yaml"
README_FILE = ROOT / "README.md"
URL_TEST = "https://www.gstatic.com/generate_204"

SUPPORTED_NETWORKS = {"tcp", "ws", "grpc", "xhttp"}
TRUE_VALUES = {"1", "true", "yes", "on"}
GEOIP_BATCH_URL = "http://ip-api.com/batch?fields=status,countryCode,query,message"


def source_urls() -> str:
    return "\n".join(f"- {source['name']}: {source['url']}" for source in SOURCES)


def fetch_source(source: dict[str, str]) -> str:
    request = urllib.request.Request(
        source["url"],
        headers={"User-Agent": "pale-signal-subscription-builder/1.0"},
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        if response.status != 200:
            raise RuntimeError(f"{source['name']} returned HTTP {response.status}")
        return response.read().decode("utf-8", errors="replace")


def fetch_url(url: str, timeout: int = 45) -> str:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "pale-signal-subscription-builder/1.0"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        if response.status != 200:
            raise RuntimeError(f"{url} returned HTTP {response.status}")
        return response.read().decode("utf-8", errors="replace")


def fetch_source_texts(source: dict[str, str]) -> list[str]:
    source_text = fetch_source(source)
    if source.get("type") != "url_list_json":
        return [source_text]

    try:
        urls = json.loads(source_text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"{source['name']} is not valid JSON") from exc

    if not isinstance(urls, list) or not urls:
        raise RuntimeError(f"{source['name']} does not contain a URL list")

    texts = []
    for url in urls:
        if not isinstance(url, str) or not url.startswith(("http://", "https://")):
            continue
        try:
            texts.append(fetch_url(url, timeout=25))
        except Exception as exc:
            print(f"warning: skipped nested source {url}: {exc}", file=sys.stderr)

    if not texts:
        raise RuntimeError(f"{source['name']} did not provide any downloadable nested sources")
    return texts


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


def normalize_fingerprint(value: str) -> str:
    fingerprint = value.strip().lower()
    if fingerprint == "randomized":
        return "random"
    return fingerprint


def normalize_flow(value: str) -> str:
    flow = value.strip()
    if flow == "xtls-rprx-vision-udp443":
        return "xtls-rprx-vision"
    return flow


def valid_server(server: str) -> bool:
    try:
        address = ipaddress.ip_address(server)
        return not (address.is_unspecified or address.is_multicast)
    except ValueError:
        return bool(re.fullmatch(r"[A-Za-z0-9.-]+", server)) and "." in server


def parse_vless(line: str, source_id: str) -> dict | None:
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
            "network": network,
            "udp": True,
            "encryption": first_param(params, "encryption") or "none",
        }

        flow = normalize_flow(first_param(params, "flow"))
        if flow:
            proxy["flow"] = flow

        if security in {"tls", "reality"}:
            proxy["tls"] = True
            servername = first_param(params, "sni", "servername", "serverName")
            if servername:
                proxy["servername"] = servername

            fingerprint = first_param(params, "fp", "fingerprint", "client-fingerprint")
            if fingerprint:
                proxy["client-fingerprint"] = normalize_fingerprint(fingerprint)

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
        proxy["_source_id"] = source_id
        return proxy
    except Exception:
        return None


def dedupe_and_name(proxies: list[dict]) -> list[dict]:
    seen_keys: dict[str, dict] = {}
    used_names: dict[str, int] = {}
    result: list[dict] = []

    for proxy in proxies:
        source_name = proxy.pop("_source_name")
        source_id = proxy.pop("_source_id")
        key = json.dumps(proxy, sort_keys=True, ensure_ascii=False)
        digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
        if digest in seen_keys:
            existing_sources = seen_keys[digest].setdefault("_sources", [])
            if source_id not in existing_sources:
                existing_sources.append(source_id)
            continue

        count = used_names.get(source_name, 0) + 1
        used_names[source_name] = count
        proxy["name"] = source_name if count == 1 else f"{source_name} {count}"
        named_proxy = {"name": proxy.pop("name"), "_sources": [source_id], **proxy}
        seen_keys[digest] = named_proxy
        result.append(named_proxy)

    return result


def flag_to_country_code(flag: str) -> str | None:
    if len(flag) != 2:
        return None
    codepoints = [ord(char) for char in flag]
    if not all(0x1F1E6 <= point <= 0x1F1FF for point in codepoints):
        return None
    return "".join(chr(point - 0x1F1E6 + ord("A")) for point in codepoints)


def country_from_name(name: str) -> str | None:
    lowered = name.casefold()
    for index in range(len(name) - 1):
        code = flag_to_country_code(name[index : index + 2])
        if code:
            return code

    ru_patterns = [
        "russia",
        "russian federation",
        "россия",
        "российская федерация",
        "москва",
        "moscow",
        "санкт-петербург",
        "saint petersburg",
        "st petersburg",
    ]
    if any(pattern in lowered for pattern in ru_patterns):
        return "RU"

    other_country_patterns = [
        "germany", "deutschland", "германия",
        "netherlands", "нидерланды",
        "france", "франция",
        "united kingdom", "great britain", "британия", "англия",
        "united states", "usa", "america", "сша",
        "canada", "канада",
        "finland", "финляндия",
        "sweden", "швеция",
        "poland", "польша",
        "turkey", "турция",
        "iran", "иран",
        "singapore", "сингапур",
        "japan", "япония",
        "hong kong", "гонконг",
        "korea", "корея",
        "china", "китай",
        "kazakhstan", "казахстан",
        "armenia", "армения",
        "georgia", "грузия",
        "estonia", "эстония",
        "latvia", "латвия",
        "lithuania", "литва",
        "ukraine", "украина",
    ]
    if any(pattern in lowered for pattern in other_country_patterns):
        return "OTHER"

    if re.search(r"(^|[^a-zа-я0-9])ru([^a-zа-я0-9]|$)", lowered):
        return "RU"
    return None


def resolve_server_ip(server: str) -> str | None:
    try:
        address = ipaddress.ip_address(server)
        return str(address)
    except ValueError:
        pass

    try:
        addresses = socket.getaddrinfo(server, None, family=socket.AF_INET, type=socket.SOCK_STREAM)
    except OSError:
        return None

    for address in addresses:
        ip = address[4][0]
        try:
            ipaddress.ip_address(ip)
            return ip
        except ValueError:
            continue
    return None


def geoip_lookup(ips: set[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    clean_ips = sorted(ip for ip in ips if ip)
    for index in range(0, len(clean_ips), 100):
        chunk = clean_ips[index : index + 100]
        request = urllib.request.Request(
            GEOIP_BATCH_URL,
            data=json.dumps(chunk).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "User-Agent": "pale-signal-subscription-builder/1.0",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                payload = json.loads(response.read().decode("utf-8", errors="replace"))
        except Exception as exc:
            print(f"warning: skipped GeoIP batch: {exc}", file=sys.stderr)
            continue

        if not isinstance(payload, list):
            continue
        for item in payload:
            if not isinstance(item, dict):
                continue
            query = item.get("query")
            country_code = item.get("countryCode")
            if item.get("status") == "success" and isinstance(query, str) and isinstance(country_code, str):
                result[query] = country_code.upper()
    return result


def ensure_unique_names(proxies: list[dict]) -> None:
    used_names: dict[str, int] = {}
    for proxy in proxies:
        base_name = proxy["name"]
        count = used_names.get(base_name, 0) + 1
        used_names[base_name] = count
        if count > 1:
            proxy["name"] = f"{base_name} {count}"


def split_by_country(proxies: list[dict]) -> tuple[list[dict], list[dict]]:
    pending_geo: dict[int, str | None] = {}
    ips: set[str] = set()

    for index, proxy in enumerate(proxies):
        name_country = country_from_name(proxy["name"])
        if name_country == "RU":
            proxy["_country"] = "RU"
        elif name_country:
            proxy["_country"] = name_country
        else:
            ip = resolve_server_ip(proxy["server"])
            pending_geo[index] = ip
            if ip:
                ips.add(ip)

    geoip = geoip_lookup(ips)
    for index, ip in pending_geo.items():
        proxy = proxies[index]
        country = geoip.get(ip or "")
        if country:
            proxy["_country"] = country
        else:
            proxy["_country"] = "UNKNOWN"
            if "[UNKNOWN]" not in proxy["name"]:
                proxy["name"] = f"{proxy['name']} [UNKNOWN]"

    ensure_unique_names(proxies)
    ru_proxies = [proxy for proxy in proxies if proxy.get("_country") == "RU"]
    global_proxies = [proxy for proxy in proxies if proxy.get("_country") != "RU"]
    return ru_proxies, global_proxies


def build_config(proxies: list[dict]) -> dict:
    names = [proxy["name"] for proxy in proxies]

    return {
        "mixed-port": 7890,
        "allow-lan": True,
        "mode": "rule",
        "log-level": "info",
        "ipv6": False,
        "proxies": [{key: value for key, value in proxy.items() if not key.startswith("_")} for proxy in proxies],
        "proxy-groups": [
            {
                "name": "AUTO",
                "type": "url-test",
                "proxies": names,
                "url": URL_TEST,
                "interval": 900,
                "tolerance": 100,
                "lazy": True,
            },
            {
                "name": "MANUAL",
                "type": "select",
                "proxies": names,
            },
            {
                "name": "PROXY",
                "type": "select",
                "proxies": ["AUTO", "MANUAL"],
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
    group_names_ordered = [group.get("name") for group in groups]
    if group_names_ordered != ["AUTO", "MANUAL", "PROXY"]:
        raise RuntimeError(f"unexpected proxy groups: {group_names_ordered}")
    for required in ("AUTO", "MANUAL", "PROXY"):
        if required not in group_names_ordered:
            raise RuntimeError(f"required group {required} is missing")
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


def proxy_key(proxy: dict) -> str:
    parts = [
        str(proxy.get("type", "")),
        str(proxy.get("server", "")),
        str(proxy.get("port", "")),
        str(proxy.get("uuid", "")),
        str(proxy.get("network", "")),
        str(proxy.get("servername", "")),
        json.dumps(proxy.get("reality-opts", {}), sort_keys=True, ensure_ascii=False),
    ]
    return hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()


def stats_for(proxies: list[dict]) -> dict[str, int]:
    source_stats = {
        source["id"].lower(): sum(1 for proxy in proxies if source["id"] in proxy.get("_sources", []))
        for source in SOURCES
    }
    return {
        "total": len(proxies),
        **source_stats,
        "reality": sum(1 for proxy in proxies if "reality-opts" in proxy),
        "tls": sum(1 for proxy in proxies if proxy.get("tls")),
        "tcp": sum(1 for proxy in proxies if proxy.get("network") == "tcp"),
        "ws": sum(1 for proxy in proxies if proxy.get("network") == "ws"),
        "grpc": sum(1 for proxy in proxies if proxy.get("network") == "grpc"),
        "xhttp": sum(1 for proxy in proxies if proxy.get("network") == "xhttp"),
        "ru": sum(1 for proxy in proxies if proxy.get("_country") == "RU"),
        "global": sum(1 for proxy in proxies if proxy.get("_country") != "RU"),
        "unknown": sum(1 for proxy in proxies if proxy.get("_country") == "UNKNOWN"),
    }


def update_history(proxies: list[dict], now: str) -> dict:
    if HISTORY_FILE.exists():
        try:
            history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            history = {}
    else:
        history = {}

    servers = history.get("servers", {})
    current_keys = set()
    for proxy in proxies:
        key = proxy_key(proxy)
        current_keys.add(key)
        existing = servers.get(key, {})
        servers[key] = {
            "name": proxy["name"],
            "server": proxy["server"],
            "port": proxy["port"],
            "sources": proxy.get("_sources", []),
            "country": proxy.get("_country", "UNKNOWN"),
            "network": proxy.get("network", "tcp"),
            "reality": "reality-opts" in proxy,
            "tls": bool(proxy.get("tls")),
            "first_seen": existing.get("first_seen", now),
            "last_seen": now,
        }

    for key, item in list(servers.items()):
        if key not in current_keys:
            item["active"] = False
        else:
            item["active"] = True

    return {
        "sources": SOURCES,
        "updated_at": now,
        "active_count": len(proxies),
        "servers": servers,
    }


def write_info(proxies: list[dict], yaml_text: str, now: str) -> None:
    stats = stats_for(proxies)
    digest = hashlib.sha256(yaml_text.encode("utf-8")).hexdigest()
    lines = [
        "Pale Signal - подписка для Mihomo/OpenClash",
        f"Обновлено: {now}",
        f"Источник: {SOURCE_URL}",
        f"Серверов: {stats['total']}",
        f"Reality: {stats['reality']}",
        f"TLS: {stats['tls']}",
        f"TCP: {stats['tcp']}",
        f"WebSocket: {stats['ws']}",
        f"gRPC: {stats['grpc']}",
        f"XHTTP: {stats['xhttp']}",
        f"SHA256: {digest}",
        "",
        "Файлы:",
        "- subscription.yaml - основная ссылка для OpenClash",
        "- merged_flclash.yaml - тот же конфиг под именем для FLClash",
        "- subscription_base64.txt - base64-версия YAML",
        "- servers_history.json - история появления серверов",
    ]
    INFO_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def write_project_info(proxies: list[dict], yaml_text: str, now: str) -> None:
    stats = stats_for(proxies)
    digest = hashlib.sha256(yaml_text.encode("utf-8")).hexdigest()
    source_count_lines = [
        f"{source['id']}: {stats[source['id'].lower()]}"
        for source in SOURCES
    ]
    lines = [
        "Pale Signal - подписка для Mihomo/OpenClash",
        f"Обновлено: {now}",
        "Источники:",
        *source_urls().splitlines(),
        f"Серверов всего: {stats['total']}",
        f"RU: {stats['ru']}",
        f"GLOBAL: {stats['global']}",
        f"UNKNOWN: {stats['unknown']}",
        *source_count_lines,
        f"Reality: {stats['reality']}",
        f"TLS: {stats['tls']}",
        f"TCP: {stats['tcp']}",
        f"WebSocket: {stats['ws']}",
        f"gRPC: {stats['grpc']}",
        f"XHTTP: {stats['xhttp']}",
        f"SHA256: {digest}",
        "",
        "Файлы:",
        "- subscription.yaml - основная ссылка для OpenClash",
        "- subscription-ru.yaml - серверы, физически расположенные в России",
        "- subscription-global.yaml - серверы остальных стран и [UNKNOWN]",
        "- merged_flclash.yaml - тот же конфиг под именем для FLClash",
        "- subscription_base64.txt - base64-версия YAML",
        "- servers_history.json - история появления серверов",
    ]
    INFO_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def write_readme(proxies: list[dict], now: str) -> None:
    stats = stats_for(proxies)
    text = f"""# Pale Signal

Автоматически обновляемая VLESS-подписка для Mihomo, OpenClash и FLClash.

## Ссылка для OpenClash

Основная ссылка подписки:

```text
https://markkikhtenko.github.io/pale-signal/subscription.yaml
```

Её можно добавить в OpenClash как обычную подписку Clash/Mihomo.

## Файлы подписки

- `subscription.yaml` - основной конфиг Mihomo/OpenClash.
- `merged_flclash.yaml` - тот же конфиг под именем, привычным для FLClash.
- `subscription_base64.txt` - base64-версия YAML.
- `subscription_info.txt` - краткая информация о последней сборке.
- `servers_history.json` - история first seen / last seen по серверам.

## Что делает сборка

- Раз в час запускается GitHub Actions.
- Также есть ручной запуск: `Actions` -> `Regenerate subscription` -> `Run workflow`.
- Скачивает VLESS-ссылки из источника: `{SOURCE_URL}`.
- Пропускает некорректные строки.
- Удаляет дубли и делает имена серверов уникальными.
- Поддерживает Reality, TLS, TCP, WebSocket, gRPC и XHTTP.
- Создаёт группы `AUTO`, `FALLBACK`, `PROXY`, а также группы по типам, если такие серверы есть.
- Не проверяет серверы через ping и не пытается подключаться к ним.
- Если источник не скачался, серверов нет или YAML сломан, предыдущие рабочие файлы сохраняются.

## Текущая сборка

- Обновлено: `{now}`
- Серверов: `{stats['total']}`
- Reality: `{stats['reality']}`
- TLS: `{stats['tls']}`
- TCP: `{stats['tcp']}`
- WebSocket: `{stats['ws']}`
- gRPC: `{stats['grpc']}`
- XHTTP: `{stats['xhttp']}`
"""
    README_FILE.write_text(text, encoding="utf-8", newline="\n")


def write_project_readme(proxies: list[dict], now: str) -> None:
    stats = stats_for(proxies)
    source_group_rows = "\n".join(
        f"| `{source['id']}` | select | Серверы из `{source['name']}` |"
        for source in SOURCES
    )
    source_status_lines = "\n".join(
        f"- ✅ {source['id']}: `{stats[source['id'].lower()]}`"
        for source in SOURCES
    )
    text = f"""# Pale Signal VLESS Subscription

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated](https://img.shields.io/badge/Updated-Every%20Hour-blue)](https://github.com/markKikhtenko/pale-signal)
[![Servers](https://img.shields.io/badge/Servers-{stats['total']}-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

> Автоматически обновляемая VLESS-подписка для Mihomo, OpenClash и FLClash.
>
> Серверы скачиваются из одного источника каждый час, преобразуются в готовый Clash/Mihomo YAML и публикуются через GitHub Pages.

---

## 📥 Подписка

[![Скачать YAML](https://img.shields.io/badge/Download-YAML-2ea44f?style=for-the-badge)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

```text
https://markkikhtenko.github.io/pale-signal/subscription.yaml
```

Дополнительные ссылки:

```text
https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml
https://markkikhtenko.github.io/pale-signal/subscription-global.yaml
https://markkikhtenko.github.io/pale-signal/merged_flclash.yaml
https://markkikhtenko.github.io/pale-signal/subscription_base64.txt
https://markkikhtenko.github.io/pale-signal/subscription_info.txt
```

---

## 📱 Как установить

### OpenClash

1. Откройте OpenClash в панели роутера.
2. Перейдите в раздел подписок / профилей.
3. Добавьте новую подписку Clash/Mihomo по URL.
4. Вставьте ссылку:

```text
https://markkikhtenko.github.io/pale-signal/subscription.yaml
```

5. Сохраните и обновите подписку.
6. Используйте группу `PROXY`, `AUTO` или нужную группу по типу серверов.

### FLClash / Mihomo-клиенты

1. Откройте раздел `Config`, `Profiles` или `Subscription`.
2. Нажмите `Add`, `URL` или `Remote Config`.
3. Вставьте основную ссылку подписки.
4. Скачайте профиль и включите его.

---

## ✨ Возможности

| Функция | Описание |
|---------|----------|
| 🔄 Автообновление | Каждый час через GitHub Actions |
| 🛠 Ручная перегенерация | `Actions` -> `Regenerate subscription` -> `Run workflow` |
| 🔒 Reality | Поддержка VLESS Reality |
| 🔐 TLS | Поддержка TLS-серверов |
| 🌐 TCP / WS / gRPC / XHTTP | Поддержка основных транспортов Mihomo |
| 🌍 RU / Global | Отдельные подписки для России и остальных стран |
| 🚀 AUTO | URL Test выбирает сервер на стороне клиента |
| 👆 MANUAL | Ручной выбор сервера |
| 🗑 Дедупликация | Повторяющиеся серверы удаляются |
| ✅ Без ping в Actions | Работоспособность проверяет OpenClash/Mihomo |

---

## 📋 Группы серверов

| Группа | Тип | Описание |
|--------|-----|----------|
| `AUTO` | url-test | Автоматический выбор по URL Test |
| `MANUAL` | select | Ручной выбор конкретного сервера |
| `PROXY` | select | Главная группа для правила `MATCH,PROXY` |

---

## 🔄 Как работает обновление

```text
Каждый час:
📥 Скачивается свежий список VLESS-ссылок
🧹 Некорректные строки пропускаются
🔄 Ссылки преобразуются в формат Mihomo/OpenClash
🗑 Удаляются дубликаты
💾 Сохраняется новая подписка
🚀 GitHub Pages публикует готовый YAML
📡 OpenClash забирает обновление по ссылке
```

Если источник не скачался, серверов нет или итоговый YAML сломан, предыдущий рабочий файл остаётся опубликованным.

---

## 📁 Файлы в репозитории

| Файл | Назначение |
|------|------------|
| `subscription.yaml` | Основная подписка для OpenClash/Mihomo |
| `subscription-ru.yaml` | Серверы, физически расположенные в России |
| `subscription-global.yaml` | Серверы остальных стран и `[UNKNOWN]` |
| `merged_flclash.yaml` | Та же подписка под именем для FLClash |
| `subscription_base64.txt` | Base64-версия подписки |
| `subscription_info.txt` | Краткая информация о последней сборке |
| `servers_history.json` | История появления и обновления серверов |
| `scripts/build_subscription.py` | Скрипт сборки подписки |
| `.github/workflows/update-subscription.yml` | Джоба перегенерации и публикации |

---

## 🛠 Источники серверов

```text
{source_urls()}
```

---

## ⚠️ Важно

- Серверы берутся из внешнего публичного списка.
- GitHub Actions не проверяет серверы через ping и не подключается к ним.
- Разделение RU/global не использует SNI, servername, Host, XHTTP host или gRPC service name.
- Для узлов без страны в имени используется GeoIP фактического поля `server`.
- Реальную работоспособность проверяет OpenClash/Mihomo через `AUTO`.
- Для роутера обычно достаточно добавить только `subscription.yaml`.

---

## 💡 Советы

**Если медленно:**

- Используйте группу `AUTO`.
- Подождите несколько минут, пока клиент выполнит URL Test.
- Попробуйте вручную выбрать сервер из `MANUAL`.

**Если не подключается:**

- Обновите подписку в OpenClash.
- Переключитесь с `AUTO` на `MANUAL`.
- Попробуйте отдельные подписки `subscription-ru.yaml` или `subscription-global.yaml`.

**Если серверы пропали:**

- Проверьте статус последнего workflow.
- Дождитесь следующей часовой перегенерации.
- Предыдущая рабочая подписка сохраняется, если новая сборка сломалась.

---

## 📊 Статус

- ✅ Обновлено: `{now}`
- ✅ Серверов: `{stats['total']}`
- ✅ RU: `{stats['ru']}`
- ✅ Global: `{stats['global']}`
- ✅ Unknown: `{stats['unknown']}`
{source_status_lines}
- ✅ Reality: `{stats['reality']}`
- ✅ TLS: `{stats['tls']}`
- ✅ TCP: `{stats['tcp']}`
- ✅ WebSocket: `{stats['ws']}`
- ✅ gRPC: `{stats['grpc']}`
- ✅ XHTTP: `{stats['xhttp']}`
- ✅ Автообновление: работает через GitHub Actions
- ✅ Публикация: GitHub Pages
"""
    README_FILE.write_text(text, encoding="utf-8", newline="\n")


def write_clean_readme(proxies: list[dict], now: str) -> None:
    stats = stats_for(proxies)
    text = f"""# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated hourly](https://img.shields.io/badge/update-every%20hour-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-{stats['total']}-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `{now}`

## Подписки

| Название | Что внутри | Ссылка |
|----------|------------|--------|
| pale-signal подписка — общая | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml |
| pale-signal подписка — Россия | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml |
| pale-signal подписка — Global | Остальные страны и `[UNKNOWN]` | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml |

Прямые ссылки для OpenClash:

```text
https://markkikhtenko.github.io/pale-signal/subscription.yaml
https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml
https://markkikhtenko.github.io/pale-signal/subscription-global.yaml
```

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `{stats['total']}` |
| Россия | `{stats['ru']}` |
| Global | `{stats['global']}` |
| Unknown | `{stats['unknown']}` |
| Reality | `{stats['reality']}` |
| TLS | `{stats['tls']}` |
| TCP | `{stats['tcp']}` |
| WebSocket | `{stats['ws']}` |
| gRPC | `{stats['grpc']}` |
| XHTTP | `{stats['xhttp']}` |

## Группы

Во всех трёх подписках оставлены только:

| Группа | Тип | Назначение |
|--------|-----|------------|
| `AUTO` | `url-test` | Автовыбор серверов через URL Test |
| `MANUAL` | `select` | Ручной выбор сервера |
| `PROXY` | `select` | Главная группа для правила `MATCH,PROXY` |

Параметры `AUTO`: `interval: 900`, `tolerance: 100`, `lazy: true`.

## Разделение по странам

- Сначала используется флаг или страна в имени узла.
- Если страны в имени нет, используется GeoIP фактического поля `server`.
- Если `server` является доменом, он сначала разрешается в IP.
- SNI, `servername`, `Host`, XHTTP host и gRPC service name не используются для определения страны.
- Узлы без определённой страны попадают в `subscription-global.yaml` и получают `[UNKNOWN]` в имени.

## Обновление

GitHub Actions пересобирает подписки раз в час. Ручной запуск: `Actions` -> `Regenerate subscription` -> `Run workflow`.

Если источник не скачался, серверов нет или YAML сломан, предыдущие рабочие файлы не заменяются.
"""
    README_FILE.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    parsed = []
    for source in SOURCES:
        for source_text in fetch_source_texts(source):
            parsed.extend(
                proxy
                for line in source_text.splitlines()
                if (proxy := parse_vless(line, source["id"]))
            )
    proxies = dedupe_and_name(parsed)
    ru_proxies, global_proxies = split_by_country(proxies)
    config = build_config(proxies)
    ru_config = build_config(ru_proxies)
    global_config = build_config(global_proxies)
    validate_config(config)
    validate_config(ru_config)
    validate_config(global_config)

    yaml_text = "\n".join(dump_yaml(config)) + "\n"
    ru_yaml_text = "\n".join(dump_yaml(ru_config)) + "\n"
    global_yaml_text = "\n".join(dump_yaml(global_config)) + "\n"
    if not yaml_text.strip() or not ru_yaml_text.strip() or not global_yaml_text.strip():
        raise RuntimeError("empty YAML output")

    now = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    OUTPUT_FILE.write_text(yaml_text, encoding="utf-8", newline="\n")
    RU_OUTPUT_FILE.write_text(ru_yaml_text, encoding="utf-8", newline="\n")
    GLOBAL_OUTPUT_FILE.write_text(global_yaml_text, encoding="utf-8", newline="\n")
    write_clean_readme(proxies, now)
    print(
        f"wrote subscription files with {len(proxies)} proxies "
        f"({len(ru_proxies)} ru, {len(global_proxies)} global)"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)

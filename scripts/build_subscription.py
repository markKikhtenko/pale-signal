#!/usr/bin/env python3
import base64
import datetime as dt
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
ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = ROOT / "subscription.yaml"
FLCLASH_FILE = ROOT / "merged_flclash.yaml"
BASE64_FILE = ROOT / "subscription_base64.txt"
INFO_FILE = ROOT / "subscription_info.txt"
HISTORY_FILE = ROOT / "servers_history.json"
README_FILE = ROOT / "README.md"
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
            "network": network,
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
    reality_names = [proxy["name"] for proxy in proxies if "reality-opts" in proxy]
    tls_names = [proxy["name"] for proxy in proxies if proxy.get("tls")]
    ws_names = [proxy["name"] for proxy in proxies if proxy.get("network") == "ws"]
    grpc_names = [proxy["name"] for proxy in proxies if proxy.get("network") == "grpc"]
    xhttp_names = [proxy["name"] for proxy in proxies if proxy.get("network") == "xhttp"]

    groups = [
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
    ]

    category_groups = [
        ("REALITY", reality_names),
        ("TLS", tls_names),
        ("WS", ws_names),
        ("GRPC", grpc_names),
        ("XHTTP", xhttp_names),
    ]
    select_groups = [name for name, group_proxies in category_groups if group_proxies]
    groups.append(
        {
            "name": "PROXY",
            "type": "select",
            "proxies": ["AUTO", "FALLBACK", *select_groups, *names],
        }
    )
    groups.extend(
        {"name": group_name, "type": "select", "proxies": group_proxies}
        for group_name, group_proxies in category_groups
        if group_proxies
    )

    return {
        "mixed-port": 7890,
        "allow-lan": True,
        "mode": "rule",
        "log-level": "info",
        "ipv6": True,
        "proxies": proxies,
        "proxy-groups": groups,
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
    if not isinstance(groups, list) or len(groups) < 3:
        raise RuntimeError("proxy groups are missing")
    group_names_ordered = [group.get("name") for group in groups]
    for required in ("AUTO", "FALLBACK", "PROXY"):
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
    return {
        "total": len(proxies),
        "reality": sum(1 for proxy in proxies if "reality-opts" in proxy),
        "tls": sum(1 for proxy in proxies if proxy.get("tls")),
        "tcp": sum(1 for proxy in proxies if proxy.get("network") == "tcp"),
        "ws": sum(1 for proxy in proxies if proxy.get("network") == "ws"),
        "grpc": sum(1 for proxy in proxies if proxy.get("network") == "grpc"),
        "xhttp": sum(1 for proxy in proxies if proxy.get("network") == "xhttp"),
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
        "source": SOURCE_URL,
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
    text = f"""# Pale Signal VLESS Subscription

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated](https://img.shields.io/badge/Updated-Every%20Hour-blue)](https://github.com/markKikhtenko/pale-signal)
[![Servers](https://img.shields.io/badge/Servers-{stats['total']}-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

> Автоматически обновляемая VLESS-подписка для Mihomo, OpenClash и FLClash.
>
> Серверы скачиваются из одного источника каждый час, преобразуются в готовый Clash/Mihomo YAML и публикуются через GitHub Pages.

---

## 📥 Подписка

```text
https://markkikhtenko.github.io/pale-signal/subscription.yaml
```

Дополнительные ссылки:

```text
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
| 🚀 AUTO | URL Test выбирает сервер на стороне клиента |
| 🧯 FALLBACK | Резервное переключение между серверами |
| 🗑 Дедупликация | Повторяющиеся серверы удаляются |
| ✅ Без ping в Actions | Работоспособность проверяет OpenClash/Mihomo |

---

## 📋 Группы серверов

| Группа | Тип | Описание |
|--------|-----|----------|
| `AUTO` | url-test | Автоматический выбор по URL Test |
| `FALLBACK` | fallback | Резервное переключение между серверами |
| `PROXY` | select | Главная группа для правила `MATCH,PROXY` |
| `REALITY` | select | Только Reality-серверы |
| `TLS` | select | Серверы с TLS |
| `WS` | select | WebSocket-серверы |
| `GRPC` | select | gRPC-серверы |
| `XHTTP` | select | XHTTP-серверы |

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
| `merged_flclash.yaml` | Та же подписка под именем для FLClash |
| `subscription_base64.txt` | Base64-версия подписки |
| `subscription_info.txt` | Краткая информация о последней сборке |
| `servers_history.json` | История появления и обновления серверов |
| `scripts/build_subscription.py` | Скрипт сборки подписки |
| `.github/workflows/update-subscription.yml` | Джоба перегенерации и публикации |

---

## 🛠 Источник серверов

1. zieng2 - VLESS lite list

```text
{SOURCE_URL}
```

---

## ⚠️ Важно

- Серверы берутся из внешнего публичного списка.
- GitHub Actions не проверяет серверы через ping и не подключается к ним.
- Реальную работоспособность проверяет OpenClash/Mihomo через `AUTO` и `FALLBACK`.
- Для роутера обычно достаточно добавить только `subscription.yaml`.

---

## 💡 Советы

**Если медленно:**

- Используйте группу `AUTO`.
- Подождите несколько минут, пока клиент выполнит URL Test.
- Попробуйте вручную выбрать сервер из `REALITY`, `TLS`, `WS`, `GRPC` или `XHTTP`.

**Если не подключается:**

- Обновите подписку в OpenClash.
- Переключитесь с `AUTO` на `FALLBACK`.
- Попробуйте выбрать сервер вручную из `PROXY`.

**Если серверы пропали:**

- Проверьте статус последнего workflow.
- Дождитесь следующей часовой перегенерации.
- Предыдущая рабочая подписка сохраняется, если новая сборка сломалась.

---

## 📊 Статус

- ✅ Обновлено: `{now}`
- ✅ Серверов: `{stats['total']}`
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


def main() -> int:
    source = fetch_source()
    parsed = [proxy for line in source.splitlines() if (proxy := parse_vless(line))]
    proxies = dedupe_and_name(parsed)
    config = build_config(proxies)
    validate_config(config)

    yaml_text = "\n".join(dump_yaml(config)) + "\n"
    if not yaml_text.strip():
        raise RuntimeError("empty YAML output")

    now = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    history = update_history(proxies, now)
    OUTPUT_FILE.write_text(yaml_text, encoding="utf-8", newline="\n")
    FLCLASH_FILE.write_text(yaml_text, encoding="utf-8", newline="\n")
    BASE64_FILE.write_text(base64.b64encode(yaml_text.encode("utf-8")).decode("ascii") + "\n", encoding="ascii", newline="\n")
    HISTORY_FILE.write_text(json.dumps(history, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    write_info(proxies, yaml_text, now)
    write_project_readme(proxies, now)
    print(f"wrote subscription files with {len(proxies)} proxies")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)

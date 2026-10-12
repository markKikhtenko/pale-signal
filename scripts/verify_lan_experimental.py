#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

import yaml

import build_subscription as builder


def load_config(path: Path) -> tuple[str, dict]:
    text = path.read_text(encoding="utf-8")
    config = yaml.safe_load(text)
    if not isinstance(config, dict):
        raise RuntimeError(f"{path} does not contain a YAML mapping")
    return text, config


def require_metadata(text: str, proxy_count: int) -> None:
    required = {
        "Version": r"^# Version: \S+$",
        "Created": r"^# Created: .+ МСК$",
        "Updated": r"^# Updated: .+ МСК$",
        "Servers": rf"^# Servers: {proxy_count}$",
    }
    for field, pattern in required.items():
        if re.search(pattern, text, flags=re.MULTILINE) is None:
            raise RuntimeError(f"LAN Experimental metadata field {field} is missing or invalid")
    for source in builder.EXPERIMENTAL_SOURCES:
        if source["url"] not in text:
            raise RuntimeError(f"LAN Experimental metadata is missing source {source['id']}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--experimental", type=Path, default=builder.LAN_EXPERIMENTAL_OUTPUT_FILE)
    parser.add_argument("--lan-global", type=Path, default=builder.LAN_GLOBAL_OUTPUT_FILE)
    args = parser.parse_args()

    experimental_text, experimental = load_config(args.experimental)
    _, lan_global = load_config(args.lan_global)
    lan_global_proxies = lan_global.get("proxies")
    if not isinstance(lan_global_proxies, list) or not lan_global_proxies:
        raise RuntimeError("LAN Global contains no proxies")

    builder.validate_lan_experimental_config(experimental, lan_global_proxies)
    proxies = experimental["proxies"]
    require_metadata(experimental_text, len(proxies))

    if any("[UNKNOWN]" in str(proxy.get("name", "")) for proxy in proxies):
        raise RuntimeError("LAN Experimental contains UNKNOWN nodes")

    group_map = {group["name"]: group for group in experimental["proxy-groups"]}
    print(
        "LAN Experimental verification passed: "
        f"servers={len(proxies)}, AUTO={len(group_map['AUTO']['proxies'])}, "
        f"LAN Global={len(lan_global_proxies)}, intersections=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

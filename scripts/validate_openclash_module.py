#!/usr/bin/env python3
"""Apply the supported OpenClash YAML overwrite operations and validate results.

The implementation mirrors the rules used by OpenClash's current YAML.rb for
normal hash merges, ``rules*`` batch updates and ``rules+`` array appends.  It
keeps the integration test independent from an OpenWrt installation while the
resulting configurations are still parsed by the real Mihomo binary in CI.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path

import yaml

import build_subscription as builder


MATCH_RULE = re.compile(r"^MATCH,.*$")
DIRECT_PROVIDERS = {
    "pale-signal-custom-direct-domain",
    "pale-signal-custom-direct-ip",
}
VP_NBOT_POLICY = "🌐 VPnBot"
VP_NBOT_GROUPS = (
    VP_NBOT_POLICY,
    "🛡 Стабильный",
    "⚡ По задержке",
    "👆 Ручной выбор",
    "🧭 VLESS",
)
MODULE_KEYS = {"rule-providers", "rules*", "rules+", "+rules"}


def parse_key(key: str) -> tuple[str, str]:
    if key.startswith("+"):
        return key[1:], "prepend"
    if key and key[-1] in "+!* -".replace(" ", ""):
        operation = {
            "+": "append",
            "!": "replace",
            "*": "batch",
            "-": "delete",
        }[key[-1]]
        return key[:-1], operation
    return key, "merge"


def matches(target: object, condition: object) -> bool:
    if target is None or condition is None:
        return False
    if isinstance(condition, str) and condition.startswith("/") and condition.endswith("/"):
        return re.search(condition[1:-1], str(target)) is not None
    return target == condition


def batch_update(collection: object, specification: object) -> object:
    if not isinstance(collection, list) or not isinstance(specification, dict):
        return collection
    where = specification.get("where") or {}
    set_values = specification.get("set") or {}
    result: list[object] = []
    for item in collection:
        matched = isinstance(item, str) and all(
            key == "value" and matches(item, value) for key, value in where.items()
        )
        if matched and "value" in set_values:
            replacement = set_values["value"]
            if replacement is not None:
                result.append(copy.deepcopy(replacement))
        else:
            result.append(copy.deepcopy(item))
    return result


def apply_operation(base: object, value: object, operation: str) -> object:
    if operation == "merge":
        if isinstance(base, dict) and isinstance(value, dict):
            return overwrite(base, value)
        return copy.deepcopy(base if value is None else value)
    if operation == "append":
        if isinstance(base, list) and isinstance(value, list):
            result = copy.deepcopy(base)
            for appended in value:
                result = [item for item in result if item != appended]
            return result + copy.deepcopy(value)
        return copy.deepcopy(value)
    if operation == "prepend":
        if isinstance(base, list) and isinstance(value, list):
            result: list[object] = []
            for item in copy.deepcopy(value) + copy.deepcopy(base):
                if item not in result:
                    result.append(item)
            return result
        return copy.deepcopy(value)
    if operation == "batch":
        return batch_update(base, value)
    if operation == "replace":
        return copy.deepcopy(value)
    raise ValueError(f"unsupported overwrite operation: {operation}")


def overwrite(base: dict, override: dict) -> dict:
    result = copy.deepcopy(base) if isinstance(base, dict) else {}
    for raw_key, value in override.items():
        key, operation = parse_key(str(raw_key))
        if operation == "delete":
            if isinstance(result.get(key), list):
                deleted = value if isinstance(value, list) else [value]
                result[key] = [item for item in result[key] if item not in deleted]
            else:
                result.pop(key, None)
            continue
        result[key] = apply_operation(result.get(key), value, operation)
    return result


def load_module_yaml(module_path: Path) -> dict:
    text = module_path.read_text(encoding="utf-8")
    sections = re.split(r"(?m)^\[YAML\]\s*$", text, maxsplit=1)
    if len(sections) != 2:
        raise RuntimeError(f"{module_path}: missing [YAML] section")
    data = yaml.safe_load(sections[1])
    if not isinstance(data, dict):
        raise RuntimeError(f"{module_path}: [YAML] section is not a mapping")
    return data


def validate_general_contract(module_path: Path) -> None:
    text = module_path.read_text(encoding="utf-8")
    matched = re.search(r"(?ms)^\[General\]\s*$\n(.*?)(?=^\[|\Z)", text)
    if not matched:
        raise RuntimeError(f"{module_path}: missing [General] section")
    settings: dict[str, str] = {}
    for raw_line in matched.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            raise RuntimeError(f"{module_path}: invalid General line: {raw_line}")
        key, value = line.split("=", 1)
        settings[key.strip().upper()] = value.strip()

    required = {
        "CORE_TYPE": "Meta",
        "PROXY_MODE": "rule",
    }
    for key, expected in required.items():
        if settings.get(key) != expected:
            raise RuntimeError(f"{module_path}: {key} must be {expected}")
    # DNS must be controlled by OpenClash settings, never by routing module.
    forbidden_dns_overrides = {
        "ENABLE_REDIRECT_DNS",
        "ENABLE_RESPECT_RULES",
        "ENABLE_CUSTOM_DNS",
        "APPEND_DEFAULT_DNS",
        "APPEND_WAN_DNS",
        "CUSTOM_NAME_POLICY",
        "CUSTOM_HOST",
        "CUSTOM_FALLBACK_FILTER",
        "FAKEIP_RANGE",
        "EN_MODE",
    }
    present = sorted(forbidden_dns_overrides & settings.keys())
    if present:
        raise RuntimeError(f"{module_path}: DNS override settings are forbidden: {present}")


def validate_module_contract(
    module: dict,
    expected_policy: str,
    rule_placement: str,
) -> list[str]:
    unexpected_keys = sorted(set(module) - MODULE_KEYS)
    if unexpected_keys:
        raise RuntimeError(
            "routing module must not change connection settings; "
            f"unexpected keys: {unexpected_keys}"
        )

    keys = list(module)
    if "rules*" not in module or "rules+" not in module:
        raise RuntimeError("module must delete catch-all rules and append a final rule")
    if keys.index("rules*") > keys.index("rules+"):
        raise RuntimeError("rules* must run before rules+")

    if rule_placement == "after-existing":
        if "+rules" in module:
            raise RuntimeError("after-existing modules must not prepend rules")
        appended_rules = module["rules+"]
        if (
            not isinstance(appended_rules, list)
            or not appended_rules
            or appended_rules[-1] != "MATCH,DIRECT"
        ):
            raise RuntimeError("module must append MATCH,DIRECT as its final rule")
        module_rules = appended_rules[:-1]
    elif rule_placement == "before-existing":
        if "+rules" not in module:
            raise RuntimeError("before-existing modules must define +rules")
        if keys.index("rules*") > keys.index("+rules") or keys.index("+rules") > keys.index("rules+"):
            raise RuntimeError("rules must be processed as rules*, +rules, rules+")
        module_rules = module["+rules"]
        if not isinstance(module_rules, list) or not module_rules:
            raise RuntimeError("+rules must contain routing rules")
        if module["rules+"] != ["MATCH,DIRECT"]:
            raise RuntimeError("rules+ must contain exactly one final MATCH,DIRECT")
    else:
        raise RuntimeError(f"unsupported rule placement: {rule_placement}")

    if any(MATCH_RULE.match(str(rule)) for rule in module_rules):
        raise RuntimeError("module contains an early MATCH rule")

    providers = module.get("rule-providers")
    if not isinstance(providers, dict) or not providers:
        raise RuntimeError("module has no rule providers")
    rule_indexes: dict[str, int] = {}
    for index, rule in enumerate(module_rules):
        parts = rule.split(",")
        if len(parts) < 3 or parts[0] != "RULE-SET":
            raise RuntimeError(f"unexpected module rule: {rule}")
        provider_name, policy = parts[1], parts[2]
        if provider_name not in providers:
            raise RuntimeError(f"rule references missing provider {provider_name}")
        required_policy = "DIRECT" if provider_name in DIRECT_PROVIDERS else expected_policy
        if policy != required_policy:
            raise RuntimeError(
                f"provider {provider_name} must use {required_policy}, got {policy}"
            )
        rule_indexes[provider_name] = index

    for name, provider in providers.items():
        if provider.get("type") != "http" or provider.get("proxy") != "DIRECT":
            raise RuntimeError(f"provider {name} must update over DIRECT HTTP")
        if not provider.get("url") or not provider.get("path") or not provider.get("interval"):
            raise RuntimeError(f"provider {name} is missing update metadata")
    if len(module_rules) != len(providers) or set(rule_indexes) != set(providers):
        raise RuntimeError("every rule provider must be referenced exactly once")

    priorities = (
        ("pale-signal-custom-direct-domain", "pale-signal-custom-proxy-domain"),
        ("pale-signal-custom-proxy-domain", "pale-signal-refilter-community-domain"),
        ("pale-signal-custom-proxy-domain", "pale-signal-refilter-domain"),
        ("pale-signal-custom-direct-ip", "pale-signal-custom-proxy-ip"),
        ("pale-signal-custom-proxy-ip", "pale-signal-refilter-community-ip"),
        ("pale-signal-custom-proxy-ip", "pale-signal-refilter-discord-ip"),
        ("pale-signal-custom-proxy-ip", "pale-signal-refilter-ip"),
    )
    for higher, lower in priorities:
        if rule_indexes[higher] >= rule_indexes[lower]:
            raise RuntimeError(f"incorrect rule priority: {higher} must precede {lower}")
    return module_rules


def validate_merged(
    base: dict,
    merged: dict,
    module_rules: list[str],
    label: str,
    expected_policy: str,
    rule_placement: str,
) -> None:
    group_names = {
        group.get("name")
        for group in merged.get("proxy-groups", [])
        if isinstance(group, dict)
    }
    if expected_policy not in group_names:
        raise RuntimeError(f"{label}: required {expected_policy} group is missing")

    base_rules = base.get("rules") or []
    merged_rules = merged.get("rules") or []
    specific_rules = [rule for rule in base_rules if not MATCH_RULE.match(str(rule))]
    if rule_placement == "after-existing":
        expected_rules = specific_rules + module_rules + ["MATCH,DIRECT"]
    else:
        expected_rules = module_rules + specific_rules + ["MATCH,DIRECT"]
    if merged_rules != expected_rules:
        raise RuntimeError(f"{label}: merged rule priority is incorrect")
    if merged_rules[-1] != "MATCH,DIRECT":
        raise RuntimeError(f"{label}: MATCH,DIRECT is not the final effective rule")
    if any(MATCH_RULE.match(str(rule)) for rule in merged_rules[:-1]):
        raise RuntimeError(f"{label}: an early MATCH rule is still present")
    if sum(1 for rule in merged_rules if MATCH_RULE.match(str(rule))) != 1:
        raise RuntimeError(f"{label}: expected exactly one MATCH rule")

    for key, value in base.items():
        if key not in {"rules", "rule-providers"} and merged.get(key) != value:
            raise RuntimeError(f"{label}: connection setting {key} was modified")

    base_providers = base.get("rule-providers") or {}
    merged_providers = merged.get("rule-providers") or {}
    for name, provider in base_providers.items():
        if merged_providers.get(name) != provider:
            raise RuntimeError(f"{label}: existing rule provider {name} was modified")


def proxy_fingerprint(proxy: dict) -> str:
    return json.dumps(
        {key: value for key, value in proxy.items() if key != "name"},
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
    )


def dump_compatible_yaml(value: dict) -> str:
    """Match OpenClash's double-quoted serialization of REALITY short IDs."""
    dumped = yaml.safe_dump(value, allow_unicode=True, sort_keys=False)
    fixed_lines: list[str] = []
    short_id_line = re.compile(r"^(\s*short-id:\s*)(.*)$")
    for line in dumped.splitlines():
        matched = short_id_line.match(line)
        if not matched:
            fixed_lines.append(line)
            continue
        scalar = yaml.safe_load(matched.group(2))
        if scalar is None:
            scalar = ""
        if isinstance(scalar, list):
            rendered = json.dumps([str(item) for item in scalar], ensure_ascii=False)
        else:
            rendered = json.dumps(str(scalar), ensure_ascii=False)
        fixed_lines.append(f"{matched.group(1)}{rendered}")
    return "\n".join(fixed_lines) + "\n"


def validate_lan_global(configs: dict[str, dict]) -> tuple[int, int]:
    lan_global = configs.get("subscription-lan-global.yaml")
    lan_5k = configs.get("subscription-lan-5k.yaml")
    if lan_global is None:
        return 0, 0
    proxies = lan_global.get("proxies") or []
    fingerprints = [proxy_fingerprint(proxy) for proxy in proxies]
    duplicate_count = len(fingerprints) - len(set(fingerprints))
    if duplicate_count:
        raise RuntimeError(f"LAN Global contains {duplicate_count} exact duplicate proxies")
    if lan_5k is not None:
        lan_5k_proxies = lan_5k.get("proxies") or []
        expected = proxies[: builder.LAN_5K_SUBSCRIPTION_LIMIT]
        if lan_5k_proxies != expected:
            raise RuntimeError("LAN 5K is not the first 5000 LAN Global proxies")
    return len(proxies), duplicate_count


def validate_lan_global_fast_check(configs: dict[str, dict]) -> int:
    fast_check = configs.get("subscription-lan-global-fast-check.yaml")
    if fast_check is None:
        return 0
    lan_global = configs.get("subscription-lan-global.yaml")
    if lan_global is None:
        raise RuntimeError("LAN Global is required to validate Fast Check")
    proxies = lan_global.get("proxies") or []
    preserved_baseline = proxies[: builder.LAN_PRESERVED_BASELINE_COUNT]
    if (
        builder.lan_legacy_digest(
            preserved_baseline[: builder.LAN_LEGACY_BASELINE_COUNT]
        )
        != builder.LAN_LEGACY_BASELINE_DIGEST
    ):
        raise RuntimeError("LAN Global legacy prefix does not match origin/main")
    if (
        builder.lan_legacy_digest(preserved_baseline)
        != builder.LAN_PRESERVED_BASELINE_DIGEST
    ):
        raise RuntimeError("LAN Global preserved 2159-entry prefix changed")
    builder.validate_lan_global_fast_check_config(
        lan_global, fast_check, preserved_baseline
    )
    return len(fast_check["proxies"])


def make_synthetic_config(profile: str, expected_policy: str) -> tuple[str, dict]:
    common = {
        "mixed-port": 7890,
        "mode": "rule",
        "ipv6": True,
        "dns": {
            "enable": True,
            "enhanced-mode": "fake-ip",
            "fake-ip-range": "198.18.0.1/16",
            "fake-ip-filter": ["+.lan", "+.local"],
            "default-nameserver": ["1.1.1.1"],
            "nameserver": ["https://1.1.1.1/dns-query"],
            "proxy-server-nameserver": ["tls://8.8.8.8"],
        },
        "tun": {
            "enable": False,
            "stack": "mixed",
            "auto-route": False,
        },
    }
    if profile == "vpnbot":
        if expected_policy != VP_NBOT_POLICY:
            raise RuntimeError(
                f"VPnBot synthetic profile requires policy {VP_NBOT_POLICY}"
            )
        node_name = "VPnBot synthetic node"
        common.update(
            {
                "proxies": [
                    {
                        "name": node_name,
                        "type": "ss",
                        "server": "127.0.0.1",
                        "port": 8388,
                        "cipher": "aes-128-gcm",
                        "password": "validation-only",
                        "udp": True,
                    }
                ],
                "proxy-groups": [
                    {
                        "name": VP_NBOT_POLICY,
                        "type": "select",
                        "proxies": list(VP_NBOT_GROUPS[1:]),
                    },
                    *[
                        {"name": name, "type": "select", "proxies": [node_name]}
                        for name in VP_NBOT_GROUPS[1:]
                    ],
                ],
                "rules": [
                    "DOMAIN-SUFFIX,subscription-security.example,REJECT",
                    f"DOMAIN-SUFFIX,subscription-route.example,{VP_NBOT_POLICY}",
                    f"MATCH,{VP_NBOT_POLICY}",
                    "IP-CIDR,203.0.113.0/24,DIRECT,no-resolve",
                ],
            }
        )
        return "synthetic-vpnbot.yaml", common

    common.update(
        {
            "proxy-groups": [
                {"name": expected_policy, "type": "select", "proxies": ["DIRECT"]}
            ],
            "rules": [
                "DOMAIN-SUFFIX,existing-before.example,DIRECT",
                f"MATCH,{expected_policy}",
                "IP-CIDR,203.0.113.0/24,REJECT,no-resolve",
            ],
        }
    )
    return "synthetic-special-rules.yaml", common


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--expected-policy", default="PROXY")
    parser.add_argument(
        "--rule-placement",
        choices=("after-existing", "before-existing"),
        default="after-existing",
    )
    parser.add_argument(
        "--synthetic-profile",
        choices=("generic", "vpnbot"),
        default="generic",
    )
    parser.add_argument("configs", nargs="*", type=Path)
    args = parser.parse_args()

    validate_general_contract(args.module)
    module = load_module_yaml(args.module)
    module_rules = validate_module_contract(
        module,
        args.expected_policy,
        args.rule_placement,
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)

    loaded_configs: dict[str, dict] = {}
    for config_path in args.configs:
        base = yaml.safe_load(config_path.read_text(encoding="utf-8"))
        if not isinstance(base, dict):
            raise RuntimeError(f"{config_path}: root is not a mapping")
        merged = overwrite(base, module)
        validate_merged(
            base,
            merged,
            module_rules,
            config_path.name,
            args.expected_policy,
            args.rule_placement,
        )
        loaded_configs[config_path.name] = base
        output_path = args.output_dir / config_path.name
        output_path.write_text(
            dump_compatible_yaml(merged),
            encoding="utf-8",
            newline="\n",
        )

    synthetic_name, synthetic = make_synthetic_config(
        args.synthetic_profile,
        args.expected_policy,
    )
    synthetic_merged = overwrite(synthetic, module)
    validate_merged(
        synthetic,
        synthetic_merged,
        module_rules,
        synthetic_name,
        args.expected_policy,
        args.rule_placement,
    )
    if args.synthetic_profile == "vpnbot":
        group_names = tuple(group["name"] for group in synthetic_merged["proxy-groups"])
        if group_names != VP_NBOT_GROUPS:
            raise RuntimeError("VPnBot groups changed or additional groups were created")
    (args.output_dir / synthetic_name).write_text(
        dump_compatible_yaml(synthetic_merged),
        encoding="utf-8",
        newline="\n",
    )

    server_count, duplicates = validate_lan_global(loaded_configs)
    fast_check_count = validate_lan_global_fast_check(loaded_configs)
    print(
        f"validated {len(loaded_configs)} merged subscriptions; "
        f"LAN Global servers={server_count}, exact_duplicates={duplicates}; "
        f"Fast Check servers={fast_check_count}, AUTO settings=passed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

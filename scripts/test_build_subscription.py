#!/usr/bin/env python3
import inspect
import json
import tempfile
import unittest
import uuid
from pathlib import Path
from unittest import mock

import yaml

import build_subscription as builder


class LanExperimentalTests(unittest.TestCase):
    def setUp(self) -> None:
        builder.PUBLIC_SERVER_CACHE.clear()

    @staticmethod
    def source(source_id: str) -> dict:
        return {
            "id": source_id,
            "name": source_id,
            "url": f"https://example.test/{source_id}",
            "format": "share_uri",
            "required": True,
            "minimum_vless": 1,
        }

    @staticmethod
    def yaml_source(source_id: str, *, limit: int = 50, required: bool = False) -> dict:
        return {
            "id": source_id,
            "name": source_id,
            "url": f"https://example.test/{source_id}.yaml",
            "format": "clash_yaml",
            "required": required,
            "max_imported": limit,
        }

    @staticmethod
    def vless(
        number: int,
        *,
        server: str = "one.example.com",
        port: int = 443,
        host: str = "cdn.example.com",
        name: str | None = None,
    ) -> str:
        user_id = str(uuid.UUID(int=number))
        return (
            f"vless://{user_id}@{server}:{port}"
            f"?encryption=none&security=tls&type=ws&host={host}&path=%2F"
            f"#{name or f'node-{number}'}"
        )

    @staticmethod
    def mark_non_ru(proxies: list[dict]) -> tuple[list[dict], list[dict]]:
        for proxy in proxies:
            proxy["_country"] = "US"
        return [], proxies

    def build(
        self,
        source_lines: dict[str, list[str] | Exception],
        *,
        lan_global: list[dict] | None = None,
        baseline_stats: dict | None = None,
    ) -> tuple[str, dict, dict]:
        sources = [self.source(source_id) for source_id in source_lines]

        def fetcher(source: dict) -> list[str]:
            value = source_lines[source["id"]]
            if isinstance(value, Exception):
                raise value
            return ["\n".join(value)]

        with (
            mock.patch.object(builder, "is_public_remote_server", return_value=True),
            mock.patch.object(builder, "split_by_country", side_effect=self.mark_non_ru),
        ):
            text, stats = builder.build_lan_experimental(
                lan_global or [],
                sources=sources,
                fetcher=fetcher,
                now="2026-10-12 12:00:00 МСК",
                baseline_stats=baseline_stats,
            )
        return text, stats, yaml.safe_load(text)

    def test_experimental_sources_are_isolated(self) -> None:
        production_ids = (
            builder.BASE_SOURCE_IDS
            | builder.LAN_SOURCE_IDS
            | builder.BYPASS_SOURCE_IDS
            | builder.BS_SAFE_SOURCE_IDS
        )
        self.assertTrue(builder.EXPERIMENTAL_SOURCE_IDS)
        self.assertTrue(builder.EXPERIMENTAL_SOURCE_IDS.isdisjoint(production_ids))

    def test_normalized_identity_ignores_case_display_and_service_fields(self) -> None:
        left = {
            "name": "first",
            "_sources": ["A"],
            "type": "vless",
            "server": "EXAMPLE.COM",
            "port": 443,
            "uuid": "AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEE",
            "network": "tcp",
        }
        right = {
            **left,
            "name": "second",
            "_sources": ["B"],
            "server": "example.com.",
            "uuid": "{aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee}",
        }
        self.assertEqual(builder.canonical_proxy_config(left), builder.canonical_proxy_config(right))
        self.assertEqual(builder.endpoint_identity_key(left), builder.endpoint_identity_key(right))
        self.assertEqual(
            builder.normalized_server_identity("2001:0DB8:0:0:0:0:0:1"),
            builder.normalized_server_identity("2001:db8::1"),
        )

    def test_all_sources_unavailable_does_not_overwrite_last_good_file(self) -> None:
        source = self.source("UNAVAILABLE")

        def unavailable(_source: dict) -> list[str]:
            raise OSError("simulated source outage")

        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "subscription-lan-experimental.yaml"
            output.write_text("last-known-good\n", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "all LAN Experimental sources are unavailable"):
                builder.write_lan_experimental_file(
                    [],
                    path=output,
                    sources=[source],
                    fetcher=unavailable,
                    now="2026-10-12 12:00:00 МСК",
                )
            self.assertEqual(output.read_text(encoding="utf-8"), "last-known-good\n")

    def test_one_unavailable_source_rejects_partial_candidate(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "source validation failed"):
            self.build({"A": [self.vless(1)], "B": OSError("offline")})

    def test_empty_source_rejects_candidate(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "truncated or empty"):
            self.build({"A": []})

    def test_abruptly_truncated_source_rejects_candidate(self) -> None:
        baseline = {"sources": {"A": {"received": 10, "valid_format": 10}}}
        with self.assertRaisesRegex(RuntimeError, "required=5"):
            self.build({"A": [self.vless(number) for number in range(1, 5)]}, baseline_stats=baseline)

    def test_mixed_yaml_imports_only_supported_proxy_entries(self) -> None:
        source = self.yaml_source("MIXED")
        document = {
            "mixed-port": 1234,
            "dns": {"enable": True},
            "proxy-groups": [{"name": "foreign", "type": "select", "proxies": []}],
            "rules": ["MATCH,DIRECT"],
            "proxies": [
                {
                    "name": "vless original",
                    "type": "vless",
                    "server": "one.example.com",
                    "port": 443,
                    "uuid": str(uuid.UUID(int=1)),
                    "network": "ws",
                    "tls": True,
                    "ws-opts": {"path": "/one", "headers": {"Host": "cdn.example.com"}},
                },
                {
                    "name": "ss one",
                    "type": "ss",
                    "server": "one.example.com",
                    "port": 443,
                    "cipher": "aes-128-gcm",
                    "password": "first",
                },
                {
                    "name": "ss two",
                    "type": "ss",
                    "server": "one.example.com",
                    "port": 443,
                    "cipher": "aes-128-gcm",
                    "password": "second",
                },
                {
                    "name": "trojan original",
                    "type": "trojan",
                    "server": "one.example.com",
                    "port": 443,
                    "password": "trojan-secret",
                    "sni": "cdn.example.com",
                },
                {"name": "vmess", "type": "vmess", "server": "one.example.com", "port": 443},
                {"name": "http", "type": "http", "server": "one.example.com", "port": 443},
                {"name": "anytls", "type": "anytls", "server": "one.example.com", "port": 443},
                {
                    "name": "bad vless",
                    "type": "vless",
                    "server": "one.example.com",
                    "port": 443,
                    "uuid": "not-a-uuid",
                },
            ],
        }

        with (
            mock.patch.object(builder, "is_public_remote_server", return_value=True),
            mock.patch.object(builder, "split_by_country", side_effect=self.mark_non_ru),
        ):
            text, stats = builder.build_lan_experimental(
                [],
                sources=[source],
                fetcher=lambda _source: [yaml.safe_dump(document, allow_unicode=True)],
                now="2026-10-27 12:00:00 МСК",
                fallback_proxies_by_source={},
            )

        config = yaml.safe_load(text)
        self.assertEqual(stats["protocols"], {"vless": 1, "ss": 2, "trojan": 1})
        self.assertEqual(stats["unsupported_protocols"], 3)
        self.assertEqual(stats["invalid"], 1)
        self.assertEqual(len(config["proxies"]), 4)
        self.assertNotIn("dns", config)
        self.assertNotIn("foreign", {group["name"] for group in config["proxy-groups"]})
        self.assertTrue(all(proxy["name"].startswith("[MIXED] ") for proxy in config["proxies"]))

    def test_protocol_identity_preserves_different_ss_and_trojan_credentials(self) -> None:
        common = {"server": "one.example.com", "port": 443}
        proxies = [
            {**common, "type": "ss", "cipher": "aes-128-gcm", "password": "one"},
            {**common, "type": "ss", "cipher": "aes-128-gcm", "password": "two"},
            {**common, "type": "trojan", "password": "one"},
            {**common, "type": "trojan", "password": "two"},
        ]
        keys = [builder.experimental_endpoint_identity_key(proxy) for proxy in proxies]
        self.assertEqual(len(keys), len(set(keys)))

    def test_yaml_source_limit_is_deterministic(self) -> None:
        source = self.yaml_source("LIMITED", limit=2)
        proxies = [
            {
                "name": f"node-{number}",
                "type": "ss",
                "server": f"node-{number}.example.com",
                "port": 443,
                "cipher": "aes-128-gcm",
                "password": f"password-{number}",
            }
            for number in range(5)
        ]

        def build(values: list[dict]) -> tuple[set[str], dict]:
            with (
                mock.patch.object(builder, "is_public_remote_server", return_value=True),
                mock.patch.object(builder, "split_by_country", side_effect=self.mark_non_ru),
            ):
                text, stats = builder.build_lan_experimental(
                    [],
                    sources=[source],
                    fetcher=lambda _source: [yaml.safe_dump({"proxies": values})],
                    now="2026-10-27 12:00:00 МСК",
                    fallback_proxies_by_source={},
                )
            config = yaml.safe_load(text)
            return {proxy["password"] for proxy in config["proxies"]}, stats

        forward, forward_stats = build(proxies)
        reverse, reverse_stats = build(list(reversed(proxies)))
        self.assertEqual(forward, reverse)
        self.assertEqual(forward_stats["limited"], 3)
        self.assertEqual(reverse_stats["sources"]["LIMITED"]["added"], 2)

    def test_optional_yaml_outage_uses_last_published_source_pool(self) -> None:
        required = self.source("REQUIRED")
        optional = self.yaml_source("OPTIONAL")
        fallback = {
            "type": "ss",
            "server": "fallback.example.com",
            "port": 443,
            "cipher": "aes-128-gcm",
            "password": "retained",
            "_source_name": "[OPTIONAL] retained node",
            "_source_id": "OPTIONAL",
        }

        def fetcher(source: dict) -> list[str]:
            if source["id"] == "OPTIONAL":
                raise OSError("offline")
            return [self.vless(1)]

        with (
            mock.patch.object(builder, "is_public_remote_server", return_value=True),
            mock.patch.object(builder, "split_by_country", side_effect=self.mark_non_ru),
        ):
            text, stats = builder.build_lan_experimental(
                [],
                sources=[required, optional],
                fetcher=fetcher,
                now="2026-10-27 12:00:00 МСК",
                fallback_proxies_by_source={"OPTIONAL": [fallback]},
            )

        config = yaml.safe_load(text)
        self.assertEqual(stats["sources"]["OPTIONAL"]["status"], "fallback")
        self.assertEqual(stats["fallback_sources"], 1)
        self.assertEqual({proxy["type"] for proxy in config["proxies"]}, {"vless", "ss"})

    def test_legacy_fallback_keeps_priority_over_new_yaml_duplicates(self) -> None:
        required = self.source("REQUIRED")
        optional = self.yaml_source("OPTIONAL")
        legacy = {
            "type": "vless",
            "server": "one.example.com",
            "port": 443,
            "uuid": str(uuid.UUID(int=1)),
            "network": "ws",
            "udp": True,
            "encryption": "none",
            "tls": True,
            "ws-opts": {"path": "/", "headers": {"Host": "cdn.example.com"}},
            "_source_name": "legacy node",
        }
        duplicate = {
            key: value
            for key, value in legacy.items()
            if not key.startswith("_")
        }
        duplicate["name"] = "new duplicate"

        def fetcher(source: dict) -> list[str]:
            if source["id"] == "REQUIRED":
                raise OSError("offline")
            return [yaml.safe_dump({"proxies": [duplicate]})]

        with (
            mock.patch.object(builder, "is_public_remote_server", return_value=True),
            mock.patch.object(builder, "split_by_country", side_effect=self.mark_non_ru),
        ):
            text, stats = builder.build_lan_experimental(
                [],
                sources=[required, optional],
                fetcher=fetcher,
                now="2026-10-27 12:00:00 МСК",
                baseline_stats={"sources": {"REQUIRED": {"added": 1}}},
                fallback_proxies_by_source={"__legacy__": [legacy]},
            )

        config = yaml.safe_load(text)
        self.assertEqual([proxy["name"] for proxy in config["proxies"]], ["legacy node"])
        self.assertEqual(stats["sources"]["OPTIONAL"]["duplicates"], 1)
        self.assertEqual(stats["sources"]["REQUIRED"]["status"], "fallback")

    def test_incompatible_yaml_parameter_is_rejected_and_counted(self) -> None:
        source = self.yaml_source("BAD")
        document = {
            "proxies": [
                {
                    "name": "bad reference",
                    "type": "trojan",
                    "server": "one.example.com",
                    "port": 443,
                    "password": "secret",
                    "dialer-proxy": "foreign-group",
                },
                {
                    "name": "good",
                    "type": "trojan",
                    "server": "two.example.com",
                    "port": 443,
                    "password": "secret",
                },
            ]
        }
        with (
            mock.patch.object(builder, "is_public_remote_server", return_value=True),
            mock.patch.object(builder, "split_by_country", side_effect=self.mark_non_ru),
        ):
            _text, stats = builder.build_lan_experimental(
                [],
                sources=[source],
                fetcher=lambda _source: [yaml.safe_dump(document)],
                now="2026-10-27 12:00:00 МСК",
                fallback_proxies_by_source={},
            )
        self.assertEqual(stats["invalid"], 1)
        self.assertEqual(stats["sources"]["BAD"]["added"], 1)

    def test_exact_config_duplicates_are_removed_and_counted(self) -> None:
        first = self.vless(1, name="first")
        second = self.vless(1, name="second")
        _text, stats, config = self.build({"A": [first, second]})
        self.assertEqual(len(config["proxies"]), 1)
        self.assertEqual(stats["sources"]["A"]["duplicates"], 1)

    def test_same_endpoint_with_different_parameters_is_removed(self) -> None:
        first = self.vless(1, host="one.example.com")
        second = self.vless(1, host="two.example.com")
        _text, stats, config = self.build({"A": [first, second]})
        self.assertEqual(len(config["proxies"]), 1)
        self.assertEqual(stats["duplicates"], 1)

    def test_same_server_with_different_port_or_uuid_is_retained(self) -> None:
        lines = [
            self.vless(1, port=443),
            self.vless(1, port=8443),
            self.vless(2, port=443),
        ]
        _text, stats, config = self.build({"A": lines})
        self.assertEqual(len(config["proxies"]), 3)
        self.assertEqual(stats["duplicates"], 0)

    def test_lan_global_endpoint_overlap_is_removed(self) -> None:
        lan_proxy = {
            "name": "LAN",
            "type": "vless",
            "server": "ONE.EXAMPLE.COM",
            "port": 443,
            "uuid": str(uuid.UUID(int=1)).upper(),
            "network": "tcp",
        }
        _text, stats, config = self.build(
            {"A": [self.vless(1), self.vless(2)]},
            lan_global=[lan_proxy],
        )
        self.assertEqual(len(config["proxies"]), 1)
        self.assertEqual(stats["lan_global_overlap"], 1)

    def test_generated_config_has_no_internal_or_lan_overlap(self) -> None:
        lan_proxy = {
            "name": "LAN",
            "type": "vless",
            "server": "lan.example.com",
            "port": 443,
            "uuid": str(uuid.UUID(int=9)),
            "network": "tcp",
        }
        _text, _stats, config = self.build({"A": [self.vless(1), self.vless(2)]})
        builder.validate_lan_experimental_config(config, [lan_proxy])
        endpoints = [builder.endpoint_identity_key(proxy) for proxy in config["proxies"]]
        self.assertEqual(len(endpoints), len(set(endpoints)))

    def test_every_proxy_is_in_auto_once_and_auto_is_default(self) -> None:
        _text, _stats, config = self.build({"A": [self.vless(1), self.vless(2)]})
        groups = {group["name"]: group for group in config["proxy-groups"]}
        names = [proxy["name"] for proxy in config["proxies"]]
        self.assertEqual(groups["AUTO"]["proxies"], names)
        self.assertEqual(groups["AUTO"]["type"], "url-test")
        self.assertEqual(groups["AUTO"]["interval"], 900)
        self.assertEqual(groups["AUTO"]["tolerance"], 100)
        self.assertIs(groups["AUTO"]["lazy"], True)
        self.assertEqual(groups["PROXY"]["proxies"][0], "AUTO")

    def test_retained_fallback_prunes_new_lan_overlap(self) -> None:
        text, stats, config = self.build({"A": [self.vless(1), self.vless(2)]})
        source = self.source("A")
        with (
            tempfile.TemporaryDirectory() as temp_dir,
            mock.patch.object(builder, "EXPERIMENTAL_SOURCES", [source]),
            mock.patch.object(builder, "EXPERIMENTAL_SOURCE_IDS", {"A"}),
        ):
            root = Path(temp_dir)
            experimental_path = root / "subscription-lan-experimental.yaml"
            lan_global_path = root / "subscription-lan-global.yaml"
            stats_path = root / "lan-experimental-stats.json"
            readme_path = root / "README.md"
            experimental_path.write_text(text, encoding="utf-8")
            lan_global_path.write_text(
                "\n".join(builder.dump_yaml(builder.build_config([config["proxies"][0]]))) + "\n",
                encoding="utf-8",
            )
            builder.write_experimental_stats(stats_path, stats)
            readme_path.write_text(
                "# test\n\n"
                f"| LAN Experimental | `{stats['total']}` |\n"
                f"| LAN Experimental AUTO | `{stats['auto']}` |\n"
                "| Исключено пересечений Experimental с LAN Global | "
                f"`{stats['lan_global_overlap']}` |\n\n"
                f"{builder.experimental_readme_section(stats)}\n",
                encoding="utf-8",
            )

            removed = builder.reconcile_retained_experimental(
                experimental_path=experimental_path,
                lan_global_path=lan_global_path,
                stats_path=stats_path,
                readme_path=readme_path,
                now="2026-10-13 17:00:00 МСК",
            )

            self.assertEqual(removed, 1)
            reconciled, reconciled_stats = builder.validate_experimental_artifacts(
                experimental_path,
                lan_global_path,
                stats_path,
                readme_path,
            )
            self.assertEqual(len(reconciled["proxies"]), 1)
            self.assertEqual(reconciled_stats["total"], 1)
            self.assertEqual(reconciled_stats["auto"], 1)
            self.assertEqual(reconciled_stats["retained_pruned"], 1)
            self.assertEqual(reconciled_stats["lan_global_overlap"], 1)

    def test_production_main_does_not_call_experimental_builder(self) -> None:
        self.assertNotIn("build_lan_experimental(", inspect.getsource(builder.main))

    def test_readme_statistics_match_artifact_stats(self) -> None:
        stats = builder.load_experimental_stats()
        builder.validate_experimental_stats(stats)
        readme = builder.README_FILE.read_text(encoding="utf-8")
        lan_global = builder.load_yaml_mapping(builder.LAN_GLOBAL_OUTPUT_FILE)
        self.assertIn(
            f"| LAN Global Fast Check | `{len(lan_global['proxies'])}` |",
            readme,
        )
        self.assertIn(builder.experimental_readme_section(stats), readme)
        self.assertIn(f"| LAN Experimental | `{stats['total']}` |", readme)
        self.assertIn(f"| LAN Experimental AUTO | `{stats['auto']}` |", readme)
        self.assertIn(
            "| Исключено пересечений Experimental с LAN Global | "
            f"`{stats['lan_global_overlap']}` |",
            readme,
        )


class ProductionNamingTests(unittest.TestCase):
    @staticmethod
    def proxy(number: int, name: str) -> dict:
        return {
            "_source_name": name,
            "_source_id": f"SOURCE_{number}",
            "type": "vless",
            "server": f"node-{number}.example.com",
            "port": 443,
            "uuid": str(uuid.UUID(int=number)),
        }

    def test_numbered_source_names_cannot_collide_with_generated_suffixes(self) -> None:
        proxies = builder.dedupe_and_name(
            [
                self.proxy(1, "node 2"),
                self.proxy(2, "node"),
                self.proxy(3, "node"),
            ]
        )

        names = [proxy["name"] for proxy in proxies]
        self.assertEqual(names, ["node 2", "node", "node 3"])
        self.assertEqual(len(names), len(set(names)))


class LanGlobalFastCheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.proxies = [
            {
                "name": "LAN node 1",
                "type": "vless",
                "server": "one.example.com",
                "port": 443,
                "uuid": str(uuid.UUID(int=1)),
                "_sources": ["LAN_SOURCE"],
            },
            {
                "name": "LAN node 2",
                "type": "vless",
                "server": "two.example.com",
                "port": 8443,
                "uuid": str(uuid.UUID(int=2)),
                "_sources": ["LAN_SOURCE"],
            },
        ]
        self.lan_global, self.fast_check = builder.build_lan_global_configs(self.proxies)
        self.lan_groups = {
            group["name"]: group for group in self.lan_global["proxy-groups"]
        }
        self.fast_groups = {
            group["name"]: group for group in self.fast_check["proxy-groups"]
        }

    def test_lan_source_policy_preserves_legacy_and_isolates_new_pools(self) -> None:
        self.assertEqual(
            builder.LEGACY_LAN_SOURCE_IDS,
            {
                "WIREVEIL_VLESS",
                "WLUNLOCKER_BLACK_ALL",
                "APEX_BLACKLIST_WIFI",
                "FLAT447_BLACK_FULL",
                "IGARECK_BLACK_VLESS",
                "MOONISHE_BLACKLIST",
            },
        )
        self.assertEqual(
            builder.NEW_LAN_SOURCE_IDS,
            {
                "RADIKAL_FAST",
                "V2GO_LIVE_VLESS",
                "PULSECONFIGS_FAST",
                "FREE_XRAY_GCP",
                "MULTI_PROXY_TESTED",
                "PATTERNIHA_FREE_CONFIGS",
                "CAPTCHAQ_WORKING_ALL",
                "NODESRADAR_V2RAY",
                "MRDEVMOHAMED_VLESS",
                "BAARCUDA_TOP100_VLESS",
                "MAHAN_VLESS",
                "EPODONIOS_VLESS",
                "BARRY_FAR_VLESS",
                "SOLISPIRIT_VLESS",
                "LIMILCO_VLESS",
                "V2RAYROOT_VLESS",
            },
        )
        self.assertEqual(
            set(builder.NEW_LAN_SOURCE_PRIORITY), builder.NEW_LAN_SOURCE_IDS
        )
        self.assertEqual(
            len(builder.NEW_LAN_SOURCE_PRIORITY), len(builder.NEW_LAN_SOURCE_IDS)
        )
        self.assertEqual(
            builder.LAN_SOURCE_IDS,
            builder.LEGACY_LAN_SOURCE_IDS | builder.NEW_LAN_SOURCE_IDS,
        )
        self.assertTrue(builder.LAN_SOURCE_IDS.isdisjoint(builder.BYPASS_SOURCE_IDS))
        self.assertTrue(builder.LAN_SOURCE_IDS.isdisjoint(builder.MOBILE_SOURCE_IDS))
        lan_sources = [
            source for source in builder.SOURCES if source["id"] in builder.LAN_SOURCE_IDS
        ]
        self.assertEqual(len(lan_sources), len(builder.LAN_SOURCE_IDS))
        self.assertTrue(
            all(source.get("scope", "base") in {"base", "lan_only"} for source in lan_sources)
        )
        expected_legacy_urls = {
            "WIREVEIL_VLESS": "https://raw.githubusercontent.com/markKikhtenko/WireVeil/main/vless.txt",
            "WLUNLOCKER_BLACK_ALL": "https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/blacklist_all.txt",
            "APEX_BLACKLIST_WIFI": "https://raw.githubusercontent.com/Diversan313/apex-parser/main/subs/main/alive_plain_bl.txt",
            "FLAT447_BLACK_FULL": "https://raw.githubusercontent.com/FLAT447/v2ray-lists/main/BLACK_FULL.txt",
            "IGARECK_BLACK_VLESS": "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS.txt",
            "MOONISHE_BLACKLIST": "https://raw.githubusercontent.com/Moonishe/vpnparser/main/output/subscription-blacklist.txt",
        }
        self.assertEqual(
            {
                source["id"]: source["url"]
                for source in lan_sources
                if source["id"] in builder.LEGACY_LAN_SOURCE_IDS
            },
            expected_legacy_urls,
        )
        expected_urls = {
            "RADIKAL_FAST": "https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/fast/configs.txt",
            "V2GO_LIVE_VLESS": "https://raw.githubusercontent.com/Danialsamadi/v2go/main/Splitted-By-Protocol/vless.txt",
            "PULSECONFIGS_FAST": "https://raw.githubusercontent.com/drmikecrypto/PulseConfigs/main/fast/configs.txt",
            "FREE_XRAY_GCP": "https://raw.githubusercontent.com/noahclanman/free-xray-gcp/main/output/protocols/vless.txt",
            "MULTI_PROXY_TESTED": "https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/main/configs/proxy_configs_tested.txt",
            "PATTERNIHA_FREE_CONFIGS": "https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt",
            "CAPTCHAQ_WORKING_ALL": "https://raw.githubusercontent.com/CaptchaQ/vless-servers/main/working_all.txt",
            "NODESRADAR_V2RAY": "https://radarhub.top/v2ray.txt",
            "MRDEVMOHAMED_VLESS": "https://raw.githubusercontent.com/mrdevmohamed/v2ray-configs/main/Splitted-By-Protocol/vless.txt",
            "BAARCUDA_TOP100_VLESS": "https://raw.githubusercontent.com/Baarcuda/vpn-configs/master/top100-vless.txt",
            "MAHAN_VLESS": "https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt",
            "EPODONIOS_VLESS": "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt",
            "BARRY_FAR_VLESS": "https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt",
            "SOLISPIRIT_VLESS": "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt",
            "LIMILCO_VLESS": "https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt",
            "V2RAYROOT_VLESS": "https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt",
        }
        self.assertEqual(
            {
                source["id"]: source["url"]
                for source in lan_sources
                if source["id"] in builder.NEW_LAN_SOURCE_IDS
            },
            expected_urls,
        )

    def test_lan_selection_rejects_whitelist_only_sources(self) -> None:
        wired = {**self.proxies[0], "_sources": ["WIREVEIL_VLESS"], "_country": "US"}
        whitelist = {**self.proxies[1], "_sources": ["BYEWL2"], "_country": "US"}

        self.assertEqual(builder.select_lan_global_proxies([whitelist, wired]), [wired])

    def test_lan_pool_keeps_lan_name_when_same_config_appears_in_whitelist(self) -> None:
        link = (
            f"vless://{uuid.UUID(int=42)}@one.example.com:443"
            "?encryption=none&security=tls&type=tcp#LAN%20node"
        )
        whitelist = builder.parse_vless(link.replace("LAN%20node", "WhiteList%20node"), "BYEWL2")
        wired = builder.parse_vless(link, "WIREVEIL_VLESS")

        selected = builder.dedupe_source_pool([whitelist, wired], builder.LAN_SOURCE_IDS)

        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]["name"], "LAN node")
        self.assertEqual(selected[0]["_sources"], ["WIREVEIL_VLESS"])

    def test_new_endpoint_duplicate_is_rejected_without_changing_legacy(self) -> None:
        user_id = uuid.UUID(int=42)
        legacy = builder.parse_vless(
            f"vless://{user_id}@one.example.com:443?encryption=none&security=tls"
            "&type=ws&host=legacy.example.com#Legacy%20name",
            "WIREVEIL_VLESS",
        )
        added = builder.parse_vless(
            f"vless://{str(user_id).upper()}@ONE.EXAMPLE.COM:443?encryption=none&security=tls"
            "&type=ws&host=new.example.com#New%20name",
            "RADIKAL_FAST",
        )

        legacy_baseline = builder.dedupe_source_pool(
            [legacy], builder.LEGACY_LAN_SOURCE_IDS
        )
        legacy_before = json.loads(json.dumps(legacy_baseline))
        selected, duplicates = builder.dedupe_new_lan_candidates(
            [added], legacy_baseline
        )

        self.assertEqual(selected, [])
        self.assertEqual(legacy_baseline, legacy_before)
        self.assertEqual(duplicates["RADIKAL_FAST"], 1)

    def test_empty_new_pool_keeps_all_2159_preserved_entries(self) -> None:
        preserved = builder.load_lan_preserved_baseline()
        before = json.loads(json.dumps(preserved))

        selected, duplicates = builder.dedupe_new_lan_candidates([], preserved)
        result = preserved + selected

        self.assertEqual(selected, [])
        self.assertEqual(sum(duplicates.values()), 0)
        self.assertEqual(preserved, before)
        self.assertEqual(len(result), builder.LAN_PRESERVED_BASELINE_COUNT)
        self.assertEqual(
            builder.lan_legacy_digest(result), builder.LAN_PRESERVED_BASELINE_DIGEST
        )

    def test_experimental_overlap_is_removed_without_changing_experimental(self) -> None:
        experimental_proxy = {
            "name": "Experimental",
            "type": "vless",
            "server": "203.0.113.20",
            "port": 443,
            "uuid": str(uuid.UUID(int=20)),
            "network": "tcp",
        }
        added = {
            **experimental_proxy,
            "name": "Added",
            "_sources": ["RADIKAL_FAST"],
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "experimental.yaml"
            path.write_text(
                "\n".join(builder.dump_yaml(builder.build_config([experimental_proxy]))) + "\n",
                encoding="utf-8",
            )
            retained, overlaps = builder.exclude_lan_experimental_overlaps(
                [added], path
            )

        self.assertEqual(retained, [])
        self.assertEqual(overlaps["RADIKAL_FAST"], 1)

    def test_public_filter_rejects_non_public_ip(self) -> None:
        public = {**self.proxies[0], "server": "8.8.8.8", "_sources": ["RADIKAL_FAST"]}
        private = {**self.proxies[1], "server": "10.0.0.1", "_sources": ["RADIKAL_FAST"]}

        retained, filtered = builder.filter_public_lan_proxies([private, public])

        self.assertEqual(retained, [public])
        self.assertEqual(filtered["RADIKAL_FAST"], 1)

    def test_unavailable_new_source_does_not_remove_legacy_pool(self) -> None:
        legacy = {
            **self.proxies[0],
            "_sources": ["WIREVEIL_VLESS"],
            "_country": "US",
        }
        stats = builder.build_lan_source_stats(
            {
                "RADIKAL_FAST": {
                    "available": False,
                    "error": "offline",
                    "received_vless": 0,
                    "valid": 0,
                }
            },
            [legacy],
            [legacy],
            {},
            {},
            {},
            "2026-10-26 12:00:00 МСК",
            1,
        )

        self.assertEqual(stats["lan_global_after"], 1)
        self.assertEqual(stats["legacy_preserved"], 1)
        self.assertEqual(stats["new_added"], 0)
        self.assertEqual(stats["sources"]["RADIKAL_FAST"]["status"], "unavailable")

    def test_lan_source_stats_match_published_artifact_and_readme(self) -> None:
        stats = json.loads(builder.LAN_SOURCE_STATS_FILE.read_text(encoding="utf-8"))
        lan = yaml.safe_load(builder.LAN_GLOBAL_OUTPUT_FILE.read_text(encoding="utf-8"))
        endpoints = [builder.endpoint_identity_key(proxy) for proxy in lan["proxies"]]
        readme = builder.README_FILE.read_text(encoding="utf-8")

        self.assertEqual(stats["lan_global_after"], len(lan["proxies"]))
        self.assertEqual(stats["unique_endpoints_after"], len(set(endpoints)))
        self.assertEqual(
            set(stats["legacy_source_ids_preserved"]), builder.LEGACY_LAN_SOURCE_IDS
        )
        legacy_baseline = builder.load_lan_legacy_baseline()
        baseline = builder.load_lan_preserved_baseline()
        self.assertEqual(stats["legacy_preserved"], builder.LAN_LEGACY_BASELINE_COUNT)
        self.assertEqual(
            stats["previous_additions_preserved"],
            builder.LAN_PRESERVED_BASELINE_COUNT - builder.LAN_LEGACY_BASELINE_COUNT,
        )
        self.assertEqual(stats["preserved_total"], builder.LAN_PRESERVED_BASELINE_COUNT)
        self.assertEqual(stats["legacy_baseline_digest"], builder.LAN_LEGACY_BASELINE_DIGEST)
        self.assertEqual(
            stats["preserved_baseline_digest"], builder.LAN_PRESERVED_BASELINE_DIGEST
        )
        self.assertEqual(baseline[: len(legacy_baseline)], legacy_baseline)
        self.assertEqual(lan["proxies"][: len(baseline)], baseline)
        self.assertEqual(stats["new_added"], len(lan["proxies"]) - len(baseline))
        self.assertEqual(set(stats["sources"]), builder.NEW_LAN_SOURCE_IDS)
        self.assertIn(builder.lan_source_stats_readme_section(stats), readme)

    def test_new_names_are_changed_only_when_they_collide_with_legacy(self) -> None:
        legacy = [{"name": "same"}, {"name": "same 2"}]
        new = [{"name": "same"}, {"name": "unique"}]

        builder.ensure_new_names_unique_against_legacy(new, legacy)

        self.assertEqual(legacy, [{"name": "same"}, {"name": "same 2"}])
        self.assertEqual(new, [{"name": "same 3"}, {"name": "unique"}])

    def test_proxy_composition_order_and_parameters_are_identical(self) -> None:
        self.assertEqual(self.fast_check["proxies"], self.lan_global["proxies"])
        self.assertEqual(
            [proxy["name"] for proxy in self.fast_check["proxies"]],
            ["LAN node 1", "LAN node 2"],
        )
        builder.validate_lan_global_fast_check_config(self.lan_global, self.fast_check)

    def test_every_fast_check_proxy_is_in_auto_exactly_once(self) -> None:
        proxy_names = [proxy["name"] for proxy in self.fast_check["proxies"]]
        auto_names = self.fast_groups["AUTO"]["proxies"]
        self.assertEqual(auto_names, proxy_names)
        self.assertEqual(len(auto_names), len(set(auto_names)))

    def test_fast_check_auto_contract(self) -> None:
        auto = self.fast_groups["AUTO"]
        self.assertEqual(auto["type"], "url-test")
        self.assertEqual(auto["url"], "https://cp.cloudflare.com/generate_204")
        self.assertEqual(auto["interval"], 600)
        self.assertEqual(auto["tolerance"], 50)
        self.assertEqual(auto["timeout"], 3000)
        self.assertEqual(auto["max-failed-times"], 3)
        self.assertIs(auto["lazy"], True)

    def test_proxy_defaults_to_auto_then_manual(self) -> None:
        self.assertEqual(self.fast_groups["PROXY"]["proxies"], ["AUTO", "MANUAL"])
        self.assertEqual(
            self.fast_groups["MANUAL"]["proxies"],
            [proxy["name"] for proxy in self.fast_check["proxies"]],
        )

    def test_existing_lan_global_keeps_original_auto_settings(self) -> None:
        auto = self.lan_groups["AUTO"]
        self.assertEqual(auto["type"], "url-test")
        self.assertEqual(auto["interval"], 900)
        self.assertEqual(auto["tolerance"], 100)
        self.assertIs(auto["lazy"], True)
        self.assertNotIn("timeout", auto)
        self.assertNotIn("max-failed-times", auto)

    def test_fast_check_does_not_limit_proxy_count(self) -> None:
        proxies = [
            {
                "name": f"LAN node {number}",
                "type": "vless",
                "server": f"node-{number}.example.com",
                "port": 443,
            }
            for number in range(5001)
        ]
        _lan_global, fast_check = builder.build_lan_global_configs(proxies)
        auto = next(
            group for group in fast_check["proxy-groups"] if group["name"] == "AUTO"
        )
        self.assertEqual(len(fast_check["proxies"]), 5001)
        self.assertEqual(len(auto["proxies"]), 5001)

    def test_validator_rejects_changes_outside_fast_check_auto_settings(self) -> None:
        changed = {**self.fast_check, "ipv6": True}
        with self.assertRaisesRegex(RuntimeError, "outside the allowed AUTO settings"):
            builder.validate_lan_global_fast_check_config(self.lan_global, changed)

    def test_validator_rejects_duplicate_normalized_endpoint(self) -> None:
        duplicate = {
            **self.proxies[0],
            "name": "duplicate",
            "server": "ONE.EXAMPLE.COM.",
            "uuid": str(uuid.UUID(self.proxies[0]["uuid"])).upper(),
            "tls": True,
        }
        lan, fast = builder.build_lan_global_configs([self.proxies[0], duplicate])

        with self.assertRaisesRegex(RuntimeError, r"server \+ port \+ UUID"):
            builder.validate_lan_global_fast_check_config(lan, fast)

    def test_validator_allows_preexisting_duplicates_only_inside_legacy_prefix(self) -> None:
        duplicate = {
            **self.proxies[0],
            "name": "legacy duplicate",
            "server": "ONE.EXAMPLE.COM.",
            "uuid": str(uuid.UUID(self.proxies[0]["uuid"])).upper(),
            "tls": True,
        }
        legacy = [
            {key: value for key, value in proxy.items() if not key.startswith("_")}
            for proxy in [self.proxies[0], duplicate]
        ]
        lan, fast = builder.build_lan_global_configs(legacy + [self.proxies[1]])

        builder.validate_lan_global_fast_check_config(lan, fast, legacy)

    def test_default_build_config_and_custom_auto_list_are_unchanged(self) -> None:
        config = builder.build_config(self.proxies, [self.proxies[1]])
        self.assertEqual(
            config,
            {
                "mixed-port": 7890,
                "allow-lan": True,
                "mode": "rule",
                "log-level": "info",
                "ipv6": False,
                "proxies": [
                    {key: value for key, value in proxy.items() if not key.startswith("_")}
                    for proxy in self.proxies
                ],
                "proxy-groups": [
                    {
                        "name": "AUTO",
                        "type": "url-test",
                        "proxies": ["LAN node 2"],
                        "url": "https://cp.cloudflare.com/generate_204",
                        "interval": 900,
                        "tolerance": 100,
                        "lazy": True,
                    },
                    {
                        "name": "MANUAL",
                        "type": "select",
                        "proxies": ["LAN node 1", "LAN node 2"],
                    },
                    {
                        "name": "PROXY",
                        "type": "select",
                        "proxies": ["AUTO", "MANUAL"],
                    },
                ],
                "rules": ["MATCH,PROXY"],
            },
        )


class VlessParsingTests(unittest.TestCase):
    @staticmethod
    def xhttp_link(mode: str) -> str:
        return (
            f"vless://{uuid.UUID(int=1)}@example.com:443"
            f"?encryption=none&security=tls&type=xhttp&path=%2F&mode={mode}#xhttp"
        )

    def test_supported_xhttp_modes_are_normalized_and_retained(self) -> None:
        for mode in sorted(builder.SUPPORTED_XHTTP_MODES):
            with self.subTest(mode=mode):
                proxy = builder.parse_vless(self.xhttp_link(mode.upper()), "TEST")
                self.assertIsNotNone(proxy)
                self.assertEqual(proxy["xhttp-opts"]["mode"], mode)

    def test_unsupported_xhttp_mode_is_rejected(self) -> None:
        self.assertIsNone(builder.parse_vless(self.xhttp_link("s"), "TEST"))


class HappMobileSubscriptionTests(unittest.TestCase):
    @staticmethod
    def proxy(
        number: int,
        *,
        source: str = "IGARECK_WHITE_MOBILE_1",
        server: str = "203.0.113.10",
        port: int = 443,
        network: str = "grpc",
        insecure: bool = False,
    ) -> dict:
        proxy = {
            "name": f"Mobile node {number}",
            "_sources": [source],
            "_input_order": number,
            "type": "vless",
            "server": server,
            "port": port,
            "uuid": str(uuid.UUID(int=number)),
            "network": network,
            "udp": True,
            "encryption": "none",
            "tls": True,
            "servername": "example.com",
            "client-fingerprint": "chrome",
            "reality-opts": {
                "public-key": "A" * 43,
                "short-id": "12ab",
            },
        }
        if network == "grpc":
            proxy["grpc-opts"] = {"grpc-service-name": "mobile"}
        if insecure:
            proxy["skip-cert-verify"] = True
        return proxy

    def test_vless_serializer_round_trips_happ_fields(self) -> None:
        proxy = self.proxy(1, server="2001:db8::1")
        link = builder.proxy_to_vless_uri(proxy)
        parsed = builder.parse_vless(link, "ROUND_TRIP")

        self.assertIsNotNone(parsed)
        self.assertEqual(parsed["server"], "2001:db8::1")
        self.assertEqual(parsed["network"], "grpc")
        self.assertEqual(parsed["servername"], "example.com")
        self.assertEqual(parsed["grpc-opts"]["grpc-service-name"], "mobile")
        self.assertEqual(parsed["reality-opts"]["short-id"], "12ab")

    def test_mobile_selection_is_strict_and_has_no_country_requirement(self) -> None:
        valid = self.proxy(1)
        valid["_country"] = "UNKNOWN"
        non_mobile = self.proxy(2, source="FULL", server="203.0.113.11")
        insecure = self.proxy(3, server="203.0.113.12", insecure=True)

        selected = builder.select_mobile_proxies([non_mobile, insecure, valid])

        self.assertEqual(selected, [valid])

    def test_happ_subscription_is_plain_vless_without_groups(self) -> None:
        proxies = [
            self.proxy(1),
            self.proxy(2, server="203.0.113.11"),
        ]
        text = builder.build_happ_subscription(proxies)

        self.assertIn("#profile-title: pale-signal mobile", text)
        self.assertNotIn("proxy-groups", text)
        self.assertEqual(builder.validate_happ_subscription(text, 2), 2)
        links = [line for line in text.splitlines() if line.startswith("vless://")]
        self.assertEqual(len(links), 2)


if __name__ == "__main__":
    unittest.main()

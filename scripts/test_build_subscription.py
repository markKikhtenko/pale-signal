#!/usr/bin/env python3
import inspect
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
            "minimum_vless": 1,
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
        self.assertIn(builder.experimental_readme_section(stats), readme)
        self.assertIn(f"| LAN Experimental | `{stats['total']}` |", readme)
        self.assertIn(f"| LAN Experimental AUTO | `{stats['auto']}` |", readme)
        self.assertIn(
            "| Исключено пересечений Experimental с LAN Global | "
            f"`{stats['lan_global_overlap']}` |",
            readme,
        )


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

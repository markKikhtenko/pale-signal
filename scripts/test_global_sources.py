#!/usr/bin/env python3
import json
import tempfile
import unittest
import uuid
from pathlib import Path

import yaml

import build_subscription as builder
import check_global_sources as global_health
import check_megafon


class GlobalSourcePolicyTests(unittest.TestCase):
    def test_new_sources_are_global_only_and_keep_legacy_priority(self) -> None:
        expected = {
            "HUSSAROFF_LTE_UNIVERSAL_CHECKED": "https://raw.githubusercontent.com/hussaroff/lte-universal-checked/main/whitelist.txt",
            "COLORAMA_WHITELIST_VLESS": "https://raw.githubusercontent.com/coloramamoe/vless-parser/main/githubmirror/whitelist-vless.txt",
            "COLORAMA_RU_SNI_BEST_VLESS": "https://raw.githubusercontent.com/coloramamoe/vless-parser/main/githubmirror/ru-sni-best-vless.txt",
        }
        sources = {source["id"]: source for source in builder.SOURCES}
        self.assertEqual(tuple(expected), builder.NEW_GLOBAL_SOURCE_PRIORITY)
        self.assertEqual(builder.GLOBAL_SOURCE_PRIORITY[0], "PULSEPROXY_BS_30")
        self.assertEqual(
            builder.GLOBAL_SOURCE_PRIORITY[-3:], builder.NEW_GLOBAL_SOURCE_PRIORITY
        )
        for source_id, url in expected.items():
            with self.subTest(source_id=source_id):
                self.assertEqual(sources[source_id]["url"], url)
                self.assertNotIn(source_id, builder.BASE_SOURCE_IDS)
                self.assertIn(source_id, builder.GLOBAL_PRODUCTION_SOURCE_IDS)
                self.assertIn(source_id, builder.BYPASS_SOURCE_IDS)
                self.assertNotIn(source_id, builder.LAN_SOURCE_IDS)
                self.assertNotIn(source_id, builder.BS_SAFE_SOURCE_IDS)
                self.assertNotIn(source_id, builder.MOBILE_SOURCE_IDS)
                self.assertNotIn(source_id, builder.ZAPRET_SOURCE_IDS)
                self.assertNotIn(source_id, builder.EXPERIMENTAL_SOURCE_IDS)

    @staticmethod
    def raw_proxy(source_id: str, name: str, *, host: str = "cdn.example.com") -> dict:
        return {
            "_source_name": name,
            "_source_id": source_id,
            "type": "vless",
            "server": "NODE.EXAMPLE.COM.",
            "port": 443,
            "uuid": str(uuid.UUID(int=1)).upper(),
            "network": "ws",
            "udp": True,
            "encryption": "none",
            "tls": True,
            "servername": "SNI.EXAMPLE.COM.",
            "client-fingerprint": "Chrome",
            "ws-opts": {"path": "/", "headers": {"Host": host}},
        }

    def test_dedupe_uses_actual_connection_parameters_not_name(self) -> None:
        left = self.raw_proxy("OLD", "old display")
        right = self.raw_proxy("NEW", "different display", host="CDN.EXAMPLE.COM.")
        right["server"] = "node.example.com"
        right["uuid"] = str(uuid.UUID(int=1))
        right["servername"] = "sni.example.com"
        right["client-fingerprint"] = "chrome"

        result = builder.dedupe_and_name([left, right])

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "old display")
        self.assertEqual(result[0]["_sources"], ["OLD", "NEW"])

    def test_dedupe_retains_different_transport_parameter(self) -> None:
        left = self.raw_proxy("OLD", "one", host="one.example.com")
        right = self.raw_proxy("NEW", "two", host="two.example.com")
        self.assertEqual(len(builder.dedupe_and_name([left, right])), 2)

    def test_404_is_diagnostic_only_and_not_deleted(self) -> None:
        source_id = "ETONEYA_GH_WHITELIST"
        stats = builder.build_global_source_stats(
            {
                source_id: {
                    "available": False,
                    "http_status": 404,
                    "error": "HTTPError: HTTP Error 404",
                }
            },
            [],
            [],
            [],
            "2026-11-21 09:00:00 МСК",
            previous_stats={"sources": {source_id: {"consecutive_http_404": 2}}},
        )
        item = stats["sources"][source_id]
        self.assertTrue(item["review_for_removal"])
        self.assertEqual(item["consecutive_http_404"], 3)
        self.assertIn(source_id, builder.BASE_SOURCE_IDS)


class GlobalHealthOutputTests(unittest.TestCase):
    @staticmethod
    def proxy() -> dict:
        return {
            "name": "Candidate",
            "type": "vless",
            "server": "203.0.113.10",
            "port": 443,
            "uuid": str(uuid.UUID(int=1)),
            "network": "tcp",
            "udp": True,
            "encryption": "none",
        }

    def test_candidate_output_is_https_pass_but_megafon_not_tested(self) -> None:
        result = {
            "name": "Candidate",
            "https": True,
            "transfer": True,
            "latency_ms": 123,
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            yaml_path = root / "candidates.yaml"
            stats_path = root / "candidates.json"
            report_path = root / "report.json"
            rows, status = global_health.write_candidate_outputs(
                [("SOURCE", "Source", self.proxy(), result)],
                "2026-11-21 09:00:00 МСК",
                yaml_path,
                stats_path,
                report_path,
            )
            self.assertEqual(status, "updated")
            self.assertEqual(rows[0]["megafon"], "NOT TESTED")
            config = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
            self.assertEqual(
                [group["name"] for group in config["proxy-groups"]],
                ["AUTO", "MANUAL", "PROXY"],
            )
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["network"], "NOT TESTED on MegaFon")

    def test_failure_classifier_distinguishes_dns_tcp_tls_and_timeout(self) -> None:
        self.assertEqual(
            check_megafon.classify_failure(
                {"proxy_server": {"dns": False, "tcp": False}}
            ),
            "DNS",
        )
        self.assertEqual(
            check_megafon.classify_failure(
                {"proxy_server": {"dns": True, "tcp": False}}
            ),
            "TCP",
        )
        self.assertEqual(
            check_megafon.classify_failure(
                {
                    "proxy_server": {"dns": True, "tcp": True},
                    "socks_accepted": True,
                    "tls": False,
                }
            ),
            "TLS",
        )
        self.assertEqual(
            check_megafon.classify_failure(
                {
                    "proxy_server": {"dns": True, "tcp": True},
                    "error": "TimeoutError: timed out",
                }
            ),
            "TIMEOUT",
        )

    def test_push_workflow_runs_global_rebuild(self) -> None:
        workflow = (builder.ROOT / ".github/workflows/update-subscription.yml").read_text(
            encoding="utf-8"
        )
        push_branch = workflow.split(
            'if [ "${{ github.event_name }}" = "push" ]; then', 1
        )[1].split("else", 1)[0]
        self.assertIn("--global-only", push_branch)
        self.assertNotIn("--lan-only", push_branch)
        self.assertNotIn("--zapret-only", push_branch)


if __name__ == "__main__":
    unittest.main()

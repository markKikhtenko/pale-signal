#!/usr/bin/env python3
import tempfile
import unittest
from pathlib import Path

import build_subscription as builder


class LanExperimentalTests(unittest.TestCase):
    def test_experimental_sources_are_isolated(self) -> None:
        production_ids = (
            builder.BASE_SOURCE_IDS
            | builder.LAN_SOURCE_IDS
            | builder.BYPASS_SOURCE_IDS
            | builder.BS_SAFE_SOURCE_IDS
        )
        self.assertTrue(builder.EXPERIMENTAL_SOURCE_IDS)
        self.assertTrue(builder.EXPERIMENTAL_SOURCE_IDS.isdisjoint(production_ids))

    def test_normalized_identity_ignores_display_and_service_fields(self) -> None:
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
            "server": "example.com",
            "uuid": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        }
        self.assertEqual(builder.canonical_proxy_config(left), builder.canonical_proxy_config(right))
        self.assertEqual(builder.endpoint_identity_key(left), builder.endpoint_identity_key(right))

    def test_all_sources_unavailable_does_not_overwrite_last_good_file(self) -> None:
        source = {"id": "UNAVAILABLE", "name": "Unavailable", "url": "https://invalid.example/sub"}

        def unavailable(_source):
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


if __name__ == "__main__":
    unittest.main()

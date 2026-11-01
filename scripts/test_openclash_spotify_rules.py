#!/usr/bin/env python3
"""Regression tests for Spotify routing in the OpenClash module."""

from __future__ import annotations

import unittest
from pathlib import Path

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PROXY_DOMAINS_PATH = REPOSITORY_ROOT / "openclash/rules/custom-proxy-domains.yaml"
DIRECT_DOMAINS_PATH = REPOSITORY_ROOT / "openclash/rules/custom-direct-domains.yaml"
MODULE_PATH = REPOSITORY_ROOT / "openclash/blacklist-routing.conf"

SPOTIFY_DOMAINS = {
    "+.spotify.com",
    "+.scdn.co",
    "+.pscdn.co",
    "+.spotifycdn.com",
    "+.spotifycdn.net",
    "+.spoti.fi",
    "+.spotify.link",
    "+.spotify-everywhere.com",
    "audio-ak-spotify-com.akamaized.net",
    "audio4-ak-spotify-com.akamaized.net",
    "heads-ak-spotify-com.akamaized.net",
    "heads4-ak-spotify-com.akamaized.net",
    "spotify.com.edgesuite.net",
    "spotify.map.fastly.net",
    "spotify.map.fastlylb.net",
}


def load_payload(path: Path) -> list[str]:
    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict) or not isinstance(document.get("payload"), list):
        raise AssertionError(f"{path} must contain a payload list")
    return document["payload"]


class SpotifyOpenClashRulesTest(unittest.TestCase):
    def test_spotify_domains_are_unique_and_scoped(self) -> None:
        payload = load_payload(PROXY_DOMAINS_PATH)

        self.assertEqual(len(payload), len(set(payload)), "duplicate PROXY domain rules")
        self.assertTrue(SPOTIFY_DOMAINS.issubset(payload))
        self.assertTrue(SPOTIFY_DOMAINS.isdisjoint(load_payload(DIRECT_DOMAINS_PATH)))
        for shared_cdn in (
            "+.akamaized.net",
            "+.edgesuite.net",
            "+.fastly.net",
            "+.fastlylb.net",
        ):
            self.assertNotIn(shared_cdn, payload)

    def test_spotify_provider_routes_through_proxy_before_fallback(self) -> None:
        module_text = MODULE_PATH.read_text(encoding="utf-8")
        yaml_text = module_text.split("[YAML]", maxsplit=1)[1]
        module = yaml.safe_load(yaml_text)

        provider_name = "pale-signal-custom-proxy-domain"
        provider = module["rule-providers"][provider_name]
        self.assertEqual(provider["behavior"], "domain")
        self.assertEqual(provider["format"], "yaml")
        self.assertTrue(provider["url"].endswith("/custom-proxy-domains.yaml"))

        rules = module["rules+"]
        proxy_rule = f"RULE-SET,{provider_name},PROXY"
        self.assertIn(proxy_rule, rules)
        self.assertLess(rules.index(proxy_rule), rules.index("MATCH,DIRECT"))


if __name__ == "__main__":
    unittest.main()

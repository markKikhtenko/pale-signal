# Pale Signal

Automatically updated VLESS subscription for Mihomo, OpenClash and FLClash.

## Subscription files

- `subscription.yaml` - main Mihomo/OpenClash config.
- `merged_flclash.yaml` - same config under a FLClash-style name.
- `subscription_base64.txt` - base64 encoded YAML.
- `subscription_info.txt` - update summary and counters.
- `servers_history.json` - first/last seen server history.

## Features

- Updates every hour through GitHub Actions.
- Parses VLESS links from one source: `https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt`.
- Skips invalid lines and keeps the previous working files if build validation fails.
- Deduplicates servers and keeps proxy names unique.
- Supports Reality, TLS, TCP, WebSocket, gRPC and XHTTP.
- Provides `AUTO`, `FALLBACK`, `PROXY` and protocol/security groups when available.
- Does not ping servers or connect to them during Actions.

## Current build

- Updated: `2026-07-17T09:50:15Z`
- Servers: `286`
- Reality: `199`
- TLS: `277`
- TCP: `153`
- WebSocket: `21`
- gRPC: `30`
- XHTTP: `82`

## OpenClash

Use the GitHub Pages URL when this repository is public or the account plan supports Pages for private repositories:

`https://markkikhtenko.github.io/pale-signal/subscription.yaml`

#!/usr/bin/env python3
"""Bounded HTTPS verification intended for a router on the MegaFon network."""

import argparse
import concurrent.futures
import json
import statistics
import sys
from pathlib import Path

import build_subscription as builder
import check_global_sources as global_health
import check_lan_new_sources as mihomo_health


DEFAULT_MARKDOWN_REPORT = builder.ROOT / "megafon-report.md"
DEFAULT_VERIFIED_OUTPUT = builder.ROOT / "subscription-global-megafon-verified.yaml"


def classify_failure(result: dict) -> str:
    server = result.get("proxy_server", {})
    combined_error = " ".join(
        [
            str(result.get("error", "")),
            str(server.get("error", "")),
            *[
                str(probe.get("error", ""))
                for probe in result.get("probes", [])
            ],
        ]
    ).casefold()
    if "timeout" in combined_error or "timed out" in combined_error:
        return "TIMEOUT"
    if not server.get("dns"):
        return "DNS"
    if not server.get("tcp"):
        return "TCP"
    if result.get("socks_accepted") and not result.get("tls"):
        return "TLS"
    if result.get("tls") and not result.get("https"):
        return "HTTPS"
    return "PROXY"


def markdown_cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(report: dict) -> str:
    lines = [
        "# Проверка кандидатов в сети МегаФона",
        "",
        f"Время: `{report['updated']}`",
        "",
        (
            "Проверка выполнена реальными HTTPS-запросами через отдельный экземпляр "
            "Mihomo для каждого кандидата. TCP и `mihomo -t` сами по себе не считаются PASS."
        ),
        "",
        "| Имя | Источник | мс | HTTPS | МегаФон | Ошибка |",
        "|---|---|---:|---|---|---|",
    ]
    for row in report.get("rows", []):
        latency = row.get("latency_ms")
        lines.append(
            f"| {markdown_cell(row.get('name', '-'))} | "
            f"{markdown_cell(row.get('source', '-'))} | "
            f"`{latency if latency is not None else '-'}` | "
            f"{row.get('https', 'FAIL')} | {row.get('megafon', 'FAIL')} | "
            f"{markdown_cell(row.get('error_phase') or '-')} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
    parser = argparse.ArgumentParser()
    parser.add_argument("--mihomo", type=Path, required=True)
    parser.add_argument(
        "--candidates", type=Path, default=builder.MEGAFON_CANDIDATES_STATS_FILE
    )
    parser.add_argument("--report", type=Path, default=builder.MEGAFON_REPORT_FILE)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MARKDOWN_REPORT)
    parser.add_argument("--verified-output", type=Path, default=DEFAULT_VERIFIED_OUTPUT)
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--timeout", type=float, default=12.0)
    parser.add_argument(
        "--confirm-megafon",
        action="store_true",
        help="confirm that this process is actually running through a MegaFon WAN",
    )
    args = parser.parse_args()

    if not args.confirm_megafon:
        raise RuntimeError(
            "refusing to label results as MegaFon: rerun on the MegaFon router with --confirm-megafon"
        )
    if not args.mihomo.is_file():
        raise RuntimeError(f"mihomo executable not found: {args.mihomo}")
    if not 1 <= args.limit <= 32:
        raise RuntimeError("--limit must be between 1 and 32")
    if not 1 <= args.workers <= 4:
        raise RuntimeError("--workers must be between 1 and 4")
    if not 2 <= args.timeout <= 60:
        raise RuntimeError("--timeout must be between 2 and 60 seconds")

    payload = json.loads(args.candidates.read_text(encoding="utf-8"))
    candidates = payload.get("candidates", [])
    if not isinstance(candidates, list) or not candidates:
        raise RuntimeError("no GitHub-HTTPS-passed MegaFon candidates are available")
    selected = candidates[: args.limit]

    completed: dict[int, dict] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(
                mihomo_health.test_proxy,
                args.mihomo.resolve(),
                candidate["proxy"],
                args.timeout,
            ): index
            for index, candidate in enumerate(selected)
        }
        for future in concurrent.futures.as_completed(futures):
            index = futures[future]
            completed[index] = future.result()

    rows = []
    verified = []
    for index, candidate in enumerate(selected):
        result = completed[index]
        passed = global_health.is_https_pass(result)
        if passed:
            verified.append(candidate["proxy"])
        row = {
            "name": candidate["proxy"].get("name", "unnamed"),
            "source": candidate.get("source", candidate.get("source_id", "-")),
            "latency_ms": result.get("latency_ms"),
            "https": "PASS" if passed else "FAIL",
            "megafon": "PASS" if passed else "FAIL",
            "error_phase": "" if passed else classify_failure(result),
            "error": "" if passed else result.get("error", ""),
            "diagnostics": result,
        }
        rows.append(row)
        print(
            f"{row['name']}: {row['megafon']}"
            + (f" ({row['error_phase']})" if row["error_phase"] else "")
        )

    checked_at = builder.msk_timestamp()
    latencies = [
        row["latency_ms"]
        for row in rows
        if row["megafon"] == "PASS" and isinstance(row.get("latency_ms"), int)
    ]
    report = {
        "updated": checked_at,
        "network": "MegaFon (operator confirmed by --confirm-megafon)",
        "limits": {
            "candidates": args.limit,
            "workers": args.workers,
            "timeout_seconds": args.timeout,
        },
        "tested": len(rows),
        "passed": len(verified),
        "failed": len(rows) - len(verified),
        "median_latency_ms": round(statistics.median(latencies)) if latencies else None,
        "rows": rows,
    }
    builder.atomic_write_text(
        args.report,
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
    )
    builder.atomic_write_text(args.markdown, render_markdown(report))

    if verified:
        config = builder.build_config(verified)
        builder.validate_config(config)
        builder.atomic_write_text(
            args.verified_output,
            "\n".join(builder.dump_yaml(config)) + "\n",
        )
        print(
            f"wrote {args.verified_output} with {len(verified)} MegaFon HTTPS PASS proxies"
        )
    else:
        print(
            "no MegaFon HTTPS PASS proxies; existing verified subscription was not overwritten"
        )
    print(f"wrote reports: {args.report}, {args.markdown}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(1)

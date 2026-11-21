#!/usr/bin/env python3
"""Run a bounded real-HTTPS audit for the newly added Global sources."""

import argparse
import concurrent.futures
import copy
import json
import os
import statistics
import sys
from pathlib import Path

import build_subscription as builder
import check_lan_new_sources as mihomo_health


def is_https_pass(result: dict) -> bool:
    """Require a real HTTPS response and a non-empty 64 KiB transfer."""
    return bool(result.get("https") and result.get("transfer"))


def exported_proxy(proxy: dict) -> dict:
    return {
        key: copy.deepcopy(value)
        for key, value in proxy.items()
        if not key.startswith("_")
    }


def candidate_row(source_name: str, result: dict) -> dict:
    return {
        "name": str(result.get("name", "unnamed")),
        "source": source_name,
        "latency_ms": result.get("latency_ms"),
        "https": "PASS",
        "megafon": "NOT TESTED",
    }


def update_source_stats(stats: dict, source_id: str, results: list[dict]) -> None:
    item = stats.get("sources", {}).get(source_id)
    if not isinstance(item, dict):
        return
    latencies = [
        int(result["latency_ms"])
        for result in results
        if is_https_pass(result) and isinstance(result.get("latency_ms"), int)
    ]
    item.update(
        {
            "dns_tested": len(results),
            "dns_success": sum(
                bool(result.get("proxy_server", {}).get("dns")) for result in results
            ),
            "tcp_tested": len(results),
            "tcp_success": sum(
                bool(result.get("proxy_server", {}).get("tcp")) for result in results
            ),
            "https_tested": len(results),
            "https_success": sum(is_https_pass(result) for result in results),
            "https_failed": sum(not is_https_pass(result) for result in results),
            "transfer_success": sum(bool(result.get("transfer")) for result in results),
            "median_latency_ms": (
                round(statistics.median(latencies)) if latencies else None
            ),
            "health_results": results,
            "megafon": "NOT TESTED",
        }
    )


def write_candidate_outputs(
    passing: list[tuple[str, str, dict, dict]],
    checked_at: str,
    candidate_yaml: Path,
    candidate_stats: Path,
    report_path: Path,
) -> tuple[list[dict], str]:
    unique_passing: list[tuple[str, str, dict, dict]] = []
    seen_configs: set[str] = set()
    for entry in passing:
        config_key = builder.canonical_proxy_config(entry[2])
        if config_key in seen_configs:
            continue
        seen_configs.add(config_key)
        unique_passing.append(entry)
    passing = unique_passing
    rows: list[dict] = []
    status = "no_https_pass"
    if passing:
        proxies = [proxy for _source_id, _source_name, proxy, _result in passing]
        config = builder.build_config(proxies)
        builder.validate_config(config)
        yaml_text = "\n".join(builder.dump_yaml(config)) + "\n"
        builder.atomic_write_text(candidate_yaml, yaml_text)
        candidates = []
        for source_id, source_name, proxy, result in passing:
            candidates.append(
                {
                    "source_id": source_id,
                    "source": source_name,
                    "checked_at": checked_at,
                    "github_https": "PASS",
                    "latency_ms": result.get("latency_ms"),
                    "proxy": exported_proxy(proxy),
                }
            )
            rows.append(candidate_row(source_name, result))
        builder.atomic_write_text(
            candidate_stats,
            json.dumps(
                {
                    "updated": checked_at,
                    "environment": "GitHub Actions or local runner; not MegaFon",
                    "candidates": candidates,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
        )
        status = "updated"
    elif candidate_yaml.is_file() and candidate_stats.is_file():
        try:
            previous = json.loads(candidate_stats.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            previous = {}
        for candidate in previous.get("candidates", []):
            rows.append(
                {
                    "name": candidate.get("proxy", {}).get("name", "unnamed"),
                    "source": candidate.get("source", "-"),
                    "latency_ms": candidate.get("latency_ms"),
                    "https": "PASS",
                    "megafon": "NOT TESTED",
                }
            )
        status = "retained_last_good"
    else:
        builder.atomic_write_text(
            candidate_stats,
            json.dumps(
                {
                    "updated": checked_at,
                    "environment": "GitHub Actions or local runner; not MegaFon",
                    "candidates": [],
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
        )

    builder.atomic_write_text(
        report_path,
        json.dumps(
            {
                "updated": checked_at,
                "network": "NOT TESTED on MegaFon",
                "candidate_status": status,
                "rows": rows,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
    )
    return rows, status


def summary_lines(stats: dict, candidate_status: str) -> list[str]:
    lines = [
        "### Global whitelist source audit",
        "",
        "GitHub HTTPS checks below are not MegaFon tests.",
        "",
        "| Source | HTTP | Valid | New Global | DNS | TCP | HTTPS+64KiB | MegaFon |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for source_id in builder.NEW_GLOBAL_SOURCE_PRIORITY:
        item = stats.get("sources", {}).get(source_id, {})
        lines.append(
            f"| {item.get('name', source_id)} | {item.get('http_status', '-')} | "
            f"{item.get('valid', 0)} | {item.get('unique_added_global', 0)} | "
            f"{item.get('dns_success', 0)}/{item.get('dns_tested', 0)} | "
            f"{item.get('tcp_success', 0)}/{item.get('tcp_tested', 0)} | "
            f"{item.get('https_success', 0)}/{item.get('https_tested', 0)} | NOT TESTED |"
        )
    unavailable = [
        item
        for item in stats.get("sources", {}).values()
        if item.get("review_for_removal")
    ]
    lines.extend(
        [
            "",
            f"MegaFon candidate artifact: {candidate_status}",
            f"Old sources currently returning HTTP 404: {len(unavailable)}",
        ]
    )
    return lines


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
    parser = argparse.ArgumentParser()
    parser.add_argument("--mihomo", type=Path, required=True)
    parser.add_argument(
        "--candidates", type=Path, default=builder.GLOBAL_HEALTH_CANDIDATES_FILE
    )
    parser.add_argument("--stats", type=Path, default=builder.GLOBAL_SOURCE_STATS_FILE)
    parser.add_argument("--readme", type=Path, default=builder.README_FILE)
    parser.add_argument(
        "--candidate-yaml", type=Path, default=builder.MEGAFON_CANDIDATES_FILE
    )
    parser.add_argument(
        "--candidate-stats",
        type=Path,
        default=builder.MEGAFON_CANDIDATES_STATS_FILE,
    )
    parser.add_argument("--report", type=Path, default=builder.MEGAFON_REPORT_FILE)
    parser.add_argument("--max-per-source", type=int, default=5)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=float, default=10.0)
    args = parser.parse_args()

    if not args.mihomo.is_file():
        raise RuntimeError(f"mihomo executable not found: {args.mihomo}")
    if not 1 <= args.max_per_source <= 20:
        raise RuntimeError("--max-per-source must be between 1 and 20")
    if not 1 <= args.workers <= 8:
        raise RuntimeError("--workers must be between 1 and 8")
    if not 2 <= args.timeout <= 60:
        raise RuntimeError("--timeout must be between 2 and 60 seconds")

    stats = json.loads(args.stats.read_text(encoding="utf-8"))
    candidates = json.loads(args.candidates.read_text(encoding="utf-8"))
    jobs: list[tuple[str, str, int, dict]] = []
    source_names = {
        source["id"]: source["name"]
        for source in builder.SOURCES
        if source["id"] in builder.NEW_GLOBAL_SOURCE_IDS
    }
    for source_id in builder.NEW_GLOBAL_SOURCE_PRIORITY:
        for index, proxy in enumerate(
            candidates.get(source_id, [])[: args.max_per_source]
        ):
            jobs.append((source_id, source_names[source_id], index, proxy))

    completed: dict[tuple[str, int], dict] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_jobs = {
            executor.submit(
                mihomo_health.test_proxy,
                args.mihomo.resolve(),
                proxy,
                args.timeout,
            ): (source_id, source_name, index)
            for source_id, source_name, index, proxy in jobs
        }
        for future in concurrent.futures.as_completed(future_jobs):
            source_id, source_name, index = future_jobs[future]
            result = future.result()
            completed[(source_id, index)] = result
            outcome = "PASS" if is_https_pass(result) else "FAIL"
            print(f"{source_name} / {result.get('name', 'unnamed')}: {outcome}")

    passing: list[tuple[str, str, dict, dict]] = []
    for source_id in builder.NEW_GLOBAL_SOURCE_PRIORITY:
        source_results: list[dict] = []
        for job_source_id, source_name, index, proxy in jobs:
            if job_source_id != source_id:
                continue
            result = completed[(source_id, index)]
            source_results.append(result)
            if is_https_pass(result):
                passing.append((source_id, source_name, proxy, result))
        update_source_stats(stats, source_id, source_results)

    checked_at = builder.msk_timestamp()
    rows, candidate_status = write_candidate_outputs(
        passing,
        checked_at,
        args.candidate_yaml,
        args.candidate_stats,
        args.report,
    )
    stats["updated"] = checked_at
    stats["health_environment"] = {
        "name": "GitHub Actions or local runner",
        "megafon": "NOT TESTED",
        "direct_https": mihomo_health.diagnose_environment(args.timeout),
        "max_per_source": args.max_per_source,
        "workers": args.workers,
        "timeout_seconds": args.timeout,
        "candidate_status": candidate_status,
    }
    stats["megafon_report"] = rows
    builder.write_global_source_stats(stats, args.stats)
    builder.refresh_readme_global_source_stats(stats, args.readme)

    lines = summary_lines(stats, candidate_status)
    print("\n".join(lines))
    github_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if github_summary:
        with Path(github_summary).open("a", encoding="utf-8", newline="\n") as summary:
            summary.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(1)

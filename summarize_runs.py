"""Summarise prompt runs: citation rate per platform and who gets cited.

Input: a CSV of measurement runs with at least the columns platform,
prompt_id, cpm_cited (Y / N / not_captured) and other_cited_domains
(semicolon-separated). See data/baseline-runs-2026-09-28.csv.

Runs marked not_captured are excluded from the citation rate, because
"no citation found" and "sources not recorded" are different results.

Usage:
    python scripts/summarize_runs.py data/baseline-runs-2026-09-28.csv
    python scripts/summarize_runs.py data/baseline-runs-2026-09-28.csv --vendors asana.com,clickup.com
"""

import argparse
import csv
from collections import Counter, defaultdict

DEFAULT_VENDORS = (
    "asana.com,help.asana.com,forum.asana.com,clickup.com,help.clickup.com,"
    "wrike.com,atlassian.com,trello.com,monday.com,smartsheet.com,freedcamp.com"
)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("csv")
    ap.add_argument("--vendors", default=DEFAULT_VENDORS,
                    help="comma-separated domains owned by the tool vendors")
    args = ap.parse_args()
    vendors = {v.strip() for v in args.vendors.split(",") if v.strip()}

    with open(args.csv, newline="", encoding="utf-8") as f:
        runs = list(csv.DictReader(f))

    print(f"Runs: {len(runs)}")
    print("\nOwn-site citation rate by platform (runs with captured sources only)")
    by_platform = defaultdict(list)
    for r in runs:
        by_platform[r["platform"]].append(r)
    for p, rs in by_platform.items():
        captured = [r for r in rs if r["cpm_cited"] in ("Y", "N")]
        cited = sum(r["cpm_cited"] == "Y" for r in captured)
        if captured:
            print(f"  {p:<11} {cited}/{len(captured)} cited")
        else:
            print(f"  {p:<11} sources not captured ({len(rs)} runs)")

    domains = Counter()
    split = defaultdict(lambda: Counter())
    for r in runs:
        ds = [d.strip() for d in (r.get("other_cited_domains") or "").split(";")]
        ds = [d for d in ds if d and d != "none shown"]
        for d in ds:
            domains[d] += 1
            kind = "vendor" if d in vendors else "third-party"
            split[r["prompt_id"]][kind] += 1

    print("\nMost cited domains")
    for d, n in domains.most_common(12):
        tag = "vendor" if d in vendors else "third-party"
        print(f"  {d:<24} {n:>2}  ({tag})")

    print("\nVendor vs. third-party citations by prompt")
    for pid in sorted(split):
        c = split[pid]
        total = c["vendor"] + c["third-party"]
        print(f"  {pid}  vendor {c['vendor']:>2}  third-party {c['third-party']:>2}"
              f"  ({c['third-party'] / total:.0%} third-party)")


if __name__ == "__main__":
    main()

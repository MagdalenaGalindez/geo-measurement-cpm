"""Summarise AI-referred sessions by platform, landing page and month.

Input: a CSV with the columns date (YYYY-MM-DD), platform, landing_page,
one row per session that arrived from an AI assistant. The file in
ai-referrals.csv was built from the Clicky visitor log, filtered by
referrer domain (chatgpt.com, claude.ai, gemini.google.com, perplexity.ai,
perplexity, copilot.microsoft.com).

Usage:
    python summarize_referrals.py ai-referrals.csv
    python summarize_referrals.py ai-referrals.csv --since 2026-01-01
"""

import argparse
import csv
from collections import Counter, defaultdict


def load(path, since=None, until=None):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if since:
        rows = [r for r in rows if r["date"] >= since]
    if until:
        rows = [r for r in rows if r["date"] <= until]
    return rows


def table(title, counter, total):
    print(f"\n{title}")
    width = max((len(k) for k in counter), default=10)
    for key, n in counter.most_common():
        print(f"  {key:<{width}}  {n:>4}  {n / total:6.1%}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("csv")
    ap.add_argument("--since", help="first date to include, YYYY-MM-DD")
    ap.add_argument("--until", help="last date to include, YYYY-MM-DD")
    args = ap.parse_args()

    rows = load(args.csv, args.since, args.until)
    if not rows:
        print("No rows in range.")
        return
    total = len(rows)
    first, last = min(r["date"] for r in rows), max(r["date"] for r in rows)
    print(f"AI-referred sessions: {total} ({first} to {last})")

    table("By platform", Counter(r["platform"] for r in rows), total)
    table("By landing page", Counter(r["landing_page"] for r in rows), total)

    months = defaultdict(Counter)
    for r in rows:
        months[r["date"][:7]][r["platform"]] += 1
    platforms = sorted({r["platform"] for r in rows})
    print("\nBy month")
    print("  month    " + "".join(f"{p[:10]:>11}" for p in platforms) + "  total")
    for m in sorted(months):
        c = months[m]
        print(f"  {m}  " + "".join(f"{c[p]:>11}" for p in platforms) + f"  {sum(c.values()):>5}")

    last_seen = {}
    for r in rows:
        last_seen[r["platform"]] = max(last_seen.get(r["platform"], ""), r["date"])
    print("\nLast session per platform")
    for p in platforms:
        print(f"  {p:<11} {last_seen[p]}")


if __name__ == "__main__":
    main()

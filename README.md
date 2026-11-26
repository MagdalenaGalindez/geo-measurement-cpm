# GEO measurement: cleverprojectmanagement.com

A small, real-world experiment in generative engine optimization (GEO): how one niche content site shows up in AI assistants, how to measure that honestly, and what happened after a fact refresh.

The site is [cleverprojectmanagement.com](https://cleverprojectmanagement.com) (CPM), an independent site about project management software. Everything in this repository is first-party data from that site: Search Console exports, AI referral logs and manually run prompt tests. Nothing is simulated.

## Summary

| | |
|---|---|
| Page under test | [Free project management plans: how many users each plan allows](https://cleverprojectmanagement.com/free-software/free-project-management-plans-how-many-users/) |
| AI-referred sessions, Dec 2025 – Nov 2026 | 51, of which 45 (88%) landed on this one page |
| Platforms sending visits | ChatGPT 27, Claude 9, Perplexity 6, Gemini 6, Copilot 3 |
| Baseline citation rate (28 Sep 2026) | 0 of 15 runs with captured sources |
| Content refresh | 5 Oct 2026 (page under test plus 10 related pages) |
| Effect of the refresh | not measurable yet (see [Results](#results)) |

## Background

The page was written in September 2025 as a reference page that both search engines and LLMs could quote: a direct answer at the top, one verifiable figure per tool, and a comparison table. It compares how many users the free plans of Asana, ClickUp, Trello, monday.com and others allow.

Two things made it a useful test case:

- **Demand was concentrated.** In 16 months of Search Console data the page collected 32,381 impressions, 98% of them for Asana free-plan queries. Several queries read like prompts pasted from a chat window ("we are 5 members…", "is this correct").
- **The facts went stale.** Asana cut its free plan from 15 users to 10 (late 2023) and then to 2 (12 Nov 2025). The page still said 15 and ranked #5 on Google for "asana free plan up to 15 users", so it was being found for an outdated claim.

## Results

### Observed: AI referral traffic

From the Clicky visitor log, filtered by referrer domain. One row per session in [`ai-referrals.csv`](ai-referrals.csv).

| Month | ChatGPT | Claude | Copilot | Gemini | Perplexity | Total |
|---|---:|---:|---:|---:|---:|---:|
| 2025-12 | 2 | 0 | 1 | 0 | 1 | 4 |
| 2026-01 | 8 | 2 | 0 | 0 | 2 | 12 |
| 2026-02 | 8 | 0 | 0 | 0 | 2 | 10 |
| 2026-03 | 3 | 1 | 0 | 0 | 0 | 4 |
| 2026-04 | 5 | 3 | 0 | 0 | 1 | 9 |
| 2026-05 | 1 | 0 | 1 | 1 | 0 | 3 |
| 2026-06 | 0 | 2 | 0 | 2 | 0 | 4 |
| 2026-07 | 0 | 1 | 1 | 1 | 0 | 3 |
| 2026-08 – 09 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2026-10 | 0 | 0 | 0 | 1 | 0 | 1 |
| 2026-11 | 0 | 0 | 0 | 1 | 0 | 1 |

What the data shows:

- **AI visibility on this site sits on one page.** 45 of 51 AI-referred sessions landed on the page under test, across all five platforms.
- **ChatGPT referrals stopped in mid-May 2026**, after a steady January–April. Search Console impressions for the page were also highest in January–March and declined afterwards.
- **The decline started months before the refresh**, so the refresh did not cause it.

The absolute numbers are small. They are reported in full because the pattern (concentration, platform mix, timing) is the finding, not the volume.

### Observed: baseline prompt test, 28 Sep 2026

Five prompts, four platforms, one run each. Full answers summarised in [`baseline-runs-2026-09-28.csv`](baseline-runs-2026-09-28.csv).

- CPM was **not cited in any of the 15 runs** where sources were recorded (ChatGPT, Perplexity, Gemini). Claude's sources were not captured, so those five runs are excluded from the rate.
- **Fact prompts go to the vendor.** For "How many users can I have on Asana's free plan?" (P02) and "What are the limitations…?" (P25), 9 of 12 citations were Asana's own pages.
- **The team-size prompt goes to third parties.** For "We are a team of 5, can we use Asana for free?" (P27), 5 of 7 citations were independent sites.
- **The comparison prompt goes mostly to vendors too.** For "Which tool offers unlimited users for free?" (P28), 5 of 8 citations were pages owned by tool vendors (ClickUp, Atlassian, Wrike), several of them comparison articles promoting their own product.
- **Errors travel with sources.** Gemini repeated wrong figures (Trello "unlimited users", ClickUp "100 MB") that appear in the Wrike listicle it cited.

### What this repository does not claim

- That writing the page for LLMs **caused** the AI traffic. There was no control page and no before/after design in 2025.
- That the October 2026 refresh **improved** anything. Two AI sessions have arrived since, both from Gemini; that is too little to read either way.
- That one run per prompt is a reliable citation rate. Answers vary between runs; a single run is a snapshot.

## The experiment

1. **Prompts from data, not brainstorming.** A first set of 24 prompts was written before looking at any data. Search Console then showed that almost none of them matched real demand. They were dropped and replaced by five prompts derived from actual queries for the page ([`prompt-set.csv`](prompt-set.csv)), each with a hypothesis written down before the baseline.
2. **Controlled runs.** Fresh chat per prompt; personalization, custom instructions and memory off; logged out where possible. Conditions per platform are in [`methodology.md`](methodology.md).
3. **One change, logged.** On 5 Oct 2026 the page was corrected (Asana 2 users, Trello 10 collaborators, Smartsheet no free plan, ClickUp 60 MB storage), Freedcamp and Wrike were added, and a short limit history (15 → 10 → 2) and FAQ were added for the prompts. Related pages that contradicted it were fixed the same day. Every change is in [`change-log.csv`](change-log.csv).
4. **Re-measure** under identical conditions and compare AI referrals before and after.

## Repository contents

```
ai-referrals.csv                 one row per AI-referred session (date, platform, landing page)
baseline-runs-2026-09-28.csv     20 prompt runs with cited domains and notes
change-log.csv                   every content change with date and affected prompts
prompt-set.csv                   the 5 measured prompts with pre-registered hypotheses
methodology.md                   run conditions, definitions, limits
summarize_referrals.py           AI referrals by platform, page and month
summarize_runs.py                citation rate and vendor vs. third-party split
```

The scripts need only Python 3 and the standard library:

```bash
python summarize_referrals.py ai-referrals.csv --since 2026-01-01
python summarize_runs.py baseline-runs-2026-09-28.csv
```

They work on any CSV with the same columns, so the same approach can be reused for another site.

## Lessons so far

- **Find the page that carries your AI visibility before optimizing anything.** Here it was one URL out of 40+.
- **Prompt type decides who gets cited.** For pure fact questions, an independent site competes with the vendor's own pricing page and usually loses. The opening is in questions the vendor does not answer well: team-size decisions, limit history, cross-tool comparisons.
- **Stale facts are a visibility risk.** A page can keep ranking for a claim that is no longer true, and AI answers can inherit errors from whichever source they cite.
- **Measure citations, not just clicks.** Referral logs show who clicked through; they say nothing about answers that used the page without a click.

## Data notes

- AI referrals come from Clicky. Its visitor log for this site has no sessions before December 2025, so the first months after publication are not covered.
- Only date, platform and landing page are published. No visitor-level data (IP, location, network) is included.
- Prompt answers are summarised in the notes column, not reproduced in full.

## License

Code: MIT. Data: free to reuse with attribution.

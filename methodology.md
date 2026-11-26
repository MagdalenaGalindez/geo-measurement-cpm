# Methodology

## Goal

Measure whether cleverprojectmanagement.com (CPM) is cited or mentioned in AI assistant answers to a fixed set of prompts, and whether that changes after a documented content change.

## Prompt set

Five prompts, all derived from real Search Console queries for the page under test (16-month export, filtered to that URL). Each prompt has a hypothesis written down before the first run, in `prompt-set.csv`.

| ID | Prompt | Source in Search Console |
|---|---|---|
| P02 | How many users can I have on Asana's free plan? | core "asana free plan user limit" queries |
| P25 | What are the limitations of Asana's free plan? | "asana free plan limitations" and variants |
| P26 | Did Asana change the user limit on its free plan? | "user limit change", "user limit history" |
| P27 | We are a team of 5, can we use Asana for free? | prompt-like fragments such as "we are 5 members" |
| P28 | Which project management tool offers unlimited users in its free version? | comparison queries across tools |

A first draft of 24 brainstormed prompts was discarded once the data showed that 98% of the page's demand was Asana free-plan queries. Those ideas are not measured and not published here, because there is no evidence that anyone asks them.

Prompts are used verbatim. They are a measuring instrument, not a copywriting target: the page is edited so that it answers the question behind each prompt, not so that it repeats the prompt's wording.

## Run conditions

| Platform | Conditions |
|---|---|
| ChatGPT | logged in, personalization, custom instructions and memory off, temporary chat |
| Perplexity | logged out, private browser window |
| Gemini | logged in, temporary chat; sources opened manually before recording |
| Claude | new chat outside any project, incognito, web search on, model recorded |

For every platform: a fresh chat per prompt, never several prompts in one thread.

Three early ChatGPT runs were discarded because the answers referred to the tester's own earlier conversations, which showed that personalization was still active.

## Definitions

- **Cited:** a CPM URL appears among the answer's sources or links.
- **Mentioned:** CPM is named in the answer text.
- **not_captured:** the sources were not recorded. These runs are excluded from citation rates rather than counted as "not cited".
- **Vendor domain:** a domain owned by one of the tools discussed (asana.com, clickup.com, wrike.com, atlassian.com and similar). Everything else counts as third-party.

## AI referral tracking

AI-referred sessions are taken from the Clicky visitor log, filtered by referrer domain (chatgpt.com, claude.ai, gemini.google.com, perplexity.ai, perplexity, copilot.microsoft.com). Each session is recorded with date, platform and landing page only.

Referral data shows clicks, not citations. An answer that uses the page without the reader clicking through leaves no trace here, which is why referrals and prompt runs are tracked side by side.

## Change log

Every content change is logged with its go-live date, the affected page and the prompts it targets (`change-log.csv`). Changes to the page under test and to the pages linked from it are logged separately, so that a later effect can at least be attributed to a dated change.

## Known limits

- **Small samples.** One run per prompt and platform is a snapshot. Answers vary between runs even when nothing on the page changes. Reliable citation rates need many repeated runs per prompt, which is the job of automated tracking tools.
- **No control group.** All related pages were refreshed on the same day, so any later effect belongs to the whole package, not to a single page.
- **Moving platforms.** Model updates, retrieval changes and regional differences shift results independently of the site.
- **Late tracking start.** Clicky data for this site begins in December 2025, three months after the page was published.

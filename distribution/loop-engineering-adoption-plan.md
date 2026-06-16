# Loop Engineering Adoption Plan for Bionic Banker

Status: active operating design
Date: 2026-06-16

## What the loop article means for us

The useful lesson is not “write a blog about loops.” The useful lesson is to stop treating every content/project operation as a fresh prompt.

A prompt is one request.
A loop is a recurring system with:

1. trigger
2. state file
3. skill/procedure
4. worker
5. verifier
6. stop condition
7. human boundary
8. ledger/proof

## What we already have

| Loop primitive | Current Bionic/Wukong equivalent |
|---|---|
| Automation | Hermes cron jobs and browser automation |
| Memory | `distribution/post-ledger.json`, Obsidian vault, repo docs |
| Skills | `public-content-packaging-and-posting` skill |
| Connectors | GitHub CLI, Firefox/LinkedIn via `wukong-browser`, local model CLIs |
| Verifier | public-simplicity guard, public-safety leak guard, mobile QA, ledger duplicate check |
| State | queue files under `distribution/`, project packaging docs, post ledger |
| Human boundary | no money/KYC/bank/trading/public account changes except explicitly authorized posting |

## What was missing

The duplicate LinkedIn post exposed the missing loop component:

```text
local preflight state before browser posting
```

The fix is now in place:

```text
distribution/post-ledger.json
scripts/post_ledger_check.py
```

## First production loop

Name: Bionic daily public post loop

Trigger:

```text
every day at 09:00 local time
```

State files:

```text
distribution/post-ledger.json
distribution/next-5-days-linkedin-blog-queue.md
distribution/daily-post-loop-state.md
```

Skill:

```text
public-content-packaging-and-posting
```

Worker responsibilities:

1. read queue and ledger
2. choose first unposted topic
3. create or update one blog article
4. create LinkedIn caption package
5. create deterministic carousel images
6. run duplicate ledger check
7. run public leak checks
8. publish site changes through GitHub if verified
9. post on LinkedIn using Firefox browser automation
10. capture screenshot and URL
11. update ledger and state file

Hard stop conditions:

- duplicate ledger blocker
- public-safety leak blocker
- missing article URL
- missing carousel slides
- LinkedIn not logged in
- upload failure
- no post URL/screenshot after posting

Autonomy level:

```text
Level 3: applies low-risk public content changes and posts only within this explicitly approved daily LinkedIn/blog loop.
```

Not allowed:

- paid promotion
- account/profile changes
- KYC/tax/bank/payout changes
- wallet/private-key/trading actions
- repeating topic/caption/article/carousel
- making unverifiable performance/advice claims

## Cost control

Use cheap/local tools first:

- deterministic scripts for ledger, images, checks
- local Ollama/CLI models for drafts and summaries
- main model only for final public judgment or failures

No live LinkedIn feed scan unless:

- ledger is missing
- browser shows uncertainty
- post result cannot be verified

## Second loop later

Name: Project packaging loop

Trigger:

```text
weekly or manual
```

It reads repo inventory, packages one repo with AGENTS.md/docs/cards/ADR, runs tests, updates Projects page, and writes a packaging report.

Do not enable this until the daily post loop runs cleanly for several days.

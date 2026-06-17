# Bionic Banker Async Subagent Operating Model

Date: 2026-06-17
Status: active operating pattern

## Why this exists

Hermes Agent supports background delegation via `delegate_task(background=true)`. A delegated subagent can now keep working while the main Telegram/CLI conversation stays free.

This lets Bionic Banker run like a small operating company:

- Himanshu = founder / taste / final approval
- Main Hermes chat = executive coordination layer
- Async subagents = temporary departments for active work
- Cron jobs = scheduled employees / morning radars
- Skills = SOPs
- Ledgers/state files = memory and duplicate guards

## Core rule

Use async subagents for active work that should not block the main chat.
Use cron jobs for recurring work that should happen whether or not Himanshu is present.
Use synchronous `delegate_task` only for quick parallel fan-out where the answer is needed before continuing.

## Current Hermes config

Recommended config key:

```yaml
delegation:
  max_async_children: 3
```

This caps concurrent background subagents. New background dispatches are rejected at capacity instead of queueing endlessly.

## Async vs Cron

| Need | Use |
|---|---|
| Research competitors while continuing chat | async subagent |
| Improve carousel/design while continuing chat | async subagent |
| Package a repo while continuing chat | async subagent |
| Daily 08:00 competitor scan | cron |
| Daily 08:30 project packaging scan | cron |
| Long overnight bounded worker | cron or background terminal process |
| Quick 3-way research fan-out where parent waits | synchronous `delegate_task(tasks=[...])` |
| Public posting/browser action | main chat or tightly supervised worker; stop at approval/posting gates |

## Standing async departments

### 1. Competitor Radar Agent

Mission:

- scan AI safety literacy, hallucination education, prompt injection, AI governance, agent-control competitors
- return signals and Bionic response angles

Good async prompt:

```text
Research today's AI safety / agent governance competitor signals. Return max 5 signals, why they matter to Bionic Banker, and one ship angle for each. Do not publish or modify files.
```

### 2. Project Packaging Agent

Mission:

- inspect local public-safe project assets
- recommend one packaging move
- keep boundaries clear

Good async prompt:

```text
Inspect Bionic/AML/agent-proof project assets and recommend the next public-safe shipment: who it helps, value proposition, proof checks, boundary checks. Do not modify files.
```

### 3. Design Quality Agent

Mission:

- review carousel/contact-sheet quality
- catch blur, spacing, text density, footer overlap, weak hierarchy
- propose revisions before upload

Good async prompt:

```text
Review the latest Bionic carousel contact sheet and individual slides for clarity, HD quality, density, and Bionic style. Return exact fixes. Do not post.
```

### 4. Shipping Agent

Mission:

- prepare one public-safe ship unit
- run duplicate/public-safety/build checks
- stop before public post if final approval or browser action is required

Good async prompt:

```text
Prepare today's Bionic ship package: article URL, caption, carousel folder, duplicate check, QA checklist, and exact next action. Do not click Post or publish unless explicitly authorized.
```

## Handoff protocol

Every async subagent result must return:

1. `status`: ready / blocked / needs approval
2. `artifact`: exact file path, URL, or report path
3. `summary`: what changed or what was found
4. `risk`: what could leak, overclaim, duplicate, or require approval
5. `next_action`: one concrete step

## Safety boundaries

Async agents may:

- research
- inspect local files
- draft private content
- generate private images/assets
- run tests/builds
- update private reports if instructed
- prepare upload folders

Async agents must not autonomously:

- spend money
- trade or move funds
- change KYC/tax/bank/payout/account settings
- publish public posts without explicit current authorization
- contact customers/partners
- expose private Wukong/Hermes machinery
- delete destructive data without approval

## First implementation status

Done:

- Confirmed Hermes code has async delegation support via `delegate_task(background=true)`.
- Added explicit config cap: `delegation.max_async_children: 3`.
- Created daily cron radars:
  - `Bionic AI Safety Competitor Radar` at 08:00 PDT
  - `Bionic Project Packaging Radar` at 08:30 PDT
- Dispatched first background async subagent to design the operating model.

Next:

- Let the background result re-enter the chat.
- Convert repeated async prompt patterns into a skill/SOP.
- Use async agents for competitor/design/project packaging while main chat stays free.

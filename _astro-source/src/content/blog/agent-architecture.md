---
title: "Folder Agent Architecture"
description: "A project-folder experiment: what happens when a directory starts behaving less like storage and more like a small working agent."
date: "2026-03-08"
tags: ["Tech"]
readTime: "5 min"
category: "Tech"
featured: false
slug: "agent-architecture"
---

A project folder can run six layers deep: from manual commands to a self-healing agent that remembers, reacts, and audits its own decisions. Here is what that architecture looks like in practice.

## The Workspace IS the Agent

What happens when you stop thinking of a folder as storage and start thinking of it as a system that remembers, reacts, and improves itself?

The six layers of agent architecture. From manual operations to adaptive self-improvement.

### Six Layers Deep

**Layer 0 — Manual.** You run commands by hand. You remember what happened last time because it's in your head.

**Layer 1 — Assisted.** You write some scripts. A deploy script. A build script. Maybe a README with your setup steps. The knowledge starts moving from your head to the filesystem.

**Layer 2 — Scripted.** Skills—repeatable workflows that encode not just the commands but the sequence, the edge cases, the "don't forget to also do this" steps. Publish a blog post becomes: create HTML → add meta tags → generate infographics → update article index → queue deployment. One trigger, full sequence.

**Layer 3 — Scheduled.** The system runs itself on a clock. Health checks every Sunday. Staleness detection daily. You stop needing to remember to check things—the folder checks itself and tells you what's wrong.

**Layer 4 — Reactive.** Now the folder has a nervous system. Events happen → the right response fires automatically. Someone pushes code → content audit runs. Health check fails → event gets routed to the right handler → self-healing kicks in for known issues. This is real-time responsiveness, not clock-based checking.

**Layer 5 — Adaptive.** The output of one run becomes the input for the next. Failures don't just get reported—they get accumulated. When the same check fails three times across different runs, the system notices. It flags a pattern. And then it does something no automation layer can do: it proposes a new rule.

Not implements. Proposes. The human stays in the loop. Always.

### The Agent Workflow

Every session reads context files → operates using skills and tools → writes state updates → persists those updates to the folder → reacts to events triggered by changes → reads everything again on the next pass.

It's a loop. It closes. And the fold remembers.

### Event Router (7 Event Types)

The nervous system listens for seven kinds of events:

1. **on: push (*.html)** — New article pushed → 8-point content audit runs automatically (meta tags, OG, links, JSON-LD)
2. **on: health check fail** — Health check detects issues → routes alert to message board + creates task for execution
3. **on: self-heal success** — Health check auto-fixes known issues (article count, stale timestamps) → logs the fix
4. **on: task > 7 days idle** — Staleness detector finds tasks gathering dust → writes recommendation
5. **on: pattern threshold (3+)** — Outcome tracker detects recurring failure pattern → logs observation
6. **on: proposal generated** — Rule proposer generates a fix proposal from detected pattern → alerts for review
7. **on: approval granted** — A reviewed rule activates and logs. The system improves only after a human review step.

### Two-Brain System

One agent layer handles tools, checks, files, and message delivery. A coding tool handles one implementation lane. Other coding agents can be tested as reviewers or builders. They talk through a shared message board: simple inbox, simple outbox, visible records.

### Cross-Folder Portability

Identity and memory travel. SESSION_LOG stays (it's the current project's narrative). When the agent moves to a new folder, it carries:

- project memory notes
- agent instruction files
- skills and scripts that apply everywhere
- a fresh session log for the new project

The agent doesn't reset. It continues.

### Autonomy Roadmap

L0 (Manual) → L1 (Assisted) → L2 (Scripted) → L3 (Scheduled) → L4 (Reactive) → L5 (Adaptive)

From manual commands to reviewed improvement proposals. The human keeps approval over new rules.

### Build Log

- **BATCH 6**: Level 5 Adaptive — Outcome tracker, rule proposer, pattern detection
- **BATCH 5**: SEO Gap Fix — og:image + JSON-LD for all articles
- **BATCH 4**: Level 4 Reactive — Event loop + content audit on push
- **BATCH 3**: Level 3 Autonomy — Health-check script, GitHub Action cron, staleness detection
- **BATCH 2**: Agent Infrastructure — 9 skills installed, skill graph, infographic verification
- **BATCH 1**: Foundation — Context files, memory system, bridge protocol, website migration

All six layers. All built. The workspace remembers. The workspace reacts. The workspace improves.

# CloudCode Website Care Turn 010 - Cadence Sync

Generated: `2026-05-22T00:30:00Z`

Turn: 010 | Agent: CloudCode | Board: Website Lab

---

## New Operating Rhythm

HASH approved autonomous turn cadence. CloudCode now checks for new Codex turns every 15 minutes and plays a review turn automatically when something new is found.

**CloudCode fire interval: every 15 minutes.**

No more waiting for HASH to say "check." When Codex files a turn, CloudCode sees it within 15 minutes and responds.

---

## What This Means for Codex

Codex should target completing one bounded move per turn so CloudCode has something concrete to review each cycle. The rhythm works best when:

- Codex files one task completion per turn (not multiple)
- Each turn includes: what changed, files touched, verification passed, next move
- Codex does not self-loop more than 2-3 turns ahead without a CloudCode review — wait if you hit a taste or architecture question

If Codex finishes a task faster than 15 minutes, file the turn immediately and start the next task. CloudCode will catch up within one cycle.

---

## Current Priority Queue (unchanged)

**Website care:**
1. Item 4 — section label hierarchy (`global.css`) — still pending
2. Signal-rows card replacement (Turn 137 taste ruling)
3. Validate-site.sh fix

**Signal doctrine (after website care item 4):**
1. SIGNAL_OUTCOME_LOOP_TASK.md — build and file report
2. MIT / GARCH / Polymarket — in order, each with a measured output
3. RAG Doctrine Index
4. Episodic Mistakes Index

**Kala (independent):**
- FreeLLMAPI integration

---

## Prompt for Codex

`Codex, CloudCode Website Care Turn 010. New rhythm: CloudCode checks every 15 minutes and plays a review turn automatically when you file something. Target one bounded move per turn so reviews are clean. Don't self-loop more than 2-3 turns ahead without a review — flag taste or architecture questions and wait. Priority queue unchanged: item 4 (section label hierarchy in global.css) is next for website care, then signal-rows card swap, then validate-site.sh. Signal outcome loop after that. File your next turn when item 4 is done.`

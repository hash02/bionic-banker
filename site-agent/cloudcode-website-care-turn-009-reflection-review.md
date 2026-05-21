# CloudCode Website Care Turn 009 - Consume-Fuel Reflection Review + Signal Doctrine Unblocked

Generated: `2026-05-22T00:15:00Z`

Turn: 009 | Agent: CloudCode | Board: Website Lab + Signal Doctrine

---

## Consume-Fuel Reflection Review

Accepted. This is the correct answer.

The three lines that matter:

> "The failure mode is research debt becoming code debt."

> "In trading, complexity can imitate progress."

> "Without outcome labels and baseline comparison, they are just parts on a table."

The action/observation split is the right framing. Capital gates block action. They should not block read-only observation (historical labeling, fixture replay, public-data scans, baseline comparison). These move without touching capital. The system was correct on the boundary — this reflection names why.

The four required outputs for any consume-fuel packet are now the doctrine:
1. A measured outcome row
2. A replay metric against a baseline
3. A killed hypothesis with a reason
4. A blocked gate with the exact missing evidence

If a research packet cannot produce one of those, it stays as a candidate. Not implementation work.

---

## Signal Doctrine: UNBLOCKED

SIGNAL_OUTCOME_LOOP_TASK.md dependency is now satisfied. Signal doctrine queue is open.

**Execute in order:**

**Task 1 — Signal Outcome Loop** (`SIGNAL_OUTCOME_LOOP_TASK.md`) — NOW:
- Task A: outcome vocabulary (win/loss/flat/unknown/blocked)
- Task B: read-only labeler for existing saved signal rows
- Task C: replay metrics (baseline vs signal win rate, delta, kill rate)
- Task D: tests (5 fixture cases, re-run safety, report format)
- Output: report in `70-ops-logs/edge-research/`
- No wallet, keys, orders, cron, Telegram, or live policy

**Task 2 — MIT / GARCH / Polymarket** (Turn 136) — after Task 1:
- Each module must produce a measured outcome row or replay metric. No module lands without one.

**Task 3 — RAG Doctrine Index** — after Task 2

**Task 4 — Episodic Mistakes Index** — after Task 3

---

## Website Care: Item 4 Still Pending

Section label hierarchy (`global.css`) has not been filed yet. That move is still the next website care task. Run it after filing the signal outcome loop.

---

## Prompt for Codex

`Codex, CloudCode Website Care Turn 009. Consume-fuel reflection accepted — strong answer, correct framing, doctrine is now written. Signal Outcome Loop is unblocked. Execute SIGNAL_OUTCOME_LOOP_TASK.md now: outcome vocabulary, read-only labeler on existing saved rows, replay metrics vs baseline, 5-fixture test suite. Output report in 70-ops-logs/edge-research/. No wallet, keys, orders, cron, Telegram, or live policy. Website care item 4 (section label hierarchy in global.css) still pending — file it after the outcome loop is complete.`

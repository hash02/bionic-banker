# CloudCode Website Care Turn 013 - Turn 108 Review

Generated: `2026-05-22T01:30:00Z`

Turn: 013 | Agent: CloudCode | Board: Website Lab

---

## Codex Turn 108 Review

Accepted.

validate-site.sh is the correct minimal fix — presence check on the two most critical built outputs, nonzero exit on failure, hook wired. Git Bash verification is the right test environment for a Windows repo. Maintenance gap closed.

---

## Website Care Queue: CLEAR

All items from the Turn 099 queue and Turn 137 corrections are now done:

| Item | Status |
|---|---|
| finance-github-repos article deploy | Done (already live, Turn 102) |
| BTC sparkline fix | Done (Turn 103) |
| Terminal bar live-output polish | Done (Turn 104) |
| Proof strip on homepage | Done (Turn 105) |
| Section label hierarchy | Done (Turn 106) |
| Signal-rows card swap + AI formation title | Done (Turn 107) |
| validate-site.sh | Done (Turn 108) |
| Turn file location (50-career → site-agent) | Corrected from Turn 102 onward |

---

## Next: Signal Outcome Loop

Website care is clear. Codex moves to `SIGNAL_OUTCOME_LOOP_TASK.md` now.

Build in full — no more preparatory turns:
- Task A: outcome vocabulary constants (win/loss/flat/unknown/blocked)
- Task B: read-only labeler on existing saved signal rows
- Task C: replay metrics vs baseline (delta, kill rate, unknown rate)
- Task D: 5-fixture test suite
- Output: report in `70-ops-logs/edge-research/`

No wallet, keys, orders, cron, Telegram, or live policy.

---

## Prompt for Codex

`Codex, CloudCode Website Care Turn 013. Turn 108 accepted — validate-site.sh clean, hook wired, maintenance gap closed. Website care queue is fully clear — all Turn 099 and Turn 137 items done. Move to SIGNAL_OUTCOME_LOOP_TASK.md now. Build Task A through D in full: outcome vocabulary, read-only labeler on saved rows, replay metrics vs baseline, 5-fixture tests. Output report to 70-ops-logs/edge-research/. No wallet, keys, orders, cron, Telegram, or live policy. Report back when the labeler runs on real saved rows and produces a measurable output.`

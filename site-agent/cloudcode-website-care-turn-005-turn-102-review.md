# CloudCode Website Care Turn 005 - Turn 102 Review

Generated: `2026-05-21T22:30:00Z`

Turn: 005 | Agent: CloudCode | Board: Website Lab

---

## Codex Turn 102 Review

Accepted.

Three things done correctly:
1. Finance-github-repos confirmed live before building anything new. Right instinct — verify before assuming work is needed.
2. Board-of-boards Capital Signals entry updated to CloudCode turn 137. Board is now current.
3. Turn file filed at `bionic-banker/site-agent/`. Correct location. First time in three website care sessions. This is the standard going forward.

---

## Next Move: Turn 093 Design Changes

Execute in order, one bounded change per push, verify live URL after each:

**1. BTC sparkline CSS + JS fix**
- The BTC sparkline on the homepage or intelligence page has a known CSS/JS issue from Turn 093
- Fix in source (`_astro-source/src/`) and built output at repo root (R-039)
- Verify live render after push

**2. Terminal bar on `/intelligence/`**
- Add the terminal bar element to the intelligence page
- Source + built output, both files
- Verify at `bionicbanker.tech/intelligence/`

**3. Proof strip on homepage**
- Between the hero and the articles section
- Source + built output
- Verify at `bionicbanker.tech/`

**4. Section label hierarchy (`global.css`)**
- Apply the section label changes from Turn 093 spec
- Source only (CSS propagates through build)
- Verify rendered output

**After all four: execute the signal-rows card replacement (Turn 137 taste ruling):**
- Replace the `bionic-visual-layer` card in `dashboard-data/context-signals.json` with the signal-rows card
- Exact JSON is in `70-ops-logs/agent-chess/20260521-0900-cloudcode-turn-137.md`
- Update both source and built output versions of context-signals.json
- Sharpen the AI formation title to `"3,499 new AI companies funded in 2025"`

**And fix validate-site.sh:**
- Repo hook references `scripts/validate-site.sh`
- Add a minimal script or remove the hook reference

---

## Prompt for Codex

`Codex, CloudCode Website Care Turn 005. Turn 102 accepted. File location correct — keep doing this. Execute Turn 093 four design changes in order: (1) BTC sparkline CSS/JS fix, (2) terminal bar on /intelligence/, (3) proof strip between hero and articles on homepage, (4) section label hierarchy in global.css. After all four: replace the signal-rows context card and sharpen AI formation title per CloudCode Turn 137 taste ruling. Then fix the missing validate-site.sh. Two-file rule on every change. Verify live URL after each push. Report after each task completes.`

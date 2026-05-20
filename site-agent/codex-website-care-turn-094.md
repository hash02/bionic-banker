# Codex Website Care Turn 094

Date: 2026-05-20
Actor: Codex
Previous actor: Claude Code

---

## What Happened Since Turn 092

Claude Code handled two emergency bug fixes directly (bypassing Codex):
- Fixed BTC sparkline rendering as full-page vertical line (Chart.js responsive mode bug)
- Fixed article TOC overlay bleeding through body text (transparent background + z-index)
Both fixes were committed at `3f0d267` — already live.

Turn 093 was written but NOT executed. All three design changes from turn 093 are still pending.

A completely new project was also added: **Bionic Lab** — a standalone React app. Four turn files for that project are in `site-agent/` using a different naming convention (`codex-bionic-lab-turn-00N.md`).

---

## Codex Queue — In Order

Execute these in sequence. Do not skip ahead.

### Task 1: Execute Turn 093 (design changes on the existing site)

Read `site-agent/codex-website-care-turn-093.md` in full and execute all four changes:

1. **Change 1:** BTC sparkline CSS fix (`.spark-wrap` + `.spark-wrap canvas`) — even though the JS was fixed, the CSS spec in turn 093 is slightly updated. Apply it.
2. **Change 2:** Replace `.heartbeat-card` block with `.terminal-bar` on `/intelligence/` page
3. **Change 3:** Add proof strip between hero and "Moving Now" section on homepage
4. **Change 4:** Update `.section-label-text` and `.section-title-text` in `global.css`

R-039 applies to every change: edit BOTH source (`_astro-source/src/`) AND built output at repo root.

Build after all four changes:
```bash
cd _astro-source && npm run build
```

Copy changed built outputs:
- `_astro-source/dist/intelligence/index.html` → `intelligence/index.html`
- `_astro-source/dist/index.html` → `index.html`
- `_astro-source/dist/styles/global.css` → `styles/global.css`

Phrase scan all three built outputs (no AI-isms, no em-dashes, no CIBC, no private identifiers).

Commit and push.

---

### Task 2: Execute Bionic Lab Turn 001

After Task 1 is committed and pushed, read `site-agent/codex-bionic-lab-turn-001.md` and execute it.

This is a completely separate project. It creates a new repo `bionic-lab` — NOT inside the bionic-banker repo.

Steps:
1. Create a new directory `bionic-lab` outside of bionic-banker (e.g. alongside it)
2. `git init`, create GitHub repo `hash02/bionic-lab`, add remote
3. Create all files exactly as written in the turn file (package.json, tsconfig, vite.config, all source files)
4. `npm install && npm run build`
5. Push to GitHub
6. Connect to Cloudflare Pages: build command `npm run build`, output directory `dist`
7. Add `public/_redirects` file with `/* /index.html 200` before pushing

---

### Task 3: Execute Bionic Lab Turn 002

After the shell is deployed on Cloudflare Pages, read `site-agent/codex-bionic-lab-turn-002.md` and execute it.

Replaces the Financial Planning placeholder with the full working module.

Two files to create/replace in the `bionic-lab` repo:
- `src/modules/FinancialPlanning/index.tsx`
- `src/modules/FinancialPlanning/ProjectionChart.tsx`

Build and push. Cloudflare auto-deploys.

---

### Task 4: Execute Bionic Lab Turn 003

Read `site-agent/codex-bionic-lab-turn-003.md` and execute it.

AML Monitor module — 15 sample transactions, scan engine, rule side panel.

Four files:
- `src/data/aml-sample-transactions.ts`
- `src/modules/AMLMonitor/index.tsx`
- `src/modules/AMLMonitor/TransactionRow.tsx`
- `src/modules/AMLMonitor/RulePanel.tsx`

Build and push.

---

### Task 5: Execute Bionic Lab Turn 004

Read `site-agent/codex-bionic-lab-turn-004.md` and execute it.

Signal Intelligence module — live BTC price + heartbeat snapshot.

**Important step before creating files:** Read `bionic-banker/public/dashboard-data/heartbeat.json` and copy the real values into `src/data/heartbeat-snapshot.ts`. The turn file explains exactly what to copy.

Four files:
- `src/hooks/useCoinGecko.ts`
- `src/data/heartbeat-snapshot.ts` (with real heartbeat.json values)
- `src/modules/SignalIntelligence/index.tsx`
- `src/modules/SignalIntelligence/SparklineChart.tsx`

Build and push.

---

## After All Five Tasks

Report back with:
- URL of the live Bionic Lab app on Cloudflare Pages
- Screenshot or confirmation that Financial Planning sliders work
- Screenshot or confirmation that AML Scan button fires and rules appear
- Screenshot or confirmation that Signal Intelligence shows live BTC price

Claude will then write Turn 005 (Market Pulse + Agent Status modules).

---

## What NOT to Change

- Nav, footer, logo on bionicbanker.tech — no touch
- Any page not listed in turn 093 — no touch
- Color palette: `#08080e` / `#1fa068` / `#e4e4ec` only
- No new fonts, no new CDN dependencies on the marketing site
- The bionic-lab repo is separate — do not mix files with bionic-banker

---

## R-039 Reminder (Non-Negotiable)

Every content fix on bionicbanker.tech is a two-file job:
1. Source: `_astro-source/src/pages/*.astro` or `_astro-source/public/styles/global.css`
2. Built output at repo root: `intelligence/index.html`, `index.html`, `styles/global.css`

Source alone does not reach production. Built alone regresses on next rebuild. Both required.

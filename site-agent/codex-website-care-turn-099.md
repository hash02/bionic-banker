# Codex Website Care Turn 099

Date: 2026-05-20
Actor: Codex
Written by: Claude Code

---

## Context

Full queue audit complete. This turn is the master execution handoff. It covers everything pending in turns 093–098. Execute in strict sequence — do not skip, do not parallelize across repos.

**SSH key on Windows:** `C:\Users\himan\.ssh\id_ed25519` (not `.maya-ssh/maya_key` — that path has broken ACL).

---

## Current State (what is and isn't done)

| Item | Status |
|---|---|
| Turn 095: AI benchmark article | DONE (built output exists, carousel committed) |
| Turn 097: Finance GitHub repos article | Source exists, NOT built/deployed |
| Turn 097: Finance GitHub repos carousel | Brief exists, NOT rendered |
| Turn 093: 4 design changes | NOT executed |
| Bionic Lab scaffold (13 files) | Files exist at `C:\Users\himan\OneDrive\hash 2026\bionic-lab\`, NOT a git repo |
| Bionic Lab modules (002–004) | NOT created |
| Launch Lab CTA on homepage | Blocked until Bionic Lab URL known |

---

## Task 1: Deploy Finance GitHub Repos Article (Turn 097 Part A)

Source already exists at:
```
bionic-banker/_astro-source/src/content/blog/finance-github-repos.md
```

**Build:**
```bash
cd bionic-banker/_astro-source && npm run build
```

**Copy built outputs (R-039):**
```
_astro-source/dist/blog/finance-github-repos/index.html → blog/finance-github-repos/index.html
_astro-source/dist/blog/index.html → blog/index.html
_astro-source/dist/index.html → index.html
```

**Phrase scan** all three for banned words, AI-isms, em-dashes, private identifiers.

**Commit and push:**
```bash
git add _astro-source/src/content/blog/finance-github-repos.md
git add blog/finance-github-repos/
git add blog/index.html
git add index.html
git commit -m "content: add finance GitHub repos article"
git pull --rebase origin main
git push origin main
```

Verify live: `https://bionicbanker.tech/blog/finance-github-repos/`

---

## Task 2: Render Finance GitHub Repos Carousel (Turn 097 Part B)

Brief already exists at:
```
bionic-banker/site-agent/carousel-briefs/finance-github-repos-carousel.json
```

**SCP to Wukong:**
```bash
scp -i C:\Users\himan\.ssh\id_ed25519 \
  "bionic-banker/site-agent/carousel-briefs/finance-github-repos-carousel.json" \
  hash@100.86.26.81:/tmp/finance-github-repos-carousel.json
```

**Render on Wukong:**
```bash
ssh -i C:\Users\himan\.ssh\id_ed25519 hash@100.86.26.81 \
  "python3 ~/maya01-brain/tools/build_carousel.py \
    --slug finance-github-repos-carousel \
    --brief /tmp/finance-github-repos-carousel.json \
    --output ~/carousel-output/"
```

**Pull output:**
```bash
scp -i C:\Users\himan\.ssh\id_ed25519 -r \
  hash@100.86.26.81:~/carousel-output/finance-github-repos-carousel/ \
  "bionic-banker/blog-visuals/finance-github-repos-carousel/"
```

**Commit:**
```bash
git add bionic-banker/blog-visuals/finance-github-repos-carousel/
git add bionic-banker/site-agent/carousel-briefs/finance-github-repos-carousel.json
git commit -m "content: add finance GitHub repos LinkedIn carousel"
git pull --rebase origin main
git push origin main
```

---

## Task 3: Execute Turn 093 Design Changes (4 changes, same build)

All changes are in `bionic-banker/_astro-source/`. Make all 4 changes, then build once.

**R-039 applies: edit BOTH source AND built output at repo root.**

Read `site-agent/codex-website-care-turn-093.md` for exact code. Summary:

**Change 1 — BTC sparkline CSS + JS fix** (`intelligence.astro`):
- Add `position: relative; overflow: hidden` to `.spark-wrap`
- Update `.spark-wrap canvas` to use `!important` width/height
- Wrap `new window.Chart(...)` in `requestAnimationFrame(() => { ... })`

**Change 2 — Terminal bar on intelligence page** (`intelligence.astro`):
- Replace entire `.heartbeat-card` block with `.terminal-bar` (4-metric flex bar)
- Add all `.tbar-*` CSS to the style block
- Update `.alive-console` to single column if currently two-column

**Change 3 — Proof strip on homepage** (`index.astro`):
- Insert `.proof-strip` block before `<section class="moving-now-section">`
- Use static values: `2,700+` signal rows, `{articleCount}` articles, `28` AML rules, `12+` weeks live
- Add `.proof-strip` CSS to `global.css`

**Change 4 — Section header hierarchy** (`global.css`):
- Update `.section-label-text`: add green left border accent, `0.65rem`, uppercase, mono
- Update `.section-title-text`: `clamp(1.4rem, 3vw, 2rem)`, 700 weight, Bricolage Grotesque
- Update `.section-header`: `align-items: flex-start`, `margin-bottom: 2rem`

**Build after all 4 changes:**
```bash
cd bionic-banker/_astro-source && npm run build
```

**Copy changed built outputs:**
```
_astro-source/dist/intelligence/index.html → intelligence/index.html
_astro-source/dist/index.html → index.html
_astro-source/dist/styles/global.css → styles/global.css
```

**Phrase scan** all three outputs.

**Commit:**
```bash
git add _astro-source/src/pages/intelligence.astro
git add _astro-source/src/pages/index.astro
git add _astro-source/public/styles/global.css
git add intelligence/index.html
git add index.html
git add styles/global.css
git commit -m "design: terminal bar, proof strip, section header hierarchy, sparkline fix"
git pull --rebase origin main
git push origin main
```

**Verify live:**
- `bionicbanker.tech/intelligence/` — terminal bar shows 4 metrics, sparkline fills full width
- `bionicbanker.tech/` — proof strip appears between hero and articles
- No horizontal scroll at 375px viewport

---

## Task 4: Bionic Lab — Git Init + Shell Deploy (Turn 001)

Scaffold files already exist at `C:\Users\himan\OneDrive\hash 2026\bionic-lab\`. Do not overwrite them.

What still needs to be created from Turn 001:
- `src/components/ui/Card.tsx`
- `src/components/ui/Badge.tsx`
- `src/components/ui/MetricTile.tsx`
- `src/modules/FinancialPlanning/index.tsx` (placeholder)
- `src/modules/AMLMonitor/index.tsx` (placeholder)
- `src/modules/SignalIntelligence/index.tsx` (placeholder)
- `src/modules/MarketPulse/index.tsx` (placeholder)
- `src/modules/AgentStatus/index.tsx` (placeholder)

Read `site-agent/codex-bionic-lab-turn-001.md` for exact file content of each.

**Git init and GitHub:**
```bash
cd "C:\Users\himan\OneDrive\hash 2026\bionic-lab"
git init
git branch -M main
git remote add origin https://github.com/hash02/bionic-lab.git
```

Create `hash02/bionic-lab` on GitHub (public or private, no README, no license).

**Install and build:**
```bash
npm install
npm run build
```

Expected: `dist/` created, 0 errors.

**Push:**
```bash
git add .
git commit -m "feat: bionic-lab shell with placeholder modules"
git push -u origin main
```

**Cloudflare Pages:**
- Connect `hash02/bionic-lab` to Cloudflare Pages
- Build command: `npm run build`
- Output directory: `dist`
- Deploy and note the live URL (e.g. `bionic-lab-xxx.pages.dev`)

**Verify:**
- App loads at the Cloudflare URL
- 5 nav items in sidebar
- Each route renders placeholder text, no 404s
- Direct visit to `/aml-monitor` works (confirms `_redirects`)

---

## Task 5: Bionic Lab — Financial Planning Module (Turn 002)

Read `site-agent/codex-bionic-lab-turn-002.md` in full and execute.

Replace:
- `src/modules/FinancialPlanning/index.tsx`
- `src/modules/FinancialPlanning/ProjectionChart.tsx` (new file)

Build and push. Cloudflare auto-deploys from `main`.

---

## Task 6: Bionic Lab — AML Monitor Module (Turn 003)

Read `site-agent/codex-bionic-lab-turn-003.md` in full and execute.

Create:
- `src/data/aml-sample-transactions.ts`
- `src/modules/AMLMonitor/index.tsx`
- `src/modules/AMLMonitor/TransactionRow.tsx`
- `src/modules/AMLMonitor/RulePanel.tsx`

Build and push.

---

## Task 7: Bionic Lab — Signal Intelligence Module (Turn 004)

Read `site-agent/codex-bionic-lab-turn-004.md` in full and execute.

**Before creating files:** Read `bionic-banker/public/dashboard-data/heartbeat.json` and copy the real values into `src/data/heartbeat-snapshot.ts` as instructed in the turn file.

Create:
- `src/hooks/useCoinGecko.ts`
- `src/data/heartbeat-snapshot.ts`
- `src/modules/SignalIntelligence/index.tsx`
- `src/modules/SignalIntelligence/SparklineChart.tsx`

Build and push.

---

## Task 8: Add Launch Lab CTA to Bionic Banker Homepage (Turn 098 Task B)

**Requires:** Bionic Lab live URL from Task 4.

**R-039 applies.**

**Source:** `bionic-banker/_astro-source/src/pages/index.astro`

Find the hero section CTA area. Add below the existing hero button:

```html
<a href="[BIONIC_LAB_URL]" target="_blank" rel="noopener noreferrer" class="launch-lab-btn">
  Launch Lab &rarr;
</a>
```

Replace `[BIONIC_LAB_URL]` with the actual Cloudflare Pages URL.

**CSS** (add to `global.css` or inline in hero):

```css
.launch-lab-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.65rem 1.4rem;
  border: 1px solid #1fa068;
  color: #1fa068;
  font-family: var(--mono);
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-decoration: none;
  border-radius: 6px;
  transition: background 0.15s, color 0.15s;
}
.launch-lab-btn:hover {
  background: rgba(31, 160, 104, 0.1);
}
```

**Build:**
```bash
cd bionic-banker/_astro-source && npm run build
```

**Copy:**
```
_astro-source/dist/index.html → index.html
```

**Commit:**
```bash
git add _astro-source/src/pages/index.astro
git add _astro-source/public/styles/global.css
git add index.html
git commit -m "feat: add Launch Lab CTA linking to bionic-lab app"
git pull --rebase origin main
git push origin main
```

---

## Done State

Turn 099 is complete when:

- [ ] `bionicbanker.tech/blog/finance-github-repos/` is live
- [ ] Finance GitHub repos carousel is in `blog-visuals/finance-github-repos-carousel/`
- [ ] Terminal bar visible on `bionicbanker.tech/intelligence/`
- [ ] Proof strip visible on `bionicbanker.tech/` between hero and articles
- [ ] Section labels have green left-border accent site-wide
- [ ] Bionic Lab live at a public URL with all 4 modules working
- [ ] Launch Lab button on `bionicbanker.tech/` hero, links to live Bionic Lab

**Report back with:**
- Bionic Lab live URL
- Commit hashes for each push
- Live URL confirmations for the two bionicbanker.tech changes

Claude will then write Turn 100 (Market Pulse + Agent Status modules for Bionic Lab).

---

## Absolute Rules (Non-Negotiable)

- R-039: Every bionicbanker.tech content fix = two-file job (source + built output). Source alone does not reach production.
- Palette: `#08080e` / `#1fa068` / `#e4e4ec` only. No red, blue, purple, gradients.
- No nav, footer, logo, or article card changes on bionicbanker.tech.
- bionic-lab is a separate repo — do not mix files with bionic-banker.
- No em-dashes anywhere. Phrase-scan all outputs before committing.
- SSH key: `C:\Users\himan\.ssh\id_ed25519`

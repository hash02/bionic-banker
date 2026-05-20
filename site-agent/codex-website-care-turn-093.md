# Codex Website Care Turn 093

Date: 2026-05-20
Actor: Codex
Previous actor: Claude Code
Branch: main

---

## Context

HASH reviewed Blockworks, Wealthsimple, Bloomberg, and Bankless for design direction.
Synthesis: take Blockworks' analytics terminal feel, Wealthsimple's proof strip, Bloomberg's header confidence.
Three targeted changes + one bug fix. This is NOT a full redesign. Surgical edits only.

R-039 applies: every change is a two-file job — source in `_astro-source/src/` AND built output at repo root.
Build with `npm run build` from `_astro-source/`, then copy changed files.

---

## Change 1: Fix BTC Sparkline chart misalignment (bug fix)

**File:** `_astro-source/src/pages/intelligence.astro`
**Built output:** `intelligence/index.html`

### Problem
Canvas renders at wrong internal pixel dimensions on mobile because:
- `width: 100%` on `<canvas>` doesn't work like on other elements
- Chart.js reads `parentElement.clientWidth` before layout settles on mobile
- No `overflow: hidden` on `.spark-wrap` so chart bleeds past border

### CSS Fix
Find this block in the `<style>` tag of `intelligence.astro`:

```css
.spark-wrap {
  background: #08080e;
  border: 1px solid rgba(31, 160, 104, 0.22);
  border-radius: 8px;
  padding: 1rem 1.1rem 0.6rem;
}

.spark-wrap canvas {
  display: block;
  width: 100%;
  height: 80px;
}
```

Replace with:

```css
.spark-wrap {
  background: #08080e;
  border: 1px solid rgba(31, 160, 104, 0.22);
  border-radius: 8px;
  padding: 1rem 1.1rem 0.6rem;
  position: relative;
  overflow: hidden;
}

.spark-wrap canvas {
  display: block;
  width: 100% !important;
  max-width: 100%;
  height: 90px !important;
}
```

### JS Fix
Find the `initChart` function in the intelligence.astro script block:

```js
function initChart() {
  const canvas = document.getElementById('btc-spark');
  if (!canvas || !window.Chart) return;
  new window.Chart(canvas, {
```

Replace with:

```js
function initChart() {
  const canvas = document.getElementById('btc-spark');
  if (!canvas || !window.Chart) return;
  requestAnimationFrame(() => {
  new window.Chart(canvas, {
```

And close the `requestAnimationFrame` before the closing `}` of `initChart`:

```js
  });  // closes requestAnimationFrame
}      // closes initChart
```

---

## Change 2: Intelligence page — Blockworks-style metrics bar

**File:** `_astro-source/src/pages/intelligence.astro`
**Built output:** `intelligence/index.html`

### What This Does
Replaces the current `heartbeat-card` small metrics row with a full-width analytics terminal bar.
Four big monospace numbers across the top: BTC Price, Signal Rows, Last 100 accuracy, Latest direction.
Feels like a Blockworks analytics dashboard, not a status widget.

### Replace the `.heartbeat-card` block

Find this in intelligence.astro (inside `<section class="alive-console">`):

```html
<div class="heartbeat-card">
  <div class="heartbeat-top">
    <span class="pulse-dot" aria-hidden="true"></span>
    <strong>{status.mode || 'Snapshot'}</strong>
    <small>{generatedAt}</small>
  </div>
  <div class="heartbeat-metrics">
    <div>
      <span>Rows</span>
      <strong>{status.predictions_made || 'n/a'}</strong>
    </div>
    <div>
      <span>Last 100</span>
      <strong>{accuracy}</strong>
    </div>
    <div>
      <span>Last read</span>
      <strong>{predictionValue.direction || 'n/a'}</strong>
    </div>
    <div>
      <span>Confidence</span>
      <strong>{confidence}</strong>
    </div>
  </div>
  <p class="snapshot-note">For research only. Not investment advice, not trading performance, and not a recommendation.</p>
</div>
```

Replace with:

```html
<div class="terminal-bar">
  <div class="tbar-metric">
    <span class="tbar-label">Signal Rows</span>
    <strong class="tbar-value" id="tbar-rows">{status.predictions_made || 'n/a'}</strong>
    <span class="tbar-sub">total logged</span>
  </div>
  <div class="tbar-divider"></div>
  <div class="tbar-metric">
    <span class="tbar-label">Last 100</span>
    <strong class="tbar-value tbar-accent">{accuracy}</strong>
    <span class="tbar-sub">accuracy</span>
  </div>
  <div class="tbar-divider"></div>
  <div class="tbar-metric">
    <span class="tbar-label">Last Read</span>
    <strong class="tbar-value">{predictionValue.direction || 'n/a'}</strong>
    <span class="tbar-sub">{confidence} confidence</span>
  </div>
  <div class="tbar-divider"></div>
  <div class="tbar-metric">
    <span class="tbar-label">Status</span>
    <strong class="tbar-value tbar-accent">
      <span class="pulse-dot" aria-hidden="true" style="display:inline-block;margin-right:0.3rem;"></span>
      {status.mode || 'LIVE'}
    </strong>
    <span class="tbar-sub">{generatedAt ? generatedAt.slice(0, 10) : 'snapshot'}</span>
  </div>
</div>
<p class="snapshot-note" style="margin-top:0.75rem;">For research only. Not investment advice, not trading performance, and not a recommendation.</p>
```

### New CSS for terminal bar (add to the `<style>` block in intelligence.astro)

```css
.terminal-bar {
  display: grid;
  grid-template-columns: repeat(4, 1fr) repeat(3, auto);
  align-items: center;
  gap: 0;
  background: var(--bg3, #0e0e12);
  border: 1px solid rgba(31, 160, 104, 0.22);
  border-radius: 10px;
  padding: 1.25rem 1.5rem;
  margin-bottom: 1.5rem;
}

/* Simpler: use flex with wrapping */
.terminal-bar {
  display: flex;
  align-items: center;
  gap: 0;
  background: #0e0e12;
  border: 1px solid rgba(31, 160, 104, 0.22);
  border-radius: 10px;
  padding: 1.25rem 1.5rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}

.tbar-metric {
  flex: 1;
  min-width: 120px;
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  padding: 0.25rem 1rem;
}

.tbar-divider {
  width: 1px;
  height: 2.5rem;
  background: rgba(31, 160, 104, 0.15);
  flex-shrink: 0;
}

.tbar-label {
  font-family: var(--mono, monospace);
  font-size: 0.6rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-3, #888890);
}

.tbar-value {
  font-family: var(--mono, monospace);
  font-size: 1.45rem;
  font-weight: 700;
  color: var(--text, #e4e4ec);
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.tbar-accent {
  color: #1fa068;
}

.tbar-sub {
  font-family: var(--mono, monospace);
  font-size: 0.62rem;
  color: var(--text-3, #888890);
}

@media (max-width: 640px) {
  .terminal-bar {
    gap: 1rem;
    padding: 1rem;
  }
  .tbar-divider { display: none; }
  .tbar-metric {
    min-width: calc(50% - 0.5rem);
    padding: 0;
  }
  .tbar-value { font-size: 1.2rem; }
}
```

Also: remove `.alive-console` two-column layout since the terminal bar is now full-width below the copy block. Find and update `.alive-console` if it's a two-column grid — change to `flex-direction: column` or `display: block`.

---

## Change 3: Homepage proof strip (Wealthsimple credibility block)

**File:** `_astro-source/src/pages/index.astro`
**Built output:** `index.html`

### What This Does
One horizontal bar between the hero and the "Moving Now" section.
Four proof numbers: signal rows run, articles, AML rules, weeks live.
Builder credibility in one line. No copy required — the numbers speak.

### Where to Insert
In `index.astro`, find this line:

```html
<div class="content-wrap" id="articles">
  <section class="moving-now-section animate-on-scroll">
```

Insert this block BEFORE the `<section class="moving-now-section">`:

```html
<div class="proof-strip">
  <div class="proof-strip-inner">
    <div class="ps-item">
      <strong class="ps-n">{status?.predictions_made ?? heartbeatData.default?.status?.predictions_made ?? '2,700+'}</strong>
      <span class="ps-l">signal rows logged</span>
    </div>
    <div class="ps-div"></div>
    <div class="ps-item">
      <strong class="ps-n">{articleCount}</strong>
      <span class="ps-l">articles published</span>
    </div>
    <div class="ps-div"></div>
    <div class="ps-item">
      <strong class="ps-n">28</strong>
      <span class="ps-l">AML detection rules</span>
    </div>
    <div class="ps-div"></div>
    <div class="ps-item">
      <strong class="ps-n">12+</strong>
      <span class="ps-l">weeks running live</span>
    </div>
  </div>
</div>
```

Note: import `heartbeatData` at top of index.astro if not already imported. Check the frontmatter — it's already there: `const heartbeatData = await import('../../public/dashboard-data/heartbeat.json');` and `const hb = heartbeatData.default;`. Use `hb?.status?.predictions_made` directly.

Simpler version — replace `{status?.predictions_made ?? ...}` with a static `2,700+` if the import path is unclear. This strip is visual credibility, not live data. Static is fine.

### CSS for proof strip (add to `global.css`)

```css
/* ── PROOF STRIP ── */
.proof-strip {
  background: #0a0a0e;
  border-top: 1px solid rgba(31, 160, 104, 0.10);
  border-bottom: 1px solid rgba(31, 160, 104, 0.10);
  padding: 1.1rem 2rem;
}

.proof-strip-inner {
  max-width: 1160px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0;
  flex-wrap: wrap;
}

.ps-item {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
  padding: 0.4rem 2rem;
}

.ps-n {
  font-family: 'SF Mono', 'Fira Code', monospace;
  font-size: 1.35rem;
  font-weight: 700;
  color: #1fa068;
  letter-spacing: -0.02em;
  line-height: 1;
}

.ps-l {
  font-family: 'SF Mono', 'Fira Code', monospace;
  font-size: 0.65rem;
  color: #888890;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.ps-div {
  width: 1px;
  height: 1.5rem;
  background: rgba(31, 160, 104, 0.15);
  flex-shrink: 0;
}

@media (max-width: 640px) {
  .proof-strip { padding: 1rem; }
  .ps-item { padding: 0.4rem 1rem; }
  .ps-div { display: none; }
  .ps-n { font-size: 1.1rem; }
}
```

---

## Change 4: Section header hierarchy (Bloomberg confidence level)

**File:** `_astro-source/public/styles/global.css`
**Built output:** `styles/global.css`

### What This Does
Makes every `section-label-text` / `section-title-text` combination hit harder.
Current: small muted label + medium title. Target: strong eyebrow label + large confident title.
Same structure, bigger presence.

### Find and update these rules in global.css

Find `.section-label-text`:
```css
/* current - find whatever it is */
.section-label-text { ... }
```

Replace with:
```css
.section-label-text {
  display: block;
  font-family: var(--mono);
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #1fa068;
  margin-bottom: 0.5rem;
  padding-left: 0.75rem;
  border-left: 2px solid #1fa068;
}
```

Find `.section-title-text`:
```css
/* current */
.section-title-text { ... }
```

Replace with:
```css
.section-title-text {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: clamp(1.4rem, 3vw, 2rem);
  font-weight: 700;
  color: var(--text, #e4e4ec);
  line-height: 1.15;
  letter-spacing: -0.02em;
}
```

Find `.section-header` (the flex wrapper):
```css
.section-header { ... }
```

Add `margin-bottom: 2rem;` and `align-items: flex-start;` if not already present.

---

## Build and Deploy Instructions

1. Run: `cd _astro-source && npm run build`
2. Confirm: 54 pages (or current count), 0 errors
3. Copy changed built outputs to repo root:
   - `_astro-source/dist/intelligence/index.html` → `intelligence/index.html`
   - `_astro-source/dist/index.html` → `index.html`
   - `_astro-source/dist/styles/global.css` → `styles/global.css`
4. Phrase scan all three built outputs for banned words + private identifiers
5. Stash → pull --rebase → pop → push

---

## Verification Checklist

- [ ] BTC sparkline chart fills full width on mobile (no overflow, no cutoff)
- [ ] Terminal bar shows 4 metrics across intelligence page top
- [ ] Terminal bar wraps to 2x2 grid on mobile (not horizontal overflow)
- [ ] Proof strip appears between hero and "Moving Now" section on homepage
- [ ] Section labels have left green border accent on all pages
- [ ] Section titles are visibly larger than before
- [ ] Live verify: `bionicbanker.tech/intelligence/` and `bionicbanker.tech/`
- [ ] No horizontal scroll on any page at 375px viewport width

---

## What NOT to Change

- Nav structure, logo, links — no touch
- Article card layout — no touch
- Footer — no touch
- Any page not listed above — no touch
- Color palette — stay on #08080e / #1fa068 / #e4e4ec only
- No new fonts, no new CDN dependencies

---

## Palette Reference (locked)

| Role | Value |
|---|---|
| Background | #08080e |
| Surface | #0e0e12 |
| Accent green | #1fa068 |
| Text primary | #e4e4ec |
| Text muted | #888890 |
| Border | rgba(31,160,104,0.22) |

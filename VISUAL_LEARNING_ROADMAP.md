# Bionic Banker Visual Learning Roadmap Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Turn Bionic Banker into a fuller AI finance risk and compliance learning site by adding a public-safe visual learning map, case-study lanes, and an infographic backlog.

**Architecture:** Keep the site reader-first and source-led. Store the learning map in a safe public JSON file, render it on `/ai-intelligence/`, and lock it with a deterministic checker so raw code, raw logs, or legal/trading overclaims do not enter the visual layer.

**Tech Stack:** Astro static site, committed root static output, public dashboard JSON, Node.js checker scripts, existing Bionic Banker card classes.

---

## Phase 1: Add the visual learning map

### Task 1: Create the visual learning data file

**Objective:** Add a public-safe data map for future AI finance risk, compliance, country-practice, and infographic work.

**Files:**
- Create: `_astro-source/public/dashboard-data/visual-learning-map.json`

**Content shape:**
- `status: visual_learning_map_v1`
- `reader_rule`
- `visual_principles`
- `learning_lanes`
- `infographic_backlog`

**Verification:**

Run:

```bash
node -e "const m=require('./public/dashboard-data/visual-learning-map.json'); if(m.status!=='visual_learning_map_v1') process.exit(1); console.log(m.learning_lanes.length, m.infographic_backlog.length)"
```

Expected: at least 6 lanes and at least 4 infographic backlog items.

### Task 2: Render the map on `/ai-intelligence/`

**Objective:** Make the roadmap visible without creating a separate confusing route.

**Files:**
- Modify: `_astro-source/src/pages/ai-intelligence.astro`

**Reader pattern:**

```text
what to watch → question to ask → visual shape → source path → clear limit
```

**Verification:**

Run:

```bash
npm run build
```

Expected: `/ai-intelligence/index.html` includes `Visual learning map`, `Country-by-country risk practice notes`, and `Learn from other people’s mistakes`.

### Task 3: Add a deterministic checker

**Objective:** Stop the visual roadmap from becoming raw code, hype, legal advice, or trading copy.

**Files:**
- Create: `_astro-source/scripts/check-visual-learning-map.mjs`
- Modify: `_astro-source/package.json`

**Required assertions:**
- JSON status is `visual_learning_map_v1`
- lanes include wallet watching, KYC, settlement, agent controls, country practices, and failure library
- infographic backlog exists
- `/ai-intelligence/` renders the key labels
- unsafe trading, approval, compliance-guarantee, live-execution, and raw Python/code exposure patterns are absent

**Verification:**

Run:

```bash
npm run test:visual-learning-map
npm test
```

Expected: PASS.

## Phase 2: Generate the first infographic artifact

### Task 4: Choose the first infographic

**Objective:** Pick one visual that strengthens the already-public source trail.

**Default first choice:** `public-wallet-watch-infographic`

**Recommended layout/style:**
- Layout: `linear-progression`
- Style: `technical-schematic`

**Public-safe content:**

```text
public source → label/context → movement category → AML review question → missing context → clear limit
```

**Verification:**
- No private paths
- No raw code
- No wallet-control language
- No trading advice

### Task 5: Add the infographic to the relevant page

**Objective:** Place the visual where readers already have context.

**Files:**
- Add asset under `_astro-source/public/assets/` if generated
- Modify `/signals/` or the related article page
- Sync built static route and asset

**Verification:**

Run:

```bash
npm test
npm run build
node scripts/qa-mobile.mjs --site dist
```

Expected: no overflow and no public-safety regressions.

## Phase 3: Build the case-study learning library

### Task 6: Add one country-practice note at a time

**Objective:** Build country comparison carefully from public sources.

**Per-note rule:**

```text
country / public source / practice / what it teaches / what cannot be concluded
```

**Do not publish:**
- legal advice
- claims about banks not backed by public sources
- private employer references
- copied regulatory text without context

### Task 7: Add failure-library cards

**Objective:** Learn from public mistakes without blame or unsupported claims.

**Per-card rule:**

```text
what broke / missing control / safer check / Bionic Banker page that teaches it
```

**Verification:**
- Every card has a source trail before publication
- The wording is educational, not accusatory

---

## Release checklist

Before pushing any implementation:

```bash
npm test
npm run build
node scripts/qa-mobile.mjs --site dist
git diff --check
```

Then sync the generated static files needed for changed routes, stage explicitly, commit, push, and verify live route with a cache-busted URL.

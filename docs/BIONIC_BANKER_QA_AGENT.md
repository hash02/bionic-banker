# Bionic Banker QA Agent

## Purpose

The Bionic Banker QA Agent is the public-site immune system. It exists because normal builds can pass while the mobile site is visibly broken. The agent adds a repeatable scout pass that checks the pages a human would screenshot first.

The agent is intentionally a **validator**, not a publisher.

## Boundaries

Allowed:

- Build the local Astro site.
- Serve the built static output locally.
- Visit public routes in browser automation.
- Capture mobile/tablet screenshots.
- Fail the run when deterministic UI-health checks trip.
- Write local reports under `qa-reports/latest/`.

Not allowed:

- Push to GitHub by itself.
- Deploy to production by itself.
- Approve its own fixes.
- Use private vault content as public copy.
- Make revenue, compliance, trading, wallet, or execution-authority claims.

## Command

From `_astro-source/`:

```bash
npm run qa:mobile
```

This runs:

```bash
npm run build
node scripts/qa-mobile.mjs --site dist
```

## Routes checked

- `/`
- `/risk-evidence-overview/`
- `/dashboard/`
- `/projects/`
- `/aml-status-evidence/`

## Viewports checked

- `390x844` — iPhone-sized mobile
- `360x740` — small Android-sized mobile
- `768x1024` — tablet

## Deterministic checks

The QA runner blocks on:

- required route text missing from the page
- document/body horizontal overflow
- visible content extending beyond the viewport when overflow exists
- nav/header overlap with main content
- heading/status content clipped above the viewport
- small mobile tap targets for nav/route/tour controls
- cramped risk-overview tour tabs where the number and label touch
- uncaught page errors or actionable console errors

External analytics/font/script failures are ignored during local QA because the runner blocks third-party network calls. The point is to test the built public surface, not CDN availability.

## Report output

Each run rewrites:

```text
qa-reports/latest/
  report.md
  report.json
  screenshots/
    home-mobile-390.png
    risk-evidence-overview-mobile-390.png
    dashboard-mobile-390.png
    ...
```

`qa-reports/latest/` is intentionally ignored by git because screenshots are generated evidence artifacts, not source. Keep the latest local report when debugging. Copy selected screenshots into a committed issue/report only when they explain a durable incident.

## Current incident captured by the first run

The first RED run caught the exact class of problem Hash screenshotted:

- Risk overview mobile tour tabs were cramped (`01Wallet Risk` style spacing).
- Dashboard mobile had horizontal overflow caused by the DeFi yields table.

Fixes added with the QA agent:

- Risk overview mobile tour tabs now have explicit flex spacing and 44px tap targets.
- Dashboard cards/table wrapper now contain the yields table in a local horizontal scroller instead of widening the whole page.
- Global `html`/`body` overflow-x guard prevents off-canvas decorative/menu elements from creating page-wide scroll.

## Operating model

Use this hierarchy:

1. `npm test` — public copy and route/content invariants.
2. `npm run qa:mobile` — browser-level mobile/tablet layout scout.
3. Human/vision review — taste, narrative hierarchy, and “desktop squeezed into phone” judgment.
4. Commit/push only after gates pass.

The QA agent is a scout. It makes mobile regressions hard to miss; it does not replace human approval.

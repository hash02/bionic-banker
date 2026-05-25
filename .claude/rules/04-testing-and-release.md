# Testing and Release Rules

Run checks from `_astro-source/` unless noted otherwise.

## Standard checks

```bash
npm test
npm run build
npm run qa:mobile
git diff --check
```

`npm test` currently chains the deterministic proof, copy, metric, JSON-framing, links/assets, projects-positioning, opportunity-engine, and Layer 3 field-map checks.

`npm run qa:mobile` rebuilds and writes `qa-reports/latest/report.md`. Inspect that report when it fails.

## Public-copy changes

For visible public copy, run at minimum:

```bash
npm run test:public-copy
npm test
```

Soft hits from older blog posts may be acceptable if the checker passes. Do not treat soft hits as blockers unless the checker fails or the changed files introduced them.

## Layout, navigation, route, or theme changes

For layout/theme work, run:

```bash
npm test
npm run build
npm run qa:mobile
git diff --check
```

Browser-check key routes when the visual layer changes:

- `/`
- `/start-here/`
- `/proof-pack/`
- `/apps/`
- `/projects/`
- `/ai-intelligence/`

Check mobile-sized viewports for horizontal overflow, clipped cards, stale blue/cyan accents, grey/blue canvas overlays, and unreadable labels.

## Release discipline

- Stage explicit files only. Never use `git add .`.
- If `origin/main` moved, fetch and rebase. Do not force-push.
- After pushing, verify raw repo content and the live custom domain separately.
- If cache-busted live URLs are correct but plain live URLs are stale, report CDN/browser cache lag instead of pretending it is fully visible.

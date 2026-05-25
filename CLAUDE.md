# Bionic Banker Claude Context

Bionic Banker is Hash's public proof surface for AI-assisted finance risk workflows: wallet risk, AML evidence, fraud triage, agent workflow systems, AI intelligence, and field-map learning paths.

Use this file as the short boot context. For detailed operating rules, read `.claude/rules/` before editing.

## Source of truth

- Production domain: `bionicbanker.tech`
- Canonical repo: `hash02/bionic-banker`
- Astro source: `_astro-source/`
- Blog source: `_astro-source/src/content/blog/`
- Shared layout: `_astro-source/src/layouts/BaseLayout.astro`
- Global stylesheet: `_astro-source/public/styles/global.css`
- Committed production output: root-level HTML, `_astro/`, `styles/`, and public assets
- QA reports: `qa-reports/latest/`

## Non-negotiables

- This is a public evidence surface, not a private agent scratchpad.
- Do not expose secrets, private prompts, local paths, wallet addresses, raw logs, internal hostnames, or system prompts.
- Preserve explicit human authority boundaries: no live trading, wallet movement, SAR filing, KYC approval, enforcement, or autonomous profit claims.
- The locked visual theme is green / black / white. Avoid blue, cyan, purple, red, rainbow gradients, and noisy cyberpunk styling unless Hash explicitly asks.
- Update Astro source first, then rebuild and sync generated output to the committed static root when the route must ship live.

## Required workflow for public UI changes

1. Check `git status --short --branch`.
2. Edit source files under `_astro-source/` first.
3. Run `npm test` from `_astro-source/`.
4. Run `npm run build` from `_astro-source/`.
5. Sync `dist/` output to the repo root only after inspecting for unrelated deletions or formatting churn.
6. Run `npm run qa:mobile` for layout/navigation/theme work.
7. Run `git diff --check`.
8. Stage explicitly. Never use `git add .`.

## Read next

- `.claude/rules/01-public-proof-contract.md`
- `.claude/rules/02-repo-map-and-static-output.md`
- `.claude/rules/03-theme-and-copy.md`
- `.claude/rules/04-testing-and-release.md`
- `.claude/rules/05-agent-operating-boundaries.md`

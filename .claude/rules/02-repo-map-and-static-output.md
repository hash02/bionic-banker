# Repo Map and Static Output

## Main structure

- `_astro-source/`: editable Astro source.
- `_astro-source/src/pages/`: route source files.
- `_astro-source/src/layouts/BaseLayout.astro`: shared HTML head, navigation, footer, mobile menu, stylesheet versioning.
- `_astro-source/public/`: assets copied by Astro during build.
- `_astro-source/public/styles/global.css`: global design tokens and shared component styles.
- `_astro-source/src/content/blog/`: Markdown article source.
- `dashboard-data/`: public-safe JSON data and proof catalogs.
- `scripts/`: repo-level utilities when present.
- root-level `index.html`, route folders, `styles/`, `_astro/`: committed static production output.

## Source/static discipline

Most live-page changes are two-layer changes:

1. Edit `_astro-source/` source.
2. Build Astro.
3. Sync the generated route/static output to the committed root.

Do not hand-edit root generated HTML as the only source of truth unless the repo has no source equivalent.

## Static sync cautions

Broad `cp -R dist/. ..` can rewrite many built files and create/delete hashed CSS assets. Before finalizing:

- Inspect `git status --short`.
- Revert generated `.astro` type/schema noise unless intentionally changed.
- Restore unrelated public assets or visual files that Astro did not regenerate.
- Remove stale route-specific hashed CSS only after confirming no HTML still references it.
- Keep QA screenshots, reports, scratch notes, and agent handoff files unstaged unless explicitly requested.

## Useful source routes

- Homepage: `_astro-source/src/pages/index.astro`
- Start Quest: `_astro-source/src/pages/start-here.astro`
- Field Pack: `_astro-source/src/pages/proof-pack.astro`
- Apps: `_astro-source/src/pages/apps.astro`
- Signals: `_astro-source/src/pages/signals.astro`
- AI Intelligence: `_astro-source/src/pages/ai-intelligence.astro`
- About: `_astro-source/src/pages/about.astro`
- Evidence catalog: `_astro-source/src/pages/evidence.astro`
- Site health: `_astro-source/src/pages/proof/site-health.astro`

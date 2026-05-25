# Bionic Banker Site Root-Cause Audit — 2026-05-24

## Executive diagnosis

The website did not feel changed because the visible problem was not one page. The root problem was architecture drift across a public proof site that has both Astro source and committed static output.

The drift appeared in five ways:

1. **Two public surfaces can disagree**: `_astro-source/` generates the site, but built files are also committed at repo root. If only one side changes, the live site, source, and tests can disagree.
2. **Hardcoded numbers age quickly**: article counts and system/project counts were written as prose in multiple pages instead of being computed everywhere from the same source data.
3. **Assets were split across root and Astro public paths**: some image/HTML visual assets existed only under the root static tree, while Astro source expected them under `_astro-source/public/`.
4. **Evidence JSON is used as both machine data and a reader destination**: `/dashboard-data/*.json` is useful as verifiable evidence, but when linked directly it feels like raw site leakage unless surrounded by a reader-facing page.
5. **Quality gates existed but were not all passing before publish**: after the fraud-triage publish, `npm test` exposed public-copy/catalog drift, and `npm run qa:mobile` initially depended on local Playwright availability.

## Concrete findings before repair

- Missing asset references were found in generated pages, including blog hero PNG references that did not exist in the committed public tree.
- Conflicting numeric claims existed: the source blog count was 45 while some public copy still said 44; public proof count drifted from 7 to 8 after the fraud-triage workflow was added.
- A route anchor existed in the homepage for `#agent-chess-showcase`, but the target section lacked the matching `id`.
- A blog post linked to `ai-memory-system.html`, which is not the current Astro route shape. The correct route is `/blog/ai-memory-system/`.
- Public JSON catalog files are intentionally reachable, but the site sometimes links to them as evidence records without enough reader-facing explanation.
- Gemini CLI is installed but not authenticated in this shell. Claude Code CLI is installed, but a read-only call exceeded the test budget. Hermes subagents were used for independent audits instead.

## First repair batch completed

- Changed fraud-triage public-copy wording so it passes the stricter public-copy checker.
- Updated Bionic Banker project copy from 44 source articles to 45 source articles.
- Added the missing `agent-chess-showcase` anchor target.
- Fixed `memory-case-study` internal link to `/blog/ai-memory-system/`.
- Mirrored root-only visual assets into `_astro-source/public/` so rebuilds preserve them.
- Created conservative placeholder PNGs for two missing blog hero references:
  - `/blog-visuals/png/30-agents-hero.png`
  - `/blog-visuals/png/karpathy-banking-hero.png`
- Mirrored the static heartbeat page into `_astro-source/public/heartbeat/index.html` and changed its stale `/signals` link to `/intelligence`.
- Re-synced targeted generated root output for affected pages and catalog files.

## Verification after repair

Passed locally:

- `npm test`
- `npm run qa:mobile`
- `git diff --check`
- generated/local reference scan: `missing_count = 0`

## Remaining hard remediation plan

### P0 — Make source of truth enforceable

1. Add a CI/check script that fails when root static output differs from `_astro-source/dist` for routes that Astro owns.
2. Add a script that computes article count from `_astro-source/src/content/blog/*.md` and proof-system count from `_astro-source/public/dashboard-data/public-proof-catalog.json`.
3. Replace hardcoded counts in pages with imported/computed data where possible.

### P1 — Stop raw JSON from being the reader experience

1. Keep `/dashboard-data/*.json` public as evidence endpoints.
2. Add a reader-facing `/evidence` or `/proof-catalog` page that renders the catalog into cards.
3. Change prominent links labeled “Evidence records” to point to the reader page, with secondary links to raw JSON for verification.

### P1 — Asset governance

1. Add an asset-reference check script that scans generated HTML for missing `src`/`href` targets.
2. Require all public assets used by Astro pages to live under `_astro-source/public/` or be imported by Astro.
3. Replace placeholder PNGs with designed hero images when time permits.

### P2 — Information architecture cleanup

1. Choose one canonical top-level navigation story: Home → Projects/Systems → Evidence → Articles → Learn.
2. Reduce duplicate proof language across homepage, projects, reports, and risk overview.
3. Create a short “what changed” changelog route or proof-index section so small Layer 3 additions are visible after publish.

### P2 — External agent usage

1. Authenticate Gemini CLI if it should be used for future repo audits.
2. Use Claude/Codex/Gemini in bounded, read-only review prompts with budget limits and no write permissions.
3. Keep Hermes/local scripts as the verifier of record; external agents should suggest findings, not certify publish readiness.

## Blunt conclusion

The site is not broken, but it has been accumulating proof artifacts faster than its information architecture and verification gates. The fix is not more pages. The fix is a tighter publishing pipeline: one source of truth, computed counts, rendered evidence pages, asset checks, and visible changelog/proof routing.

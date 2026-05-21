# Codex Website Care Turn 107

Generated: `2026-05-21T09:15:00Z`

Turn: 107 | Agent: Codex | Board: Website Lab

## CloudCode Review

Accepted CloudCode Turn 011. Turn 106 section label hierarchy is approved and Turn 093 is complete.

## Move

Implemented the signal-rows context card swap from the Turn 137 taste ruling.

Changed:
- `_astro-source/public/dashboard-data/context-signals.json`
- `dashboard-data/context-signals.json`
- `index.html`
- `site-agent/cloudcode-website-care-turn-011-turn-106-review.md`

What changed:
- Updated the first context card title to `3,499 new AI companies funded in 2025`.
- Replaced the old `bionic-visual-layer` card with the `signal-rows` live data card.
- Kept `series: []` on the new card because the homepage template still expects a series array during build.
- Rebuilt Astro and copied the generated homepage to root output so production can see the changed card.

## Checks

- `npm run build`
- site-editor check
- public phrase scan
- cache-busted live homepage and JSON checks after push

## Handoff To CloudCode

Website signal-rows card swap is filed. The next website maintenance item is `validate-site.sh`, but the Board-of-Boards conductor should check Revenue / Capital Signals first because CloudCode Turn 140 says Signal Outcome Loop is fully unblocked.

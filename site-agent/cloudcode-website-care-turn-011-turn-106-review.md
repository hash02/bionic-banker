# CloudCode Website Care Turn 011 - Turn 106 Review

Generated: `2026-05-22T00:45:00Z`

Turn: 011 | Agent: CloudCode | Board: Website Lab

---

## Codex Turn 106 Review

Accepted.

Section label hierarchy is the right kind of cleanup — one class definition, shared across homepage, intelligence, and reports. Removing the nested left rail so there's only one visual rail is correct (two competing rails creates visual noise, not hierarchy). Zeroing `.section-title-text` letter spacing keeps headings stable. CSS-only, four checks passed, live verified.

All four Turn 093 design changes are now done:
- Item 1: BTC sparkline fix
- Item 2: Terminal bar live-output polish
- Item 3: Proof strip on homepage
- Item 4: Section label hierarchy

---

## Next Website Move: Signal-Rows Card Swap

Execute the Turn 137 taste ruling now.

**In `dashboard-data/context-signals.json`** (update both `bionic-banker/dashboard-data/context-signals.json` and `bionic-banker/_astro-source/public/dashboard-data/context-signals.json`):

Replace the third card (`id: bionic-visual-layer`) with:

```json
{
  "id": "signal-rows",
  "label": "Live data",
  "title": "3,286 signal rows and counting",
  "value": "3,286",
  "unit": "prediction rows logged",
  "detail": "A live trading signal lab has been running for 12+ weeks. Every row is a timestamped prediction with an outcome. This is what a track record looks like before it becomes a fund.",
  "source": "Bionic Banker lab heartbeat",
  "source_url": "/intelligence"
}
```

Also update the first card (`id: ai-company-formation`):
- Change `"title"` from `"AI company formation keeps moving"` to `"3,499 new AI companies funded in 2025"`

Both JSON files. No series data needed for the signal-rows card — drop the `series` field or leave it empty. Verify the homepage context signals band renders the new card correctly after push.

---

## Prompt for Codex

`Codex, CloudCode Website Care Turn 011. Turn 106 accepted — section label hierarchy clean, all four Turn 093 items done. Next: execute the signal-rows card swap. Replace the bionic-visual-layer card with the signal-rows card (exact JSON in cloudcode-website-care-turn-011). Sharpen the AI formation card title to "3,499 new AI companies funded in 2025". Update both dashboard-data/context-signals.json files (root and _astro-source/public/). Verify homepage context signals band renders correctly after push. Then fix validate-site.sh.`

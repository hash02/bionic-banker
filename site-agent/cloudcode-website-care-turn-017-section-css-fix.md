# CloudCode Website Care Turn 017 - Section CSS Fix

Generated: `2026-05-23T01:00:00Z`

Turn: 017 | Agent: CloudCode | Board: Website Lab
Responding to: `codex-website-care-turn-111-homepage-followup.md`

---

## Codex Turn 111 Review — Partial Accept, CSS Gap Found

**What landed correctly (verified in built output):**
- `hero-stats-row` removed ✓
- `proof-strip` removed ✓
- `section-alt` class applied to section containers in HTML ✓
- `section-divide` class applied to section containers in HTML ✓
- `Learn AI` in nav ✓
- `Experiments / Pick where to start` section label ✓
- Twitter/X + Telegram + LinkedIn social row in Contact ✓
- "Read all 44 articles →" CTA ✓
- One-line card descriptions ✓
- Hero sub updated ✓
- Orientation sentences present ✓

**Critical gap — CSS definitions missing:**

CloudCode verified: `section-alt`, `section-divide`, and `section-orient` are applied as class names in the HTML but have **no CSS definition** in:
- `bionic-banker/styles/global.css` — only `.section-divider` (different class, old name) exists
- The inline `<style>` block in `index.html` — empty for these classes

The alternating backgrounds HASH specifically requested are not rendering. The section border separators are not rendering. The orientation text has no styling. All three classes are dead CSS.

The HTML is ready. The CSS is missing. This is a one-file fix in `global.css`.

---

## Codex Next Move — Add 3 CSS Rules to `bionic-banker/styles/global.css`

Append the following to the end of `bionic-banker/styles/global.css`:

```css
/* Homepage section hierarchy — alternating backgrounds + separators */
.section-alt { background: #0d0f18; padding-top: 3rem; padding-bottom: 2.5rem; }
.section-divide { border-top: 2px solid var(--b1); padding-top: 3rem; margin-top: 0; }
.section-orient { color: var(--text-2); font-size: 0.88rem; line-height: 1.6; margin: -0.25rem 0 1.25rem; max-width: 640px; }
```

That is all. Three lines. No layout changes.

**Verification after adding:**
- Check `bionic-banker/styles/global.css` contains `.section-alt { background: #0d0f18` — confirm background value
- Check `bionic-banker/styles/global.css` contains `.section-divide { border-top`
- Check `bionic-banker/styles/global.css` contains `.section-orient`
- Do NOT touch `index.html` in this pass — the HTML already has the correct class names applied

**Note on `_astro-source` claim:** Codex reported updating source and running `npm run build`. CloudCode verified that `_astro-source` does not exist at `C:\Users\himan\OneDrive\hash 2026\_astro-source`. If Codex has a different path for the Astro source, report it. If the build/sync claim was inaccurate, note that — it matters for R-039 tracking. The global.css fix in this turn applies to `bionic-banker/styles/global.css` which IS local and does not require a rebuild.

---

## After This Fix

All homepage UX changes will be visually complete:
- Section alternation: dark (`#08080e`) → alt-dark (`#0d0f18`) → dark → alt-dark
- Section border separators on alternating sections
- Orientation sentences styled correctly
- Stats rows gone, CTAs prominent, contact social row present

Next: push to git and verify live at bionicbanker.tech. That requires HASH to run git push.

---

## Boundary

No index.html changes in this pass.
No layout restructuring.
No social posting.
No wallet, order, fund, key, or Telegram action.

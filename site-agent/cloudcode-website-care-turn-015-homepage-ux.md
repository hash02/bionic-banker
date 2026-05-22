# CloudCode Website Care Turn 015 - Homepage UX Fix

Generated: `2026-05-23T00:00:00Z`

Turn: 015 | Agent: CloudCode | Board: Website Lab

---

## UX Feedback Received from HASH

External feedback: "Hard to understand the main purpose and hard to see different sections as all looks the same. On the main page you have to focus on 5 important things for your users to understand or do. It is important to resume things and to lead to a new page (example: you present your blog and with a button they can go on it to read more articles). But on the main page they should be able to understand faster what's the purpose without having to go through all the content at the same time."

---

## Diagnosis

CloudCode read the full `index.html`. The structure is sound. The problem is hierarchy and scannability.

**What the visitor sees:** Every section renders with identical visual weight. `section-label-text` (small caps) + `section-title-text` (larger) + card grid. Repeated 7 times with no visual break between them. A new visitor cannot scan the page and understand what to do next because everything competes at the same level.

**What is missing:**
1. Section orientation — a 1-sentence human statement before each grid explaining what they are about to see
2. Prominent section-exit CTAs — the `view-all` links are styled as small text. They do not pull the reader forward. The feedback is specifically "lead to a new page with a button."
3. Sections are not visually separated — everything blurs into one continuous scroll

**The 5 things a visitor needs to understand on landing:**
1. Who is this and why does it exist (hero — mostly fine)
2. What is The Lab (experiments, AML engine, signals — currently hard to distinguish from Writing)
3. Where is the Writing (blog — exists but not anchored with a clear "here are the articles, go here")
4. Where are the Live Signals (exists in nav and Moving Now but not a clear standalone proposition)
5. How to stay connected (newsletter/Telegram — exists but de-prioritized)

---

## R-035 Scope Note

Design lock is active. Two tiers of changes:

**Tier 1 — Within R-035 (content additions using existing CSS classes):**
- Add orientation sentences before each section's card grid
- Upgrade section-exit CTAs from `view-all` text links to a second `btn-ghost` button at the section bottom
- Sharpen hero sub paragraph for a new visitor (less jargon on first read)

**Tier 2 — Requires partial R-035 lift (minimal CSS only):**
- Section visual separators: adding `border-top: 1px solid var(--b1)` and increased `padding-top` to section containers to create breathing room between sections. This is 3-4 CSS lines, zero layout restructuring, zero blast radius.
- HASH must confirm Tier 2 before Codex touches CSS.

**Codex executes Tier 1 only in this turn.** Flag Tier 2 in the turn report for HASH decision.

---

## HASH Approval — Tier 2 Confirmed + 5-Section Priority

HASH confirmed: fix everything, ASAP.

The 5 things the homepage should communicate clearly (in order of priority):
1. **Hero** — big idea, who is this, what is the main title/hook
2. **Blog/Writing** — the articles, with a prominent CTA to go read them
3. **The Lab** — experiments and live signals
4. **Contact + Social** — how to reach HASH (contact form + Twitter/X + Telegram)
5. **Newsletter** — subscribe/stay in the loop

Sections that are currently pulling attention but are NOT in the top 5: "Context Signals" (the 3-stat cards with bar charts) and "Moving Now" (live price/wallet/writing cards). These can stay but must be visually subordinate — smaller, less prominent than the 5 priority sections. Do not delete them. Just ensure they don't compete with the 5 primary sections.

Tier 2 CSS is approved: add section visual separators. Specifically:
- `border-top: 2px solid var(--b1)` and `padding-top: 3rem` on each major section container to create clear visual breaks
- Context Signals and Moving Now sections: add a subtle `background: rgba(31,160,104,0.03)` tint to distinguish them as secondary/data sections vs primary content sections
- This is targeted CSS only — no layout restructuring, no flexbox/grid changes

---

## Codex Move — Full Changes to `bionic-banker/index.html`

R-039 applies: edit the built output at `bionic-banker/index.html`. The Astro source (`_astro-source/src/pages/index.astro` on Dell) requires a separate Dell SSH sync pass — note it in the turn but do not block on it.

### Change 1 — Hero sub paragraph (sharpen for first-time visitor)

Current:
```
An AML engine with 28 detection rules. A wallet risk scorer that explains itself in plain language. Agent systems that coordinate in real time. Built by someone working inside finance, all running in public.
```

Replace with:
```
I work inside finance and build the things it cannot easily explain. An AML detection engine. A wallet risk scorer that shows its reasoning. Agent systems that coordinate in real time. All running in public, all open to inspect.
```

The h1 already hooks the visitor. The sub now immediately answers "who is this person" before listing what they built.

### Change 2 — Orientation sentence before "Context Signals" grid

After the section-header div for Context Signals, before the `context-signal-grid`, add:
```html
<p class="section-orient">Three numbers that show why building in this space right now is not a hobby — it is a bet on timing.</p>
```

### Change 3 — Orientation sentence before "Moving Now" grid

After the section-header for Moving Now, before the `moving-now-grid`, add:
```html
<p class="section-orient">A live market price, a wallet risk snapshot, and the latest piece of writing — refreshed automatically.</p>
```

### Change 4 — Orientation sentence before "The Lab" grid

After the section-header for The Lab, before the `proof-route-grid`, add:
```html
<p class="section-orient">Five entry points into the work. Pick whichever fits where you are right now.</p>
```

### Change 5 — Prominent CTA at end of "The Lab" section

After the `proof-route-grid` closing div, add:
```html
<div style="text-align:center;margin:2rem 0 0.5rem;">
  <a href="/proof-tour" class="btn-primary">Walk the full lab →</a>
</div>
```

### Change 6 — Orientation sentence before "Writings" / Articles grid

After the section-header for Writings, before the `mag-grid`, add:
```html
<p class="section-orient">44 pieces on AML detection, blockchain infrastructure, AI agents, Canadian finance, and what the inside of a bank looks like when you are also building outside it.</p>
```

### Change 7 — Prominent CTA at end of Articles grid

After the `mag-grid` closing div, before the `bottom-split` div, add:
```html
<div style="text-align:center;margin:2rem 0 1rem;">
  <a href="/articles" class="btn-primary">Read all 44 articles →</a>
</div>
```

### Change 8 — `section-orient` style + Tier 2 section separators (CSS additions to existing `<style>` block)

Add to the existing inline `<style>` block in `<head>`:

```css
.section-orient{color:var(--text-2);font-size:.88rem;line-height:1.6;margin:-.25rem 0 1.25rem;max-width:640px;}
.section-divide{border-top:2px solid var(--b1);padding-top:3rem;margin-top:1rem;}
.section-secondary{background:rgba(31,160,104,0.03);}
```

Then apply these classes:
- Add `section-divide` to the `context-signal-section`, `moving-now-section`, `proof-route-section`, and the Writings `section-header` wrapper div
- Add `section-secondary` to `context-signal-section` and the Moving Now section wrapper to visually subordinate the data/live sections vs primary content sections

### Change 9 — Contact section: add Twitter/X link prominently

The contact section currently has a form only. Add a social row above the form:

```html
<div class="social-links-row" style="display:flex;gap:1rem;margin-bottom:1.5rem;flex-wrap:wrap;">
  <a href="https://twitter.com/BionicBanker" target="_blank" rel="noopener" class="btn-ghost">Twitter / X →</a>
  <a href="https://t.me/BionicBanker" target="_blank" rel="noopener" class="btn-ghost">Telegram →</a>
  <a href="https://linkedin.com/in/himanshu-h-a357684a" target="_blank" rel="noopener" class="btn-ghost">LinkedIn →</a>
</div>
```

This makes the Contact section actually answer "how do I reach this person" immediately, before the form. The form is for longer messages; the buttons are for quick connection. Twitter is listed first per HASH's feedback.

---

## Output Expected

- `bionic-banker/index.html` updated with all 9 changes
- Report in turn file: what changed, visual structure before/after summary, before/after for the hero sub
- Note Astro source sync needed on Dell when SSH is next available (R-039 source half)

---

## Boundary

No CSS layout restructuring (no flexbox/grid changes, no component removal).
No new sections beyond what is specified above.
No Astro rebuild on Dell without SSH approval.
No social posting.
No wallet, order, fund, key, or Telegram action.
Tier 2 CSS approved by HASH — execute as specified above.

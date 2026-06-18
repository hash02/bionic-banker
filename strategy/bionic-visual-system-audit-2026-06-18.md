# Bionic Banker visual system audit — 2026-06-18

## Verdict

The new screenshot-inspired homepage section should not become a hard-coded one-off. It should become a reusable visual grammar: **control-desk surfaces** for high-density AI/finance information.

Bionic Banker is already directionally premium: black/green identity, serious copy, strong article visuals, source-trail framing, and a homepage that now has a clear operating-stack moment.

It is not yet a fully mature premium design system. The missing layer is not more decoration. The missing layer is **repeatable motion + reusable system components**.

## What the reference image teaches

Do not copy the brand or exact UI. Extract the pattern:

1. **Information as an interface** — content is organized like a working environment, not a marketing brochure.
2. **Left rail / explorer** — gives context and orientation.
3. **Top path / command bar** — tells the reader where they are in the system.
4. **Grouped rows** — dense information becomes scanable when grouped into labeled stacks.
5. **Subtle colored lanes** — color indicates category, not decoration.
6. **Grid field** — gives technical depth without heavy illustration.
7. **Micro-motion** — small hover, glow, scanline, and node movement make the page feel alive without becoming gimmicky.

## Current alignment

### Strong

- Brand palette is coherent: black, green, muted white.
- Public language is serious: controls, evidence, source trail, review, limits.
- Homepage now has one strong system-map section.
- Article visuals increasingly use diagrams instead of generic blog images.
- Navigation is simple enough for first-time readers.

### Weak / missing

- The design system is split across one large global CSS file plus many page-level styles.
- Core pages are visually uneven:
  - Homepage and Signals have the strongest system feel.
  - Blog listing, AI Models, Projects, About, and AI Intelligence are more static/card-like.
- Motion exists mostly as hover transitions, not as a deliberate interaction language.
- 3D exists selectively on the homepage, but not as a reusable component model.
- Infographics are mostly static SVG/PNG; there is no lightweight animated version for web pages.
- There is no public visual-system spec that tells future work what to reuse and what to avoid.

## Code audit snapshot

Generated from `_astro-source/src/pages` and `public/styles/global.css`.

- Astro pages: 34
- Components: 2
- Global CSS: 2,424 lines
- Global CSS contains:
  - `@keyframes`: 4
  - `animation:`: 4
  - `transition:`: 35
  - `backdrop-filter`: 3
  - `radial-gradient`: 9
  - `linear-gradient`: 25
  - no global `perspective`, `rotateX`, or `translateZ`

Core page status:

| Page | Status | Notes |
|---|---|---|
| Homepage | Strongest | 3D/console/system stack now present. Good direction. |
| Signals | Strong | Dense and system-like, but can be simplified and aligned to control-desk grammar. |
| Articles | Medium | Functional but still closer to a blog grid than a premium intelligence interface. |
| AI Models | Medium | Needs richer model-map/stack structure. |
| AI Intelligence | Weak-medium | Good content lane, visually underpowered. |
| Projects | Medium | Should become a demo/proof shelf with screenshots, status, and limits. |
| About | Weak-medium | Clean, but not visually memorable. |

## Recommended visual system

### Name

**Bionic Control Desk**

### Component families

1. **Console shell**
   - sidebar/explorer
   - command/path bar
   - dense grouped rows
   - category color lanes

2. **Evidence card**
   - claim
   - source trail
   - limit
   - next action / next read

3. **System diagram card**
   - input → model → gate → output
   - animated only where it clarifies flow

4. **3D stack panel**
   - layered cards using CSS transforms
   - limited to hero and system overview surfaces

5. **Motion rules**
   - subtle hover elevation
   - slow grid shimmer
   - scanning line on console panels
   - particles only in hero / system map
   - no heavy animation inside article body

## Motion/3D position

Yes, the site should become more dynamic. But not everywhere.

Use dynamic visuals when they explain:

- source trail moving through gates
- model output becoming an evidence record
- risk signal moving into human review
- payment/request/approval flow
- wallet or transaction graph structure

Avoid motion when it competes with reading:

- article paragraphs
- footnotes/source sections
- long blog grids
- mobile pages with limited space

## Priority edit plan

### Phase 1 — codify the system

- Create shared CSS classes for console shell, evidence cards, rows, badges, and grid fields.
- Move repeated page-level visual patterns out of ad hoc inline CSS over time.
- Keep homepage as the first reference implementation.

### Phase 2 — align core pages

1. Articles page: convert from blog grid to intelligence library with filters + grouped rows.
2. AI Models page: add model-map / concept-stack visual.
3. Projects page: add demo shelf with status, screenshot, public boundary, and what it cannot do.
4. AI Intelligence page: add control-desk overview and source queue structure.
5. About page: turn into operator profile + public boundary + system philosophy.

### Phase 3 — add lightweight motion

- CSS-only scanline / glow / row hover motion.
- Optional canvas only on homepage and one system-map page.
- Animated SVG flow components for selected articles.
- Respect reduced-motion media query.

## Critical feedback

The current site is credible and improving, but not yet at the level where every page feels like one premium product. It still feels partly like a strong blog with some advanced visual moments.

The next jump is to make every public surface feel like it belongs to the same operating system.

The mistake would be adding random 3D. The better move is to create reusable control-desk components and apply them selectively.

## Decision

Treat the screenshot-derived style as a **design grammar**, not a hard-coded rule:

> Every important Bionic surface should answer: where am I, what is the source, what is the control, what is the limit, and what can I inspect next?

The visual form should support that answer: explorer, path, grouped rows, evidence cards, diagrams, and restrained motion.

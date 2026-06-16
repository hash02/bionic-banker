# Bionic Banker Carousel Design Standard

## Reason

The first AI-agent gates carousel was too sparse: seven slides, low text density, weak visual hierarchy, and too much empty bottom space. Future carousels should feel like compact evidence cards, not oversized title cards.

## Format

Default LinkedIn format:

- 3 slides for one argument
- 1080 x 1350 portrait
- deterministic HTML/CSS/SVG/Python rendering
- browser-rendered HD output preferred: 2160 x 2700 PNG generated from 1080 x 1350 HTML/CSS using device scale factor 2
- no AI-generated text inside images
- contact sheet required before upload

Use 2 slides only for short announcements. Use 5 slides only when each slide has a distinct visual/data role. Avoid 7+ slides unless there is real data density.

## Slide structure

### Slide 1 — Thesis card

Purpose: hook + visual map.

Required:

- strong title
- one-line thesis
- 4–6 dense bullets or micro-panels
- footer with topic/boundary

### Slide 2 — Evidence/control card

Purpose: show the mechanism.

Required:

- table, decision tree, control map, or before/after comparison
- at least 5 meaningful labels
- one short takeaway

### Slide 3 — Operating rule card

Purpose: make the reader save/share.

Required:

- checklist or rule set
- clear boundary/disclaimer
- URL or project/source cue

## Density target

Each slide should have:

- 70–140 words, or
- 35–70 words plus diagram/table, or
- a dense checklist/table with at least 8 visible information units.

Avoid slides with only one sentence unless it is the cover of a high-quality visual series.

## Visual system

Use Bionic style:

- black/near-black background
- green source-map accents
- off-white text
- thin panels and grid lines
- small labels like `REQUEST`, `RULE`, `AUDIT`, `HUMAN REVIEW`
- evidence/control/risk vocabulary

Do not use:

- generic gradient cards
- oversized empty margins
- one-liner slides repeated seven times
- decorative elements that carry no information

## QA checklist

Before upload:

- [ ] 2–3 slides unless the content truly needs more
- [ ] text fills vertical space without crowding
- [ ] no huge empty lower third
- [ ] contact sheet visually checked
- [ ] all slides 1080x1350
- [ ] exact approved title preserved
- [ ] duplicate ledger check passes
- [ ] public-copy/leak guards pass for article/caption

# Codex Website Care Turn 092

Date: 2026-05-20
Actor: Codex
Previous actor: Claude Code

---

## What Claude Did This Turn

1. Completed the 30-agents article source: `_astro-source/src/content/blog/30-agents-which-ones-i-built.md` (1,800+ words)
2. Built Astro site (54 pages confirmed)
3. Copied `blog/30-agents-which-ones-i-built/index.html` to repo root
4. Committed and pushed — article is live
5. Wrote LinkedIn seeds for 5 images from the second image batch (banned words, HTML vs Markdown, 12 fintech prompts, karpathy, clone-yourself-claude)

---

## What Codex Needs To Do This Turn

### Task 1: Verify 30-agents article is live

- URL to verify: `https://bionicbanker.tech/blog/30-agents-which-ones-i-built/`
- Check: page loads, title renders, GEO opener paragraph is before the first H1
- GEO opener text should start with: "GenAI Works published a 30-agent engineering reference"

### Task 2: Verify Karpathy article is live

- URL to verify: `https://bionicbanker.tech/blog/karpathy-banking-software-era/`
- Check: page loads, title renders correctly
- Codex turn 091 flagged some wording concerns — do a phrase scan on the built output:
  - Banned words scan: no AI-isms (delve, leverage, utilize, seamless, transformative, innovative, groundbreaking, etc.)
  - No CIBC mentions
  - No private IPs, paths, wallet addresses
  - "inside a bank" appears multiple times — check if any instance needs softening (not a bank employee context — builder who works inside finance)
- If any banned term found: fix in both source and built output, commit and push

### Task 3: Write hero image JSON briefs for Wukong

Claude writes briefs. Wukong renders. Codex delivers the briefs to Wukong.

**Brief A — 30-agents hero image:**

File to write: `/tmp/30-agents-hero-brief.json`

```json
{
  "slug": "30-agents-which-ones-i-built",
  "output_filename": "30-agents-hero.png",
  "dimensions": { "width": 1200, "height": 630 },
  "background": "#08080e",
  "layout": "split-six",
  "concept": "Six-category taxonomy grid showing the 30-agent framework categories (Foundation, Intelligence, Multimodal, Specialized, Domain, Integration) with a 14/30 counter showing HASH's build coverage",
  "elements": [
    {
      "type": "headline",
      "text": "30 AI Agents",
      "color": "#e4e4ec",
      "size": "large",
      "position": "top-left"
    },
    {
      "type": "subheadline",
      "text": "I built 14. Before seeing the framework.",
      "color": "#8a8aa0",
      "size": "medium",
      "position": "below-headline"
    },
    {
      "type": "counter",
      "text": "14 / 30",
      "color": "#1fa068",
      "size": "xlarge",
      "position": "center-right"
    },
    {
      "type": "grid",
      "items": ["Foundation", "Intelligence", "Multimodal", "Specialized", "Domain", "Integration"],
      "highlight": ["Foundation", "Intelligence", "Domain"],
      "highlight_color": "#1fa068",
      "default_color": "#8a8aa0",
      "position": "bottom"
    }
  ],
  "palette": {
    "background": "#08080e",
    "accent": "#1fa068",
    "text_primary": "#e4e4ec",
    "text_muted": "#8a8aa0"
  },
  "no_gradients": true,
  "no_red": true,
  "no_blue": true,
  "no_purple": true
}
```

**Brief B — Karpathy hero image:**

File to write: `/tmp/karpathy-banking-hero-brief.json`

```json
{
  "slug": "karpathy-banking-software-era",
  "output_filename": "karpathy-banking-hero.png",
  "dimensions": { "width": 1200, "height": 630 },
  "background": "#08080e",
  "layout": "three-columns",
  "concept": "Three vertical columns representing Software 1.0 / 2.0 / 3.0, showing the progression from explicit code to neural nets to LLMs, with a fourth annotation showing where banking currently sits across all three",
  "elements": [
    {
      "type": "column",
      "label": "1.0",
      "sublabel": "Explicit Code",
      "note": "COBOL still runs it",
      "color": "#8a8aa0",
      "position": "left"
    },
    {
      "type": "column",
      "label": "2.0",
      "sublabel": "Neural Nets",
      "note": "Fraud detection, credit scoring",
      "color": "#8a8aa0",
      "position": "center"
    },
    {
      "type": "column",
      "label": "3.0",
      "sublabel": "LLMs",
      "note": "Where the interesting thing happens",
      "color": "#1fa068",
      "position": "right"
    },
    {
      "type": "headline",
      "text": "Karpathy drew the map.",
      "color": "#e4e4ec",
      "size": "large",
      "position": "top"
    },
    {
      "type": "subheadline",
      "text": "Here is what the terrain looks like from inside finance.",
      "color": "#8a8aa0",
      "size": "medium",
      "position": "below-headline"
    }
  ],
  "palette": {
    "background": "#08080e",
    "accent": "#1fa068",
    "text_primary": "#e4e4ec",
    "text_muted": "#8a8aa0"
  },
  "no_gradients": true,
  "no_red": true,
  "no_blue": true,
  "no_purple": true
}
```

**Wukong invocation pattern:**
```bash
scp /tmp/30-agents-hero-brief.json hash@100.86.26.81:/tmp/
ssh -i ~/.ssh/maya_key hash@100.86.26.81 "python3 ~/maya01-brain/tools/build_blog_infographics.py --slug 30-agents-which-ones-i-built --brief /tmp/30-agents-hero-brief.json"

scp /tmp/karpathy-banking-hero-brief.json hash@100.86.26.81:/tmp/
ssh -i ~/.ssh/maya_key hash@100.86.26.81 "python3 ~/maya01-brain/tools/build_blog_infographics.py --slug karpathy-banking-software-era --brief /tmp/karpathy-banking-hero-brief.json"
```

After Wukong renders: copy PNGs to `bionic-banker/blog-visuals/png/`, update article source frontmatter to reference the image, rebuild, push.

### Task 4: Check if articles index / homepage shows both new articles

- Homepage at `https://bionicbanker.tech/` should show both new articles in the recent posts grid
- If not visible, check index.html in repo root for article card rendering

---

## Division of Labor Reminder

- Claude: writing content, JSON briefs
- Codex: build, copy, commit, push, Wukong invocations, live verification
- Wukong: render images from briefs
- HASH: final approve on image output before blog post hero update

---

## Articles Live After This Turn

- `blog/karpathy-banking-software-era/` — Karpathy / Software 1.0/2.0/3.0 from inside finance
- `blog/30-agents-which-ones-i-built/` — 30-agent framework cross-reference

Both need hero images. Wukong renders from the JSON briefs in this turn file.

---

## Phrase Scan Notes

Run phrase scan on BOTH new article built outputs before anything else. Scan for:
- AI-isms: delve, leverage, utilize, seamless, transformative, innovative, groundbreaking, optimize, breakthrough, pivotal, data-driven, robust, crucial, comprehensive
- Banned phrases: "inside the bank" (reframe to "inside finance"), em-dashes (—, –), "bank employee"
- Private identifiers: CIBC, MAYA, KAYA, KALA, WUKONG, maya_key, any IP address, any wallet address

Fix any hit before pushing.

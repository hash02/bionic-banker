# Codex Website Care Turn 096

Date: 2026-05-20
Actor: Codex
Previous actor: Claude Code

---

## Context

A LinkedIn carousel needs to be built for the AI benchmark article (turn 095). Claude Code wrote the content brief as a JSON file. Your job is to send the brief to Wukong and trigger the carousel render.

**R-040 rule applies:** Wukong owns infographic rendering end-to-end. Do not write HTML templates or Playwright code here. Send the brief to Wukong, run the build command there.

---

## Task: Build LinkedIn Carousel — AI Benchmark

### Step 1: Verify the brief exists

```
site-agent/carousel-briefs/ai-benchmark-carousel.json
```

Should be there. 9 slides, 1080x1080 format, dark palette.

### Step 2: SCP brief to Wukong

```bash
scp -i ~/.ssh/maya_key \
  "site-agent/carousel-briefs/ai-benchmark-carousel.json" \
  hash@100.86.26.81:/tmp/ai-benchmark-carousel.json
```

### Step 3: SSH to Wukong and run the carousel builder

```bash
ssh -i ~/.ssh/maya_key hash@100.86.26.81 \
  "python3 ~/maya01-brain/tools/build_carousel.py \
    --slug ai-benchmark-carousel \
    --brief /tmp/ai-benchmark-carousel.json \
    --output ~/carousel-output/"
```

If `build_carousel.py` does not exist on Wukong, use the blog infographics builder and adapt:

```bash
ssh -i ~/.ssh/maya_key hash@100.86.26.81 \
  "python3 ~/maya01-brain/tools/build_blog_infographics.py \
    --slug ai-benchmark-carousel \
    --brief /tmp/ai-benchmark-carousel.json"
```

### Step 4: Pull output back

The carousel output is a PDF (LinkedIn carousel format) and/or individual PNG slides. Pull to local:

```bash
scp -i ~/.ssh/maya_key -r \
  hash@100.86.26.81:~/carousel-output/ai-benchmark-carousel/ \
  "blog-visuals/ai-benchmark-carousel/"
```

### Step 5: Commit the output

```bash
git add blog-visuals/ai-benchmark-carousel/
git add site-agent/carousel-briefs/ai-benchmark-carousel.json
git commit -m "content: add AI benchmark LinkedIn carousel"
git pull --rebase origin main
git push origin main
```

---

## Expected Output

A folder at `blog-visuals/ai-benchmark-carousel/` containing:
- `slide-01.png` through `slide-09.png` (1080x1080 each)
- `ai-benchmark-carousel.pdf` (combined, for LinkedIn upload)

---

## Done State

Turn is complete when:
- PDF + PNGs are in `blog-visuals/ai-benchmark-carousel/`
- Files are committed and pushed
- Report back with file list and confirm PDF is ready for LinkedIn upload

HASH will handle the actual LinkedIn post. Do not post anything.

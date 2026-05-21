# Codex Website Care Turn 097

Date: 2026-05-20
Actor: Codex
Previous actor: Claude Code

---

## Context

Two deliverables from Claude Code need deploying: a blog article and a LinkedIn carousel. Run them in order.

---

## Task A: Deploy Blog Article — Finance GitHub Repos

Source file already written at:
```
_astro-source/src/content/blog/finance-github-repos.md
```

### Build
```bash
cd _astro-source && npm run build
```

### Copy built output (R-039)
```
_astro-source/dist/blog/finance-github-repos/index.html → blog/finance-github-repos/index.html
_astro-source/dist/blog/index.html → blog/index.html
_astro-source/dist/index.html → index.html
```

### Commit
```bash
git add _astro-source/src/content/blog/finance-github-repos.md
git add blog/finance-github-repos/
git add blog/index.html
git add index.html
git commit -m "content: add finance GitHub repos article"
git pull --rebase origin main
git push origin main
```

Verify live: `https://bionicbanker.tech/blog/finance-github-repos/`

---

## Task B: Build LinkedIn Carousel — Finance GitHub Repos

Brief at:
```
site-agent/carousel-briefs/finance-github-repos-carousel.json
```

10 slides, 1080x1080. Same render process as the AI benchmark carousel (turn 096).

### SCP to Wukong
```bash
scp -i ~/.ssh/maya_key \
  "site-agent/carousel-briefs/finance-github-repos-carousel.json" \
  hash@100.86.26.81:/tmp/finance-github-repos-carousel.json
```

### Render on Wukong
```bash
ssh -i ~/.ssh/maya_key hash@100.86.26.81 \
  "python3 ~/maya01-brain/tools/build_carousel.py \
    --slug finance-github-repos-carousel \
    --brief /tmp/finance-github-repos-carousel.json \
    --output ~/carousel-output/"
```

### Pull output
```bash
scp -i ~/.ssh/maya_key -r \
  hash@100.86.26.81:~/carousel-output/finance-github-repos-carousel/ \
  "blog-visuals/finance-github-repos-carousel/"
```

### Commit
```bash
git add blog-visuals/finance-github-repos-carousel/
git add site-agent/carousel-briefs/finance-github-repos-carousel.json
git commit -m "content: add finance GitHub repos LinkedIn carousel"
git pull --rebase origin main
git push origin main
```

---

## Done State

- Article live at `https://bionicbanker.tech/blog/finance-github-repos/`
- Carousel PDF + PNGs in `blog-visuals/finance-github-repos-carousel/`
- Both committed and pushed
- Report back with live URL and commit hashes

HASH posts to LinkedIn manually. Do not post.

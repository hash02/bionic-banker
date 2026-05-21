# Codex Website Care Turn 095

Date: 2026-05-20
Actor: Codex
Previous actor: Claude Code

---

## Context

Claude Code wrote a new blog article. Your job is to deploy it. No design changes. No new modules. One article, both files (R-039), build, commit, push.

---

## Task: Deploy Blog Article — AI Model Benchmark Cost

The article is already written and sitting at:

```
_astro-source/src/content/blog/ai-model-benchmark-cost.md
```

That file is complete. Do not edit the content. Your job is the deploy sequence only.

### Step 1: Verify the source file is there

```bash
ls _astro-source/src/content/blog/ai-model-benchmark-cost.md
```

Should exist. If it does not, stop and report back.

### Step 2: Build

```bash
cd _astro-source && npm run build
```

Zero errors expected. If errors appear, check the frontmatter in the .md file — must match the schema exactly (title, description, date, tags, readTime, category, featured, slug).

### Step 3: Copy built output to repo root (R-039)

The Astro build outputs to `_astro-source/dist/`. After build, copy the article's built output to the repo root:

```
_astro-source/dist/blog/ai-model-benchmark-cost/index.html
→ blog/ai-model-benchmark-cost/index.html
```

Also update the blog index page if the build regenerates it:

```
_astro-source/dist/blog/index.html → blog/index.html
```

And the homepage if article count or "latest" listing changes:

```
_astro-source/dist/index.html → index.html
```

Use judgment on which root files changed. When in doubt, copy the one that changed.

### Step 4: Commit

```bash
git add _astro-source/src/content/blog/ai-model-benchmark-cost.md
git add blog/ai-model-benchmark-cost/
git add blog/index.html
git add index.html
git commit -m "content: add AI model benchmark cost article"
```

### Step 5: Push

```bash
git pull --rebase origin main
git push origin main
```

Always pull --rebase before push (heartbeat cron commits every hour, causes conflicts otherwise).

### Step 6: Verify live

After push, Cloudflare Pages deploys automatically. Check:

```
https://bionicbanker.tech/blog/ai-model-benchmark-cost/
```

Confirm:
- Page loads
- Title displays correctly: "The Leaderboard Nobody Is Talking About the Right Way"
- Table renders (the benchmark data table with 14 rows)
- Article appears in /blog/ listing

---

## Done State

Turn is complete when:
- Article is live at the URL above
- No build errors
- Both source and built output are committed (R-039 satisfied)

Report back with the live URL and commit hash.

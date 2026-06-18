# Distribution Metrics Ledger

Purpose: track Bionic Banker platform-native distribution performance and make the distribution agent self-improve from real results.

## Schema

Each post should be logged as:

```yaml
- date:
  platform:
  post_url:
  topic:
  format:
  hook:
  visual_path:
  caption_path:
  article_url:
  posted_at_local:
  metrics:
    impressions_2h:
    impressions_24h:
    impressions_7d:
    reactions:
    comments:
    reposts:
    saves:
    profile_views:
    new_followers:
  qualitative:
    best_comment:
    who_engaged:
    what_worked:
    what_failed:
    next_test:
```

## Current test queue

### Test 001 — LinkedIn hallucination evidence checklist

```yaml
platform: linkedin
topic: AI hallucination evidence checklist for finance teams
format: sharp single-image post + short caption + first-comment link
hook: "An AI answer is not evidence."
visual_path: /home/hash/bionic-banker/social-assets/linkedin-ready/ai-hallucination-evidence-checklist-finance/ai-hallucination-evidence-checklist-finance-v4-final.png
caption_path: /home/hash/bionic-banker/distribution/linkedin-ai-hallucination-evidence-checklist-finance-short.md
article_url: https://bionicbanker.tech/blog/ai-hallucination-evidence-checklist-finance/
status: ready_not_posted
hypothesis: recognizable finance-control mistake + practitioner question will outperform article-announcement framing.
```

## Weekly review questions

1. Which hook created comments?
2. Which visual made people stop?
3. Which topic produced profile clicks or follows?
4. Which platform fit the idea best?
5. Which pattern should be locked, changed, or retired?

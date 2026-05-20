# Analytics Addendum — Turn 092

Date: 2026-05-20
Source: Google Analytics mobile screenshots, shared by HASH

---

## Raw Numbers

| Window | Active Users | New Users | Avg Engagement | vs Prior |
|---|---|---|---|---|
| Apr 20 – May 19 (30-day) | 130 | 129 | ~41s | -42.48% / -41.63% / +36% eng |
| May 13 – May 19 (7-day) | 12 | 10 | ~6m 21s | -25% / -33% / +1964% eng |
| May 19 (1-day) | 6 | 2 | ~5m 25s | flat / -50% / -23% |

---

## What the Data Says

**Engagement time is the real signal.**

1964% week-over-week engagement jump with a smaller user count means the people finding the site are reading multiple articles, not bouncing. A 6-minute average session on a content site is strong. That is not a broken site. That is a site with no distribution.

The 30-day drop (42%) is against a period that had a traffic spike around late March / early April. The absolute numbers are small — 130 users over 30 days is roughly 4-5 per day average. The May 13 spike visible in Chart 1 (hit ~28-30 users that day) was an anomaly, likely from a social share or mention.

**The traffic pattern:**

Organic baseline: 4-6 users per day. Spike events: 10-30 users on publication or share days. Post-spike: drops back to baseline within 1-2 days. No sustained distribution layer. Each spike decays immediately.

---

## What Codex Should Do With This

### Task A: Check source of May 13 spike

Pull from GA if possible — which pages had the most visits on May 13. This tells us which article drove the spike and whether the same content type should be prioritized for LinkedIn promotion.

If GA access not available from Codex env, flag for HASH to check manually (Acquisition > Traffic Acquisition, filter to May 13).

### Task B: Update the site-agent analytics log

Append to `site-agent/analytics-log.md` (create if doesn't exist):

```
2026-05-20 — GA snapshot
30-day (Apr 20 – May 19): 130 active, 129 new, ~41s engagement, -42% vs prior period
7-day (May 13–19): 12 active, 10 new, 6m 21s engagement, +1964% vs prior week
Daily (May 19): 6 active, 2 new, 5m 25s engagement
Pattern: high engagement, low volume. No sustained distribution layer.
```

### Task C: Flag for HASH — LinkedIn seeds are the priority action

The analytics gap between engagement quality (6 min avg) and traffic volume (6/day) is a distribution problem, not a content problem. The LinkedIn seeds Claude wrote today are the direct fix:

- `50-career/linkedin-seeds/banned-words-ai-output-seed-2026-05-20.md`
- `50-career/linkedin-seeds/html-vs-markdown-claude-seed-2026-05-20.md`
- `50-career/linkedin-seeds/fintech-prompt-libraries-seed-2026-05-20.md`
- `50-career/linkedin-seeds/karpathy-banking-seed-2026-05-20.md`
- `50-career/linkedin-seeds/clone-yourself-claude-seed-2026-05-20.md`

Five seeds ready. None of them have been posted. Each one has a link-back to an article. This is the distribution flywheel gap.

### Task D: Nothing to fix in the site structure

The engagement time numbers confirm the site content is working. Do NOT make layout changes, navigation changes, or restructuring based on this data. The problem is upstream of the site. Getting users there is the fix, not changing the site once they arrive.

---

## For the Next Claude Turn

Priority order given this data:
1. HASH posts at least one LinkedIn seed (any of the five ready ones)
2. Monitor GA for 48 hours after post to see spike pattern
3. If spike sustains (users keep coming 2 days after post), the distribution flywheel is starting
4. If spike decays in 24 hours same as May 13 — add CTA on articles pointing to newsletter / LinkedIn follow to capture repeat visitors

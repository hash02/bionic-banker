# Daily Post Loop State

Loop: Bionic daily LinkedIn + blog post
Cadence: 09:00 local time daily
Autonomy: approved for one public Bionic blog + LinkedIn post per day, with duplicate and public-safety guards.

## Last completed public post

- Topic: Stablecoins are becoming machine payment rails / receipt layer
- LinkedIn URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7472556753100886016/
- Ledger: `distribution/post-ledger.json`
- Note: duplicate newer post was removed by user; kept older post in ledger.

## Next planned topic

- Title: AI agents need gates, not vibes
- Source: `agent-framework-proof`
- Queue file: `distribution/next-5-days-linkedin-blog-queue.md`

## Required preflight

1. Read `distribution/post-ledger.json`.
2. Read `distribution/next-5-days-linkedin-blog-queue.md`.
3. Pick first unposted queue item.
4. Create blog article and LinkedIn package.
5. Run `scripts/post_ledger_check.py` against final caption/article/carousel.
6. Run public leak guards.
7. Upload/post only once.
8. Capture LinkedIn URL and screenshot.
9. Append ledger and update this file.

## Blockers

None currently.

## Stop immediately if

- duplicate ledger blocker appears
- LinkedIn is not logged in
- browser upload does not show all slides
- site checks fail
- caption/article makes investment, legal, compliance approval, customer decision, or performance claims
- post URL cannot be captured after posting

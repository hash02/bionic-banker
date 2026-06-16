# Repeated Workflow Inventory

Status: active
Purpose: identify tasks performed more than twice and convert repeatable patterns into skills/checklists.

## Tasks repeated more than twice

| Workflow | Evidence / pattern | Convert to skill? | Status |
|---|---|---:|---|
| Public website packaging guard | build, simplicity check, public safety leak check, projects positioning, mobile QA | yes | skill created |
| LinkedIn post preparation | pick article, create caption, prepare carousel assets, upload/post, capture URL | yes | skill created |
| Duplicate-post prevention | ledger, caption hash, article URL, carousel path, 24h cadence | yes | skill created |
| Repo-to-project packaging | inspect repo, rank public-safety, add AGENTS/docs/cards/ADR, run tests | yes | included in skill |
| Public/private leak review | scan for internal names, paths, credentials, wallet authority, overclaims | yes | included in skill |
| Obsidian/internal index writing | summarize repos into vault notes and packaging index | maybe | defer |
| Carousel QA | check slide dimensions, contact sheet, mobile readability, upload order | yes | included in skill |
| Git commit/push discipline | status, targeted add, commit, verify, push only clean intended files | maybe | defer to GitHub skill |

## Skill created

```text
public-content-packaging-and-posting
```

Scope:

- packaging Bionic projects for public site
- creating LinkedIn-ready post/carousel packages
- duplicate-post ledger checks
- public leak guards
- deterministic verification before public posting

## Do not automate without explicit approval

- deleting posts
- publishing same-day follow-up posts
- changing account/profile settings
- paid promotion
- paid tools/subscriptions
- bank/tax/KYC/payment settings

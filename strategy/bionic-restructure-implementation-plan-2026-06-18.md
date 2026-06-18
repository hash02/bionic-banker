# Bionic Banker Restructure Implementation Plan

Date: 2026-06-18
Source reviewed: `bionicbanker-restructure-plan-with-references.md`

## Decision

Adopt the restructure plan with one important constraint:

```text
Do not turn Bionic Banker into a resume site.
Build a compressed public front door that serves employers, collaborators, and like-minded builders.
```

The correct frame is:

```text
Bionic Banker = public proof surface for governed AI in finance
Himanshu = regulated banking + AI governance builder
Work = evidence trails, AML workflows, model-risk checks, human review
Archive = full brain for those who want it
```

## My critique of the new plan

The plan is strong. It fixes the first critique's hiring bias by broadening the audience to collaborators and builders.

The best parts:

1. It separates `front door` from `archive`.
2. It keeps the source-trail/human-review thesis instead of deleting the voice.
3. It makes `/work/` the compression layer.
4. It names edge cases clearly: stale metrics, regulated-employment risk, static-demo hypocrisy, audience conflict.
5. It ties Bionic's wedge to current market/regulatory signals.

The weak parts:

1. The proposed nav `Home | Work | Writing | Projects | About | Contact` may be too much if applied immediately.
2. The external report list is useful for strategy but too heavy for public pages.
3. `/work/` must be short. If we put the whole plan there, we recreate the same overload.
4. The Advice Review Layer is not built yet, so it should be marked `prototype proof` or use AML/Agent Proof as temporary lead.
5. We should not cite future-dated or difficult-to-verify reports publicly without checking them first.

## Implementation principle

Build the smallest public compression layer first.

Do not redesign the whole site in one pass.

Do not expose strategy docs, edge-case tables, or long external bibliography on the public front door.

## Phase 1 — Ship `/work/` compression page

Route:

```text
/work/
```

Purpose:

```text
A 60-second page for employers, collaborators, and like-minded builders.
```

Page structure:

1. Hero
2. Identity strip
3. Three proof cards
4. Work-with-me lanes
5. Best writing links
6. Contact / boundary

### Hero copy

Headline:

```text
I build governed AI systems for finance.
```

Subhead:

```text
Bionic Banker is a public lab for AI finance controls: source trails, model-risk checks, AML workflows, agent governance, and human review.
```

CTA:

```text
View proof
Contact
```

### Identity strip

```text
Himanshu — Canadian banking + AI governance builder.
Focused on wealthtech trust, AML/compliance automation, model-risk checks, and evidence trails for AI-assisted financial workflows.
```

### Three proof cards

Card 1 — AI Financial Advice Review Layer

```text
Prototype proof for reviewing AI-generated financial answers before they become client-facing text or operational decisions.
Input: sample question + AI answer.
Output: claim table, risk flags, human-review trigger, evidence packet.
Boundary: educational proof, not financial/legal/compliance advice.
```

Card 2 — AML Detection Engine

```text
Rules-based AML triage proof with test coverage and explicit limits.
Input: synthetic/controlled transaction data.
Output: risk flags and review notes.
Boundary: triage support, not SAR filing or compliance approval.
```

Card 3 — Agent Governance / Audit Trail

```text
Control pattern for AI agents that touch tools, sources, and workflow actions.
Input: agent task / output / tool trace.
Output: gates, blocked actions, audit trail, human review point.
Boundary: proof layer, not production authorization system.
```

## Phase 2 — Upgrade About page

Goal: make Himanshu legible without making the site self-centered.

Add:

```text
Name
Current background: regulated Canadian banking
Builder lane: AI governance / evidence systems for financial workflows
Target collaboration lanes: AI governance, model risk, AML automation, wealthtech trust
Links: LinkedIn, GitHub, resume/contact
Boundary: public work uses synthetic/public material, not employer/client data
```

## Phase 3 — Curate Writing page

Do not show 63 posts equally.

Add a `Start here` or `Featured writing` section with 6–10 pieces:

- AI agents need gates, not vibes
- AI Hallucination Evidence Checklist for Finance Teams
- Human-in-loop agent payments
- Agent graveyard
- Wallet risk notes
- What Claude can't do for KYC

Everything else remains in archive/index.

## Phase 4 — Reframe stale/weak surfaces

Do not delete the full brain. Move it behind archive framing.

Actions:

```text
Signals -> archived experiment unless actively refreshed
BTC accuracy -> never homepage / never Work page
Risk self-scores -> private or builder archive
Gaps -> Builder notes, not main CTA
Labs/Dashboard/System Map -> no top nav
```

## Phase 5 — Build the Advice Review Layer proof

Files already started under:

```text
/home/hash/wealthsimple-campaign/ai-financial-advice-review-layer/
```

Needed:

```text
sample-ai-answer.md
review-checklist.yaml
evidence-packet-example.md
static-demo-page.md or Astro page
```

Public route later:

```text
/work/ai-financial-advice-review-layer/
```

or initially a section on `/work/`.

## Phase 6 — External reference discipline

External reports are useful for strategy, but public pages should cite only 2–4 high-confidence references per page.

For `/work/`, do not dump the bibliography.

Use only:

- OSFI E-23 for Canadian model-risk context, if verified.
- OWASP LLM / Excessive Agency for security/control context.
- One agentic finance governance source if verified.
- Bionic's own proof artifacts.

## Phase 7 — Hardcode the restructure guard

After `/work/` exists, add a repo guard:

```bash
npm run test:work-page-contract
```

It should verify:

- `/work/` exists.
- hero contains `I build governed AI systems for finance`.
- page has identity block.
- page has exactly 3–4 proof cards.
- each proof card has boundary language.
- page contains contact links.
- no stale metrics such as BTC accuracy or May signal rows.
- no private Wukong/Hermes/local path language.

## Execution order

1. Create `/work/` static page.
2. Run public-copy/simplicity/safety checks.
3. Build and visually inspect.
4. Sync static root.
5. Commit/push.
6. Add `Work` link in homepage CTA first, not necessarily nav yet.
7. After approval, consider nav change.
8. Add About identity improvements.
9. Build Advice Review Layer demo.
10. Add work-page contract guard.

## Immediate build recommendation

Do not change the global nav first.

First ship:

```text
/work/
```

Then add a homepage block:

```text
Work with Himanshu
Governed AI systems for finance: AML workflows, model-risk checks, agent audit trails, and evidence packets.
```

This is safer than a full redesign and directly answers the critique.

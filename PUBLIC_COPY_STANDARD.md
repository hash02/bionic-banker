# Bionic Banker Public Copy Standard

Bionic Banker is a public AI + finance + compliance/risk platform. Public pages should use simple reader-first language: what it is, what it does, what supports it, what stays private, and what the system cannot do. Keep the serious risk, monitoring, and audit tone, but do not make readers decode internal agent language.

## Core standard

Use public language that a compliance, risk, data, audit, or governance buyer would recognize:

- risk assessment
- wallet screening
- transaction monitoring
- risk signal
- supporting records
- evidence records
- audit trail
- decision history
- controls
- monitoring
- reporting
- clear limits
- requires human approval
- plain-language summary
- risk rationale

Every public page or card should answer:

1. What is this?
2. What does it do?
3. Why does it matter?
4. What can the reader check?
5. What can it not do?

## World and voice anchors

The public site should carry the same pattern as Hash's wider operating world, but translated for normal readers:

- The private world is a falsifiability machine. The public site should say this as: show the source, show the check, show the limit.
- Bionic Banker is the public surface for finance, AI, compliance, agent workflows, and career/business trust. The public reader should not need to know vault paths, agent names, or internal boards to understand it.
- The loop is one thing at a time: signal, source trail, plain-language note, human decision.
- The voice should sound like Hash explaining a system out loud: direct, specific, cautious, and useful. If it sounds like a pitch deck, rewrite it.
- Counts, dates, rule numbers, article totals, system-card totals, and status claims must be computed or checked from source files before they appear in public copy.
- Do not use internal shorthand as visible labels. Prefer clear reader labels such as clear limits, source trail, review note, case packet, system health, and proof pack.

## Do not use publicly

Avoid these words/phrases in navigation, titles, hero sections, route labels, product descriptions, dashboard cards, JSON shown to the site, and generated public HTML:

- Proof Tour
- AML Proof
- proof page
- proof surface
- proof path
- proof route
- Read the proof
- Wallet Risk Lab
- public workbench
- Live Signals
- Experiments
- AI Learning
- receipt / receipts, unless referring to a real payment receipt
- vibe / vibes
- magic
- truth layer
- clean wallet
- safe wallet
- guaranteed compliance
- approved KYC / KYC approved
- licensed compliance product, unless explicitly negated as a boundary
- autonomous profit
- guaranteed return
- live execution enabled
- wallet power: true
- trade power: true
- roast / roaster / roasts, except in historical repository URLs that cannot be renamed safely

## Preferred replacements

- Proof Tour → Risk & Evidence Overview
- proof page → evidence page or status evidence page
- proof surface → public page, evidence view, or what you can inspect
- proof path / proof route → review map, system overview, or page
- proof → supporting record, evidence record, verification, audit trail, or benchmark result
- Wallet Risk Lab → Wallet Risk Assessment
- Live Signals → Risk Signals or Market & Risk Signals
- Experiments → Systems, Case Studies, Workflows, or Reports
- AI Learning → Knowledge Base
- receipt → evidence record or audit entry
- roast / roaster → risk note, assessment note, risk-note generator, reader-ready summary, risk rationale
- truth layer → evidence layer, review layer, or verification layer
- clean wallet / safe wallet → lower-risk wallet, no current risk signal, no elevated signal in this sample
- demo → public demonstration, prototype, walkthrough, or reproducible example
- lab → system, sandbox, research environment, or controlled environment
- approval power / outside-action power → what the system cannot do or clear limit
- human-reviewed agent work → requires human review
- reviewer question → what this shows

## Allowed technical exceptions

Do not blindly replace legitimate technical or historical language:

- cryptographic proof / zero-knowledge proof in ZK articles
- institutional research lab names such as Borealis AI lab or TRM Labs
- old external repository URLs that still contain historical names
- CSS class names or legacy internal identifiers when they are not visible public copy

If an exception is used, make sure nearby public-facing prose still uses the mature wording and states the boundary.

## Required public boundaries for compliance/risk pages

Compliance, AML, wallet-risk, trading, or finance pages should include clear boundaries when relevant:

- not legal advice
- not investment advice
- not a KYC approval
- not SAR filing software
- not a licensed compliance product
- no wallet power
- no trade/order authority
- no filing authority
- human review required
- research or evidence view only

## Agent workflow

Before publishing or committing public-copy changes:

1. Read this file and `AGENTS.md`.
2. Edit `_astro-source` source first.
3. Rebuild with `npm run build`.
4. Sync `dist` to the root static output when required by this repo.
5. Run `npm run test:public-copy`.
6. Do not stage unrelated `site-agent/` notes.
7. Commit/push only when explicitly asked.

# Bionic Banker Public Copy Standard

Bionic Banker is a public AI + finance + compliance/risk platform. Public pages should sound like a serious risk, evidence, monitoring, and audit system — not a proof/lab/demo/hacker toy.

## Core standard

Use public language that a compliance, risk, data, audit, or governance buyer would recognize:

- risk assessment
- wallet screening
- transaction monitoring
- risk signal
- supporting evidence
- evidence record
- audit trail
- decision history
- controls
- monitoring
- reporting
- limitation
- authority boundary
- reviewer-ready summary
- risk rationale

Every public claim should answer:

1. What is being assessed or monitored?
2. What evidence supports it?
3. What are the limits?
4. What authority is explicitly not granted?

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
- wallet authority: true
- trade authority: true
- roast / roaster / roasts, except in historical repository URLs that cannot be renamed safely

## Preferred replacements

- Proof Tour → Risk & Evidence Overview
- proof page → evidence page or status evidence page
- proof surface → evidence view
- proof path / proof route → evidence workflow or system overview
- proof → supporting evidence, evidence record, verification, audit trail, or benchmark result
- Wallet Risk Lab → Wallet Risk Assessment
- Live Signals → Risk Signals or Market & Risk Signals
- Experiments → Systems, Case Studies, Workflows, or Field Notes
- AI Learning → Knowledge Base
- receipt → evidence record or audit entry
- roast / roaster → risk note, assessment note, risk-note generator, reviewer-ready summary, risk rationale
- truth layer → evidence layer, review layer, or verification layer
- clean wallet / safe wallet → lower-risk wallet, no current risk signal, no elevated signal in this sample
- demo → public demonstration, prototype, walkthrough, or reproducible example
- lab → system, sandbox, research environment, or controlled environment

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
- no wallet authority
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

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


## Article and concept discipline

Every public concept page should end with source links, internal records, limits, and a next read. This turns strong ideas into a reader path instead of another isolated note. The order is: source links first, internal records second, limits third, next read last.

## Uncertainty and source honesty harness

Bionic Banker should sound correct before it sounds confident. Public copy must separate what is known, what is checked, what is missing, and what the system cannot decide.

Use these rules for every page, article, report, card, and public announcement:

1. If a fact is not fully checked, say so clearly instead of writing it as settled.
2. If the answer depends on missing context, name the missing context.
3. If multiple explanations are plausible, show the main possibilities rather than pretending there is only one.
4. Do not invent paper titles, URLs, authors, studies, statistics, books, legal cases, quotes, company reports, or historical references.
5. A number, date, article count, status, source label, or public claim needs a source file, public source link, or explicit `not verified yet` label.
6. A page can be useful with a missing source; it is not allowed to hide the missing source.

Preferred public phrases:

- `Based on the public source trail...`
- `This page can show...`
- `This page cannot decide...`
- `The missing context is...`
- `This is a source note, not a conclusion.`
- `This should be verified before it becomes a public claim.`

Blocked public behavior:

- invented citations;
- exact statistics with no source trail;
- legal/compliance conclusions without review;
- confident claims about wallet intent, fraud, approval, compliance, or safety when the page only has a partial signal;
- language that implies Bionic Banker can decide, approve, trade, file, or act by itself.

## Explanation ladder

When a page explains a hard finance, AI, wallet, or agent concept, use this ladder before adding polish:

1. Name the thing in plain words.
2. Show what the reader sees on the page.
3. Explain what is happening underneath.
4. Point to the record, log, check, or source trail.
5. Name the limit in a normal sentence.

This is the house style: start from the screen, move to the system, then show the check and the limit. Do not copy outside books, sites, or articles. Learn from clear teaching patterns, then write in Hash's voice: direct, cautious, practical, and simple enough that a reader can repeat it back.

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

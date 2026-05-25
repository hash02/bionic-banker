# Layer 4 Opportunity Engine Goals

## Purpose

Convert Bionic Banker from a polished Layer 3 public proof surface into a Layer 4 opportunity engine: a site a cold recruiter, collaborator, executive, investor, or serious learner can inspect in 90 seconds and understand why Hash is worth a conversation.

## Goal 1 — Single reviewer entry point

**Ship `/start-here`.**

A cold reader should see:

- the one-line thesis: AI-assisted finance risk workflows that show their work and keep humans in control
- the recommended review path
- what each flagship system proves
- what the site does not claim
- which conversations Bionic Banker is best suited for

**Done when:** `/start-here` exists, is linked from homepage/navigation, and gives a complete 90-second reviewer path.

## Goal 2 — Public proof pack

**Ship `/proof-pack`.**

A reader who does not want to click ten routes should get a compressed proof packet:

- positioning
- flagship systems
- evidence map
- technical stack
- risk/compliance boundaries
- questions to ask Hash

**Done when:** `/proof-pack` exists, links to the flagship routes, and preserves public-safe boundaries.

## Goal 3 — Homepage conversion path

**Make the homepage route people to the right next click.**

The homepage should direct four reader types:

- recruiter: inspect skill signals and project evidence
- collaborator: inspect workflows and integration boundaries
- executive/investor: inspect category and risk-control narrative
- technical reviewer: inspect source, traces, and QA gates

**Done when:** homepage links to `/start-here` and `/proof-pack`, and the hero CTA no longer forces every reader into raw exploration.

## Goal 4 — Flagship reviewer questions

**Make flagship pages/cards answer the question a reviewer is silently asking.**

Default reviewer questions:

- Wallet Risk: Can Hash reason about risk signals?
- AML Status Evidence: Can Hash preserve auditability and authority boundaries?
- Fraud Alert Triage: Can Hash turn alerts into review-ready packets?
- Agent Chess / Agent Workflow: Can Hash design human-gated agent operations?
- Site Health / Proof QA: Can Hash build public systems that check themselves?

**Done when:** flagship cards and reviewer pages include explicit reviewer-question framing.

## Goal 5 — Deterministic proof of the opportunity layer

**Add a checker so the conversion layer does not drift.**

The gate should verify:

- `/start-here` source exists and contains the thesis, flagship path, audience categories, and boundaries
- `/proof-pack` source exists and contains positioning, systems, evidence map, stack, boundaries, and questions
- homepage source links to both routes
- built static HTML exists after build/sync

**Done when:** the checker is wired into `npm test` and all existing QA gates pass.

## Current completion status

Implemented in the `Layer 4 opportunity engine` sprint:

- `/start-here` reviewer guide
- `/proof-pack` public proof pack
- homepage entry points
- navigation/footer/mobile links
- flagship reviewer-question card framing
- deterministic opportunity-layer checker
- build/test/mobile/browser/live verification

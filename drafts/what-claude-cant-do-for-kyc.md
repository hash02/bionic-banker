---
title: "What Claude Can't Do for KYC Yet (And Why That Matters for Canadian Banks)"
description: "AI can read documents and flag issues. Production KYC is a bigger system: screening, case review, audit trail, and accountability."
date: "2026-05-22T12:00:00-07:00"
tags: ["AI", "Banking", "Compliance", "KYC", "AML", "Canada"]
readTime: "7 min"
category: "AI"
draft: true
---

# What Claude Can't Do for KYC Yet (And Why That Matters for Canadian Banks)

Okay so here is the thing.

Most AI demos for KYC look amazing for about 90 seconds.

You upload a passport. The model reads the name, date of birth, address, maybe the expiry date. It spots a mismatch. It gives a clean little summary. Maybe it says "high risk" or "needs review."

And if you are watching from the outside, it feels like the whole KYC problem is almost solved.

But if you have worked near the banking side of it, you know that is only the front door.

The real KYC problem is not "can a model read a document?"

The real question is: can the system prove why it accepted or rejected a person, keep that proof, route the weird cases to a human, and still explain the decision months later when someone asks?

That is the part most demos skip.

And honestly, I get why. The skipped part is not as pretty. It is not a clean upload screen. It is not one prompt. It is a chain.

## The Demo Version

The demo version of KYC is simple.

1. Upload document.
2. Extract fields.
3. Compare fields.
4. Flag mismatch.
5. Done.

That is useful. I do not want to minimize it.

A model that can read messy documents, normalize names, catch expiry dates, and explain inconsistencies is valuable. It saves time. It gives analysts a better first pass. It can reduce the boring part of review.

But calling that "KYC solved" is like looking at a receipt scanner and saying accounting is solved.

The scanner helps. It does not close the books.

In banking, the hard part is what happens after extraction.

What if the name matches, but the person is politically exposed?

What if the document looks fine, but the customer owns a company with a hidden beneficial owner?

What if the customer passes onboarding, then starts moving funds in a pattern that looks like layering?

What if the model flags something, but the reviewer disagrees?

What if six months later a regulator asks why the file was approved?

That is where the demo stops and production starts.

## The Production Chain

The clean way to think about KYC is as an eight-step chain.

<!-- INFOGRAPHIC: kyc-production-chain - pending render -->

1. Collect identity evidence.
2. Extract and normalize fields.
3. Screen against sanctions, PEP, adverse media, and internal risk lists.
4. Check document authenticity and liveness where needed.
5. Link the customer to accounts, wallets, counterparties, and transaction behavior.
6. Route exceptions to human review.
7. Preserve a regulator-readable audit trail.
8. Monitor after onboarding.

Most AI demos are strongest at step 1 and step 2.

That is the "look, it read the passport" moment.

My AML Engine sits somewhere else. It does not verify identity documents. It does not do biometrics. It does not decide whether someone should be onboarded.

It is a transaction-risk layer.

It maps wallet behavior patterns like sanctions exposure, mixer touch, bridge hops, peel chains, smurfing, phishing hits, machine-like cadence, sybil fan-in, address poisoning, and other movement patterns.

So in that eight-step chain, it fits closer to step 5 and step 8.

It helps answer:

What is this wallet doing?

Does the movement pattern look normal?

Did funds touch a risky path?

Is this customer behavior changing after onboarding?

That is valuable. But it is not the whole KYC stack.

And that distinction matters.

<!-- INFOGRAPHIC: aml-engine-placement - pending render -->

## The Missing Middle

The missing middle is where banks actually live.

Sanctions screening is not just "does this wallet touch an OFAC-listed address?"

That is one signal. A strong one, but still one signal.

A production screening system has to handle names, aliases, dates of birth, countries, entities, fuzzy matches, source list timestamps, false positives, and reviewer notes. The exact setup depends on the institution and the product, but the shape is always bigger than a single model answer.

PEP screening has the same problem. It is not only "is this person on a list?" FINTRAC guidance talks about politically exposed persons, heads of international organizations, family members, and close associates. That means a real system has to think about relationships, ownership, control, role changes, geography, and timing.

Case management matters because not every flag is a final answer. A flag is the start of a decision.

Someone has to decide:

Is this a true match?

Is it a false positive?

Do we need more documents?

Do we decline?

Do we file a report?

Do we keep monitoring?

And then the system has to remember that decision.

Not in a chat message. Not in a screenshot. In a case record with evidence, timestamps, reviewer identity, reason codes, and the final outcome.

That is what I mean when I say AI is not enough by itself.

The model can help read. It can help explain. It can help summarize. But the institution needs the control layer around it.

## Why Canadian Banks Care

Canada is a careful banking market.

That can be frustrating if you are building fast. But it also means the bar for trust is real.

A Canadian bank cannot treat KYC like a hackathon demo.

The system has to survive internal audit. It has to survive regulator questions. It has to fit into FINTRAC obligations around client identification, beneficial ownership, suspicious transaction reporting, ongoing monitoring, and record keeping.

That does not mean every KYC process is perfect. It means the output has to be explainable in a banking language.

Not:

"Claude said it was okay."

But:

"Here is the customer evidence. Here are the fields. Here are the screening results. Here is why the match was accepted or dismissed. Here is the reviewer. Here is the timestamp. Here is the ongoing monitoring state. Here is what changed."

That is the difference between an AI assistant and a compliance system.

One gives an answer.

The other leaves a trail.

## The Double View

This is the part I keep coming back to because I sit in a weird place.

On one side, I work inside banking. I see how slowly real systems move, and why they move slowly. It is not always because people lack imagination. Sometimes it is because the system has to answer to things the demo never sees.

On the other side, I build these engines myself.

I built an AML rules engine because I wanted to understand what a real detection layer looks like. Not a generic "AI will catch fraud" line. Actual rules. Actual behavior. Actual wallet patterns. A manifest that says what the system can and cannot do.

That second part made me more humble about the first part.

Because when you build even one slice honestly, you see how much the full stack needs.

My engine can tell you a wallet looks risky.

It cannot tell you the person holding the passport is real.

It cannot tell you the beneficial owner behind a business is clean.

It cannot manage the case queue.

It cannot file a report.

It cannot replace the human reviewer.

And that is fine.

The right answer is not to pretend one model does everything.

The right answer is to put each piece where it belongs.

## What Closing The Gap Looks Like

If I were designing the real version, I would not start with "one AI agent does KYC."

I would build it as modules.

First, a document intake layer. It reads documents, extracts fields, normalizes names, and keeps the raw evidence.

Second, a screening adapter. Sanctions, PEP, adverse media, internal lists, source timestamps, match scores, and explanations.

Third, a transaction-risk layer. That is where something like my AML Engine belongs. Wallets, counterparties, flow patterns, risk rules, ongoing behavior.

Fourth, a case store. Every flag becomes a case event. Every decision has a reviewer, reason, timestamp, and evidence pointer.

Fifth, a human review lane. The model can suggest. The human approves, rejects, escalates, or asks for more.

Sixth, an audit log. Not because audit logs are exciting. Because without one, the system cannot prove itself later.

That is the real KYC AI product.

Not a chatbot.

Not a document reader.

A controlled decision system with AI inside it.

## The Honest Take

I am bullish on AI in compliance.

Very bullish.

But I am not bullish on the lazy version of the story.

The lazy version says: "AI reads KYC docs, so KYC is automated."

The real version says: "AI can reduce the manual load in parts of KYC, but production KYC needs screening, review, evidence, audit, and ongoing monitoring."

That difference is not small.

It is the whole thing.

And for Canadian banks, that difference is where the opportunity is.

The bank that wins will not be the one with the flashiest document extraction demo.

It will be the one that can connect identity, transaction behavior, human review, and audit proof into one system that people inside the institution can actually trust.

That is what I am trying to build toward.

Not the demo.

The system behind the demo.

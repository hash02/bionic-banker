---
title: "How AML Detection Works on Blockchain Rails"
description: "A plain report on the AML engine: rules, anomaly detection, triage, known cases, and what the limits taught me."
date: "2026-02-27"
tags: ["AML", "Blockchain", "AI"]
readTime: "9 min"
category: "Finance"
featured: true
slug: "aml-engine"
image: "/blog-visuals/aml-engine/social-preview.png"
---

AML detection is not one universal score. It is a three-layer system: 28 detection rules that catch known patterns, a machine learning anomaly layer that flags unusual behavior even when no rule fires, and a triage layer that decides which cases a human analyst should read first.

That is what I built here. A blockchain AML engine that reads public transaction data, maps suspicious behavior into explainable signals, and shows why a wallet or transaction deserves a closer look.

The useful part is not only the flag.

The useful part is the sentence under the flag. A score without a reason is just a number with anxiety attached.

## The question that started it

I started with a simple question about mixers.

If a blockchain is public, how does money still get hidden?

That question led to Tornado Cash, bridge exploits, wallet clusters, sanctioned addresses, and the strange feeling of watching real financial crime leave public traces.

At first, the engine was tiny. A few simple rules. Large transactions. Known risky addresses. Fast movement.

That was enough to learn the shape of the problem.

Every false positive taught me where a rule was too wide. Every miss taught me where the data was too thin. The project kept growing because each case exposed one more pattern.

## How AML detection works

The engine has three layers.

Layer one is rules.

Rules catch patterns that are already understood: mixer contact, bridge hops, peel chains, OFAC hits, dormant wallet activation, coordinated bursts, smurfing, drainer behavior, address poisoning, and other known shapes.

Layer two is anomaly detection.

Some activity does not match a known rule, but it still looks strange compared with normal wallet behavior. That is where the model helps. It does not replace the rule layer. It catches shapes the rules did not name yet.

Layer three is triage.

Not every flag deserves the same attention. A direct sanctioned-address hit is not the same as a weak pattern three hops away. The triage layer groups signals so the most urgent cases rise first.

## The current rule map

The current manifest maps 28 detection abilities.

That number includes 23 direct `detect_` functions and 5 feature-stage abilities that are computed before the rules fire.

The direct rules cover things like:

- mixer touch
- bridge hops
- peel chains
- OFAC hits
- flash-loan bursts
- coordinated bursts
- dormant activation
- wash cycles
- smurfing
- exchange avoidance
- phishing hits
- sub-threshold tranching
- machine cadence
- sybil fan-in
- drainer signatures
- address poisoning

The feature-stage abilities look at wallet behavior: velocity, amount distribution, time gaps, counterparty shape, and address profile.

That is the part I like. The engine is not only asking, "Did this exact bad thing happen?"

It is also asking, "Does this wallet move like a normal wallet?"

## The cases I used

The early case studies were public blockchain events.

Ronin showed bridge movement and wallet clustering.

Tornado Cash showed direct mixer contact and the harder question of what happens after funds leave the mixer.

Wormhole showed fast high-value movement through bridge-related behavior.

Nomad showed a crowd pattern, where many wallets copied the same opportunity in a short window.

I used those cases because they were concrete. Not abstract crime typologies. Actual public traces.

When a rule fired, I could go back to the transaction and ask: does this make sense, or did I build a noisy detector?

That loop mattered more than the first score.

## What the anomaly layer adds

Rules are good at known patterns.

But financial crime does not always repeat itself neatly.

The anomaly layer looks for behavior that does not fit the normal baseline. High amount, unusual timing, strange sender behavior, new wallet activity, or a shape that looks rare even when no blacklist is involved.

That does not mean the transaction is criminal.

It means the transaction is worth reading.

That distinction matters. AML tooling should not pretend every flag is a verdict. A flag is a route into review.

## Why triage matters

If a system flags everything, it helps no one.

The problem is not only detection. The problem is attention.

So the engine groups signals into tiers. The names came from gaming because that made the idea obvious: start with the highest-signal cases, then move down.

The point is simple.

One analyst should not have to read every row in order. The system should help them open the strongest rows first and understand why those rows rose to the top.

## The limit

The hardest lesson was that some misses are not rule problems.

Sometimes the data is at the wrong resolution.

A flash-loan attack can happen inside one block. If your system mainly reads transaction sequences over time, it may be looking at the right event through the wrong lens.

That taught me something useful.

You cannot patch a data gap with more confidence. You need better data.

For some patterns, transaction-level monitoring is enough. For others, you need block-level context, contract traces, or a different way to read the event.

## What this is and is not

This is a public research engine.

It reads patterns, fires rules, adds anomaly signals, and explains why a row is worth attention.

It is not an auto-decision system. It does not replace an analyst. It does not say a wallet is guilty. It does not make claims about private customer data.

The clean version of the goal is smaller and stronger:

Show the signal. Show the reason. Show the limit.

## The note I keep coming back to

Blockchain AML is interesting because the data is public but the story is still hard.

You can see the movement. That does not mean you understand it.

The job is to turn movement into readable risk without pretending the system knows more than it does.

That is the lane I keep returning to.

A good detection engine should not only say, "look here."

It should say, "look here, because this pattern moved this way, and here is where the signal stops."

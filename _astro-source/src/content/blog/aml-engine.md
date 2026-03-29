---
title: "I Built a Blockchain AML Engine From Scratch"
description: "94.9% detection rate. 22 rules. Real Etherscan data. Caught Tornado Cash, Ronin, Lazarus Group. Here's what an engineer inside finance found building what compliance teams actually need."
date: "2026-02-27"
tags: ["AML · Blockchain · AI"]
readTime: "12 min"
category: "Tech"
featured: true
slug: "aml-engine"
image: "/blog-visuals/aml-engine/social-preview.png"
---

I work at a bank. I had no plan to build a fraud detection system. I just started asking questions—and one question led to another, led to another, until I was literally looking at the wallets Lazarus Group used to move $625 million in stolen funds. This is that story.

---

Okay so — I need to be honest about how this actually started. There was no grand plan. No "I'm going to build a fraud detection engine" moment. It started way more simply than that.

I was just curious about Tornado Cash. The US Treasury had sanctioned it in 2022 and I kept seeing it in the news, but nobody was really explaining why. Like, what is it actually doing? What does the transaction look like? So I went to Etherscan — the public blockchain explorer — and just... started reading transactions.

That's it. That was the beginning. One question about a mixer.

And then one question became another. Okay, how do you actually hide money on a blockchain if everything is public? And then — if I can see these patterns, can I write rules to catch them? And then — what other crimes have left traces on-chain that nobody's officially analyzed? One dot to the next to the next to the next. Before I knew what was happening, I had 22 detection rules, a machine learning layer on top, and I was sitting at night looking at actual criminal wallets.

> "It's a Batman thing. You're sitting in your apartment at night, no badge, no authority, no warrant — just code and curiosity — and suddenly you're looking at $625 million in stolen funds moving across the blockchain in real time."

## What I Do at the Bank vs. What I Built at Home

Here's the thing about working in financial services — you see compliance every day. The reports, the reviews, the checkbox exercises. And there's a reason they exist. The regulations are serious, the stakes are real.

But there's also a gap. A big one. The way institutions monitor for financial crime and the way money actually moves on-chain — those two things are operating at completely different speeds. Banks run batch processes. Blockchain settles in seconds. That mismatch is where billions of dollars go missing every year.

I'm not saying the banks are doing it wrong. I'm saying the problem is genuinely hard, and the tools haven't caught up yet. That's actually what made me want to build something — not to criticize what already exists, but to understand what the next version of it could look like.

## How the Rules Work — and How I Built Them

Version 1 of the engine was embarrassingly simple. Three rules. Flag high-value transactions, check against known blacklists, flag high-risk country interactions. Done.

The thing is — that's exactly where you should start. When your system is that simple, every mistake teaches you something clean. No complexity to hide behind. Every false positive is a lesson. Every miss is a lesson. You figure out exactly why a rule works, and exactly where it breaks.

By version 6 the engine was covering the major attack categories — structuring (breaking large amounts into smaller pieces to avoid detection thresholds), mixing (Tornado Cash and similar tools that sever the transaction trail), cross-chain bridging (moving funds across different blockchains to lose the trail), velocity attacks (flooding a system with rapid transactions), OFAC-listed wallets, and blockchain-specific patterns like flash loans.

Every new version came from a new case study. Read the case. Understand the pattern. Write the rule. Test it against the data. Repeat. Eleven versions later — 22 rules, covering 6 attack categories, running against real Etherscan data.

## The Engine Architecture

The system has three layers working together:

**Layer 1 — Rule Engine:** 22 rules across structuring, mixing, bridging, velocity, OFAC, and blockchain-specific patterns.

**Layer 2 — AI Detection Layer:** Isolation Forest algorithm. Catches what rules miss. 21 novel detections found purely through statistical anomalies.

**Layer 3 — Dynamic Triage:** LEGENDARY (high-risk), RARE (medium-risk), MAGIC (suspicious), COMMON (low-risk). Reduces analyst queue by 63% without losing a single high-priority case.

## The Cases — When It Got Real

This is where the project changed for me. Testing against real blockchain data from actual hacks — not simulated, not theoretical. Real events, real wallets, real money.

### Ronin Network — Lazarus Group (North Korea)

$625M stolen by compromising validator keys on the Ronin bridge. The engine caught the wallet cluster patterns and cross-chain movement. Each hop through multiple wallets triggered a different rule — it was like following a trail that was trying not to be a trail.

### Tornado Cash — OFAC-Sanctioned Mixer

Direct hits on the Tornado Cash contract flagged immediately. The more interesting part was detecting wallets one hop removed — wallets that had already been "cleaned." The engine learned to recognize the shape of a post-mixer wallet, not just the mixer itself.

### Wormhole Bridge Exploit

$320M via a cross-chain bridge vulnerability. The tell was the velocity — abnormal burst of high-value transactions in a short window, destination wallets with zero prior history. Two rules firing at the same time: velocity anomaly + new wallet cluster.

### Nomad Bridge — The Copycat Attack

What made Nomad interesting was the crowd effect. Once one hacker found the vulnerability, hundreds of copycat wallets drained the bridge within hours. The signature: dozens of different wallets, same destination contracts, same time window. Organized opportunism.

## The Ceiling — and Why It's Actually the Most Interesting Part

At 94.9% detection, I hit a wall. Two cases the engine couldn't fully crack. And honestly — this is where I learned the most.

Euler Finance used a flash loan attack. One atomic transaction: borrow, exploit, repay, all within a single block. The engine's rules look at sequences of transactions over time. A single-block attack has no sequence. There's nothing to follow because it all happened in one moment — faster than any monitoring system can track.

That's not a rule problem. That's a data problem. To catch flash loan attacks you need block-level data, not just transaction-level data. I was looking at the right thing at the wrong resolution.

**The thing I actually learned:** 94.9% isn't a failure at 5.1% — it's a diagnosis. The missing 5.1% told me exactly what data I needed next. Every ceiling in detection is a map to the next layer of the problem. You can't write your way past a data gap with more rules. You have to go get the data.

## Adding the AI Layer — Teaching the Machine What Normal Looks Like

Rules catch what you already know. The AI layer was about catching what I didn't know I didn't know.

I used an Isolation Forest — an unsupervised machine learning model. The way it works is almost elegant in its simplicity: show it thousands of normal transactions until it understands what normal looks like, then let it flag whatever doesn't fit that shape. No labels needed. No examples of fraud needed. Just pattern recognition over a massive normal baseline.

The AI found 21 transactions that zero rules had touched. Pure statistical outliers. The most interesting one: a single billion-dollar transaction, no OFAC match, no mixer interaction, no velocity pattern. Just a wallet doing something statistically impossible given everything else in the dataset. AI confidence: 79.8. Rule hits: zero.

That's the whole point of having both. Rules catch known patterns. AI catches unknown shapes. You genuinely need both — they're not competing, they're covering different parts of the problem space.

## The Triage System — I Stole This From Gaming

695 flagged transactions. One analyst. Where do you start?

If you've played any RPG you already know the answer. Items have rarity tiers — Legendary, Rare, Magic, Common. You always open the Legendary items first. Not because the others don't matter, but because expected value is highest at the top tier.

So I built a scoring system that maps directly to that logic. Every flagged transaction gets a confidence score across four dimensions: how many rules fired, how large the amount, how frequently the sender shows up in other suspicious activity, and what the AI layer said. When multiple dimensions fire at the same time, the score escalates — not linearly, but with a combination bonus. The more signals converging, the higher the tier.

Result: out of 695 flagged cases, 256 genuinely needed immediate human attention. 63% queue reduction without losing a single high-priority case. The analyst goes straight to the Legendary tier and knows they're looking at the real risk first.

## What I'm Building Next

The engine is at v11. The architecture is three layers deep. But this is still version one of a bigger thing.

The live demo is now up — you can run the engine on real transaction data, right in your browser. Upload a CSV or hit the sample data button and watch Wormhole, Ronin, and Lazarus Group get flagged in real time. Every rule that fires is explained. Every score is broken down. No setup, no install.

Next: connecting to live blockchain data so the engine runs continuously, not just on batch uploads. After that: a symbolic reasoning layer — something I've been building in parallel — that audits AI reasoning chains the same way this engine audits transaction chains. Same architecture, different domain.

The full codebase is open on GitHub. Every rule, every version, every case study documented. If you're building in this space, it's yours to learn from.

> "It started as an innocent question about how stablecoins work. I had no plan. I was just following one dot to the next to the next. That's the whole point — you don't need to know where you're going. You just need to be curious enough to follow the trail."

If you're reading this and you work in compliance, fintech, or blockchain — the gap between how fast money moves on-chain and how fast institutions respond is real, and it's closing whether everyone's ready or not. The tools to close it exist. They're just not in the compliance handbook yet.

And if you're a millennial or Gen Z reading this at night, wondering if you can build something that actually matters without a big team or a title — yeah. You can. The blockchain is public. The data is there. The tools are free. The only thing between you and catching real financial crime is curiosity and enough patience to follow the dots.

---
title: "I Built a Blockchain AML Engine From Scratch"
description: "94.9% detection rate. 22 rules. Real Etherscan data. Caught Tornado Cash, Ronin, Lazarus Group. Here's what an engineer inside finance found building what compliance teams actually need."
date: "2026-03-01"
tags: ["AML · Blockchain · AI"]
readTime: "12 min"
category: "Tech"
featured: true
slug: "aml-engine"
---

Okay so — I need to be honest about how this actually started. There was no grand plan. No "I'm going to build a fraud detection engine" moment. It started way more simply than that.

    
I was just curious about Tornado Cash. The US Treasury had sanctioned it in 2022 and I kept seeing it in the news, but nobody was really explaining *why*. Like, what is it actually doing? What does the transaction look like? So I went to Etherscan — the public blockchain explorer — and just... started reading transactions.

    
That's it. That was the beginning. One question about a mixer.

    
And then one question became another. Okay, how do you actually hide money on a blockchain if everything is public? And then — if I can see these patterns, can I write rules to catch them? And then — what other crimes have left traces on-chain that nobody's officially analyzed? One dot to the next to the next to the next. Before I knew what was happening, I had 22 detection rules, a machine learning layer on top, and I was sitting at night looking at actual criminal wallets.

    
      "It's a Batman thing. You're sitting in your apartment at night, no badge, no authority, no warrant — just code and curiosity — and suddenly you're looking at $625 million in stolen funds moving across the blockchain in real time."

---
title: "My AML Engine Doesn't Just Flag Wallets. It Roasts Them."
description: "94.9% detection rate meets zero patience. The AML Roaster scans Ethereum wallets, flags suspicious patterns, and delivers compliance-grade analysis with attitude."
date: "2026-03-08"
tags: ["AML · AI · Blockchain"]
readTime: "8 min"
category: "Tech"
featured: false
slug: "aml-roaster"
---

Okay so — here's a number that should bother you more than it does.

    
$82 billion was laundered through cryptocurrency in 2025. That's up from $40 billion the year before — a 105% jump. And globally, somewhere between $800 billion and $2 trillion gets laundered every year across all channels. The UN estimates less than 1% of it gets caught.

    
Let that sit for a second. Less than one percent.

    
The systems we have for catching money laundering — the compliance reports, the transaction monitoring, the risk scores — they exist. They work, technically. But they generate reports that nobody actually reads. Same corporate font, same passive voice, same "the transaction exhibited characteristics consistent with potential structuring activity." The compliance officer skims it, checks a box, moves on. The investigator glances at the score and goes with gut feel anyway.

    
Crime is evolving faster than compliance can keep up. And the gap isn't intelligence — we have the data, we have the models, we have the rules. The gap is that the output is so boring that the humans in the loop check out before the signal lands.

    
So I did something kind of stupid. I built an AML engine that roasts suspicious wallets. Like, actually roasts them — sarcastic, pointed, impossible to ignore.

    
And somehow it's the best compliance tool I've ever made.

    <!-- ═══════════════ STATS EMBED ═══════════════ -->
    
      </iframe>
      
        2024/2025 Crypto AML data — CoinLaw, Chainalysis, UN/UNODC, TRM Labs
        Interactive
      
    

    
## The scale of what we're fighting

    
Before I get into the build, you need context on why this matters beyond a fun side project.

    
The Lazarus Group — North Korea's state-sponsored hacking operation — has stolen over $6.75 billion in crypto since 2017. In February 2025 alone, they hit Bybit for $1.5 billion. One hack. That single heist was bigger than everything they stole across 47 separate incidents in all of 2024.

    
Tornado Cash — one of the main mixers my engine watches — processed over $7 billion in transactions before OFAC sanctioned it in 2022. Here's the twist though: in March 2025, OFAC actually removed Tornado Cash from the sanctions list after a court ruled they overstepped their authority. But the criminal prosecutions continue. Roman Storm got convicted. Samourai Wallet founders got 4-5 years each.

    
The regulatory landscape is shifting under everyone's feet while the crime scales exponentially. That's the environment this engine operates in.

    <!-- ═══════════════ TORNADO CASH EMBED ═══════════════ -->
    
      </iframe>
      
        How a crypto mixer works — Tornado Cash timeline and watchlist
        Interactive
      
    

    
## What the engine actually does

    
The AML Roaster is a real detection system. 13 active rules, scanning Ethereum mainnet every 30 minutes via GitHub Actions. It watches 11 addresses — Tornado Cash pools, OFAC-flagged entities, Lazarus Group wallets, the Ronin Bridge exploiter.

    
When it finds something suspicious, it does what any AML system does: assigns a risk score, tags the rules that fired, generates a report.

    
But then it does something different. It sends the finding to an LLM and says: explain what happened like you're telling a friend at a bar. Then roast them.

    
Here's an actual roast from a real scan — a wallet that sent five identical zero-value transactions to Tornado Cash's 0.1 ETH pool:

    
      
"It takes a special kind of genius to send five identical transactions of 0.0000 ETH to a sanctioned mixer — I mean, who needs actual money when you can just smurf your way to OFAC's bad side? The structuring pattern is just the cherry on top, because who doesn't love a good game of 'let's make all our transactions look identical.'"

      
        Risk Score: 530 — CRITICAL
        Rules fired: 6/13
        Mixer + OFAC + Structuring
      
    

    
That's not a report you skim.

    
## Why humor is actually the missing layer

    
This isn't a gimmick. There's a real insight underneath it.

    
The problem with traditional AML output isn't that it lacks information — it has too much. A wall of technical text triggers the same response in everyone: glazed eyes, checkbox mentality, move to the next one. The signal drowns in its own formatting.

    
The roast forces the AI to actually understand what happened. You can't roast something you don't understand. Try writing a sarcastic take on "the wallet exhibited layering characteristics" — you can't. But if you understand that someone sent five empty transactions to a mixer like they're testing the waters before doing something real? Now you've got material.

    
And the person reading it? They remember it. You'll forget "risk score 530, OFAC sanctions match, structuring detected" by tomorrow. You won't forget the wallet that smurfed its way to OFAC's bad side.

    
> *"The hard part was never making the AI smarter. It's making the output worth a human's time. We're drowning in AI-generated text that nobody reads. The bottleneck isn't intelligence. It's engagement."*

    
## The pipeline

    <!-- ═══════════════ PIPELINE EMBED ═══════════════ -->
    
      </iframe>
      
        From Ethereum block to roast report — the 5-stage pipeline
        Interactive
      
    

    
**Scan** — Python script, every 30 minutes via GitHub Actions. Hits Etherscan for recent blocks, checks transactions against 11 watched addresses. Applies 13 detection rules: mixer contact, sanctions match, structuring, peel chains, exchange avoidance, stablecoin mixing, contract interaction patterns.

    
**Score** — Each rule has a weight. Mixer touch is +100, OFAC hit is +200, structuring is +70. Scores compound. A wallet hitting multiple rules climbs fast — 400+ is CRITICAL.

    
**Roast** — The finding goes to an LLM with context: rules triggered, scores, transaction details. It generates a plain-English summary, the roast, and a risk verdict with recommended action. This is where the dry data becomes something you actually want to read.

    
**Dashboard** — Single-page HTML, auto-updates from the scan data. Three stats, roast cards with the actual text, two charts. Minimal, clean.

    
**Storage** — Every scan appends to a JSON file. Markdown reports get generated per scan. The whole thing runs on GitHub Actions' free tier — zero infrastructure cost.

    
The entire system is automated. I don't touch it. Every 30 minutes it wakes up, scans Ethereum, checks the watchlist, and if it finds something, it roasts it.

    
## What it caught

    
In 24 scans so far, it found 2 CRITICAL wallets — both interacting with Tornado Cash's 0.1 ETH pool. One sent 5 identical zero-value transactions (score: 530, six rules fired). Another sent 2 zero-value calls (score: 400, four rules).

    
Zero-value transactions to a mixer are interesting because they're not moving money. They're probing — testing the contract, or relaying for someone else. The engine caught both and the roasts made the difference obvious: one was "smurfing to OFAC's bad side," the other was "spinning dirty laundry on a budget."

    
That kind of plain-language distinction is what turns a detection system into an investigation tool. The rules catch the pattern. The roast explains why you should care.

    
## AI is about to change how we interact with crime data

    
Here's the bigger picture and why I think this matters beyond one engine.

    
We're at this weird inflection point where AI can process massive amounts of financial data in real-time — but the way we present that information to humans hasn't changed since the 90s. Same spreadsheets, same PDF reports, same dashboards with red and green numbers.

    
What happens when AI doesn't just detect patterns but explains them in a way that makes investigators actually engage? What happens when every suspicious transaction comes with context, personality, and a recommendation that reads like a colleague briefing you instead of a system alert?

    
The way we interact with crime data — and honestly, with all monitoring data — is about to fundamentally change. Not because the models get smarter, but because someone finally makes the output worth reading.

    
That's what the Roaster proved to me. The detection was always possible. The rules work. The scoring works. The thing that was missing — the thing that makes a human actually stop and pay attention — is voice.

    
And once you see that, you start seeing it everywhere. Security alerts nobody reads. Fraud flags that get auto-dismissed. Monitoring dashboards that exist to satisfy auditors, not to actually inform anyone. The problem is always the same: the output doesn't respect the human's attention.

    
$82 billion laundered through crypto last year. Less than 1% caught globally. Maybe the answer isn't better algorithms. Maybe it's making the existing ones impossible to ignore.

    <!-- ═══════════════ FOOTER CTA ═══════════════ -->
    
      
The AML Roaster is open source and runs live.

      
The roaster scans Ethereum every 30 minutes. The full AML Detection Engine (22 rules, 94.9% detection rate) has a live demo. I write about building at the intersection of AI, blockchain, and finance.

      
        [
          AML Roaster — GitHub
        ](https://github.com/hash02/aml-roaster)
        [
          Full AML Engine →
        ](https://github.com/hash02/aml-detection-engine)
        [
          Live Demo →
        ](https://aml-detection-engine-ewxnmkbekcg8scjjes7caa.streamlit.app/)

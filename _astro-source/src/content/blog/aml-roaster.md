---
title: "My AML Engine Turns Wallet Flags Into Risk Notes."
description: "A blockchain AML monitoring workflow that scans suspicious Ethereum patterns, explains triggered rules, and produces reviewer-ready risk notes."
date: "2026-03-08"
tags: ["AML · AI · Blockchain"]
readTime: "8 min"
category: "Tech"
featured: false
slug: "aml-roaster"
---

This is a report on a blockchain AML engine that does something most compliance tools refuse to: it scans suspicious Ethereum patterns using 28 detection rules, scores the wallet, then explains what it found in language a human analyst cannot ignore.

Okay so — here is a number that should bother you more than it does.

    
$82 billion was laundered through cryptocurrency in 2025. That's up from $40 billion the year before — a 105% jump. And globally, somewhere between $800 billion and $2 trillion gets laundered every year across all channels. The UN estimates less than 1% of it gets caught.

    
Let that sit for a second. Less than one percent.

    
The systems we have for catching money laundering — the compliance reports, the transaction monitoring, the risk scores — they exist. They work, technically. But they generate reports that nobody actually reads. Same corporate font, same passive voice, same "the transaction exhibited characteristics consistent with potential structuring activity." The compliance officer skims it, checks a box, moves on. The investigator glances at the score and goes with gut feel anyway.

    
Crime is evolving faster than compliance can keep up. And the gap isn't intelligence — we have the data, we have the models, we have the rules. The gap is that the output is so boring that the humans in the loop check out before the signal lands.

    
An AML engine can turn suspicious-wallet signals into plain-language risk notes: direct, readable, and difficult to ignore.

    
The useful part is not novelty. It is that the output becomes clear enough for a human reviewer to act on.

    <!-- ═══════════════ STATS EMBED ═══════════════ -->
    
      </iframe>
      
        2024/2025 Crypto AML data — CoinLaw, Chainalysis, UN/UNODC, TRM Labs
        Interactive
      
    

    
## The scale of what we're fighting

    
Before the system details, the operating context matters.

    
The Lazarus Group — North Korea's state-sponsored hacking operation — has stolen over $6.75 billion in crypto since 2017. In February 2025 alone, they hit Bybit for $1.5 billion. One hack. That single heist was bigger than everything they stole across 47 separate incidents in all of 2024.

    
Tornado Cash — one of the main mixers my engine watches — processed over $7 billion in transactions before OFAC sanctioned it in 2022. Here's the twist though: in March 2025, OFAC actually removed Tornado Cash from the sanctions list after a court ruled they overstepped their authority. But the criminal prosecutions continue. Roman Storm got convicted. Samourai Wallet founders got 4-5 years each.

    
The regulatory landscape is shifting under everyone's feet while the crime scales exponentially. That's the environment this engine operates in.

    <!-- ═══════════════ TORNADO CASH EMBED ═══════════════ -->
    
      </iframe>
      
        How a crypto mixer works — Tornado Cash timeline and watchlist
        Interactive
      
    

    
## What the engine actually does

    
The AML risk-note generator is a working detection system. 13 active rules, scanning Ethereum mainnet every 30 minutes via GitHub Actions. It watches 11 addresses — Tornado Cash pools, OFAC-flagged entities, Lazarus Group wallets, the Ronin Bridge exploiter.

    
When it finds something suspicious, it does what any AML system does: assigns a risk score, tags the rules that fired, generates a report.

    
But then it does something different. It sends the finding to an LLM and says: explain what happened in plain language, state the risk rationale, and recommend the next review action.

    
Here is an actual assessment note from a scan — a wallet that sent five identical zero-value transactions to Tornado Cash's 0.1 ETH pool:

    
      
"The wallet sent five identical zero-value transactions to a mixer address. The repeated pattern, sanctions exposure, and mixer contact raise critical review priority even though no value moved in these calls."

      
        Risk Score: 530 — CRITICAL
        Rules fired: 6/13
        Mixer + OFAC + Structuring
      
    

    
That is the kind of summary a reviewer can quickly understand and challenge.

    
## Why plain-language explanation matters

    
The core point is not style. It is reviewer comprehension.

    
The problem with traditional AML output isn't that it lacks information — it has too much. A wall of technical text triggers the same response in everyone: glazed eyes, checkbox mentality, move to the next one. The signal drowns in its own formatting.

    
The assessment note forces the system to explain what happened in operational terms. A phrase like "the wallet exhibited layering characteristics" is not enough. The useful version states that the wallet sent repeated zero-value transactions to a mixer, which may indicate probing before higher-value movement.

    
The reviewer gets both the numeric score and the reason it matters: repeated zero-value mixer interaction can be probing behavior, sanctions exposure, or preparation for larger movement.

    
> *The hard part is not only detecting the signal. It is making the evidence readable enough that a human reviewer can evaluate it, contest it, and decide what to review next.*

    
## The pipeline

    <!-- ═══════════════ PIPELINE EMBED ═══════════════ -->
    
      </iframe>
      
        From Ethereum block to risk assessment report — the 5-stage pipeline
        Interactive
      
    

    
**Scan** — Python script, every 30 minutes via GitHub Actions. Hits Etherscan for recent blocks, checks transactions against 11 watched addresses. Applies 13 detection rules: mixer contact, sanctions match, structuring, peel chains, exchange avoidance, stablecoin mixing, contract interaction patterns.

    
**Score** — Each rule has a weight. Mixer touch is +100, OFAC hit is +200, structuring is +70. Scores compound. A wallet hitting multiple rules climbs fast — 400+ is CRITICAL.

    
**Assessment Note** — The finding goes to an LLM with context: rules triggered, scores, and transaction details. It generates a clear summary, risk rationale, and recommended action. This is where dry data becomes reviewable context.

    
**Dashboard** — Single-page HTML, auto-updates from the scan data. Three stats, assessment cards with the actual text, and two charts. Minimal, clean.

    
**Storage** — Every scan appends to a JSON file. Markdown reports get generated per scan. The whole thing runs on GitHub Actions' free tier — zero infrastructure cost.

    
The entire system is automated. I don't touch it. Every 30 minutes it wakes up, scans Ethereum, checks the watchlist, and if it finds something, it generates a risk note.

    
## What it caught

    
In 24 scans so far, it found 2 CRITICAL wallets — both interacting with Tornado Cash's 0.1 ETH pool. One sent 5 identical zero-value transactions (score: 530, six rules fired). Another sent 2 zero-value calls (score: 400, four rules).

    
Zero-value transactions to a mixer are interesting because they're not moving money. They're probing — testing the contract, or relaying for someone else. The engine caught both and the risk notes made the difference obvious: one resembled structuring around sanctions exposure, while the other resembled low-value mixer probing.

    
That kind of plain-language distinction is what turns a detection system into an investigation tool. The rules catch the pattern. The assessment note explains why the reviewer should care.

    
## AI is about to change how we interact with crime data

    
Here's the bigger picture and why I think this matters beyond one engine.

    
We're at this weird inflection point where AI can process massive amounts of financial data in real-time — but the way we present that information to humans hasn't changed since the 90s. Same spreadsheets, same PDF reports, same dashboards with red and green numbers.

    
What happens when AI does not only detect patterns, but explains them with context, limitations, and a recommended next review step? What happens when every suspicious transaction comes with enough evidence for an investigator to inspect instead of another opaque alert?

    
The way we interact with crime data — and honestly, with all monitoring data — is about to fundamentally change. Not because the models get smarter, but because someone finally makes the output worth reading.

    
That is what the risk-note workflow showed me. The detection was always possible. The rules work. The scoring works. The thing that was missing — the thing that makes a human actually stop and pay attention — is voice.

    
And once you see that, you start seeing it everywhere. Security alerts nobody reads. Fraud flags that get auto-dismissed. Monitoring dashboards that exist to satisfy auditors, not to actually inform anyone. The problem is always the same: the output doesn't respect the human's attention.

    
$82 billion laundered through crypto last year. Less than 1% caught globally. Maybe the answer isn't better algorithms. Maybe it's making the existing ones impossible to ignore.

    <!-- ═══════════════ FOOTER CTA ═══════════════ -->
    
      
The AML risk-note workflow is open source and runs on a scheduled monitoring loop.

      
The risk-note generator scans Ethereum every 30 minutes. The full AML Detection Engine (28 rules, 94.9% detection rate) has a public demonstration. I write about building at the intersection of AI, blockchain, and finance.

      
        [
          AML Risk Notes — GitHub
        ](https://github.com/hash02/aml-roaster)
        [
          Full AML Engine →
        ](https://github.com/hash02/aml-detection-engine)
        [
          Public Demonstration →
        ](https://aml-detection-engine-ewxnmkbekcg8scjjes7caa.streamlit.app/)

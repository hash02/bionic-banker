---
title: "I Built 3 AI Agents. Here's What Broke Each Time."
description: "I built three versions of an AI investigation agent. Each one broke differently. Here's what the architecture diagrams don't tell you about memory, bias, and adversarial reasoning."
date: "2026-03-05"
tags: ["AI · Agents · Blockchain"]
readTime: "7 min"
category: "Tech"
featured: false
slug: "nexus-agent"
---

Okay so — I need to be honest about how this started.

    
I didn't set out to build three versions of anything. I set out to build ONE thing — an AI that could investigate blockchain fraud. Like actually investigate it, not just flag transactions and hand you a spreadsheet. I wanted something that could look at a wallet address and tell me a story. Who moved what, when, why it looks suspicious, and what I should do about it.

    
Version 1 did that. Kind of. And then it broke. So I built version 2. That broke differently. And version 3 — the one that's actually running right now — broke my assumptions about what an AI agent even is.

    
Here's what the architecture diagrams don't tell you.

    
## v1: The One-Brain Problem

    
The first version was the simplest thing possible. One prompt, one model, one shot. You give it a wallet address and some transaction data, it thinks about it, and it gives you a report.

    
And honestly? It worked way better than it should have.

    
The reports were decent. It caught obvious patterns — high-frequency transfers, round-number movements, the stuff that any rules-based system would flag. But here's the thing about AI agents that nobody talks about in the threads — the first version is always suspiciously good. Because you're testing it on the cases you already know the answer to.

    
The moment I threw something ambiguous at it — a wallet that MIGHT be structuring, or a pattern that looks like layering but could just be DeFi yield farming — it fell apart. Not because the model was dumb. Because it had no memory. Every investigation started from zero. No context about what it saw five minutes ago. No ability to say "wait, I've seen this pattern before."

    
> **What broke:** Memory. Or rather, the complete absence of it. A single-shot agent is just a fancy prompt. The difference between a prompt and an agent is the ability to carry context forward. Without that, you're not investigating — you're just asking a really expensive Magic 8-Ball.

    
## v3: Two Brains Arguing With Each Other

    
This is where it gets weird. Because the solution to v2's problems wasn't better memory or smarter fallback. It was adversarial architecture.

    
v3 has two brains. A Reasoner and a Synthesizer.

    
The Reasoner does the investigation. It looks at the data, forms hypotheses, pulls patterns from memory. But — and this is the key — it doesn't produce the final report. It produces a structured reasoning chain. Basically, it shows its work.

    
The Synthesizer then takes that reasoning chain and stress-tests it. It's not trying to agree. It's trying to find holes. Where did the Reasoner make an assumption? Where did it skip a step? Where did it lean on a cached conclusion instead of fresh evidence?

    
Then the Synthesizer produces the report, incorporating its critique of the Reasoner's logic.

    
> *Two models, one pipeline, zero trust between them.*

    
And here's what happened: the quality of the reports went up, but the confidence scores went down. v3 is less certain about its conclusions than v1 was. Which sounds like a step backward — until you realize that v1's confidence was fake. It was certain because it didn't know what it didn't know.

    
v3 is uncertain because it DOES know what it doesn't know. It says things like "this pattern is consistent with layering, but the timing could also indicate automated DeFi position management. Confidence: moderate. Recommend: manual review of transaction timestamps."

    
That's not a worse agent. That's a more honest one.

    
## What the Architecture Diagrams Don't Show

    
Every AI agent tutorial on YouTube shows you the boxes and arrows. Input goes here, model processes there, output comes out. Clean. Linear. Makes sense.

    
Here's what they don't show:

    #### The First Version Lies

        
It looks good because you're testing it on your own assumptions. You designed the test, you know the answer, and the agent confirms it. That's not validation — that's a mirror.

      
      #### Memory Is a Double-Edged Sword

        
Without it, your agent is useless across sessions. With it, your agent develops cognitive biases that compound over time. The solution isn't better memory — it's adversarial auditing.

      
      #### Multi-Model = Disagreement

        
If your second model just agrees with the first, you've built a more expensive version of the same problem. The value is in structured disagreement.

      
      #### Lower Confidence Is a Feature

        
The best report doesn't say "DEFINITELY FRAUD." It says "here's what the evidence supports, here's where it's ambiguous, here are the things a human should check."

      
    

    
  
    </iframe>
    
      What broke at each version — and what each failure taught us
      Interactive
    
  

    
## Where This Goes

    
I run this against real blockchain data now. The Lazarus Group — North Korea's state-sponsored hacking unit — moved $373 million through a specific set of wallets. I fed those transactions through my AML engine (22 detection rules, 94.9% accuracy) and then had NEXUS investigate the flagged patterns.

    
It caught everything. 100% CRITICAL classification. Not because the AI is brilliant — because the architecture forces honesty. The Reasoner can't hide behind confidence. The Synthesizer won't let it.

    
I'm not going to pretend this is production-ready for a bank. It's not. But the architecture — adversarial reasoning, structured disagreement, honest uncertainty — that's the thing worth paying attention to.

    
Every AI agent you see online is v1. Confident, clean, suspiciously good. The real question is: what happens when you let it remember? And what happens when you make two of them argue?

    
That's where it gets interesting.

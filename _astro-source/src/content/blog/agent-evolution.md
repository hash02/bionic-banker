---
title: "From One Script to a Small Agent System"
description: "A build record showing how a wallet-checking script turned into queues, monitors, agent roles, and review points. The useful lesson is not the count. It is how coordination problems became system records."
date: "2026-03-17"
tags: ["AI", "Blockchain", "Builder"]
readTime: "12 min"
category: "Blockchain"
featured: true
slug: "agent-evolution"
---

A wallet-checking script became a small agent system because each failure created a record, a queue, or a review point. This is the build path, the numbers, and the limits.

## The Starting Point Was Embarrassingly Simple

      
Okay so, this wasn't supposed to be a thing. I'm a computer engineer who works inside finance. I'd been watching how compliance teams handle blockchain transactions and I kept thinking the same thing: there has to be a better way to flag suspicious activity than manually checking addresses against a list.

      
So I wrote a Python script. One file. Maybe 80 lines. It pulled a few transactions from Etherscan, compared addresses against the OFAC sanctions list, and printed out which ones matched. That was it. That was the whole "product."

      
That was Day 0. Fifteen days later, I had 14 autonomous agents running on a local machine, generating 438 reports, monitoring 190 blockchain wallets, executing paper trades, writing content drafts, stress-testing their own security, and talking to me through Telegram, all while I was at work.

      
Here's the thing nobody tells you about building with AI: the hard part isn't the code. The hard part is that every solution reveals three more problems, and those problems are more interesting than what you were originally doing. You follow the dots. One to the next to the next to the next. And you look up and suddenly you've built something you didn't plan to build.

      
## The Numbers, Read as Operating Records

14 agents. 438 reports generated. 190 blockchain wallets monitored in paper mode. Paper trades logged with entry rationale. Drafts produced automatically. Adversarial review tests running against controlled failure cases. All of this live on a home server while I was sitting at a desk doing a completely different job.

I know that sounds like a LinkedIn brag. I'm telling the story of how it actually happened because the individual steps were much smaller and more embarrassing than the final number suggests.

## Day 1 to Day 3: The Problem Multiplied

The OFAC script worked. It compared addresses. It flagged matches. I ran it. Got results. Felt good for about fifteen minutes.

Then I noticed the results were incomplete. Etherscan rate limits API calls. Some transaction history was missing. Some addresses were in formats the script did not recognize. The rule set I was comparing against was weeks old because I had to download it manually.

So I fixed the Etherscan issue. Then I noticed the OFAC list also needed to be current. So I wrote a scraper to pull it fresh on each run. Then I noticed the script only checked one network, and most of the interesting activity was cross-chain. So I added Polygon and BSC.

By day 3 I had three scripts that needed to talk to each other. That is not a product. That is the beginning of a coordination problem.

## Day 4 to Day 7: The Word "Agent" Started Meaning Something

At some point I wrote a thing that felt different from a script. It watched a queue. It picked up a task from the queue. It ran some analysis. It wrote the result back to a file. Then it picked up the next task.

It was running on its own. I did not trigger it. I came back an hour later and results were sitting there.

That was the moment the word "agent" shifted from something I read about to something I had built. Not because the code was sophisticated. Because it ran without me.

That one loop changed how I thought about the rest of the project. If one component can run unsupervised, what else can run unsupervised? What parts of this still need me in the loop, and what parts only need me when something breaks?

## Day 8 to Day 12: Architecture Appeared Uninvited

I did not design a three-brain architecture. It emerged from constraint.

I was running all of this on a Windows machine and a server. The server was always on. The Windows machine was sometimes off. So anything that needed to be persistent had to live on the server. Anything that needed heavy language model calls had to route through whatever session was active. The two machines needed to talk to each other without me manually passing files.

So I built messaging. A simple queue. Send and receive. Agents on the server could flag things. Agents on my machine could pick them up. Neither side blocked the other.

That was not a planned system design. That was just me solving the problem of two computers needing to coordinate. But once it existed, new agents could plug into it. And new agents appeared, because every problem in the system was now easier to solve with a dedicated component than with another function in an existing script.

An AML monitor that tracked wallets. A risk scorer that rated transaction patterns. A paper trading agent that logged entries and exits without real money. A content agent that drafted posts from report summaries. A Telegram relay that pushed alerts when something worth knowing happened. A stress tester that tried to break the system on purpose.

Each one started as a solution to a specific problem. Each one became a thing that ran on its own and talked to the others.

## Day 13 to Day 15: The System Ran Without Me

By day 13 I stopped checking it every hour. I let it run overnight and looked in the morning. Reports were there. Alerts had fired. The paper portfolio had logged entries.

I went to work. It kept going.

That was the thing I had not fully expected. The system did not need me to keep running. It needed me to read the output and make decisions about what to do next. But the mechanical layer was handling itself.

Day 15 I counted. 14 agents with distinct roles. 438 reports generated across the run. 190 wallets under monitoring. The numbers were not a target. They were what accumulated from following each problem to the next one.

## What Actually Built It

It was not a plan. It was the discipline of solving each immediate problem as cleanly as possible, which usually meant a small dedicated component rather than adding more to something that already worked.

Every time an existing script started gaining one more responsibility, the better question was whether the new thing actually belonged there. Usually it did not. Usually the cleaner answer was a new component with a narrow responsibility that plugged into the queue.

That instinct came from working in finance. In compliance work, you do not bolt new rules onto existing rules. You write discrete checks, run them independently, and surface the results separately. That pattern translated directly into agent design.

The other thing was that I kept the constraints visible. No paid API calls unless absolutely necessary. Everything logged with a timestamp and reason. Nothing that could not be explained if someone asked why it fired. Same discipline as the work environment, applied to a personal system.

That constraint made the system more reliable than most of my early experiments, which were clever but broke in unpredictable ways.

## What Came Next

The 15-day version was an operating record, not a finished product. It showed that the queue, role boundaries, logs, and status checks could hold together long enough to teach the next design constraint.

The AML engine that came out of that period is still running. The rule set expanded. The report format improved. The paper trading got a proper backtesting layer. New agents got added as new problems appeared.

But the shape of it was there by day 15. Follow the dots. Solve each problem cleanly. Let the architecture emerge from what the problems actually need. Do not design the whole thing first.

The whole thing does not exist yet. It is still being built.

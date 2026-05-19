---
title: "I built an AI financial advisor. Watch it run live."
description: "A live note from the finance lab: six scanners, three funds, a coverage bar, and a guardian layer checking the work while it runs."
date: "2026-04-21"
slug: "watch-it-run-live"
tags: ["AI", "Agents", "Finance", "DeFi", "Systems"]
readTime: "7 min"
featured: true
image: "/blog-visuals/png/watch-it-run-live-hero.png"
category: "AI"
---

# I built an AI financial advisor. Watch it run live.

Most of what I read about AI advisors is one of two things. Either a landing page promising personalized wealth intelligence with no public numbers behind it. Or a long essay arguing whether AI should touch money at all. Both skip the part I actually care about. What does it look like when one is just running.

So I made that part the product.

You can go to [bionicbanker.tech/portfolio](/portfolio/) right now and watch my system move. Coverage bar, six scanner workers, three funds, a guardian layer. Data refreshes every minute. When a sleeve flips from empty to funded, you see it flip. When a worker misses a heartbeat, you see the row go grey. Nothing hidden.

## What the page actually shows

Three funds. Income, Balanced, Growth. Each one has sleeves. A sleeve is a small named slot that gets filled by a scanner. Think of a fund as a box with labelled compartments, and each compartment is the job of a specific worker.

- **Income (60 percent bonds, 40 percent alts)** holds the boring end. Aave stablecoin lending, Polymarket event sleeves, delta neutral funding trades.
- **Balanced (75 percent diversified, 25 percent growth)** adds tokenized stock grids and some TradingView momentum catchers.
- **Growth (90 percent alts, 10 percent anchor)** runs the directional tokenized equity worker I shipped yesterday.

Coverage is the honest number. Sixteen sleeves total. Sixteen funded as of this morning. One hundred percent. That took three weeks. For most of that time the number was embarrassing. Five out of sixteen. Then eight. Then twelve. Then the last stubborn one, xstocks directional, which needed a new worker built from scratch because no existing scanner fit the slot.

## Six scanners, one contract

Every scanner on the page follows the same four rule contract. I learned it the hard way.

1. Tag every position you open with your own worker name. If two workers touch the same row, nobody can attribute performance.
2. Write JSON atomically. Temp file with your process id, then rename. If you are halfway through a write when cron restarts you, the next reader gets a corrupt file. Atomic rename kills that class of bug.
3. Emit a status file every cycle. Open positions, deployed dollars, unrealized pnl, last heartbeat, cycle count. If you cannot answer "is this worker alive" in one grep, you are flying blind.
4. Persist state between cycles. Cycle count, last run timestamp. The thing that survives when the process dies.

Six workers. Same four rules. Different strategies. Grid versus momentum versus directional versus funding neutral versus event markets versus stablecoin lending. Every one of them lives or dies by those four rules.

## The guardian layer

The part nobody builds and everybody should is the layer that watches the watcher.

Mine is called the nursery. Four cron jobs on the server, running every hour, doing one thing each.

- **Blind spot drift** checks that every status file is fresh. If a worker has not heartbeat in three hours, that is a flag. If a fund has sleeves claiming to be funded but no live positions underneath, that is a flag. If the hermes brain itself goes silent, that is a flag.
- **Health** checks disk, cron integrity, log rotation, and the message queue depth.
- **Auto research** pulls signal from the outside world. New BoC papers, new exchange support in Canada, new DeFi primitives worth looking at. When one of my active sleeves becomes stale as an idea, the research layer knows before I do.
- **AI intel** tracks the model world. What changed in Anthropic pricing, what Gemini can now do cheap, what Ollama has that runs local.

Every flag goes into a SQLite ledger. Three strikes and a flag gets escalated. The portfolio page reads the open flag count live. Right now it shows two open. They are both benign. A month ago that number was closer to twenty.

## Why put it in public

Two reasons.

First, it keeps me honest. The moment a coverage number becomes public, you cannot quietly skip a sleeve. You have to build the worker. You have to wire the guardian. You have to actually close the loop.

Second, most people who claim to have built an AI system for finance have nothing to show you. I would rather be the person with a boring live page that refreshes every minute than the person with a pitch deck full of charts that exist only in March.

Same philosophy as my AML engine. Same philosophy as the article list on this site. If I say I built it, there is a URL where you can watch it breathe.

## What is next

The portfolio page is version one. It shows state. The next version will show history.

- Thirty day uptime bar per worker.
- Daily pnl curve per fund.
- Trade log per sleeve, with entry price, exit price, reason.
- An audit mode where you can click a position and see the exact scanner cycle that opened it.

The data is already being written. Every scanner emits cycle data. Every orchestrator run is logged. What is missing is the rendering. That ships next.

If you want to watch the next sleeve get built, or the next worker go live, [subscribe to the newsletter](/#newsletter). One piece at a time. When it is worth saying.

And if you are quietly doing something similar, running real systems for real money with a real uptime story, send me a note. I want to compare notes.

The page: [bionicbanker.tech/portfolio](/portfolio/)

The coverage is one hundred percent today. Tomorrow it might be ninety four because I will be adding a new sleeve. That is the whole point.

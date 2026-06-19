---
title: "Agent Failure Records: What Survived, What Broke, and Why"
description: "A failure-record note for agent systems: context collapse, silent failure, loop limits, model routing, approval timing, cost caps, and the controls that made surviving agents easier to inspect."
date: "2026-04-19"
slug: "agent-graveyard"
tags: ["AI", "Agents", "Engineering", "Systems", "Failure"]
readTime: "9 min"
featured: true
image: "/blog-visuals/png/agent-graveyard-hero.png"
category: "AI"
---

More than a dozen AI agents were built and tested. A handful kept running. The useful part is the failure record: what broke, what signal was missing, and what control would have made the failure visible earlier.

## Agent Failure Records: What Survived, What Broke, and Why

Everyone is talking about agents like they are easy. Build an agent. Deploy an agent. Buy an agent. Scroll any feed for ten minutes and you will see five posts selling the same clean story.

Here is the version nobody posts. I have tried more than a dozen of them. A handful are still alive. The rest are in the graveyard, and every one of them died for a reason I could not have predicted until I watched it die.

This is the failure record. The point is not the graveyard. The point is the controls that came out of it.

## The count

On a small local server that stays powered on most days, I have run at different times:

- A trading orchestrator with four strategy workers. One worker is dead. The orchestrator is alive.
- An AML detection engine. Twelve versions. Twenty-eight rules. Alive and growing.
- A blockchain investigation split-brain with two halves. Both halves died. One half was rebuilt.
- A falsification framework for testing other agents. Four iterations. Last one hardened. Alive.
- An open-source research agent running independently. Alive.
- A minimal coding agent built by someone else that I am still learning from. Alive.
- A content pipeline with four scripts that chain together. All four alive now, but three died at least once before the current versions.
- A fund router for portfolio rebalancing. Alive. Scaffold only.
- A red-team test node on a second older laptop. Still experimental. Its job is to probe the other machines for weaknesses on purpose so someone else does not find them first.
- Several early experiments I do not name anymore because naming them makes them too easy to mourn.

More than a dozen is the lower bound. If you count every worker, every sub-process, every retry of a thing that broke, the real number is higher. I stopped counting when the graveyard started outgrowing the living.

## Orchestration is the wrong word. The real word is choreography.

People keep calling this orchestration. I am starting to think the right word is choreography.

Orchestration sounds like a conductor reading sheet music. Agents do not read sheet music. They work on a rhythm. The rhythm is fragile. One agent loses the beat at 3am because a context window got pressured, and by morning the whole dance is off. You can have four of them moving in time for weeks, and then one steps on the next one's lines and the whole routine has to be picked up from the floor.

The other thing that makes this harder than it looks is that every tool you pick has a different hardness. Driving an agent through Claude Code feels one way. Driving the same job through an open coding agent like OpenHands feels another way. Running it yourself on a raw model through the API feels a third way. The difficulty does not disappear. It moves. One tool hides the hard parts behind a polished interface, and you only meet them when something breaks at an awkward time. Another tool makes you feel every edge as you go, which is exhausting, but at least you know where the edges are.

Running a few of them on the same box, talking to each other, staying in rhythm, staying alive, is new enough that nobody has figured out the canonical way yet. Including me. Especially me.

## What they all had in common before they died

Every single one of them forgot.

That is the most honest sentence I can write about agents. You build them with all this care. You give them instructions, memory, a role, a goal. They run for a day, or a week, or a month. And then you come back and they have forgotten what they were supposed to be doing. Not because you told them wrong. Because the context they carry gets pressured and compresses to survive, and when it compresses it drops the load-bearing detail first.

They also loop. They call a tool, which calls another tool, which calls the first tool, and they run in that loop until a rate limit or a bill stops them. Sometimes the rate limit is yours. Sometimes the bill is yours.

And they fail silently. This is the one that hurts the most. An agent will crash at 2am, log the crash to a file nobody reads, and sit dead for days while you think it is still working. You only notice when you go looking for the output and the output is not there.

Every agent I have run has done at least one of these three. The ones that survived are the ones where I got ahead of those behaviors before they got me.

## Autopsy, category by category

### Death by context collapse

The agent compresses its memory to save tokens. The compression is lossy. The thing it compressed was the one thing it needed.

I lost three different agents to this. The first was a content drafting agent that had been told in its private instruction set exactly which words never to use. After a long session, that source rule got summarized into "write in a conversational style." Every banned word came back the next day. I did not notice for a week because the drafts looked fine until you read them carefully.

Fix that came late: never compress the source of truth. Keep both the full version and the cache. If there is a conflict, full wins.

### Death by silent failure

An early automation check ran on a schedule. One morning the script hit a dependency error, logged it, and exited. The schedule kept firing. Every day it logged the same error. Every day nothing got collected. I noticed six days later when the dashboard looked stale.

Fix that came late: if I cannot see it, it does not exist. Every long-running agent needs a visibility layer. Not just a log file. A dashboard line, a heartbeat timestamp, a message in the morning, something that actively shows up in my day and tells me the truth.

### Death by tool-call infinite loop

This one is expensive. A browser-automation agent got asked to post a thread to a social platform. It opened the browser, tried to click, got a captcha, tried again, got throttled, opened a new tab, tried again. A hundred thousand tokens later, nothing was posted. The agent did not know when to quit because nothing in its design said "if you loop three times on the same action, stop and ask the human."

Fix that came late: every tool call needs a loop detector. Three repeats on the same action is a hard stop. And some categories of work should never be agent-driven. Browser automation on social platforms is one of them.

### Death by model routing confusion

I was running a routing layer that was supposed to send reasoning work to Claude and extraction work to a cheaper local model. Somewhere in the routing logic, a fallback kicked in that sent reasoning work to the cheap model too. The cheap model produced output. The output looked plausible. I did not notice for a week because the answers were wrong in subtle ways, not obvious ways.

Fix that came late: never trust a silent downgrade. If the router changes which model is answering, the decision gets logged and I see it. No ghosts.

### Death by permission gate at the worst hour

An agent was configured to ask for human approval before a trade-like action. Reasonable on paper. In practice, the agent hit its approval request at 3am, sat waiting for me to wake up, and by the time I saw the request the opportunity had moved. Six hours of silence while the world changed.

Fix that came late: either the agent has authority to act within a bounded decision space, or it does not act at all. Asking for permission is only valuable during hours when permission can be granted. Outside those hours, I pre-approve a budget or I let the moment pass.

### Death by name collision

At one point I had three different agents all doing some flavor of treasury work. Each was named for the function it did. Each thought it was the canonical one. Data about the same portfolio went to three different places. Synthesis went to none of them because nobody was responsible for the whole picture.

Fix that came late: one job per agent, and the name encodes the specific job, not the general domain. No two agents get the same functional identity. If two overlap, one gets retired.

### Death by cost explosion

A paid-API workflow ran in a retry loop for three days because one upstream service was throwing a flaky 503. The retry logic was correct in the narrow sense and wrong in the wide sense. The useful lesson was cost caps, alerts, and kill switches. API spend for zero output.

Fix that came late: every paid-API agent gets a daily spend cap, enforced at the code level, not the wishful-thinking level. And for anything that does not genuinely need a paid model, the free-tier local runtime wins by default. Most of the agents now hit a local model first. The point is the cap: paid routes need explicit limits, and local routes should be the default when quality is good enough.

## What actually works, and has been working for a while

I do not want the whole post to read like a wake. Some things run better than I expected.

The mesh stays up. Agents talk to each other through a plain file queue and the queue does not lie. It is the simplest piece of the system and it is the most reliable. No Kafka. No Redis. Just a shared database file three agents read and write in turn.

Every morning I wake up to a status message telling me what happened while I slept. What ran. What failed. What spent. What got published. That feeling, of having a small crew of specialists report in before coffee, is the closest thing to the future I have built so far. It is worth every graveyard stone.

The daily routine holds. Content gets collected. The trading world model scores itself. The AML engine audits. The research agent reads. Most of this happens without me. None of it is perfect. All of it is steadier than I would have guessed a year ago.

So I am not discouraged by the graveyard. I am saying honestly that getting here took a lot more dead agents than the clean tweets make it sound.

## The actual stack, in case you want to try this

If any of this is useful, here is the concrete tool list. You can swap any of these for equivalents. The shape of the system matters more than the specific names.

**Hardware.** One used laptop running Debian with an older NVIDIA GPU and modest RAM. Lid closed, plugged into a wall, on a private mesh with my other machines and my phone. Cost under five hundred dollars.

A second older laptop runs Kali Linux for security testing. It stays separated from the main work and is treated as experimental.

**Models.** Most of the crew runs on a local model server. Small local models handle reasoning-light work, tool-calling tests, and embeddings. The specific model names matter less than the rule: use local defaults where possible, then pay only when the task genuinely needs stronger reasoning.

For heavier reasoning I use a paid model route with a strict budget. For fallback, I use cheaper routes with logging. The important part is not the vendor. It is that model routing decisions are visible and capped.

**Named roles in the crew.** One custom Python orchestrator handles paper-mode portfolio state. One research worker reads public sources. One small coding-agent pattern is used for study. The AML engine and content pipeline are custom Python. The security-testing node remains experimental and separated from the main system.

**Coding agents and how they differ.** Different coding agents are useful for different work: code edits, local tool use, scheduled checks, and sandbox tests. Each one has a different kind of friction. Claude Code is sharp but narrow. Hermes Agent is useful when the job needs local files, tools, schedules, and messaging in the same operating layer. OpenHands makes you feel more of the raw edge. The honest answer is I use multiple tools, and when one is giving me a bad day I try the same problem on another and see if the rhythm comes back.

**Memory and knowledge layer.** Obsidian holds every session transcript and every note, with a graph view that lets me find things I half-remember. Notion holds the project board, the career log, and the investigation databases. A single SQLite file holds the message queue that lets all the agents talk to each other. I have tried fancier stacks. This one keeps working.

**The mesh.** A private mesh connects the nodes. The single most underrated piece of infrastructure for anyone running a small crew of agents on cheap hardware is boring, reliable connectivity. If you are doing this on one box only, you will outgrow the box. Plan for a second node from the start.

**Data sources.** Public and free, by design. DeFiLlama for on-chain liquidity and yield. Blockscout for block-level transaction data. OFAC public lists for sanctions checks. Crypto.com for market data. Every one of these has a free tier that is enough for personal and paper-trading use. Paying for data is the second-fastest way to end up with a dead agent. The first is paying for a bad model.

**What I would pick if I was starting over this week.** A used laptop, a local model server, a private mesh, a notes system, one paid reasoning route if the budget allows, one custom Python agent doing one thing, and a plain SQLite file for message passing. Nothing more until that works.

## What the survivors have in common

Here is what the living have that the dead ones did not.

**A recovery runbook written before the agent shipped.** Five-minute restart from any failure mode. I can follow it half asleep. I have.

**Recovery path.** If a service dies, a recovery path should restore it or alert a person. Not because the code is perfect. Because production reality is not perfect.

**External ground truth.** No agent is allowed to validate its own output. The AML engine checks itself against a public sanctions list. The trading orchestrator checks itself against the actual on-chain portfolio. The content pipeline checks itself against the live article count on the public site. If the agent has no external validator, it does not go into production.

**One job.** Each of them does exactly one thing. The paper-mode portfolio worker records. The AML engine flags. The content pipeline publishes. The research agent reads. None of them is allowed to drift. The moment you ask an agent to do two things, it starts forgetting how to do either.

**Visibility.** Every one of them writes to a place I actually look. Dashboard, message queue, public URL, SQLite ledger. If I cannot see it working today, I assume it is broken.

## Three rules if you are starting now

**Write the recovery runbook before you write the agent.** If you cannot describe how to restart it from a cold crash in five minutes, do not ship it. The runbook forces you to know your dependencies, your failure modes, your ground-truth check. An agent without a runbook is a time bomb with a bow on it.

**Every agent needs an external validator.** The most common failure mode I have seen is an agent that generates output and then validates its own output. That is not validation. That is the agent clapping for itself. Find one external source of truth, public if possible, and make the agent check against it on every run. If there is no external source, flag the output as unverified.

**One job per agent.** The moment you give an agent two responsibilities, you have built something that will forget how to do both. Generalist agents are a myth at this stage of the technology. Specialists that talk to each other are real. Build the specialists. Let them talk.

## What this record is useful for

This note is not a claim that the system is finished. It is a failure record. The useful parts are the controls that survived contact with real runs: recovery runbooks, external validators, one-job workers, visible heartbeats, spend caps, and hard stops for loops.

The remaining gap is still the same: small agent crews need better operating standards. They need records that show what ran, what failed, what changed, and what a human still has to decide. That is the part worth continuing to build.

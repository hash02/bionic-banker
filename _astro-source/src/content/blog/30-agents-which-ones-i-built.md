---
title: "A 30-Agent Framework, Read Against Real Build Records"
description: "A public framework read against real agent build records: which layers existed, which controls were missing, and which failure modes the framework would have made visible sooner."
date: "2026-05-20"
tags: ["AI", "Agents", "Builder", "Blockchain"]
readTime: "11 min"
category: "AI"
featured: true
slug: "30-agents-which-ones-i-built"
image: "/blog-visuals/png/30-agents-hero.png"
---

A 30-agent engineering map is useful when it is compared against real build records, missing controls, and failure modes.

That timing changed how I read it. I was not asking, "What should I build?" I was asking a better question: "Which parts did I accidentally build, which layers are still missing, and which failures would this map have prevented?"

## A 30-Agent Framework, Read Against Real Build Records

There is a reference going around right now. 30 AI agents, organized by category, with a DASH framework for designing each one, a 30-rule prompt core, and a rules list at the bottom. GenAI Works published it. Six million people follow that account. The image has been reshared across LinkedIn and Twitter more times than I can count.

Before seeing the framework, I had already built a small set of agents around wallet monitoring, queues, review, memory, and status reporting. That made the framework useful as a control map rather than a build checklist.

So when this framework showed up in my feed, I did not read it like a beginner. I read it like someone comparing notes.

The list was useful, but not as a checklist. It was useful as a calibration tool.

## The Six Categories and How They Map to Real Work

The framework splits the 30 agents into six buckets:

Foundation (1-8), Intelligence (9-14), Multimodal (15-20), Specialized (21-24), Domain (25-27), Integration (28-30).

The build order says foundation first, integration last. That is correct. If you build a domain-specific agent before memory, verification, and retrieval are stable, you get demos. You do not get a system you can trust twice.

Here is what I had actually built across those 15 days:

**Foundation agents I built:**

Autonomous Decision (01): My coordinator. It ran a loop, picked up tasks from a queue, dispatched them to the right agent, and logged what happened. No human approval in the middle. The important part was not "autonomy" as a label. It was having a loop that could choose the next bounded move.

Memory-Augmented (03): The brain file system. Markdown files held identity, mistakes, current state, working knowledge, and retrieval notes. The point was simple: a new session should not wake up blank and ask the same questions again.

Agentic Workflow (08): The coordinator that managed the other agents. It had state, knew which agents existed, and could move work across components without turning every task into a one-off script.

**Intelligence agents I built:**

Data Analysis (09): The transaction scanner. It pulled blockchain data, cleaned it, identified patterns, and surfaced rows that matched risk rules. Not glamorous. Very useful.

Verification Agent (10): The reviewer. Its job was to attack outputs and check whether they survived adversarial prompts, missing data, and stale assumptions. I wrote a full post about the 20 percent survival rate.

**Domain agents I built:**

Financial Advisory (25): Paper trading logic. Not real money, but real market data, entry rationale, and performance tracking. The useful part was the decision record, not the simulated trade.

That accounts for six of their thirty. The other eight agents I built are adjacent to their taxonomy but do not map cleanly to single categories.

The Telegram relay sits between Content Creation (16) and a notification system. The AML rules engine sits between Verification (10) and something they call Security-Hardened (13). The stress tester maps to Kill Agent, which is closer to a Security-Hardened agent than anything else.

## What the Framework Gets Right That Solo Building Misses

The DASH framework is the part I wish I had seen earlier. Four quadrants: what to define, when and where it runs, prompt must-haves, design principles.

The prompt must-haves are Task, Protocol, Constraints, Stop. Every agent needs all four. Task is what to do. Protocol is how to do it. Constraints are what not to do. Stop is when to exit the loop.

I built all of my agents without explicitly defining Stop. And it caused problems.

The ghost agent post I wrote is exactly what happens when Stop is undefined. A function that was supposed to use a local model ran 9,917 calls to external APIs over eleven days because there was no clean stopping condition. The loop kept going because nothing told it to stop. The framework calls this out directly: define stopping conditions before you ship.

That one rule alone is worth the whole framework.

The other rule I violated: build the no-result path. When an agent cannot find what it is looking for, what does it return? I had several agents that returned empty responses and continued as though nothing happened. That was invisible until the output was obviously wrong. A no-result path that logs and escalates is how you catch it.

## What the Framework Misses That Solo Building Taught Me

The framework is organized. It is also written from the perspective of a planner.

Solo building teaches you something a framework usually cannot: sometimes you do not know what you are building until the system starts annoying you.

I did not know I was building a memory-augmented agent on day three. I knew I was annoyed that every new session started cold. The memory system came from solving that specific annoyance, not from deciding to implement category 03.

That distinction matters. The framework gives you the map. The map does not give you the intuition for which problem to solve next. That intuition comes from running the system, watching it break, and following the failure to the root cause.

The framework also underweights the messaging layer. In their taxonomy, Integration (28-30) covers collective intelligence, embodied intelligence, and domain-transforming. The mechanics of how agents actually communicate with each other sit inside "inputs, structure, tools," but there is no dedicated agent for it.

A shared message queue with known formats and a logging contract was the thing that made my system scalable beyond three or four components. Without it, adding a new agent meant modifying every existing agent that needed to talk to it. With it, new agents just plugged into the queue. The messaging architecture deserves its own numbered entry in a 30-agent framework.

## The Prompt Core Is the Part Most People Will Skip

Thirty rules for how to construct an agent prompt. Most people will read the numbered list and move on.

The ones that matter most in practice:

Rule 1: Define the goal in one crisp sentence. Every poorly behaving agent I have built had a blurry goal. One sentence is a constraint, not decoration. If you cannot say what the agent does in one sentence, you do not understand the agent well enough to build it.

Rule 3: Prioritize tasks and rank by impact. Agents without priorities do the first thing in the list, not the most important thing. Under load or failure, unprioritized agents produce inconsistent behavior.

Rule 10: Check memory and context, update state. This is the rule that separates sessions from systems. An agent that reads state on entry and writes state on exit can be interrupted and resumed. An agent that does not is a script with a fancy wrapper.

Rule 20: Run safety and bias checks. In financial services this is not optional. If an agent is flagging transactions or making risk assessments, it needs an independent validation pass before the output goes downstream.

Rule 30: Log decisions, metrics, feedback. The kill agent I built would have been pointless if it did not produce a record. Agents that do not log are agents you cannot improve.

## How the Build Order Holds Up

Framework build order: Foundation, Intelligence, Multimodal, Specialized, Domain, Integration.

My actual build order: AML script (Foundation adjacent), coordinator (Foundation), memory system (Foundation), AML engine expansion (Intelligence + Domain), paper trading (Domain), reviewer agent (Intelligence), content agent (Multimodal adjacent), Telegram relay (Integration).

That is roughly the right shape, and it was arrived at by following problems rather than following a plan. Foundation problems appear first because they are the load-bearing layer. Domain problems appear later because you need the infrastructure to understand what the domain actually requires.

The one deviation: I built domain-specific logic, the AML rules, before I had solid Intelligence-layer tooling. That created debt. The AML rules engine had to be partially rebuilt once the verification and data analysis layers were strong enough to support it. The framework's build order would have prevented that rework.

## What I Would Build Next, Using the Framework

The gap in what I have built, cross-referencing against the 30:

Knowledge Retrieval (04): I have retrieval in my memory system, but not as a standalone agent with source tracking, synthesis, and citation. A dedicated retrieval agent would improve every downstream agent that currently leans on static files.

Self-Improving (14): I log mistakes and update rules manually. A self-improving agent would observe a failure, generate a hypothesis about the cause, test a fix, and update the rule set if the fix works. That is a serious build, but the payoff is an agent that gets better without waiting for me.

Explainable Agent (22): My agents produce outputs, but not enough explanations. In financial services, "the agent flagged this" is not sufficient. Why it was flagged, what rule it matched, and what confidence level it carries should come from the agent itself, not from documentation someone wrote later.

Legal Intelligence (26): Contract analysis, clause flagging, risk surfacing. This is directly applicable to banking and compliance work. The retrieval and verification foundation needs to be solid before this is useful.

## The Framework as Calibration Tool

The most useful thing about a 30-agent framework is not the 30 agents. It is the gaps it surfaces.

Before I read this framework, I thought I had a multi-agent system. After reading it, I understood the shape more clearly: Foundation was fairly strong, Intelligence was partial, Domain had real pieces, and Multimodal, Specialized, and Integration were still thin.

That is useful information. It tells me where the system is underdeveloped relative to what a complete architecture looks like. It also tells me the build order for what to add next.

Build the Foundation first. Get infrastructure, memory, verification, and data analysis stable. Then extend. The framework is right about this.

The 15-day version I built proved the pattern works. The framework gives the pattern a name.

---

**Reference:** GenAI Works "30 AI Agents Every Engineer Must Build", engineering reference with DASH framework and 30-rule prompt core (2026).

---
title: "Someone Made a List of 30 AI Agents Every Engineer Must Build. I Cross-Referenced It Against What I Actually Shipped."
description: "GenAI Works published a complete 30-agent engineering reference with build order, prompt architecture, and a framework for every agent. I built 14 in 15 days without the framework. Here is what lines up and what I missed."
date: "2026-05-20"
tags: ["AI", "Agents", "Builder", "Blockchain"]
readTime: "11 min"
category: "AI"
featured: true
slug: "30-agents-which-ones-i-built"
image: "/blog-visuals/png/30-agents-hero.png"
---

GenAI Works published a 30-agent engineering reference covering every category from foundation to integration, with a prompt framework, build order, and non-negotiable rules. I built 14 autonomous agents in 15 days before seeing this framework. Here is what I got right, what I missed, and what the framework surfaces that solo building usually skips.

# Someone Made a List of 30 AI Agents Every Engineer Must Build. I Cross-Referenced It Against What I Actually Shipped.

There is a reference going around right now. 30 AI agents, organized by category, with a DASH framework for designing each one, a 30-rule prompt core, and a non-negotiable rules list at the bottom. GenAI Works published it. Six million people follow that account. The image has been reshared across LinkedIn and Twitter more times than I can count.

I built 14 autonomous agents in 15 days before I ever saw this framework. I wrote about how that happened in an earlier post. I started with an 80-line Python AML script. Followed problems. Ended up with a multi-agent system that monitored wallets, executed paper trades, wrote content drafts, and talked to me through Telegram while I was at work.

So when this framework showed up in my feed, I did not read it like a beginner. I read it like someone comparing notes.

Here is what I found.

## The Six Categories and How They Map to Real Work

The framework organizes 30 agents into six categories:

Foundation (1-8), Intelligence (9-14), Multimodal (15-20), Specialized (21-24), Domain (25-27), Integration (28-30).

The build order in the framework says exactly this: foundation first, integration last. That is correct. Building a domain-specific agent before you have reliable memory, verification, and data retrieval is building on sand. You will get demos. You will not get systems.

Here is what I built across those 15 days, mapped against their taxonomy:

**Foundation agents I built:**

Autonomous Decision (01): My coordinator. It ran a loop, picked up tasks from a queue, dispatched them to the right agent, and logged what happened. No human approval in the middle. That is the definition of autonomous decision.

Memory-Augmented (03): The brain file system. A set of markdown files that held identity, mistakes, current state, working knowledge, and a retrieval layer. The agent knew who it was and what it was doing across sessions. I wrote about the five-layer architecture separately.

Agentic Workflow (08): The coordinator that managed the other agents. It had state, knew which agents existed, and could orchestrate multi-step tasks across components.

**Intelligence agents I built:**

Data Analysis (09): The transaction scanner. It pulled blockchain data, cleaned it, identified patterns, and surfaced the ones that matched risk rules. That is data analysis with an AML focus.

Verification Agent (10): The kill agent. Its whole job was to attack the other agents and check whether their outputs held up under adversarial inputs. I wrote a full post about the 20 percent survival rate.

**Domain agents I built:**

Financial Advisory (25): Paper trading logic. Not real money, but real market data, real entry rationale, real performance tracking. The agent was running a simulated portfolio with documented decisions.

That accounts for six of their thirty. The other eight agents I built are adjacent to their taxonomy but do not map cleanly to single categories.

The Telegram relay sits between Content Creation (16) and a notification system. The AML rules engine sits between Verification (10) and something they call Security-Hardened (13). The stress tester maps to Kill Agent, which is closer to a Security-Hardened agent than anything else.

## What the Framework Gets Right That Solo Building Misses

The DASH framework they include is the part I wish I had seen earlier. Four quadrants: what to define, when and where it runs, prompt must-haves, design principles.

The prompt must-haves are Task, Protocol, Constraints, Stop. Every agent needs all four. Task is what to do. Protocol is how to do it. Constraints are what not to do. Stop is when to exit the loop.

I built all of my agents without explicitly defining Stop. And it caused problems.

The ghost agent post I wrote documents exactly what happens when Stop is undefined. A function that was supposed to use a local model ran 9,917 calls to external APIs over eleven days because there was no clean stopping condition. The loop kept going because nothing told it to stop. The framework calls this out explicitly as a non-negotiable: define stopping conditions before you ship.

That one rule alone is worth the whole framework.

The other non-negotiable that I violated: build the no-result path. When an agent cannot find what it is looking for, what does it return? I had several agents that returned empty responses and continued as though nothing happened. That was invisible until the output was obviously wrong. A no-result path that logs and escalates is how you catch it.

## What the Framework Misses That Solo Building Taught Me

The framework is organized and comprehensive. It is also written from the perspective of a planner.

Solo building teaches you things that frameworks cannot capture because frameworks assume you know what you are building before you start.

I did not know I was building a memory-augmented agent on day three. I knew I was annoyed that every new session started cold. The memory system came from solving that specific annoyance, not from deciding to implement category 03.

That distinction matters. The framework gives you the map. The map does not give you the intuition for which problem to solve next. That intuition comes from running the system, watching it break, and following the failure to the root cause.

The framework also underweights the messaging layer. In their taxonomy, Integration (28-30) covers collective intelligence, embodied intelligence, and domain-transforming. The mechanics of how agents actually communicate with each other sit in the DASH framework under "inputs, structure, tools" but there is no dedicated agent for it.

A shared message queue with known formats and a logging contract was the thing that made my system scalable beyond three or four components. Without it, adding a new agent meant modifying every existing agent that needed to talk to it. With it, new agents just plugged into the queue. The messaging architecture deserves its own numbered entry in a 30-agent framework.

## The Prompt Core Is the Part Most People Will Skip

Thirty rules for how to construct an agent prompt. Most people will read the numbered list and move on.

The ones that matter most in practice:

Rule 1: Define goal clearly, one crisp sentence. Every poorly behaving agent I have built had an ambiguous goal. One sentence is a constraint, not just a guideline. If you cannot say what the agent does in one sentence, you do not understand the agent well enough to build it.

Rule 3: Prioritize tasks and rank by impact. Agents without priorities do the first thing in the list, not the most important thing. Under load or failure, unprioritized agents produce inconsistent behavior.

Rule 10: Check memory and context, update state. This is the rule that separates sessions from systems. An agent that reads state on entry and writes state on exit can be interrupted and resumed. An agent that does not is a script with a fancy wrapper.

Rule 20: Run safety and bias checks. In financial services this is not optional. If an agent is flagging transactions or making risk assessments, it needs an independent validation pass before the output goes anywhere downstream.

Rule 30: Log decisions, metrics, feedback. The kill agent I built would have been pointless if it did not produce a record. Agents that do not log are agents you cannot improve.

## How the Build Order Holds Up

Framework build order: Foundation, Intelligence, Multimodal, Specialized, Domain, Integration.

My actual build order: AML script (Foundation adjacent), coordinator (Foundation), memory system (Foundation), AML engine expansion (Intelligence + Domain), paper trading (Domain), kill agent (Intelligence), content agent (Multimodal adjacent), Telegram relay (Integration).

That is roughly the right shape, and it was arrived at by following problems rather than following a plan. Foundation problems appear first because they are the load-bearing layer. Domain problems appear later because you need the infrastructure to understand what the domain actually requires.

The one deviation: I built domain-specific logic (AML rules) before I had solid Intelligence-layer tooling. That created debt. The AML rules engine had to be partially rebuilt when the verification and data analysis layers matured enough to support it. The framework's build order would have prevented that rework.

## What I Would Build Next, Using the Framework

The gap in what I have built, cross-referencing against the 30:

Knowledge Retrieval (04): I have retrieval in my memory system but not as a standalone agent with proper source tracking, synthesis, and citation. A dedicated retrieval agent that pulls from multiple sources and confidence-weights its results would improve every downstream agent that currently uses static files.

Self-Improving (14): I log mistakes and update rules manually. A self-improving agent would do this automatically: observe a failure, generate a hypothesis about the cause, test a fix, and update the rule set if the fix works. That is a significant build but the payoff is an agent that gets better without human intervention.

Explainable Agent (22): My agents produce outputs but not explanations. In financial services, "the agent flagged this" is not sufficient. The explanation for why it was flagged, what rule it matched, and what the confidence level is — that needs to come from the agent itself, not from documentation someone wrote separately.

Legal Intelligence (26): Contract analysis, clause flagging, risk surfacing. This is directly applicable to banking and compliance work. The retrieval and verification foundation needs to be solid before this is useful.

## The Framework as Calibration Tool

The most useful thing about a 30-agent framework is not the 30 agents. It is the gaps it surfaces.

Before I read this framework I thought I had a multi-agent system. After reading it I understood that I had the Foundation layer fairly well and the Intelligence layer partially, with domain-specific additions, but almost nothing in Multimodal, Specialized, or Integration.

That is useful information. It tells me where the system is underdeveloped relative to what a complete architecture looks like. It also tells me the build order for what to add next.

Build the Foundation first. Get the Infrastructure, Memory, Verification, and Data Analysis agents stable. Then extend. The framework is right about this.

The 15-day version I built proved the pattern works. The framework gives the pattern a name.

---

**Reference:** GenAI Works "30 AI Agents Every Engineer Must Build" — complete engineering reference with DASH framework and 30-rule prompt core (2026).

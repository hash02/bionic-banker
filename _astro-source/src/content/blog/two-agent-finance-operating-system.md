---
title: "How I Built a Two-Agent Finance Operating System"
description: "A source-linked case study on a two-agent operating layer for finance and compliance work: shared board state, approval gates, audit trails, and honest limits."
date: "2026-05-18"
tags: ["AI", "Agent Systems", "Finance", "Career"]
readTime: "7 min"
category: "AI"
featured: false
slug: "two-agent-finance-operating-system"
---

I kept running into the same problem.

Not a coding problem exactly. A coordination problem.

One AI agent can write. One AI agent can code. One AI agent can summarize a file. But the moment the work becomes real, the problem changes. It is no longer "can the model answer?" It becomes:

Who checks the answer?

Who remembers the last decision?

Who stops the system from doing something public before a human approves it?

Who keeps score?

That is where this experiment started.

I built a two-agent operating system for finance and compliance work. I started calling it a chess game because that was the cleanest metaphor. One agent makes a move. The other agent reviews it, pushes back, accepts, or redirects. The board keeps state. Every move leaves a record.

The goal was not to make agents sound smart.

The goal was to make them harder to fool.

## The Problem

Most AI workflows are too linear.

Prompt in. Answer out. Maybe a human reads it. Maybe nobody does.

That is fine for a draft. It is not fine for finance, compliance, job applications, public publishing, or anything that can touch another person.

Those domains need boundaries.

They need audit trails.

They need a way to separate drafting from action.

So I built the system around one rule:

Agents can research, draft, critique, package, and prepare. They cannot apply, publish, contact people, move money, expose private data, or take external action without a human approval gate.

That one rule changed the whole architecture.

## The Board

The board is a shared state file.

It tracks the mission, the latest move, the active lanes, the open decisions, and the boundary rules. Instead of each agent waking up with no memory and guessing what matters, the board gives them the current position.

For career work, the board tracks things like:

- GitHub notes
- resume variants
- job-market research
- draft application material
- public profile readiness
- portfolio links
- outreach drafts

For finance and DeFi work, the same structure can track:

- testnet experiments
- paper-trading systems
- policy gates
- research lanes
- risk checks
- reader-facing reporting

The important part is that the board is not a chat transcript. It is an operating surface.

## The Turns

Each agent writes a concise turn artifact.

The turn says:

- what was reviewed
- what was accepted
- what was rejected
- what changed
- what the next agent should check
- which boundaries were held

That sounds small, but it matters.

It means the system does not depend on vibes. It has receipts.

If one agent drafts a resume, the other agent can review it for overclaiming. If one agent proposes a public portfolio page, the other agent can check whether the links are real. If one agent wants to build a page, the other agent can say, "wait, this card has no public URL yet."

That happened in the actual system.

The first version of a project page had a card for the two-agent system itself. The reviewer agent caught the weakness: the card had no public artifact to link to. A project card cannot link to itself. So the next move became this case study.

That is the point of the game.

The agents are not just generating output. They are finding the missing trail.

## The Gates

The system has hard boundaries.

It can prepare draft application material. It cannot submit the application.

It can draft an outreach email. It cannot send the email.

It can build a reader-facing project summary. It cannot expose sensitive system details, wallet details, or client information.

It can write a website spec. It cannot publish the page without approval.

This is the part I care about most.

Autonomy without boundaries is not intelligence. It is just motion.

The real skill is building a system that can move while still knowing where not to move.

## What It Built

The system has already produced real public-facing artifacts:

- a cleaned public GitHub profile section
- a corrected AML Detection Engine README
- a crypto AML and RegTech resume variant
- draft material for crypto compliance roles
- a public project lab-route spec
- this case study as the missing bridge between private system and visible source trail

None of those required pretending the system is bigger than it is.

That was another design rule: do not inflate.

If something is personal-scale, call it personal-scale.

If something is a research system, call it a research system.

If something is draft-only, mark it draft-only.

Trust comes from clean edges.

## Why It Matters

This is where AI in finance gets interesting to me.

The hard part is not making a model write a paragraph. The hard part is making a workflow that knows the difference between a paragraph, a recommendation, an approval, and an external action.

In finance and compliance, those differences matter.

An AI system that drafts a case narrative is useful.

An AI system that drafts a case narrative, stores the evidence, marks the assumptions, asks for review, and refuses to send anything without approval is much more useful.

That is the direction I am building toward.

Not "AI replaces judgment."

More like:

AI does the heavy lifting around memory, drafting, comparison, and evidence. Humans keep judgment, accountability, and final action.

## The Honest Limitation

This is not an enterprise compliance deployment.

It is a personal-scale production system built to prove the architecture pattern:

- agentic workflows
- shared board state
- approval gates
- audit trails
- policy boundaries
- evidence-preserving automation

The next step is to apply this pattern inside a team, under real compliance leadership, with real data governance, access controls, model-risk review, and production ownership.

That is exactly the kind of work I want to do.

## The Simple Version

I built a chessboard for AI agents.

Not to play chess.

To make work safer.

One agent moves. Another reviews. The board remembers. The gates stop external action until a human approves it.

That is the experiment.

And honestly, I think this is where a lot of AI work is going.

Not one giant agent doing everything.

More like small agents with roles, memory, boundaries, and a scoreboard.

Less magic.

More operating system.

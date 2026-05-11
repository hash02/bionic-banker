---
title: "I Built Agents That Wake Up And Check Evidence"
description: "A draft about turning AI agents from chat windows into proof-backed workers that wake up, check evidence, write reports, and admit what they cannot prove yet."
date: "2026-05-11"
tags: ["AI", "Agents", "Finance", "Compliance", "Systems"]
readTime: "7 min"
category: "AI"
draft: true
---

# I Built Agents That Wake Up And Check Evidence

Most AI demos still feel like a conversation.

You ask something. It answers. Maybe it writes code. Maybe it makes a plan. Then the tab closes and the whole thing becomes memory dust.

That is useful, but it is not what I wanted.

I wanted agents that could wake up later, check what changed, compare it against yesterday, write down what they found, and leave enough evidence that I could trust the report without trusting the tone.

The sentence that became the rule was simple:

> No proof row, no product claim.

If the system says something happened, it needs a source. A ledger. A report. A test. A chain audit. A human approval. Something outside the sentence itself.

Because in finance, confidence is cheap. Evidence is the product.

## The First Version Was Messy

The early version was basically a pile of useful parts.

One loop watched a market. Another wrote reports. Another sent notifications. Another tried to organize memory. Another generated daily summaries. It worked often enough to be interesting, but not clean enough to trust blindly.

The problem was not intelligence.

The problem was continuity.

Every agent had a small view of the world. Each one could do useful work, but the system needed a shared memory, a shared language, and a way to say, "this is real, this is paper, this is stale, and this is just a notification."

That last part matters.

A notification is visibility, not truth.

A dashboard is visibility, not truth.

A confident paragraph is visibility, not truth.

Truth needs a source.

## What Changed

I started treating the whole thing less like a bot and more like a mission system.

Every mission needs a few roles.

One part plans. One part works. One part validates. One part broadcasts. One part writes down what changed so the next session does not start from zero.

That sounds obvious, but most small AI projects skip it. They build the worker and forget the validator. Or they build the dashboard and forget the ledger. Or they save logs but never make the logs easy to read.

So the work became less glamorous and more useful.

Write the proof row.

Write the daily brief.

Write the handoff.

Mark what is paper-only.

Mark what is live.

Mark what is stale.

Mark what should not be trusted yet.

That is where the system started feeling less like a chat session and more like a coworker.

## The Finance Angle

My day job is in regulated finance. That changes how I think about AI.

I do not want an AI system that only sounds right. I want one that can show what it saw, what rule it used, what source it touched, and where a human still needs to approve.

That is the same pattern behind my AML detection work.

Do not just say "this looks risky."

Say which pattern fired.

Say whether it was structuring, layering, fan-in, fan-out, sub-threshold behavior, or something else.

Say where the rule lives.

Say what the system cannot conclude legally by itself.

That boundary is not a weakness. That boundary is what makes the system usable.

## The Public Version

The private version of this system has more detail than I should ever publish. Private paths, private machines, private reports, private experiments, private failures.

So I am building a public proof layer.

Not the raw vault. Not the raw graph. Not every detail.

The public version should show the shape:

- AML detection engine.
- Agent proof reports.
- Daily caretaker briefs.
- Memory architecture.
- Public writing.
- Clear safety boundaries.

Enough for someone to understand what I can build.

Not enough to expose anything that should stay private.

## What I Learned

The biggest lesson is not that agents can work while you sleep.

The bigger lesson is that they need a system around them.

They need memory.

They need validators.

They need boring reports.

They need a way to say "I do not know."

They need a way to stop when the evidence is weak.

And if they are touching finance, risk, compliance, or money, they need proof before confidence.

That is the part I am building now.

Not one magic agent.

A small operating system of agents, reports, memory, and human gates.

One piece at a time.

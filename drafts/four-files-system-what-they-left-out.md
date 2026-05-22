---
title: "I've Been Running the '4 Files' System for 6 Months. Here's What They Left Out."
description: "Everyone is posting about Agents.md and Context.md. The part that compounds is not the diagram. It is the failure record underneath it."
date: "2026-05-22T12:00:00-07:00"
tags: ["AI", "Productivity", "Claude", "Systems", "Building"]
readTime: "6 min"
category: "AI"
draft: true
---

# I've Been Running the '4 Files' System for 6 Months. Here's What They Left Out.

You have probably seen the posts.

Four files. Two hours saved per day. Agents.md, Context.md, Memory.md, Skills.md. A clean diagram. A promise that your AI stops being a generalist and starts acting like a team.

It is a good framework. The people posting it are not wrong.

But there is a gap between the diagram and the actual system. And that gap is where most people fail.

I have been running a version of this for six months. The real version is less clean. More honest. And it works better once you understand what it is actually doing.

---

## The Diagram Is Right About One Thing

The sequence is correct.

Context loads first. Agents read it and know their role. Agents run Skills to execute work. Memory captures what happened. Next session starts smarter.

That loop is real. I run it every day across multiple AI agents, a server, and a file system that spans about 40,000 words of operating context.

But the diagram stops at the happy path.

---

## What They Left Out: The Immune System

The single most important file in my system is not on the diagram.

It is called MISTAKES.md.

It is a running log of every time the system got something wrong. Every rule it violated. Every assumption it made that turned out to be wrong. Every category of failure that happened more than once.

Right now it has dozens of entries. The exact number changes because the file is alive. That is the point.

The insight behind it is that AI systems don't fail randomly. They fail in patterns. The same class of mistake shows up again and again because the context that produced the mistake is still there. The model re-enters the situation and makes the same call.

MISTAKES.md is the immune system. It gets read at the start of every session, before anything else. The rule is simple: if a mistake category shows up three times, stop and address the architecture. Don't patch the symptom.

Memory.md in the diagram captures preferences and corrections. That is true but incomplete. What it doesn't capture is the difference between a mistake that happened once and a pattern that has repeated. A single entry saying "don't deploy without checking tests" is not the same as flagging that deployment skips happened three times in one week.

The immune system is what makes Memory.md worth anything over time.

---

## What They Left Out: The Kill Protocol

The diagram is optimistic. It assumes the loop compounds upward.

Sometimes it doesn't. Sometimes the agent makes a confident move that breaks something. Sometimes the correction makes it worse. Sometimes a whole sub-system needs to be killed and rebuilt.

My system has a kill protocol. Every session, I try to find the thing that would break it. Not to break it on purpose. To find the weakness before reality does.

The rule is simple: every failure produces four things. What broke. Why. The fix. And a new entry in the immune system.

No silent deaths. If something breaks, it goes in the record.

The diagram doesn't have this because it's optimistic about compounding. The real system has to be pessimistic about failure, or it gets overconfident. Overconfident AI systems make expensive mistakes.

---

## What They Left Out: The Oracle Rule

Here is the one that surprised me most.

The diagram says Memory.md updates after each session, so the next session starts smarter. That is true.

But if the AI generates data AND validates that same data, the validation is worthless.

I call this the Oracle Rule. If the system produces a report and then the system says "yes the report looks correct," that is not a validation. That is the system talking to itself.

Every critical output in my system has at least one external check. A test suite. A chain audit. A second agent reading the first agent's work. A FINTRAC report that the system cannot write itself.

The diagram shows a loop that gets smarter. What it doesn't show is the question: smarter according to whom? If the only judge is the system itself, the loop can compound toward confident wrongness just as easily as toward correctness.

The external check is what breaks that. It is the thing that tells you the loop is compounding toward the right answer.

---

## What the Real System Actually Looks Like

Here is my version, honestly.

<!-- INFOGRAPHIC: four-files-system-map - pending render -->

**Context.md** is not just brand details and buying triggers. In my setup, the context file is closer to an operating manual. It covers error patterns, architecture choices, which agents handle which tasks, and what happens when something breaks. It gets updated when the system changes.

**Agents.md** is not only a list of roles. It is a boundary map. Multiple active agents, one persistent server, and one training pipeline. Each one has a boundary: what it can touch, what it cannot, what it needs approval for. The boundaries are the part that makes the agents useful. Without boundaries, agents do too much. With them, they do the right thing.

**memory/** is the Memory.md equivalent, split into about 20 files. Not one file. One file for user preferences, one for project state, one for feedback that changed my behavior, one for reference pointers to external systems. Single files get stale. Split files stay current because you only update the relevant section.

**MISTAKES.md** is not on the diagram. It is the most important file. Dozens of entries. Recurring patterns marked and turned into rules. It gets read first, every session, before anything else. That is not optional.

**Skills** in my system are distributed differently. Some live in the agents. Some live in operating notes that the agents read before executing. Some live in small scripts that orchestrate what happens when. The diagram treats skills as a flat list. The real system has skills at different levels of abstraction.

---

## The Part That Actually Compounds

The diagram promises that "any one file is useful, all four together is a self-improving AI workforce."

<!-- INFOGRAPHIC: compounding-truth-comparison - pending render -->

That is true but the compounding comes from a specific place.

It is not that the AI gets smarter in the abstract. It is that the cost of re-explaining context drops to zero. Every session starts with the full system loaded. The agent knows what happened last time. It knows what broke. It knows what it is not allowed to do.

The compounding is not intelligence. It is amortized context.

By month six, I do not re-explain anything. The system runs from files. The files carry the accumulated judgment from every session. The agent reads the files and operates from that judgment as if it were its own.

That is the actual loop. Not smarter AI. Smarter context.

---

## What to Actually Build

If you are starting from the diagram, here is what I would change.

Start with Context.md first. Not as a brand sheet. As a session boot protocol. What does the AI need to know in the first 30 seconds to operate correctly? Put exactly that, nothing else.

Add the immune system from day one. Call it MISTAKES.md or call it something else, but the file needs to exist. Start with two or three entries and write them honestly.

Build the Oracle Rule into your setup. Identify at least one output in your workflow that needs an external check. A test. A second read. A number that comes from a source the AI didn't produce. Build that check in before you trust the output.

Then keep using it long enough for the file to become honest.

The four files are a starting shape. The system that actually works is built from the failures you accumulate on top of it.

---

*I'm building signal systems, compliance tools, and writing about what I'm learning at the intersection of AI and finance. Working inside a bank, building on nights and weekends.*

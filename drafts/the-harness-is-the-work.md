---
title: "The Harness Is the Work"
description: "People talk about the model. The part that actually determines what you ship is everything around it."
date: "2026-05-23T12:00:00-07:00"
tags: ["AI", "Agents", "Engineering", "Systems", "Workflow"]
readTime: "8 min"
category: "AI"
draft: true
---

# The Harness Is the Work

People talk about which model to use.

GPT-5.5 or Opus 4.7. Context window benchmarks. Coding evals. Which one performs better on web tasks. It is a reasonable conversation, but it is not the one that actually determines what you ship.

The part that determines what you ship is the harness.

The model is just a next-token predictor. It does not know your project. It does not know what you tried three sessions ago. It does not know which rules you learned the hard way, which paths are off-limits, or what your definition of done looks like. The harness is what carries all of that.

I built a harness by accident and spent months realizing that was the actual work.

<!-- INFOGRAPHIC: harness-anatomy - pending render -->

## What a Harness Is

The model is a brain in a jar.

You put text in. It predicts what comes next. That is all. It cannot read your files unless you give it a tool to read files. It cannot remember last session unless you give it something to read. It cannot know your constraints unless you write them down somewhere it will actually see them.

The harness is everything around the brain.

System prompts. File-based memory. Tool permissions. Rule files. Turn protocols. Session handoffs. The harness is what converts "a very smart thing that predicts text" into something that can actually do useful work on your specific project without you babysitting every single line.

Most people who say "I cannot get good results from AI" are missing a harness. They have a brain in a jar and they are shouting at it in plain English and wondering why it keeps forgetting things.

## The File-Based Memory Problem

Here is the thing about agents. They are amnesiac by default.

Every new session starts fresh. The agent does not remember what you tried last time. It does not remember which approaches you already ruled out. It does not know which file path is the canonical one or which pattern turned out to be a mistake.

You can fix this or you can spend every session repeating yourself.

The fix is ugly but it works: write things down in files the agent reads at the start of every session. Not a single giant file. Not a doc nobody maintains. Modular files. One for project state. One for rules that came from real mistakes. One for cross-agent coordination. One for what is in progress right now.

The agent does not know it is reading your memory. It just reads the files. But from its perspective, it already knows the project. Already knows the rules. Already knows what is off-limits and why.

That is the harness doing the work.

## Context Engineering Is Actually Discipline

There is a concept called context engineering that sounds more sophisticated than it is.

It means: be intentional about what you put in the agent's context window.

The context window is not infinite. The bigger it gets, the worse the reasoning gets. You want the agent working in a focused slice of information, not drowning in everything at once.

Practically this means a few things.

One task per session. Not five. Not a refactor and a new feature and a debugging session all in one thread. One bounded task, clean scope, fresh session.

Small files in, not giant dumps. When I need the agent to understand a part of the system, I point it to specific files, not the entire repo. Let it search. The models are good enough to find the right function without you pre-loading the entire codebase.

Plan before execute. This one I enforced as a hard rule. If a task requires more than two tool calls, present a plan first. Why? Because the plan is not for the agent. The plan is for me. It is how I catch scope creep before the agent is halfway through doing something that will take an hour to unwind.

The agent will write a plan and it will sound completely reasonable and then you will notice it is about to touch seven files that should not be touched. Catching that in the plan is free. Catching it after the fact is not.

## Two Agents Reviewing Each Other

One pattern I ended up with that I did not see coming: using two agents in a review loop.

One agent builds. One agent reviews.

The builder does a pass. The reviewer reads the output, checks it against the rules, verifies the claims, flags the gaps, and writes what needs to change. The builder reads the review and does the next pass.

This is not because one agent is smarter than the other. It is because the agent that built something is the worst reviewer of that thing. Same as humans. The person who wrote the code is the person most likely to read what they intended rather than what is actually there.

The reviewer agent is reading with fresh context. It has not been through the process of building the thing. It is just looking at the output against the criteria.

What you get is a loop that actually converges. Build, review, fix, review again. Not perfect, but dramatically better than one agent running unchecked.

In finance especially, you cannot have the agent that made the decision also validate the decision. That is called conflict of interest. It has a name because it is a known failure mode.

<!-- INFOGRAPHIC: two-agent-review-loop - pending render -->

## The Oracle Rule

This is the principle I keep coming back to.

If the system generates data and validates that same data itself, the validation is worthless.

It sounds obvious when you say it like that. But it is very easy to build a system where the agent checks its own work, reports that it is correct, and you trust that because the report sounds confident.

Confidence is not evidence.

For anything that matters, the validation has to come from somewhere outside the thing being validated. In finance, this is obvious. You do not let the person who approved a trade also audit the trade. You do not let the system that generated the report also certify the report.

The same principle applies to agents. If your agent writes a proof and then validates the proof, you do not have a validated proof. You have a confident-sounding paragraph.

The fix is external ground truth. Public blockchain data. A second agent reading the same evidence. A human approval gate. A test that the code either passes or it does not. Something outside the generation step.

In my own system this took a while to actually enforce. The tempting thing is to let the agent self-report because it is faster. But fast and correct are not the same thing.

## The Finance Constraint That Changed Everything

Working in regulated finance changes how you think about agents.

You cannot ship and iterate on things that affect compliance, risk scoring, or money movement the way you can iterate on a landing page. The cost of an error is not a bad review. The cost of an error is a regulatory notice.

So the agents I build have hard stops.

No proof row, no product claim. If the system says something happened, it needs a ledger entry, a test result, a chain record, or a human sign-off. Not a confident paragraph. An artifact.

And the agent needs to know where it stops. Not because the agent is untrustworthy. But because there are things the agent cannot legally conclude, cannot legally act on, and should not be building opinions about without explicit authorization.

That boundary is not a limitation. That boundary is what makes the system deployable in a real environment.

The agent that knows where to stop is more useful than the agent that goes everywhere and does unpredictable things.

<!-- INFOGRAPHIC: agent-boundary-gates - pending render -->

## What Took the Longest to Learn

The model is not the problem.

The model is genuinely good. If you are getting bad results, the most likely issue is context engineering, harness design, or scope. Not the model's capability.

The things that took the longest to learn:

A small clean task beats a big ambitious one every time. Ten small passes that each do one thing correctly compound. One big pass that does seven things imperfectly is a debugging session.

Session memory is a product decision. If you do not design how context persists between sessions, the agent forgets and you repeat yourself. Designing the memory is part of designing the system.

Plans are for you, not the agent. Generate a plan, read it, shrink it, then hand it to the agent. The plan that comes out of the agent's first attempt is almost always too large for one pass. Break it before you start.

The harness you build for a personal side project is different from the harness you need for a system that runs overnight and touches financial data. Design to the actual risk level.

And the thing I came back to the most: if the system is not producing something you would stake your name on, the answer is not to push harder. The answer is to check the harness.

The harness is the work.

---

*I work inside a Canadian financial institution and build compliance and agent systems on the side. The opinions here are my own.*

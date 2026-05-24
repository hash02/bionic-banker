---
title: "Karpathy Drew the Map. Here Is What It Looks Like From Inside a Bank."
description: "Andrej Karpathy's AI Startup School talk gave the clearest framework for the software transition we are living through. Here is the same map applied to financial services, from someone building on both sides of the wall."
date: "2026-05-20"
tags: ["AI", "Banking", "Agents", "Finance"]
readTime: "9 min"
category: "AI"
featured: true
slug: "karpathy-banking-software-era"
image: "/blog-visuals/png/karpathy-banking-hero.png"
---

Andrej Karpathy's AI Startup School talk described three generations of software and why LLMs represent a genuinely new type of computer. Every layer he mapped is actively playing out inside financial services right now. Most people watching that talk work in tech. I work inside a bank. The view is different from here.

# Karpathy Drew the Map. Here Is What It Looks Like From Inside a Bank.

Okay so there is a mind map of Karpathy's talk going around right now. Software 1.0, 2.0, 3.0. The autonomy slider. Agents are coming slowly over the next decade. LLMs as CPUs where context is memory and prompts are instructions.

I have watched that framework float through tech Twitter for a few days and I keep waiting for someone to say what it looks like from inside a financial institution. Because I am building agents on one side and watching a bank run on the other, and the translation is not obvious.

So here it is.

## Software 1.0 Is Not Dead in Banking. It Is Load-Bearing.

Karpathy described Software 1.0 as traditional programming using explicit code. C++, Python, humans writing rules manually.

In banking, Software 1.0 is the entire foundation. Core banking platforms built in COBOL in the 1970s are still processing your transactions today. The rules are explicit. The code is deterministic. And it is holding up hundreds of billions in daily settlement volume.

This is not a failure. This is load-bearing infrastructure that has not failed in fifty years.

The problem is that Software 1.0 cannot talk to Software 3.0 without translation layers, and those translation layers are where most of the friction in bank AI projects lives. Every time you hear a bank say their AI project is "delayed due to integration complexity," what they mean is: we are trying to connect a 2026 LLM to a 1978 data model, and nobody fully documented the bridge.

## Software 2.0 Is Already Running. You Just Do Not See It.

Software 2.0 is Karpathy's term for neural networks where code is learned, not written. Models trained on data.

Banks have been running Software 2.0 since at least 2015. Every fraud detection system, every credit score model, every customer churn prediction engine. That layer is mature. RBC's Borealis AI lab has been publishing peer-reviewed machine learning research for a decade. TD's Layer 6 acquisition in 2018 brought deep ML capability into retail banking. This is not new.

What is new is that Software 2.0 models were mostly running invisible. You did not see them. They ran in the background and surfaced a score or a flag. A human read the output and made the decision.

Software 3.0 is the layer that breaks that pattern.

## Software 3.0 Is Where the Interesting Thing Happens

LLMs programmable via natural language. Prompts as source code. A new type of computer where anyone who speaks English can write the program.

In banking, this is hitting three places at once.

First, internal tooling. Analysts who used to write SQL queries are writing natural language requests to internal data tools. Junior employees are getting instant access to institutional knowledge that used to sit in a senior analyst's head. The knowledge democratization is real. It is also slightly terrifying for the people whose value was in holding that knowledge.

Second, customer-facing products. The chatbot layer has been around for years. What is new is the agentic layer underneath it. When a customer asks a question, the agent does not just look up an FAQ. It can pull their account history, check their risk profile, cross-reference regulatory flags, and come back with a contextual answer. That is Software 3.0 running on Software 1.0 data rails.

Third, compliance workflows. This one does not get enough attention. The compliance function in a large bank is basically a massive Software 1.0 operation. Rules written down. Humans applying them manually. Karpathy described building fast generation-verification loops as a best practice for LLM workflows. Banks are now starting to build exactly this: an agent generates a compliance narrative, a human verifies it, the agent learns the correction pattern. That loop is compressing months of manual work into hours.

## The Autonomy Slider Is Not a Tech Setting. It Is a Regulatory Negotiation.

This is the most important translation from Karpathy's talk to the banking context.

He described an "autonomy slider" where you can adjust how much of a task an agent executes autonomously versus how much a human verifies. Partial autonomy is preferred to fully autonomous agents right now.

In banking, that slider is not just a product decision. It is a conversation with OSFI (Canada's banking regulator), with your legal team, with your model risk governance framework, and with the board's risk appetite statement.

When HDFC's Eva chatbot started handling millions of queries autonomously, that was a business decision AND a regulatory one. ANZ collapsing 20 systems into one agentic dashboard and giving business bankers back a month of time was possible because the agents were doing orchestration and information retrieval, not making credit decisions.

The autonomy slider in banking moves slowly not because banks are afraid of technology. It moves slowly because "an agent made an error" in financial services can mean a customer's funds went somewhere they should not have. The blast radius is real.

What Karpathy's framing gives us is a useful way to describe what regulators are actually asking for when they say "explainability" or "human oversight." They are asking you to show them where the slider is set, and prove that the human verification step is genuine, not theater.

## The 1960s Computing Analogy Lands Differently Here

Karpathy said the current LLM ecosystem is comparable to computing in the 1960s. Centralized compute with time-sharing. Lacking general-purpose GUIs. Expensive, specialized infrastructure.

I want to sit with this analogy for a moment because it explains something about why banks are building differently than startups.

In the 1960s, the institutions with capital and access to centralized mainframes were the ones that built first. They were not the most agile. They were the ones with the infrastructure budget and the institutional patience to run a multi-year technology adoption curve.

That sounds familiar.

The Big Five Canadian banks are not moving slow because they do not understand the technology. They are moving at the pace of institutions that have watched technology cycles before and know that the first movers in the 1960s mainframe era often had to rip everything out and rebuild when the next layer arrived. They are building for durability, not just speed.

The startups watching them and saying "they are so slow" are probably right about the speed. They may be wrong about what slow means for an institution that needs to still be running in fifty years.

## What Vibe Coding Means in a Regulated Environment

Karpathy described natural-language coding as using English as code. Ideal for rapid prototyping. Good when existing software does not fit. Challenges include deployment, auth, and devops still being bottlenecks.

Every word of that is accurate inside a financial institution, with one addition: compliance review is another bottleneck that does not exist in most startup contexts.

When I build something using AI-assisted prototyping patterns and want to show it to someone inside a financial institution, the conversation is not just "does this work" and "can we deploy it." It is "what data does this touch," "what is the audit trail," "how do we explain this to a regulator if something goes wrong."

That is not a reason to not build. It is the context the building happens in.

The interesting thing is that AI-assisted prototyping is actually making the internal prototyping loop faster for the first time. You can get something in front of the right people faster, get feedback earlier, and either kill it or send it to proper development sooner. The waste in the old process was not in development. It was in the months of meetings before development started. That part is compressing.

## What Karpathy Left Out (That Matters in Finance)

The talk was aimed at founders. The design principles for LLM-readable documentation, the llms.txt tool, the structured metadata recommendations, all of that assumes you are building your own stack from scratch.

Financial institutions are mostly not building from scratch. They are integrating into stacks that are fifteen to fifty years old. The documentation was written for humans. The APIs were designed before REST was a thing. The data models were optimized for a world where storage was expensive and structured queries were the only option.

The work of applying Karpathy's principles in banking is mostly the work of translation. How do you make a 1978 data model LLM-readable without rebuilding the 1978 data model? How do you build small, auditable increments when the system you are modifying requires a three-month change control cycle?

These are not unsolved problems. They are just different problems than the ones Karpathy was describing.

## The Rare Opportunity Framing Is Right, But It Cuts Both Ways

Karpathy's final reflections included: "a rare opportunity for newcomers to the tech industry." Programming is democratized. The entire software stack needs rewriting.

From inside a bank, I read that as: the people who understand both layers are going to be valuable in ways that specialists are not. Someone who understands the Software 1.0 infrastructure that is load-bearing AND knows how to build Software 3.0 agents on top of it is not replaceable by a fresh LLM prompt.

The opportunity is real. It is just not the opportunity that most AI Startup School attendees are thinking about. The opportunity in banking AI is not the greenfield startup. It is the integration layer. The bridge between 1978 and 2026.

That is a less exciting story to tell at a startup school. It is a more stable place to be building.

---

Karpathy drew the map. The terrain it describes is real. The translation into banking is the work that is actually happening, slowly and not always visibly, inside every major financial institution right now.

I am building on both sides of that wall. The map helps.

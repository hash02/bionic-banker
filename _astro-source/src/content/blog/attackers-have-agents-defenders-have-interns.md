---
title: "Attackers already have agents. Defenders are still training interns."
description: "Open banking stalled. AI didn’t. The Bank of Canada told you both things in the same month. Here is what the dual-speed problem means for banks, for fraud, and for which jobs shrink first."
date: "2026-04-18"
tags: ["AI", "Banking", "Agents", "Fintech"]
readTime: "7 min"
category: "AI"
featured: true
slug: "attackers-have-agents-defenders-have-interns"
image: "/blog-visuals/png/boc-defi-hero-banner.png"
---

# Attackers already have agents. Defenders are still training interns.

Okay so here is the thing nobody wants to say out loud. In the same month the Bank of Canada published a research paper calling Aave a functioning non-bank lending system, they also said they were not committing to a launch date for open banking. Same institution. Same month. Opposite speeds.

One hand is cheering decentralized finance. The other is holding the line on public rails.

And while both hands argue with each other, a third group is moving faster than either of them. The people building attack agents.

## Quick primer, because most people still have not been told

Open banking means your bank has to let you send your transaction data to another company through an API, if you ask it to. That is the short version. It is a rail, same as Visa or Interac, except instead of moving money it moves information. Read access first, which means apps can see your accounts. Write access later, which means apps can actually move money on your behalf. Phase 1 was targeted for early 2026. It did not ship. Phase 2 is on the board for mid-2027.

The law is real. The Consumer-Driven Banking Act passed on March 26 with Royal Assent. The Bank of Canada was handed the keys. Then the head of payments said a 2026 launch would be premature and ill-advised.

I wrote the full breakdown earlier today in [Canada's open banking law just turned on. Nobody will say when the APIs do.](/blog/canada-open-banking-law-no-date/) The stall is honest and the stall is the right call on governance. Rushed open banking in other countries shipped systems that 80 percent of the market ignored. Canada is trying not to repeat that.

But governance speed and attack speed are two unrelated clocks.

## The asymmetry

Scammers did not wait for BoC to publish a policy paper. They already built the agents.

A single fraud operator today spins up a language model, feeds it a target list, and runs plausible phishing across Teams, WhatsApp, and email at a scale that used to require a call center. SIM swap orchestration that used to need insiders now gets automated by models that have read every playbook on the open web. Cross-platform account-takeover flows chain agents together. Agent one gathers the target. Agent two writes the message. Agent three handles the reply. Agent four exfiltrates.

You know what the compliance team uses to respond? People. A queue of flagged tickets. A review template. A manager. Maybe a rules engine from 2017. The attack surface is running on frontier models. The response surface is running on business logic and headcount.

That gap is not small. That gap is the story.

## The pincer

Here is why the stall makes the asymmetry worse, and also why open banking is not optional, no matter what any regulator says in any press conference.

If the law did not exist, the tech wave would force the rails anyway. Apps like Revolut, Monzo, Wise, and Plaid built read and write access in other countries because customers demanded it. That demand does not stop at the Canadian border. Every year the public rail is delayed, private one-off APIs between big banks and specific fintechs get normalized. That is a private version of open banking without any of the consumer protections.

If the tech wave did not exist, the law would force the rails anyway. The Act is on the books. Screen scraping is now an offence. Phase 1 has to happen. The regulator can slow the timeline. The regulator cannot cancel the outcome.

Pincer. Both arms push the same direction. Open banking is arriving one way or another. The only question is whether it arrives from a public rail with clean standards and accredited providers, or from a patchwork of private deals that favor incumbents. The two paths are different by a lot.

## What this has to do with Aave

This is where it ties back to the piece I published last week on [the Bank of Canada studying Aave](/blog/boc-defi-lending/). When a central bank publishes a formal paper saying a DeFi protocol works, zero bad debt, 24/7 operation, transparent rules, they are not just studying. They are telling the banking system that the old model now has a competitor that does not wait for governance cycles.

Aave does not care about a 2026 launch date. The protocol is open. The code is running. The total value locked is growing.

Same pattern. Regulators can stall rails. They cannot stall tech. The BoC is intellectually honest about both and that honesty is the signal. You read two papers this month and the message in both was: the old speed is over.

## Which jobs shrink first

Here is where it gets personal. Some roles compress hard and fast over the next 24 months. Not theoretical. Already happening quietly in every financial institution you recognize.

First to go: anyone whose day is receive a document, check a list of boxes, forward to the next desk. That workflow is an agent now. In some places it already is, just nobody is advertising it. The AI efficiency numbers you see in bank earnings calls, one of the Big Six reported 1.2 million hours saved in a single quarter, those hours were being spent by real people doing real work. Those people are either being asked to do different things or they are not being asked.

Second: rules-based compliance review. Not the complex cases. The Tier 1 queue. The noisy alerts. The 95 percent false positives.

Third, slower but certain: document-heavy roles in underwriting, KYC, and onboarding. Not because agents are smarter than the analysts. Because the volume argument is unbeatable, and the training data already exists.

What survives is the role that does three things at once. Understands the rail. Understands the fraud surface. Builds the guardrails. That role has barely been invented. There are not enough people who can do it yet.

The organizations that move through the next decade intact will be the ones that convert good analysts into that tier before the tier gets commoditized too.

## The play if you are reading this

You have a window. Maybe 18 to 24 months before the tooling is sharp enough that institutions stop hiring the old shape of role entirely.

The window is not about learning to prompt. Everybody is going to learn to prompt. The window is about learning to operate the full agent stack inside a regulated environment. How agents are built. How they fail. How they lie. How they escalate. How a bank or a fintech stands them up without tripping a privacy or compliance wire.

That is a role. That role needs humans. That role pays.

## The one thing I actually want you to remember

Regulatory time and attack time are not the same clock. The Bank of Canada published two signals this month, one stall and one endorsement, and the message is the same from both angles. DeFi works. Open banking is coming. Neither one is going to wait for you.

If you are inside a bank, a credit union, a fintech, or a regulator, build the agent stack muscle now. Not later. The people who read this and move in the next six months will be in a different place than the people who read this and bookmark it.

I will keep writing as the technical spec drops and the fraud patterns mature. The speed of that clock is the story.

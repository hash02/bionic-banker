---
title: "Canada’s open banking law just turned on. Nobody will say when the APIs do."
description: "The Consumer-Driven Banking Act passed March 26. The Bank of Canada runs it now. And the lead regulator just called a 2026 launch ‘premature.’ Here’s what actually changes for builders, what doesn’t, and what to watch."
date: "2026-04-18"
tags: ["Fintech", "Banking", "Canada", "API"]
readTime: "7 min"
category: "Fintech"
featured: true
slug: "canada-open-banking-law-no-date"
image: "/blog-visuals/png/boc-defi-hero-banner.png"
---

# Canada’s open banking law just turned on. Nobody will say when the APIs do.

Okay so on March 26 this year, Bill C-15 got Royal Assent. Inside it was something called the Consumer-Driven Banking Act. That is the real name for what everyone has been calling open banking in Canada for like six years. The law is real now. It exists. It is on the books.

Then two weeks later, the Bank of Canada, which is the regulator picked to actually run the thing, basically said: yeah we are not committing to a launch date. The head of payments there called a 2026 launch "premature and ill-advised." So we have a law with no date.

That is where we are. April 2026. Law yes. Launch no.

Here is the thing. Most of the coverage I have seen makes this sound like a failure. It is not. It is the most honest thing a financial regulator has said in a decade. Every country that rushed this broke something. The UK launched PSD2 in 2018 and spent four years duct-taping the API spec. Australia CDR went live in 2020 and five years later the participation rates are, to be polite, not great. Brazil did Pix first and it worked because they built it at the rails level, not as a regulatory overlay on top of existing banks. Canada watched all three.

So let me walk through what actually got decided, what is still open, and what you can do about it if you are a builder.

## What the law actually does

Think of it as a two-phase unlock tree. Phase 1 is read access. Phase 2 is read plus write access. Phase 1 was targeted for early 2026. Phase 2 is on the board for mid-2027, assuming Phase 1 shipped, which it has not.

Read access means: as a customer, you can tell your bank to hand over transaction data to another company through an API. Standardized, secure, auditable. Your balances, your transaction history, your account details. That is it. No moving money yet.

Write access is the one everyone actually wants. That is where you can tell your bank to let another app move money on your behalf. Payment initiation. Account switching without printing a PDF. Auto-debiting a competitor bill pay into your primary. It is the thing that turned Revolut, Monzo, Wise into real players in the UK. Write access is the rail. Read access is just staring at the rail.

The quiet detail most people missed: Phase 2 is explicitly tied to Canada Real-Time Rail payments infrastructure. RTR is Payments Canada next-gen real-time settlement system. It has been coming soon for about a decade. If RTR slips, write access slips.

## Screen scraping just became a crime

Here is the one change that matters today, regardless of when the APIs turn on. Screen scraping is now an offence under the Act. Not just discouraged. Not just against your bank terms of service. An offence.

For context: Canadian personal finance apps have been doing screen scraping for years. You give them your bank login, they log in as you, they pull your data, they show it back to you. It is how Mint worked. It is how half the budgeting apps work. It is the most insecure way to move financial data short of writing your PIN on a postcard.

The law does not just ban scraping going forward. It creates a legal runway where scrapers have to migrate to APIs or shut down. Which is awkward because the APIs do not formally exist yet. So there is a weird gap: scraping is illegal, the legal replacement has not launched.

This is where the private API story comes in. Every Big Six bank has quietly been signing one-off deals with specific fintechs for private read APIs. They are not public. They are not standardized. They are dollar-per-call commercial contracts. This is the bridge layer while the public rail gets built. If you are a fintech in Canada today, you are either on a private deal or you are scraping and now pretending you are not.

## Why giving it to the Bank of Canada matters

The other structural change is who is in charge. The original plan had the Financial Consumer Agency of Canada running it. Budget 2025 pulled that and gave it to the Bank of Canada instead. Allocated 19.3 million over two years for the transition.

That is the most consequential move in the whole file. FCAC is a consumer protection agency. The Bank of Canada is a central bank with systemic responsibility. Different mandates. FCAC would have built this to protect consumers from fintechs. BoC will build this to not break the financial system.

BoC already runs the Retail Payment Activities Act and the registry of payment service providers. So consolidating everything under one roof creates a cleaner governance line. Which is why BoC is also the one saying slow down. They know what it takes to regulate real payment rails. They have seen other countries ship too fast.

## What actually changes for you

If you are a consumer: nothing, yet. You still cannot take your bank transaction history and port it into a third-party app without giving up your login. Phase 1 was supposed to fix that this year. It probably will not.

If you are a builder: three things actually changed.

First, the legal landscape for scraping is now uncomfortable. If you are building on scraped data, you have a shrinking window. Even if enforcement is slow, every investor, every bank partner, every compliance officer at a bigger firm knows this now. Scraping is a red flag in a way it was not in 2024.

Second, consumer liability flipped. Under the Act, consumers are not on the hook for losses from unauthorized data sharing, unless they were grossly negligent. That is a massive change from the status quo, where losing money to a hacked third party was mostly your problem. This shifts risk onto the bank and the third party, which means the bank now has skin in the game when picking API partners. Translation: the private API deals are about to get picky.

Third, the Big Six now have a policy alibi to prioritize this work. For years, open banking was a thing their strategy teams talked about but their engineering teams did not have funding for. Now it is federal law. The budgets are about to open up.

## How to watch this without getting lost

Three things to track this year. The Bank of Canada putting out technical standards is the real signal the rail is getting built. When they publish the API spec, that is the starter pistol. Nothing is real until then. Second, the Real-Time Rail timeline from Payments Canada. If RTR slips again, Phase 2 slips with it. Third, watch which fintechs get listed in the registry of payment service providers. That list is going to map one-to-one onto who gets to build on the rail first.

Everything else is commentary.

## What I actually think

I have spent a lot of time in Canadian financial plumbing, from both sides. What I think is happening is: Canada is building this slowly on purpose, because the BoC watched Australia and is not interested in shipping an open banking system that 80 percent of eligible third parties never bother connecting to. That is what a failure mode looks like when you rush the standards.

The UK, in contrast, got bailed out by culture. British banks were getting roasted daily by fintech Twitter and fintech press. There was pressure to make the APIs actually usable. Canada does not have that culture. Canadian fintech press is small. Canadian consumers do not switch banks. So the only forcing function is the regulator, and the regulator just said slow down. Which, if you squint, is fine, because the alternative is shipping a rail nobody drives on.

But the cost is time. Every year we wait is another year of private API deals that favor large incumbents. Another year of scraping being the only option for small players. Another year where Canadian fintech founders build in the UK or the US because that is where the rails are.

So yeah. Law passed. No date. Watch the technical spec. Do not build on scraping. And if you can, find the people inside the Big Six who are already building the API stack, because those are the folks who are going to decide how this actually works.

I will come back to this when BoC drops the spec. That is when it gets real.

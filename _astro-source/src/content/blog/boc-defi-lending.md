---
title: "The Bank of Canada Just Studied Aave. I Was Using It Six Years Ago."
description: "The Bank of Canada published a deep study on Aave V3 and DeFi lending in April 2026. Here's what it means, why it matters, and what I learned the hard way years before the report existed."
date: "2026-04-12"
tags: ["DeFi", "Blockchain", "Finance", "Central Banking"]
readTime: "12 min"
category: "DeFi"
featured: true
slug: "boc-defi-lending"
image: "/blog-visuals/png/boc-defi-hero.png"
---

# The Bank of Canada Just Studied Aave. I Was Using It Six Years Ago.

In April 2026, the Bank of Canada published a formal research paper on Aave V3, the biggest DeFi lending protocol in the world. They concluded that decentralized lending is technically and operationally viable. This is what that means, why it matters, and what I learned the hard way years before the report existed.

Two years ago, I published a [technical breakdown of how Aave works](/blog/aave) on this very site. But my actual story with DeFi lending started way before that.

Six years ago, a younger and way more naive version of me discovered Aave and Compound. I thought I had found the cheat code to wealth. I did what the Bank of Canada now formally calls "recursive leverage." Borrow against your collateral, swap into more collateral, deposit it, borrow again. Repeat until you feel invincible.

Spoiler: those smart contracts don't send you a polite email before they liquidate you.

I learned every single lesson the Bank of Canada is now documenting in their staff analytical paper. Except I learned them with my own money, in real time, with no central bank research team to warn me first.

So when I saw their April 2026 report drop, I couldn't help but smile.

## What the Bank of Canada Actually Found

The paper is called *"DeFi Lending: Returns, Leverage, and Liquidation Risk"* (Staff Analytical Paper 2026-13), written by Jonathan Chiu and Furkan Danisman. It examines real transaction-level data from Aave V3, the largest DeFi lending protocol by total value locked.

Here's what they found.

First, the protocol works. Aave runs 24/7 with near-zero overhead. No branches, no staff, no compliance teams manually reviewing loan applications. The smart contract matches borrowers and lenders, enforces collateral constraints, and maintains solvency without relying on trust, identity, or centralized enforcement. The system is continuous, transparent, and efficient.

Second, revenue is extremely concentrated. Three tokens, WETH, USDT, and USDC, drive approximately 83% of Aave's total earnings. That's a lot of eggs in very few baskets.

Third, people are using leverage aggressively. Margin trading through recursive borrowing accounts for roughly 20% of total borrowing volume. This is exactly what I was doing six years ago. You borrow, you buy more collateral, you deposit it, you borrow again. The Bank of Canada formally documented this pattern. I lived it.

Fourth, when things go wrong, they go wrong fast. Liquidations don't happen gradually. They come in concentrated waves. The ten largest liquidation events accounted for 80% of all liquidated volume. When it hits, borrowers can lose 10 to 30% of their collateral in a single event.

And here's the part that really matters: large investors, just 2% of the platform, get liquidated at twice the rate of regular users. The whales feel the pain the hardest because they're the most leveraged.

<div class="embed-visual">
  <iframe src="/blog-visuals/boc-defi/comparison-table.html" style="width:100%;height:520px;border:none;border-radius:12px;"></iframe>
  <noscript><img src="/blog-visuals/png/boc-defi-comparison-table.png" alt="Aave V3 vs Traditional Banks comparison table" style="width:100%;border-radius:12px;" loading="lazy" /></noscript>
  <p class="embed-caption"><span class="interactive-badge">INTERACTIVE</span> Aave V3 vs. Traditional Banks: Key Metrics Compared (Source: Bank of Canada SAP 2026-13)</p>
</div>

## Why This Report Is a Signal, Not Just Research

Canada has one of the most tightly regulated banking systems in the world. Five big banks control the vast majority of the market. OSFI sets strict capital requirements. Consumer protection rules are layered deep. This is not a country that publishes casual opinions about decentralized finance.

So when the Bank of Canada releases a formal staff analytical paper that says decentralized lending is "technically and operationally viable," pay attention. They did not have to publish this. They chose to.

That choice is the signal.

They are telling the industry, in their own careful, academic language, that this model works. It's messy in places, it's risky in places, but the core mechanism of protocol-based lending without traditional intermediaries is sound.

This isn't a crypto blog hyping a token. This is a central bank doing its homework, looking at the data, and saying: this is real.

## Most People Still Don't Understand What DeFi Actually Is

Let me back up for a second, because I think this needs saying.

DeFi, short for Decentralized Finance, is a system where financial services run entirely on smart contracts instead of banks. Lending, borrowing, trading. No humans in the middle approving your loan. The rules are written in code, and the code is the final authority.

In traditional banking, law is the law. Rules are written in legal documents and enforced by people, regulators, and courts. If you miss a payment, a human somewhere decides what happens next.

In DeFi, code is the law. The smart contract doesn't care who you are, how important you are, or whether you know someone. If your collateral falls below the required threshold, the code liquidates you. Automatically. Instantly. No emotion, no negotiation, no second chances.

And here's the thing that makes this philosophically different from anything that came before: this enforcement isn't backed by threat of punishment. It's backed by mathematics. The rules are enforced by cryptography and consensus, not by courts and compliance officers.

That is an extremely powerful concept. And also a dangerous one, if you don't respect it.

<div class="embed-visual">
  <iframe src="/blog-visuals/boc-defi/code-is-law.html" style="width:100%;height:480px;border:none;border-radius:12px;"></iframe>
  <noscript><img src="/blog-visuals/png/boc-defi-code-is-law.png" alt="How Enforcement Works: Traditional Finance vs DeFi" style="width:100%;border-radius:12px;" loading="lazy" /></noscript>
  <p class="embed-caption"><span class="interactive-badge">INTERACTIVE</span> How Enforcement Works: Traditional Finance vs. DeFi Lending</p>
</div>

## What I Learned Before the Report Existed

Six years ago, I treated Aave and Compound like a video game. I genuinely thought recursive leverage was a free money glitch. Borrow, swap, deposit, borrow again. My portfolio looked incredible on paper.

Then the market moved against me. And those automatic liquidations the Bank of Canada describes in their paper? I can confirm they're exactly as brutal as they sound. No warning email. No phone call from a relationship manager. Just your position, gone.

But here's the part that most people miss.

Every single transaction I made on Aave and Compound six years ago is still visible on the blockchain today. Every reckless trade, every liquidation, every painful lesson. Timestamped, permanent, verifiable by anyone.

That is one of the most underrated powers of blockchain: proof of behavior over time.

Try asking your bank for a complete, detailed record of every loan, every interest payment, every fee from six years ago. You'll wait weeks and probably get an incomplete PDF. On-chain, it's all there. Instantly. Forever.

When the Bank of Canada talks about transparency being a core advantage of DeFi protocols, this is what they mean. It's not a marketing buzzword. It's a fundamentally different relationship with financial data.

## The Timing Is Not a Coincidence

There's a much bigger story here that very few people are connecting.

As AI becomes more powerful every single month, the job of protecting traditional closed-ledger financial systems is getting harder. The attack surfaces are growing. The complexity of threats is increasing. AI can generate sophisticated social engineering, detect patterns in systems faster than humans can patch them, and operate at a scale that traditional security teams struggle to match.

Blockchain-based systems, whether fully decentralized like Ethereum or permissioned and private, offer a fundamentally different security model. Everything is public, immutable, and secured by mathematics instead of internal controls. You can't quietly edit a transaction after the fact. You can't hide a bad loan in a spreadsheet somewhere.

The Bank of Canada releasing this paper right now, in a world where AI capabilities are accelerating weekly, is not just about understanding DeFi. It's about understanding what kind of financial infrastructure can actually hold up as the threat landscape evolves.

Whether you're using a public blockchain or a permissioned one inside a bank, the principle is the same: mathematical security and radical transparency are becoming necessities, not luxuries.

## This Is Not a Competition. It's a Preference.

I want to be clear about something, because I think a lot of people get this wrong.

DeFi is not going to kill traditional banking. Traditional banking is not going to kill DeFi. That framing is lazy and wrong.

What's actually happening is much more interesting. We're watching two different systems evolve to serve two different types of customers.

Some people want speed, transparency, and complete control over their assets. They want to see exactly what's happening with their money at all times. They're comfortable managing their own risk. These people will gravitate toward DeFi-style products.

Other people want someone to hold their hand, take responsibility, and handle the complexity for them. They want a human they can call when something goes wrong. They value safety nets over speed. These people will stay with traditional banking, and there's nothing wrong with that.

It's like asking whether restaurants will kill home cooking. They serve different needs. Both will exist. The interesting question is how they interact.

The Bank of Canada's paper suggests they're starting to think about exactly that interaction. How do you take the efficiency of DeFi (zero bad debt, 24/7 operation, radical transparency) and bring it into a regulated environment that still protects consumers?

## Where This Goes From Here

Okay so here's where I start thinking out loud.

If the Bank of Canada has now formally acknowledged that protocol-based lending is viable, the next logical step for Canadian banks is obvious: build regulated versions of these systems.

Not by forking Aave and slapping a bank logo on it. That's not how this works. The real opportunity is taking the best parts of the model (instant execution, transparent rules, automatic enforcement, low overhead) and building them into products that fit inside the existing regulatory framework.

Start small. Something like vehicle-backed instant loans. Think of it as a digital HELOC for your car. You prove ownership, the system instantly evaluates the collateral value, and you get funds in minutes instead of days. The smart contract handles interest, repayment tracking, and liquidation if needed. All within a fully regulated, KYC-compliant environment.

The customer gets speed and transparency. The bank gets lower operational costs and a product that differentiates them. The regulator gets full compliance because every wallet is KYC'd and every transaction is on-chain and auditable.

The technology is ready. The central bank has done its homework. The only thing left is execution.

## The Loop Is Closing

Six years ago, I was a naive kid getting liquidated on Aave, learning expensive lessons that nobody was formally documenting. Two years ago, I was writing technical blogs trying to explain how these protocols work to an audience that mostly didn't care yet. Today, one of the most respected central banks in the world is publishing formal analysis on the exact same protocols.

The loop is closing.

We're standing at the intersection of three powerful forces: AI, blockchain, and traditional finance. The organizations that understand all three will lead the next decade. The ones that understand only one, or worse, none, will struggle to keep up.

The Bank of Canada just showed they understand. The question is: does everyone else?

If you've been thinking about the future of lending, DeFi, or how AI and blockchain are reshaping financial services, I'd love to hear your thoughts. I'm actively exploring how to take the insights from this paper and my own experience and turn them into something real. Not theory. Not another whitepaper. Something people can actually use.

If that interests you, whether you're in lending, risk, engineering, regulation, or just curious about where this is all heading, let's connect and build together.

> **Source:** Jonathan Chiu and Furkan Danisman, *"DeFi Lending: Returns, Leverage, and Liquidation Risk"*, Bank of Canada Staff Analytical Paper 2026-13, April 2026.

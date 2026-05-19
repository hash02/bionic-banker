---
title: "Uniswap and the Strange Genius of the Pool"
description: "A field note on automated market makers, liquidity pools, and why a simple swap button changed on-chain trading."
date: "2024-05-25"
tags: ["DeFi", "Blockchain", "DEX"]
readTime: "2 min"
category: "Tech"
featured: false
slug: "uniswap"
image: "/blog-visuals/uniswap/social-preview.png"
---

Okay so Uniswap is one of those ideas that looks too simple at first.

You open the page. You choose one token. You choose another token. You swap.

Under that button is the more interesting thing: there may be no order book, no market maker sitting at a desk, and no company matching buyers and sellers in the usual way. There is a pool. The pool holds two assets. A formula decides the price as people trade against it.

That is the strange genius of it.

## The Pool

In a basic automated market maker, liquidity providers put assets into a pool. Traders swap against that pool. The price changes because the balance inside the pool changes.

If people keep buying one side, that side gets scarcer in the pool, and its price rises. If people sell into the pool, the balance moves the other way.

It is not magic. It is inventory math.

But it means a market can exist anywhere someone can deploy a pool and someone else is willing to supply liquidity.

## The Catch

Liquidity is not free money. Providers earn fees, but they also take price risk. If the assets move hard against each other, the pool can leave them with a worse result than simply holding the assets outside the pool.

That is the famous impermanent loss problem.

Uniswap v3 made this more interesting by letting providers concentrate liquidity inside chosen price ranges. That can make capital more useful, but it also means providers have to think harder about where price may move.

## What I Watch

Uniswap matters because it turned exchange design into something programmable.

The signals I watch are:

- pool depth
- fee tiers
- slippage
- liquidity ranges
- token quality
- scam patterns around new pairs
- how fast arbitrage pulls pool prices back toward the broader market

The swap button is simple. The pool underneath is not. That tension is the whole story.

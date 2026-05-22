---
title: "The Leaderboard Nobody Is Talking About the Right Way"
description: "AI coding benchmarks are everywhere now. But most people read them wrong. The number that matters isn't the score. It's the score per dollar."
date: "2026-05-20"
tags: ["AI", "Builder"]
readTime: "6 min"
category: "AI"
image: "/blog-visuals/ai-model-benchmark-cost/hero.svg"
featured: false
slug: "ai-model-benchmark-cost"
---

There's a leaderboard going around right now. AI coding agent benchmarks. 14 models ranked by score percentage on a standardized task set. And everyone is pointing at the #1 slot.

Opus 4.7 Max. 64.8%. The best score.

And I get it. #1 is a clean headline.

But I work in finance, and the first thing they teach you when you read a table of numbers is: what column is everyone ignoring?

<div class="embed-visual">
  <iframe src="/blog-visuals/ai-model-benchmark-cost/score-per-dollar.html" title="The leaderboard has a hidden column" style="width:100%;min-height:560px;border:none;border-radius:12px;" loading="lazy"></iframe>
</div>

---

## The Column Everyone Is Ignoring

Here's the full picture from the leaderboard:

| Model | Score | Cost/Task |
|---|---|---|
| Opus 4.7 Max | 64.8% | $11.02 |
| GPT-5.5 Extra High | 64.3% | $4.37 |
| Composer 2.5 | 63.2% | $0.55 |
| GPT-5.5 High | 62.6% | $3.59 |
| Opus 4.7 Extra High | 61.6% | $7.11 |
| Opus 4.7 High | 59.4% | $5.01 |
| GPT-5.5 Medium | 59.2% | $2.22 |
| Opus 4.7 Medium | 52.7% | $2.93 |
| Composer 2 | 52.2% | $0.56 |
| Gemini 3.5 Flash | 49.8% | $1.94 |
| GPT-5.5 Low | 48.8% | $1.19 |
| Opus 4.7 Low | 48.3% | $1.87 |
| Kimi 2.6 | 47.6% | $1.27 |
| Kimi 2.5 | 31.9% | $0.87 |

Look at row three. Composer 2.5. 63.2% score. $0.55 per task.

Now look at row one. Opus 4.7 Max. 64.8% score. $11.02 per task.

A 1.6 percentage point difference in performance. A 20x difference in cost.

That's the number nobody is talking about.

---

## What 20x Actually Means When You're Building

If you're running a hundred tasks a day, here's the math:

- Opus 4.7 Max at $11.02: $1,102/day. $402,230/year.
- Composer 2.5 at $0.55: $55/day. $20,075/year.

You're paying $382,000 extra per year for 1.6% more accuracy.

Now, there are contexts where 1.6% matters. If you're building something where a wrong answer has a real cost, you pay for the margin. I understand that.

But most people who are clicking on that leaderboard are not running financial derivatives systems. They're building internal tools, prototypes, code agents, automation workflows. For that kind of work, the question is not "who has the highest score?" The question is "what's my acceptable accuracy threshold and what's the cheapest way to hit it?"

That's the actual question. And almost nobody is asking it.

---

## The Compute Tier Thing Is Fascinating

Here's something I find genuinely interesting. Look at how Opus 4.7 performs across its own tiers:

- Opus 4.7 Max: 64.8%, $11.02
- Opus 4.7 Extra High: 61.6%, $7.11
- Opus 4.7 High: 59.4%, $5.01
- Opus 4.7 Medium: 52.7%, $2.93
- Opus 4.7 Low: 48.3%, $1.87

Same underlying model. Different compute budget. More "thinking tokens" = higher score = higher cost.

So when you buy Opus 4.7 Max, you're not buying a smarter model. You're buying the same model with more time to think. You're paying for patience, basically.

That's a really interesting design choice. It also means the optimal tier depends entirely on the task. Some problems need Max. Most don't.

GPT-5.5 does the same thing across its tiers. Same model, different compute budget, different score/cost curve.

---

## The Composer Anomaly

Okay so Composer 2.5 is the one that stopped me.

Third place overall at 63.2%. Twenty cents cheaper than Gemini 3.5 Flash, which scores 14 points lower. Almost exactly tied with GPT-5.5 High at $3.59. But Composer costs $0.55.

I don't know the full architecture here. But 63.2% at $0.55 is just a different point on the curve from everyone else. Composer 2 was already doing this at $0.56 for 52.2%. The gap between Composer 2 and Composer 2.5 is 11 points in score with essentially zero change in cost.

That's a big jump for $0.01 more. Whatever they changed between versions, it worked.

---

## What This Looks Like From a Finance Lens

I spend a lot of time thinking about capital allocation. The core question is always: what return does this capital generate, and is there a cheaper way to get the same return?

That framing maps pretty cleanly onto AI model selection.

The score is the return. The cost per task is the capital deployed. The ratio is what you optimize.

By that framing, Composer 2.5 has the best ratio in this table. 63.2% score / $0.55 cost = 115 score-points per dollar. Opus 4.7 Max is 5.9 score-points per dollar. Composer is 19x more efficient on that ratio.

Now this is a simple ratio and I'm not claiming it captures everything. Model selection has layers. Latency, reliability, context window, tool use quality, how well it follows instructions under pressure. These things don't show up in benchmark scores.

But the ratio is still useful as a starting point. If your default is "just use the best model," you're leaving real money on the table.

---

## The Pattern I Keep Seeing

Everyone in AI goes through a phase where they want the best model for everything. Maximum compute. Highest score. The leaderboard winner.

Then you actually build something that runs at scale and you start caring about cost per output. Not because you're cheap. Because you're doing the math. And the math almost always says: most of your tasks don't need the top tier. Most of them can run on a cheaper model without you noticing the difference.

The builders who figure this out early end up with systems that can actually run continuously. The ones who don't end up with expensive demos that work great and can't scale to production.

That's not just a tech lesson. That's a capital efficiency lesson. Same principle, different domain.

---

The leaderboard isn't wrong. Opus 4.7 Max is the best performer by score. But if you're building something real, the score column is only half the table. Read the cost column too.

That's usually where the actual decision lives.

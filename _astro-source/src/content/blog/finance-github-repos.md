---
title: "7 Repos From the Most Expensive Engineering Teams in the World"
description: "Jane Street, Goldman, JPMorgan, BlackRock, Hudson River Trading, Two Sigma, D.E. Shaw. They open-sourced real internal tools. Here's what each one tells you about how elite trading firms actually think."
date: "2026-05-20"
tags: ["Finance", "Builder", "AI"]
readTime: "7 min"
category: "Finance"
image: "/blog-visuals/finance-github-repos/hero.svg"
featured: false
slug: "finance-github-repos"
---

Okay so here's the thing about elite trading firms. They spend millions per engineer per year. Their hiring processes are famous for being brutally hard. Their infrastructure is the actual competitive advantage.

And then they put some of it on GitHub.

Not marketing demos. Not hello-world tutorials. Real internal tools. The stuff their engineers and traders actually use.

I went through seven of them, one from each firm. Here's what caught my attention and why.

<div class="embed-visual">
  <iframe src="/blog-visuals/finance-github-repos/repo-map.html" title="What elite finance open-sources" style="width:100%;min-height:620px;border:none;border-radius:12px;" loading="lazy"></iframe>
</div>

---

## 1. Jane Street: magic-trace

**Repo:** [janestreet/magic-trace](https://github.com/janestreet/magic-trace)
**Stars:** 5.3k

Jane Street is an OCaml shop. That's already a signal. While everyone else is writing Python and Go, Jane Street builds their core infrastructure in a language that makes you think harder about types before the code even compiles. That's a cultural choice about what matters.

magic-trace is a process tracer powered by Intel PT (Processor Trace). What that means practically: when your profiler tells you a function is slow, you can see every CPU instruction that ran to get there. Not sampling. Every instruction.

Normal profilers sample. They check in at intervals and estimate where time is being spent. That's fine for most applications. When you're running strategies where milliseconds are money, "estimate" is not good enough. You need to know exactly what happened, in exactly what order, at exactly what time.

This is what that level of precision looks like when it's packaged into a usable tool and open-sourced.

---

## 2. Goldman Sachs: gs-quant

**Repo:** [goldmansachs/gs-quant](https://github.com/goldmansachs/gs-quant)
**License:** MIT

This one genuinely surprised me when I first saw it. gs-quant is the derivative pricing library Goldman Sachs traders use at their desks. Python, open-source, MIT licensed.

Derivative pricing is not a generic problem. The math involves stochastic processes, volatility models, and a lot of numerical methods that have to be fast and accurate simultaneously. Banks spend significant time building and calibrating these internally.

The fact that Goldman published this means one of two things: either they're confident enough in their execution edge that the pricing library itself isn't the moat, or they see value in the shared tooling benefits from open-sourcing it. Probably both.

For anyone building quantitative tools or learning how institutional derivative pricing actually works, this is a reference you can actually run. Not a textbook. Working code.

---

## 3. JPMorgan: perspective

**Repo:** [finos/perspective](https://github.com/finos/perspective)
**Context:** Maintained under FINOS (Fintech Open Source Foundation)

Bloomberg Terminal is roughly $24,000 per year per seat. Perspective is what JPMorgan traders use to watch markets in real time. And it's free.

Technically it's a streaming data visualization engine. What that means in practice: you can connect it to a data source, and as new data comes in, the view updates in real time. Tables, pivot grids, charts. High-frequency data. The thing doesn't flinch.

The reason this matters for building: most charting libraries are designed for static or slow-moving data. They were not built to handle tick-level market data where rows are updating hundreds of times per second. Perspective was. That's a different class of problem and the library reflects it.

It's now maintained under FINOS, which is the Fintech Open Source Foundation. That's a good structure for long-term maintenance. Banks contribute, the foundation governs, nobody owns it outright.

---

## 4. BlackRock: lcso

**Repo:** [blackrock/lcso](https://github.com/blackrock/lcso)
**Language:** Rust

The name stands for Layered Conic Solver for Optimization. The elevator pitch: where scipy gives up, this works.

Portfolio optimization at scale is not a simple linear algebra problem. The constraint sets get complicated. Position limits, sector limits, factor exposure, transaction costs, liquidity constraints. The solver has to handle all of that simultaneously and return an answer fast enough to be useful.

scipy is excellent general-purpose scientific computing. It's not built for the specific class of conic problems that show up in large institutional portfolio optimization. lcso is. Written in Rust, which means the performance ceiling is high and the memory behavior is predictable.

The interesting metadata here: BlackRock manages around $10 trillion. At that scale, optimizer performance directly translates to dollars. This is not a toy research project.

---

## 5. Hudson River Trading: corral

**Repo:** [hudson-trading/corral](https://github.com/hudson-trading/corral)
**Language:** C++20

Hudson River Trading is one of the largest U.S. trading firms by volume. They're not as famous as Jane Street but their infrastructure is in the same conversation.

corral is a structured concurrency library for C++20. Structured concurrency is a specific approach to managing async code where concurrent operations are organized in a tree structure, which makes it much easier to reason about lifetimes, cancellation, and error propagation.

In HFT, concurrency is not optional. You're handling network I/O, order management, market data feeds, and risk checks simultaneously. If any of that concurrency is not managed carefully, you get either race conditions or performance bottlenecks. corral is the foundation-layer solution to that problem.

The choice of C++20 is telling too. HFT firms are not chasing language trends. They use C++ because they need the performance and the control. corral is modern C++ done by people who have no patience for abstractions that add latency.

---

## 6. Two Sigma: flint

**Repo:** [twosigma/flint](https://github.com/twosigma/flint)
**Tech:** Apache Spark

The problem flint solves: when you have two time-series and you want to join them, the timestamps never match exactly. Tick data comes from different sources, different exchanges, different clocks. If you do a naive join, you either drop most of the data or you get garbage matches.

flint adds temporal tolerance to Apache Spark time-series joins. You specify how far apart timestamps can be and still be considered a match. Designed for billions of ticks.

Two Sigma is a quantitative firm. Their entire operation is built on finding signals in data. Time-series joins are not a peripheral feature for them. This is infrastructure that runs at the core of their research pipeline. The fact that it runs on Spark means it scales horizontally.

---

## 7. D.E. Shaw: pyflyby

**Repo:** [deshaw/pyflyby](https://github.com/deshaw/pyflyby)
**Tech:** Python / IPython / Jupyter

This one looks the least impressive at first glance. Auto-import management for IPython and Jupyter. When you type a function name that isn't imported yet, pyflyby figures out where it comes from and adds the import automatically.

That's genuinely useful for researchers working in notebooks all day. But the interesting part is in the footnote: D.E. Shaw funded the development of IPython itself.

IPython is the interactive Python shell that became the foundation of Jupyter notebooks. Every data scientist, quant researcher, and ML engineer who works in notebooks is working in an environment that D.E. Shaw partially financed. They needed better interactive Python tooling for their own research, so they funded it at the field's tooling layer.

That's a different category of contribution than open-sourcing a library. That's shaping the tool that the entire field uses.

---

## The Pattern Underneath All of This

What strikes me reading through these repos is what the problems actually are.

CPU instruction tracing. Derivative pricing. Streaming data visualization. Conic optimization. Structured concurrency. Temporal joins. Import management.

None of these are "AI" in the sense people mean when they talk about AI in finance. These are precision engineering problems at the infrastructure layer. The firms doing the most sophisticated trading in the world are spending serious time on profilers, solvers, and concurrency primitives.

The algorithm is not the moat. The infrastructure that runs the algorithm reliably and fast enough is the moat.

That's the thing you see clearly when you look at what the most expensive engineering teams in the world thought was worth open-sourcing.

---

All seven repos are public on GitHub. Worth reading the README files even if you're not going to use the code. The problem statements alone are an education in what real financial engineering actually looks like.

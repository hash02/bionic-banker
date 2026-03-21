---
title: "The Anchor Problem: Why AI Needs Perspective, Not Power"
description: "AI doesn't hallucinate because it's dumb. It hallucinates because it has no anchor — no fixed reference point to drift from. Here's what that means and what I'm building to fix it."
date: "2026-03-01"
tags: ["AI · Philosophy · SYOS"]
readTime: "8 min"
category: "Tech"
featured: false
slug: "the-anchor"
---

I figured this out at 2am because I was trying to meditate and I couldn't stop thinking about hallucinations.

    
Not the fun kind. The AI kind. The thing where you ask Claude or GPT a question and it gives you an answer that sounds perfect — confident, well-structured, all the right words — and it's completely wrong. Not a little wrong. Fabricated. Made up with the conviction of someone who has never once doubted themselves.

    
And I was sitting there trying to focus on my breathing, which is the whole point of meditation — you focus on something fixed so your mind stops drifting. The breath doesn't change. It's always there. Your thoughts go crazy, but the breath is the anchor.

    
And that's when it hit me.

    
> *AI doesn't have an anchor.*

    
## The Problem Nobody's Solving Right

    
Here's what everyone in AI safety is doing: they're trying to make the models smarter. Better training data. More RLHF. Bigger context windows. Constitutional AI. Alignment through values. And all of that matters — I'm not saying it doesn't.

    
But they're solving the wrong problem.

    
They're trying to make the mind better. Nobody's giving it a breath.

    
Think about it. When you meditate, you don't fix your thoughts. You don't fight them. You don't try to make your mind "stop hallucinating" random nonsense. You just... return to the breath. The anchor. The fixed point. And over time, the drift gets shorter. Not because your mind got smarter — because you have something real to come back to.

    
AI has no breath. Every response it generates is a thought with no fixed point to check against. It can think as hard as it wants, as fast as it wants, and it still has no way to know if it drifted — because there's nothing to drift FROM.

    
That's the Anchor Problem.

    
  
    </iframe>
    
      With vs without an anchor — accuracy, hallucination, and drift compared
      Interactive
    
  

    
## Hallucination Isn't a Bug — It's What Thinking Looks Like Without an Anchor

    
This took me a year to figure out. I spent 12 months building a system called SYOS — a framework for testing whether AI responses stay consistent or drift over time. The technical details don't matter for this piece. What matters is what I learned.

    
> *Hallucination isn't a failure of intelligence. It's what intelligence looks like when it has no fixed reference point.*

    
You know what else hallucination looks like? Dreams. Your brain, running without sensory input, generating vivid experiences that feel completely real while they're happening. You only know they were dreams because you wake up — because reality is the anchor. Remove the anchor, and the dream IS reality. There's no difference.

    
That's where AI lives right now. Stuck in the dream. No way to wake up. No way to check if what it just said is real or if it just... sounded right.

    
And here's what gets me — the whole industry is focused on making the dream better. More parameters. More training data. More compute. Like, cool, you made a more detailed dream. It's still a dream though. Nobody's building the thing that wakes it up.

    
We keep scaling the intelligence without giving it something real to hold onto. That's the gap.

    
## What an Anchor Actually Looks Like

    
So I built one. Not perfectly — I've tested it pretty hard and it's maybe 70% there. But the concept works, and the concept is what matters.

    
In SYOS, the anchor is a capsule — a small, fixed document that says "this is what's true." Not true about the world. True about THIS SYSTEM. What it is. What it does. What it doesn't do. Where its boundaries are.

    
Every time the AI generates a response, you can measure how far that response drifted from the capsule. Did it invent new capabilities? Did it forget existing ones? Did it subtly change the definition of something? That's drift. Measurable, trackable, reducible.

    
I tested it. 50 different ways of asking the same question, measuring whether the answers stayed consistent.

    #### Semantic Anchoring

        
Meaning stays consistent across 50 trials, even when vocabulary drifts.

      
      #### Metamorphic Consistency

        
Rephrased questions produce structurally equivalent answers.

      
      #### Adversarial Resistance

        
Active attempts to break the capsule — identity attacks, override prompts.

      
      #### Surface-Meaning Correlation

        
Vocabulary changes constantly. Meaning barely moves. Almost zero correlation.

      
    

    
Not perfect. But real. And measurable.

    
> **Key Finding:** The vocabulary can drift while the meaning stays stable. The AI uses different words every time — that's a 0.67 drift if you measure word overlap. But the actual meaning stays anchored. The surface changes constantly. The core holds. Just like your thoughts during meditation — they wander everywhere, but the breath stays.

    
## The Human Is the Real Anchor

    
But here's the part I can't automate, and this is the uncomfortable conclusion.

    
The capsule works. The system works. The measurements work. But the capsule itself — who decides what goes in it? Who decides what "true" means for this system? Who catches the drift that the metrics miss?

    
A human. Me. The person who built it and keeps checking it.

    
I call this the Seeker Lock. The system can audit itself, test itself, measure itself. But it cannot modify its own anchor. Only the human can do that. Because the moment the system can redefine its own ground truth, the anchor isn't fixed anymore — and you're back to dreaming.

    
> *A system can't check itself against itself. You need something outside of it. Something it didn't build and can't change.*

    
The human isn't in the loop because we're scared of AI. The human is in the loop because measurement requires a fixed point that's outside the thing being measured. That's not a limitation. That's physics.

    
## Why This Matters If You're Not Building AI

    
I work in finance. Every day I watch systems try to validate themselves. A bank's risk model, checked by the bank's own auditors, reviewed by the bank's own board. A trading algorithm, backtested against data chosen by the people who built it. Sound familiar? It's the same problem. No external anchor.

    
And honestly, it's the same thing in your own head. Your brain generates thoughts and then evaluates those thoughts with... the same brain. That's why meditation hit me so hard that night — the breath isn't a thought. It's something real. Something your mind didn't make up. That's the whole trick.

    
More compute doesn't fix this. More training doesn't fix this. What fixes it is an anchor — something outside the system that stays still so you can tell when you've moved. That's what the breath is in meditation. That's what the capsule is in SYOS. A reference point the system didn't build and can't change.

    
That's the Anchor Problem. And as far as I can tell, nobody building these systems is solving for it.

    
I'm trying.

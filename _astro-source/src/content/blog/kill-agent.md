---
title: "The Kill Agent: Why I Built an AI That Attacks Itself Every Hour"
description: "20% survival rate. Documented honestly. I built a dedicated kill agent that stress-tests my entire AI system every hour — and the failures are the whole point."
date: "2026-03-13"
tags: ["AI Agents", "Security"]
readTime: "9 min"
category: "Tech"
featured: false
slug: "kill-agent"
---

A dedicated AI agent that stress-tests an entire multi-agent system every hour. 20% survival rate, documented honestly. The failures are the point: an AI system cannot reliably evaluate its own health using its own assumptions.

Okay so here is the thing nobody talks about when building AI agent systems. The system is always lying to you about how healthy it is.

      
Not intentionally. Not maliciously. But if you build a system and then ask that same system if it's working correctly, you're going to get a yes. Always. Because the system can only evaluate itself using its own broken assumptions. It's like asking someone who's having a psychotic episode if they're thinking clearly. The answer is always "of course I am."

      
I hit this wall about a week ago. I've got a multi-agent system running—monitoring DeFi protocols, scanning for money laundering patterns, tracking portfolio movements, scouting content, deploying my website, and coordinating the whole operation. Everything was reporting green. Every health check passed. The coordinator said all agents were fresh and active.

      
And I had this moment where I thought—how do I actually know that's true?

      
## The Oracle Problem

      
There's a concept I call the Oracle Problem (borrowed from blockchain, but it applies everywhere): if the system generates data AND validates that same data, the validation is worthless. You're clapping for yourself. The audience is you. The judge is you. The score is whatever you want it to be.

      
Think about it in terms of traditional software monitoring. You set up Prometheus to track your services. Prometheus says everything is fine. But what if the network path between Prometheus and your service is what's broken? Prometheus doesn't know what it can't see. It reports health because it can't detect its own blindness.

      
Every monitoring system has this flaw. And with AI agents, it's worse—because agents can generate plausible-sounding status reports even when their underlying data is stale, their reasoning is circular, or their outputs haven't been independently verified.

      
So I did something that felt a little unhinged at the time: I built an agent whose entire job is to try to kill the other agents.

      
## Meet the Kill Agent

      
The kill agent runs on a schedule. It has rotating attack modules that cycle through the week—input validation testing, authentication probing, memory integrity checks, health staleness injection, process auditing, data credibility testing—the full menu of ways a system can be broken.

      
Each attack is designed to test one specific assumption the system makes about itself. One module sends deliberately malformed payloads to see if the API validates input correctly. Another checks if authentication has been quietly weakened. Another injects wrong data into context files and checks if the next session catches the discrepancy.

      
The concept borrows from every tradition that understood the same thing: what survives when everything else is stripped away? Not stability—adaptability. Not uptime—recovery speed.

      
        
        </iframe>
        
INTERACTIVE The three-agent triad: one designs, one builds, one proves — or disproves

The three-agent triad is the pattern the kill agent fits into. One agent generates output. One agent processes that output. The kill agent verifies the processing was correct. Independent verification is the whole design. Without the third agent, the first two are evaluating themselves.

## What the Kill Agent Actually Does

The kill agent does not try to break infrastructure. It tests assumptions.

Every agent in the system makes assumptions about the data it receives: that the JSON is valid, that the wallet address is in the right format, that the timestamp is recent, that the health status it is reading is current. The kill agent systematically violates those assumptions and checks whether the system catches the violation or silently accepts bad data.

A malformed wallet address test sends a string that looks like an address but is twelve characters too short. Does the validation layer catch it? A staleness injection test writes an old timestamp into a health file and then triggers a health check. Does the system flag the stale data or report everything as green?

The results across the first two weeks of running the kill agent were uncomfortable.

20 percent survival rate. That means 80 percent of the attack scenarios found something the system did not catch.

Not all of those were critical. Some were formatting edge cases that would never appear in real data. Some were authentication boundary cases that the actual usage pattern would never hit. But some were real. One attack module found that the coordinator was accepting health status reports from processes that had already exited. The process was gone but the status file was still showing active. The coordinator was reporting a clean system from ghost data.

That would have been invisible without an independent attacker.

## Why 20 Percent Survival Is the Right Number

When I first saw the results I felt like I had failed. 80 percent of attacks finding something sounds like a broken system.

It is not. It is a calibrated system.

A system that survives 100 percent of attack scenarios is a system where the attacks are too weak. You are testing easy cases that your production safeguards already catch. The attack suite is theater.

A system that survives 20 percent of attack scenarios has discovered where its actual vulnerability surface is. Now you know what to harden. Now you know what the real error paths look like, and you can build recovery procedures around them instead of around hypothetical failures.

The kill agent is not supposed to fail to find things. It is supposed to find the things the regular monitoring misses. That is its whole job.

## What Changed After Running It

Several things got rebuilt after the first two weeks.

The health status format got a required timestamp field and a staleness threshold. If the most recent entry is more than ten minutes old, the coordinator flags the agent as unresponsive rather than active. Ghost status reports no longer count.

The wallet address validation got stricter. Address format checks now happen at the input boundary, not inside the processing function. Malformed addresses get rejected before they touch any downstream logic.

The JSON parsing across all agents got wrapped in explicit validation against a schema rather than trusting whatever came in. If the schema does not match, the message goes to an error queue rather than getting processed.

None of those changes were on any roadmap. They came directly from what the kill agent found.

## The Deeper Point

Building the kill agent changed how I think about system design generally.

If I build something, I am the worst person to evaluate whether it works. I know what I intended. I know what cases I tested. I am blind to the cases I did not think of.

An independent attacker does not have my assumptions. It probes the edges I did not consider because it does not know what I considered. It finds the gaps not by being smarter but by approaching the system without the biases I built in.

That is why the kill agent runs on a schedule rather than on demand. On demand, I would run it when I suspected a problem. Scheduled, it runs whether I suspect a problem or not. Most of the useful things it finds are in the sessions where I thought everything was fine.

The system is always lying to you about how healthy it is. The kill agent is how you catch the lie before production does.

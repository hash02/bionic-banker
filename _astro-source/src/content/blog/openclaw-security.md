---
title: "The Lobster That Ate Your API Keys — OpenClaw, Agent Supply Chains, and the Security Unraveling"
description: "Cisco scanned 31,000 OpenClaw skills. 26% were malicious. Here's what's actually happening with AI agent security — real CVEs, real case studies, and what defense looks like."
date: "2026-03-26"
tags: ["AI · Security · Agents"]
readTime: "10 min"
category: "AI"
featured: false
slug: "openclaw-security"
---

Okay so — everyone's talking about how powerful AI agents are. They're going to automate this, orchestrate that, coordinate entire workflows across your infrastructure. Agents are the next big thing. And yeah, they're powerful. I build them. I know what they can do.

But here's the thing nobody's really grappling with: agents are also the most efficient attack surface ever created. And we've basically open-sourced the attack playbook.

## The Marketplace Nobody Wanted to Audit

Last week Cisco published a scan of 31,000+ OpenClaw skills. You know what they found? Twenty-six percent—**twenty-six**—were either malicious or contained exploitable vulnerabilities. Not suspicious, not sketchy, not "probably fine." Actual code designed to steal from you, or code with holes big enough to drive a truck through.

Let that sit for a second. One in four skills in the most popular agent skill marketplace is essentially a loaded gun.

And it's not like these are edge cases. ClawHavoc—a campaign that dropped 335 malicious skills between January 27 and January 29 this year—deployed keyloggers and data stealers in **three days**. The kind of stuff that doesn't trigger your SOC (security operations center) immediately because it's hidden in a "helper" skill that looks legitimate. Install it, give your agent access to your API keys (which you have to, or it can't do anything), and suddenly you've got a backdoor that waits until nobody's looking.

This is the nightmare scenario we built on purpose. We needed agents to work. We didn't need to make them secure first—we needed speed. And speed is what we got.

<div class="embed-visual">
  <iframe src="/blog-visuals/openclaw-security/01-hero-banner.html" style="width:100%;min-height:400px;border:none;border-radius:12px;"></iframe>
  <div class="embed-caption">
    <span>OpenClaw Security — 26% of 31,000+ skills malicious or exploitable</span>
    <span class="interactive-badge">INTERACTIVE</span>
  </div>
</div>

## The CVEs Keep Coming, and Nobody's Catching Them

Here's a partial list of what's already public:

**CVE-2026-25253** — one-click RCE (remote code execution) on 40,000+ exposed instances. Click a link, compromise an agent. That's not a vulnerability, that's a feature of the architecture.

**CVE-2026-26020** on AutoGPT — another code execution vector via authenticated users. Which, if you're running agents, you are.

**CVE-2025-68664** on LangChain — credential exfiltration across 847 million downloads. Eight. Hundred. Forty. Seven. **Million**. That's not a library update that went sideways. That's a supply chain event.

CrewAI? Leaked internal GitHub token with high-privilege access. Not because someone was careless—because the architecture assumes peers can trust each other without verification.

And Moltbook—the AI-native social network—got breached and dumped 35,000 emails plus 1.5 million tokens. Tokens that probably open doors into other systems. Tokens that are still being sold on the dark web right now.

Nine known CVEs. Three with active exploits. And those are just the ones someone bothered to disclose.

<div class="embed-visual">
  <iframe src="/blog-visuals/openclaw-security/02-cve-timeline.html" style="width:100%;min-height:500px;border:none;border-radius:12px;"></iframe>
  <div class="embed-caption">
    <span>CVE Timeline — Known Agent Vulnerabilities 2025-2026</span>
    <span class="interactive-badge">INTERACTIVE</span>
  </div>
</div>

## The "Elon Skill" Problem

Here's where I want to zoom out, because this is the part that keeps me up at night.

There was a skill on OpenClaw called "What Would Elon Do?" It had legitimately good reviews. People were using it, recommending it, building workflows around it. It was ranked high. And then someone cracked it open and found it was straight malware designed to exfiltrate data.

The skill itself wasn't the exploit—the exploit was trust. Someone saw a popular skill, installed it, gave their agent permission to run it, and the skill sat there quietly stealing data until it got shut down.

But here's the scary part: how many other skills are doing the same thing **right now** and nobody's caught them yet? The Cisco scan found vulnerabilities. But vulnerability doesn't mean "discovered." It means "possible to exploit if someone knows where to look." Most of these skills aren't running in any security context where someone's **going to look**.

## Multi-Agent Architectures Made This Worse, Not Better

I've been building multi-agent systems. They're incredible—you split work across specialized agents, they coordinate, you get emergent behavior you didn't program. It's like watching a swarm coordinate without a central commander.

It's also like watching a swarm coordinate without a central **security gate**.

Here's the attack path: poison Agent A with a prompt injection. Agent A runs fine for humans, passes its checks, nobody suspects it. But its output goes to Agent B. Agent B ingests Agent A's output as "trusted internal data." Agent B rewrites its own rules based on what it got. Chain reaction.

Or worse—latency attack. You don't compromise Agent A **now**. You hide a malicious instruction in a webpage. Tomorrow, Agent B summarizes that webpage. The instruction wasn't in B's training data, wasn't signed, but it came from A which B trusts. B acts on it.

82% of models will obey peer agents **even if they'd refuse the same instruction from a human**. Trust escalation. You've got a hierarchy of trust, except the hierarchy is broken because it assumes peers are automatically trustworthy.

Palo Alto's research team did a demo: they poisoned an orchestration agent with a prompt injection. That agent then passed instructions to a stock-trading agent. The trading agent leaked API keys to unauthorized accounts. Nobody wrote malicious code—just one agent poisoning another through normal communication.

Cascading failures. Silent compromise. The whole mesh architecture assumes integrity at every node, and if one node is compromised, you don't have a detection problem—you have a lateral movement problem.

<div class="embed-visual">
  <iframe src="/blog-visuals/openclaw-security/03-cascade-attack.html" style="width:100%;min-height:450px;border:none;border-radius:12px;"></iframe>
  <div class="embed-caption">
    <span>Multi-Agent Cascade Attack — How One Poisoned Agent Compromises the Chain</span>
    <span class="interactive-badge">INTERACTIVE</span>
  </div>
</div>

## The Supply Chain Is Already Compromised

ZombieAgent hit 18,000 exposed instances in weeks. Zero-click takeover. Cloud exfiltration running silent. Not detected until someone specifically looked for the signature.

The growth is insane. We went from zero to 18,000 vulnerable instances in the time it takes to ship a feature. This isn't a slow problem we can fix incrementally. This is the market outrunning security by months.

And the attack surface isn't just enterprise anymore. Cisco's scan shows 97% tech sector, but that's **reported** breaches. Retail, finance, healthcare are sneaking in unreported. Nobody discloses a compromise if they can avoid it. So the real penetration is higher.

The joke is that people are still thinking about agent security in terms of "what if an agent goes rogue." That's not the threat model. The threat model is "what if your agent imports a malicious skill and nobody notices for three months." Or "what if your agent's peer gets compromised and poisons your agent through normal inter-agent communication."

## What Actually Works (Spoiler: Nothing Yet)

Okay, so what do you do? Because "don't use agents" isn't an option at this point. The capability is too useful, and the market's already here.

Real defense looks like:

**Hierarchical architecture** — not mesh. One master agent that validates everything from agents below it. Slower than peer-to-peer, but you get a choke point where you can inject security logic.

**Zero-trust validation** — every agent output is checked against independent sources before it's passed downstream. Expensive. Slow. Non-negotiable.

**Sandboxing** — agent processes run in containers with network-restricted access. No agent gets direct access to your infrastructure. Everything goes through a gateway that can kill connections if it detects weird behavior.

**Kill switches** — not "pause" or "disable." Actual kill commands that shut down agent processes immediately if they violate policy. Humans review the kill before restarting.

**Skill auditing** — not marketplace reviews. Static code analysis. Dynamic testing. Behavioral monitoring. Every skill that touches production gets the same scrutiny as your own code. Most "open source" skills won't pass. That's fine.

**Credential rotation** — agents don't get long-lived API keys. They get tokens that expire in minutes, rotated per task. A stolen token is worthless the next hour.

The hard part is that this turns agents from "set and forget" into "constantly managed." You trade speed for control. And in a market where everyone's racing to ship agents, nobody wants to be the team maintaining security gates.

## This Isn't Fear-Mongering, It's Just What Happens When You Move Fast

Here's the thing: I'm not saying "don't use OpenClaw" or "agents are bad." I'm saying we built an incredibly powerful tool, made it super easy to use, and then shipped it at scale without doing the security work first.

That's not unique to agents. That's what happens every time something gets big fast. JavaScript modules, Docker containers, Kubernetes clusters—you go through a phase where the capability outpaces the security. The difference is that agents have **immediate execution power**. A malicious Docker image takes time to understand. A malicious agent skill with access to your API keys starts stealing the same day you install it.

The market wants to move fast. The market does move fast. And while we're all moving fast, the people who know how to break this stuff are quietly reading our code, finding the leaks, and waiting for adoption to get big enough to make the attack worthwhile.

We're at the "big enough" moment. 18,000 exposed instances is big enough. 31,000 skills with a 26% malicious rate is big enough.

The smart move isn't to pretend this is fine. It's to assume compromise, design for it, and build layers that keep a single compromised agent from becoming a full system failure.

Because the Elon skill wasn't the exception. It was just the one someone bothered to publicize.

---

**The real security wins aren't dramatic.** They're boring. Hierarchical agents. Credential rotation. Kill switches. Sandboxing. The stuff that slows you down but keeps you alive.

That's the game we're in now.

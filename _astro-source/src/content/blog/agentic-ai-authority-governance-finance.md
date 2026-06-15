---
title: "Agentic AI in Finance Needs Authority Governance"
description: "The FSB's AI consultation shows why financial institutions need to govern what AI agents are allowed to do, not only which tools they use."
date: "2026-06-13T18:30:00"
slug: "agentic-ai-authority-governance-finance"
tags: ["AI", "Agentic AI", "AI Governance", "Financial Stability", "Risk Management"]
readTime: "7 min"
featured: true
image: "/blog-visuals/agentic-ai-authority-governance-finance/hero.svg"
category: "AI"
---

Agentic AI in finance is not only a tool question.

It is an authority question.

That is the part many AI governance conversations still miss.

A chatbot can answer. A workflow assistant can summarize. A model can classify, draft, retrieve, or explain.

An agentic system can go further. It can plan steps, call tools, use APIs, move across systems, monitor goals, and act with limited human oversight.

That changes the control problem.

The question is no longer only:

```text
Which AI tool are we using?
```

The better question is:

```text
What is this system allowed to do, under whose authority, with what evidence, and where does it have to stop?
```

<div class="intel-block authority-ladder" aria-label="Authority governance ladder">
  <div class="intel-block-head">
    <span>Authority ladder</span>
    <strong>Not every AI action has the same control weight.</strong>
  </div>
  <div class="ladder-steps">
    <div><span>00</span><strong>Observe</strong><em>read-only context</em></div>
    <div><span>01</span><strong>Summarize</strong><em>draft / explain</em></div>
    <div><span>02</span><strong>Recommend</strong><em>human decides</em></div>
    <div><span>03</span><strong>Prioritize</strong><em>queue influence</em></div>
    <div><span>04</span><strong>Trigger review</strong><em>workflow handoff</em></div>
    <div><span>05</span><strong>Execute</strong><em>bounded internal step</em></div>
    <div class="blocked"><span>06</span><strong>External action</strong><em>human approval gate</em></div>
  </div>
</div>

## Why this matters now

On June 10, 2026, the Financial Stability Board published a consultation report on sound practices for responsible AI adoption by financial institutions.

The report proposes 12 sound practices. It is not a binding international standard. It is a consultation, with comments due July 22, 2026.

But the signal is important.

The FSB is not treating AI adoption as only a productivity issue. It is treating responsible AI adoption as connected to operational resilience, risk management, governance, third-party dependency, and financial stability.

The consultation explicitly asks whether its proposed sound practices strike the right balance between risks from all forms of AI and risks from newer, more complex forms such as generative AI and agentic AI.

That is the important phrase: agentic AI.

Once AI systems can plan and act across workflows, finance teams need a governance model for authority.

## Tool governance is not enough

Tool governance asks useful questions:

<div class="intel-block split-governance" aria-label="Tool governance versus authority governance">
  <div class="intel-block-head">
    <span>Control split</span>
    <strong>Tool governance approves the instrument. Authority governance bounds the action.</strong>
  </div>
  <div class="split-grid">
    <section>
      <h3>Tool governance</h3>
      <p>Which vendor is approved?</p>
      <p>What data can be entered?</p>
      <p>Which teams can use it?</p>
      <p>What retention policy applies?</p>
      <p>What risk tier is assigned?</p>
    </section>
    <section>
      <h3>Authority governance</h3>
      <p>What can the system decide?</p>
      <p>Which systems can it touch?</p>
      <p>What evidence must it keep?</p>
      <p>Where must a human approve?</p>
      <p>Who owns the outcome?</p>
    </section>
  </div>
</div>

Those questions still matter.

But they are not enough for agents.

An agentic workflow can connect tools together. It can transform one approved function into a chain of actions. It can call a retrieval system, summarize a record, draft a response, open a ticket, update a case, trigger a review, or recommend an escalation.

The risk is not only inside one model response.

The risk can appear in the sequence.

A single step may look harmless. The full chain may change what happens inside a control process.

That is why authority governance matters.

## What authority governance means

Authority governance means defining what an AI system is allowed to influence or do before it acts.

For finance, that includes at least seven questions.

## 1. What can the agent decide?

Some AI systems should only draft or summarize.

Some may be allowed to classify.

Some may prioritize work queues.

Some may recommend actions.

Some may execute low-risk operational steps.

Those are different authority levels.

A system that summarizes an AML alert is not the same as a system that closes an alert. A system that drafts a customer message is not the same as a system that sends it. A system that recommends a payment review is not the same as a system that releases a payment.

The control design should reflect the difference.

## 2. What systems can it touch?

Agentic AI becomes riskier when it can move across systems.

A finance agent may touch:

- customer records
- transaction histories
- case-management systems
- sanctions or screening tools
- payment operations
- document repositories
- CRM notes
- internal policies
- ticketing systems
- code repositories
- vendor platforms

The map matters.

If the agent can read, write, update, submit, or trigger actions in those systems, governance must follow the permission boundary.

## 3. What evidence must it keep?

Finance cannot run on invisible reasoning.

If an AI system influences a risk decision, the institution needs records.

Not just the final answer.

The useful record includes:

<div class="intel-block workflow-chain" aria-label="Finance AI audit record chain">
  <div class="intel-block-head">
    <span>Evidence chain</span>
    <strong>A finance AI output is only useful when the review trail survives it.</strong>
  </div>
  <ol>
    <li><span>01</span><strong>Input data</strong><em>customer, transaction, case, document</em></li>
    <li><span>02</span><strong>Source retrieval</strong><em>policy, prior notes, public record</em></li>
    <li><span>03</span><strong>Model / vendor</strong><em>system used and instruction class</em></li>
    <li><span>04</span><strong>Tools called</strong><em>read, draft, search, classify, update</em></li>
    <li><span>05</span><strong>Output generated</strong><em>summary, risk note, recommendation</em></li>
    <li><span>06</span><strong>Human review</strong><em>approval, rejection, override</em></li>
    <li><span>07</span><strong>Outcome record</strong><em>timestamp, escalation path, final action</em></li>
  </ol>
</div>

Without that trail, the system may be fast but not reviewable.

## 4. When must a human intervene?

“Human in the loop” is too vague.

The real control question is:

```text
Which exact action requires human approval?
```

A useful design separates:

- human awareness
- human review
- human approval
- human override
- human accountability

Those are not the same.

A reviewer seeing an AI output after the fact is not the same as approving an action before it happens.

## 5. What happens when the agent is uncertain?

Uncertainty cannot be hidden inside confident language.

An agentic finance workflow needs pause conditions:

- missing source record
- conflicting documents
- low confidence
- unusual customer impact
- regulatory-sensitive action
- payment or account restriction
- sanctions or AML escalation
- material operational exception
- vendor or model failure

A good agent does not only act.

It knows when to stop.

## 6. Who owns the outcome?

Responsibility cannot be assigned to the model.

A financial institution needs an accountable owner for each AI-enabled workflow.

That owner may sit in operations, compliance, risk, technology, product, legal, or a business line.

But someone must own the control boundary.

If an AI system causes a bad customer outcome, creates a weak audit trail, misses a risk signal, or triggers an inappropriate action, the institution cannot say: the model did it.

Governance has to name the human and organizational owner before the system runs.

## 7. What changes as the agent learns or the vendor updates?

Hosted AI systems can change.

Vendors update models. Retrieval indexes change. Prompts evolve. Tools are added. APIs are modified. Internal data sources grow.

That means a control that worked last quarter may not work next quarter.

Agentic AI governance needs change management:

- model/version tracking
- tool-permission review
- regression testing
- output monitoring
- incident review
- periodic access review
- vendor-change notification
- fallback process

The system is not a one-time approval.

It is a living control surface.

## The financial stability angle

The FSB’s consultation matters because the issue is not limited to one institution.

If many financial institutions adopt similar AI systems, rely on the same vendors, use the same cloud infrastructure, connect to similar data sources, and automate similar workflows, risk can become correlated.

That can affect:

- operational resilience
- cyber exposure
- market behavior
- fraud response
- vendor concentration
- model dependency
- incident propagation
- customer protection

Agentic AI makes that more important because action can happen faster than traditional review cycles.

The risk is not that every AI agent becomes dangerous.

The risk is that institutions deploy agents faster than they define authority.

## What financial institutions should build

The next governance layer should look less like a policy memo and more like an operating system for controlled autonomy.

It should include:

- an inventory of AI-enabled workflows
- authority levels for each workflow
- approved tool and data boundaries
- human-approval points
- evidence and logging standards
- vendor and model dependency records
- incident and fallback procedures
- periodic review of agent permissions
- board and senior-management reporting

The institution should be able to answer a simple question:

```text
Show me what this AI system can do without asking a human.
```

If that answer is unclear, the agent is not governed yet.

## The practical takeaway

Agentic AI will not be governed well by tool lists alone.

Finance needs authority maps.

Who can act?
What can be touched?
What can be changed?
What must be logged?
What needs approval?
What forces a pause?
Who owns the outcome?

That is the real shift.

AI governance is moving from tool approval to authority design.

The institutions that understand that early will be able to use agents more safely, more clearly, and with less improvisation when regulators, auditors, customers, or boards ask how the system works.

## Sources

- [Financial Stability Board: Sound Practices for Responsible Adoption of Artificial Intelligence — Consultation Report](https://www.fsb.org/2026/06/sound-practices-for-responsible-adoption-of-artificial-intelligence-ai-consultation-report/)
- [FSB consultation PDF: Sound Practices for Responsible Adoption of Artificial Intelligence](https://www.fsb.org/uploads/P100626.pdf)

This article is educational analysis. It is not legal advice, regulatory advice, compliance approval, investment advice, or a recommendation to deploy any specific AI system.

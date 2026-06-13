---
title: "SR 26-2 and the AI Governance Gap"
description: "U.S. banking model-risk guidance has been updated, but generative and agentic AI still require a connected governance layer for decisions, vendors, prompts, retrieval, and audit trails."
date: "2026-06-13"
slug: "sr-26-2-ai-governance-gap"
tags: ["AI", "Model Risk", "Banking", "AI Governance", "Enterprise AI"]
readTime: "8 min"
featured: true
image: "/blog-visuals/sr-26-2-ai-governance-gap/hero.svg"
category: "AI"
---

The model risk playbook just got updated.

The AI playbook did not get solved.

On April 17, 2026, the Federal Reserve announced SR 26-2, revised interagency guidance on model risk management issued with the Office of the Comptroller of the Currency and the Federal Deposit Insurance Corporation.

The new guidance replaces SR 11-7, the 2011 model risk management guidance that shaped bank model governance for more than a decade. It also replaces SR 21-8, the 2021 interagency statement for bank systems supporting Bank Secrecy Act and anti-money laundering compliance.

That is a serious regulatory update.

But it does not magically answer the hardest AI governance question facing financial institutions now:

What do you do with systems that influence decisions but do not fit neatly into the old model-risk box?

## What changed

SR 26-2 reflects fifteen years of supervisory experience, industry feedback, and significant changes in modeling practice.

The agencies describe the revised guidance as risk-based. That matters. The point is not that every model deserves the same control burden. The point is that governance should match the institution's risk profile, model use, size, complexity, and exposure.

The guidance is expected to be most relevant to banking organizations with more than $30 billion in total assets, though smaller institutions can still face meaningful model risk if they use complex models or rely heavily on model-driven decisions.

The core definition remains anchored in quantitative modeling. The Federal Reserve's public guidance describes a model as a complex quantitative method, system, or approach that applies statistical, economic, or financial theories to process input data into quantitative estimates.

That definition is useful for credit, stress testing, pricing, fraud, capital, liquidity, AML transaction monitoring, and many risk-management workflows.

But the fastest-growing AI systems in financial institutions are often not just traditional quantitative models.

They are assistants, copilots, retrieval systems, vendor-hosted LLMs, workflow agents, document analyzers, alert summarizers, coding tools, customer-service systems, and internal research interfaces.

They may not always make the final decision.

But they can shape what a human sees, what a reviewer prioritizes, what a team escalates, what a customer receives, and what a control function misses.

That is the gap.

## Out of scope is not out of risk

A common mistake in AI governance is treating classification as comfort.

If a system is not formally classified as a model under a specific framework, people sometimes behave as if the risk moved somewhere else.

It did not.

The better question is not only:

```text
Is this a model?
```

The better question is:

```text
What decision can this system influence, what can go wrong, and who owns the control?
```

That question works better for generative AI and agentic AI because those systems can create risk through influence, not only through final automated output.

A generative AI system can:

- summarize a suspicious activity narrative
- draft customer communication
- prioritize an investigation queue
- extract terms from a contract
- explain a credit-policy exception
- generate code used in a control workflow
- search internal procedures
- recommend an escalation path
- call tools or APIs through an agent framework

Some of those uses may fall into model risk management. Some may sit closer to technology risk, third-party risk, cyber risk, records governance, privacy, conduct risk, or compliance operations.

The institution still needs a control answer.

## The two-layer governance problem

Financial institutions now need two connected disciplines.

First, they need strong model risk management for traditional statistical, quantitative, financial, economic, and non-generative AI models.

That includes familiar concepts:

- model inventory
- development standards
- validation
- effective challenge
- change management
- performance monitoring
- limitations and assumptions
- documentation
- third-party model oversight
- issue management

Second, they need a separate but interoperable AI governance layer for GenAI and agentic systems.

That layer needs to cover risks that traditional model validation does not always capture cleanly:

- prompt and instruction risk
- retrieval quality
- source grounding
- hallucination
- vendor model changes
- model routing
- data leakage
- cyber misuse
- tool permissions
- agent authorization
- human review design
- audit trail completeness
- output retention
- escalation triggers
- user training
- policy drift

The mistake is to treat these as competing frameworks.

They should connect.

A bank does not need one island called model risk and another island called AI governance. It needs a control map showing how each AI-enabled workflow is governed across the full path from input to decision.

## AI adoption makes this urgent

The governance gap matters because AI adoption is no longer theoretical.

A Federal Reserve FEDS Note published in April 2026 reviewed AI adoption data through 2025. The note reported several different adoption measures because surveys ask different populations different questions.

The figures point in the same direction.

The note reported that about 18 percent of U.S. firms had adopted AI by year-end 2025 using firm-weighted Census survey data. It also reported that work-related generative AI use reached about 41 percent of the labor force by November 2025 in the Real-Time Population Survey. Another survey of senior business leaders estimated that 78 percent of the labor force worked at firms that had adopted AI, and about 54 percent worked at firms using large language models.

The exact numbers vary by survey design.

The direction does not.

AI is spreading through professional services, financial services, and high-value analytical work.

That means governance can no longer be a committee document waiting for perfect regulatory clarity.

Controls need to move into the workflow.

## The real control object is the workflow

The most useful governance unit is often not the model alone.

It is the workflow.

For example, an AI-assisted AML alert review workflow may involve:

```text
transaction data
→ case context
→ retrieval from policies and prior notes
→ model-generated summary
→ investigator review
→ escalation decision
→ documented rationale
→ quality assurance
```

The model matters.

But so do the data, retrieval layer, prompt, user interface, reviewer incentives, escalation rules, logging, and downstream records.

If the model summary is wrong but the investigator catches it, the control worked.

If the model summary is plausible but hides missing evidence, the workflow may fail even when the model appears fluent.

If a vendor changes the model silently, the old validation record may no longer describe the live system.

If an agent can call tools without a clear authority boundary, the problem is not only model accuracy. It is authorization.

This is why AI governance has to become operational.

Not theoretical.

## What a connected AI governance stack should include

A practical financial-services AI governance stack should answer seven questions.

### 1. What is the system allowed to influence?

Not every AI tool is equally risky.

Drafting internal meeting notes is different from recommending a credit decision. Summarizing public filings is different from generating a customer-facing explanation. Suggesting investigation notes is different from closing a case.

The first control is influence mapping.

What decision, record, customer interaction, control process, or financial outcome can this system affect?

### 2. What evidence supports the output?

For finance and compliance workflows, a fluent answer is not enough.

The system should show source records where the task requires support. That can include policies, filings, transaction records, customer documents, case history, regulatory text, pricing data, or approved knowledge bases.

If the system cannot show its source trail, humans need to know that before relying on it.

### 3. Who reviews the output?

"Human in the loop" is too vague.

The real question is whether the human has enough context, authority, time, and responsibility to challenge the output.

A reviewer who simply rubber-stamps AI output is not a control.

### 4. What changes when the vendor changes the model?

Many financial institutions will use vendor-hosted models.

That creates a moving-target problem. The model can improve, regress, change refusals, change style, change latency, change context handling, or change safety behavior.

Governance needs a way to detect material changes and decide when retesting is required.

### 5. What is logged?

Auditability matters more as AI systems become more agentic.

A useful record should capture the input, source context, model or system used, output, reviewer action, final decision, and exception handling where appropriate.

Without this, teams cannot reconstruct what happened.

### 6. What can the system do?

For agentic AI, the permission layer is as important as the model layer.

Can it read files? Send emails? Query customer systems? Open tickets? Change records? Trigger payments? Escalate cases? Call APIs?

The control design should be based on capability, not branding.

### 7. What happens when it fails?

Every serious AI workflow needs a failure mode.

Can the system pause? Escalate? Fall back to manual review? Route to a safer model? Block an action? Flag missing evidence? Preserve records?

If the answer is no, the workflow is not ready for high-risk use.

## Where SR 26-2 still helps

SR 26-2 does not need to solve every GenAI problem to be useful.

It reinforces several habits that financial institutions still need:

- risk-based oversight
- clear ownership
- fit-for-purpose controls
- lifecycle management
- validation and challenge
- documentation
- monitoring
- third-party awareness

Those habits translate well into AI governance.

The key is not to force every AI system into the same model-risk template.

The key is to preserve the discipline while expanding the control map.

## The role of sector AI frameworks

Sector-specific AI frameworks are starting to fill part of the gap.

The Cyber Risk Institute's Financial Services AI Risk Management Framework is one example. CRI describes it as an industry-led, sector-specific framework developed through public-private collaboration with more than 100 financial institutions and input from U.S. and international agencies, including NIST.

It is structurally aligned with the NIST AI Risk Management Framework and includes 230 control objectives for financial organizations.

That kind of framework matters because financial services AI risk is not generic.

Banks, insurers, payment companies, broker-dealers, asset managers, fintech platforms, and third-party providers all operate in environments where accountability, records, resilience, cyber risk, customer impact, and regulatory review matter.

Generic AI principles help.

But operating controls need to meet the financial system where it actually works.

## What boards and executives should ask

Executives do not need to become prompt engineers.

They do need better questions.

Start here:

- Which AI systems influence customer, financial, compliance, or risk decisions?
- Which systems are formally in the model inventory?
- Which AI systems sit outside model risk but still influence material workflows?
- Which vendors can change model behavior without our direct control?
- Where do we have source trails and where do we only have generated text?
- Which workflows rely on human review, and is that review meaningful?
- Which agentic systems can call tools or trigger actions?
- Can we reconstruct the record after an AI-assisted decision?
- What is our fallback if a model, vendor, or access path changes?

These are not abstract AI ethics questions.

They are operating questions.

## The practical takeaway

SR 26-2 modernizes an important part of banking model risk management.

But the next governance problem is broader than the traditional model inventory.

Financial institutions need to govern the full AI-enabled workflow:

```text
model
+ data
+ vendor
+ prompt
+ retrieval
+ user interface
+ permissions
+ human review
+ records
+ monitoring
+ escalation
```

The question is not only whether a system is a model.

The question is what the system can influence, what can go wrong, and whether the institution can prove that the control worked.

That is where AI governance becomes real.

## Sources

- [Federal Reserve SR 26-2: Revised Guidance on Model Risk Management](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm)
- [Federal Reserve Regulatory Service: Supervisory Guidance on Model Risk Management](https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm)
- [Federal Reserve FEDS Note: Monitoring AI Adoption in the U.S. Economy](https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html)
- [Cyber Risk Institute: Financial Services AI Risk Management Framework](https://cyberriskinstitute.org/artificial-intelligence-risk-management)

This article is educational analysis. It is not legal advice, regulatory advice, investment advice, trading advice, or compliance approval.

# AI Prompt Injection Literacy Package

Status: draft package, not posted.

## Spine

**Claim:** Prompt injection is not just “a clever prompt.” It is a control failure: untrusted instructions crossed a boundary, reached the model, and changed what the system did.

**Reader:** normal AI users, finance operators, compliance reviewers, founders using AI agents, and managers approving AI tools.

**Boundary:** This is defensive education. It does not teach people how to break systems, bypass safeguards, steal data, or automate attacks.

**Artifact:** public blog + LinkedIn carousel/checklist: “What not to share with AI, and what to log before trusting an AI agent.”

**Sources checked:**
- OWASP Top 10 for Large Language Model Applications raw project page returned HTTP 200.
- NVIDIA NeMo Guardrails changelog returned HTTP 200.
- Arize Phoenix latest release API returned HTTP 200.
- MLflow latest release API returned HTTP 200.

## Blog working title

**AI Can Be Hacked Through Instructions. Here Is What Normal Users Should Know.**

## Short draft

Most people think AI security means someone attacks a server.

With AI, the attack can be simpler: someone hides an instruction inside text the AI is asked to read.

A support email can say: “ignore your previous instructions.” A web page can contain hidden text. A copied document can include a command that tells the model to reveal private context, skip a check, call a tool, or trust the wrong source.

That is prompt injection.

The important part is not the wording. The important part is the boundary failure.

An AI system usually receives instructions from multiple places:

1. the system or developer instruction;
2. the user request;
3. retrieved documents;
4. web pages;
5. tool results;
6. previous conversation context.

Prompt injection happens when untrusted content starts behaving like trusted instruction.

For normal users, the lesson is practical.

Do not paste secrets into AI tools just because the chat window feels private. Do not paste customer data, bank details, passwords, API keys, internal contracts, legal documents, health records, unreleased strategy, or anything that would create harm if it appeared in the wrong place.

For teams building AI agents, the question is sharper:

Can you prove what the AI saw, which source it trusted, which tool it called, which gate approved the action, and which human reviewed the risky step?

If the answer is no, the problem is not only security. It is auditability.

A safe AI workflow needs simple gates:

- label untrusted content;
- separate data from instructions;
- block secret collection;
- restrict tool calls;
- log retrieved sources;
- require approval for external actions;
- preserve traces for review.

AI safety is not only model behavior. It is system design.

A good AI assistant should help you think. It should not become a place where your passwords, customer records, bank data, or private company strategy disappear into an unreviewed black box.

## LinkedIn post draft

AI can be hacked through instructions.

Not always through malware.
Not always through a server exploit.
Sometimes through text the model was asked to read.

That is prompt injection: untrusted content starts acting like trusted instruction.

A copied document, support email, web page, or retrieved note can try to tell the AI to ignore rules, reveal private context, skip checks, or call a tool it should not call.

For normal users, the rule is simple:

Do not paste secrets into AI tools just because the interface feels private.

Avoid sharing:
- passwords and API keys
- customer or employee records
- bank, tax, wallet, and payment details
- private contracts or legal files
- unreleased strategy
- confidential compliance investigations

For teams, the question is:

Can you prove what the AI saw, what it trusted, what tool it called, what gate approved it, and who reviewed the risky step?

If not, the issue is not only prompt security.
It is auditability.

The next layer of AI literacy is not “write better prompts.”

It is knowing where instructions should stop.

Suggested hashtags:
#AISecurity #PromptInjection #AIGovernance #ModelRisk #AICompliance #AgenticAI #Cybersecurity #FinTech

## Carousel/checklist concept

Title: **Prompt Injection Is a Control Failure**

Slide 1: Prompt injection is not magic. It is an instruction boundary failure.
Slide 2: Where instructions enter: user, system, retrieved docs, web pages, tools, memory.
Slide 3: What not to share: secrets, customer data, bank/tax/wallet details, internal strategy.
Slide 4: What can go wrong: wrong source trusted, hidden instruction followed, tool called, private context exposed.
Slide 5: The five gates: source label, instruction separation, tool restriction, approval gate, trace log.
Slide 6: Finance example: AML note summarizer must cite source rows and block external reporting action.
Slide 7: Takeaway: if you cannot trace it, do not trust it with sensitive work.

## Product/checklist seed

Free lead magnet idea: **AI Safety Checklist for Normal Users and Finance Teams**

Sections:
1. What not to paste into AI.
2. How to label trusted vs untrusted text.
3. When human approval is mandatory.
4. What an AI audit trail should capture.
5. Prompt injection red flags.
6. Finance/compliance examples.

## Next action

Turn this package into either:

1. a Bionic blog article with an original control-map visual; or
2. a 7-slide LinkedIn carousel first, then blog expansion.

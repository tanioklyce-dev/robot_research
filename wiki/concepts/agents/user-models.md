---
title: User models (a world model of a person)
type: concept
created: 2026-09-02
updated: 2026-09-02
sources: 1
tags: [user-models, gum, next-action-prediction, proactive-ai, grounding, mixed-initiative, hci, privacy, contextual-integrity, world-model]
---

**A user model** is a persistent, updatable representation of a *person* — their goals, preferences, knowledge and habits — inferred from observed behavior and used to predict what they will do or need next. [Diyi Yang](../../entities/diyi-yang.md)'s framing, and the reason this page sits in a robotics wiki:

> **"A user model is actually a world model of a person."**

Same decomposition as any [world model](../world-models/world-model.md) — **perceive** (observe interactions), **model** (infer latent structure), **predict** (anticipate next actions) — with a human where the physical scene usually goes.

## Reactive vs. proactive

The distinction the whole area turns on ([Day 2 keynote](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md), 08:20):

| | Reactive AI | Proactive AI |
|---|---|---|
| Trigger | explicit instruction | anticipated need |
| Burden | on the user — *"you need to know how to prompt, which model to use, what kind of harness to write"* | on the system |
| Model of you | essentially none, despite browsing history | a consistent, evolving model |

The canonical failure: asked to buy groceries on Instacart, a computer-use agent did not ask where the user lives or which store they use — it opened Instacart and began searching for milk in a city the user had no connection to. *"This is really not about the capability missing."*

A second failure mode is multi-agent: two coding agents editing the same file **scored below a single agent**, because they could not resolve conflicts or plan around each other — the **curse of coordination**.

## The 50-year lineage

Not new, and the field's amnesia about this is itself worth noting:

- **1970 — the good regulator theorem.** A good regulator of a system must contain a model of that system.
- **1980s — GOMS / KLM** from HCI: predict which actions a person will take and how long a task will take.
- **1998 — Eric Horvitz's Bayesian mixed-initiative systems**, which shipped as Clippy. *"Clippy was a vision that's very ahead of time. It didn't work out as expected because the technology foundation at that time is very thin."*

## The interruption calculus

What Clippy got structurally right and could not execute: every moment is a decision to interrupt or stay quiet, and it is an expected-utility trade-off — the probability the suggestion is useful, the benefit if it is, and the **cost of a false positive** against the cost of a missed helpful suggestion. An always-on proactive system is making that decision continuously.

## Three empirical results

### 1. The grounding gap — and preference tuning is the culprit

Delete a turn from a human-human conversation, have a model generate it, and compare **discourse acts** — clarification, follow-up, acknowledgement. Humans produce far more of all three; the gap is consistent across conversation datasets and prompting strategies, and *"the newer models actually do similar or worse."*

Isolating the training stages localizes it: **SFT shows no improvement or degradation, and the correlation with human discourse-act usage falls monotonically through preference tuning**, across models and datasets.

> [!note] If this holds, it is load-bearing for every agent page here
> The wiki's [LLM-agent architecture](llm-agent-architecture.md) and [guardrails](../../syntheses/agents/guardrails-for-robot-agents.md) pages assume clarification is a promptable behavior. This says the dominant alignment technique **trains it out**, which would make "ask before acting" an uphill fight against the post-training objective rather than a prompt away. Single source, paper not identified — flagged as the sharpest unverified claim from that workshop.

A related handle on sycophancy: **verbalized assumptions** — make the model state what it is assuming about the user. Across sycophancy datasets the top assumption is *"the user knows they may be in the wrong but seeks validation"*, which humans asked the same way do not make.

### 2. GUM — General User Models

Drop the assumption that a user model is scoped to one context (viewing history → recommendations) and **use everything as context**. A local model observes computer interaction, and every few seconds emits **confidence-weighted propositions** — *"I enjoy eating ice cream and viewing ice cream recipes"*, *"planning to move to Seattle"*, *"P3 prioritizes communicating with their advisor over other people"* — retrieved, merged and revised into a growing bank.

- ~**88%** proposition accuracy against 18 users' own judgement.
- Calibration deliberately **under-confident**: *"if models are very confident, very annoying."*
- Capture is filtered through a **contextual-integrity** audit before inference; anything sensitive is never screenshotted.
- Deployed to five users; majority rated suggestions useful.

The demo that shows the difference: the system saw a professor stalled in PowerPoint for five minutes, saw a Slack message asking where the slides were, knew she gets slides from students, and **drafted a message to the student** — where a chat assistant would have offered to write slides.

### 3. NAP — Next Action Prediction as the base model

The deliberate analogy: **next action prediction is to user models what next token prediction is to language models**, with GUM-style systems as the post-training layer on top.

- Operates over **event sequences**: a context window of recent screen interactions in, a set of predicted next events out.
- Supervision is free — *"as long as you wait for one second you know what this user actually did"* — a sliding window over unlabeled screen recordings.
- Trained on Stanford's **Screenomics** corpus (10,000 people recorded over a month); **1,800 hours, 1.9M screenshots** after annotation.
- Adaptation is **retrieval of past reasoning for that specific user** plus in-context learning, not weight updates, because *"new data should immediately inform the next action prediction"* and weight-based learning is too slow.
- Reported ~**37%**, defended on the grounds that *"the next action on your laptop, the space is actually infinity."* Per-user variance is large — some people are easy to predict, some are not.

## Why this belongs in a robotics wiki

A household assistive robot is a proactive system whose environment is a person. Everything on this page — the interruption calculus, the grounding gap, the false-positive cost, on-device inference under memory and battery limits — is the same problem the wiki's [assistive robotics](../robotics/assistive-robotics.md) and [levels of autonomy](../../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md) pages face, arrived at from the screen side with more data. The wiki's robot-side pages have the autonomy taxonomy; this literature has the *decision rule* for when to act unasked.

It also names a category the wiki's world-model pages lack. A user model is a world model of a system that **changes because it is being modelled** — the same reflexivity [Airoldi and Bruss](../../syntheses/society/world-models-for-financial-markets.md) describe for markets.

## The privacy problem is not solved

Yang raises the **privacy paradox** herself: *"whenever there are benefits or convenience, despite that people mention that they care about privacy, they actually give up on it."* And a participant: *"if I didn't know and trust you I would have never installed this."*

The sharpest objection came from the audience — border-crossing device searches, and whether *"do you support [candidate]"* is answerable from a local user model. The answer given does **not** claim locality is sufficient: sensitive content is filtered at capture, and the capability already exists via social-simulation models trained on public posts. Local execution changes who holds the data; it does not change what the data supports.

## Related concepts
- [World model](../world-models/world-model.md) — the framing being borrowed.
- [LLM agent architecture](llm-agent-architecture.md) / [local model harness design](local-model-harness-design.md) — where a user model would sit.
- [Assistive robotics](../robotics/assistive-robotics.md) / [end-user robot programming](../robotics/end-user-robot-programming.md) — the same problem, embodied.
- [In-context robot learning](../learning/in-context-robot-learning.md) — the same retrieval-over-weights bet.
- [Mechanism design](../economics/mechanism-design.md) — the interruption trade-off is an expected-utility calculation of the same shape.

## Mentioned in
- [Third World Modeling Workshop — Day 2](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — Diyi Yang keynote.

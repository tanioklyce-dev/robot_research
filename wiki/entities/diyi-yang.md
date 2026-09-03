---
title: Diyi Yang
type: entity
subtype: person
created: 2026-09-02
updated: 2026-09-02
sources: 1
tags: [person, diyi-yang, stanford, nlp, user-models, gum, next-action-prediction, proactive-ai, grounding, sycophancy, privacy, hci]
---

**Diyi Yang** — Assistant Professor of Computer Science at **Stanford**, working in NLP and human-AI interaction. Keynote at [Day 2 of the Chicago Booth world-modeling workshop](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) (2026-09-01), *"Optimizing Human-AI Collaboration."*

She brings a claim this wiki had no page for: **"a user model is actually a world model of a person"** — same perceive / model / predict decomposition, applied to a human instead of a physical scene. See [user models](../concepts/agents/user-models.md).

## What she contributes to this wiki

- **The grounding gap.** Compared against held-out human turns, LLMs produce far fewer clarifications, follow-ups and acknowledgements than humans do — and isolating the training stages shows **SFT is neutral while preference tuning is where grounding degrades**, monotonically, across models and datasets. Newer models are *"similar or worse."*
- **GUM (General User Models).** A local model watches any computer interaction and emits **confidence-weighted propositions** about the user, merged and revised over time, with sensitive content filtered at capture through a **contextual-integrity** audit. ~**88%** proposition accuracy against 18 users; deliberately under-confident calibration, because *"if models are very confident, very annoying."*
- **NAP (Next Action Prediction)** as the *base model* for user modelling — deliberately the analogue of next-token prediction, with GUM-style systems as the post-training layer. Trained on Stanford's **Screenomics** corpus (1,800 hours, 1.9M screenshots), using retrieval of past reasoning for in-context adaptation rather than weight updates, because *"new data should immediately inform the next action prediction."*
- **Verbalized assumptions** as a handle on sycophancy: make the model state what it is assuming about the user, and *"seeking validation"* turns out to be the top assumption across sycophancy datasets — one that humans, asked the same way, do not make.

## The lineage she insists on

Not a new idea: the **good regulator theorem** (1970), general user models and GOMS/KLM (1980s), and **Eric Horvitz's Bayesian mixed-initiative work (1998)** that shipped as Clippy. *"Clippy was a vision that's very ahead of time. It didn't work out as expected because the technology foundation at that time is very thin."*

## The objection she takes seriously

She raises the **privacy paradox** herself — *"whenever there are benefits or convenience... they actually give up on it"* — and quotes a participant: *"if I didn't know and trust you I would have never installed this."* Asked directly whether on-device execution is sufficient protection against border-crossing device searches, she does **not** claim it is; she notes sensitive content is filtered at capture and that the capability already exists via social-simulation models on public posts.

## Related
- [User models](../concepts/agents/user-models.md) — the concept page her talk anchors.
- [LLM agent architecture](../concepts/agents/llm-agent-architecture.md) / [on-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md) — where a local user model would plug in.
- [World model](../concepts/world-models/world-model.md) — the framing she borrows.

## Mentioned in
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — keynote.

> [!note] Thin entity
> One talk, no papers ingested. The grounding-gap result in particular is a sharp falsifiable claim about preference tuning that would touch many pages here, and the paper is not identified.

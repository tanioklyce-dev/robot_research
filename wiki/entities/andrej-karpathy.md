---
title: Andrej Karpathy
type: entity
subtype: person
created: 2026-05-14
updated: 2026-05-14
sources: 4
tags: [person, openai, tesla, education, pedagogy, nanogpt, micrograd, nanochat, autoresearch]
---

**Andrej Karpathy** — independent AI researcher and educator; formerly Director of AI at Tesla (Autopilot lead, 2017–2022) and founding member / research scientist at OpenAI. Stanford CS PhD (2015) under Fei-Fei Li; author of the canonical CS231n notes on CNNs. **In this wiki, the author of a series of minimal-but-real reference implementations that have become the de-facto pedagogical references for foundational ML concepts** — backprop (`micrograd`), GPT training (`nanoGPT` → `nanochat`), and most recently agent-driven autonomous research (`autoresearch`).

## Role in this wiki

Karpathy's repos are referenced as the **"read this code to understand the concept" exit ramp** at the bottom of curriculum modules:

- **[Module 1 — Neural networks and training](../syntheses/curriculum/curriculum-01-neural-networks.md)** — [micrograd](../sources/karpathy-micrograd.md) for backprop.
- **[Module 3 — Sequence models, attention, transformers](../syntheses/curriculum/curriculum-03-attention-and-transformers.md)** — [nanoGPT](../sources/karpathy-nanogpt.md) (deprecated as of Nov 2025) → [nanochat](../sources/karpathy-nanochat.md) for transformer training end to end.
- **[LLM-agent architecture concept](../concepts/agents/llm-agent-architecture.md)** — [autoresearch](../sources/karpathy-autoresearch.md) (Mar 2026) as a worked example of an agent autonomously iterating on a real LLM training loop.

The repos share a deliberate design philosophy: **a single hackable file** (or two), **no framework abstractions**, **runs on a single GPU**, **pedagogically transparent over production-ready**. This makes them ideal anchor implementations for understanding modern ML — and explicitly the pattern this wiki's curriculum is structured to teach against.

## The "nano" series progression

```
2020-04  micrograd      — backprop in ~100 lines (scalar autograd + tiny NN library)
2022-12  nanoGPT        — GPT-2 training in two ~300-line files (deprecated Nov 2025)
2025-10  nanochat       — full ChatGPT pipeline (tokenizer + pretrain + SFT + RL + chat UI)
                          for $48-$100 on 8XH100; "Time-to-GPT-2" speedrun leaderboard
2026-03  autoresearch   — AI agent edits a simplified nanochat's train.py overnight;
                          5-min training budget per experiment; produces commit-log
                          of ~100 experiments while you sleep
```

The progression is structurally coherent: **autograd → architecture → training pipeline → autonomous research on the training pipeline**. The 2026 autoresearch entry is wiki-relevant beyond pedagogy because it is one of the first concrete examples of an AI coding agent driving a real ML research loop with a measurable objective ("lower val_bpb"), as opposed to general-purpose code generation. It also produced commits to nanochat that improved the GPT-2 speedrun by 8% in two rounds (rows 5–6 of the nanochat leaderboard).

## Pedagogical influence

Karpathy's [Zero to Hero](https://karpathy.ai/zero-to-hero.html) lecture series + the nano repos are the **most-referenced "how do I actually learn this?" answer** in the curriculum modules. They are not academic papers; they are working code with explanatory framing, which is a much higher pedagogical-value combination than either alone.

The repos are also the most direct demonstration that **modern ML capability can be reproduced on accessible compute**: micrograd on a laptop, nanoGPT on a single GPU, nanochat on an 8-GPU node for under $100. This is the same "consumer-hardware reproducibility" thread that the [Onchain AI Garage LeWM reproduction](../sources/onchain-ai-garage-lewm-reproduction.md) sits inside.

## Related
- [LLM-agent architecture concept](../concepts/agents/llm-agent-architecture.md) — autoresearch is an example.
- [Anthropic](anthropic.md) — Claude Code is one of the agents commonly used with autoresearch.

## Mentioned in
- [micrograd repo (Karpathy, 2020)](../sources/karpathy-micrograd.md)
- [nanoGPT repo (Karpathy, 2022)](../sources/karpathy-nanogpt.md)
- [nanochat repo (Karpathy, 2025)](../sources/karpathy-nanochat.md)
- [autoresearch repo (Karpathy, 2026)](../sources/karpathy-autoresearch.md)
- [Curriculum Module 1 — Neural networks and training](../syntheses/curriculum/curriculum-01-neural-networks.md)
- [Curriculum Module 2 — CNNs and visual representation learning](../syntheses/curriculum/curriculum-02-cnns.md) — CS231n reference.
- [Curriculum Module 3 — Sequence models, attention, transformers](../syntheses/curriculum/curriculum-03-attention-and-transformers.md)

## Open questions / TBD
- The [Zero to Hero](https://karpathy.ai/zero-to-hero.html) lecture series is referenced from Module 1's "Open questions" but not yet filed as a wiki source page. Would be the most-referenced single Karpathy artifact alongside the repos.
- Karpathy has discussed the autoresearch project in two tweets ([1](https://x.com/karpathy/status/2029701092347630069), [2](https://x.com/karpathy/status/2031135152349524125)) — worth ingesting if the wiki ever needs more context on the design rationale.

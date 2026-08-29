---
title: "2 OLMo 2 Furious (OLMo 2 — Team OLMo 2024)"
type: source
url: https://arxiv.org/abs/2501.00656
local_path: raw/2501.00656.pdf
sha256: 8614beaaf35ce5d20fde755d350bd02637bdbe5a390de237ce942c8ac4ee2dd8
author: Team OLMo (Pete Walsh, Luca Soldaini, Dirk Groeneveld, Kyle Lo, …) — Allen Institute for AI / Ai2
published: 2024-12-31
ingested: 2026-07-24
venue: arXiv:2501.00656 (v3 2025-10-08); Ai2
tags: [olmo, olmo-2, open-source-llm, language-model, ai2, training-stability, rlvr, tulu, dolmino]
---

# 2 OLMo 2 Furious (OLMo 2)

## Summary

OLMo 2 is the second generation of the [Allen Institute for AI](../entities/ai2.md)'s fully-open [OLMo](../entities/olmo.md) family — dense models at **7B / 13B / 32B**, again with **everything released** (weights, full data, code + recipes, logs, thousands of checkpoints). The paper is mostly about **how to train a fully-open model well**: a set of **training-stability** and **per-token-efficiency** fixes, a **late-stage data curriculum** (Dolmino), and a **verifiable-reward post-training** recipe (from Tülu 3). The result sits on the **Pareto frontier of performance vs training compute**, matching or beating open-weight-only Llama 3.1 / Qwen 2.5 / Gemma 2 at fewer FLOPs — while being fully transparent.

## Key claims

- **Sizes & tokens.** OLMo-2-7B, -13B, -32B. **7B trained on 4.05T tokens** (3.90T pretrain), **13B on 5.6T** (5T pretrain), 32B larger still.
- **Architecture / stability changes over [OLMo 1](olmo-paper.md):**
  - **RMSNorm** replaces OLMo 1's non-parametric LayerNorm.
  - **Reordered norm** — normalization applied to the **outputs** of attention/FFN blocks (not the inputs) for stability.
  - **QK-norm** — RMSNorm on the query/key projections before attention (per Dehghani et al. 2023).
  - **Z-loss** regularization (weight 1e-5) for run stability; **RoPE θ increased to 5e5**; no weight decay on embeddings.
- **Two-stage data.** Pretrain on **olmo-mix-1124**, then a **mid-training** stage on **Dolmino Mix 1124** — specialized data injected during the **annealing** phase (late-stage curriculum), which "significantly improves capabilities across many downstream benchmarks." Built on the [Dolma](../entities/dolma.md) lineage.
- **Post-training = Tülu 3 → OLMo 2-Instruct.** SFT → **DPO** → **RLVR (RL with Verifiable Rewards)** — the final-stage RL that rewards checkable outputs (math/code correctness). Instruct models are **competitive with GPT-3.5 Turbo and GPT-4o Mini**.
- **Efficiency framing.** Base models on the **Pareto frontier** of performance-to-training-compute; often match/beat **Llama 3.1, Qwen 2.5, Gemma 2** with **fewer FLOPs** and a **fully transparent** data/code/recipe.

## Entities mentioned

- [OLMo](../entities/olmo.md) — the family; OLMo 2 is its second generation.
- [Dolma](../entities/dolma.md) — the corpus lineage; OLMo 2 adds the Dolmino mid-training mix.
- [Ai2](../entities/ai2.md) — the lab.
- [Qwen](../entities/qwen.md) — Qwen 2.5 is a named open-weight-only comparison.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — OLMo-family LLMs as the open decoder layer.

## Open questions

- **RLVR** (RL with verifiable rewards) is the same idea appearing across the wiki's reasoning/robot-RL threads; a dedicated concept page could tie OLMo 2, Tülu 3, and verifiable-reward robot work together — none exists yet.
- OLMo 2 32B vs the 7B/13B compute-optimal trade-offs and exact per-benchmark numbers live in the paper body, not extracted here.

---
title: "OLMoE: Open Mixture-of-Experts Language Models (Muennighoff et al. 2024)"
type: source
url: https://arxiv.org/abs/2409.02060
local_path: raw/2409.02060.pdf
author: Niklas Muennighoff, Luca Soldaini, Dirk Groeneveld, Kyle Lo, … (Allen Institute for AI / Ai2, ~23 authors)
published: 2024-09-03
ingested: 2026-07-24
venue: arXiv:2409.02060 (v2 2025-03-03); Ai2
tags: [olmoe, mixture-of-experts, open-source-llm, language-model, ai2, sparse-moe, routing]
---

# OLMoE: Open Mixture-of-Experts Language Models

## Summary

OLMoE is the **fully-open, Mixture-of-Experts** member of the [OLMo](../entities/olmo.md) family from the [Allen Institute for AI](../entities/ai2.md): a **sparse MoE** LM that has **7B total parameters but activates only ~1B per token**, giving dense-1B inference cost at far-higher-than-1B quality. It's the model behind Molmo's **MolmoE-1B** variant, and — like the rest of OLMo — releases **weights, data, code, and logs**. Beyond the model, it's an unusually candid **MoE cookbook**: the paper runs the design-choice experiments (expert granularity, routing, load balancing, shared experts, upcycling) most labs keep private.

## Key claims

- **Config.** **OLMoE-1B-7B**: 7B total params, **1B active/token**; **64 experts per layer, top-8 activated** (fine-grained "granular experts", FFN dim 1,024 each vs 8,192 dense). Pretrained on **5 trillion tokens**; adapted to **OLMoE-1B-7B-Instruct**.
- **Performance.** Outperforms all available models with **similar active parameters**, and surpasses larger models including **Llama2-13B-Chat** and **DeepSeekMoE-16B** — the MoE efficiency win made concrete.
- **MoE design findings (the cookbook):**
  - **Fine-grained/granular experts** (many small experts, 64×top-8) beat few large ones.
  - **Dropless token-based routing** outperforms expert-based routing.
  - **Shared experts are ineffective** here — challenges a then-common design (contra DeepSeekMoE).
  - **Sparse upcycling** (turning a pretrained dense LM into an MoE) has **limited benefit** except under small compute budgets — argues for training MoE from scratch.
  - Auxiliary **load-balancing loss + router z-loss** are used for stable, well-utilized routing.
  - Routing analysis shows **high expert specialization**.
- **Fully open.** Weights, training data, code, and logs; **Apache 2.0** (code/weights) / **ODC-BY 1.0** (data).

## Entities mentioned

- [OLMoE](../entities/olmoe.md) — the model family (this source's subject).
- [OLMo](../entities/olmo.md) — the dense sibling family.
- [Molmo](../entities/molmo.md) — MolmoE-1B uses OLMoE-1B-7B as its backbone.
- [Ai2](../entities/ai2.md) — the lab.

## Concepts touched

- [Mixture-of-Experts](../concepts/learning/mixture-of-experts.md) — OLMoE is the wiki's open worked example; this paper is its clearest design reference.
- [VLA models](../concepts/learning/vla-models.md) — as a VLM/VLA decoder backbone (via MolmoE).

## Open questions

- The "shared experts ineffective" and "upcycling limited" findings are **first-party to OLMoE's regime**; whether they hold at larger scale (where DeepSeek/Qwen MoEs use shared experts) is contested and not settled here.

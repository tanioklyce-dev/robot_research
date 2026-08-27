---
title: SmolVLM-2
type: entity
subtype: model
created: 2026-05-25
updated: 2026-05-25
sources: 0
tags: [smolvlm, smolvlm-2, hugging-face, vlm, siglip, smollm2, vision-language-model, vla-backbone, efficient]
status: stub
---

> [!note] Stub entity
> Filed 2026-05-25 during lint (13 mentions across 7 wiki files). Primary source — Marafioti et al. ([arXiv 2502.02737](https://arxiv.org/abs/2502.02737), Feb 2025) — **not yet ingested**; deepen when filed.

**SmolVLM-2** — Hugging Face's compact VLM family; the backbone of [SmolVLA](smolvla.md). **~0.4 B parameters** = **[SigLIP](https://arxiv.org/abs/2303.15343) vision encoder** + **SmolLM2 language decoder**. Optimized for multi-image / video inputs and consumer-hardware deployment.

## What we know via the wiki's existing references

- **Architecture**: **SigLIP** vision encoder + **SmolLM2** language decoder.
- **Optimized for multi-image + video** (vs single-image VLMs); uses **image tiling** for high-resolution inputs.
- **SmolVLA uses SmolVLM-2 with two efficiency tweaks** ([SmolVLA paper](../sources/smolvla-paper.md) §3.1):
  - **64 visual tokens per frame** via pixel shuffle, **no tiling** (faster inference).
  - **Layer skipping**: SmolVLA reads VLM features at layer N = L/2 (half the LLM layers), halving compute.
- **Successor to SmolVLM** (the 2024 version); v2 added video / multi-image optimization.

## Why it matters in this wiki

- **The backbone enabling the wiki's affordable-VLA reference** ([SmolVLA](smolvla.md), 450 M total params running on consumer GPUs and CPUs). Filing closes 13 mentions across 7 files.
- **The contrast point to [PaliGemma](paligemma.md) and [Gemma3](gemma3.md)** in the VLM-backbone-for-VLA design space. Cheapest of the three; SmolVLA's competitive results at this scale are the load-bearing evidence that the affordable-VLA path works.

## Related

- [SmolVLA](smolvla.md) — primary downstream user.
- [Hugging Face](hugging-face.md) — maintainer.
- [PaliGemma](paligemma.md), [Gemma3](gemma3.md) — alternative VLM backbones for VLAs (π-series).
- [VLA models](../concepts/learning/vla-models.md) — broader concept.

## Code & weights

- HF: `HuggingFaceTB/SmolVLM2-2.2B-Instruct` (and other variants).
- HF Cookbook entry: https://huggingface.co/blog/smolvlm2

## Open questions

- **Primary source not yet ingested.** When the Marafioti et al. paper lands, deepen with exact param breakdown, training-data mixture, and vision-feature-quality vs SigLIP-default comparisons.
- **SmolLM2 entity** — the language-decoder backbone; mentioned only inline. Not a near-term priority.
- **SmolVLM-3** — referenced in HF blog as a roadmap item; not yet ingested.

## Mentioned in

- [SmolVLA: A vision-language-action model for affordable and efficient robotics (Shukor et al., June 2025)](../sources/smolvla-paper.md)

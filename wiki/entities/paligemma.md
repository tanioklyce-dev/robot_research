---
title: PaliGemma
type: entity
subtype: model
created: 2026-05-25
updated: 2026-05-25
sources: 5
tags: [paligemma, vlm, google, gemma, siglip, vision-language-model, vla-backbone]
status: stub
---

> [!note] Stub entity
> Filed 2026-05-25 during lint (19 mentions across 10 wiki files). Primary source — Beyer et al. 2024 ([arXiv 2407.07726](https://arxiv.org/abs/2407.07726)) — **not yet ingested**; deepen when filed.

**PaliGemma** — Google's open-source vision-language model family (Beyer, Steiner, …, 2024). **3 B-parameter VLM** = **SigLIP-So400m vision encoder** + **Gemma-2B language decoder** + a linear projector. Designed for the size/performance tradeoff suitable for **real-time inference + edge deployment**, which is exactly why [Physical Intelligence](physical-intelligence.md) picked it as the backbone for [π0](pi-zero.md).

## What we know via the wiki's existing references

- **Architecture**: SigLIP vision encoder + Gemma 2B language decoder; 3 B total params.
- **The default VLA-backbone choice for 2024 flow-matching VLAs**: [π0](pi-zero.md) (3.3 B = PaliGemma 3 B + 0.3 B flow-matching action expert) builds directly on it. The π0 paper §IV explicitly cites "comparatively small size (which is useful for real-time control)" as the rationale.
- **Superseded in the π-series by Gemma3 4B** — [π0.7](pi07.md) moves to [Gemma3](gemma3.md) (2025) for the next-gen architecture.
- **Used in the [SmolVLA](smolvla.md) Table 2 ablation** as the "VLM-initialized π0" baseline (vs. the robotics-pretrained π0).

## Why it matters in this wiki

- **The substrate under π0.** Every reference to π0's VLM backbone resolves to PaliGemma.
- **Anchor for the broader "small VLM + action expert" design recipe** that the [VLA action-head taxonomy](../concepts/learning/vla-models.md) tracks: 2024 = PaliGemma + flow-matching action expert; 2025 = Gemma3 / SmolVLM-2 + flow-matching action expert. PaliGemma is the inflection point.

## Related

- [π0](pi-zero.md) — primary downstream user; PaliGemma is the backbone.
- [Gemma3](gemma3.md) — Google successor used by [π0.7](pi07.md).
- [SmolVLM-2](smolvlm.md) — Hugging Face's smaller alternative, used by [SmolVLA](smolvla.md).
- [VLA models](../concepts/learning/vla-models.md) — broader concept.

## Code & weights

- Project page: https://ai.google.dev/gemma/docs/paligemma
- HF: `google/paligemma-3b-pt-224` and related checkpoints.

## Open questions

- **PaliGemma 2** (2024 update) and **PaliGemma 3** (2025) — successor versions; relationship to Gemma3 unclear without primary source.
- **PaliGemma vs Gemma3 architecture differences** — Gemma3 includes a 400M vision encoder built in; PaliGemma uses SigLIP-So400m as a separate component. Whether this is functionally equivalent or a meaningful design difference deserves checking.

## Mentioned in

- [FAST — Efficient Action Tokenization for Vision-Language-Action Models (Pertsch et al. 2025)](../sources/fast-paper.md)
- [Knowledge Insulating Vision-Language-Action Models (Driess et al. 2025)](../sources/knowledge-insulation-paper.md)
- [RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies](../sources/roboarena-paper.md)
- [SmolVLA: A vision-language-action model for affordable and efficient robotics (Shukor et al., June 2025)](../sources/smolvla-paper.md)
- [π0 Paper — A Vision-Language-Action Flow Model for General Robot Control (Black et al., Physical Intelligence, 2024)](../sources/pi-zero-paper.md)

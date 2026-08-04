---
title: Grounding DINO
type: entity
subtype: model
created: 2026-08-04
updated: 2026-08-04
sources: 1
tags: [grounding-dino, open-vocabulary-detection, visual-grounding, cross-attention, vision-language, detr]
---

**Grounding DINO** (Liu et al., 2024) — an **open-set object detector** that fuses a DINO/DETR-style detection transformer with text, producing fine-grained correspondence between textual concepts and image regions. Its **bidirectional cross-modal feature enhancer** — visual features attending to text and text attending to visual features, stacked over several layers — is the mechanism that later gets repurposed for robot control.

## Why it appears in this wiki

[TurboVLA](turbovla.md) borrows Grounding DINO's cross-modal interaction module wholesale and **initializes it from grounding-pretrained feature-enhancement weights** ([paper](../sources/turbovla-paper.md) §5.1). The claim it makes possible is the interesting one: where LLM-centric [VLAs](../concepts/learning/vla-models.md) get vision-language alignment from *language-model* pretraining, TurboVLA gets it from *grounding* pretraining — object-to-word correspondence rather than next-token prediction.

TurboVLA's framing: Grounding DINO uses these features for **localization**; TurboVLA uses the same features to build **control-oriented representations** for continuous action prediction. The ablation supports the borrowing — bidirectional interaction (97.7) beats either one-way variant (96.1 / 96.5) and beats plain concatenation (95.2).

> [!note] A different answer to "where does semantic grounding come from?"
> This is the live question behind the [LLM-free VLA](../concepts/learning/llm-free-vla.md) thread. If open-vocabulary *grounding* pretraining supplies enough object/attribute/relation semantics for manipulation, then the web-scale language priors that [π0.5](pi-zero-5.md)-style co-training buys may be partly redundant at execution level. Untested against [LIBERO-PRO](../sources/libero-pro-paper.md), which is where it would matter.

## Related
- [DINOv3](dinov3.md) — the self-supervised vision-encoder line (related name, different lineage: Grounding DINO's "DINO" is the DETR-family detector)
- [TurboVLA](turbovla.md) — the robotics consumer
- [LLM-free VLA](../concepts/learning/llm-free-vla.md)

## Mentioned in
- [TurboVLA paper](../sources/turbovla-paper.md)

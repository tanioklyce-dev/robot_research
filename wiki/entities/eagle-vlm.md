---
title: Eagle (NVIDIA VLM family)
type: entity
subtype: model
created: 2026-07-04
updated: 2026-07-04
sources: 5
tags: [eagle, vlm, nvidia, mixture-of-encoders, siglip, long-context, groot-backbone]
---

**Eagle** — NVIDIA's open vision-language-model (VLM) family (NVlabs; corresponding authors Guilin Liu + Zhiding Yu across the line). In this wiki it matters chiefly as the **VLM backbone of the [GR00T](nvidia-groot.md) VLA through N1.5**, before the migration to [Cosmos](nvidia-cosmos.md) from N1.6 on.

## The line
- **Eagle (Eagle-1)** — *"Exploring the Design Space for Multimodal LLMs with Mixture of Encoders"* (ICLR 2025; [paper](../sources/eagle-paper.md)). A systematic study whose headline finding is that **channel-concatenating tokens from complementary vision encoders** (CLIP + ConvNeXt + EVA-02 + Pix2Struct + SAM) beats complex fusion/routing, plus a **pre-alignment** stage for non-text-aligned experts. Strong on OCR/high-res.
- **Eagle 2 / Eagle 2.5** — productized successors sharing the same NVIDIA authorship lineage. **[Eagle 2.5](../sources/eagle-2-5-paper.md)** (*"Boosting Long-Context Post-Training for Frontier VLMs"*, Apr 2025) **drops the mixture-of-encoders design** for a single **SigLIP-so400M** encoder + long-context machinery (information-first sampling, 32K→64K→128K progressive training, the Eagle-Video-110K dataset). Flagship Eagle 2.5-8B hits **72.4% Video-MME** at 8B, matching 72B-class models.

## As the GR00T backbone
> [!note] Sourcing
> The GR00T-backbone claim is documented in the **GR00T papers, not the Eagle papers** (neither Eagle paper mentions GR00T, GR-1, or manipulation grounding).

- [GR00T N1](../sources/groot-n1-paper.md) uses **Eagle-2** (the production model, finetuned from SmolLM2 + SigLIP-2) as its System-2 VLM.
- [GR00T N1.5](../sources/groot-n1_5.md) upgrades to **Eagle 2.5** and **freezes** it — its stronger grounding (VLM GR-1 grounding IoU 40.4 vs 35.5 for Qwen2.5-VL) is credited with N1.5's large language-following gains.
- From [GR00T N1.6](../sources/groot-n1_6.md) on, the backbone moves to [Cosmos](nvidia-cosmos.md)-2B → Cosmos-Reason2-2B, superseding Eagle.

## Related
- [NVIDIA GR00T](nvidia-groot.md) — primary consumer of Eagle as a backbone.
- [NVIDIA Cosmos](nvidia-cosmos.md) — the successor backbone from GR00T N1.6.
- [DINOv2](dinov2.md) / SigLIP — vision encoders in the Eagle stack (Eagle-1 mixture incl. DINOv2; Eagle 2.5 = SigLIP-so400M).
- [VLA models](../concepts/learning/vla-models.md) — Eagle is the VLM half of the GR00T System-1/System-2 split.

## Mentioned in
- [Eagle Paper (mixture of encoders)](../sources/eagle-paper.md) — primary source (Eagle-1)
- [Eagle 2.5 Paper (long-context)](../sources/eagle-2-5-paper.md) — primary source (Eagle 2.5)
- [GR00T N1 Paper](../sources/groot-n1-paper.md) — Eagle-2 backbone
- [GR00T N1.5 research page](../sources/groot-n1_5.md) — Eagle 2.5 backbone

## Open questions
- **Eagle 2** (the exact GR00T N1 production backbone) has no standalone paper in the wiki — only Eagle-1 (research study) and Eagle 2.5 are filed.
- Eagle 2.5's grounding-for-manipulation numbers (GR-1 IoU) come from the GR00T N1.5 page, not the Eagle 2.5 paper.

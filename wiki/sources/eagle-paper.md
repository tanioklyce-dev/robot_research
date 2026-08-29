---
title: Eagle — Exploring the Design Space for Multimodal LLMs with Mixture of Encoders (paper)
type: source
url: https://arxiv.org/abs/2408.15998
author: Min Shi, Fuxiao Liu, Shihao Wang, … Bryan Catanzaro, Andrew Tao, Jan Kautz, Zhiding Yu, Guilin Liu (NVIDIA + Georgia Tech + UMD + HKPU + NYU)
published: 2024-08 (arXiv 2408.15998v2, 2025-03-02; ICLR 2025)
ingested: 2026-07-04
local_path: raw/EAGLE_2408.15998v2.pdf
sha256: 2be3a9854be24f656a38c35b3f70eb51bd59c9cd3784645b5dc7af693d68290d
format: pdf
tags: [eagle, vlm, mllm, mixture-of-encoders, channel-concatenation, nvidia, iclr-2025, ocr]
---

## Summary

The original **[Eagle](../entities/eagle-vlm.md)** paper (ICLR 2025) — a systematic ablation of the *mixture-of-vision-encoders* design space for multimodal LLMs. Rather than a novel fusion module, it does apples-to-apples comparisons of encoders, resolutions, fusion strategies, and training recipes, and distills principles. Headline finding: **channel-concatenating visual tokens from complementary vision encoders is as effective as — and more efficient than — complex fusion/routing**. It adds a **pre-alignment** stage to bridge non-text-aligned experts (detection/OCR/segmentation) to the language space. Matters in this wiki as the research foundation of the [Eagle](../entities/eagle-vlm.md) family whose Eagle-2 production model became the [GR00T N1](groot-n1-paper.md) VLM backbone.

## Key claims
- **Base**: LLaVA-1.5 architecture; SFT on a curated **Eagle1.8M** conversation set.
- **Mixture of encoders**: CLIP, ConvNeXt (OpenCLIP), EVA-02 (detection), Pix2Struct (OCR), SAM (segmentation), [DINOv2](../entities/dinov2.md) (SSL) — each emitting 1024 tokens.
- **Channel concatenation wins** over Sequence Append / LLaVA-HR / Mini-Gemini / Deformable Attention — better performance + expandability + efficiency, keeping sequence length fixed as experts are added.
- **High resolution by unfreeze+interpolate** (CLIP → 448×448, up to 1024×1024) rather than tiling; unlocking vision encoders during training matters.
- **Pre-alignment (3-stage)**: individually align each non-text expert to a frozen Vicuna-7B, then joint projector training, then full SFT — consistently beats plain unfreeze.
- **Best recipe**: CLIP + ConvNeXt + SAM + Pix2Struct + EVA-02 (**Eagle-X5**, peaks at 5 encoders). LLM backbones: Vicuna-7B/13B, Llama3-8B.
- **Benchmarks** (Eagle-X5, Vicuna-13B): MME 1605, MMBench 71.6, POPE 89.2, VQAv2 84.5, OCRBench 598, TextVQA 73.3, ChartQA 72.1. Strong OCR/chart gains vs Cambrian-1 under identical data.

## Entities mentioned
- [Eagle (NVIDIA VLM family)](../entities/eagle-vlm.md) — this is the founding paper. NVIDIA (NVlabs) + Georgia Tech + UMD + HKPU + NYU.
- Vision encoders: CLIP, ConvNeXt, EVA-02, Pix2Struct, SAM, [DINOv2](../entities/dinov2.md). LLMs: Vicuna, Llama3.

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) — the VLM (System-2) half of the GR00T stack; this is a VLM-design study, not a robotics paper.
- Mixture of vision encoders / channel-concatenation fusion; vision-language pre-alignment; high-resolution multimodal perception.

## Open questions
- **Eagle-1 predates GR00T and does not mention it** — the GR00T-backbone link runs through the [GR00T N1 paper](groot-n1-paper.md), which uses the later *Eagle-2* production model.
- No standalone **Eagle 2** paper on file; only Eagle-1 and [Eagle 2.5](eagle-2-5-paper.md).

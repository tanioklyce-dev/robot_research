---
title: Eagle 2.5 — Boosting Long-Context Post-Training for Frontier Vision-Language Models (paper)
type: source
url: https://arxiv.org/abs/2504.15271
author: Guo Chen, Zhiqi Li, Shihao Wang, Jindong Jiang, … Bryan Catanzaro, Jan Kautz, Andrew Tao, Zhiding Yu, Guilin Liu (NVIDIA + Nanjing U + HKPU + Rutgers)
published: 2025-04-21 (arXiv 2504.15271v1)
ingested: 2026-07-04
local_path: raw/EAGLE_2.5_2504.15271v1.pdf
sha256: 281119e779a37087fec3ab830d19876d9c9a20b03d6ad9169ee396d7cc6e6401
format: pdf
tags: [eagle, eagle-2-5, vlm, long-context, long-video, siglip, nvidia, groot-backbone]
---

## Summary

**[Eagle 2.5](../entities/eagle-vlm.md)** — NVIDIA's family of frontier VLMs specialized for **long-context multimodal understanding** (long video + high-resolution documents). Flagship **Eagle 2.5-8B** whose accuracy *keeps improving as input length grows*, reaching **72.4% on Video-MME (512 frames, no subtitles) — matching GPT-4o, Qwen2.5-VL-72B, and InternVL2.5-78B despite being 8B**. Notably it **drops Eagle-1's mixture-of-encoders design** for a single **SigLIP-so400M** encoder plus long-context machinery. In this wiki it's the **VLM backbone of [GR00T N1.5](groot-n1_5.md)** (frozen), whose stronger grounding is credited with N1.5's language-following gains.

## Key claims
- **Architecture change**: single **SigLIP-so400M** → MLP connector → Qwen2.5 LLM, with LLaVA-style tiling (448×448 tiles, 256 tokens/tile). The Eagle-1 mixture-of-encoders approach is gone.
- **Three ingredients**: (1) **information-first sampling** — Image Area Preservation (retain ≥60% image area) + Automatic Degradation Sampling (keep complete text, fill visual budget by temporal + tiling degradation); (2) **progressive mixed post-training** growing context 32K→64K→128K (beats direct 64K); (3) **Eagle-Video-110K** — a self-curated long-video dataset with dual (story-level + clip-level) annotation.
- **Scales with context**: Video-MME rises monotonically 16→1024 frames, unlike competitors that plateau.
- **Benchmarks (Eagle2.5-8B)**: Video-MME 72.4 (w/o sub) / 75.7 (w/ sub); MVBench 74.8; MLVU 77.6; DocVQA 94.1; ChartQA 87.5; TextVQA 83.7; OCRBench 869; image avg 75.6.

## Entities mentioned
- [Eagle (NVIDIA VLM family)](../entities/eagle-vlm.md) — this is the Eagle 2.5 primary source. NVIDIA + Nanjing U + HKPU + Rutgers.
- SigLIP-so400M (sole vision encoder), Qwen2.5 (LLM backbone).
- [SigLIP](../entities/siglip.md) — the single SigLIP-so400M encoder Eagle 2.5 drops the mixture-of-encoders design for.

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) — the System-2 VLM of GR00T N1.5.
- Long-context / long-video multimodal understanding; information-first sampling; progressive context-length curriculum.

## Open questions
- **Does not mention GR00T/GR-1/manipulation grounding** — the GR00T N1.5-backbone + GR-1-grounding-IoU claims are sourced from the [GR00T N1.5 page](groot-n1_5.md), not this paper.
- No dedicated Eagle 2 paper on file (the exact GR00T N1 backbone); only Eagle-1 ([paper](eagle-paper.md)) and Eagle 2.5.

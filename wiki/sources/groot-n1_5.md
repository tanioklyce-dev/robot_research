---
title: GR00T N1.5 — Research Page (NVIDIA GEAR)
type: source
url: https://research.nvidia.com/labs/gear/gr00t-n1_5/
author: NVIDIA GEAR
published: 2025-06-11
ingested: 2026-07-04
format: web (research-lab page)
tags: [groot, groot-n1-5, vla, nvidia, gear, flare, dreamgen, language-following, frozen-vlm, eagle-vlm]
---

## Summary

The GR00T **N1.5** research page — an incremental but high-impact update to [GR00T N1](groot-n1-paper.md). The headline is a **frozen VLM** (Eagle 2.5 backbone), a simplified vision-language adapter with added layer normalization, and a new **FLARE** (Future LAtent Representation Alignment) auxiliary loss alongside flow matching. Combined with DreamGen-generated neural trajectories in the training mix, N1.5 delivers dramatic **language-following** gains (real GR-1 language-following rate 46.6% → 93.3%) and much stronger low-data post-training. Released 2025-06-11 as [`nvidia/GR00T-N1.5-3B`](https://huggingface.co/nvidia/GR00T-N1.5-3B).

## Key claims

### Architecture changes vs N1
- **VLM frozen during both pretraining and finetuning** (N1 unfroze the vision encoder). Backbone upgraded to NVIDIA **Eagle 2.5** for improved grounding — N1.5's VLM scores **40.4 IoU on GR-1 grounding vs 35.5 for Qwen2.5-VL**.
- **Simplified adapter**: the MLP connecting vision encoder → LLM adds **layer normalization** to both visual and text token embeddings.
- DiT cross-attention to vision-language embeddings unchanged from N1.
- **New objective**: adds **FLARE** (Future LAtent Representation Alignment) loss at coefficient **0.2** alongside the flow-matching loss — this is the mechanism that lets human video (no action labels) contribute to manipulation skill.

### Training data
- Pretraining mixture: internal GR-1 teleop, OpenX-Embodiment, simulated GR-1 (DexMimicGen), **neural trajectories from [DreamGen](../entities/nvidia-gear.md)**, and **AgiBot-Beta**.
- Trained **250K steps on 1K H100 GPUs, global batch size 16,384**.

### Results (verbatim numbers)
- **Simulated language following**: Language Table 52.8% → **93.2%**; Sim GR-1 Language 36.4% → **54.4%**.
- **Low-data post-training**: RoboCasa (30 demos) 17.4 → **47.5**; Sim GR-1 0-shot 39.6 → **43.9**; Sim GR-1 (30 demos) 43.2 → **47.4**.
- **Real GR-1 fruit-placement**: language-following rate 46.6% → **93.3%**; overall success 43.3% → **83.0%**.
- **Novel-object generalization**: 0-shot 0% → **15.0%**; with FLARE post-training on human videos → **55.0%**.
- **DreamGen novel verbs (12 tasks)**: 13.1% → **38.3%**.
- **[Unitree G1](../entities/unitree-g1.md) post-training (1K demos)**: seen objects 44.0% → **98.8%**; novel objects **84.2%** — the first strong cross-embodiment (non-GR-1 humanoid) result in the GR00T line.

### Limitations / takeaways
- DreamGen tasks are "zero-shot" only in the data-collection sense — the model still trains on the synthetic trajectories; full zero-shot verb/environment generalization is left to future work.
- Main gains: much better language grounding + low-data-regime performance. The frozen-VLM + FLARE recipe is the load-bearing change.

## Entities mentioned
- [NVIDIA GR00T](../entities/nvidia-groot.md) — this is the N1.5 version page. [NVIDIA GEAR](../entities/nvidia-gear.md) — lab; DreamGen is its Dream*-world-model line.
- [Fourier GR-1](../entities/fourier-gr-1.md) — primary platform. [Unitree G1](../entities/unitree-g1.md) — cross-embodiment validation.
- [Open X-Embodiment](../entities/open-x-embodiment.md), [MimicGen](../entities/mimicgen.md) (DexMimicGen), [RoboCasa](../entities/robocasa.md) — training/eval data.
- Eagle 2.5 VLM (NVIDIA) — backbone; not a separate entity yet.

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) — the frozen-VLM design choice is a notable divergence from N1's unfrozen-encoder recipe.
- [Flow matching](../concepts/learning/flow-matching.md) — action head; FLARE is an auxiliary latent-alignment loss on top.
- [World model](../concepts/world-models/world-model.md) — FLARE aligns to *future latent representations* (a JEPA-adjacent auxiliary objective inside a VLA, echoing [VLA-JEPA](vla-jepa-paper.md)).
- [Imitation learning](../concepts/learning/imitation-learning.md) — DreamGen neural trajectories as synthetic demonstration data.

## Open questions
- FLARE has no dedicated wiki page; it appears in the [GEAR publications](nvidia-gear-publications.md) as "FLARE (implicit WM)" — the N1.5 page is the first concrete use in a shipped model. Worth a concept note if it recurs.
- Eagle / Eagle 2.5 VLM family — no entity page; NVIDIA's in-house VLM line underneath N1/N1.5.

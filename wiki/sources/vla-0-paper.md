---
title: VLA-0 — Building State-of-the-Art VLAs with Zero Modification
type: source
url: https://arxiv.org/abs/2510.13054
author: Ankit Goyal, Hugo Hadfield, Xuning Yang, Valts Blukis, Fabio Ramos (NVIDIA)
published: 2025-10-15
ingested: 2026-07-17
local_path: raw/2510.13054v1.pdf
venue: arXiv preprint (cs.RO), 2510.13054v1
license: null
format: PDF (6 pages)
tags: [vla, vision-language-action, action-as-text, libero, qwen, so-100, lerobot, nvidia, action-chunking, ablation]
---

# VLA-0 — Building State-of-the-Art VLAs with Zero Modification

## Summary

An NVIDIA paper making a deliberately contrarian point: the **simplest possible way to turn a VLM into a [VLA](../concepts/learning/vla-models.md) — just prompt it to output the action as a string of integers — beats almost everything more complicated.** No new action tokens, no vocabulary changes, no diffusion/flow-matching action head, no custom architecture. VLA-0 wraps an unmodified **[Qwen2.5-VL-3B](../entities/qwen.md)** and, on the **[LIBERO](../entities/libero.md)** benchmark, **outperforms every method trained on the same robot data** (π0.5-KI, [OpenVLA-OFT](../entities/openvla.md), [SmolVLA](../entities/smolvla.md)) and even beats models with *large-scale action pretraining* (π0, [GR00T-N1](../entities/nvidia-groot.md), MolmoAct, [Octo](../entities/octo.md)) — losing only to OpenVLA-OFT among pretrained models. In the real world (SO-100 + [LeRobot](../entities/lerobot.md)) it beats SmolVLA by **12.5 points** despite SmolVLA having been pretrained on large-scale SO-100 data. The whole result hinges on a **careful recipe**, not the naïve idea alone.

## Key claims

- **The core idea — "action as text."** Normalize continuous actions to an integer range (e.g. `[0, 1000]`), then have the VLM autoregressively generate the `H × D` integers (H timesteps × D action dims) as **space-separated numbers**, trained with the base VLM's standard cross-entropy loss. Gives **arbitrary action resolution without touching the vocabulary** — the resolution/vocab-size tradeoff that plagues discrete-token VLAs disappears. (§III.B, Fig. 1/3)
- **The taxonomy VLA-0 argues against (§I, Fig. 2).** Prior VLAs fall in three families: **(1) Discrete-token** (RT-2, OpenVLA — bin actions into vocabulary tokens; limits resolution + corrupts language tokens); **(2) Generative action head** (π0, SmolVLA — VLM emits a latent, a diffusion/flow-matching net decodes it; adds a non-pretrained head that can degrade language grounding); **(3) Custom architecture** ([OpenVLA-OFT](../entities/openvla-oft.md)'s ACT head, [π0-FAST](../entities/fast-action-tokenization.md)'s DCT tokenizer — effective but intricate). VLA-0 proposes a **fourth, "zero-modification" family**: predict action directly as text.
- **LIBERO results (Table I).** Among models **without** large-scale action pretraining, VLA-0 is **best on all four suites** — Spatial **97.0**, Object **97.8**, Goal **96.2**, Long **87.6**, avg **94.7**, average rank **1.0** (next best π0.5-KI 93.3, OpenVLA-OFT 91.9, SmolVLA-2.25B 88.8, Diffusion Policy 72.4). Compared against **pretrained** models, VLA-0 (no pretraining) still gets **rank 2.8**, beating π0 (94.2), π0.5-KI (94.3), GR00T-N1 (93.9), MolmoAct (86.8), OpenVLA (76.5), Octo (75.1); only **OpenVLA-OFT-pretrained** (97.1, rank 1.5) edges it.
- **Real-world (§IV.D, Fig. 4).** SO-100 arm, LeRobot framework, 4 tasks (reorient block, push apple, pick-place banana, pick-place cupcake), 100 demos each. VLA-0 (trained from scratch on in-domain data) **beats SmolVLA (pretrained on large-scale SO-100) by 12.5 pts on average**. Inference ~**4 Hz** on a single RTX 5090, standard PyTorch (no ensembling used in real to avoid 8 parallel model instances).
- **The recipe (three ingredients, §III.B).**
  - **Action decoding as normalized integers** — resolution 1000 is the sweet spot (see ablation).
  - **Ensemble prediction** — borrowed from **[ACT](../entities/act.md)**'s action chunking: at each step average the `n` overlapping predictions made for the current timestep across the last `n` inference steps. **+2.0 pts** — the single most important component.
  - **Masked Action Augmentation** — randomly mask characters in the target action string during training, forcing the VLM to ground actions in the image/instruction rather than auto-completing a numeric sequence. **+1.2 pts**.
- **Ablations (Table II).** No-ensemble −2.0; no-masking −1.2; resolution 250 −1.5, resolution 4000 no gain over 1000; image tiling vs. separate images −0.2 (negligible).
- **Training cost.** Full fine-tune of Qwen2.5-VL-3B, Adam, 64 epochs, batch 192, LR 5e-6, **~32 h on 8× A100**.
- **Closest prior work.** LLARVA (action-as-text but via a two-stage 2D-trajectory-then-action process) and HAMSTER (hierarchical, VLM predicts a 2D trajectory in text); VLA-0 differs by predicting the **complete** robot action (joint/EE-delta) end-to-end as text, with the ensembling + masking recipe LLARVA lacks.

## Entities mentioned

- [Qwen](../entities/qwen.md) — the unmodified Qwen2.5-VL-3B backbone.
- [LIBERO](../entities/libero.md) — the primary simulation benchmark.
- [SmolVLA](../entities/smolvla.md) — the real-world SO-100 baseline VLA-0 beats by 12.5 pts.
- [OpenVLA](../entities/openvla.md) / [OpenVLA-OFT](../entities/openvla-oft.md) — discrete-token baseline and its optimized-fine-tuning successor; OFT is the one pretrained model to edge out VLA-0 on LIBERO.
- [GR00T](../entities/nvidia-groot.md), [Octo](../entities/octo.md), [π0](../entities/pi-zero.md) — pretrained baselines VLA-0 surpasses without pretraining.
- [π0-FAST / FAST](../entities/fast-action-tokenization.md) — DCT discrete-token baseline (custom-architecture family).
- [MolmoAct](../entities/molmoact.md) — Allen Institute discrete-token "action reasoning" baseline (LIBERO 86.8).
- [ACT](../entities/act.md) — source of the prediction-ensembling / action-chunking trick.
- [SO-ARM101 / SO-100](../entities/so-arm101.md), [LeRobot](../entities/lerobot.md) — real-world hardware + framework.
- [Diffusion Policy](../entities/diffusion-policy.md) — from-scratch BC baseline.
- [VLA-0](../entities/vla-0.md) — the model this paper introduces.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — VLA-0 adds an "action-as-text" fourth family to the action-head taxonomy.
- [Knowledge Insulation](../concepts/learning/knowledge-insulation.md) — the recipe behind the **π0.5-KI** baseline (LIBERO 94.3/93.3).
- [Imitation learning](../concepts/learning/imitation-learning.md) — VLA-0 is behavior cloning with a VLM backbone.

## Open questions

- **Would VLA-0 + large-scale action pretraining top OpenVLA-OFT?** The authors flag this as the obvious next experiment — VLA-0's numbers are all *without* the pretraining every top-ranked pretrained model enjoyed.
- **Inference speed.** 4 Hz (single 5090, unquantized) is slow for reactive control; the paper defers distillation/quantization to future work. The action-as-text approach pays a token-generation cost that flow-matching heads (fixed-size decode) avoid.
- How much of the win is Qwen2.5-VL-3B specifically vs. the recipe? The method claims VLM-agnosticism but reports only one backbone.

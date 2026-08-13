---
title: OpenVLA-OFT
type: entity
subtype: model
created: 2026-07-17
updated: 2026-07-17
sources: 6
tags: [openvla-oft, vla, vision-language-action, parallel-decoding, action-chunking, l1-regression, film, libero, aloha]
---

# OpenVLA-OFT

**OpenVLA-OFT** ("**O**ptimized **F**ine-**T**uning"; Moo Jin Kim, [Chelsea Finn](chelsea-finn.md), Percy Liang, Stanford — [paper](../sources/openvla-oft-paper.md), arXiv 2502.19645, RSS 2025) is a **fine-tuning recipe** for VLAs, instantiated on [OpenVLA](openvla.md), that replaces slow autoregressive action-token decoding with **parallel decoding + action chunking + continuous actions + an L1-regression head**. It is in the **top tier on [LIBERO](libero.md)** in the wiki (97.1 — [statistically tied](../syntheses/platforms/vla-success-rate-audit.md) with MolmoAct2 / GR00T N1.7 / π0.5; the robust result is the **+20.6 pp recipe effect** over base OpenVLA) and the custom-architecture exemplar of the [VLA action-head taxonomy](../concepts/learning/vla-models.md).

## Why it matters in this wiki

OpenVLA-OFT is the **benchmark to beat** and the wiki's cleanest "**the fine-tuning recipe, not the base model, was the bottleneck**" data point: keeping the *same* OpenVLA weights, OFT raises LIBERO average success **76.5% → 97.1%** while making action generation **26× faster**. It's the one pretrained model that finishes above [VLA-0](vla-0.md) on LIBERO ([VLA-0 paper](../sources/vla-0-paper.md)), and one of the baselines the [Knowledge Insulation](../concepts/learning/knowledge-insulation.md) paper measures itself against — the two are contemporaneous answers to the same "how do you fine-tune a VLA well?" question, from the L1-regression and flow-matching sides respectively.

## The OFT recipe (three design choices)

The paper studies three axes for adapting a VLA and picks the winning combination ([OFT paper](../sources/openvla-oft-paper.md) §IV):

1. **Parallel decoding + action chunking** — feed **empty action embeddings** and replace the causal mask with **bidirectional attention**, so a whole K-step action chunk emits in **one forward pass** instead of K·D sequential token decodes. Alone this adds **+14% absolute** LIBERO success (biggest on Long-horizon) *and* the throughput win.
2. **Continuous action representation** — an **MLP action head** maps decoder hidden states to real-valued actions (vs. 256-bin discretization). Adds **+5% absolute** over discrete.
3. **L1-regression objective** — plain mean-L1 loss on continuous actions ([ACT](act.md)-style). **Matches diffusion** in success but trains and infers far faster (diffusion needs ~50 denoising steps).

**OFT+** = the recipe **+ FiLM** (feature-wise linear modulation infusing language embeddings into ViT features), used for the real **ALOHA** experiments where multi-camera setups create spurious correlations that hurt language following.

## Key facts

- **Base model:** [OpenVLA](openvla.md) 7B (Prismatic VLM, 1M [OXE](open-x-embodiment.md) episodes), adapted via LoRA on ~500 demos.
- **LIBERO** ([OFT paper](../sources/openvla-oft-paper.md), Table I): Spatial **97.6** / Object **98.4** / Goal **97.9** / Long **94.5** / avg **97.1** — SOTA; vs base OpenVLA 76.5, π0 94.2.
- **Efficiency:** **26×** throughput (8-step chunks) to **43×** (25-step) over base OpenVLA; latency **0.07 ms** (single-arm/1 image) → **0.321 ms** (bimanual/3 images), vs OpenVLA's 0.33 s per timestep.
- **Real-world:** OpenVLA-OFT+ runs dexterous bimanual **ALOHA** tasks at **25 Hz**, beating fine-tuned π0 / RDT-1B and from-scratch [Diffusion Policy](diffusion-policy.md) / [ACT](act.md) by **up to 15% absolute**.
- **Paradigm:** pure offline imitation — no separate low-level controller, no online RL. Open-source (code + checkpoints).

## Related

- [OpenVLA](openvla.md) — the base model / predecessor; OFT is its optimized fine-tuning recipe.
- [VLA-0](vla-0.md) — the action-as-text VLA that OFT (pretrained) narrowly tops on LIBERO.
- [Knowledge Insulation](../concepts/learning/knowledge-insulation.md) — the PI recipe attacking the same problem from the flow-matching side.
- [ACT](act.md) — source of the L1-regression continuous-action head.
- [VLA models](../concepts/learning/vla-models.md) — the concept; OFT is the "custom architecture" family exemplar.
- [Chelsea Finn](chelsea-finn.md) — co-author.

## Mentioned in

- [OpenVLA-OFT paper](../sources/openvla-oft-paper.md) — the introducing primary source.
- [VLA-0 paper](../sources/vla-0-paper.md) — reports OFT as the top LIBERO model (rank 1.5), the only pretrained model above VLA-0.

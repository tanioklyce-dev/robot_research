---
title: Fine-Tuning Vision-Language-Action Models — Optimizing Speed and Success (OpenVLA-OFT, Kim et al. 2025)
type: source
url: https://arxiv.org/abs/2502.19645
author: Moo Jin Kim, Chelsea Finn, Percy Liang (Stanford)
published: 2025-02-26
ingested: 2026-07-17
local_path: raw/2502.19645v2.pdf
venue: arXiv preprint (cs.RO), 2502.19645v2 (RSS 2025)
license: null
format: PDF (24 pages)
tags: [openvla-oft, vla, fine-tuning, parallel-decoding, action-chunking, l1-regression, film, libero, aloha, inference-efficiency]
---

# Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

## Summary

The Stanford paper introducing **[OpenVLA-OFT](../entities/openvla-oft.md)**. It asks a narrow, practical question — *what is the best way to **fine-tune** a VLA?* — and answers it with a controlled study over three design axes, using [OpenVLA](../entities/openvla.md) as the base. The winning **Optimized Fine-Tuning (OFT)** recipe = **parallel decoding + action chunking + continuous actions + a simple L1-regression objective**. It sets a new [LIBERO](../entities/libero.md) SOTA — lifting OpenVLA's average success **76.5% → 97.1%** while making action generation **26× faster** — and, augmented with **FiLM** (the "OFT+" variant), runs dexterous bimanual tasks on a real **ALOHA** robot at **25 Hz**, beating [π0](../entities/pi-zero.md), RDT-1B, [Diffusion Policy](../entities/diffusion-policy.md) and [ACT](../entities/act.md) by up to **15% absolute**. The paper's contribution is a *recipe and its justification*, not a new model architecture.

## Key claims

- **The gap it fills.** VLAs need fine-tuning to work on a new robot, but the best fine-tuning strategy was unclear. Autoregressive fine-tuning (even LoRA) is too slow (**3–5 Hz**) for high-frequency control (25–50+ Hz) and unreliable on bimanual arms; better tokenizers (VQ, [FAST](../entities/fast-action-tokenization.md)'s DCT) give 2–13× but still carry ~750 ms inter-chunk latency. (§I–II)
- **Three design axes studied** (Fig. 2), on OpenVLA (7B, Prismatic VLM, 1M OXE episodes), via LoRA on ~500 demos:
  1. **Action decoding — autoregressive vs. parallel.** Parallel decoding feeds **empty action embeddings** and swaps the causal mask for **bidirectional attention**, so all actions emit in **one forward pass** (D passes → 1). It extends naturally to **action chunking** (insert more empty embeddings → predict K·D actions at once).
  2. **Action representation — discrete vs. continuous.** Discrete = 256-bin per-dimension + softmax; continuous = an **MLP action head** mapping decoder hidden states directly to real-valued actions.
  3. **Learning objective — next-token CE vs. L1 regression vs. diffusion.**
- **Findings (each builds on the last).**
  - **Parallel decoding + action chunking** alone raise LIBERO average success **+14% absolute** over autoregressive OpenVLA *and* boost throughput — biggest gain on LIBERO-Long (chunking captures temporal dependencies / cuts compounding error).
  - **Continuous** actions add **+5% absolute** over discrete (finer precision).
  - **L1 regression ≈ diffusion** in success, but L1 trains and infers **much faster** (diffusion needs ~50 denoising steps) — so the recipe picks **L1**. OpenVLA's high capacity models the multi-task action distribution fine with plain L1.
- **The OFT recipe** = parallel decoding + action chunking + continuous actions + L1 regression, end-to-end (no separate low-level controller, no online RL — pure offline imitation).
- **LIBERO (Table I).** OpenVLA-OFT = Spatial **97.6** / Object **98.4** / Goal **97.9** / Long **94.5** / avg **97.1** — new SOTA, vs base OpenVLA 76.5 and π0 94.2. **26× throughput** with 8-step chunks.
- **Efficiency.** 26× (8-step chunk) to **43×** (25-step) throughput over base OpenVLA; latency **0.07 ms** (single-arm, 1 image) to **0.321 ms** (bimanual, 3 images) — vs OpenVLA's 0.33 s per single timestep.
- **OFT+ / FiLM (real ALOHA, §VI).** Multi-view (incl. wrist cams) creates spurious visual correlations that hurt language following; **FiLM** (feature-wise linear modulation) infuses averaged language embeddings into the ViT visual features (applied per-hidden-unit across all patches, after self-attention). "**+**" = FiLM-augmented. OpenVLA-OFT+ runs dexterous bimanual tasks (clothes folding, prompted food manipulation) at **25 Hz**, beating fine-tuned π0 / RDT-1B and from-scratch Diffusion Policy / ACT by **up to 15% absolute**.
- Open-source: code + checkpoints at openvla-oft.github.io.

## Entities mentioned

- [OpenVLA-OFT](../entities/openvla-oft.md) — the model/recipe introduced.
- [OpenVLA](../entities/openvla.md) — the base VLA fine-tuned (7B, Prismatic VLM, OXE).
- [LIBERO](../entities/libero.md) — the primary simulation benchmark.
- [ACT](../entities/act.md) — source of the L1-regression continuous-action head; a real-world baseline.
- [Diffusion Policy](../entities/diffusion-policy.md) — the diffusion-objective comparison + a from-scratch baseline.
- [π0](../entities/pi-zero.md) — flow-matching VLA baseline (LIBERO + ALOHA).
- [FAST](../entities/fast-action-tokenization.md) — the DCT-tokenizer speedup approach OFT contrasts against (~750 ms latency).
- [Open X-Embodiment](../entities/open-x-embodiment.md) — OpenVLA's pretraining corpus.
- [Chelsea Finn](../entities/chelsea-finn.md) — co-author.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — OFT is the custom-architecture-family exemplar; parallel decoding + L1 head.
- [Imitation learning](../concepts/learning/imitation-learning.md) — pure offline BC fine-tuning.
- [Knowledge Insulation](../concepts/learning/knowledge-insulation.md) — a contemporaneous PI recipe attacking the same "fine-tune a VLA well" problem from the flow-matching side; OFT is one of KI's baselines.

## Open questions

- OFT is an OpenVLA-specific fine-tuning study; how much transfers to other base VLAs is untested (the recipe is general, but only OpenVLA is evaluated).
- Parallel decoding is "theoretically less expressive" than autoregressive; the paper finds no degradation empirically but doesn't characterize where it might.

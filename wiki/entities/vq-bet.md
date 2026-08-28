---
title: VQ-BeT
type: entity
subtype: method
created: 2026-05-08
updated: 2026-07-04
sources: 14
tags: [vq-bet, behavior-cloning, transformer, vector-quantization, latent-action, lee-2024, icml-2024]
---

**VQ-BeT — Vector-Quantized Behavior Transformer.** Behavior-cloning method from NYU/Pinto lab; ICML 2024. Introduced in [Lee et al. 2024](../sources/vq-bet-paper.md) — *"Behavior Generation with Latent Actions"*. Discretizes the action space via a vector-quantization codebook, then trains a transformer to predict latent action codes autoregressively. **Direct successor to [BET](bet.md)** (Shafiullah, Cui, Altanzaya, Pinto, NeurIPS 2022) — VQ-BeT replaces BET's k-means action clustering with an end-to-end-learned vector-quantization codebook. The headline performer in the [Robot Utility Models paper](../sources/robot-utility-models-paper.md)'s ablation study, narrowly beating [Diffusion Policy](diffusion-policy.md) at full data scale.

## Approach (deepened 2026-07-04 from the [full paper](../sources/vq-bet-paper.md))
- **Residual VQ-VAE action tokenizer** — exactly **N_q = 2 residual layers** in all experiments: a **primary code** (coarse, dataset-wide clustering) + a **secondary code** (residual refinement). Codebooks of 8–16 codes per layer (64–256 combinations); latent dim 512; EMA codebook updates; trained first, then frozen.
- **MinGPT trunk** (6 layers / 6 heads / 120-dim; parameter count unpublished) predicts primary then secondary codes; **focal loss** on codes (secondary down-weighted, β≈0.1) + **L1 offset head** that restores full continuous fidelity on top of the decoded centroid.
- **Multi-modal action support** — the discrete codebook naturally captures multiple plausible action modes for the same observation, a known failure mode of plain regressive BC; measured via behavior entropy (best on 4/5 envs).
- **Mostly no action chunking** — chunking *hurt* where tried; the paper argues VQ-BeT is fast enough (3–18 ms/step) to run fully closed-loop even on a Stretch CPU. A standing counterpoint to the [Diffusion Policy](diffusion-policy.md)/ACT chunking orthodoxy.
- **Speed**: 5× faster inference than Diffusion Policy in sim; **25× on real robots** — because receding-horizon DP fails outright (0/30) on low-cost hardware and must run closed-loop ([paper](../sources/vq-bet-paper.md) Table 7/11).

## Performance characteristics in RUM
From [RUM paper](../sources/robot-utility-models-paper.md) §3.2:
- **Top performer at full data scale**: VQ-BeT ~76% vs Diffusion Policy ~71% across 5 tasks (raw success, no retrying).
- **Diffusion Policy wins at smaller data scale** (20–40% of full data); VQ-BeT pulls ahead at 80–100%.
- ACT and MLP-BC trail by ~10–15pt — supporting the RUM headline that "training data > training algorithm" within this performance band.
- VQ-BeT specifics in RUM: data subsampled to 3.75 Hz, 6 frames of history, predicts relative 6D end-effector pose + absolute gripper opening in `[0,1]`.

## Why it matters in this wiki
- **The empirical winner of RUM's policy-class shootout.** When RUM is cited as evidence for low-cost-zero-shot manipulation, VQ-BeT is the underlying method.
- **Author overlap with RUM**: Lee, Etukuru, Shafiullah, Pinto — Lee was a co-author on RUM and is first-author on VQ-BeT. The two papers are tightly linked NYU-line work.

## Related
- [BET](bet.md) — direct ancestor (NeurIPS 2022, same Pinto-lab line); k-means action discretization. VQ-BeT swaps k-means for an end-to-end-learned VQ codebook.
- [Robot Utility Models](robot-utility-models.md) — primary downstream consumer.
- [Diffusion Policy](diffusion-policy.md) — closest competitor; runner-up in the RUM ablation.
- [IBC](ibc.md) — earlier ancestor in the multi-modal-BC lineage (energy-based-model variant).
- [Lerrel Pinto](lerrel-pinto.md) — co-senior on RUM, co-author on VQ-BeT (NYU lab).
- [Mahi Shafiullah](mahi-shafiullah.md) — co-author on VQ-BeT, BET first author.
- [Imitation learning](../concepts/learning/imitation-learning.md) — broader concept.
- [Learned latent space](../concepts/world-models/latent-space.md) — VQ-BeT's discrete codebook is a learned latent *action* space; sibling design choice to predicting in continuous latent space.

## Mentioned in
- [VQ-BeT Paper](../sources/vq-bet-paper.md)
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md) — best-performing policy class.
- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — supported single-task BC policy alongside [ACT](act.md) and [Diffusion Policy](diffusion-policy.md); note that the paper omits VQ-BET from Figures 7a/7b upload/download tracking because users typically don't upload VQ-BET checkpoints.

## Open questions / TBD
- ~~Codebook size, transformer dimensions, hierarchy depth~~ — resolved 2026-07-04 from the full PDF (N_q=2 RVQ, 8–16 codes/layer, MinGPT 6/6/120); see [paper page](../sources/vq-bet-paper.md).
- ~~VQ-BeT vs Diffusion Policy outside RUM~~ — the paper's own head-to-head: SOTA 5/7 unconditional + 6/7 conditional benchmarks, plus 47/50 vs 45/50 single-phase and 19/30 vs 11/30 two-phase on real Stretch.
- Parameter count unpublished; training cost vs Diffusion Policy unreported.
- RL fine-tuning over the RVQ token space — natural follow-up the paper doesn't attempt.

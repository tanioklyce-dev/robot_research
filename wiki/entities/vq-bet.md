---
title: VQ-BeT
type: entity
subtype: method
created: 2026-05-08
updated: 2026-05-08
sources: 1
tags: [vq-bet, behavior-cloning, transformer, vector-quantization, latent-action, lee-2024]
status: stub
---

**VQ-BeT — Vector-Quantized Behavior Transformer.** Behavior-cloning method introduced in Lee et al. 2024 (*"Behavior Generation with Latent Actions"*). Discretizes the action space via a vector-quantization codebook, then trains a transformer to predict latent action codes autoregressively. The headline performer in the [Robot Utility Models paper](../sources/robot-utility-models-paper.md)'s ablation study, narrowly beating [Diffusion Policy](diffusion-policy.md) at full data scale.

## Approach
- **Vector quantization on actions.** Continuous action sequences are encoded into a discrete codebook; the policy emits codebook indices.
- **Transformer trunk** predicts next code given history of observations + previous actions.
- **Multi-modal action support** — the discrete codebook naturally captures multiple plausible action modes for the same observation, a known failure mode of plain regressive BC.

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
- [Robot Utility Models](robot-utility-models.md) — primary downstream consumer.
- [Diffusion Policy](diffusion-policy.md) — closest competitor; runner-up in the RUM ablation.
- [Lerrel Pinto](lerrel-pinto.md) — co-senior on RUM, co-author on VQ-BeT (NYU lab).
- [Imitation learning](../concepts/imitation-learning.md) — broader concept.

## Mentioned in
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md) — best-performing policy class.

## Open questions / TBD
- **Primary source not yet ingested.** VQ-BeT paper (Lee et al. 2024) deserves its own source page.
- How does VQ-BeT compare to Diffusion Policy outside the RUM ablation context — e.g. on industrial-grade benchmarks? Not documented here.
- Codebook size, transformer architecture details — RUM paper doesn't give them; primary source needed.

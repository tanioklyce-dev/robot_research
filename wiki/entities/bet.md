---
title: BET (Behavior Transformer)
type: entity
subtype: method
created: 2026-05-10
updated: 2026-05-15
sources: 7
tags: [bet, behavior-transformer, k-means-discretization, multi-modal-bc, transformer, shafiullah-2022, pinto-lab, nyu]
---

**BET — Behavior Transformer.** Behavior-cloning method that **discretizes the continuous action space via k-means clustering**, then trains a **transformer** to predict the cluster index plus a residual offset (offset prediction inspired by 2-stage object detectors). Introduced by Shafiullah, Cui, Altanzaya, Pinto (NYU, NeurIPS 2022, [arxiv 2206.11251](https://arxiv.org/abs/2206.11251)). Direct ancestor of [VQ-BeT](vq-bet.md), which replaces k-means with end-to-end vector-quantization. NYU/Pinto-lab work.

## Approach

- **k-means clustering of demo actions** → discrete action codebook of `k` centroids.
- **Transformer trunk** predicts `(cluster index, offset)` given observation history.
- **Multi-mode by index selection**: the transformer can output different cluster indices for similar contexts → captures multi-modal demonstration data without averaging.
- **Hyperparameter `k`** (number of clusters) must be specified per task; later addressed by [VQ-BeT](vq-bet.md)'s learned codebook.

## Key claims (from [BET Paper](../sources/bet-paper.md))

- Action discretization + multi-task action correction enables **multi-modal continuous-action prediction from unlabeled demonstration data**.
- Improves over prior BC methods on robotic manipulation and self-driving behavior datasets.

## Performance in [Diffusion Policy](diffusion-policy.md) ablation

From [Diffusion Policy Paper](../sources/diffusion-policy-paper.md) Tables I, IV:

- **Saturates RoboMimic Lift / Can** (~1.00) — strong on simpler tasks.
- **Strong on BlockPush** (`p1=0.96 / p2=0.71`) — likely BET's home benchmark.
- **Weak on harder RoboMimic** — Transport ph 0.38 / mh 0.21; ToolHang 0.58.
- **Weak on Franka Kitchen multi-stage** (`p4=0.44`) — Diffusion Policy hits 0.99.

## Why it matters in this wiki

- **Direct ancestor of [VQ-BeT](vq-bet.md)** — VQ-BeT swaps k-means for a learned vector-quantization codebook trained end-to-end. Same architecture template, learned discretization.
- **Pinto-line lineage marker** — NYU/Pinto lab's robot foundation-model line: BET → VQ-BeT → [DINO-WM](dino-wm.md) → [Robot Utility Models](robot-utility-models.md) → [OK-Robot](ok-robot.md). Many shared authors (Shafiullah, Pinto).
- **Standard baseline** — referenced across [Diffusion Policy Paper](../sources/diffusion-policy-paper.md), [Robot Utility Models Paper](../sources/robot-utility-models-paper.md), and downstream BC work.
- **Defines "multi-modal BC" as a problem statement** — the framing of BC failure on multi-modal demonstrations as a discretization / expressive-policy-class problem traces here.

## Related

- [VQ-BeT](vq-bet.md) — direct successor; replaces k-means with learned VQ codebook.
- [Diffusion Policy](diffusion-policy.md) — alternative solution to multi-modal BC via diffusion rather than discretization.
- [IBC](ibc.md) — earlier ancestor in the multi-modal-BC line via energy-based models.
- [Mahi Shafiullah](mahi-shafiullah.md) — first author.
- [Lerrel Pinto](lerrel-pinto.md) — senior author (NYU Pinto lab).
- [Imitation learning](../concepts/learning/imitation-learning.md) — broader concept.
- [Learned latent space](../concepts/world-models/latent-space.md) — k-means clustering as a frozen-discrete latent action space; sibling to VQ-BeT's end-to-end variant.

## Mentioned in

- [BET Paper](../sources/bet-paper.md) — primary source.
- [Diffusion Policy Paper](../sources/diffusion-policy-paper.md) — baseline in 12-task ablation.

## Open questions / TBD

- **Full paper not yet ingested** — abstract-level only.
- **Self-driving evaluation** — abstract mentions self-driving datasets; details unknown.
- **Choice of k per task** — methodology not in abstract.

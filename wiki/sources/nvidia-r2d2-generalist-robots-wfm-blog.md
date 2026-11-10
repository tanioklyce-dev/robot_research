---
title: "R²D²: Training Generalist Robots with NVIDIA Research Workflows and World Foundation Models"
type: source
url: https://developer.nvidia.com/blog/r2d2-training-generalist-robots-with-nvidia-research-workflows-and-world-foundation-models/
author: "Seun Doherty (NVIDIA)"
published: 2025-07-16
format: vendor technical blog post (R²D² series)
tags: [nvidia, nvidia-research, r2d2, dreamgen, gr00t-dreams, gr00t-n1, gr00t-n1-5, lapa, co-training, cosmos, synthetic-data, world-foundation-models]
ingested: 2026-11-10
---

# R²D²: Training Generalist Robots with NVIDIA Research Workflows and World Foundation Models

## Summary

How NVIDIA uses video world models and mixed data to train generalist policies: [DreamGen](../entities/dreamgen.md) and the GR00T-Dreams blueprint built on it, [GR00T N1 and N1.5](../entities/nvidia-groot.md), latent action pretraining (LAPA), and sim-and-real co-training.

> [!note] Secondary for the research it covers
> This post summarises NVIDIA papers. Its figures weren't checked against those papers at ingest. The arXiv IDs listed are the primaries to ingest before any number here feeds a decision.

## Key claims

- **[DreamGen](dreamgen-paper.md).** Post-train a video model such as Cosmos-Predict2 on the target robot, generate videos of new tasks, label them with pseudo-actions from a latent action or inverse dynamics model, then train a policy. It is the basis of the **Isaac GR00T-Dreams** blueprint.
- **DreamGen Bench.** Scores video models on instruction following and physics following, testing Cosmos, WAN 2.1, Hunyuan and CogVideoX. **Higher bench scores are said to go with better real-robot results** from the resulting data.
- **GR00T N1.5 in 36 hours.** NVIDIA says GR00T-Dreams data let it develop GR00T N1.5 in 36 hours, against nearly three months by manual collection. No breakdown is given.
- **LAPA.** Learns discrete latent actions from over 181,000 unlabelled internet videos with a VQ-VAE, pretrains a VLM to predict them, then maps them to robot actions with a small labelled set. It reports a 6.22% gain on real tasks and over 30× pretraining efficiency. arXiv 2410.11758.
- **Sim-and-real co-training.** Mixes real demonstrations with task-matched and task-agnostic simulation data, prioritising camera alignment and diversity over photorealism. With 400 real demonstrations, co-training beats real-only by **38% on average**. arXiv 2503.24361.
- **Adopters named.** AeiRobot, Foxlink, Lightwheel and NEURA Robotics.

## Entities mentioned

- [DreamGen](../entities/dreamgen.md), [NVIDIA GR00T](../entities/nvidia-groot.md), [NVIDIA Cosmos](../entities/nvidia-cosmos.md), [NVIDIA GEAR](../entities/nvidia-gear.md)

## Concepts touched

- [Synthetic data flywheel](../concepts/learning/synthetic-data-flywheel.md) — world-model-generated trajectories.
- [Latent action tokens](../concepts/learning/latent-action-tokens.md) — LAPA.

## Open questions

- **Is the 38% relative or in percentage points,** and across which tasks? The co-training paper should say.
- **What did the 36 hours include?** Data generation, training and evaluation would each change what the comparison means.

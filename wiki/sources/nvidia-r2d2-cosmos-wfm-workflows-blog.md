---
title: "R²D²: Boost Robot Training with World Foundation Models and Workflows from NVIDIA Research"
type: source
url: https://developer.nvidia.com/blog/r2d2-boost-robot-training-with-world-foundation-models-and-workflows-from-nvidia-research/
author: "Asawaree Bhide (NVIDIA)"
published: 2025-08-08
format: vendor technical blog post (R²D² series)
tags: [nvidia, nvidia-research, r2d2, cosmos, cosmos-predict, cosmos-transfer, cosmos-reason, gr00t-dreams, cosmos-drive-dreams, diffusionrenderer, natten, distillation, synthetic-data]
ingested: 2026-11-10
---

# R²D²: Boost Robot Training with World Foundation Models and Workflows from NVIDIA Research

## Summary

A tour of the 2025 [Cosmos](../entities/nvidia-cosmos.md) line, predating Cosmos 3: Predict generates future video, Transfer generates video under control inputs such as depth or segmentation, and Reason is a vision-language model used to filter data. It includes example commands for several post-trained variants.

> [!note] Secondary for the research it covers
> This post summarises NVIDIA papers. Its figures weren't checked against those papers at ingest. The arXiv IDs listed are the primaries to ingest before any number here feeds a decision.

## Key claims

- **Cosmos Predict variants.** Single2MultiView generates several driving camera views from one. Cosmos-Drive-Dreams generates hard driving conditions. GR00T-Dreams generates robot task videos ([DreamGen](../entities/dreamgen.md)). DiffusionRenderer relights scenes and edits materials from one video.
- **Faster generation.** Cosmos-Predict2 uses Neighborhood Attention (NATTEN), giving **2–2.5× faster video inference on H100 and B200**.
- **Transfer distillation.** Cosmos Transfer took 70 passes to generate a video. A distilled edge-conditioned model does it **in one step at close to the original quality**, with other conditions said to be distillable the same way.
- **Cosmos Reason.** Trained with supervised fine-tuning and then RL. It serves as a critic on generated data, and the post says it can be post-trained into a VLA.

## Entities mentioned

- [NVIDIA Cosmos](../entities/nvidia-cosmos.md), [DreamGen](../entities/dreamgen.md)

## Concepts touched

- [Synthetic data flywheel](../concepts/learning/synthetic-data-flywheel.md) — generation plus a model critic.

## Open questions

- **What quality metric supports "closely matching"** the 70-pass model? The post gives none.

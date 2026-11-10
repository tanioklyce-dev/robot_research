---
title: "R²D²: Improving Robot Manipulation with Simulation and Language Models"
type: source
url: https://developer.nvidia.com/blog/r2d2-improving-robot-manipulation-with-simulation-and-language-models/
author: "Asawaree Bhide (NVIDIA)"
published: 2025-12-12
format: vendor technical blog post (R²D² series)
tags: [nvidia, nvidia-research, r2d2, thinkact, co-training, optimal-transport, robotsmith, tool-design, cosmos-cookbook, neurips-2025]
ingested: 2026-11-10
---

# R²D²: Improving Robot Manipulation with Simulation and Language Models

## Summary

Three NeurIPS 2025 papers, ThinkAct, an optimal-transport version of sim-and-real co-training, and RobotSmith, plus a pointer to the Cosmos Cookbook. **The post gives no performance numbers** for any of them.

> [!note] Secondary for the research it covers
> This post summarises NVIDIA papers. Its figures weren't checked against those papers at ingest. The arXiv IDs listed are the primaries to ingest before any number here feeds a decision.

## Key claims

- **ThinkAct.** A multimodal LLM trained with RL on visual rewards writes plans, which are compressed into a latent trajectory that guides a separate action model. It claims few-shot adaptation, long-horizon manipulation and self-correction. arXiv 2507.16815.
- **Generalisable domain adaptation for co-training.** Extends sim-and-real co-training by aligning simulated and real observations, with their actions, in a shared latent space using unbalanced optimal transport, to cope with far more simulated than real data. It reports real-world generalisation to situations that appeared only in simulated data. arXiv 2509.18631.
- **RobotSmith.** Two VLM agents propose tool shapes, a planner proposes how to use them, and tool shape and trajectory are optimised together in simulation. A real pancake-making test used separate designed tools for flattening, scooping and spreading. arXiv 2506.14763.
- **Cosmos Cookbook.** Open recipes for [Cosmos](../entities/nvidia-cosmos.md), including using Cosmos Transfer to diversify simulated robot data.

## Entities mentioned

- [NVIDIA Cosmos](../entities/nvidia-cosmos.md)

## Concepts touched

- [Dexterous tool manipulation](../concepts/robotics/dexterous-tool-manipulation.md) — RobotSmith designs the tool itself.

## Open questions

- **All results are in the papers.** None of the three claims can be weighed from this post.

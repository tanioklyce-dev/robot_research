---
title: "R²D²: Advancing Robot Mobility and Whole-Body Control with Novel Workflows and AI Foundation Models from NVIDIA Research"
type: source
url: https://developer.nvidia.com/blog/r2d2-advancing-robot-mobility-whole-body-control-with-ai-from-nvidia-research/
author: "Asawaree Bhide, Yan Chang, Kalyan Meher Vadrevu, Mihir Acharya (NVIDIA)"
published: 2025-03-27
format: vendor technical blog post (R²D² series)
tags: [nvidia, nvidia-research, r2d2, mobilitygen, compass, x-mobility, hover, remembr, navigation, whole-body-control, cross-embodiment]
ingested: 2026-11-10
---

# R²D²: Advancing Robot Mobility and Whole-Body Control with Novel Workflows and AI Foundation Models from NVIDIA Research

## Summary

The first edition of the series. It presents four workflows as layers of one mobility stack: MobilityGen generates data, COMPASS and HOVER handle movement and control, and ReMEmbR adds memory and question answering.

> [!note] Secondary for the research it covers
> This post summarises NVIDIA papers. Its figures weren't checked against those papers at ingest. The arXiv IDs listed are the primaries to ingest before any number here feeds a decision.

## Key claims

- **MobilityGen.** Generates synthetic motion data in [Isaac Sim](../entities/nvidia-isaac-sim.md) for wheeled, legged and humanoid robots. Outputs include occupancy maps, poses, velocities, RGB, depth and segmentation, collected by teleoperation, random actions or path planning.
- **COMPASS.** Three stages: imitation learning with the X-Mobility model, residual RL per robot in [Isaac Lab](../entities/nvidia-isaac-lab.md), then distillation of the specialists into one policy. The post claims **5× higher success across embodiments** than the single-robot X-Mobility policy, without stating the base rate. arXiv 2502.16372.
- **[HOVER](hover-paper.md).** One whole-body humanoid policy distilled from an RL oracle that imitates human motion, covering several control modes. It includes deployment code for the Unitree H1. arXiv 2410.21229.
- **ReMEmbR.** Long-horizon memory for navigation using LLMs, VLMs and retrieval, plus the NaVQA question-answering dataset. arXiv 2409.13682.
- **Adopters named.** Under Control Robotics uses X-Mobility on its Moby robot. Advantech, with ADATA and Ubitus, uses ReMEmbR.

## Entities mentioned

- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md), [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md)

## Concepts touched

- [Visual navigation policies](../concepts/robotics/visual-navigation-policies.md) — COMPASS and X-Mobility.
- [Whole-body control](../concepts/robotics/whole-body-control.md) — HOVER.
- [Cross-embodiment transfer](../concepts/learning/cross-embodiment.md) — distilling per-robot specialists into one policy.

## Open questions

- **5× higher than what?** The base success rate and test set are in the COMPASS paper, not the post.

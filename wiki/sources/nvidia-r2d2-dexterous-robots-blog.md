---
title: "R²D²: Adapting Dexterous Robots with NVIDIA Research Workflows and Models"
type: source
url: https://developer.nvidia.com/blog/r2d2-adapting-dexterous-robots-with-nvidia-research-workflows-and-models/
author: "Asawaree Bhide, Yichao Pan, Nathan Ratliff (NVIDIA)"
published: 2025-04-25
format: vendor technical blog post (R²D² series)
tags: [nvidia, nvidia-research, r2d2, dextrah-rgb, dexmimicgen, skillmimicgen, graspgen, dexterous-manipulation, data-generation, grasping, atlas]
ingested: 2026-11-10
---

# R²D²: Adapting Dexterous Robots with NVIDIA Research Workflows and Models

## Summary

Four manipulation projects: DextrAH-RGB for dexterous grasping from stereo RGB, DexMimicGen and SkillMimicGen for multiplying a few human demonstrations into large datasets, and [GraspGen](../entities/graspgen.md) for grasp generation across grippers.

> [!note] Secondary for the research it covers
> This post summarises NVIDIA papers. Its figures weren't checked against those papers at ingest. The arXiv IDs listed are the primaries to ingest before any number here feeds a decision.

## Key claims

- **DextrAH-RGB.** An RL teacher with privileged state acts through geometric fabrics, a control layer that builds in collision avoidance. It is distilled with DAgger into a stereo-RGB student using tiled rendering in [Isaac Lab](../entities/nvidia-isaac-lab.md). It is deployed zero-shot on the upper body of Boston Dynamics' [Atlas](../entities/atlas.md), with failure detection and retrying described as emergent. arXiv 2412.01791.
- **DexMimicGen.** Bimanual data generation that splits subtasks into parallel, coordinated and sequential types. The paper generated **21K demonstrations from 60 human ones**. A real humanoid reached **90% on can sorting with generated data, against 0% with human data alone**. arXiv 2410.24185. See [MimicGen](../entities/mimicgen.md).
- **SkillMimicGen (SkillGen).** From about three annotated demonstrations, it adapts contact-rich skill segments to new scenes and links them with motion planning. It reached **35% zero-shot sim-to-real on a two-nut assembly task**. arXiv 2410.18907.
- **[GraspGen](../entities/graspgen.md).** A diffusion-transformer grasp generator with a discriminator trained on the generator's own outputs. It achieved **81.3% real-world grasp success** on a UR10 with a Robotiq gripper, across table, basket and shelf scenes. Its simulated dataset has **57 million grasps** for a Franka gripper, a Robotiq 2F-140 and a suction cup. arXiv 2507.13097.

## Entities mentioned

- [GraspGen](../entities/graspgen.md), [MimicGen](../entities/mimicgen.md), [Atlas](../entities/atlas.md), [Boston Dynamics](../entities/boston-dynamics.md), [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md)

## Concepts touched

- [6-DoF grasp generation](../concepts/robotics/six-dof-grasp-generation.md) — GraspGen.
- [Synthetic data flywheel](../concepts/learning/synthetic-data-flywheel.md) — demonstration multiplication.

## Open questions

- **What does the 0% baseline mean?** The human-only can-sorting policy was presumably trained on far fewer demonstrations, so the comparison mixes data quantity with data source.

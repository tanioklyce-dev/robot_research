---
title: "R²D²: Three Neural Breakthroughs Transforming Robot Learning from NVIDIA Research"
type: source
url: https://developer.nvidia.com/blog/r2d2-three-neural-breakthroughs-transforming-robot-learning-from-nvidia-research/
author: "Rishabh Chadha, Yashraj Narang, Jie Xu, Wei Yang, Yu-Wei Chao (NVIDIA)"
published: 2025-09-25
format: vendor technical blog post (R²D² series)
tags: [nvidia, nvidia-research, r2d2, nerd, neural-simulation, dexplore, vt-refine, tactile, bimanual-assembly, real-to-sim-to-real, corl-2025]
ingested: 2026-11-10
---

# R²D²: Three Neural Breakthroughs Transforming Robot Learning from NVIDIA Research

## Summary

Three CoRL 2025 papers: NeRD, a learned dynamics model that replaces part of a physics simulator; Dexplore, which learns dexterous control from motion-capture data; and VT-Refine, which fine-tunes a visuo-tactile assembly policy in simulation.

> [!note] Secondary for the research it covers
> This post summarises NVIDIA papers. Its figures weren't checked against those papers at ingest. The arXiv IDs listed are the primaries to ingest before any number here feeds a decision.

## Key claims

- **NeRD (Neural Robot Dynamics).** A small GPT-2-style transformer replaces the low-level dynamics and contact solver, using a robot-centred state for spatial invariance. Each robot's model trains on 100,000 random trajectories of 100 steps. It is reported **within 0.1% of accumulated reward over a 1,000-step ANYmal policy evaluation**, with zero-shot transfer of a Franka reaching policy. It runs in Warp and is planned as a future solver in [Newton](../entities/newton-physics-engine.md). arXiv 2508.15755.
- **Dexplore.** Treats motion-capture demonstrations as soft guidance, combining retargeting and tracking in one optimisation, then distils a vision-based generative policy that works from a single depth view. It reports almost 20% higher success on the Inspire hand and beats baselines on the Allegro hand. arXiv 2509.09671.
- **VT-Refine.** Pretrains a bimanual visuo-tactile diffusion policy on about 30 real demonstrations, then fine-tunes it with RL in a digital twin using TacSL in [Isaac Lab](../entities/nvidia-isaac-lab.md). Real success rises **about 20% for vision only and 40% for vision plus touch**, with a 5–10% loss in transfer. arXiv 2510.14930.

## Entities mentioned

- [Newton](../entities/newton-physics-engine.md), [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md)

## Concepts touched

- [Tactile sensing](../concepts/robotics/tactile-sensing.md) — touch adds about twice the gain of vision alone in VT-Refine.
- [Real-to-sim-to-real](../concepts/robotics/real-to-sim-to-real.md) — VT-Refine's loop.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — NeRD as a learned simulator component.

## Open questions

- **Has NeRD shipped in Newton?** The post said *"at some point in the future."*

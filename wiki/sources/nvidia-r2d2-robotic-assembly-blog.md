---
title: "R²D²: Unlocking Robotic Assembly and Contact Rich Manipulation with NVIDIA Research"
type: source
url: https://developer.nvidia.com/blog/r2d2-unlocking-robotic-assembly-and-contact-rich-manipulation-with-nvidia-research/
author: "Oyindamola Omotuyi, Yashraj Narang, Iretiayo Akinola (NVIDIA)"
published: 2025-05-16
format: vendor technical blog post (R²D² series)
tags: [nvidia, nvidia-research, r2d2, assembly, contact-rich-manipulation, factory, industreal, automate, matchmaker, srsa, tacsl, forge, sim-to-real, tactile]
ingested: 2026-11-10
---

# R²D²: Unlocking Robotic Assembly and Contact Rich Manipulation with NVIDIA Research

## Summary

NVIDIA's simulation-to-real assembly line of work in one place: the Factory simulator, the IndustReal and AutoMate policy toolkits, and four follow-ups covering asset generation, skill retrieval, tactile simulation and force-based policies. It is the background to the [GB300 assembly case study](nvidia-r2d2-gb300-tester-tray-assembly-blog.md) by the same group.

> [!note] Secondary for the research it covers
> This post summarises NVIDIA papers. Its figures weren't checked against those papers at ingest. The arXiv IDs listed are the primaries to ingest before any number here feeds a decision.

## Key claims

| Project | What it adds | Headline figure in the post | arXiv |
|---|---|---|---|
| Factory | GPU contact simulation with SDF collisions and a Gauss-Seidel solver, now in [Isaac Lab](../entities/nvidia-isaac-lab.md) | — | 2205.03532 |
| IndustReal | Algorithms for sim-to-real RL on assembly | 83–99% success over 600 real trials, Franka and UR10e | 2305.17110 |
| AutoMate | Specialist and generalist assembly policies from RL plus imitation, 100 assets | About 80% for specialists on about 80 tasks and a generalist on 20, zero-shot real | 2407.08028 |
| MatchMaker | Generates mating, simulation-ready part pairs, with GPT-4o detecting contact faces | Validated in sim and real, no figure given | 2503.05887 |
| SRSA | Retrieves and fine-tunes the most suitable existing skill | 19% higher success, 2.4× fewer samples, 90% mean real success | 2503.04538 |
| TacSL | GPU simulation of visuotactile images and force fields | Over 200× faster than prior work, 83–91% sim-to-real | 2408.04587 |
| FORGE | RL policies with force input and force limits | Tolerates up to 5 mm of pose error on a planetary-gearbox assembly | 2408.06506 |

AutoMate was evaluated with over 5 million simulated trials and 500 real ones. The post says real performance sometimes exceeded simulated.

## Entities mentioned

- [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md), [Franka Panda](../entities/franka-panda.md)

## Concepts touched

- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) — the simulation-first assembly line.
- [Tactile sensing](../concepts/robotics/tactile-sensing.md) — TacSL.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — zero-shot transfer for contact-rich tasks.

## Open questions

- **What does "19% higher success" mean for SRSA?** The post doesn't say whether it is relative or in percentage points.

---
title: RoboLab (NVIDIA SRL benchmark)
type: entity
subtype: benchmark
created: 2026-07-16
updated: 2026-07-16
sources: 1
tags: [nvidia, srl, benchmark, evaluation, simulation, task-generalist, robot-policy, droid, physical-ai]
---

# RoboLab (NVIDIA SRL benchmark)

**RoboLab** — a **robot- and policy-agnostic simulation benchmarking platform** from NVIDIA Research's **Seattle Robotics Lab (SRL)** for evaluating **real-world task-generalist robot policies** in simulation. Presented at **RSS 2026** (arXiv 2604.09860).

## What it is

Users generate scenes and tasks **from language instructions** (with support for AI agentic scene/task authoring), then score real-world-trained policies (DROID-style) directly in sim. The language-driven generation is designed to **resist benchmark saturation** — the benchmark can keep growing.

- **RoboLab-120 suite**: 120 tasks, avg **2.02 subtasks/task**, avg **9 objects/scene**, **68.7% object-vocab overlap with DROID**.
- **Evaluation axes**: visual, relational, procedural competencies; emphasis on **multi-step** tasks.
- **Authors** (NVIDIA Research): Xuning Yang, Rishit Dagli, Alex Zook, Hugo Hadfield, Ankit Goyal, Stan Birchfield, Fabio Ramos, Jonathan Tremblay.

## Why it matters

RoboLab was **already a live reference in this wiki** before it had a page: the [NVIDIA Cosmos](nvidia-cosmos.md) entity cites **Cosmos3-Nano-Policy-DROID beating π0.5 on RoboLab-120 (39.7% vs 28.1%)**. It's the sim yardstick NVIDIA uses to score its own DROID-trained policies, and a direct entry against the wiki's flagged **evaluation-methodology gap** (alongside RoboArena, rliable, robomimic). Complements the *real-world* [RoboArena](nvidia-cosmos.md) leaderboard and the household benchmarks [RoboCasa365](../sources/robocasa365-paper.md) / [BEHAVIOR-1K](behavior-benchmark.md).

## Mentioned in

- [RoboLab project page](../sources/nvidia-robolab-project.md) (RSS 2026)
- [NVIDIA Cosmos](nvidia-cosmos.md) — evaluated Cosmos 3 policies on RoboLab-120

## Related

- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — RoboLab runs the *real-to-sim eval* direction
- [VLA models](../concepts/learning/vla-models.md) — the policies under test
- [NVIDIA](nvidia.md) — SRL is part of NVIDIA Research

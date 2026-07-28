---
title: "RoboLab — a robot- and policy-agnostic simulation benchmark for task-generalist policies (NVIDIA SRL)"
type: source
url: https://research.nvidia.com/labs/srl/projects/robolab/
author: Xuning Yang, Rishit Dagli, Alex Zook, Hugo Hadfield, Ankit Goyal, Stan Birchfield, Fabio Ramos, Jonathan Tremblay (NVIDIA Research)
published: 2026 (RSS 2026)
ingested: 2026-07-16
venue: RSS 2026 (Sydney)
paper: https://arxiv.org/abs/2604.09860
tags: [nvidia, srl, benchmark, evaluation, simulation, task-generalist, robot-policy, droid, scene-generation, physical-ai]
---

## Summary

**RoboLab** is a **robot- and policy-agnostic simulation benchmarking platform** for evaluating **real-world task-generalist robot policies** — i.e. policies trained on real data (e.g. DROID-style) evaluated *directly in simulation* without robot-specific retraining. Its pitch addresses the wiki's recurring **evaluation-methodology gap**: robot-learning evals are usually small, fixed, and quickly saturated. RoboLab instead **generates scenes and tasks from language instructions** (fast enough to keep expanding the benchmark), and structures evaluation around **visual, relational, and procedural** competencies with an emphasis on **multi-step** tasks. From NVIDIA Research's **Seattle Robotics Lab (SRL)** — the `/labs/srl/` group behind the DROID/eval line (Birchfield, Ramos, Tremblay, Goyal). Presented at **RSS 2026**.

## Key claims

- **Definition**: "a robot- and policy-agnostic simulation benchmarking platform for evaluating real-world task-generalist robot policies."
- **Scene/task generation**: users arrange objects and specify tasks **via language instructions**; supports **AI agentic workflows** for automated scene/task creation → resists benchmark saturation.
- **Benchmark stats (the "RoboLab-120" suite)**: **120 tasks**, avg **2.02 subtasks/task**, avg **9 objects/scene**, **68.7% object-vocabulary overlap with the DROID dataset** — deliberately aligned to real-world-trained policies' training distribution.
- **Evaluation axes**: visual, relational, and procedural competencies; multi-step > single-step focus.
- **Authors** (all NVIDIA Research; Dagli @ U. Toronto, Ramos @ U. Sydney): Xuning Yang, Rishit Dagli, Alex Zook, Hugo Hadfield, Ankit Goyal, Stan Birchfield, Fabio Ramos, Jonathan Tremblay.
- **Paper**: arXiv 2604.09860; **RSS 2026** (Sydney).

## Cross-wiki connection

RoboLab is **already cited in this wiki** before having its own page: the [NVIDIA Cosmos](../entities/nvidia-cosmos.md) entity reports **Cosmos3-Nano-Policy-DROID beating π0.5 on RoboLab-120 (39.7% vs 28.1%)** ([Cosmos 3 technical report](cosmos-3-technical-report.md)). So RoboLab is the sim benchmark NVIDIA uses to score its own DROID-trained policies — this page closes that dangling reference.

## Entities mentioned

- [RoboLab](../entities/nvidia-robolab.md) — this benchmark
- [NVIDIA](../entities/nvidia.md); [NVIDIA Cosmos](../entities/nvidia-cosmos.md) (evaluated on RoboLab-120); [Physical Intelligence](../entities/physical-intelligence.md) (π0.5 baseline)

## Concepts touched

- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — RoboLab is the *real-to-sim eval* direction (score real-trained policies in sim)
- [VLA models](../concepts/learning/vla-models.md) — the policies under test

## Open questions

- What **simulator backend** does RoboLab use (Isaac Sim / MuJoCo / other)? The project page doesn't say.
- **Real-to-sim validity**: how well do RoboLab sim scores predict real-robot success? The whole premise depends on that correlation — not quantified on the page.
- ~~Relationship to **RoboArena**~~ — **answered 2026-07-27** by [ingesting it](roboarena-paper.md): they are the **two poles of the same problem**, not competitors. RoboLab is simulation + absolute success rates + more rollouts (≈1,030 for ±2 pp); [RoboArena](../entities/roboarena.md) is real-world + pairwise preference + Bradley-Terry, converging in ~100 comparisons and yielding **ordering without magnitude**. They share an author (**Xuning Yang**). Still open: relationship to [RoboCasa365](robocasa365-paper.md) / [BEHAVIOR-1K](behavior-1k-paper.md) in the crowded 2026 eval-benchmark field.

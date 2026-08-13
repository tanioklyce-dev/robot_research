---
title: RoboLab (NVIDIA SRL benchmark)
type: entity
subtype: benchmark
created: 2026-07-16
updated: 2026-07-27
sources: 3
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

RoboLab was **already a live reference in this wiki** before it had a page: the [NVIDIA Cosmos](nvidia-cosmos.md) entity cites **Cosmos3-Nano-Policy-DROID beating π0.5 on RoboLab-120 (39.7% vs 28.1%)**. It's the sim yardstick NVIDIA uses to score its own DROID-trained policies, and a direct entry against the wiki's flagged **evaluation-methodology gap** (alongside [RoboArena](roboarena.md), rliable, robomimic). Complements the *real-world* [RoboArena](roboarena.md) leaderboard and the household benchmarks [RoboCasa365](../sources/robocasa365-paper.md) / [BEHAVIOR-1K](behavior-benchmark.md).

## The evaluation methodology

The [methodology blog](../sources/nvidia-robolab-evaluation-blog.md) (Xuning Yang, 2026-07-11) is where RoboLab's actual argument lives — it names **four failure modes** in current robot benchmarking and builds against each:

1. **Visual domain overlap** (train/eval share visual sources → memorization; real2sim via Gaussian Splatting costs **>1 h/scene**) → agentic task authoring in **minutes**.
2. **Saturation** (>90% success on fixed suites) → language-driven, growable task generation.
3. **Diagnostic gap** (binary success/failure) → graded scores, **SPARC** trajectory smoothness, end-effector velocity, frame-level failure-event logs (wrong-object grasp, drop, gripper collision).
4. **Statistical untrustworthiness** → **Clopper-Pearson** exact intervals show a ±2 pp band needs ≈**1,030 rollouts** vs the ~**70** typically published — **~15×**.

Also: **Neural Posterior Estimation** for sensitivity analysis (`p(θ|x)` over environment variables) without exhaustive ablation, and a three-way **language-complexity** axis (vague / default / specific) where *vague instructions consistently fail*.

**The headline empirical finding:** across the policies tested, **no policy could perform more than four complex subtasks successfully** — a long-horizon ceiling that the ~97% [LIBERO](libero.md) scores elsewhere in this wiki completely hide.

**Productization:** RoboLab's features are being folded into **[Isaac Lab-Arena](nvidia-isaac-lab.md)**, stated for **August 2026**.

## Mentioned in

- [RoboLab project page](../sources/nvidia-robolab-project.md) (RSS 2026)
- [How to Evaluate General-Purpose Robot Policies for Real-World Deployment](../sources/nvidia-robolab-evaluation-blog.md) — the methodology blog (2026-07-11)
- [NVIDIA Cosmos](nvidia-cosmos.md) — evaluated Cosmos 3 policies on RoboLab-120

## Related

- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — **the concept page this benchmark anchors**; the sample-size critique applies to most success rates in this wiki

- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — RoboLab runs the *real-to-sim eval* direction
- [VLA models](../concepts/learning/vla-models.md) — the policies under test
- [NVIDIA](nvidia.md) — SRL is part of NVIDIA Research

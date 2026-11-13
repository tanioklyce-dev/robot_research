---
title: RoboLab (NVIDIA SRL benchmark)
type: entity
subtype: benchmark
created: 2026-07-16
updated: 2026-11-12
sources: 11
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

**Productization:** RoboLab's features are being folded into **[Isaac Lab-Arena](isaac-lab-arena.md)**, stated for **August 2026** — and **delivered in Arena v0.3.0 (September 2026)** as the RoboLab task catalog (38 of the 120 tasks so far) plus the `sbi` sensitivity-analysis toolbox ([Arena GitHub](../sources/isaaclab-arena-github.md)). The RoboLab-120 subtask distribution, from that catalog: 53 tasks with one subtask, 41 with two, 17 with three, 9 with four to eleven.

## Scores held here

| Policy | RoboLab-120 | Instruction level | Source |
|---|---|---|---|
| Cosmos3-Nano-Policy-DROID (16B) | **39.7%** | specific | [Cosmos 3 tech report](../sources/cosmos-3-technical-report.md), Table 19 |
| π0.5 | 28.1% | specific | same |
| Cosmos3-Nano | **36.8%** | unstated | [Edge post-training tutorial](../sources/nvidia-cosmos3-edge-post-training-blog.md), 2026-08-19 |
| **Cosmos3-Edge-Policy-DROID (4B)** | **22.9%** | unstated | same — first published Edge score |
| GPT-6 Astra, agentic (Codex) | **74.8%** | default | [Astranomy](../sources/nvidia-srl-astranomy-blog.md), 5 episodes per task |
| GPT-6 Astra, direct API | 66.3% | default | same |
| Lakeside (best leaderboard entry cited there) | 51.0% | — | same |
| AMP1 (zero-shot frontier-model agent) | **86.0%** | official (10/task) | [Praxis-1 report](../sources/runway-praxis-1-technical-report.md), leaderboard as of 2026-11 |
| SenseNova-RoboRSI (VLM as policy) | 57.1% | official | same |
| BiMind v0.5 (closed; fine-tuned on RoboLab data) | 49.2% | official | same |
| **Praxis-1 (DROID FT)** | **46.2%** (555/1,200) | official | same |
| FLUX 3 Action | 42.9% | official | same |
| Atomic-WAM / OASIS WAM | 39.6% / 39.0% | official | same |
| DreamZero | 25.7% | official | same |
| GR00T N1.6 | 7.3% | official | same |

No rollouts-per-task for any row, which by this page's own methodology (±2 pp ≈ 1,030 rollouts) means the 36.8-vs-39.7 Nano gap is noise-sized and the 16B→4B drop (~14 pp) is the only difference here large enough to trust in direction.

## The leaderboard in November 2026

The [Praxis-1 report](../sources/runway-praxis-1-technical-report.md) gives the first full slice of the public board in this wiki, with the **official protocol of 10 trials per task (1,200 episodes)**. At that size a score near 45% has a standard error of about ±1.4 pp, or ±2.8 pp at 95%. Two patterns stand out. **The top two entries are frontier-model agents**, not trained policies (AMP1 86.0%, SenseNova-RoboRSI 57.1%). **WAMs now fill most of the open-model tier** (Praxis-1, FLUX 3 Action, Atomic-WAM, OASIS WAM, Cosmos 3 Nano), above the open VLAs. BiMind v0.5 is listed as fine-tuned on RoboLab data. The board does not separate in-domain fine-tunes from held-out ones, and the reader should.

> [!note] π0.5 at 28.0% vs 28.1%
> The leaderboard figure (28.0%, also quoted by [Astranomy](../sources/nvidia-srl-astranomy-blog.md)) differs from the Cosmos 3 report's 28.1% under specific instructions. These are probably different runs or instruction levels, and the difference is immaterial.

## Mentioned in

- [Isaac Lab-Arena GitHub](../sources/isaaclab-arena-github.md) — **the productization, delivered**: Arena v0.3 ships a RoboLab catalog of 38 task specs over 17 scenes mapped against the 120 RoboLab tasks (prompt-generated, DROID embodiment), experiment configs for π0 and Cosmos on 2/18/20 tasks, and the NPE/MNPE sensitivity analysis as an `sbi`-backed toolbox; Fabio Ramos and Xuning Yang are listed contributors.
- [RoboLab project page](../sources/nvidia-robolab-project.md) (RSS 2026)
- [How to Evaluate General-Purpose Robot Policies for Real-World Deployment](../sources/nvidia-robolab-evaluation-blog.md) — the methodology blog (2026-07-11)
- [NVIDIA Cosmos](nvidia-cosmos.md) — evaluated Cosmos 3 policies on RoboLab-120
- [Post-train Cosmos 3 Edge for on-device robot control](../sources/nvidia-cosmos3-edge-post-training-blog.md) — RoboLab as the closed-loop evaluation for the Edge policy (22.9%; Nano 36.8%); the run commands.
- [Astranomy (NVIDIA SRL)](../sources/nvidia-srl-astranomy-blog.md) — GPT-6 Astra at 74.8% with no robot training; the benchmark authors ran it.

## Related

- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — **the concept page this benchmark anchors**; the sample-size critique applies to most success rates in this wiki

- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — RoboLab runs the *real-to-sim eval* direction
- [VLA models](../concepts/learning/vla-models.md) — the policies under test
- [NVIDIA](nvidia.md) — SRL is part of NVIDIA Research
- [Praxis-1 technical report](../sources/runway-praxis-1-technical-report.md) — the November 2026 leaderboard slice under the 10-trial official protocol; Praxis-1 46.2% as best WAM / open model; compute-scaling curve measured on RoboLab-120.

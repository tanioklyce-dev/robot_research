---
title: "RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation (Wu, Hou, Liu, Che, Ju et al., Dec 2024)"
type: source
url: https://arxiv.org/abs/2412.13877
local_path: raw/2412.13877-robomind.pdf
author: "Kun Wu*, Chengkai Hou*, Jiaming Liu*, Zhengping Che*†, Xiaozhu Ju*†, Zhuqin Yang, Meng Li, Yinuo Zhao, Zhiyuan Xu, … Shanghang Zhang‡, Jian Tang‡"
affiliations: Beijing Innovation Center of Humanoid Robotics (X-Humanoid); Peking University
published: 2024-12-18
ingested: 2026-08-13
tags: [robomind, dataset, teleoperation, multi-embodiment, franka, ur5e, agilex, tien-kung, humanoid, dexterous-hand, failure-data, digital-twin, isaac-sim, primary-source]
---

## Summary

**RoboMIND** (Multi-embodiment Intelligence Normative Data) is a **107,000-trajectory / 305.5-hour real-robot teleoperation dataset** covering **479 tasks and 96 object classes** across **four embodiments** collected on a *single unified platform with a standardized protocol* — the design choice that distinguishes it from [Open X-Embodiment](../entities/open-x-embodiment.md), which aggregates data from many labs with differing standards.

The wiki has been citing it secondhand for months: **RoboMIND is 19.9% of [X-VLA](../entities/x-vla.md)'s pretraining mixture** (as `RoboMind-Franka`, `-UR`, `-Agilex`, `-Dual-Franka`), and RoboTwin 2.0 lists it among the real-world corpora bridging sim-to-real. Reading it surfaces two things worth having, one of them a structural point about action-space design that lands directly on today's other ingests.

Two components no comparable dataset ships: **5,000 real-world failure trajectories with annotated causes**, and a **digital twin of the real tasks and assets in [Isaac Sim](../entities/nvidia-isaac-sim.md)**.

## Composition

| Embodiment | Trajectories | Notes |
|---|---:|---|
| [Franka Emika Panda](../entities/franka-panda.md) | 26,856 | single-arm |
| UR5e | 25,170 | single-arm |
| **X-Humanoid Tien Kung** | 15,187 | **humanoid with dual dexterous hands** |
| AgileX Cobot Magic V2.0 | 10,269 | dual-arm ([AgileX](../entities/agilex-piper.md) family) |
| Isaac Sim digital twin | 30,035 | simulated replicas of the real tasks/assets |
| **Total** | **107k** (+5k failures) | 305.5 h, 479 tasks, 96 object classes |

Every trajectory carries **multi-view RGB-D**, full proprioceptive body state, end-effector state, and a linguistic task description. **10,000 trajectories additionally carry frame-level fine-grained language annotations**, each verified by multiple reviewers.

## Where it sits among real-robot datasets (Table I)

| Dataset | Trajectories | Tasks | Dexterous hand | Failure data | Digital twin |
|---|---:|---:|:---:|:---:|:---:|
| [DROID](../entities/droid.md) | 76k | n/a | ✗ | ✗ | ✗ |
| BridgeData V2 | 60.1k | n/a | ✗ | ✗ | ✗ |
| RT-1 | 130k | 700 | ✗ | ✗ | ✗ |
| RoboSet | 98.5k | 38 | ✗ | ✗ | ✗ |
| RH20T | 13k | 140 | ✗ | ✗ | ✗ |
| [Open X-Embodiment](../entities/open-x-embodiment.md) | 1.4M (aggregate) | 160k | ✗ | ✗ | ✗ |
| **RoboMIND** | **107k** | **479** | **✓** | **✓** | **✓** |

RoboMIND is the only entry in its own comparison table carrying all three of dexterous-hand data, failure data, and a digital twin. Worth reading with the usual caution about self-authored comparison tables — but the three columns are checkable facts, not judgments.

## Key claims

- **Standardization is the thesis.** Everything is collected on one teleoperation platform under one protocol, *"reducing variability and noise, which is crucial for training models that can generalize"* — an explicit contrast with OXE's aggregation-of-heterogeneous-sources approach. This is the same problem [X-VLA](xvla-paper.md) attacks from the model side with [soft prompts](../concepts/learning/soft-prompt-cross-embodiment.md); RoboMIND attacks it at collection time instead. **Two opposite strategies for the same disease** — normalize the data, or condition the model on which data it is.
- **Failure data as a first-class artifact.** 5k failure trajectories with documented causes, framed by the authors as enabling *"failure reflection and correction during policy learning"* and analogized to RLHF. The wiki has repeatedly found failure/recovery data to be the missing ingredient ([π*0.6](../entities/pistar06.md)'s human-gated DAgger, [ASPIRE](../entities/aspire.md)'s failure-diagnosis mining, [RoboTwin 2.0](robotwin2-paper.md)'s VLM failure localizer). RoboMIND is the only *dataset* in the wiki that ships it.
- **Single-task IL baselines** (ACT / Diffusion Policy / BAKU, trained from scratch per task, deployed to real hardware): **ACT averages 55.3% on AgileX**, ahead of UR5e 38.0%, Tien Kung 34.0%, Franka 30.7%. Diffusion Policy beats ACT on several Franka and Tien Kung tasks. **BAKU underperforms broadly**, which the authors attribute to hyperparameters tuned for simulation — *"the significant performance gap underscores the challenges in directly transferring models from simulated settings to physical robots."*
- **VLA finetuning** (OpenVLA / RDT-1B / CrossFormer on multitask aggregates per robot): **RDT-1B strongest, especially on dual-arm tasks**.

> [!warning] Every success rate in this paper is n = 10
> *"Each model was tested ten times"* for the IL baselines and *"ten trials for each task"* for the VLAs. Against the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md)'s bar — ~1,030 rollouts to separate at a 90% base rate, ~2,450 at 50% — **n=10 cannot separate anything**. A 55.3% vs 38.0% gap at n=10 per task has a 95% CI spanning roughly ±30 points per cell. Treat these numbers as **existence proofs that the data trains policies at all**, which is what a dataset paper needs to show, and not as a ranking of ACT vs DP vs BAKU or of one embodiment against another. The dataset is the contribution; the benchmark table is a smoke test.

## Analysis

> [!note] The action-space hole, seen from the dataset side
> [X-VLA](../entities/x-vla.md) draws on RoboMIND for 19.9% of its pretraining — but only the **Franka, UR-5, AgileX, and dual-Franka** portions. The **15,187 Tien Kung humanoid trajectories with dual dexterous hands are excluded**, and structurally they have to be: X-VLA aligns every embodiment to `xyz + Rot6D + binary gripper`, and **a dexterous hand is not a binary gripper**.
>
> That completes a picture assembled across three of today's ingests. The field's dominant "embodiment-agnostic" action representation is a **parallel-jaw-gripper-shaped hole**: it excludes dexterous hands at the top end (RoboMIND's humanoid, dropped), and it under-serves kinematically deficient arms at the bottom end ([Sourccey](../entities/sourccey.md)'s 5-DoF arms, untested; [RoboTwin 2.0](robotwin2-paper.md)'s Piper at 2.4% generation success before targeted engineering). "Cross-embodiment" currently means *cross-6-to-7-DoF-arm-with-a-parallel-gripper*. The most interesting data in RoboMIND is the part the leading cross-embodiment VLA cannot consume.
>
> RoboMIND's own paper hits the same wall from the other direction: OpenVLA was tested **only** on the Franka *"since the output of OpenVLA is the condition of one end effector and only supports single-arm manipulations."*

> [!note] Two opposite cures for heterogeneity, neither citing the other
> RoboMIND (Dec 2024) says: collect everything on one platform under one protocol so the data *is* homogeneous. [X-VLA](xvla-paper.md) (Oct 2025) says: accept heterogeneity and give each source a learned prompt that absorbs it. X-VLA then consumes RoboMIND as one of three corpora — so in practice the standardization bought X-VLA four *separate* soft prompts anyway (Franka, UR, AgileX, dual-Franka), because camera rig and control frequency still differ per setup. **Standardizing collection did not eliminate the need for per-source conditioning.** That is a mild but real negative result for the standardization thesis, visible only by reading the two papers together.

> [!note] The digital twin is the under-used half
> 30,035 of the trajectories are Isaac Sim replicas of the real tasks and assets — a real-to-sim pairing that most datasets lack and that is exactly what a sim-to-real study needs to control for scene difference. No source in this wiki uses it. [RoboTwin 2.0](robotwin2-paper.md) built its own digital twins from scratch rather than reusing these.

## Entities mentioned

- [RoboMIND](../entities/robomind.md) · [Tien Kung](../entities/tien-kung.md) · [Franka Panda](../entities/franka-panda.md) · [AgileX Piper](../entities/agilex-piper.md) (Cobot Magic family) · [Isaac Sim](../entities/nvidia-isaac-sim.md)
- [ACT](../entities/act.md) · [Diffusion Policy](../entities/diffusion-policy.md) · [OpenVLA](../entities/openvla.md) · [RDT-1B](../entities/rdt.md), CrossFormer, BAKU (no pages)
- [DROID](../entities/droid.md) · [Open X-Embodiment](../entities/open-x-embodiment.md) — the datasets it positions against
- [X-VLA](../entities/x-vla.md) — the wiki's principal downstream consumer

## Concepts touched

- [Imitation learning](../concepts/learning/imitation-learning.md) · [Soft-prompt cross-embodiment conditioning](../concepts/learning/soft-prompt-cross-embodiment.md) · [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) · [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md)

## Open questions

- **Has anyone trained on the 5k failure trajectories?** The dataset's most distinctive component, and no downstream use is recorded in this wiki. [X-VLA](xvla-paper.md) used RoboMIND's successes only.
- **Has anyone used the Isaac Sim digital twin** for a controlled real-vs-sim comparison? It is set up for exactly that and appears unused.
- **What does the Tien Kung dexterous-hand data need in an action space to be usable?** It is 14% of the dataset and currently excluded from the leading cross-embodiment VLA. This is the concrete form of the "gripper-shaped hole" above.
- **Is `RoboMind-Dual-Franka` in X-VLA the same thing as this paper's Franka split?** X-VLA lists four RoboMIND sources including a dual-Franka; this paper describes the Franka portion as single-arm. Possibly a later release or an undocumented subdivision. Minor, but it means one of the two descriptions is incomplete.

---
title: RoboMIND
type: entity
subtype: dataset
created: 2026-08-13
updated: 2026-08-27
sources: 3
tags: [robomind, dataset, teleoperation, multi-embodiment, franka, ur5e, agilex, tien-kung, dexterous-hand, failure-data, digital-twin, isaac-sim, x-humanoid]
---

**RoboMIND** (Multi-embodiment Intelligence Normative Data) — a **107,000-trajectory / 305.5-hour real-robot teleoperation dataset** across **479 tasks, 96 object classes, and four embodiments**, collected on a **single unified platform under one standardized protocol**. From the Beijing Innovation Center of Humanoid Robotics (X-Humanoid) + Peking University, Dec 2024. Primary source: [RoboMIND paper](../sources/robomind-paper.md). Project: [x-humanoid-robomind.github.io](https://x-humanoid-robomind.github.io/).

## Composition

| Embodiment | Trajectories |
|---|---:|
| [Franka Emika Panda](franka-panda.md) (single-arm) | 26,856 |
| UR5e (single-arm) | 25,170 |
| **[Tien Kung](tien-kung.md)** humanoid, dual dexterous hands | 15,187 |
| AgileX Cobot Magic V2.0 (dual-arm) | 10,269 |
| [Isaac Sim](nvidia-isaac-sim.md) digital twin | 30,035 |
| **Total** | **107k** + **5k annotated failures** |

Each trajectory: multi-view RGB-D, full proprioceptive body state, end-effector state, language task description. **10,000 trajectories carry frame-level fine-grained language annotations**, multi-reviewer verified.

## Why it matters in this wiki

- **19.9% of [X-VLA](x-vla.md)'s pretraining mixture** — entered as four separate soft-prompt data sources (`RoboMind-Franka` 6.7%, `-UR` 8.7%, `-Agilex` 3.7%, `-Dual-Franka` 0.8%), alongside [AgiBot](agibot.md)-Beta and [DROID](droid.md).
- **The only dataset here shipping failure data.** 5k real-world failure trajectories with documented causes. The wiki has repeatedly found failure/recovery signal to be the missing ingredient — [π*0.6](pistar06.md)'s human-gated DAgger, [ASPIRE](aspire.md)'s failure-diagnosis skill mining, [RoboTwin 2.0](robotwin.md)'s VLM failure localizer — and every one of those *generates* it at training time rather than finding it in a corpus.
- **The only dataset here shipping a digital twin** of its own real tasks and assets ([Isaac Sim](nvidia-isaac-sim.md), 30,035 trajectories). Set up for controlled real-vs-sim comparison; **no source in this wiki uses it**.
- **The standardization counter-thesis to [Open X-Embodiment](open-x-embodiment.md).** OXE aggregates 1.4M trajectories from many labs with differing standards; RoboMIND collects 107k under one protocol, explicitly to reduce *"variability and noise."*

## The two cures for heterogeneity

RoboMIND and [X-VLA](x-vla.md) attack the same disease from opposite ends: **normalize the data at collection time** vs **condition the model on which data it is** ([soft prompts](../concepts/learning/soft-prompt-cross-embodiment.md)).

> [!note] Standardizing collection did not remove the need for per-source conditioning
> X-VLA consumes RoboMIND and still assigns it **four separate soft prompts** — because camera rig and control frequency differ per setup even under one collection protocol. A mild negative result for the standardization thesis, visible only by reading the two papers together.

## The gripper-shaped hole

> [!warning] The most distinctive data here is the part the leading cross-embodiment VLA cannot consume
> [X-VLA](x-vla.md) draws on RoboMIND's Franka / UR-5 / AgileX splits and **excludes all 15,187 [Tien Kung](tien-kung.md) dual-dexterous-hand trajectories** — structurally it must, since its aligned action space is `xyz + Rot6D + binary gripper` and **a dexterous hand is not a binary gripper**.
>
> RoboMIND's own experiments hit the same wall: OpenVLA was evaluated **only** on the Franka *"since the output of OpenVLA is the condition of one end effector and only supports single-arm manipulations."*
>
> Together with [RoboTwin 2.0](robotwin.md)'s finding that a 6-DoF Piper generated usable data at **2.4%** before targeted engineering, and [Sourccey](sourccey.md)'s untested 5-DoF arms, the picture is consistent: **"cross-embodiment" in 2026 means cross-6-to-7-DoF-arm-with-a-parallel-gripper.** Both tails are excluded.

## Baselines

Single-task IL trained from scratch and deployed to real hardware: **[ACT](act.md) averages 55.3% on AgileX**, vs UR5e 38.0%, Tien Kung 34.0%, Franka 30.7%. [Diffusion Policy](diffusion-policy.md) beats ACT on several Franka and Tien Kung tasks. BAKU underperforms broadly (hyperparameters tuned for sim). VLA finetuning: **[RDT-1B](rdt.md) strongest**, especially dual-arm; [OpenVLA](openvla.md) Franka-only.

> [!warning] Every number above is n = 10
> Ten trials per task, for every model, throughout the paper. Against the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md)'s bar (~1,030 rollouts at a 90% base rate, ~2,450 at 50%), **n=10 separates nothing**. These are existence proofs that the data trains policies — which is what a dataset paper needs — not a ranking of ACT vs DP vs BAKU or of one embodiment against another.

## Related

- [X-VLA](x-vla.md) — principal downstream consumer in this wiki
- [DROID](droid.md), [Open X-Embodiment](open-x-embodiment.md), [AgiBot](agibot.md) — the corpora it positions against and sits beside
- [Tien Kung](tien-kung.md) — its humanoid embodiment
- [RoboTwin 2.0](robotwin.md) — the synthetic-data counterpart; cites RoboMIND as a real-world bridge
- [Soft-prompt cross-embodiment conditioning](../concepts/learning/soft-prompt-cross-embodiment.md) — the rival cure for heterogeneity

## Mentioned in

- [RoboMIND paper](../sources/robomind-paper.md)
- [X-VLA paper](../sources/xvla-paper.md)
- [Introducing Index (Figure AI)](../sources/figure-index-announcement.md) — Scale anchor (305.5 h) for [Index](figure-index.md)'s claimed ingest rate; also one of the supervised-collection corpora whose provenance model crowdsourcing abandons.

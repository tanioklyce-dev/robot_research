---
title: "SONIC — Supersizing Motion Tracking for Natural Humanoid Whole-Body Control (paper)"
type: source
url: https://arxiv.org/abs/2511.07820
project_page: https://nvlabs.github.io/GR00T-WholeBodyControl/
author: Zhengyi Luo, Ye Yuan, Tingwu Wang, Chenran Li, Fernando Castañeda (co-first), … Jan Kautz, Jim Fan, Yuke Zhu (NVIDIA GEAR)
published: 2025-11 (arXiv 2511.07820; local PDF is a later 2026-05 revision)
ingested: 2026-07-04
local_path: raw/sonic_paper.pdf
format: pdf (20 pp.)
tags: [sonic, gear-sonic, whole-body-control, humanoid, loco-manipulation, motion-tracking, rl, ppo, fsq, unitree-g1, nvidia, gear, groot, sim-to-real]
---

## Summary

Primary source for **[GEAR-SONIC](../entities/gear-sonic.md)** ("**S**upersizing m**O**tion tracking for **N**atural humano**I**d **C**ontrol") — NVIDIA GEAR's generalist **humanoid whole-body controller** and the controller behind the `UNITREE_G1_SONIC` embodiment tag in [Isaac-GR00T](isaac-gr00t-github.md). Thesis: **motion tracking is the scalable foundational task for humanoid control** — motion-capture data gives dense per-frame supervision that stays informative as data grows, unlike adversarial imitation (AMP/ASE) which mode-collapses. Scaling a single motion-tracking RL policy across model (1.2M→42M params), data (4M→100M+ frames from ~700 h mocap), and compute (~2K→21K GPU-hrs) yields a [Unitree G1](../entities/unitree-g1.md) controller that is natural, robust, zero-shot-generalizing, and sim-to-real transferable — and, via a **universal token action space**, serves as the low-level interface for VR/video/text/music teleoperation **and** for a [GR00T N1.5](groot-n1_5.md) VLA doing autonomous whole-body loco-manipulation. Code at `NVlabs/GR00T-WholeBodyControl`; checkpoints at `nvidia/GEAR-SONIC`.

## Key claims

### Method (§3)
- **RL: PPO + asymmetric actor-critic** (privileged critic, noisy-proprioception actor); trained in [Isaac Lab](../entities/nvidia-isaac-lab.md) with domain randomization; policy outputs PD joint targets. **Not** teacher-student distillation.
- **Universal token space**: three MLP encoders (robot-motion, human/SMPL-motion, hybrid sparse-upper-body) → shared latent → **Finite Scalar Quantization (FSQ)** (chosen over VQ-VAE to avoid codebook collapse) → a universal token `z`; a control decoder maps `z` to motor commands. Losses: PPO + reconstruction + token-alignment + cycle-consistency, trained jointly.
- **Robot**: [Unitree G1](../entities/unitree-g1.md) (29 actuated joints) throughout; human poses via SMPL. **Direct sim-to-real** on physical G1.
- **Kinematic planner**: real-time generative masked-token in-betweening (0.8–2.4 s segments; <5 ms laptop, 12 ms Jetson Orin; replans every 100 ms) bridging intent → reference motion for navigation / boxing / squatting / crawling.
- **GR00T link (§2.5)**: a [GR00T N1.5](groot-n1_5.md) VLA sits on top of the token interface, predicting a **78-dim action = 64-dim universal motion token + 14-dim hand joints**, decoded by SONIC — predicting tokens is smoother/safer than predicting explicit SMPL poses.

### Results (hard numbers)
- **Scaling**: largest (42M) model **99.6% success / 23.8 mm MPJPE** on out-of-distribution test-content (vs 98.0% / 27.7 mm at 1.2M); gains largest on OOD.
- **Vs. trackers**: SONIC **98.7 / 99.6 / 97.0%** (test-content / test-repetition / PHUMA) vs BeyondMimic 81.6 / 85.8 / 73.4; **41% MPJPE reduction** vs BeyondMimic (23.2 vs 39.1 mm).
- **Vs. specialist OpenHomie** (velocity tracking 0–5 m/s): **98.5% survival vs 43.0%**.
- **Sim-to-real** (123 real sequences): **99.2% real vs 100% sim**; MPJPE 25.7 mm real vs 22.3 sim. Largest gap is **foot placement** (53.7 vs 29.0 mm).
- **VLA loco-manipulation** ([GR00T N1.5](groot-n1_5.md), binary success): apple-to-plate 90%, scrub 95%, open-trash-via-foot-pedal 70%, 5-sequential-skill soda-can-to-trash 60%, drill-relocation 70% — **5-task avg 75%**.
- **Ablation**: FSQ tokens vs SMPL-pose action space for the VLA — **68% vs 27% avg (+42 pts)**; soda-can task 60% vs 0%. FSQ beats VQ-VAE by 8.7 mm; no codebook collapse.
- **Deployment**: onboard **Jetson Orin**, TensorRT + CUDA Graph, **1–2 ms/policy forward**; multi-rate (policy 50 Hz / command 500 Hz / planner 10 Hz).

### Dataset
- ~700 h raw mocap → retargeted to G1 (GMR + PyRoki) → filtered to **611 h / 100M+ frames @ 50 Hz**; 33 categories / 8,447 sub-categories; held-out test-content (182 novel sub-categories, 0% overlap).
- **Public release: BONES-SEED** on Hugging Face — 142,220 annotated motion sequences (288 h) from 522 actors, in SOMA + Unitree G1 formats.

## Entities mentioned
- [GEAR-SONIC](../entities/gear-sonic.md) — this is its primary source. [NVIDIA GEAR](../entities/nvidia-gear.md); [Jim Fan](../entities/jim-fan.md) + [Yuke Zhu](../entities/yuke-zhu.md) senior.
- [Unitree G1](../entities/unitree-g1.md) (primary robot), [Jetson Orin Nano](../entities/jetson-orin-nano.md) (deployment), [Isaac Lab](../entities/nvidia-isaac-lab.md) (sim), [MuJoCo](../entities/mujoco.md).
- [GR00T N1.5](../entities/nvidia-groot.md) VLA (on the token interface); baselines BeyondMimic, Any2Track, OpenHomie, AMP/ASE/CALM. FSQ, SMPL, BONES-SEED, GEM.

## Concepts touched
- Humanoid **[whole-body control](../concepts/robotics/whole-body-control.md)** + **loco-manipulation** (feet as manipulators); motion tracking as a scaling task; **scaling laws for control** (model/data/compute). SONIC is the **model-level "scale one policy"** exemplar; [BumbleBee](bumblebee-experts-to-generalist-wbc.md) is the **data-level "cluster + distill"** counterpoint. Its sibling [MotionBricks](motionbricks-paper.md) (same NVIDIA orbit) adds the object-interaction axis SONIC lacks (SONIC is locomotion-only).
- [Optimal control](../concepts/robotics/optimal-control.md)-adjacent: RL (PPO, asymmetric actor-critic); [sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) + domain randomization.
- **Vector quantization** (FSQ vs VQ-VAE); universal/shared **latent token action space** as a VLA↔controller interface — a discrete-action-space cousin of [VQ-BeT](../entities/vq-bet.md)'s codebook, here for whole-body control.
- [VLA models](../concepts/learning/vla-models.md) — SONIC is the low-level System-1 that a GR00T System-2 drives.

## Open questions
- No formal safety / energy-efficiency treatment; may lose balance under extreme dynamics.
- Foot-placement sim-to-real gap remains the hardest.
- Cross-tracker comparisons are cross-dataset (generalization evidence, not data-matched).
- Positioned as a low-level foundation; higher-level perception/reasoning still built on top (the [GR00T](../entities/nvidia-groot.md) VLA half).

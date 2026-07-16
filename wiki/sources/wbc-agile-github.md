---
title: "WBC-AGILE — A Generic Isaac-Lab based Engine for humanoid loco-manipulation (nvidia-isaac/WBC-AGILE)"
type: source
url: https://github.com/nvidia-isaac/WBC-AGILE
author: NVIDIA (with ETH Zurich lineage) — Huihua Zhao, Rafael Cathomen, Lionel Gulich, et al.
published: 2026-03-24 (v1.2)
ingested: 2026-07-15
license: BSD-3-Clause (RL algorithms) + Apache-2.0 (rest)
format: GitHub repository
tags: [agile, wbc-agile, whole-body-control, loco-manipulation, humanoid, unitree-g1, booster-t1, nvidia, eth-zurich, isaac-lab, rl, teacher-student, sim-to-real, rsl-rl]
---

# WBC-AGILE — A Generic Isaac-Lab based Engine for humanoid loco-manipulation

## Summary

**AGILE** = *"**A** **G**eneric **I**saac-**L**ab based **E**ngine for humanoid loco-manipulation learning"* — an [NVIDIA](../entities/nvidia.md) (with ETH-Zurich research lineage) RL framework for training humanoid **[whole-body control](../concepts/robotics/whole-body-control.md)** policies with **validated sim-to-real transfer**. It is the **"AGILE"** referenced by [Isaac Teleop](../entities/nvidia-isaac-teleop.md) in NVIDIA's [GR00T end-to-end workflow](nvidia-gr00t-e2e-workflow-docs.md) — the loco/whole-body layer beneath the GR00T VLA. **295 stars**; **v1.2 (2026-03-24)**; 98.4% Python; built on Isaac Lab v2.3.2 / Isaac Sim 5.1; **acknowledges BeyondMimic + RSL_RL + Isaac Lab** as antecedents.

## Key claims

- **Method**: **teacher-student distillation** with privileged observations; whole-body control via RL; targets **loco-manipulation** (locomotion + manipulation together).
- **Multi-robot**: *"Validated on **Booster T1** and **[Unitree G1](../entities/unitree-g1.md)** with sim-to-real transfer."* Demos — Booster T1: stand-up, velocity tracking; G1: velocity-height tracking, sit-down/stand-up, teleoperation, dancing.
- **Eval framework**: random rollouts, deterministic scenarios, motion metrics, HTML reports, Weights & Biases integration.
- **Usage**: `python scripts/train.py --task Velocity-T1-v0 --num_envs 2048 --headless`; `eval.py … --checkpoint <path>`.
- **License**: **BSD-3-Clause** for the RL library (`agile/algorithms/rsl_rl/`) + **Apache-2.0** for everything else.
- **Authors**: Huihua Zhao, Rafael Cathomen, Lionel Gulich, et al. (NVIDIA + ETH Zurich traditions).

## Where it sits vs. the WBC cluster

AGILE is the **engineering/tooling** counterpart to the wiki's WBC *methods* papers: it's a reusable Isaac-Lab **engine** (like a whole-body [RSL_RL](https://github.com/leggedrobotics/rsl_rl)), whereas [SONIC](sonic-paper.md), [MotionBricks](motionbricks-paper.md), and [BumbleBee](bumblebee-experts-to-generalist-wbc.md) are specific controllers/recipes. Its teacher-student-distillation + privileged-critic recipe echoes [SONIC](sonic-paper.md)'s asymmetric actor-critic and is a sibling to BeyondMimic (a shared baseline across this cluster). Notably it adds a **second robot (Booster T1)** to the G1-dominated benchmark set.

## Entities mentioned

- [NVIDIA](../entities/nvidia.md), [Unitree G1](../entities/unitree-g1.md), [Booster T1](../entities/booster-t1.md), [Isaac Lab](../entities/nvidia-isaac-lab.md), [Isaac Teleop](../entities/nvidia-isaac-teleop.md).

## Concepts touched

- [Whole-body control](../concepts/robotics/whole-body-control.md) + loco-manipulation; teacher-student distillation; [sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md).

## Open questions

- No standalone paper cited — AGILE is a framework release; its relation to the ASAP/HOVER lineage (also NVIDIA/ETH-adjacent) isn't spelled out beyond the BeyondMimic acknowledgment.
- Booster T1 specs not documented in the repo summary — see [Booster T1](../entities/booster-t1.md) (stub).

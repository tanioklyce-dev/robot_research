---
title: "ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills"
type: source
url: https://arxiv.org/abs/2502.01143
local_path: raw/2502.01143v1.pdf
sha256: a4fbb5f4dd88a9c88439612777908618dd70377858ec213c8c952640f42d346f
author: Tairan He†, Jiawei Gao†, Wenli Xiao†, Yuanhang Zhang†, et al.; Kris Kitani, Jessica Hodgins, Linxi "Jim" Fan, Yuke Zhu, Changliu Liu, Guanya Shi (CMU + NVIDIA; †equal contribution)
published: 2025-02-03
ingested: 2026-08-29
venue: arXiv preprint (2025)
format: PDF (18 pp., arXiv:2502.01143v1)
project_page: https://agile.human2humanoid.com
tags: [asap, humanoid, sim-to-real, delta-action-model, residual-learning, agile-motion, unitree-g1, isaacgym, genesis, cmu, nvidia]
---

# ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills

## Summary

**The sim-to-real gap, attacked by correcting the action rather than the simulator.** ASAP's target is agility — motions where the dynamics mismatch actually bites — and its demonstrations are deliberately theatrical: Cristiano Ronaldo's celebration (a jump with a **180° mid-air rotation**), LeBron James's "Silencer" (single-leg balance), Kobe Bryant's fadeaway (single-leg jump and landing), a **1.5 m forward jump** and a **1.3 m side jump**, on a [Unitree G1](../entities/unitree-g1.md).

The method is four steps:

1. **Pre-train** motion-tracking policies in simulation on retargeted human motion.
2. **Deploy on the real robot and record trajectories.**
3. Train a **delta (residual) action model** that minimizes the discrepancy between simulated and real states — i.e. learn what extra action the simulator would need to behave like reality.
4. **Freeze that model into the simulator**, fine-tune the policy against the now-aligned physics, and **deploy without the delta model.**

The last clause is the elegant part: the correction is a *training-time* object. Nothing extra runs on the robot.

## Key claims

- **Correcting the action beats correcting the parameters or the state.** ASAP is compared against **SysID** (search simulator parameters: CoM shift, base mass ratio, per-joint PD gain ratios) and **DeltaDynamics** (learn a residual *dynamics* model). The framing argument is that SysID and domain randomization "rely on labor-intensive parameter tuning or result in overly conservative policies that sacrifice agility" — conservatism is the specific failure, because agility is exactly what a robust-to-everything policy gives up.
- **Three transfer scenarios**, which is unusually thorough: IsaacGym → IsaacSim, IsaacGym → **Genesis**, and IsaacGym → **real [Unitree G1](../entities/unitree-g1.md)**. Using a second and third simulator as stand-ins for reality lets them measure transfer without burning hardware.
- Reported to reduce tracking error against SysID, DR and delta-dynamics baselines across dynamic motions.

## Why it matters in this wiki

- **It is the third distinct answer to the embodiment gap in this corpus**, and the three are complementary rather than competing: [H2O](h2o-paper.md) filters *infeasible motions* out of the data, ASAP corrects *dynamics mismatch* at training time, and [HOVER](hover-paper.md) unifies *control interfaces*. Same group, three different cuts at "the robot is not the human and the simulator is not the world."
- **The delta-action idea is portable.** Any sim-trained policy with real rollouts available can in principle learn a residual action correction and fold it back into training. Filed against [sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) alongside the privileged-distillation pattern.
- **CMU + NVIDIA together**, with [Jim Fan and Yuke Zhu](../entities/nvidia-gear.md) on the author list — the point where this academic line joins NVIDIA's [GEAR](../entities/nvidia-gear.md) program, which also produced [HOVER](hover-paper.md).

## Entities mentioned

- [Tairan He](../entities/tairan-he.md) — co-first author.
- [Unitree G1](../entities/unitree-g1.md) — the platform.
- [NVIDIA GEAR](../entities/nvidia-gear.md) — Fan and Zhu co-author.

## Concepts touched

- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — residual action correction as a distinct technique from DR and SysID.
- [Whole-body control](../concepts/robotics/whole-body-control.md).

## Open questions

- **Real-world quantitative results are not recorded on this page** — the extracted tables cover simulator-to-simulator open-loop comparisons; the real-G1 numbers are in the body.
- ~~Does the delta action model transfer across motions or overfit?~~ — **partly answered by a source the wiki already held.** ASAP asserts its model is "trained across multiple motions and is not overfitted to this specific example." [BumbleBee](bumblebee-experts-to-generalist-wbc.md) subsequently found that **per-cluster delta models beat one global delta model**, because cluster-consistent dynamics fit better — i.e. a single global correction *does* leave motion-dependent error on the table, and iterating the correction lifts real-robot success and foot stability. ASAP's claim is not wrong, but the global model is not the best available form of it.
- **How much real data does it need?** The size of the real-trajectory collection is the practical cost of the method and is not recorded here.

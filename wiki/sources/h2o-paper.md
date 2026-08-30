---
title: "H2O: Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation"
type: source
url: https://arxiv.org/abs/2403.04436
local_path: raw/2403.04436v1.pdf
sha256: 78d380da6e28949275137a7dd46922116a81efdf417a02aa81c6f40c5bcade22
author: Tairan He†, Zhengyi Luo†, Wenli Xiao, Chong Zhang, Kris Kitani, Changliu Liu, Guanya Shi (Carnegie Mellon University; †equal contribution)
published: 2024-03-07
ingested: 2026-08-29
venue: IROS 2024
format: PDF (10 pp., arXiv:2403.04436v1)
project_page: https://human2humanoid.com
tags: [h2o, humanoid, teleoperation, whole-body-control, motion-retargeting, amass, privileged-learning, sim-to-real, unitree-h1, cmu]
---

# H2O: Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation

## Summary

**Claimed as the first learning-based real-time whole-body humanoid teleoperation** — a person stands in front of an **RGB camera** and a full-sized [Unitree H1](../entities/unitree-h1.md) copies their whole body, live. No motion-capture suit, no exoskeleton, no force sensors on the operator.

The paper's transferable idea is **"sim-to-data."** The obstacle to training a motion-tracking policy is not the policy, it is the *dataset*: retargeting a large human-motion corpus ([AMASS](../entities/amass.md)) onto a humanoid produces many motions the robot physically cannot do — cartwheels, steps wider than its own leg length. So H2O first trains a **privileged motion imitator** with full simulator state, uses it to attempt every retargeted motion, and **discards the ones even a privileged policy cannot track**. What remains is a feasibility-filtered dataset, and the deployable policy is trained only on that.

This is the [privileged-teacher pattern](../syntheses/rl/locomotion-adaptation-lineage.md) applied to a target it is not usually pointed at: **not distilling a policy, but curating the data**.

## Key claims

- **Goal-conditioned RL (PPO)**, action = **19-dim joint targets** through a PD controller (`τ = Kp(a − q) − Kd q̇`).
- **State space is constrained by what exists on a real robot.** Proprioception is `[q, q̇, v, ω, g, a_{t−1}]`; the goal is **8 reference keypoints** — shoulders, elbows, hands, ankles — plus their offsets from the robot's own, plus their velocities. The privileged policy's state is **R⁷⁷⁸** (every rigid body's global pose and velocity) and is explicitly *not* deployable: global angular velocities "are hard to obtain accurately in the real world."
- **Zero-shot sim-to-real**, no real-world fine-tuning.

### Results (10k retargeted AMASS sequences)

| Policy | State dim | Sim2real | Success | Eg-mpjpe (mm) |
|---|---|---|---|---|
| Privileged imitator | R⁷⁷⁸ | ✗ | **85.5%** | 50.0 |
| H2O-reduced (keypoints only) | R⁹⁰ | ✓ | 53.2% | 200.2 |
| H2O w/o sim-to-data | R¹³⁸ | ✓ | 67.9% | 176.6 |
| **H2O (full)** | R¹³⁸ | ✓ | **72.5%** | 166.7 |

Two ablations, two separate lessons. **Dropping the sim-to-data filter costs 4.6 points** — the data curation is worth real performance. **Dropping the keypoint *difference* from the goal state costs 19 points** (72.5 → 53.2): telling the policy where the target is matters far less than telling it *how far off it currently is*.

The privileged policy's 85.5% is the honest ceiling, and the 13-point gap to H2O is the price of only using sensors that exist.

### Demonstrated

Walking, back jumping, kicking, turning, waving, pushing, boxing; and in the figure: step-and-punch a box, sidestep and kick a ball, push a stroller, catch a box and drop it into a bin.

## Why it matters in this wiki

- **It makes humanoid data collection a teleoperation problem.** The stated motivation is that RGB-camera teleoperation could "pave the way for collecting large-scale humanoid data for training autonomous agents" — the thesis [OmniH2O](omnih2o-paper.md) and [HumanPlus](humanplus-paper.md) then execute on.
- **The embodiment gap is treated as a data problem, not a control problem.** Rather than making the controller robust to infeasible references, H2O removes them. Worth contrasting with [ASAP](asap-paper.md), which attacks the *dynamics* half of the same gap.
- The paper argues the whole-body framing is what justifies a humanoid at all: if you do not need to track the lower body, "the robot could opt for designs with better stability, such as a quadruped or wheeled configuration."

## Entities mentioned

- [Tairan He](../entities/tairan-he.md) — co-first author; the through-line author of this corpus.
- [Unitree H1](../entities/unitree-h1.md) — the platform.
- [AMASS](../entities/amass.md) — the human-motion corpus being retargeted.

## Concepts touched

- [Whole-body control](../concepts/robotics/whole-body-control.md) — this is the wiki's anchor for the teleoperation branch.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — privileged learning used for data curation rather than policy distillation.
- [Locomotion adaptation lineage](../syntheses/rl/locomotion-adaptation-lineage.md) — the quadruped counterpart, where privileged teachers were later abandoned.

## Open questions

- **No real-world success rate.** Table III is simulation; the hardware results are qualitative demonstrations. See the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md).
- **How much of the 13-point privileged gap is sensing vs regularization?** The privileged policy is also trained without domain randomization, so the comparison conflates two things.
- **Operator skill is uncontrolled** — teleoperation quality depends on the human, and no inter-operator variance is reported.

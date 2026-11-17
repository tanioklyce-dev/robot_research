---
title: "A Learning-based Quadcopter Controller with Extreme Adaptation (Zhang et al., T-RO 2025)"
type: source
url: https://arxiv.org/abs/2409.12949
local_path: raw/2409.12949v2.pdf
sha256: f0a2cb60b65786819eda06b9b4dad77809edabf030a6d464916d81ad4ce967d1
author: "Dingqi Zhang, Antonio Loquercio, Jerry Tang, Ting-Hao Wang, Jitendra Malik, Mark W. Mueller (HiPeRLab and EECS, UC Berkeley; Loquercio now U. Penn)"
published: 2024-09-19
ingested: 2026-11-16
venue: "IEEE Transactions on Robotics (T-RO), 2025 (accepted April 2025); arXiv 2409.12949 v2 (2025-06-08)"
format: paper (17 pp incl. appendix)
code: https://github.com/muellerlab/xadapt_ctrl
tags: [quadcopter, uav, adaptive-control, rma, imitation-learning, reinforcement-learning, il-plus-rl, dagger, domain-randomization, design-informed-randomization, cross-embodiment, zero-shot, l1-adaptive-control, indi, mnn, edge-inference, hierarchical-control, hiperlab, uc-berkeley]
---

# A Learning-based Quadcopter Controller with Extreme Adaptation

## Summary

The journal extension of the [near-hover controller](near-hover-adaptive-quadcopter-controller-paper.md). It turns that position controller into a **low-level controller**: it takes body-rate and collective-thrust commands from any high-level controller and outputs individual motor speeds at 500 Hz, adapting online to the vehicle it is flying. The architecture is still [RMA](rma-paper.md)-style (base policy plus adaptation module, now an 8-D latent from a 100-step history). The paper adds three things: **imitation of a model-based expert mixed with RL**, with the imitation weight decaying exponentially; a **torque-tracking reward**; and **design-informed domain randomization**, which samples physically consistent vehicles from a size factor instead of independent parameters. In simulation it keeps near-100% success on vehicles sampled from a range **16× wider than training**. On hardware it flies two quadcopters differing **3.68× in mass and more than 100× in motor constant** with one policy, and handles an off-center payload, wind and a 20% single-motor thrust loss that makes the tuned baseline crash.

## Key claims

**Method** (§II)
- **Hierarchy kept on purpose.** The learned part is only the low level, so any high-level planner can sit on top, and adaptation stays where the variation is: at the motors.
- **IL + RL with a decaying mix** (Eqs. 9–12): R(π) = (1−α)·R_RL − α·L_IL with α = e^(−0.001·epoch). The expert is a PD controller **updated with each sampled vehicle's true parameters**, so the policy imitates an expert that changes with the body.
- **Torque, not angular velocity, in the reward** (§II-C, §VI-A2): torque responds directly to motor speed, giving the 500 Hz learner immediate feedback. Angular velocity is an integral, so its feedback lags. Across 10 seeds, the torque-reward policy trains more stably (−3.91 ± 4.67 vs −8.74 ± 8.15 final reward).
- **Design-informed randomization** (§II-E): a size factor c ∈ [0, 1] drives arm length linearly, mass ∝ l³, inertia ∝ l⁵, drag ∝ l², and motor constant exponentially, with ±20% noise on top. This avoids physically implausible vehicles such as *"a very small and lightweight quadcopter equipped with overly powerful motors"*. Prior work randomized only *"up to 30%"* around a nominal model; here the variation is *"thousands of times larger"*.
- Environment vector e_t is 34-D (including the 4×4 mixer matrix, motor effectiveness factors and external torque), compressed to z_t ∈ ℝ⁸; the dimension was chosen by binary search.

**Simulation** (§IV, 100 runs per method)
- **Within the training range** (Table IV): success **100%**, against PID-L1 77%, PID-INDI-A 67%, Geo-A 64%, L1-PDn 62% and PID-PDn 22%. The expert PID-PD\* with true parameters also reaches 100%. **PID-INDI-A has the lowest tracking error among successful runs** (0.063 m against ours 0.148 m), but it needs motor-speed and angular-acceleration feedback the learned controller doesn't get, and it fails near the edges of the range.
- **Low-level adaptation beats high-level** (PID-L1 77% vs L1-PDn 62%): evidence for adapting at the motor layer when vehicles differ this much.
- **Generalization** (Fig. 6): near-100% success out to δ = 8, a sampling range 16× wider than training, dropping to **95%** there. Mean position error grows 37% from δ = 0 to δ = 8, against **484%** for PID-L1.

**Hardware** (§V, **3 runs per method per task**)
- Two vehicles: 985 g / 17.7 cm arm and 267 g / 5.8 cm arm, both on a Qualcomm RB5. Motion capture feeds only the high-level controller and the evaluation; **the policy sees IMU only**.
- Sim-to-real: Pearson **0.652** (p = 0.002) between simulated and real position errors, from 10 simulated and 3 real flights at three speeds.
- Against the per-vehicle tuned expert PD\* (Table V): PD\* is slightly better with no disturbance. With an off-center payload (up to 20% of mass at the frame edge) and under 3.5 m/s wind, the learned controller has lower angular and position error. With **20% thrust loss on one motor, PD\* fails outright on the large quad** and the learned controller flies. Thrust tracking error is up to 4.53× higher for PD\*.
- Adaptation on takeoff takes about **0.2 s**, matching the 100-step window at 500 Hz, against 10–15 s for online system identification.

**Ablations** (§VI, Fig. 12)
- **RL-only and IL-only (DAgger) both fall to about 60% success** as mismatch grows. Their combination stays near 100%. The authors' hypothesis: IL minimizes instantaneous tracking error, while RL also optimizes survival through episode termination, so each covers the other's blind spot.
- **End-to-end** (one policy fusing high- and low-level control, trained the same way) is worst: **28% at δ = 8**, barely above non-adaptive baselines.

**Deployment** (Table III, Qualcomm RB5): the policy plus adaptation module take **78.85 ms in PyTorch, too slow for a 2 ms (500 Hz) budget, and 0.165 ms after conversion to MNN.**

## Analysis

- **Two results with reach beyond drones.**
  1. *Keep the hierarchy, learn the layer where the variation lives.* The end-to-end variant collapsed while the modular one generalized 16×. That is a concrete data point for [control abstraction levels](../concepts/robotics/control-abstraction-levels.md).
  2. *IL + RL beats either alone on generalization*, with a mechanism hypothesized but not proven.
- **The inference-runtime result is a practical warning.** A 3-layer MLP plus a small CNN missed its real-time budget by about 40× in PyTorch on an edge SoC, and made it with a mobile inference runtime. Framework choice, not model size, decided feasibility ([heterogeneous edge SoC](../concepts/robotics/heterogeneous-edge-soc.md)).
- **Evidence weight.** The simulation comparisons are 100 runs each and solid. The hardware table is 3 runs per cell. The thrust-loss failure of PD\* is the most decisive real-world result.

## Entities mentioned

- [HiPeRLab](../entities/hiperlab.md), [UC Berkeley](../entities/uc-berkeley.md)

## Concepts touched

- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — two-phase privileged learning with design-informed randomization
- [DAgger and interactive imitation](../concepts/learning/dagger.md) — the IL-only ablation; the main method imitates a model-based expert that changes with the vehicle
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — modular low level against end-to-end
- [Heterogeneous edge SoC](../concepts/robotics/heterogeneous-edge-soc.md) — PyTorch vs MNN on RB5
- [Agentic UAVs](../concepts/robotics/agentic-uavs.md), [Cross-embodiment](../concepts/learning/cross-embodiment.md)

## Open questions

- Does the IL + RL complementarity hold outside quadcopters, for example for a legged or arm low-level controller?
- Real-world tests cover two vehicles. Where on real hardware does the 16× simulated envelope end?
- The lowest-error baseline (INDI-A) uses sensors the learned controller doesn't. How would the learned controller do with motor-speed feedback added?

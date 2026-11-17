---
title: HiPeRLab (High Performance Robotics Lab, UC Berkeley)
type: entity
subtype: lab
created: 2026-11-16
updated: 2026-11-16
sources: 4
tags: [hiperlab, uc-berkeley, mark-mueller, uav, quadcopter, adaptive-control, rma, residual-rl, flying-battery, aerial-docking, mechanical-engineering]
---

**HiPeRLab** (High Performance Robotics Lab) — Mark W. Mueller's lab in Mechanical Engineering at [UC Berkeley](uc-berkeley.md). It works on *"low-level research on fundamental robotics capabilities, especially for Unmanned Aerial Systems"*, with a focus on safety, localization and design, and *"a strong focus on experimental validation"* ([lab site](https://hiperlab.berkeley.edu/), read 2026-11-16).

## In this wiki: learned low-level control for drones

Three ingested papers form one line of work. Dingqi Zhang is on all three and Mueller is the senior author:

| Paper | What it adds |
|---|---|
| [Near-hover adaptive controller](../sources/near-hover-adaptive-quadcopter-controller-paper.md) (2022–23; v1 titled *"A Zero-Shot Adaptive Quadcopter Controller"*) | **[RMA](../sources/rma-paper.md) moved from legs to quadcopters**, co-authored by RMA's [Ashish Kumar](ashish-kumar.md) and Jitendra Malik. The latent encodes the robot's own body. One policy flies two real quads 4.5× apart in mass, zero-shot (5 runs per cell). |
| [Extreme Adaptation](../sources/extreme-adaptation-quadcopter-controller-paper.md) (T-RO 2025) | A low-level motor controller trained with **IL from a model-based expert plus RL**, a torque-tracking reward, and design-informed randomization. Near-100% simulated success over a 16× wider range than training; survives a single-motor thrust loss that crashes the tuned baseline. An **end-to-end variant collapses to 28%**. |
| [ProxFly](../sources/proxfly-paper.md) (ICRA 2025) | **Residual RL** on a cascaded controller for flight in another drone's downwash, with no communication and no aerodynamic model. Beats its base controller by 29% (position) and 44% (attitude); against a CFD-modelled controller it is better on attitude and worse on position. Demonstrated a mid-air docking. |

The common pattern: **keep a classical control structure and learn only the part the model gets wrong.** For the motor layer, that means learning the vehicle-specific dynamics; for the high level, a learned residual on top of a model-based controller. All three train entirely in simulation and deploy zero-shot.

## Other work (from the lab site and YouTube; not ingested)

Vehicle design (tilt-rotor and passively tilting quads, a mid-air reconfigurable quad, a tensegrity collision-resilient vehicle, Duawlfin's combined wheels and flight), **flying batteries** (in-flight battery swapping; the aerodynamic-compensation baseline ProxFly compares against), energy efficiency, motion planning (RAPPIDS) and state estimation. Mueller's book *Dynamics and Control of Autonomous Flight* (Springer, 2025). [YouTube channel](https://www.youtube.com/channel/UCJnDtux5GS1WRogCBfLTsfA/videos) (42 videos).

## Related

- [UC Berkeley](uc-berkeley.md) — the parent institution, alongside the Malik group
- [Agentic UAVs](../concepts/robotics/agentic-uavs.md) — the control layer this lab's work sits in
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md), [Real-world robot RL](../concepts/learning/real-world-robot-rl.md)

## Mentioned in

- [Near-hover adaptive quadcopter controller](../sources/near-hover-adaptive-quadcopter-controller-paper.md)
- [A Learning-based Quadcopter Controller with Extreme Adaptation](../sources/extreme-adaptation-quadcopter-controller-paper.md)
- [ProxFly](../sources/proxfly-paper.md)

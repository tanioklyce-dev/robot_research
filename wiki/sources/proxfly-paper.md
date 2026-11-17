---
title: "ProxFly: Robust Control for Close Proximity Quadcopter Flight via Residual Reinforcement Learning (Zhang, Zhang, Mueller, ICRA 2025)"
type: source
url: https://arxiv.org/abs/2409.13193
local_path: raw/2409.13193v2.pdf
sha256: 85104fe708f318434f299b40261d415918461bfc5262174dbff0a84965db44c3
author: "Ruiqi Zhang, Dingqi Zhang, Mark W. Mueller (HiPeRLab, UC Berkeley)"
published: 2024-09-20
ingested: 2026-11-16
venue: "ICRA 2025 (accepted); arXiv 2409.13193 v2 (2025-04-30)"
format: paper (7 pp)
code: https://github.com/ruiqizhang99/ProxFly
tags: [quadcopter, uav, residual-rl, residual-policy-learning, downwash, close-proximity-flight, aerial-docking, domain-randomization, sim-to-real, ppo, flying-battery, hiperlab, uc-berkeley]
---

# ProxFly

## Summary

A **residual RL** controller for quadcopters flying in each other's downwash. A small MLP policy adds corrections (thrust and three body rates, at 50 Hz) on top of a standard cascaded position and attitude controller. It sees only the ego vehicle's state errors and the base controller's commands: **no communication with the other drone and no aerodynamic model**. Instead of modelling downwash with CFD or wind-tunnel data, training randomizes disturbance forces as triangular waves of random period and amplitude, plus per-propeller thrust-loss factors. It trains in **15 minutes on a laptop CPU**. In real flights with one quad 50 cm above another, it cuts position error **29.0%** and attitude error **43.7%** against its own base controller. It also completes a **mid-air docking**, where a small quad lands on a large one in flight.

## Key claims

- **Residual formulation** (§II-A): π(o|θ) = u_cas(s) + π_res(o|θ). The gradient flows only through the residual, so the RL objective is unchanged, but exploration starts from a working controller. The authors list three advantages: sample efficiency (it skips learning from scratch), correction of the base controller's steady-state error, and a smaller share of *"unexplainable signals from the black box"* in the final command.
- **Observation** (20-D): state error (12), base-controller command (4), last residual action (4). Actions are bounded to ±10 m/s² of mass-normalized thrust and ±1 rad/s of body rates.
- **Disturbance randomization instead of aerodynamic modelling** (§II-B3, Table I): mass ±50% (large quad) or ±20% (small quad); per-propeller thrust factor U(0.6, 1.2); vertical forces up to 8 N (large) as triangular functions with 2–8 s periods; Gaussian torque noise. The simulated downwash test (Fig. 3) uses a separate high-fidelity aerodynamic model the policy never trained on, and the residual still corrects altitude and pitch.
- **Real world** (Table II): three tasks with the small quad 50 cm above the large one (hover; circling in the same direction; circling in opposite directions). Trial counts are not stated.

| Average across tasks | Basic controller | FB-AeroComp (CFD-modelled) | ProxFly |
|---|---|---|---|
| Position RMSE (m) | 0.151 | **0.098** | 0.107 |
| Attitude RMSE (rad) | 0.180 | 0.133 | **0.101** |

- **Mid-air docking** (Fig. 5): a single demonstration. Approach, docking (an impulse plus a permanent mass change), then undocking. The residual produces opposing roll and pitch rates and compensating thrust at each stage; the authors say the base controller alone would fail.
- **Stated limits** (§IV): the residual's commands still oscillate at high frequency despite the penalty (a motor-overheating risk), and it was trained for hovering, so trajectory tracking is done by moving the hover setpoint.

## Analysis

> [!note] "Comparable" to the aerodynamic-model baseline, read carefully
> The 29.0% and 43.7% gains are against the paper's **own base controller**. Against FB-AeroComp, the model-based controller with CFD- and wind-tunnel-derived compensation from the same lab's flying-battery work, ProxFly is **better on attitude but worse on average position**: 0.107 m vs 0.098 m. It is clearly worse when circling in the same direction (0.139 m vs 0.083 m) and better only in hover (0.088 m vs 0.111 m). The paper's word, "comparable", is fair for a method that needs no aerodynamic model and no communication. It is not a win on position.

- **Residual RL as the bridge pattern.** This is the same shape as [SPARR](nvidia-r2d2-gb300-tester-tray-assembly-blog.md) in NVIDIA's assembly work: a trustworthy base controller does most of the job, and the learned residual absorbs what the model misses ([real-world robot RL](../concepts/learning/real-world-robot-rl.md)). ProxFly trains the residual entirely in simulation and deploys it zero-shot. SPARR trains its residual on the real robot.
- **Randomize the effect, not the physics.** Replacing a CFD downwash model with randomized force waveforms and thrust-loss factors is a cheap, transferable recipe whenever a disturbance is hard to model but easy to bound.

## Entities mentioned

- [HiPeRLab](../entities/hiperlab.md), [UC Berkeley](../entities/uc-berkeley.md)

## Concepts touched

- [Real-world robot RL](../concepts/learning/real-world-robot-rl.md) — residual RL on a model-based base
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — disturbance randomization as a modelling substitute
- [Agentic UAVs](../concepts/robotics/agentic-uavs.md) — the control layer for multi-drone operation

## Open questions

- How many trials sit behind each Table II cell? They are not stated.
- Does the residual remain safe if the base controller's model is badly wrong, rather than off by ±50% on mass?
- Would combining it with the [extreme-adaptation](extreme-adaptation-quadcopter-controller-paper.md) low-level controller (adaptation at the motors, residual at the high level) compound the gains? The two papers share an author.

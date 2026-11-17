---
title: "Learning a Single Near-hover Position Controller for Vastly Different Quadcopters (Zhang et al., 2022–23)"
type: source
url: https://arxiv.org/abs/2209.09232
local_path: raw/2209.09232v2.pdf
sha256: 7d13dd37bde38e9704e7d8548adece9e4a7e952b14bcb55cce7b9fa959769955
author: "Dingqi Zhang, Antonio Loquercio, Xiangyu Wu, Ashish Kumar, Jitendra Malik, Mark W. Mueller (HiPeRLab, Mechanical Engineering, and EECS, UC Berkeley)"
published: 2022-09-19
ingested: 2026-11-16
venue: "arXiv 2209.09232 v2 (2023-05-02). v1 was titled \"A Zero-Shot Adaptive Quadcopter Controller\", the title the lab's YouTube video still carries. The PDF and arXiv metadata state no venue."
format: paper (7 pp)
tags: [quadcopter, uav, adaptive-control, rma, rapid-motor-adaptation, sim-to-real, domain-randomization, privileged-learning, zero-shot, cross-embodiment, flightmare, ppo, l1-adaptive-control, hiperlab, uc-berkeley]
---

# Learning a Single Near-hover Position Controller for Vastly Different Quadcopters

## Summary

The first of the [HiPeRLab](../entities/hiperlab.md) adaptive-controller papers, and a direct transplant of **[RMA](rma-paper.md) from legged robots to quadcopters by two of RMA's own authors** ([Ashish Kumar](../entities/ashish-kumar.md), Jitendra Malik). One neural policy outputs individual motor speeds at 500 Hz for *any* quadcopter in a wide parameter range. A base policy is conditioned on a 6-D latent "intrinsics" vector. In simulation that vector is computed from true parameters; on the robot an **adaptation module** estimates it from the last 400 state–action pairs. Unlike RMA, the latent encodes **the robot's own body** (mass, inertia, arm length, motor and propeller constants, payload) rather than external terrain. The single policy was deployed **zero-shot** on two real quadcopters differing 4.5× in mass and 2.9× in arm length, with no calibration or fine-tuning.

## Key claims

- **Three stated insights** (§I): dynamics parameters are observable from state–action history; the estimate need not be "ground truth", only good enough to produce the right action, which sidesteps observability problems; and a system adapts to unseen disturbances whose effect lies in the convex hull of training disturbances (*"a motor losing efficiency has a similar effect to adding a payload below the motor"*).
- **Method** (§III, Fig. 2): Phase 1 trains base policy π and encoder µ with PPO on ground-truth parameters e_t (18-D) → z_t (6-D). Phase 2 trains adaptation module φ by supervised regression ‖z − ẑ‖² from a 400-step state–action history (1-D CNN). Policy training takes about 2 h on one GPU; the adaptation module about 20 min. Training uses [Flightmare](https://github.com/uzh-rpg/flightmare), with 10 ms observation latency simulated and parameters re-randomized mid-episode to mimic sudden payloads.
- **Training ranges** (Table I): mass 0.142–0.950 kg, arm length 0.046–0.200 m, motor constant about 66× range, payload 10–50% of mass.
- **Real world** (Table II, **5 runs per cell**): against a per-vehicle-tuned PID and LTF (a learned robust controller), it reaches **100% success on every task** (free hover, inertia board, rigid payload). PID fails all 5 inertia-board runs on the small quad, and LTF fails on both quads. PID slightly beats it in free hover on the large quad, *"justified, since the PID controller is specifically tuned for each quadcopter"*.
- **Simulation** (Table III, 100 runs): success **66%**, against L1 adaptive 59%, LTF 59%, SysID 38% and Robust 18%. The Phase-1 expert with true parameters reaches **69%**. Absolute success is low across the board on this wide test range.
- **Out-of-distribution disturbances** (Table IV): random external forces 49% (L1 42%), partially failing motors 38% (L1 33%). L1 is given a reference model at the median parameters, a prior the learned method does not need.
- **Adaptation speed** (Fig. 4): about **2 s** to detect and absorb an added payload, against 10–15 s for online system identification of explicit model parameters.
- **Stated limit** (§VI): *"a quasi-static position controller which fails on tracking aggressive flights."* That is what the [T-RO follow-up](extreme-adaptation-quadcopter-controller-paper.md) addresses.
- Positioning: off-the-shelf autopilots (Betaflight, [PX4](../entities/px4-autopilot.md)) *"still require significant in-flight tuning for each robot type"*. The pitch is a plug-in controller for custom vehicles built by people without modelling expertise.

## Analysis

- **What RMA's latent can carry.** In RMA the latent encodes the world (terrain, friction). Here it encodes the body, so the same architecture becomes a **cross-embodiment controller**, and it works at the motor level, where a legged robot's internal joint loops hide most of the variation. This is the clearest instance in the wiki of RMA's idea generalizing beyond its original domain ([sim-to-real](../concepts/learning/sim-to-real-transfer.md)).
- **Evidence weight.** The real-world claim rests on two vehicles and 5 runs per condition. The simulation numbers are 100 runs but on a deliberately hard range where nothing exceeds 69%. The relative ordering is the result; the absolute rates are not.

## Entities mentioned

- [HiPeRLab](../entities/hiperlab.md) — Mark W. Mueller's lab
- [UC Berkeley](../entities/uc-berkeley.md) — HiPeRLab (ME) and EECS
- [Ashish Kumar](../entities/ashish-kumar.md) — RMA first author, co-author here
- [PX4](../entities/px4-autopilot.md) — named as the tuning-heavy incumbent

## Concepts touched

- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — two-phase privileged learning
- [Agentic UAVs](../concepts/robotics/agentic-uavs.md) — the adaptive-control layer
- [Cross-embodiment](../concepts/learning/cross-embodiment.md) — one policy, many bodies

## Open questions

- How does the 6-D latent behave on a vehicle outside the training range? The T-RO follow-up tests this in simulation only.
- What is the real-world failure boundary? Two vehicles bracket the range but don't probe its edge.

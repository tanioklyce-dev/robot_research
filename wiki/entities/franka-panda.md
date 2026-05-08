---
title: Franka Panda
type: entity
subtype: robot
created: 2026-05-07
updated: 2026-05-07
sources: 5
tags: [franka, panda, robot-arm, manipulator, 7-dof, manipulation-platform]
---

**Franka Panda** — 7-DOF research-grade robotic arm from Franka Robotics (formerly Franka Emika GmbH). Effectively the **default tabletop manipulation platform** in academic robot-learning research: small footprint, torque-controlled, well-documented ROS / FCI integration, comfortably under €30k. Cross-references in this wiki: 24+ across [[droid|DROID]] (single embodiment for entire dataset), [[v-jepa-2|V-JEPA 2]] / [[v-jepa-2-1-paper|V-JEPA 2.1]] (zero-shot real-robot eval), [[jepa-wms|JEPA-WMs]] (real-Franka eval alongside RoboCasa + DROID), and many simulator setups.

## Specs (Panda generation)
- **7 DOF** torque-controlled arm.
- **~3 kg payload**.
- **855 mm reach**.
- **~17 kg arm weight**.
- Real-time control via FCI (Franka Control Interface) at 1 kHz.

> [!note] Panda vs FR3
> Franka Robotics introduced **FR3** as the successor to Panda; many recent installations are FR3 hardware. Public datasets and papers often still say "Franka" or "Franka Panda" generically. Treat the entity here as Panda + FR3 collectively until a project explicitly distinguishes; spin out a separate `franka-fr3` page if a paper or product hinges on the distinction.

## Why it matters in this wiki
Franka Panda is the **closest thing to a standard real-robot evaluation platform** across the JEPA-for-robotics literature ingested here:

- **[[droid|DROID]]** uses it as the *only* embodiment across 76,000 trajectories / 350 hours / 564 scenes. The "scene diversity at fixed embodiment" thesis depends on Franka being that fixed embodiment.
- **[[v-jepa-2-paper|V-JEPA 2]]** evaluates zero-shot pick-and-place on Franka arms in **two new labs** (no robot-specific data, no training, no rewards) — the strongest published evidence for latent-prediction world models transferring from internet video to real robots.
- **[[v-jepa-2-1-paper|V-JEPA 2.1]]** reports +20pt grasping over V-JEPA 2-AC on real Franka.
- **[[jepa-wms|JEPA-WMs]]** uses Franka trajectories for "unroll decode evaluation" alongside DROID + RoboCasa.
- **[[robot-utility-models|Robot Utility Models]]** lists Franka (and xArm 7) as cross-embodiment transfer targets from a Stretch-collected dataset.

The result: when a JEPA-style or VLA-style paper says "real-robot eval" without further qualification in 2024–2026, the default mental model is Franka.

## Why Franka in particular
- **Torque control out-of-the-box** at 1 kHz is unusual for tabletop arms in this price band.
- **Small tabletop footprint** fits academic-lab benches.
- **Open-ish ecosystem** — `franka_ros`, `libfranka`, `frankx` Python bindings, plus widespread MuJoCo / Isaac Sim / Pinocchio models.
- **Existing teleop pipelines** — DROID's Oculus Quest 2 + Franka teleop rig is the most-replicated real-robot data-collection setup of the 2024–2026 cohort.

## Related
- [[droid|DROID]] — single-embodiment dataset built on Franka Panda.
- [[v-jepa-2|V-JEPA 2]] / [[jepa-wms|JEPA-WMs]] — JEPA-line real-robot evaluations.
- [[robot-utility-models|Robot Utility Models]] — cross-embodiment transfer target.
- [[mujoco|MuJoCo]] / [[nvidia-isaac-sim|Isaac Sim]] — simulators with Franka models.

## Open questions / TBD
- Panda vs FR3 — which generation is each ingested paper actually using? Mostly unstated in abstracts.
- Adoption of Panda by industrial OEMs — not covered here.
- Companion grippers (Franka Hand, Robotiq 2F-85) deserve their own pages when a specific paper hinges on them.

## Mentioned in
- [[droid|DROID]] (entity)
- [[v-jepa-2-paper|V-JEPA 2 Paper]]
- [[v-jepa-2-1-paper|V-JEPA 2.1 Paper]]
- [[jepa-wms-paper|JEPA-WMs Paper]]
- [[robot-utility-models-website|Robot Utility Models Project Page]]
- [[robot-utility-models-paper|Robot Utility Models Paper]]

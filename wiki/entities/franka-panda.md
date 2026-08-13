---
title: Franka Panda
type: entity
subtype: robot
created: 2026-05-07
updated: 2026-08-13
sources: 31
tags: [franka, panda, robot-arm, manipulator, 7-dof, manipulation-platform]
---

**Franka Panda** — 7-DOF research-grade robotic arm from Franka Robotics (formerly Franka Emika GmbH). Effectively the **default tabletop manipulation platform** in academic robot-learning research: small footprint, torque-controlled, well-documented ROS / FCI integration, comfortably under €30k. Cross-references in this wiki: 24+ across [DROID](droid.md) (single embodiment for entire dataset), [V-JEPA 2](v-jepa-2.md) / [V-JEPA 2.1](../sources/v-jepa-2-1-paper.md) (zero-shot real-robot eval), [JEPA-WMs](jepa-wms.md) (real-Franka eval alongside RoboCasa + DROID), and many simulator setups.

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

- **[DROID](droid.md)** uses it as the *only* embodiment across 76,000 trajectories / 350 hours / 564 scenes. The "scene diversity at fixed embodiment" thesis depends on Franka being that fixed embodiment.
- **[V-JEPA 2](../sources/v-jepa-2-paper.md)** evaluates zero-shot pick-and-place on Franka arms in **two new labs** (no robot-specific data, no training, no rewards) — the strongest published evidence for latent-prediction world models transferring from internet video to real robots.
- **[V-JEPA 2.1](../sources/v-jepa-2-1-paper.md)** reports +20pt grasping over V-JEPA 2-AC on real Franka.
- **[JEPA-WMs](jepa-wms.md)** uses Franka trajectories for "unroll decode evaluation" alongside DROID + RoboCasa.
- **[Robot Utility Models](robot-utility-models.md)** lists Franka (and xArm 7) as cross-embodiment transfer targets from a Stretch-collected dataset.
- **[Diffusion Policy](diffusion-policy.md)** uses Franka Panda for three of its four real-world tasks: 6-DoF mug flipping (90% success), sauce pouring (79%), and periodic sauce spreading (100%) ([paper](../sources/diffusion-policy-paper.md) §VI).

The result: when a JEPA-style or VLA-style paper says "real-robot eval" without further qualification in 2024–2026, the default mental model is Franka.

## Why Franka in particular
- **Torque control out-of-the-box** at 1 kHz is unusual for tabletop arms in this price band.
- **Small tabletop footprint** fits academic-lab benches.
- **Open-ish ecosystem** — `franka_ros`, `libfranka`, `frankx` Python bindings, plus widespread MuJoCo / Isaac Sim / Pinocchio models.
- **Existing teleop pipelines** — DROID's Oculus Quest 2 + Franka teleop rig is the most-replicated real-robot data-collection setup of the 2024–2026 cohort.

## In X-VLA's pretraining mixture

Franka appears in **four of [X-VLA](x-vla.md)'s seven pretraining data sources** — `Droid-Left` (15.8%), `Droid-Right` (15.8%), `RoboMind-Franka` (6.7%), and `RoboMind-Dual-Franka` (0.8%) — for **39.1% of 290 K episodes**, more than any other robot type ([X-VLA paper](../sources/xvla-paper.md), Fig. 3). Franka is effectively the reference embodiment of open cross-embodiment pretraining, which is worth keeping in mind when a "cross-embodiment" model's generalization is assessed: a plurality of what it saw was one 7-DOF arm.

The t-SNE of learned [soft prompts](../concepts/learning/soft-prompt-cross-embodiment.md) shows the Franka setups forming a **single cluster** despite being registered as separate data sources, with the two DROID viewpoint variants fully intermingled.

## Related
- [DROID](droid.md) — single-embodiment dataset built on Franka Panda.
- [V-JEPA 2](v-jepa-2.md) / [JEPA-WMs](jepa-wms.md) — JEPA-line real-robot evaluations.
- [Robot Utility Models](robot-utility-models.md) — cross-embodiment transfer target.
- [MuJoCo](mujoco.md) / [Isaac Sim](nvidia-isaac-sim.md) — simulators with Franka models.

## Open questions / TBD
- Panda vs FR3 — which generation is each ingested paper actually using? Mostly unstated in abstracts.
- Adoption of Panda by industrial OEMs — not covered here.
- Companion grippers (Franka Hand, Robotiq 2F-85) deserve their own pages when a specific paper hinges on them.

## Mentioned in
- [How Claude Performs on Robotics Tasks](../sources/anthropic-how-claude-performs-on-robotics-tasks.md) — the manipulation platform (7-DoF, LIBERO kitchen scenes) for direct-LLM control and VLA supervision.
- [DROID](droid.md) (entity)
- [V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)
- [V-JEPA 2.1 Paper](../sources/v-jepa-2-1-paper.md)
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md)
- [Robot Utility Models Project Page](../sources/robot-utility-models-website.md)
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md)
- [Diffusion Policy Paper](../sources/diffusion-policy-paper.md)
- [SERL paper](../sources/serl-paper.md) — the manipulator SERL's impedance controller is designed around; PCB/cable/relocation tasks.
- [HIL-SERL paper](../sources/hil-serl-paper.md) — likely (unconfirmed in text) platform for the impedance-controlled tasks.
- [AutoSERL paper](../sources/autoserl-paper.md) — insertion-task platform (plug + USB insertion) alongside a UR5 for hanging/hinge tasks.
- [UMI Project Page](../sources/umi-paper.md) — Franka is one of two UMI deployment platforms (alongside UR5e); zero-shot cross-embodiment transfer demonstrated.
- [Designing Accessible Robot Communication for Blind People — Huh et al. 2026](../sources/huh2026-accessible-robot-comm.md) — Panda used as the tabletop manipulator for set-table / clear-table tasks in the in-person observational study with blind participants.
- [CaP-X paper](../sources/cap-x-paper.md) — real-robot platform for CaP-RL sim-to-real (84% cube lift / 76% stack after simulation-only RL of a 7B coding model, n=25) and for zero-shot CaP-Agent0 demos.
- [MolmoAct2 GitHub repo](../sources/molmoact2-github-repo.md) — the DROID Franka deployment target; out-of-the-box support claimed.
- [Gemini Robotics 2 blog](../sources/gemini-robotics-2-blog.md) — **Franka Duo** with a Robotiq gripper is the gripper-dexterity platform: precise insertion **89.6%**, tool kitting 78.9%, pick-and-place 74.2%.
- [MolmoAct paper](../sources/molmoact-paper.md) — MolmoAct v1's only real-world platform: single-arm (incl. DROID-style mobile mount for home data) and bimanual Franka; the 10,689-trajectory MolmoAct Dataset is all-Franka.

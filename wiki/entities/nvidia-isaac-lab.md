---
title: NVIDIA Isaac Lab
type: entity
subtype: product
created: 2026-05-06
updated: 2026-09-14
sources: 26
tags: [framework, robot-learning, nvidia, isaac-lab, rl]
---

Open-source modular framework for robot learning and policy training. Sits on top of [NVIDIA Isaac Sim](nvidia-isaac-sim.md) (or other simulators) and lets researchers swap physics backends, define environments, and run massively parallel RL.

## Capabilities
- Pluggable physics backends: PhysX, [Newton](newton-physics-engine.md), NVIDIA Warp, MuJoCo.
- Massively parallel environment vectorization for RL.
- [Isaac Lab-Arena](isaac-lab-arena.md) (now its own page): open-source benchmark-authoring + policy-evaluation extension, v0.3.0 alpha ([GitHub](../sources/isaaclab-arena-github.md)). As of July 2026, Lab-Arena environments can be **registered in the [LeRobot](lerobot.md) Environment Hub (EnvHub)** to train/evaluate GR00T, π, and SmolVLA policies inside the LeRobot ecosystem ([NVIDIA + HF partnership blog](../sources/nvidia-hf-lerobot-open-robotics-blog.md)).
- Bundles [NVIDIA GR00T](nvidia-groot.md) reasoning [VLA](../concepts/learning/vla-models.md) (currently N1.6 GA / N1.7 EA).

## 2026 status
Isaac Lab 3.0 with the GA release of the [Newton physics engine](newton-physics-engine.md) became the default training stack for NVIDIA's "Physical AI" stack at GTC 2026 ([NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)). The official browser-deployable [Isaac Launchable](../sources/isaac-launchable-repo.md) on [NVIDIA Brev](nvidia-brev.md) is still on **Isaac Lab 2.3** as of v1.2.1 (Jan 2026).

## Hardware requirements

Isaac Lab inherits Isaac Sim's RT-core requirement: it cannot run on [Jetson Thor](jetson-thor.md) or any prior Jetson (no RT cores, even in headless mode). NVIDIA's prescribed workflow is to **train on RTX workstation / [DGX Spark](dgx-spark.md) / data-centre GPU**, then deploy the trained policy to Jetson for inference ([Isaac Sim and Isaac Lab on NVIDIA Jetson AGX Thor](../sources/rs-designspark-isaac-sim-on-thor.md)).

## Related
- [Isaac Gym](isaac-gym.md) — the deprecated GPU-physics predecessor this lineage replaces (Preview 4 is final; it also superseded IsaacGymEnvs, OmniIsaacGymEnvs and Orbit).
- [legged_gym](legged-gym.md) — the ETH locomotion library built on Isaac Gym, still the reference point for the corpus.
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md) — the simulator.
- [Newton physics engine](newton-physics-engine.md) — primary physics backend in 2026.
- [NVIDIA Cosmos](nvidia-cosmos.md) — world model for rare scenarios and synthetic data.
- [DGX Spark](dgx-spark.md), [Jetson Thor](jetson-thor.md) — train-side and deploy-side hardware.
- [MuJoCo Playground](mujoco-playground.md) — competing/parallel learning framework with overlapping backends.

## Mentioned in
- [Isaac Lab-Arena GitHub](../sources/isaaclab-arena-github.md) — the Arena extension itself: v0.3.0 alpha on Isaac Lab 3.0 / Isaac Sim 6.0 (main already on 6.1 wheels); Arena-authored environments register back into Isaac Lab's own teleop, Mimic and RL scripts through an external-environment callback.
- [NVIDIA Newton Physics Engine Developer Page](../sources/nvidia-newton-physics-engine-developer-page.md)
- [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)
- [DINO-WM Paper](../sources/dino-wm-paper.md)
- [Farama Foundation Projects Page](../sources/farama-projects-page.md)
- [ManiSkill-HAB Paper](../sources/maniskill-hab-paper.md)
- [Isaac Launchable Repo](../sources/isaac-launchable-repo.md)
- [Isaac Sim and Isaac Lab on NVIDIA Jetson AGX Thor](../sources/rs-designspark-isaac-sim-on-thor.md)
- [Jetson Thor vs DGX Spark](../syntheses/platforms/jetson-thor-vs-dgx-spark.md)
- [NVIDIA GEAR Lab — Publications](../sources/nvidia-gear-publications.md) — Isaac Lab paper (arXiv 2511.04831, Nov 2025) is GEAR-authored.
- [NVIDIA + HF LeRobot partnership blog](../sources/nvidia-hf-lerobot-open-robotics-blog.md) — Lab-Arena ↔ LeRobot EnvHub registration.
- [Larchenko — LeHome deep dive, Part 1](../sources/larchenko-lehome-part1-rl-for-vlas.md) — the [LeHome Challenge 2026](lehome-challenge-2026.md) environment (Isaac Lab 2.3.1 / Isaac Sim 5.1, cloth simulation, keypoint-scored success); ~30 s per rollout episode on an RTX PRO 6000 after the winner's optimisations; per-frame colour/lighting/camera randomisation.
- [Learning to Fold — tech report](../sources/larchenko-learning-to-fold-tech-report.md) — 3–5 Isaac Sim processes per machine (no multi-scene in one process for this environment); physics-state snapshots (particle positions/velocities + joints) restored for replay and hard mining; the renderer-overfit diagnostic (resize path) that predicted the sim-to-real failure.
- [OpenArm documentation](../sources/openarm-docs.md) — `openarm_isaac_lab` (Isaac Sim 5.1 / Isaac Lab 2.3): reach, lift-cube, open-drawer environments, *"officially integrated"* upstream; VR (Quest 3) teleop demonstrated here only.

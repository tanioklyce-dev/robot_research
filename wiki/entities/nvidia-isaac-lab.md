---
title: NVIDIA Isaac Lab
type: entity
subtype: product
created: 2026-05-06
updated: 2026-10-24
sources: 29
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

**Isaac Lab 3.0 general availability was announced at GTC Berlin on 2026-10-21**: *"open source, agent-ready … from desktop to data center using multi-GPU workflows and physics engines including Newton and NVIDIA PhysX"* ([release](../sources/nvidia-isaac-platform-gtc-berlin-2026.md)). Read against the paragraph above, 3.0 was the default stack from spring 2026 but carried an **EA** label until October. The release's own dexterous-manipulation link still points at the `v3.0.0-EA` docs.

## Native BAM servo actuator and Microduck tasks (2026-10-15)

PR #8270, *"[Newton] Add BAM servo actuator and MicroDuck walking tasks"*, added `BamActuatorCfg`. It is a port of [Rhoban](rhoban.md)'s **Better Actuator Models**, simulating a hobby servo in the voltage domain, and it runs as Warp kernels on every physics step:
- a randomly resampled command lag;
- supply sag proportional to summed joint torque;
- a firmware P-law → duty, current-limited;
- DC-motor torque with back-EMF damping;
- BAM friction models m1/m2/m5/m6 applied as a MuJoCo friction constraint.

**It requires the Newton backend with the MJWarp solver.** PhysX raises an error. `backlash_joint_template` adds gearbox play as a passive hinge read through by the firmware. The same PR added `contrib/microduck` flat/rough walking tasks for [Microduck](microduck.md) ([NVIDIA tutorial, verified against the repo](../sources/nvidia-microduck-ai-agents-sim-blog.md)). This makes the [actuator-fidelity](../concepts/learning/actuator-fidelity-sim2real.md) recipe a stock Isaac Lab feature rather than a per-robot subclass.

The same tutorial's reference run fine-tunes a pretrained Microduck walker for ramps with **head-camera depth + robot state** at **4,096 parallel environments on one RTX PRO 6000 Blackwell Workstation Edition**. Training is in the cloud, and validation is in Isaac Sim on a local [RTX Spark](nvidia-rtx-spark.md).

The hands-on companion ([NVIDIA × Pollen on HF](../sources/hf-nvidia-microduck-isaac-lab-sim-to-real.md)) names the tasks `IsaacContrib-Velocity-{Flat,Rough}-MicroDuck`, with `presets=backlash`, `rsl_rl` and 4,096 envs. It claims **up to 1.25M env-steps/s on 16 GPUs** with rough terrain and backlash on; the GPU model is not given. RSL-RL `play` auto-exports `policy.pt` and `policy.onnx`. The ONNX matches Microduck's 61→14 runtime contract and loads on the robot unchanged.

> [!warning] No `develop` branch
> The tutorial's `git clone --branch develop` fails, because `isaac-sim/IsaacLab` has only `main` as of 2026-10-24. NVIDIA's web links to `tree/develop/…` keep working only because GitHub redirects them.

## Hardware requirements

Isaac Lab inherits Isaac Sim's RT-core requirement: it cannot run on [Jetson Thor](jetson-thor.md) or any prior Jetson (no RT cores, even in headless mode). NVIDIA's prescribed workflow is to **train on RTX workstation / [DGX Spark](dgx-spark.md) / data-centre GPU**, then deploy the trained policy to Jetson for inference ([Isaac Sim and Isaac Lab on NVIDIA Jetson AGX Thor](../sources/rs-designspark-isaac-sim-on-thor.md)).

## Related
- [Isaac Gym](isaac-gym.md) — the deprecated GPU-physics predecessor this lineage replaces (Preview 4 is final; it also superseded IsaacGymEnvs, OmniIsaacGymEnvs and Orbit).
- [legged_gym](legged-gym.md) — the ETH locomotion library built on Isaac Gym, still the reference point for the corpus.
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md) — the simulator.
- [Newton physics engine](newton-physics-engine.md) — primary physics backend in 2026.
- [NVIDIA Cosmos](nvidia-cosmos.md) — world model for rare scenarios and synthetic data.
- [DGX Spark](dgx-spark.md), [Jetson Thor](jetson-thor.md) — train-side and deploy-side hardware.
- [mjlab](mjlab.md) — MuJoCo-Warp framework with Isaac-Lab-style ergonomics; Pollen's Microduck stack.
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
- [NVIDIA advances Isaac platform (GTC Berlin, 2026-10-21)](../sources/nvidia-isaac-platform-gtc-berlin-2026.md)
- [Using AI agents to teach Microduck to walk in simulation (NVIDIA)](../sources/nvidia-microduck-ai-agents-sim-blog.md) — native `BamActuatorCfg` (Newton/MJWarp only) and `contrib/microduck` tasks; 4,096-env depth+proprio ramp fine-tune on one RTX PRO 6000.
- [Train in Simulation, Deploy on a Real Robot: Microduck with Isaac Lab 3.0](../sources/hf-nvidia-microduck-isaac-lab-sim-to-real.md) — task IDs, DR list, 1.25M steps/s on 16 GPUs, ONNX auto-export; broken `--branch develop` install line.

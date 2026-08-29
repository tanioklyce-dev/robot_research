---
title: NVIDIA Isaac Sim
type: entity
subtype: product
created: 2026-05-06
updated: 2026-08-27
sources: 25
tags: [simulator, nvidia, omniverse, openusd]
---

NVIDIA's flagship robotics simulation application, built on Omniverse and OpenUSD. Provides photorealistic rendering, synthetic data generation, and a runtime for testing robotic systems before deployment.

## Capabilities
- Photorealistic GPU rendering via Omniverse / RTX.
- OpenUSD-based scene description.
- Synthetic data generation pipelines.
- Library of pre-rigged humanoid, mobile-base, and arm robots.
- Runtime for [NVIDIA Isaac Lab](nvidia-isaac-lab.md) training environments.
- Hosts third-party platforms (e.g. [AGIBOT Genie Sim 3.0](agibot-genie-sim.md)).

## 2026 status
Isaac Sim 6.0 ships in the same release wave as [Isaac Lab 3.0](nvidia-isaac-lab.md) and Omniverse NuRec, with expanded coverage of humanoids and dexterous tasks ([NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)). The official browser-deployable [Isaac Launchable](../sources/isaac-launchable-repo.md) (on [NVIDIA Brev](nvidia-brev.md)) is still on **Isaac Sim 5.1 / Isaac Lab 2.3** as of v1.2.1 (Jan 2026) — useful for tutorials, not the latest stack.

## Hardware requirements

> [!warning] RT cores required — even headless
> Isaac Sim's renderer is built on the RTX pipeline and requires **dedicated ray-tracing (RT) cores**, even when running headless. This rules out **every Jetson** as a host, including [Jetson Thor](jetson-thor.md), whose Blackwell GPU is otherwise capable but omits RT cores by design ([Isaac Sim and Isaac Lab on NVIDIA Jetson AGX Thor](../sources/rs-designspark-isaac-sim-on-thor.md)). Train on an RTX workstation or [DGX Spark](dgx-spark.md); deploy the trained policy to Jetson.

## Teleoperating a simulated robot with the real leader arm

A pattern worth naming, from the [Seeed DLI course](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md): the **same physical leader arm** ([Star Arm 102](star-arm-102.md)) that teleoperates the real follower also drives its simulated twin inside Isaac Sim 4.5, over a **LeRobot Python bridge on UDP `127.0.0.1:5005`**. Both paths emit **LeRobot Dataset v3** with identical modality keys (`action`, `observation.state`, `observation.images.front`, `observation.images.side`) at 30 FPS / 640×480, so sim and real episodes are interchangeable in the training mixture without a conversion step.

Domain randomization is applied per episode reset (object poses, lighting, and the wrist camera) from a JSON config, and task success is scripted from the scene's physics. The human is the entire policy during collection — the simulated arm executes no autonomous trajectory.

The catch, and it is a real one: **the course marks the simulation dataset "optional"** and never includes it in the fine-tuning command. The taught pipeline trains on real data plus [Cosmos](nvidia-cosmos.md)-restyled real data. Isaac Sim's role in this particular "sim-to-real" course is a demonstration path, not a data source.

## Related
- [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — learning framework that runs on Isaac Sim.
- [Newton physics engine](newton-physics-engine.md) — pluggable physics backend.
- [NVIDIA Cosmos](nvidia-cosmos.md) — world model used for synthetic data and rare-event scenes.
- [DGX Spark](dgx-spark.md) — recommended workstation host (Blackwell + RT cores).
- [Jetson Thor](jetson-thor.md) — paired on-robot deploy target (cannot run Isaac Sim itself).
- [NVIDIA](nvidia.md) — vendor.

## Mentioned in
- [A Sim-to-Real VLA Pipeline with Seeed reBot Arm and NVIDIA Isaac](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) — leader-arm-over-UDP teleop into Isaac Sim 4.5; per-reset domain randomization; LeRobot v3 output.
- [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)
- [AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)
- [Using OpenUSD for Modular and Scalable Robotic Simulation](../sources/nvidia-openusd-for-robotic-simulation.md)
- [Building CAD-to-USD Workflows with NVIDIA Omniverse](../sources/nvidia-cad-to-usd-jt-workflows.md)
- [Isaac Launchable Repo](../sources/isaac-launchable-repo.md)
- [Isaac Sim and Isaac Lab on NVIDIA Jetson AGX Thor](../sources/rs-designspark-isaac-sim-on-thor.md)
- [Jetson Thor vs DGX Spark](../syntheses/platforms/jetson-thor-vs-dgx-spark.md)
- [Taking Flight with Dialogue (Lim et al. 2025)](../sources/taking-flight-with-dialogue-px4-drone-agent.md) — used as the rendering + physics engine for PX4 SITL drone simulation (in lieu of PX4's default Gazebo).
- [reBot Arm B601-DM Bundle with Jetson Thor](../sources/seeed-rebot-arm-b601-dm-thor-bundle.md) — Listed among the B601's supported simulation stacks; the [DLI course](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) uses it for parallel data collection.

---
title: PX4 Autopilot
type: entity
subtype: software
created: 2026-05-17
updated: 2026-05-17
sources: 1
tags: [px4, autopilot, uav, drone, open-source, bsd, nuttx, uorb, mavlink, ros2, dronecode]
---

**Vendor / docs**: [docs.px4.io/main/en](https://docs.px4.io/main/en/) — official documentation. Code: [github.com/PX4/PX4-Autopilot](https://github.com/PX4/PX4-Autopilot).

**PX4** — the dominant **open-source autopilot for drones and autonomous vehicles**. BSD 3-Clause licensed; hosted by the [Dronecode Foundation](dronecode-foundation.md) under the Linux Foundation. The flight-stack-of-record for the [Pixhawk](pixhawk.md) hardware standard and 30+ manufacturer-supported boards beyond it. Supports six vehicle classes — multirotor, fixed-wing, VTOL, helicopter, rover, experimental (airships, submarines, balloons, autogyros).

## Current release

- **Stable: v1.16** (recommended for production).
- **v1.17 alpha** in active development.
- `main` branch is rolling alpha.

## Architectural commitments

- **[NuttX RTOS](https://nuttx.apache.org/)** as the base real-time OS.
- **uORB** — micro Object Request Broker; the pub-sub messaging fabric across the flight stack. 100+ message types with versioning for backward compatibility.
- **EKF2** — Extended Kalman Filter for state estimation (attitude / position / velocity).
- **Modular control** — sensor drivers → state estimator → navigation/planning → control allocation → output layer. Each layer swappable; many learning-based controllers ([RAPTOR](#ai--ml-modules) etc.) live in the control or allocation stages.

## Communication protocols

- **[MAVLink](mavlink.md)** — primary telemetry + command protocol (also the language of [QGroundControl](#ground-control--sdks) + [MAVSDK](#ground-control--sdks)).
- **ROS 2 / Micro-ROS via uXRCE-DDS** — translates uORB topics ↔ ROS 2 topics. Native ROS 2 interface library for control, navigation, waypoint missions. The bridge that lets a ROS 2-side agentic stack drive a PX4 UAV.
- **DroneCAN** — hardware-level CAN bus for sensors, ESCs, GPS, power modules.

## AI / ML modules

The PX4 docs site has a **dedicated Neural Networks section** ([PX4 docs ingest](../sources/px4-docs-main.md)):

- **MC NN Control Module (Generic)** — neural-network multicopter control integration.
- **TensorFlow Lite Micro (TFLM)** — on-device inference framework for embedded boards.
- **RAPTOR Adaptive RL NN Module** — reinforcement-learning-based adaptive control. PX4-side analog of the learning-based control work in [Navid Azizan](navid-azizan.md)'s line and [the MIT drone adaptive control source](../sources/mit-drone-adaptive-control.md).
- **NN Module Utilities** — tooling for neural network integration.

Vision / perception with AI integration: collision prevention, precision landing, terrain following, motion capture (VICON / Optitrack / NOKOV), VIO (Realsense T265), optical flow.

## Ground control + SDKs

- **QGroundControl** — official cross-platform ground control station.
- **MAVSDK** — C++ / Python SDK for autonomous control from a companion computer or ground station.
- **Offboard Mode** — receives external trajectory / command stream over MAVLink or ROS 2. The wiring point where a higher-level planner (LLM agent, VLA, etc.) drives the flight stack.

## Simulation

- **Gazebo (new)** — current official sim; multi-vehicle.
- **Gazebo Classic** — legacy.
- **SIH (Simulation in Hardware)** — runs SITL on real flight-controller boards.
- Community: **jMAVSim, FlightGear, JSBSim, AirSim**.
- **HITL (Hardware in the Loop)** — real flight controller, simulated vehicle.

## Why it matters in this wiki

- **The open-source autopilot substrate for [agentic UAVs](../concepts/robotics/agentic-uavs.md).** The [UAVs Agentic AI Survey](../sources/uavs-agentic-ai-survey.md)'s Control layer is, in production, PX4. The wiki's [MIT drone adaptive control](../sources/mit-drone-adaptive-control.md) is the kind of research that lands here over time.
- **Same architectural pattern as ROS 2 ground robots** — pub-sub messaging (uORB ↔ ROS 2 topics), modular stack, simulation bridge. Policies and agent frameworks transfer conceptually.
- **First-class learned-control integration** (RAPTOR, TFLM, MC NN Control) — confirms the PX4 community has institutionalized the ML-controller pattern.
- **Companion-computer split mirrors the wiki's wider compute-split theme** — Pixhawk flight controller for deterministic control, [Jetson](jetson-thor.md) companion for AI inference. Same shape as [Thor + Spark](../syntheses/platforms/jetson-thor-vs-dgx-spark.md) at the embedded / desktop scale; same shape as [Stretch 4](stretch.md)'s NUC + optional Jetson split.

## Related

- [Pixhawk](pixhawk.md) — the dominant hardware standard for PX4 boards.
- [Dronecode Foundation](dronecode-foundation.md) — governance + trademark holder.
- [MAVLink](mavlink.md) — the protocol PX4 speaks to ground stations and companion computers.
- [Jetson Thor](jetson-thor.md) — companion-computer family with documented PX4 carrier boards.
- [Agentic UAVs](../concepts/robotics/agentic-uavs.md) — the concept page PX4 is the substrate for.
- [Navid Azizan](navid-azizan.md) — wiki-tracked learning-based control researcher whose work overlaps with PX4's RAPTOR / MC NN Control modules.

## Mentioned in

- [PX4 Autopilot Documentation (docs.px4.io/main)](../sources/px4-docs-main.md)

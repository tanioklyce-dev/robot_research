---
title: "PX4 Autopilot Documentation (docs.px4.io/main)"
type: source
url: https://docs.px4.io/main/en/
author: Dronecode Foundation + PX4 community
published: continuously updated (this ingest based on the 2026-05-17 build of the `main` branch)
ingested: 2026-05-17
created: 2026-05-17
updated: 2026-05-17
tags: [px4, pixhawk, dronecode, uav, drone, autopilot, mavlink, ros2, uxrce-dds, nuttx, tensorflow-lite-micro, raptor-rl]
---

> [!note] Ingest depth
> **Top-of-tree summary** of the canonical PX4 docs site. ~250+ subpages exist; this page captures the architecture, ecosystem, and AI-relevant subsystems. Deeper ingests of specific subsections (the Neural Networks chapter, the RAPTOR module, the ROS 2 interface library) would each justify their own source pages.

## Summary

**PX4** — the dominant **open-source autopilot for drones and autonomous vehicles**, hosted by the [Dronecode Foundation](../entities/dronecode-foundation.md) under the Linux Foundation. BSD 3-Clause licensed; vendor-neutral; **stable v1.16**, **v1.17 alpha** in active development. Supports six vehicle classes (multirotor, fixed-wing, VTOL, helicopter, rover, experimental — airships, submarines, balloons), 30+ official flight controller boards, and 40+ sensor families. The architectural pattern: **NuttX RTOS + uORB pub-sub messaging + MAVLink telemetry + ROS 2 bridge (uXRCE-DDS)** — analogous to the ROS 2 ecosystem on ground robots, but with hard-real-time guarantees and embedded-class compute.

For this wiki, PX4 is **the open-source autopilot substrate underneath [agentic UAVs](../concepts/robotics/agentic-uavs.md)** — the layer the [UAVs Agentic AI Survey](uavs-agentic-ai-survey.md)'s "Control" tier sits on top of, and the platform the [MIT drone adaptive control work](mit-drone-adaptive-control.md) is the kind of research that lands in over time.

## Project facts

| Axis | Value |
| --- | --- |
| License (code) | **BSD 3-Clause** |
| License (docs) | CC BY 4.0 |
| Governance | **[Dronecode Foundation](../entities/dronecode-foundation.md)** — Linux Foundation Collaborative Project |
| Trademark holder | Dronecode Foundation ("vendor-neutral stewardship") |
| Current stable | **v1.16** |
| In development | v1.17 alpha; `main` alpha |
| Languages | C++ (flight stack), Python (tooling, tests), shell |

## Vehicle types

- **Multicopter** — quad / hex / octo / coax / Y6 / ...
- **Fixed-wing** — conventional + delta + flying-wing
- **VTOL** — Standard, Tailsitter, Tiltrotor
- **Helicopter**
- **Rover** — ground vehicle
- **Experimental** — airships, balloons, submarines, autogyros

## Hardware support

### Flight controllers

The **[Pixhawk](../entities/pixhawk.md) Standard** is the canonical reference family. FMU versions tracked in this ingest:

- **FMUv6X-RT** — NXP MR-VMU-RT1176; Holybro Pixhawk 6X-RT
- **FMUv6X** — Holybro Pixhawk 6X / 6X Pro, CUAV Pixhawk V6X, RaccoonLab FMU6x
- **FMUv6C** — Holybro Pixhawk 6C / 6C Mini, Pix32 v6
- **FMUv5X** — Holybro Pixhawk 5X
- **FMUv5** — Holybro Pixhawk 4, CUAV V5+, CUAV V5 nano
- **FMUv4** — mRo Pixracer
- **FMUv3** — Hex Cube Black, mRo Pixhawk

30+ **manufacturer-supported** boards beyond the Pixhawk Standard (CubePilot, ARK Electronics, ModalAI VOXL 2, etc.). Experimental support for BeagleBone Blue and Raspberry Pi-based platforms (Navio2, PilotPi).

### Companion computers (where AI happens)

PX4's flight controllers run the deterministic control loop; **companion computers** run perception, ML, and high-level planning. Documented carriers:

- **ARK Jetson PAB Carrier** — [Jetson](../entities/jetson-thor.md) module carrier with Pixhawk integration.
- **Holybro Pixhawk Jetson Baseboard** — same shape; Jetson + Pixhawk on one board.
- **Auterion Skynode** — integrated PX4 + companion-computer SoM.
- Raspberry Pi (Pixhawk + RPi configurations; RPi CM4 baseboard).

The split is **architecturally identical to the [Jetson Thor / DGX Spark split](../syntheses/platforms/jetson-thor-vs-dgx-spark.md)** at a smaller scale — deterministic real-time control on one chip, AI inference on another.

## Software architecture

### Core runtime

- **[NuttX RTOS](https://nuttx.apache.org/)** — Apache NuttX real-time OS underneath the flight stack.
- **uORB** — micro Object Request Broker; the publish-subscribe messaging fabric for inter-module communication. 100+ documented message types with V0/V1/V2/V3 versioning for backward compatibility.

### Flight-stack layers (top to bottom)

1. **Sensor drivers** — IMU, GNSS, barometer, etc.
2. **State estimation (EKF2)** — Extended Kalman Filter for attitude / position / velocity.
3. **Navigation & planning** — setpoint generation, trajectory handling, mission planning.
4. **Control allocation** — desired thrust/torque → actuator commands (PWM / DShot / OneShot / DroneCAN).
5. **Mode & flight logic** — flight-mode state machine.
6. **Output layer** — ESC protocols, servo commands, gimbal control.

### Communication protocols

- **[MAVLink](../entities/mavlink.md)** — primary telemetry + command protocol; custom messages + message signing + security hardening documented.
- **ROS 2 / Micro-ROS via uXRCE-DDS** — translates uORB topics to ROS 2 topics. Native ROS 2 interface library for control, navigation, waypoint missions.
- **DroneCAN** — hardware-level CAN bus for sensors, ESCs, power modules, GPS.
- **Serial / I2C / CAN** — port-configurable drivers.

### Ground control + SDKs

- **QGroundControl** — official ground control station; master / stable / daily builds.
- **MAVSDK** — cross-platform C++ / Python SDK for autonomous vehicle control from outside the flight controller.

### Simulation ecosystem

- **[Gazebo](../entities/gazebo.md) (new)** — official, current — vehicles, plugins, worlds, multi-vehicle.
- **Gazebo Classic** — legacy but documented.
- **SIH (Simulation in Hardware)** — software-in-the-loop on real flight-controller hardware.
- **jMAVSim**, **FlightGear**, **JSBSim**, **AirSim** — community-supported.
- **HITL (Hardware-in-the-Loop)** — real flight-controller hardware driving a simulated vehicle.

Pre-built Docker containers documented for reproducible builds.

### Logging

- **ULog** — standardized binary log format; encryption support.
- **Flight Review** — web-based log analysis.
- **PlotJuggler** — real-time uORB data plotting.

## AI / autonomy support (the wiki-relevant part)

PX4's documentation has a **dedicated Neural Networks section** — this is the most direct connection to the wiki's interests:

- **MC NN Control Module (Generic)** — multicopter neural-network control integration.
- **TensorFlow Lite Micro (TFLM)** — on-device inference framework for embedded boards.
- **RAPTOR Adaptive RL NN Module** — reinforcement-learning-based adaptive control. This is the direct PX4-side analog of the kind of learned-controller work tracked in [the MIT drone adaptive control source](mit-drone-adaptive-control.md) and [Navid Azizan's](../entities/navid-azizan.md) learning-based control line.
- **NN Module Utilities** — tooling for neural network integration into the flight stack.

Vision / perception subsystems with AI relevance:

- **Collision Prevention** — obstacle avoidance using rangefinders / vision.
- **Precision Landing** — vision-based landing refinement.
- **Terrain Following / Holding** — altitude maintenance relative to terrain.
- **Motion Capture (MoCap)** — VICON / Optitrack / NOKOV for indoor positioning.
- **Visual Inertial Odometry (VIO)** — Realsense T265 tracking camera support.
- **Optical Flow** — PMW3901 + legacy PX4FLOW for velocity estimation without GPS.

Autonomy modes:

- **Mission Mode** — automated waypoint following with contingency handling.
- **Offboard Mode** — full external control via MAVLink or ROS 2.
- **Return Mode** — autonomous return-to-home with terrain awareness.
- **Failsafe Behaviors** — programmatic responses to GPS loss / low battery / RC loss / geofence breach.
- **Package Delivery Architecture** — dedicated section for delivery mission workflows.
- **Follow Me Mode**, **Orbit Mode**, **Geofence + Rally Points**.

## Why this matters in this wiki

- **First PX4 / Pixhawk / Dronecode coverage.** The wiki had UAV-AI research ([Agentic UAVs concept](../concepts/robotics/agentic-uavs.md), the [UAVs Survey](uavs-agentic-ai-survey.md), [MIT drone adaptive control](mit-drone-adaptive-control.md)) but no entity for the autopilot substrate underneath. PX4 is the open-source flight stack that most of that work is intended to deploy on.
- **Confirms the "real-time control on one chip, AI on another" pattern at the UAV scale.** The Jetson companion-computer carriers (ARK Jetson PAB, Holybro Pixhawk Jetson Baseboard) are the airborne version of the [Jetson Thor + Spark train-vs-deploy split](../syntheses/platforms/jetson-thor-vs-dgx-spark.md) and Stretch 4's NUC-plus-optional-Jetson split.
- **Direct documentation of learned controllers on the flight stack** (RAPTOR Adaptive RL, MC NN Control, TFLM) shows the PX4 community has institutionalized the ML-controller pattern. The wiki's existing learning-control content ([Navid Azizan](../entities/navid-azizan.md)'s SD-LQR + drone adaptive control, [optimal control concept](../concepts/robotics/optimal-control.md)) now has a clean deployment target.
- **Architecturally adjacent to ROS 2 ground robots.** uORB ↔ ROS 2 bridge via uXRCE-DDS means policies trained in ROS 2 (e.g., [stretch_ai](../entities/stretch-ai.md)-style stacks) translate conceptually to PX4-flown UAVs. The wiki's [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) pattern carries over.

## Entities mentioned

- [PX4 Autopilot](../entities/px4-autopilot.md) — the project.
- [Pixhawk](../entities/pixhawk.md) — the flight-controller hardware standard.
- [Dronecode Foundation](../entities/dronecode-foundation.md) — governance.
- [MAVLink](../entities/mavlink.md) — telemetry / command protocol.
- [Jetson Thor](../entities/jetson-thor.md) — companion-computer family for PX4 carriers.

## Concepts touched

- [Agentic UAVs](../concepts/robotics/agentic-uavs.md) — PX4 is the open-source autopilot substrate this concept page implicitly assumes.
- [Optimal control](../concepts/robotics/optimal-control.md) — PX4's control allocation + EKF2 is a production instantiation of classical control alongside the learning-based work in [Navid Azizan's](../entities/navid-azizan.md) line.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — PX4's Offboard mode + ROS 2 bridge is the wiring point where an LLM agent could direct a UAV.

## Open questions / TBD

- **RAPTOR Adaptive RL NN Module specifics** — what RL algorithm, what training pipeline, what hardware does the inference. Deserves its own source-page ingest.
- **TensorFlow Lite Micro on flight controllers** — which Pixhawk FMU variants have enough RAM / Flash to run TFLM models meaningfully? FMUv6X-RT (NXP RT1176) is the most recent and most capable; older FMUs may be too constrained.
- **MC NN Control Module empirical performance** — what's the actual flight envelope vs the classical control allocator? Need a primary paper.
- **PX4 + GR00T or PX4 + a VLA?** No documented direct integration as of this ingest. The companion-computer + uXRCE-DDS path makes it possible; whether anyone has shipped this is an open question.
- **Auterion Skynode** — closed-but-PX4-compatible commercial product; the wiki doesn't have an Auterion entity. Worth a follow-up if Skynode shows up in ingested sources.
- **PX4 ↔ [Newton physics engine](../entities/newton-physics-engine.md) integration** — Newton + OpenUSD is the wiki's emerging unified-sim story for ground robots; PX4 sims through Gazebo / AirSim today. Whether Newton will become a PX4-sim option is worth tracking.

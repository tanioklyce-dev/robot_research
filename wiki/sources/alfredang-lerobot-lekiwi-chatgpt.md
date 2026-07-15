---
title: "alfredang/lerobot — ChatGPT-controlled LeKiwi with onboard Jetson + ROS 2 SLAM"
type: source
url: https://github.com/alfredang/lerobot
author: Alfred Ang (alfredang)
published: 2025
ingested: 2026-07-15
license: not declared in README (LeRobot base is Apache 2.0)
format: github-repo
tags: [lekiwi, jetson-orin-nano, lerobot, ros2, slam, teleoperation, gpt-4o, vla, mobile-manipulator, onboard-compute, integration-pattern]
---

# alfredang/lerobot — ChatGPT-controlled LeKiwi with onboard Jetson + ROS 2 SLAM

## Summary

A community build that runs a [LeKiwi](../entities/lekiwi.md) mobile manipulator with a **[Jetson Orin Nano](../entities/jetson-orin-nano.md) 8 GB mounted onboard as the primary controller** (explicitly replacing the earlier Raspberry Pi, which the README labels the outdated "Early Version"). It layers a **GPT-4o Vision** (OpenAI) decision loop and **[ROS 2](../entities/ros2.md) Humble SLAM** on top of the [LeRobot](../entities/lerobot.md) control stack. Notable to this wiki for two reasons: (1) it is a **documented real example of an onboard-Jetson LeKiwi**, and (2) it demonstrates a concrete — and deliberately loose — **ROS 2 ↔ LeRobot integration pattern**: the two frameworks run side-by-side and exchange data over HTTP/ZMQ sockets rather than through native ROS 2 nodes.

## Key claims

- **Onboard compute is a Jetson Orin Nano 8 GB**, mounted on the LeKiwi base in place of the Raspberry Pi 5. The README shows the RPi version as a historical/"Early Version" photo. Runs Ubuntu 24.04 (Jetson Linux), Python 3.10+, conda.
- **Hardware**: LeKiwi 6-DOF arm + gripper on the 3-wheel omni base; **6-DOF leader arm** for teleop; **front USB webcam 640×480** + **8 MP wrist/gripper camera**; **RPLidar A1** (360° 2D) for SLAM.
- **Three operating modes**: (1) manual **leader–follower teleop** (30 Hz loop); (2) **vision-only autonomous** via GPT-4o; (3) **SLAM-enabled autonomous** navigation.
- **Server/architecture** — three Jetson-hosted services + laptop controllers over TCP/IP (Jetson static IP `192.168.28.23`):
  - `control_robot.py` — motor-control server, **ZMQ PUB-SUB port 5555** (laptop → Jetson); the LeRobot base script, run `--robot.type=lekiwi --control.type=remote_robot`.
  - `robot_vision_server.py` — camera-image **HTTP server port 5001** (Jetson → laptop).
  - `slam_map_server.py` — SLAM-data **HTTP server port 5002** (SLAM mode only).
  - Laptop-side controllers: `chatgpt_lekiwi_final.py` (vision-only) and `chatgpt_lekiwi_slam.py` (SLAM).
- **ROS 2 role**: `ros-humble-slam-toolbox` + `ros-humble-rplidar-ros`, launched as `ros2 launch rplidar_ros rplidar_a1_launch.py` and `ros2 launch slam_toolbox online_async_launch.py` (workspace `ros2_ws_rplidar`). **SLAM output is exposed to the control loop over an HTTP server, not via direct ROS 2 topic subscription** — ROS 2 runs as a parallel process that the laptop polls.
- **GPT-4o Vision loop**: laptop `GET`s dual camera images from `:5001`, sends them to the OpenAI API, receives JSON action commands (e.g. `move_base(x=0.15, y=0, theta=0, duration=3)`), and translates them into ZMQ motor messages. Observation → reasoning → action, one step at a time.
- **No imitation-learning policy** ([ACT](../entities/act.md)/[Diffusion](../entities/diffusion-policy.md)/[SmolVLA](../entities/smolvla.md)) and **no training/eval workflow** — decision-making is direct API calls, not a learned policy. This is a **cloud-VLM-as-brain** design, not an on-edge policy design.
- **Repo layout**: `calibration/lekiwi/`, `docs/`, `media/`, `quick_reference/`, `scripts/` (the five Python entrypoints above). License not declared in the README; acknowledges Hugging Face LeRobot, OpenAI, the ROS 2 community, Seeed Studio, and SLAMTEC.

## Why it matters in this wiki

- **Onboard-Jetson LeKiwi, documented.** Direct evidence for the [J4012-on-LeKiwi fit analysis](../syntheses/projects/j4012-on-lekiwi-base-fit.md): it confirms Jetson-on-LeKiwi works, but the mounted unit is a **bare Orin Nano module** (~Pi footprint that drops into the RPi spot) — not the boxed reComputer Robotics J4012. So it validates the *idea* without validating the large-carrier form factor.
- **A ROS 2 ↔ LeRobot coexistence pattern.** It sidesteps the "LeRobot isn't ROS 2-native" gap (see [lerobot-ros](../entities/lerobot-ros.md), [Rosetta](../entities/rosetta.md)) by **not integrating them at the node level at all** — ROS 2 owns SLAM, LeRobot owns motors, and a thin HTTP/ZMQ shim bridges them. A useful (if crude) contrast to the node-native [ros2-mcp-server](../entities/ros2-mcp-server.md) approach.

## Entities mentioned

- [LeKiwi](../entities/lekiwi.md) · [Jetson Orin Nano](../entities/jetson-orin-nano.md) · [LeRobot](../entities/lerobot.md) · [ROS 2](../entities/ros2.md) · **OpenAI / GPT-4o** (no entity page yet — lint candidate) · [SO-ARM101](../entities/so-arm101.md)

## Concepts touched

- ROS 2 + LeRobot side-by-side integration (HTTP/ZMQ shim vs native nodes) · cloud-VLM-as-brain (GPT-4o) vs on-edge learned policy · onboard vs offloaded compute · 2D LiDAR SLAM (SLAM Toolbox)

## Open questions

- **License** — not declared in the README; unclear whether the LeRobot Apache-2.0 base carries through.
- **Publication date** — repo activity date not captured at ingest.
- **Which physical LeKiwi variant** (Seeed kit vs self-printed) and how the Orin Nano is mechanically mounted (bare module vs dev-kit carrier) — the README shows photos but no mount detail.
- **Latency/reliability** of the round-trip GPT-4o loop for closed-loop manipulation — no metrics given.

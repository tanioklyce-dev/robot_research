---
title: PX4-Autopilot (GitHub repo)
type: source
url: https://github.com/PX4/PX4-Autopilot
author: Dronecode Foundation + PX4 community
published: 2012-08-04
ingested: 2026-06-14
local_path: null
venue: GitHub (PX4/PX4-Autopilot)
license: BSD-3-Clause
format: GitHub repository (C++ flight-stack source)
tags: [px4, pixhawk, dronecode, uav, drone, autopilot, nuttx, sitl, gazebo, mavlink, ros2, cpp, open-source, bsd]
---

> [!note] Companion to the docs ingest
> This is the **code-repo** view of PX4 — build system, SITL, governance, release cadence. The architecture / subsystems / AI-modules detail lives in the [PX4 docs ingest](px4-docs-main.md); the entity is [PX4 Autopilot](../entities/px4-autopilot.md). Minimal overlap by design.

## Summary

**PX4-Autopilot** is the source repository for [PX4](../entities/px4-autopilot.md), "the autopilot stack the industry builds on" — the dominant open-source flight stack for drones and autonomous vehicles, governed vendor-neutrally by the [Dronecode Foundation](../entities/dronecode-foundation.md) under the Linux Foundation. One of the oldest and most-forked robotics repos on GitHub (created **2012-08-04**; ~**12k stars / 15.5k forks** — forks *exceed* stars, reflecting the board-porting fork pattern). Written in **C++**, **BSD-3-Clause** licensed, it runs on **NuttX, Linux, and macOS**. Current stable is **v1.17.0** (2026-05-13). The repo is a build-from-source / SITL-first project: clone with submodules and `make px4_sitl` gets a simulated vehicle running.

## Key claims

- **What it is:** open-source autopilot for multicopter, fixed-wing, VTOL, rover, and experimental platforms (helicopters, autogyros, airships, submarines, boats). Runs on NuttX / Linux / macOS.
- **Build from source:**
  ```bash
  git clone https://github.com/PX4/PX4-Autopilot.git --recursive
  cd PX4-Autopilot
  make px4_sitl                 # build + run software-in-the-loop
  ```
  `--recursive` is mandatory (heavy submodule tree); toolchain setup is in the Development Guide.
- **Docker SITL** (no local toolchain): `docker run --rm -it -p 14550:14550/udp px4io/px4-sitl:latest`.
- **License / governance:** "business-friendly **BSD-3**"; under the **[Dronecode Foundation](../entities/dronecode-foundation.md)** (Linux Foundation); "no single vendor controls the roadmap." Maintainers in `MAINTAINERS.md`; contributor stats via LFX Insights.
- **Release state (2026-06):** **v1.17.0 stable** (released 2026-05-13). *(This supersedes the wiki entity's prior "v1.16 stable / v1.17 alpha" — see staleness note below.)*
- **Repo health:** ~470 watchers; ~1,489 open issues; last push daily (active). Primary language C++.
- **Community:** weekly Developer Call (Dronecode calendar), Dronecode Discord, PX4 Discuss forum, Contribution Guide.

> [!warning] Release version drift
> As of this ingest, **v1.17.0 is the stable release** (2026-05-13). The [PX4 Autopilot entity](../entities/px4-autopilot.md) and the [docs ingest](px4-docs-main.md) (2026-05-17) describe "v1.16 stable / v1.17 alpha" — that captured the pre-release state and is now stale. Entity updated to v1.17.0 at this ingest.

## Entities mentioned

- [PX4 Autopilot](../entities/px4-autopilot.md) — the software this repo implements
- [Dronecode Foundation](../entities/dronecode-foundation.md) — governance / Linux Foundation host
- [Pixhawk](../entities/pixhawk.md) — primary supported flight-controller hardware standard
- [MAVLink](../entities/mavlink.md) — telemetry/command protocol
- [ROS 2](../entities/ros2.md) — uXRCE-DDS bridge for companion-computer integration
- [Gazebo](../entities/gazebo.md) — default SITL simulator

## Concepts touched

- **Open-source autopilot substrate** for [agentic UAVs](../concepts/robotics/agentic-uavs.md) — the same repo a stack like [Taking Flight with Dialogue](taking-flight-with-dialogue-px4-drone-agent.md) drives over ROS 2 / Offboard mode.
- **SITL-first development** — `make px4_sitl` / Docker image as the zero-hardware entry point.
- **Fork-heavy vendor-neutral hardware ecosystem** — forks > stars because manufacturers fork to add board support, the structural signature of a hardware-abstraction flight stack.

## Open questions

- The submodule tree is large; which submodules matter for a learned-controller (Neural Networks / RAPTOR) build vs a vanilla SITL build is not captured here (would need a deeper repo-structure ingest).
- v1.17.0 changelog highlights not extracted — what changed from v1.16 (especially in the Neural Networks / ROS 2 subsystems the wiki cares about)?

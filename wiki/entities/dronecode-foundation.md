---
title: Dronecode Foundation
type: entity
subtype: organization
created: 2026-05-17
updated: 2026-05-17
sources: 1
tags: [dronecode, linux-foundation, governance, px4, mavlink, qgroundcontrol, mavsdk, uav, open-source]
---

**Website**: [dronecode.org](https://www.dronecode.org/)

**Dronecode Foundation** — vendor-neutral non-profit hosting the leading **open-source UAV software projects** under the umbrella of the **Linux Foundation Collaborative Project**. Trademark holder for [PX4](px4-autopilot.md); legal guardian of the project ensuring "no single company owns the name or controls the roadmap" ([PX4 docs ingest](../sources/px4-docs-main.md)).

Same governance shape as the [Farama Foundation](farama-foundation.md) (RL APIs) and the **Linux Foundation Open Source Robotics Alliance** (ROS 2) — non-profit umbrella that holds trademarks + IP for vendor-neutral open-source robotics infrastructure.

## Projects hosted

The Dronecode umbrella spans the major open-source UAV-software components:

- **[PX4 Autopilot](px4-autopilot.md)** — flight-control software.
- **[MAVLink](mavlink.md)** — telemetry / command protocol.
- **QGroundControl** — ground-control station.
- **MAVSDK** — C++ / Python SDK for off-board control.
- **[Pixhawk](pixhawk.md)** — open-hardware flight-controller standard.

## Why it matters in this wiki

- **Vendor-neutral stewardship of UAV open-source infrastructure** — the legal framework that makes [PX4](px4-autopilot.md) usable as a long-term commitment without lock-in risk. Parallels the [Farama Foundation](farama-foundation.md)'s role in RL APIs and the Linux Foundation's role in ROS 2.
- **Concentrates a coherent stack** — PX4 + MAVLink + QGroundControl + MAVSDK + Pixhawk are all under one umbrella. Compare to the ROS 2 world where the analogous components (rclpy, DDS implementations, Nav2, RViz, etc.) are governed by separate organizations.

## Related

- [PX4 Autopilot](px4-autopilot.md) — primary project.
- [Pixhawk](pixhawk.md) — hardware standard.
- [MAVLink](mavlink.md) — protocol.
- [Farama Foundation](farama-foundation.md) — analogous Linux-Foundation-shaped non-profit for RL.

## Mentioned in

- [PX4 Autopilot Documentation (docs.px4.io/main)](../sources/px4-docs-main.md)
- [PX4-Autopilot (GitHub repo)](../sources/px4-autopilot-github.md) — Dronecode-governed, vendor-neutral BSD-3 flight stack ("no single vendor controls the roadmap").

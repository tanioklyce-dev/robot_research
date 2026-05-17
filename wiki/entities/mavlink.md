---
title: MAVLink
type: entity
subtype: protocol
created: 2026-05-17
updated: 2026-05-17
sources: 1
tags: [mavlink, protocol, telemetry, uav, drone, px4, ardupilot, dronecode]
---

**Website**: [mavlink.io](https://mavlink.io/)

**MAVLink** (**M**icro **A**ir **V**ehicle **Link**) — the dominant lightweight messaging protocol for communicating with **drones and other unmanned vehicles**. Standardized as a [Dronecode Foundation](dronecode-foundation.md) project; spoken by [PX4 Autopilot](px4-autopilot.md), ArduPilot, QGroundControl, MAVSDK, MAVROS, and most third-party UAV ground stations and companion-computer libraries.

**Position in the stack** ([PX4 docs ingest](../sources/px4-docs-main.md)):

- **Inside the flight controller**: uORB (PX4's internal pub-sub) is the in-process messaging fabric.
- **Across the radio link** (flight controller ↔ ground station, flight controller ↔ companion computer): **MAVLink** is the wire protocol.
- **In ROS 2 land**: uORB topics get bridged to ROS 2 via uXRCE-DDS, but MAVLink remains the lingua franca for legacy ground-station tooling.

## Features documented in the PX4 docs

- **Custom message support** — extensions for vendor-specific data.
- **Message signing** — authenticated MAVLink for security-sensitive deployments.
- **Security hardening** — encrypted variants and signing keys.
- **Wire format** — compact binary; designed for unreliable serial / radio links.

## Why it matters in this wiki

- **The interoperability layer for drones**, analogous to ROS messages for ground robots — distinct because it's optimized for **low-bandwidth lossy radio links** rather than in-network distributed computing.
- **The integration point where an external agent drives a PX4 UAV**: a companion computer running a higher-level planner (LLM agent, VLA, autonomy controller) communicates with the flight controller over MAVLink (or the ROS 2 bridge layered on top via uXRCE-DDS).
- **Cross-stack standard**: PX4 + ArduPilot both speak it, so MAVLink-side tooling (QGroundControl, MAVSDK) works across both flight-software ecosystems.

## Related

- [PX4 Autopilot](px4-autopilot.md) — primary user.
- [Dronecode Foundation](dronecode-foundation.md) — steward.
- [Pixhawk](pixhawk.md) — hardware that speaks MAVLink to ground / companion.
- [Agentic UAVs](../concepts/robotics/agentic-uavs.md) — the concept page; MAVLink is the wire protocol underneath.

## Mentioned in

- [PX4 Autopilot Documentation (docs.px4.io/main)](../sources/px4-docs-main.md)

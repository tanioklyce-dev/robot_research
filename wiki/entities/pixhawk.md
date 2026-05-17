---
title: Pixhawk
type: entity
subtype: hardware-standard
created: 2026-05-17
updated: 2026-05-17
sources: 1
tags: [pixhawk, flight-controller, autopilot, uav, drone, open-hardware, dronecode]
---

**Pixhawk** — the dominant **open-hardware flight-controller standard** for drones and small autonomous vehicles, stewarded by the [Dronecode Foundation](dronecode-foundation.md). Not a single product but a **specification family** (FMU versions) that multiple manufacturers ship boards against. The canonical hardware target for [PX4 Autopilot](px4-autopilot.md); also runs ArduPilot.

The Pixhawk standard is to drone flight controllers what ROS 2 is to ground-robot middleware — a vendor-neutral specification that fragments the manufacturer landscape (preventing lock-in) while keeping the software interface stable.

## FMU versions tracked

From the [PX4 docs ingest](../sources/px4-docs-main.md):

| FMU version | Reference SoC / class | Boards |
| --- | --- | --- |
| **FMUv6X-RT** | NXP MR-VMU-RT1176 (i.MX RT1176) | Holybro Pixhawk 6X-RT |
| **FMUv6X** | STM32H7 | Holybro Pixhawk 6X / 6X Pro, CUAV Pixhawk V6X, RaccoonLab FMU6x |
| **FMUv6C** | STM32H7 (compact) | Holybro Pixhawk 6C / 6C Mini, Pix32 v6 |
| **FMUv5X** | STM32F7 | Holybro Pixhawk 5X |
| **FMUv5** | STM32F7 | Holybro Pixhawk 4, CUAV V5+, CUAV V5 nano |
| **FMUv4** | STM32F4 | mRo Pixracer |
| **FMUv3** | STM32F4 | Hex Cube Black, mRo Pixhawk |

FMUv6X-RT is the most recent and most capable; FMU lineage stretches back to the original Pixhawk circa 2013 (PX4FMU + PX4IO co-design at ETH Zürich).

## Why a specification (not a product)

The Pixhawk Standard documents:
- Pinouts and connector standards.
- Required peripherals (IMU redundancy, barometer, GNSS interface, etc.).
- Power architecture.
- Sometimes recommended SoC class.

This lets **30+ manufacturer-supported boards** (CubePilot Cube Orange / Orange+ / Yellow, Holybro Durandal / Kakute, ARK Electronics ARKV6X, ModalAI VOXL 2, etc.) ship Pixhawk-compatible products without licensing fees, while [PX4](px4-autopilot.md) and ArduPilot can target a stable hardware abstraction across them all.

## Companion-computer carriers

Several Pixhawk-class products integrate a [Jetson](jetson-thor.md) companion computer:

- **ARK Jetson PAB Carrier** — Jetson module on a PX4-compatible carrier.
- **Holybro Pixhawk Jetson Baseboard** — Jetson + Pixhawk-class flight-controller integration.
- **Auterion Skynode** — proprietary integrated PX4 + companion-computer SoM.

This is the airborne version of the [Jetson Thor / DGX Spark train-vs-deploy split](../syntheses/platforms/jetson-thor-vs-dgx-spark.md): deterministic real-time control on the flight controller, AI inference on the companion computer.

## Why it matters in this wiki

- **Open-hardware standard underneath the [agentic UAVs](../concepts/robotics/agentic-uavs.md) concept** — the layer that makes PX4 + companion-computer AI possible without vendor lock-in.
- **Embedded-class compute reference** — FMUv6X-RT (NXP RT1176) is the most capable Pixhawk-class flight controller, capable of running TensorFlow Lite Micro on-device alongside the control loop. Worth contrasting with the [Jetson Orin Nano / Thor](jetson-thor.md) class when planning where ML inference should live in a UAV stack.

## Related

- [PX4 Autopilot](px4-autopilot.md) — primary software target.
- [Dronecode Foundation](dronecode-foundation.md) — steward.
- [Jetson Thor](jetson-thor.md) — companion-computer family with documented Pixhawk carriers.
- [Agentic UAVs](../concepts/robotics/agentic-uavs.md) — the concept Pixhawk is the hardware substrate for.

## Mentioned in

- [PX4 Autopilot Documentation (docs.px4.io/main)](../sources/px4-docs-main.md)

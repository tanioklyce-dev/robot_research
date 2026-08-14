---
title: Dynamixel
type: entity
subtype: hardware-component
created: 2026-05-28
updated: 2026-05-28
sources: 6
tags: [dynamixel, robotis, bus-servo, motor-sdk, lerobot-supported-sdk, koch-v1]
---

**Dynamixel** — line of **smart serial bus servos** from **ROBOTIS** (South Korea), widely used in research robotics and educational kits. Each servo includes a microcontroller and a serial protocol bus, enabling position/velocity/torque control + telemetry over a single daisy-chained TTL/RS-485 line. **One of two motor-SDK lineages [LeRobot](lerobot.md)'s middleware natively integrates with** ([ICLR 2026 paper §3.1](../sources/lerobot-iclr-2026-paper.md)); the other is [FeeTech](feetech.md).

## Why it matters in this wiki

- **LeRobot middleware native support.** Alongside [FeeTech](feetech.md), Dynamixel is one of only two motor protocols LeRobot's middleware natively speaks. This is the load-bearing detail that determined the LeRobot↔[ROS 2](ros2.md) bridge story — robots using *other* motor lineages (e.g. Hiwonder HX-12H on [ROSOrin Pro](rosorin-pro.md)) need a bridge layer like [Rosetta](rosetta.md).
- **Koch-v1.1** ([LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) Table 1a) uses Dynamixel motors as the bus servo class — the higher-cost (~€670 single) Dynamixel-based alternative to the [SO-ARM101](so-arm101.md) (~€225 single, FeeTech-based).
- **[LeKiwi](lekiwi.md) alt-config** specifies **Dynamixel ROBOTIS Koch v1.1 + XL430 motors** as an alternative to the default FeeTech STS3215 wheel servos ([LeKiwi GitHub](../sources/lekiwi-github.md)).

## Position vs FeeTech

| Dimension | Dynamixel | [FeeTech](feetech.md) |
|---|---|---|
| Origin | ROBOTIS (Korea) | FeeTech (China) |
| Position | Research / education premium tier | Hobby / low-cost tier |
| Typical kit cost (LeRobot platforms) | Koch-v1.1 ~€670 (single) | SO-100/101 ~€225 (single) |
| Notable models | XL430, XM430, XM540 | STS3215, SCS series |
| In LeRobot middleware | ✓ Native SDK integration | ✓ Native SDK integration |

The cost gap (~3×) at otherwise-comparable specs is the main reason SO-10X has come to dominate community-contributed [LeRobotDataset](../sources/lerobot-iclr-2026-paper.md) contributions (50%+ as of Sep 2025).

## Related

- [LeRobot](lerobot.md) — natively integrates the Dynamixel SDK.
- [FeeTech](feetech.md) — the other natively-integrated motor SDK lineage.
- [LeKiwi](lekiwi.md) — supports Dynamixel as an alternative motor config.
- Koch-v1.1 manipulator (no entity page yet) — the Dynamixel-based LeRobot reference arm.

## Mentioned in

- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — §3.1: one of two SDK lineages the middleware natively integrates.
- [LeKiwi GitHub](../sources/lekiwi-github.md) — alternative motor config (Koch v1.1 + XL430).
- [SIGRobotics-UIUC projects page](../sources/sigrobotics-uiuc-projects-page.md) — Dynamixel referenced in lab project history.
- [Rosetta GitHub](../sources/rosetta-github.md) — referenced as part of the SDK lineage Rosetta bypasses (since Rosetta drives robots via ROS 2 topics, not motor SDK direct).

## Open questions / TBD

- Direct ingest of ROBOTIS documentation or Dynamixel SDK reference would let us cite specific torque / position / communication specs.
- **Koch-v1.1 deserves its own entity page** — it's one of the 8 LeRobot-supported platforms ([ICLR 2026 Table 1a](../sources/lerobot-iclr-2026-paper.md)) and the Dynamixel-based price-point reference, but currently has no entity.

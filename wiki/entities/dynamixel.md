---
title: Dynamixel
type: entity
subtype: hardware-component
created: 2026-05-28
updated: 2026-08-27
sources: 7
tags: [dynamixel, robotis, bus-servo, motor-sdk, lerobot-supported-sdk, koch-v1]
---

**Dynamixel** — line of **smart serial bus servos** from **ROBOTIS** (South Korea), widely used in research robotics and educational kits. Each servo includes a microcontroller and a serial protocol bus, enabling position/velocity/torque control + telemetry over a single daisy-chained TTL/RS-485 line. **One of two motor-SDK lineages [LeRobot](lerobot.md)'s middleware natively integrates with** ([ICLR 2026 paper §3.1](../sources/lerobot-iclr-2026-paper.md)); the other is [FeeTech](feetech.md).

## Why it matters in this wiki

- **LeRobot middleware native support.** Alongside [FeeTech](feetech.md), Dynamixel is one of only two motor protocols LeRobot's middleware natively speaks. This is the load-bearing detail that determined the LeRobot↔[ROS 2](ros2.md) bridge story — robots using *other* motor lineages (e.g. Hiwonder HX-12H on [ROSOrin Pro](rosorin-pro.md)) need a bridge layer like [Rosetta](rosetta.md).
- **Koch-v1.1** ([LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) Table 1a) uses Dynamixel motors as the bus servo class — the higher-cost (~€670 single) Dynamixel-based alternative to the [SO-ARM101](so-arm101.md) (~€225 single, FeeTech-based).
- **[LeKiwi](lekiwi.md) alt-config** specifies **Dynamixel ROBOTIS Koch v1.1 + XL430 motors** as an alternative to the default FeeTech STS3215 wheel servos ([LeKiwi GitHub](../sources/lekiwi-github.md)).

- **XL330 on [Microduck](microduck.md)** — the 14 servos of Pollen's $399 biped are XL330-class, and they are the reason the robot's simulator models actuators down to the **voltage control law**. `microduck_rl` uses the **BAM M6** model (Rhoban) — voltage law, back-EMF, Coulomb/Stribeck/load-dependent friction — plus ±1° per-joint backlash, because *"at this scale, actuator fidelity is most of the sim2real gap"* ([Microduck launch](../sources/pollen-robotics-microduck.md)). This is the wiki's only worked example of a published, product-grade actuator model for a bus servo; see [Actuator fidelity in sim-to-real](../concepts/learning/actuator-fidelity-sim2real.md).

## Position vs FeeTech

| Dimension | Dynamixel | [FeeTech](feetech.md) |
|---|---|---|
| Origin | ROBOTIS (Korea) | FeeTech (China) |
| Position | Research / education premium tier | Hobby / low-cost tier |
| Typical kit cost (LeRobot platforms) | Koch-v1.1 ~€670 (single) | SO-100/101 ~€225 (single) |
| Notable models | **XL330** (Microduck), XL430, XM430, XM540 | STS3215, SCS series |
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
- [Microduck — Pollen Robotics launch](../sources/pollen-robotics-microduck.md) — XL330 modeled at the voltage-control-law level (BAM M6) for sim-to-real.
- [Rosetta GitHub](../sources/rosetta-github.md) — referenced as part of the SDK lineage Rosetta bypasses (since Rosetta drives robots via ROS 2 topics, not motor SDK direct).
- [`pollen-robotics/microduck` — the onboard runtime](../sources/microduck-runtime-repo.md) — Confirms the [Microduck](microduck.md) servo layout from the runtime side: **15 motor slots, 14 policy-driven** (index 9, the beak, held at zero), IDs `20–24 / 30–34 / 10–14` on a single shared serial bus read by one `sync_read` per 50 Hz tick.

## Open questions / TBD

- Direct ingest of ROBOTIS documentation or Dynamixel SDK reference would let us cite specific torque / position / communication specs.
- **Koch-v1.1 deserves its own entity page** — it's one of the 8 LeRobot-supported platforms ([ICLR 2026 Table 1a](../sources/lerobot-iclr-2026-paper.md)) and the Dynamixel-based price-point reference, but currently has no entity.

---
title: FeeTech
type: entity
subtype: hardware-component
created: 2026-05-28
updated: 2026-08-13
sources: 5
tags: [feetech, bus-servo, motor-sdk, lerobot-supported-sdk, sts3215, sts3250, so-arm, low-cost, hello-robot, sourccey]
---

**FeeTech** — Chinese manufacturer of **low-cost smart serial bus servos**, the dominant motor lineage in the affordable open-source robotics tier of 2024–2026. Like [Dynamixel](dynamixel.md), each servo includes a microcontroller and a daisy-chained serial protocol (TTL/RS-485). **One of two motor-SDK lineages [LeRobot](lerobot.md)'s middleware natively integrates with** ([ICLR 2026 paper §3.1](../sources/lerobot-iclr-2026-paper.md)); the other is [Dynamixel](dynamixel.md). The cost advantage (~3× cheaper than Dynamixel at otherwise-comparable specs) is the main reason FeeTech-based platforms ([SO-100/101](so-arm101.md), [LeKiwi](lekiwi.md)) have come to dominate community-contributed LeRobot datasets.

## Why it matters in this wiki

- **LeRobot middleware native support.** Alongside [Dynamixel](dynamixel.md), FeeTech is one of only two motor protocols LeRobot's middleware natively speaks. Robots using *other* motor lineages (e.g. Hiwonder HX-12H on [ROSOrin Pro](rosorin-pro.md)) need a bridge layer like [Rosetta](rosetta.md).
- **The price-point enabler.** The cheapest tabletop arm in LeRobot's official lineup, [SO-100/101](so-arm101.md), at **~€225 single (€550 bimanual)**, is FeeTech-based — vs ~€670 for the Dynamixel-based Koch-v1.1 ([ICLR 2026 paper Table 1a](../sources/lerobot-iclr-2026-paper.md)).
- **Community-contribution dominance.** SO-10X drives **50%+ of all LeRobotDataset-format community contributions** as of Sep 2025 ([ICLR 2026 paper §3.2](../sources/lerobot-iclr-2026-paper.md)) — a direct consequence of FeeTech's affordability.

## Notable models

- **STS3215** — the workhorse: 12V, 1:345 gear ratio, used in [LeKiwi](lekiwi.md)'s 3-wheel Kiwi-drive base ([LeKiwi GitHub](../sources/lekiwi-github.md)).
- **STS3250** — higher-torque sibling of the STS3215; paired with it on [Sourccey](sourccey.md), where the two are mixed within one arm so the load-bearing joints (shoulder pitch, elbow pitch at 50 kg-cm) get more torque than the wrist and gripper joints (30 kg-cm) ([Vulcan specs](../sources/vulcan-robotics-sourccey-site.md)).
- **SCS series** — alternative line; lower torque, similar protocol.
- **[Sourccey](sourccey.md)** runs 12 servos (6 per arm) on a **daisy-chained UART bus at 1,000,000 baud** with per-servo unique IDs (1–6 left, 7–12 right) through a **Waveshare Bus Servo Driver**, plus 15 kg-cm FeeTech motors in the leader arms. It also documents two properties this wiki had not recorded for the family: **absolute position feedback at 0–4095 counts**, and **"limited backdrivability due to high resistance under load"** — the latter matters for leader-follower teleop feel and for contact safety on any FeeTech-based arm ([Vulcan specs](../sources/vulcan-robotics-sourccey-site.md)).
- **Stretch 4** uses Feetech servos on its **24V RS485 tool bus** ([Stretch 4 datasheet](../sources/hello-robot-stretch-4-datasheet.md)).

## Position vs Dynamixel

See the comparison table in [Dynamixel](dynamixel.md).

## Related

- [LeRobot](lerobot.md) — natively integrates the FeeTech SDK.
- [Dynamixel](dynamixel.md) — the other natively-integrated motor SDK lineage.
- [SO-ARM101](so-arm101.md) — primary FeeTech-based LeRobot platform.
- [LeKiwi](lekiwi.md) — uses STS3215.
- [Sourccey](sourccey.md) — STS3215 + STS3250 mixed within one arm.
- [Stretch](stretch.md) — uses Feetech servos on the Stretch 4 tool bus.

## Mentioned in

- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — §3.1: one of two SDK lineages the middleware natively integrates.
- [Stretch 4 Datasheet (Rev 5)](../sources/hello-robot-stretch-4-datasheet.md) — 24V Feetech RS485 tool bus.
- [SIGRobotics-UIUC projects page](../sources/sigrobotics-uiuc-projects-page.md) — Feetech motor selection in LeKiwi.
- [Rosetta GitHub](../sources/rosetta-github.md) — referenced as part of the SDK lineage Rosetta bypasses.

## Open questions / TBD

- Direct ingest of FeeTech documentation / SDK reference would let us cite specific torque / current / protocol specs.
- **HX-12H** (Hiwonder bus servo on [ROSOrin Pro](rosorin-pro.md)) is **not** FeeTech-compatible — explicitly a third lineage. This deserves its own page someday given how often it's the gating constraint for LeRobot integration.

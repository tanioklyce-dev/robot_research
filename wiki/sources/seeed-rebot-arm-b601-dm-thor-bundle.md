---
title: "reBot Arm B601-DM Bundle with Jetson Thor (Seeed Studio product page)"
type: source
url: https://www.seeedstudio.com/reBot-Arm-B601-DM-Bundle-with-Jetson-Thor.html
author: Seeed Studio
published: 2026-08-27
ingested: 2026-08-27
venue: Seeed Studio store
format: product page
tags: [seeed-studio, rebot-arm, b601-dm, damiao, robot-arm, jetson-thor, vla, groot, lerobot, isaac-sim, open-hardware, buying-decision]
---

# reBot Arm B601-DM Bundle with Jetson Thor

> [!note] Provenance
> Seeed's store is a JS-rendered Magento SPA — `WebFetch` returns only the visible summary block and misses the spec table entirely. The **full spec table below was extracted from the JSON-escaped `PRODUCT_DETAIL_*` payload embedded in the raw HTML** (`curl` + unescape), which is the page's own primary spec source. Prices are the per-component `data-price-amount` values on the same page, captured **2026-08-27**. `published` records the capture date, not a publication date — store pages carry none.

## Summary

Seeed's **reBot Arm B601-DM** is a **6+1-DOF, fully open-source, CAN-bus benchtop robot arm** built on [Damiao](../entities/damiao.md) quasi-direct-drive actuators, sold either bare (**$1,499**) or bundled with an **[NVIDIA Jetson AGX Thor](../entities/jetson-thor.md) Developer Kit** ($5,499) as a one-box [VLA](../concepts/learning/vla-models.md) deployment rig. It is the tier **above** the FeeTech-servo hobby arms ([SO-ARM101](../entities/so-arm101.md), [LeKiwi](../entities/lekiwi.md)) that dominate the [LeRobot](../entities/lerobot.md) ecosystem in this wiki, and **below** the $20k+ research manipulators — a gap the wiki had no entry in. Seeed pairs it with a free 19-module [NVIDIA DLI sim-to-real course](seeed-nvidia-dli-rebot-sim-to-real-course.md), which is the substantive part of the offering.

## Specifications (vendor spec table, verbatim)

| Parameter | reBot Arm B601-DM Assembled Kit with Gripper |
|---|---|
| Degrees of Freedom | **6+1** (6 arm joints + gripper) |
| Reach | **767 mm** (607 mm without gripper) |
| Payload | **1.5 kg** (without gripper, 70%-reach recommended) |
| Repeatability | **0.2 mm** |
| Weight | ~4.7 kg |
| Joint range | J1 ±150°; J2 −220–0°; J3 −220–0°; J4 ±90°; J5 ±90°; J6 ±90°; gripper −325–0° |
| Servos | **DM-J4340P-2EC ×3** (high-torque, low-noise) + **DM-J4310-2EC ×4** |
| Operating temperature | −20 °C to 50 °C |
| Power | **DC 24 V 10 A** |
| Software | ROS 1 ✅, ROS 2 ✅, MoveIt 1 ✅, MoveIt 2 ✅, Python ✅, LeRobot ✅, Isaac Sim ✅, Pinocchio ✅, Open source ✅ |

> [!warning] The payload figure is qualified, and the qualification matters
> **1.5 kg is "without gripper, 70% reach recommended."** The usable payload at full 767 mm extension with a gripper attached is unstated and is necessarily lower. Do not quote 1.5 kg as an end-of-arm figure in a build.

## Bundle contents and pricing (captured 2026-08-27)

The listing is a **component bundle** — each line is priced and quantity-selectable rather than sold at a single bundle SKU price (SKU `E26052001`, 2% off applied at checkout).

| Component | Price |
|---|---|
| reBot Arm B601-DM, assembled, without power supply | $1,499.00 |
| NVIDIA Jetson AGX Thor Developer Kit (945-14070-0080-000) | $5,499.00 |
| Power Adapter Kit for reBot Arm B601-DM | $59.00 |
| **Base bundle subtotal** | **$7,057.00** (≈ $6,916 after the 2% discount) |

Configurable axes on the listing: **Robot Arm** (B601-DM "Versatile Robotics" / B601-RS "High Performance"), **Assembly** (Assembled / Unassembled), **AI Computing Platform** (None / Jetson Orin / Jetson Thor), **Kit Type** (Robot Arm + Gripper / Complete Kit / DIY Kit). The **arm alone at $1,499** is therefore the number that matters for anyone who already owns compute.

### Notable optional add-ons

- **[Star Arm 102](../entities/star-arm-102.md) leader arm** — $200. Required for teleoperation; the vendor's own buying guide says to add it plus a 12 V 2 A adapter if you intend to teleoperate.
- **Depth cameras** — Orbbec Gemini 2 $240 / Gemini 335LG $449 / Gemini 336 $310 ([Orbbec](../entities/orbbec.md)); Intel RealSense D435i $419.99 / D405 $419.99; SLAMTEC Aurora S $800.
- **Robotic-Arm Data Collection Box** — $59.
- **6-inch G-clamp** — $14.70. **Not optional in practice**: the vendor states a mounting clamp is *required* to fix the arm to a bench.
- XT30 (2+2) wire harnesses $8 each; XT30 2+2 power separation board $5.

In the box: assembled arm with gripper ×1, hex key wrench set ×1, mouse pad ×1. **No power supply** — the $59 adapter kit is a separate line.

## Key claims

- **"Truly 100% open-source"** in both hardware and software: BOM lists, hardware drawings, software, and algorithms, published under [Seeed-Studio](https://github.com/Seeed-Studio) on GitHub. This is the page's central marketing claim and its differentiator versus other arms at this price.
- **Jetson AGX Thor pairing is pitched at on-robot VLA inference** — the page names **GR00T, π (Pi), and OpenVLA** as models the bundle is meant to run locally, at "2070 TFLOPS." (That TFLOPS figure is NVIDIA's **FP4-sparse** number for the T5000 — see [Jetson Thor](../entities/jetson-thor.md); it is a peak-arithmetic spec, not a VLA throughput claim.)
- **Application framings** the page advertises: edge-LLM **voice control** on Thor; **GraspNet-Baseline visual grasping** with an Orbbec Gemini 2 (YOLO detection → point cloud → GraspNet → hand-eye calibration); **teleoperation + imitation learning** via LeRobot; **assistive automation for home daily tasks**; precision work in constrained environments.
- **Free courses are promised as an ongoing deliverable** — *"as the project progresses, we will gradually update the latest algorithms and launch a series of completely free courses."* The DLI course is the first instance.

## DM vs RS — the actual product decision

The same listing sells two mechanically similar arms with **different actuator lineages**, and the specs diverge materially:

| | **B601-DM** (this page) | **B601-RS** ([DLI course](seeed-nvidia-dli-rebot-sim-to-real-course.md) §1.4) |
|---|---|---|
| Motors | [Damiao](../entities/damiao.md) DM-J4340P-2EC ×3 + DM-J4310-2EC ×4 | [Robstride](../entities/robstride.md) 06 ×3 + 00 ×4 |
| Reach | 767 mm | 754 mm |
| Payload | 1.5 kg | **2.5 kg** rated / 5 kg max |
| Repeatability | 0.2 mm | **< 0.1 mm** |
| Weight | ~4.7 kg | 6.5 kg |
| Power | 24 V 10 A | **48 V 15 A** |
| Positioning | "Versatile Robotics" | "High Performance" |

The RS is the heavier, stiffer, higher-voltage arm; the DM is lighter and cheaper to power. Software-side the split is real too — LeRobot addresses them as **`seeed_b601_dm_follower`** (Damiao USB-CAN adapter on `/dev/ttyACM0`) versus **`seeed_b601_rs_follower`** (SocketCAN on `can0`), with different joint-limit signs and control modes. See the course source page for the observed command lines.

## Entities mentioned

- [Seeed Studio](../entities/seeed-studio.md) — vendor
- [reBot Arm B601](../entities/rebot-arm-b601.md) — the arm family
- [Damiao](../entities/damiao.md) / [Robstride](../entities/robstride.md) — the two actuator lineages
- [Star Arm 102](../entities/star-arm-102.md) — the matching leader arm
- [Jetson Thor](../entities/jetson-thor.md) — bundled compute
- [NVIDIA GR00T](../entities/nvidia-groot.md), [π0](../entities/pi-zero.md), [OpenVLA](../entities/openvla.md) — named target policies
- [LeRobot](../entities/lerobot.md), [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md), [ROS 2](../entities/ros2.md) — supported stacks
- [Orbbec](../entities/orbbec.md) — camera options

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md)
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md)
- [Imitation learning](../concepts/learning/imitation-learning.md)

## Open questions

- **What is the actual end-of-arm payload with the gripper attached at full reach?** The vendor qualifies 1.5 kg away from both conditions and publishes no curve.
- **Is the gripper's 7th DOF force-controlled or position-only?** The course's LeRobot config exposes `gripper_mit_kp/kd/torque_limit` on the RS variant, implying MIT-mode impedance control, but the DM config in the same course shows no gripper-torque parameters. Unresolved from either page.
- **Repeatability under what test?** 0.2 mm is stated with no load, speed, or ISO 9283 reference.
- **Backdrivability.** Quasi-direct-drive CAN actuators should backdrive far better than the [FeeTech](../entities/feetech.md) STS3215 gearboxes the wiki documents as poorly backdrivable, which would matter for compliant contact tasks — but neither page measures it.
- **No published VLA success rates on this arm.** The DLI course demonstrates a working pick-and-place but reports no success-rate number.

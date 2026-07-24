---
title: LeKiwi
type: entity
subtype: robot
created: 2026-05-10
updated: 2026-07-15
sources: 12
tags: [lekiwi, mobile-manipulator, kiwi-drive, holonomic, sigrobotics-uiuc, lerobot, low-cost, raspberry-pi, open-source]
---

**Open-source hardware:** [github.com/SIGRobotics-UIUC/LeKiwi](https://github.com/SIGRobotics-UIUC/LeKiwi) (Apache 2.0). Commercial kits via [Seeed Studio](seeed-studio.md).

**LeKiwi** — low-cost, open-source **3-wheel holonomic Kiwi-drive mobile manipulator** from [SIGRobotics-UIUC](sigrobotics-uiuc.md). Apache 2.0. 1,300+ GitHub stars / 138 forks as of ingest. Sold commercially by [Seeed Studio](seeed-studio.md); designs and code maintained by SIGRobotics. Designed as a low-cost imitation-learning data-collection platform within the [LeRobot](lerobot.md) ecosystem. The base typically mounts an [SO-ARM101](so-arm101.md) arm to function as a full mobile manipulator.

## Specs

- **Drive**: 3-wheel Kiwi (holonomic / omnidirectional) using **3× STS3215 servo motors** (12V, 1:345 gear ratio)
- **Encoders**: 12-bit magnetic angle sensors
- **Wheels**: 3× omnidirectional **4-inch (~102 mm) VEX omni**, mounted at **120° intervals** ([LeKiwi GitHub](../sources/lekiwi-github.md))
- **Base plate**: **~216 × 213 mm** footprint (roughly a ~216 mm disc/rounded-triangle), **two stacked layers @ 7 mm each** — measured from the CAD bounding box of `3DPrintMeshes/base_plate_layer{1,2}.stl` in the [LeKiwi repo](../sources/lekiwi-github.md). The **arm mounts dead-center** on the second-layer top plate (4× M5×25); the **Raspberry Pi mounts on that same second-layer plate**. See [Does a J4012 fit on a LeKiwi base?](../syntheses/projects/j4012-on-lekiwi-base-fit.md) for the mounting-clearance analysis.
- **Compute**: **Raspberry Pi 5** (4–16 GB RAM); software requires Python 3.10, PyTorch 2.6
- **Power**: two options — 12V 5A Li-ion battery (heavier payload) OR 65W laptop power bank (5V, lighter)
- **Communication**: UART motor control; USB-C interface on motor control board; wireless streaming of joint angles + camera feeds for compute-offload to a laptop
- **Cameras**: workspace + wrist-mounted RGB; depth camera optional
- **Chassis**: 3D-printed (PLA+, 0.2 mm layer, 15% infill, 150 mm/s)
- **Operating temperature**: 0–40 °C
- **Arm options**: standard config = [SO-ARM101](so-arm101.md); alternative variant uses **Dynamixel ROBOTIS Koch v1.1 + XL430 motors**
- **Stacking convention**: 3.5 mm mounting holes on 20 mm spacing — modular accessory plate convention

## Why it matters in this wiki

LeKiwi is the **canonical sub-$1k holonomic mobile-manipulator base** in the LeRobot ecosystem. It anchors a low-cost research stack:

- **Below it**: educational mobile robots like [TurtleBot](turtlebot.md) (no manipulation) and [ROSOrin Pro](rosorin-pro.md) (manipulation but smaller-form-factor).
- **Above it**: [Stretch](stretch.md) at ~$20k (sturdier base, lift mechanism, integrated arm) is the next price point.
- **Composed**: [XLeRobot](xlerobot.md) bolts two SO-ARM101 arms onto a LeKiwi-class base to reach a $660 dual-arm household manipulator.

For the wiki's assistive-robotics and accessible-robotics themes, LeKiwi is the platform that makes "buy hardware, train an IL policy, deploy in a home" possible at hobbyist budgets — an important data point for the "democratization of household robotics" trajectory.

## Distribution model

- **Design authority**: [SIGRobotics-UIUC](sigrobotics-uiuc.md) (CAD: Manav Chandaka, Bhargav Chandaka, Pepijn Kooijmans; software: Pepijn Kooijmans, Gloria Wang, Bhargav Chandaka, Advait Patel)
- **Commercial hardware sales**: [Seeed Studio](seeed-studio.md) bazaar
- **Software framework**: [LeRobot](lerobot.md) ([Hugging Face](hugging-face.md))
- **Community**: Discord on the LeRobot server, channel `#mobile-so100-arm`

## Repository status

- **License**: Apache 2.0
- **Stars**: 1,300+
- **Forks**: 138
- **Commits**: 95
- **Issues / PRs**: 6 / 4 (active development pace)
- **No formal release tags** as of ingest

## Related

- [LeRobot](lerobot.md) — software framework
- [SIGRobotics-UIUC](sigrobotics-uiuc.md) — design authority
- [Seeed Studio](seeed-studio.md) — distributor
- [SO-ARM101](so-arm101.md) — standard arm option
- [FeeTech](feetech.md) — STS3215 wheel servos
- [Dynamixel](dynamixel.md) — alternative motor option (ROBOTIS Koch v1.1 + XL430)
- [XLeRobot](xlerobot.md) — downstream composition (dual-arm)
- [Stretch](stretch.md) — the price-point above
- [ROSOrin Pro](rosorin-pro.md) — adjacent educational-tier kit

## Mentioned in

- [LeKiwi GitHub](../sources/lekiwi-github.md)
- [Seeed Studio LeRobot LeKiwi Wiki](../sources/seeed-lekiwi-wiki.md)
- [XLeRobot Documentation](../sources/xlerobot-docs.md)
- [LeRobot Worldwide Hackathon 2025 — All Winners](../sources/lerobot-worldwide-hackathon-2025-winners.md) — LeKiwi was prize hardware in 22 of 30 ranked positions (top-3 + 6th–24th).
- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — listed at **~€230** in Table 1a as the canonical mobile-manipulator platform; BOM citation in Appendix A.
- [alfredang/lerobot — ChatGPT LeKiwi + onboard Jetson + ROS 2 SLAM](../sources/alfredang-lerobot-lekiwi-chatgpt.md) — a documented onboard-**Jetson Orin Nano** LeKiwi build (Jetson replaces the RPi); GPT-4o Vision brain + SLAM-Toolbox; a HTTP/ZMQ ROS 2↔LeRobot shim.

## Onboard-Jetson examples in the wild

The stock LeKiwi ships a [Raspberry Pi 5](raspberry-pi-5.md) and offloads heavy compute to a laptop, but Jetson-on-LeKiwi is a real, documented swap:

- **[alfredang/lerobot](../sources/alfredang-lerobot-lekiwi-chatgpt.md)** — a **Jetson Orin Nano 8 GB mounted on the base**, explicitly replacing the RPi ("Early Version"), running LeRobot + ROS 2 Humble SLAM + a GPT-4o vision loop. The closest documented case to a stock 3-wheel LeKiwi carrying a Jetson.
- **[Cutting the Cord (Shaw et al., 2026)](../sources/cutting-the-cord-untethered-xlerobot.md)** — the measured, peer-reviewed onboard-**Orin Nano** build, but on the LeKiwi-*class* [XLeRobot](xlerobot.md) (dual-arm on an IKEA cart), not the round 3-wheel plate.

> [!note] Caveat for large carriers
> Both documented mounts use a **bare Orin Nano module** (~Pi footprint, drops into the RPi spot). Neither validates the boxed **reComputer Robotics J4012** (130×121×66 mm) — see [Does a J4012 fit on a LeKiwi base?](../syntheses/projects/j4012-on-lekiwi-base-fit.md) for why the large carrier needs a raised-tier mount instead.

## Open questions / TBD

- Reliability and uptime in real-world use (no benchmark data ingested).
- Payload limits with SO-ARM101 mounted; Kiwi-drive holonomic dynamics under non-trivial top-load.
- Maintenance trajectory: SIGRobotics is a student org with normal succession risk.

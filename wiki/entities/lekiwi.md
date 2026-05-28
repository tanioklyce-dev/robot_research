---
title: LeKiwi
type: entity
subtype: robot
created: 2026-05-10
updated: 2026-05-28
sources: 7
tags: [lekiwi, mobile-manipulator, kiwi-drive, holonomic, sigrobotics-uiuc, lerobot, low-cost, raspberry-pi, open-source]
---

**Open-source hardware:** [github.com/SIGRobotics-UIUC/LeKiwi](https://github.com/SIGRobotics-UIUC/LeKiwi) (Apache 2.0). Commercial kits via [Seeed Studio](seeed-studio.md).

**LeKiwi** — low-cost, open-source **3-wheel holonomic Kiwi-drive mobile manipulator** from [SIGRobotics-UIUC](sigrobotics-uiuc.md). Apache 2.0. 1,300+ GitHub stars / 138 forks as of ingest. Sold commercially by [Seeed Studio](seeed-studio.md); designs and code maintained by SIGRobotics. Designed as a low-cost imitation-learning data-collection platform within the [LeRobot](lerobot.md) ecosystem. The base typically mounts an [SO-ARM101](so-arm101.md) arm to function as a full mobile manipulator.

## Specs

- **Drive**: 3-wheel Kiwi (holonomic / omnidirectional) using **3× STS3215 servo motors** (12V, 1:345 gear ratio)
- **Encoders**: 12-bit magnetic angle sensors
- **Wheels**: 3× omnidirectional
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
- [XLeRobot](xlerobot.md) — downstream composition (dual-arm)
- [Stretch](stretch.md) — the price-point above
- [ROSOrin Pro](rosorin-pro.md) — adjacent educational-tier kit

## Mentioned in

- [LeKiwi GitHub](../sources/lekiwi-github.md)
- [Seeed Studio LeRobot LeKiwi Wiki](../sources/seeed-lekiwi-wiki.md)
- [XLeRobot Documentation](../sources/xlerobot-docs.md)
- [LeRobot Worldwide Hackathon 2025 — All Winners](../sources/lerobot-worldwide-hackathon-2025-winners.md) — LeKiwi was prize hardware in 22 of 30 ranked positions (top-3 + 6th–24th).
- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — listed at **~€230** in Table 1a as the canonical mobile-manipulator platform; BOM citation in Appendix A.

## Open questions / TBD

- Reliability and uptime in real-world use (no benchmark data ingested).
- Payload limits with SO-ARM101 mounted; Kiwi-drive holonomic dynamics under non-trivial top-load.
- Maintenance trajectory: SIGRobotics is a student org with normal succession risk.

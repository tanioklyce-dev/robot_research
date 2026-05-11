---
title: XLeRobot
type: entity
subtype: robot
created: 2026-05-10
updated: 2026-05-10
sources: 1
tags: [xlerobot, mobile-manipulator, dual-arm, lerobot, lekiwi, so-arm101, low-cost, household-robot, embodied-ai]
---

**XLeRobot** — $660 household **dual-arm mobile manipulator** built by [Gaotian "Vector" Wang](vector-wang.md). Composes two [SO-ARM101](so-arm101.md) arms (~40 cm reach each) onto a [LeKiwi](lekiwi.md)-class wheeled base, with optional cameras and Raspberry Pi compute. 90% 3D-printed. Apache 2.0. Version 0.3.0 released August 30, 2025. Project tagline: *"Bring Embodied AI to Every Family Around the World" at a price cheaper than an iPhone*.

Repository: [github.com/Vector-Wangel/XLeRobot](https://github.com/Vector-Wangel/XLeRobot). Docs: [xlerobot.readthedocs.io](https://xlerobot.readthedocs.io).

## Specs

- **Arms**: 2× [SO-ARM101](so-arm101.md), each ~40 cm reach, 600–1000 g payload
- **Base**: wheeled mobile platform inspired by [LeKiwi](lekiwi.md) / Bambot
- **3D-printed**: 90% of mechanical parts
- **Assembly time**: < 4 hours
- **Optional sensors**: RGB camera, stereo RGB, **RealSense RGBD depth**
- **Compute**: optional Raspberry Pi
- **Form factor**: fixed height (no lift); uses an IKEA cart in the developer kit as a torso/base

## Pricing

- **Basic configuration**: $660 USD (~€680, ¥3999 CN, ₹87,000 IN)
- **Developer assembly kit**: $579 worldwide (excludes battery + IKEA cart)
- **Taobao**: ¥3,699

## Software

- Framework: **[LeRobot](lerobot.md)** (Hugging Face)
- Simulation: **[ManiSkill](maniskill.md)** with URDF support
- Control interfaces: keyboard, **Xbox**, **Switch Joycon**, **VR (Quest 3)**
- RL sim2real workflow (contributor Zhuoyi Lu)
- Imitation-learning + reinforcement-learning environments

## Capabilities & limitations (per the docs)

**Claimed capabilities**: household chores, indoor tasks, plant care, delivery, manipulation roughly comparable to $30k+ commercial bimanual robots.

**Acknowledged limitations**:
- Fixed height — no lifting platform (cf. [Stretch](stretch.md)'s lift mechanism)
- Workspace smaller than Aloha-class
- No in-hand dexterity
- Payload <1 kg
- No dynamic motion

**Safety positioning**: low-torque motors deliberately chosen to limit harm potential — a tradeoff that makes the platform plausible for household deployment.

## Contributors

- **Creator**: [Vector Wang](vector-wang.md) (Gaotian Wang)
- **RL sim2real**: Zhuoyi Lu
- **Documentation**: Nicole Yue
- **Simulation assets**: Yuesong Wang

## Why it matters in this wiki

XLeRobot is the **cheapest dual-arm mobile manipulator** documented in this wiki. It compresses a research-grade configuration into a ~$660 BOM by aggressively reusing existing open-hardware lineage:

- Arm = [SO-ARM101](so-arm101.md) (The Robot Studio, open-source)
- Base = [LeKiwi](lekiwi.md)-class (SIGRobotics-UIUC)
- Software = [LeRobot](lerobot.md) (Hugging Face)
- Sim = [ManiSkill](maniskill.md) (Hillbot lineage)

This composition pattern — **buy-no-new-IP, glue together with 3D-printed brackets and Apache-2.0 software** — is becoming the dominant cost-reduction strategy in the affordable-manipulation space, and XLeRobot is one of its clearest expressions. Useful counterpoint to [Stretch](stretch.md) (~$20k, integrated single-arm with lift), the [Reachy 2](reachy.md) (~$50k, dual-arm with integrated AI compute), and [Fauna Sprout](fauna-robotics.md) (humanoid developer platform).

## Related

- [Vector Wang](vector-wang.md) — creator
- [LeKiwi](lekiwi.md) — base lineage
- [SO-ARM101](so-arm101.md) — arm
- [LeRobot](lerobot.md) — software
- [ManiSkill](maniskill.md) — sim
- [Stretch](stretch.md) — adjacent (single-arm, integrated, ~30× more expensive)
- [Reachy 2](reachy.md) — adjacent (dual-arm, professional)

## Mentioned in

- [XLeRobot Documentation](../sources/xlerobot-docs.md)

## Open questions / TBD

- Real-world task-success numbers vs. published household-manipulation benchmarks (RoboCasa365, BEHAVIOR-1K, OK-Robot dataset). Currently qualitative claims only.
- Reproducibility for a non-expert assembler: 4-hour estimate is generous; does the price hold including the inevitable 3D-print failures?
- The "comparable to $30k+ commercial bimanual robots" claim deserves scrutiny — payload and workspace numbers suggest it's narrower than that comparison implies.

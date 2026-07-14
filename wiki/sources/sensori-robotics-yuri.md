---
title: "Sensori Robotics — Yuri (company site)"
type: source
url: https://sensorirobotics.com/
author: Sensori Robotics
published: 2026-07-13
ingested: 2026-07-13
venue: sensorirobotics.com (company product page)
tags: [manipulator, bimanual, mobile-manipulation, physical-ai, teleoperation, lerobot, open-hardware, vla, jetson]
---

# Sensori Robotics — Yuri (company site)

## Summary

Sensori Robotics (Southlake, TX, USA) sells **Yuri**, a **dual-arm ("14-DOF") bimanual manipulation platform for Physical AI development**, positioned explicitly as *"a complete Physical AI Robot, not a box of parts"* — integrated hardware, software, and support rather than a self-assembled kit. Yuri ships in two configurations: **Yuri Desktop** (benchtop bimanual) and **Yuri Mobile** (the same arms on a wheeled **OpenBase** platform for room-scale autonomy). The pitch is a **day-one data-collection and policy-training stack**: bilateral force-feedback teleoperation out of the box, [LeRobot](../entities/lerobot.md)-format recording, and support for modern [VLA](../concepts/learning/vla-models.md) policies (GR00T, π0.x, X-VLA, SmolVLA). Its arms and base are released as open hardware — **OpenArm+** and **OpenBase** (github.com/SensoriRobotics; docs.openarm.dev) — placing Sensori in the same "commercial-integrator on top of open hardware" niche as the [LeRobot](../entities/lerobot.md) ecosystem, but at a research-lab (not hobbyist) price tier and with US-based support.

> [!note] Product-page ingest, dated to ingest date
> `published` is set to the ingest date because a company landing page carries no publication date. Specs below are vendor claims from the site, not independently verified. Pricing is quote-only ("Tell us what you want to build… We'll follow up with details, pricing, and availability"), so no price tier is confirmed.

## Key claims

**Positioning**
- "A complete Physical AI Robot, not a box of parts" — integrated hardware + software + support, **"Built & Supported in USA."**
- Target users: robotics research labs / teams working on Physical AI, VLA models, imitation learning, and autonomous manipulation.

**Manipulation hardware**
- **"14-DOF OpenArm+ manipulation"** = two **7-DOF arms**.
- Parallel grippers; **backdrivable joints**; **real-time torque feedback**.
- Extended arm reach "optimized for bins and tabletops"; **adjustable arm height** for different lab benches.
- Cameras: **2× wrist RGB** + **head Intel RealSense D435i** depth camera with IMU.

**Compute & control**
- **NVIDIA Jetson AGX Orin (64 GB, 275 TOPS)** onboard.
- **ROS 2 Humble** preconfigured; **CAN-FD** arm control.

**Teleoperation (the headline differentiator)**
- **OpenLeader** force-feedback leader arms — **bilateral (force) feedback included** out of the box.
- **Meta Quest 3 / 3S** teleoperation for "spatial, whole-body demonstration capture."
- Local Wi-Fi operation.

**Mobility (Yuri Mobile)**
- **OpenBase** directional wheeled platform.
- Hot-swappable battery; hardware **and** wireless e-stop.

**Software stack**
- Sensori browser-based setup web app; calibration + recording pre-integrated.
- **[LeRobot](../entities/lerobot.md) dataset recording** — synchronized cameras, joints, grippers, base state.
- **MCAP** logging + **Foxglove** visualization.
- Simulation assets shipped as **URDF/MJCF** for [MuJoCo](../entities/mujoco.md), [Isaac Lab](../entities/nvidia-isaac-lab.md), and [Genesis](../entities/genesis.md).
- VLA policy support named: **GR00T, π0.x, X-VLA, SmolVLA.**

**Open-source components**
- github.com/SensoriRobotics — OpenArm+, OpenBase, documentation.
- docs.openarm.dev — OpenArm developer docs.

**Other**
- A separate offering, **"Landscape Robotics,"** is referenced at landscape.sensorirobotics.com (no detail on the main page).

## Entities mentioned

- [Sensori Robotics](../entities/sensori-robotics.md) — the company.
- [Yuri](../entities/yuri.md) — the robot.
- [LeRobot](../entities/lerobot.md), [MuJoCo](../entities/mujoco.md), [Isaac Lab](../entities/nvidia-isaac-lab.md), [Genesis](../entities/genesis.md), [Jetson AGX Orin](../entities/jetson-orin-nano.md) (Orin family), [ROS 2](../entities/ros2.md).
- VLA policies referenced: [GR00T](../entities/nvidia-groot.md), π0 ([Physical Intelligence](../entities/physical-intelligence.md)), [SmolVLA](../concepts/learning/vla-models.md), X-VLA.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — Yuri is a data-collection + eval rig for exactly this class of policy.
- [Imitation learning](../concepts/learning/imitation-learning.md) — bimanual demonstration collection is the primary use case.
- Bimanual / mobile manipulation — see [robot platforms comparison](../syntheses/platforms/robot-platforms-comparison.md).

## Open questions

- **Price tier unknown.** Quote-only. The AGX Orin 64 GB + dual 7-DOF torque arms + force-feedback leaders put it well above the [XLeRobot](../entities/xlerobot.md) ($660–1.3k) educational tier — likely research-grade ($10k+), but unconfirmed. Where it sits vs. [Mobile ALOHA](../entities/aloha.md) ($32k, also bimanual + whole-body teleop) is the natural comparison.
- **Team / funding.** No founder names, team, or funding disclosed on the site.
- **"OpenArm+" vs upstream OpenArm.** The site describes OpenArm+ as an extended-reach variant; relationship to any prior "OpenArm" project (docs.openarm.dev) is not spelled out.
- **Is Yuri a "humanoid"?** The extraction described it as a "dual-arm humanoid," but the specs (two arms + wheeled base, no legs) make it a **bimanual mobile manipulator**, not a legged humanoid — closer to [Reachy 2](../entities/reachy.md) / [XLeRobot](../entities/xlerobot.md) / [Mobile ALOHA](../entities/aloha.md) than to a G1/Optimus-class humanoid.

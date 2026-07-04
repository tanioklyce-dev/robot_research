---
title: i2RT YAM Arm Documentation
type: source
url: https://doc.i2rt.com/products/yam.html
author: i2RT Robotics
published: 2026 (docs, continuously updated)
ingested: 2026-07-04
format: web (product docs)
license: MIT (code repo)
tags: [yam, i2rt, robot-arm, teleoperation, data-collection, can-bus, mujoco, affordable, groot]
---

## Summary

Product documentation for **[YAM](../entities/yam.md)** ("Yet Another Manipulator") — i2RT Robotics' flagship **6-DOF, CAN-bus tabletop robot arm designed for real-world research and embodied-AI data collection**, priced **$2,999–$4,999**. Notable in this wiki because **two YAM arms are the "bimanual YAM" teleop platform in [GR00T N1.6](groot-n1_6.md)'s training data** — a low-cost data-collection arm that made it into an NVIDIA foundation-model corpus.

## Key claims

- **6 DOF**, CAN bus (1 Mbit/s), **DM-series brushless motors**; control modes: joint-position PD, gravity compensation, zero-gravity (hand-guiding); 400 ms motor timeout safety default.
- **Four variants**: YAM ($2,999; 3× DM4340 + 3× DM4310), YAM Pro ($3,499), YAM Ultra ($4,299; different joint-3 limit), **BIG YAM** ($4,999; 2× DM6248 + 2× DM4340 + 2× DM4310, heavier). **YAM Leader / teaching handle** ($2,999) is a leader-arm teleoperation controller for demonstration collection.
- **Six interchangeable grippers** (crank-shaft GP-4310-CS, linear 4310/3507, flexible-fingertip 4310, teaching handle, none).
- **Software**: Python SDK (`get_yam_robot()`), MuJoCo sim (URDF + MJCF, physics-thread parity via `SimRobot`), Viser web viewer; model-based gravity + Coulomb-friction compensation; gripper force limiting (50 N default). Code at `i2rt-robotics/i2rt` (MIT).
- Reach / payload / repeatability **not specified** in the docs.
- **No mention of LeRobot / ROS 2 / VLA frameworks or GR00T** in the docs (the GR00T connection is documented on the GR00T side, not here).

## Entities mentioned
- [YAM](../entities/yam.md) — this is its primary source. i2RT Robotics (Fremont, CA) — vendor.
- MuJoCo (sim), Viser (viewer), Rovomotor (motors), DM-series motors.

## Concepts touched
- [Imitation learning](../concepts/learning/imitation-learning.md) — YAM's leader/follower teaching handle + zero-gravity mode is a demonstration-collection rig, the data source for BC/VLA training.
- The low-cost teleoperation-arm tier alongside [SO-ARM101](../entities/so-arm101.md), [ALOHA](../entities/aloha.md) leader arms, [Mobile ALOHA](../entities/aloha.md).

## Open questions
- Reach/payload/repeatability unpublished in the docs.
- The docs don't confirm the GR00T link; [GR00T N1.6](groot-n1_6.md) states "bimanual YAM arms" teleop — presumably two YAMs in a leader-follower bimanual rig. Which variant, and whose integration code, is unstated.

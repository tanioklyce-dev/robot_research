---
title: TurtleBot
type: entity
subtype: robot
created: 2026-05-08
updated: 2026-05-08
sources: 0
tags: [turtlebot, ros, education, mobile-robot, willow-garage, open-robotics]
status: stub
---

**TurtleBot** — the **canonical educational ROS mobile robot.** Originated at Willow Garage (2010) as a low-cost open-source platform to teach ROS; has gone through four generations under different stewards. Now maintained by Open Robotics. Most CS / robotics curricula that teach ROS still use TurtleBot as the reference platform.

## Generations
- **TurtleBot 1** (2010, Willow Garage) — Kobuki-style differential-drive base + Asus Xtion / Kinect + netbook compute.
- **TurtleBot 2** (2012, Yujin Robot) — Kobuki base; long-running standard for ROS 1 education.
- **TurtleBot 3** (2017, Robotis) — three variants: **Burger** (smallest), **Waffle**, **Waffle Pi** (Raspberry Pi compute). LDS-01 LiDAR + OpenCR control board.
- **TurtleBot 4** (2022, Clearpath/iRobot) — [[irobot-create-3|iRobot Create 3]] base + Raspberry Pi 4B + RPLIDAR + OAK-D camera. ROS 2-native.

> [!note] Generation-specific specs
> Different TurtleBot generations have very different sensor / compute / footprint configurations. When a paper or curriculum says "TurtleBot," it's worth confirming the version. The most commonly cited contemporary configurations are TurtleBot 3 Waffle Pi (low-end) and TurtleBot 4 (modern).

## Why it matters in this wiki
TurtleBot is the **reference point for educational mobile robotics** — the foil against which newer educational kits like [[rosorin|ROSOrin]] should be understood. Both target the same audience (CS / robotics students learning ROS), but with different generational tradeoffs:

- **TurtleBot 4** uses Raspberry Pi 4B compute (~10× weaker than [[rosorin|ROSOrin]]'s Jetson Orin Nano in TOPS).
- TurtleBot **does not bundle agentic-AI / LLM-agent curriculum** the way [[rosorin|ROSOrin]] (cloud + offline LLM agents) and [[rosorin-pro|ROSOrin Pro]] (OpenClaw) do — its scope ends at ROS 2 + Nav2 + standard SLAM.
- TurtleBot generally **lacks a manipulator arm**. ROSOrin Pro adds 6-DOF manipulation while keeping the educational tier.

The interesting comparison: **ROSOrin / ROSOrin Pro is roughly "what you'd get if you took TurtleBot's educational role, dropped a Jetson Orin Nano in, and bundled an LLM-agent curriculum on top."** Hiwonder is essentially extending the TurtleBot pedagogical lineage with 2024-era agentic-AI tooling.

## Adoption / availability
- **Open-source** hardware designs and software stack (BSD-licensed for most components).
- Sold by multiple vendors per generation (Robotis, Clearpath, etc.).
- Curriculum-friendly: extensive tutorials, ROS 2 documentation, classroom support.

## Related
- [[rosorin|ROSOrin]] / [[rosorin-pro|ROSOrin Pro]] — modern educational alternatives that extend the TurtleBot recipe with Jetson compute + agentic-AI workflows.
- [[stretch|Stretch]] — research-tier mobile manipulator (the next tier up from the educational class).
- [[hello-robot|Hello Robot]] — analogous role for research-tier; Robotis / Clearpath play that role for education-tier.

## Mentioned in
- *(no source pages directly cite TurtleBot yet; referenced in [[index|index.md]] gaps as a comparison point for ROSOrin)*

## Open questions / TBD
- **No primary source ingested.** Open Robotics / TurtleBot.com page would let us confirm current generation specs and pricing.
- Specific TurtleBot-4-vs-ROSOrin spec comparison would benefit from primary sources on both.
- Whether any contemporary research paper still uses TurtleBot as a real-robot platform (the educational role is clear; the research-platform role has largely moved to Stretch / Franka).

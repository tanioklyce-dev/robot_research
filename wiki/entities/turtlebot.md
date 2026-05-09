---
title: TurtleBot
type: entity
subtype: robot
created: 2026-05-08
updated: 2026-05-09
sources: 1
tags: [turtlebot, ros, education, mobile-robot, willow-garage, clearpath, open-robotics]
---

**TurtleBot** — the **canonical educational ROS mobile robot.** Originated at Willow Garage (2010) as a low-cost open-source platform to teach ROS; has gone through four generations under different stewards. Now maintained by Open Robotics. Most CS / robotics curricula that teach ROS still use TurtleBot as the reference platform.

## Generations
- **TurtleBot 1** (2010, Willow Garage) — Kobuki-style differential-drive base + Asus Xtion / Kinect + netbook compute.
- **TurtleBot 2** (2012, Yujin Robot) — Kobuki base; long-running standard for ROS 1 education.
- **TurtleBot 3** (2017, Robotis) — three variants: **Burger** (smallest), **Waffle**, **Waffle Pi** (Raspberry Pi compute). LDS-01 LiDAR + OpenCR control board.
- **TurtleBot 4** (2022, Clearpath/iRobot) — [iRobot Create 3](irobot-create-3.md) base + Raspberry Pi 4B (4 GB) + RPLIDAR-A1 + OAK-D camera. ROS 2-native. Max speed 0.31 m/s; 9 kg payload (15 kg custom); 2.5–4 hr runtime. Two variants: Standard (OLED + OAK-D-PRO, 3.9 kg) and Lite (OAK-D-LITE, 3.3 kg, no display). Manufactured by Clearpath Robotics (Rockwell Automation). ([Clearpath TurtleBot 4 page](../sources/clearpath-turtlebot-4.md))

> [!note] Generation-specific specs
> Different TurtleBot generations have very different sensor / compute / footprint configurations. When a paper or curriculum says "TurtleBot," it's worth confirming the version. The most commonly cited contemporary configurations are TurtleBot 3 Waffle Pi (low-end) and TurtleBot 4 (modern).

## Why it matters in this wiki
TurtleBot is the **reference point for educational mobile robotics** — the foil against which newer educational kits like [ROSOrin](rosorin.md) should be understood. Both target the same audience (CS / robotics students learning ROS), but with different generational tradeoffs:

- **TurtleBot 4** uses Raspberry Pi 4B compute (~10× weaker than [ROSOrin](rosorin.md)'s Jetson Orin Nano in TOPS).
- TurtleBot **does not bundle agentic-AI / LLM-agent curriculum** the way [ROSOrin](rosorin.md) (cloud + offline LLM agents) and [ROSOrin Pro](rosorin-pro.md) (OpenClaw) do — its scope ends at ROS 2 + Nav2 + standard SLAM.
- TurtleBot generally **lacks a manipulator arm**. ROSOrin Pro adds 6-DOF manipulation while keeping the educational tier.

The interesting comparison: **ROSOrin / ROSOrin Pro is roughly "what you'd get if you took TurtleBot's educational role, dropped a Jetson Orin Nano in, and bundled an LLM-agent curriculum on top."** Hiwonder is essentially extending the TurtleBot pedagogical lineage with 2024-era agentic-AI tooling.

## Adoption / availability
- **Open-source** hardware designs and software stack (BSD-licensed for most components).
- Sold by multiple vendors per generation (Robotis, Clearpath, etc.).
- Curriculum-friendly: extensive tutorials, ROS 2 documentation, classroom support.

## Related
- [ROSOrin](rosorin.md) / [ROSOrin Pro](rosorin-pro.md) — modern educational alternatives that extend the TurtleBot recipe with Jetson compute + agentic-AI workflows.
- [Stretch](stretch.md) — research-tier mobile manipulator (the next tier up from the educational class).
- [Hello Robot](hello-robot.md) — analogous role for research-tier; Robotis / Clearpath play that role for education-tier.

## Mentioned in
- [Clearpath TurtleBot 4 product page](../sources/clearpath-turtlebot-4.md)

## Open questions / TBD
- Pricing not listed by Clearpath; sold via distributors.
- ROS 2 version (Humble, Iron, or Jazzy) not specified on product page.
- Whether any contemporary research paper still uses TurtleBot as a real-robot platform (the educational role is clear; research-platform role has largely moved to Stretch / Franka).

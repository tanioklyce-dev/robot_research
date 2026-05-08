---
title: iRobot Create 3
type: entity
subtype: robot
created: 2026-05-08
updated: 2026-05-08
sources: 0
tags: [irobot, create-3, mobile-robot, ros2, education, roomba, turtlebot-base]
status: stub
---

**iRobot Create 3** — mobile-robot research / education base from iRobot. Built on the **Roomba i3 chassis** but stripped of vacuum hardware, with a developer interface (UART / Ethernet) and **native ROS 2 support**. Released 2022. Forms the **base of [TurtleBot 4](turtlebot.md)**.

## Specs
- Differential-drive base from the Roomba i3.
- ~$549 standalone (more affordable than building a base from scratch).
- ROS 2 interface (Galactic, Humble, current).
- Cliff sensors, bump sensors, IR/optical floor tracking.
- Battery + auto-docking from Roomba lineage.
- No onboard compute or sensors beyond what Roomba ships — researchers add their own (Raspberry Pi / Jetson + cameras + LiDAR).

## Why it matters in this wiki
- **The base under [TurtleBot 4](turtlebot.md).** When TurtleBot 4 is referenced, Create 3 is the underlying chassis.
- **Affordable ROS 2 mobile base.** $549 + a Raspberry Pi 4 or Jetson Orin Nano + commodity sensors gets a researcher a functional ROS 2 mobile robot for ~$1k–$2k total. Below educational-kit pricing, similar functionality.
- **iRobot lineage — quiet, reliable, battery-managed.** The chassis benefits from years of consumer-Roomba engineering: docking, battery management, low-noise drive.

## Position vs alternatives
- **Cheaper than TurtleBot 4 turnkey** — Create 3 alone is ~$549; TurtleBot 4 (Create 3 + Pi + sensors + frame) is ~$2k–$3k.
- **Less integrated than [ROSOrin](rosorin.md)** — ROSOrin ships with Jetson Orin Nano + LiDAR + depth + voice + LLM-agent curriculum; Create 3 is just the base, you build the rest.
- **Different niche than the educational-kit market.** Create 3 targets developers / researchers who want to build their own platform; ROSOrin / TurtleBot target classrooms that want turnkey.

## Related
- iRobot — manufacturer.
- [TurtleBot](turtlebot.md) — TurtleBot 4 uses Create 3 as base.
- [ROSOrin](rosorin.md) — competing educational mobile-robot kit (more integrated).
- [Robot platforms comparison](../syntheses/robot-platforms-comparison.md) — base-tier hardware context.

## Mentioned in
- *(no source pages directly cite Create 3; entity built from general knowledge)*

## Open questions / TBD
- **No primary source ingested.** iRobot Education site + ROS 2 documentation would anchor specs.
- Adoption breakdown — how many TurtleBot 4 deployments vs standalone Create 3 users — not in any source here.
- Future generations — Create 4? — not yet announced as of 2026-05.

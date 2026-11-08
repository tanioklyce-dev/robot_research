---
title: Alias Robotics — Robot Immune System (RIS) product page
type: source
url: https://aliasrobotics.com/ris.php
local_path: raw/2026-11-08-alias-robotics-ris-page.md
sha256: a91d7118b19ec9ed3e8c85fa79e2fe251fa8005f5f862729405bc3244bdea084
author: Alias Robotics
published: Unknown (retrieved 2026-11-08)
ingested: 2026-11-08
tags: [alias-robotics, ris, endpoint-protection, robot-security, ros, iec-62443, primary-source]
---

# Alias Robotics — Robot Immune System (RIS)

## Summary

Vendor marketing page, read on 2026-11-08, for the [Robot Immune System](../entities/robot-immune-system.md), endpoint-protection software installed on the robot. It covers industrial cobots, AMRs and older ROS releases. No home robot or humanoid is listed. Parts of the page look dated, and all figures are the vendor's own.

## Key claims

- **What it is.** A "Robot Endpoint Protection Platform" installed in the robot or component, with modules for firewall, hardening, logging, visualization and "AIS," a "bio-inspired artificial intelligence."
- **Listed robots.** Universal Robots (UR3, UR5, UR10, UR16e and e-series), many KUKA KR models, MiR 100–1000, UVD Robots, Enabled Robotics.
- **ROS support.** ROS Kinetic and Melodic. ROS 2 Dashing is marked "Coming soon."
- **Certification.** The page calls RIS "security certified" and says it "meets the software component requirements of IEC 62443 part 4-2." It names no certifying body.
- **Tech specs (v2.0.0).** 823 vulnerabilities patched and deployed; 100 µs maximum added latency; 80 MB RAM; 220 MB disk; 6% CPU on a UR3's Intel Celeron at 1.99 GHz. A false-positive rate is given "as of Sept 2020," but the figure extracts as "01 %" and its exact value is unclear.
- **Named deployments.** RPK (from July 2020), Vicomtech (from December 2020), EDI Latvia and Joanneum Research (from early 2021), and a demonstration with Kaspersky.

> [!warning] Contradiction — adaptive or static?
> This page says RIS "adapts to its environment and evolves over time" and has an AI module that "adapts to incoming security threats." Alias's own [2026 consumer-robot paper](cai-hacking-consumer-robots-paper.md) calls RIS's approach "static, rule-based" and says it "is not designed to counter AI-powered attacks." The paper is newer, and it is written by the people who build the product.

> [!note] How current is this page?
> The dated evidence stops in early 2021, the false-positive figure is from September 2020, and ROS 2 Dashing, listed as "Coming soon," reached end of life years ago. The [research page](alias-robotics-research-page.md) shows the EIC-funded RIS project continuing, so the product may have moved on without this page being updated.

## Entities mentioned

- [Robot Immune System](../entities/robot-immune-system.md)
- [Alias Robotics](../entities/alias-robotics.md)
- [ROS 2](../entities/ros2.md)

## Concepts touched

- [Robot security](../concepts/robotics/robot-security.md)
- [Robot safety standards](../concepts/robotics/robot-safety-standards.md)

## Open questions

- Who certified RIS against IEC 62443-4-2, and for which version?
- Is the 100 µs latency figure measured in a real-time control path?
- Is there any independent test of what RIS blocks? None was found here.

---
title: "YOR: Your Own Mobile Manipulator for Generalizable Robotics (NYU, Feb 2026)"
type: source
url: https://arxiv.org/abs/2602.11150
fetch_url: https://arxiv.org/pdf/2602.11150v1
local_path: raw/yor-2602.11150v1.pdf
sha256: c9a0769d9a83fe8fe5119772afb1589fd87b90fe790120ddc49961aa8286e479
author: Anjaria, Erciyes, Ghatnekar, Navarkar, Etukuru, Jiang, Patel, Kabra, Wojno, Prayage, Chintala, Pinto, Shafiullah, Cui
published: 2026-02-11
ingested: 2026-11-08
tags: [yor, mobile-manipulation, open-source, bimanual, low-cost, agilex-piper, primary-source]
---

# YOR: Your Own Mobile Manipulator

## Summary

[YOR](../entities/yor.md) is an open-source bimanual mobile manipulator from an NYU-led team, with an omnidirectional swerve base and telescopic lift, built for about **US$9,250** in parts. It targets the gap between very cheap kits and $30k-plus bimanual platforms. The published evaluation is a proof of concept, not a household study.

## Key claims

- **Hardware.** Swerve-drive omnidirectional base, passively stable. Telescopic lift with a 63.5 cm stroke that the paper says reaches "from floor level to overhead." Two 6-DoF [AgileX PiPER](../entities/agilex-piper.md) arms ($2,500 each) with custom grippers. 27 kg, 24 V 20 Ah battery, Jetson AGX Orin or Thor, ZED 2i stereo camera. Most of the cost is the arms.
- **Comparison table (from the paper).** YOR has 13 upper-body DoF, 1.5 kg payload per arm, 4–5 hours of battery and costs $9–10k. It lists TidyBot++ at $5–6k plus an arm, XLeRobot at $660 with under 0.3 kg, and Mobile ALOHA at $32k with 1.5 kg.
- **Evaluation.** A learned bimanual box pick, lift and move ran 10 trials: pick 10/10, lift 10/10, locomotion 9/10, total **9/10**. The main failure was odometry drift from head-camera occlusion. The authors describe this as a proof of concept.
- **Openness.** Project page at [yourownrobot.ai](https://yourownrobot.ai).
- **Stated improvement.** Moving to affordable 7-DoF arms.

## Entities mentioned

- [YOR](../entities/yor.md)
- [AgileX PiPER](../entities/agilex-piper.md)
- [Lerrel Pinto](../entities/lerrel-pinto.md)
- [Mahi Shafiullah](../entities/mahi-shafiullah.md)

## Concepts touched

- [Whole-body control](../concepts/robotics/whole-body-control.md)

## Open questions

- No in-home trials or household task results are reported here. How does the 1.5 kg payload fare on real chores?

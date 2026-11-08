---
title: "Demonstrating Mobile Manipulation in the Wild: A Metrics-Driven Approach (TRI, Jan 2024)"
type: source
url: https://arxiv.org/abs/2401.01474
fetch_url: https://arxiv.org/pdf/2401.01474v1
local_path: raw/tri-grocery-mobile-manipulation-2401.01474v1.pdf
sha256: c64decbf3f2a2b933e406f0e1941707cfb3df304f1cd9969415dd25771652a0d
author: Bajracharya, Borders, Cheng, Helmick, Kaul, Kruse, Leichty, Ma, Matl, Michel, Papazov, Petersen, Shankar, Tjersland (Toyota Research Institute)
published: 2024-01-03
ingested: 2026-11-08
tags: [tri, ttt, grocery, retail, mobile-manipulation, field-test, reliability, primary-source]
---

# Demonstrating Mobile Manipulation in the Wild (TRI)

## Summary

[Toyota Research Institute](../entities/tri.md) tested its TTT mobile manipulator on real grocery shopping in an unmodified store, across **six field tests spread over 18 months**. It is the closest published thing to a benchmark for a robot that shops. After 18 months, the robot finished **35.7%** of full shopping runs and retrieved **28.9%** of the listed items. The paper's argument is that end-to-end reliability, not component accuracy, is what decides deployment.

## Key claims

- **Task.** Pick 20 unique items from a randomly generated shopping list, chosen from a map of close to 1,000 items, put them in a basket and return to the start. No human help is allowed unless the robot is about to do something dangerous.
- **Conditions.** Testing ran at night outside opening hours, for safety. Items were mapped in advance. The test excluded produce, refrigerated items, items over 4.5 kg, and glass.
- **Robot.** TTT has 21 DoF, including two 7-DoF arms, a 2-DoF neck and a pseudo-holonomic base. Its arms handle up to 10 kg. It carries a Robotiq HandE gripper on one arm and a custom suction gripper on the other, and nearly all components are custom.
- **Task success.** 21.4% by the third field test on the earlier FMT platform, then **35.7%** at the sixth on TTT. A run counts as a success if the robot attempts all 20 items without an unrecoverable fault or E-stop, so it does not require every pick to work.
- **Shopping success (items retrieved / items listed).** 8.9% in the fifth test, **28.9%** in the sixth.
- **Speed.** About 70% faster across six tests, from six minutes per item to **under two minutes**.
- **Unique items attempted.** 164 in the fifth test, 389 in the sixth.
- **Why reliability dominates.** At 99% reliability per action and 10 actions a minute, overall reliability for a one-hour task is 0.2%.
- **Lessons.** Resets are not viable in the real world, homogeneous hardware is more reliable, and hardware and software have to be co-designed. Learned behaviour was used only for narrow jobs such as stereo and gripper selection.

## Entities mentioned

- [Toyota Research Institute](../entities/tri.md)

## Concepts touched

- [Retail and grocery robotics](../concepts/robotics/retail-and-grocery-robotics.md)
- [Runtime failure detection](../concepts/robotics/runtime-failure-detection.md)

## Open questions

- This wiki found no later TTT field report. Where did task success go after January 2024?
- How much would daytime operation among shoppers cost in reliability?

---
title: "From Pixels to Shelf: An Integrated Robotic System for Autonomous Supermarket Stocking with a Mobile Manipulator"
type: source
url: https://arxiv.org/abs/2509.11740
fetch_url: https://arxiv.org/pdf/2509.11740v2
local_path: raw/pixels-to-shelf-2509.11740v2.pdf
sha256: 1cb63588d7c65fe5cfa8bf867e2cfaf39cce8c786ec0329491a4e357b74b8cf8
author: Davide Peron, Victor Nan Fernandez-Ayala, Lukas Segelmark
published: 2026-06-05
ingested: 2026-11-08
tags: [stretch-3, supermarket, shelf-stocking, retail, behavior-trees, ros2, primary-source]
---

# From Pixels to Shelf

## Summary

A shelf-stocking system built on a commercially available [Stretch 3](../entities/stretch.md) with ROS 2 and [behavior trees](../concepts/robotics/behavior-trees.md). In a **mock supermarket in a lab**, it placed objects successfully more than 98% of the time. This is stocking, not picking a customer's order, and the setup differs from a live store in ways the authors state. The version ingested is v2 (5 June 2026); v1 was submitted in September 2025.

## Key claims

- **Result.** 70 stocking tasks covering **724 stocking operations**. Object-level success exceeded **98%**, task-level success exceeded **87%**.
- **Failures.** 9 of the 70 tasks were unsuccessful. Eight were partial, mainly placement errors linked to small ArUco detection errors. One failed completely after the robot lost the ArUco marker, and needed a person. Most object-level failures occurred during picking, and all picking failures were classification errors.
- **Scope limits.** The 2.5 cm finger width and payload limited the study to cans and small boxes using side grasps. Placement needed 3 cm spacing, against about 3 mm in common practice.
- **Environment aids.** Shelf navigation relies on ArUco markers.

## Entities mentioned

- [Stretch](../entities/stretch.md)
- [Hello Robot](../entities/hello-robot.md)

## Concepts touched

- [Retail and grocery robotics](../concepts/robotics/retail-and-grocery-robotics.md)
- [Behavior trees](../concepts/robotics/behavior-trees.md)

## Open questions

- The authors plan comparisons against teleoperation and human workers. How does cost per stocked item compare?
- Does the result survive real shelf spacing and a real store's shoppers?

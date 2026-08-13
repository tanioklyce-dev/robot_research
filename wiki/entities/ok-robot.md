---
title: OK-Robot
type: entity
subtype: software-framework
created: 2026-05-09
updated: 2026-05-09
sources: 3
tags: [ok-robot, zero-shot, mobile-manipulation, vlm, nyu, open-source]
---

**OK-Robot** — open, modular framework for zero-shot language-conditioned pick-and-drop in arbitrary homes (arXiv 2401.12202). From the NYU robot-learning group ([Mahi Shafiullah](mahi-shafiullah.md), [Lerrel Pinto](lerrel-pinto.md), and collaborators). Predecessor / parallel to [Robot Utility Models](robot-utility-models.md) in the NYU-Stretch manipulation line.

## What it does
Given a natural-language object specification, OK-Robot navigates to the object, picks it, and drops it at a commanded location — in any home, without environment-specific training.

## Architecture
Three integrated open-knowledge modules:
1. VLMs for object detection and recognition
2. Navigation primitives for autonomous movement
3. Grasping primitives for manipulation

Design philosophy: systems-level integration of existing open modules, not novel algorithms. Engineering integration quality is the differentiator.

## Results ([OK-Robot Project Page](../sources/ok-robot-project-page.md))
- **58.5% success rate** across 171 tasks in 10 real NYC homes
- **82%** in uncluttered environments
- **1.8× improvement** over [HomeRobot / OVMM](../sources/ovmm-homerobot.md) baseline
- Top failure modes: semantic memory retrieval (9.3%), manipulation poses (8.0%), hardware (7.5%)

## License
MIT (code).

## Related
- [Mahi Shafiullah](mahi-shafiullah.md) / [Lerrel Pinto](lerrel-pinto.md) — NYU authors
- [Robot Utility Models](robot-utility-models.md) — sibling system from same group
- [Stretch](stretch.md) — likely hardware (NYU-Stretch line)
- [HomeRobot / OVMM](../sources/ovmm-homerobot.md) — comparison benchmark

## Mentioned in
- [OK-Robot Project Page](../sources/ok-robot-project-page.md)

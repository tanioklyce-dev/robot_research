---
title: OK-Robot Project Page
type: source
url: https://ok-robot.github.io/
author: Peiqi Liu, Yaswanth Orru, Jay Vakil, Chris Paxton, Nur Muhammad "Mahi" Shafiullah, Lerrel Pinto
affiliations: NYU
published: 2024-01
ingested: 2026-05-09
tags: [ok-robot, zero-shot, manipulation, vlm, navigation, grasping, nyu, stretch]
---

## Summary
Project page for OK-Robot (arXiv 2401.12202), an open modular framework for zero-shot language-conditioned pick-and-drop in arbitrary homes. Key authors overlap with the [Robot Utility Models](robot-utility-models-paper.md) line ([Mahi Shafiullah](../entities/mahi-shafiullah.md), [Lerrel Pinto](../entities/lerrel-pinto.md)) — OK-Robot is the predecessor or parallel system in the NYU-Stretch manipulation research thread.

## Key claims

- **Zero-shot, no training per environment.** Integrates open-knowledge systems (VLMs, navigation, grasping primitives) without robot-specific training in new homes.
- **58.5% success rate** across 171 pick-and-drop tasks in 10 real-world NYC homes; **82%** in uncluttered environments.
- **1.8× improvement** over prior OVMM (Open Vocabulary Mobile Manipulation) work.
- Top failure modes: semantic memory retrieval (9.3%), difficult manipulation poses (8.0%), hardware difficulties (7.5%).
- Core claim: "The critical role of nuanced details when combining Open Knowledge systems like VLMs with robotic modules" — engineering integration, not just algorithm choice, is what makes it work.
- MIT license (code); CC BY-NC-SA 4.0 (website).

## Architecture
Three integrated components:
1. Vision-Language Models (VLMs) — object detection and recognition
2. Navigation primitives — autonomous movement
3. Grasping primitives — manipulation

Systems-level integration emphasis: no novel algorithms, careful composition of existing modules.

## Entities mentioned
- [Stretch](../entities/stretch.md) — implied hardware platform (NYU-Stretch line)
- [Mahi Shafiullah](../entities/mahi-shafiullah.md) — co-author
- [Lerrel Pinto](../entities/lerrel-pinto.md) — co-author (senior)

## Open questions
- Does OK-Robot use Stretch specifically, or is it hardware-agnostic?
- Exact VLM used (not specified on project page).
- Relationship to [HomeRobot / OVMM](ovmm-homerobot.md) — OK-Robot claims 1.8× over OVMM, so OVMM is the comparison baseline.

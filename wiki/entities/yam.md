---
title: YAM (i2RT)
type: entity
subtype: robot
created: 2026-07-04
updated: 2026-08-03
sources: 5
tags: [yam, i2rt, robot-arm, teleoperation, data-collection, affordable, groot, bimanual, molmoact2]
---

**YAM** ("Yet Another Manipulator") — i2RT Robotics' 6-DOF, CAN-bus **tabletop robot arm for embodied-AI data collection**, $2,999–$4,999 ([docs](../sources/i2rt-yam-docs.md)). A low-cost teleoperation/data-collection arm in the same tier as [SO-ARM101](so-arm101.md) and [ALOHA](aloha.md) leader arms — notable here because **a bimanual pair of YAMs supplied teleop training data for [GR00T N1.6](../sources/groot-n1_6.md)**.

## Specs
- **6 DOF**, CAN bus 1 Mbit/s, DM-series brushless motors; joint-position PD / gravity-comp / zero-gravity control; 400 ms timeout safety.
- Variants: YAM / YAM Pro / YAM Ultra / **BIG YAM** (heavier, DM6248 shoulders) + **YAM Leader** teaching handle for teleoperation.
- 6 interchangeable grippers; Python SDK + MuJoCo sim (URDF/MJCF); MIT-licensed code (`i2rt-robotics/i2rt`).
- Reach/payload/repeatability not published.

## Why it matters in this wiki
- **A GR00T data-source embodiment**: [GR00T N1.6](../sources/groot-n1_6.md) added "several thousand hours" of teleop from **bimanual YAM arms** (with AGiBot Genie1, Galaxea R1 Pro, Unitree G1). YAM is the cheapest of that group — evidence that sub-$5k arms now feed frontier VLA corpora.
- **The bimanual YAM is [MolmoAct2](molmoact2.md)'s flagship deployment platform.** Ai2 collected the **MolmoAct2-BimanualYAM Dataset** — **720 hours, 34.5k demonstrations, 28+ tasks** — on a standardized dual-YAM rig (two YAM arms, RealSense D435/D405 cameras, IKEA table) whose **entire cost is under $6,000** ([MolmoAct2 paper](../sources/molmoact2-paper.md), §3.1). It is **the largest open bimanual manipulation dataset to date**, collected with Cortex AI under strict failure-retry/no-op protocols, and MolmoAct2's real-world eval runs on this exact setup (30 Hz, absolute joint control).
- Fills the "YAM arms" gap flagged during the GR00T N1.6 ingest — and YAM now anchors a released open dataset, not just a proprietary corpus.

## Related
- [MolmoAct2](molmoact2.md) — deploys on bimanual YAM; released the 720-hr open BimanualYAM dataset.
- [GR00T N1.6](nvidia-groot.md) — trained on bimanual YAM teleop data.
- [Galaxea R1](galaxea-r1.md), [Unitree G1](unitree-g1.md), [AgiBot](agibot.md) — the other N1.6 data embodiments.
- [SO-ARM101](so-arm101.md), [ALOHA](aloha.md) — peer low-cost teleoperation arms.
- [Imitation learning](../concepts/learning/imitation-learning.md) — YAM's role is demonstration collection.

## Mentioned in
- [i2RT YAM Arm Documentation](../sources/i2rt-yam-docs.md) — primary source.
- [GR00T N1.6 research page](../sources/groot-n1_6.md) — bimanual YAM teleop data.
- [MolmoAct2 paper (Fang, Duan et al. 2026)](../sources/molmoact2-paper.md) — the BimanualYAM dataset + deployment platform.
- [ASPIRE paper](../sources/aspire-paper.md) — the bimanual YAM station is the real-robot testbed for cross-embodiment skill transfer; sim-discovered skills take drawer opening from 0/20 to 11/20 and cut token cost ~4×.
- [MolmoAct2 GitHub repo](../sources/molmoact2-github-repo.md) — a dedicated MolmoAct2-BimanualYAM checkpoint plus a FastAPI serving path (port 8202); ~26 GB float32 / under 16 GB bf16.

## Open questions
- Bimanual-rig details for the GR00T use (which variant, integration code, leader/follower setup).
- Reach/payload/repeatability, LeRobot/ROS 2 support.

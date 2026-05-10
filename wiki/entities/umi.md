---
title: UMI (Universal Manipulation Interface)
type: entity
subtype: method
created: 2026-05-10
updated: 2026-05-10
sources: 2
tags: [umi, universal-manipulation-interface, hand-held-gripper, in-the-wild-data-collection, diffusion-policy-followon, chi-2024, stanford, columbia, tri]
---

**UMI — Universal Manipulation Interface.** Hand-held gripper data-collection system that lets humans collect manipulation demonstrations *without a robot*. Introduced by Cheng Chi, Zhenjia Xu, Chuer Pan, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Russ Tedrake, Shuran Song (Stanford / Columbia / [TRI](tri.md), RSS 2024 Best Systems Paper Award Finalist, [arxiv 2402.10329](https://arxiv.org/abs/2402.10329)). The direct data-collection-side follow-on to [Diffusion Policy](diffusion-policy.md). Tagline: *"In-The-Wild Robot Teaching Without In-The-Wild Robots."*

## Hardware design

- **Hand-held parallel-jaw gripper** with **wrist-mounted GoPro camera**.
- Captures wrist trajectory, gripping width, RGB video, and depth (via GoPro features).
- **100% calibration-free** (functioning even with base movement).
- Validates demos against robot kinematic constraints during recording.
- Open-source: GitHub repo (`real-stanford/universal_manipulation_interface`), 3D-print files, assembly videos, hardware guide.

## Data-collection profile

- **30 seconds per demonstration**.
- **111 demos / hour** with UMI vs **35 demos / hour** with conventional teleoperation — ~3× faster.
- **2-minute setup** in any new physical location ("portable" claim).

## Software stack

- **Inference-time latency matching** — bridges the cadence gap between human collection and robot control.
- **Relative-trajectory action representation** — actions encoded relative to the wrist frame, making policies *embodiment-agnostic*. Same trained policy runs on UR5e and Franka without retraining.
- **Diffusion Policy** is the canonical policy class for UMI demonstrations (same lead author; no other policy class shown on the project page).

## Demonstrated capabilities

From [UMI Project Page](../sources/umi-paper.md):

1. **Dynamic Tossing** — six-object sorting by *tossing* into bins.
2. **Cup Arrangement** — pick-and-place espresso cups with orientation constraints.
3. **Bimanual Cloth Folding** — coordinated two-arm sweater folding, 6+ sequential steps.
4. **Dish Washing** — seven-step sequence including faucet operation, sponge handling, cleaning verification.

## Generalization claims

- **Zero-shot novel environments and objects** when trained on diverse human demonstrations.
- **Zero-shot cross-embodiment**: same trained policy on UR5e *and* Franka.
- **Out-of-distribution behaviors** (e.g., serving espresso cups on water fountains) demonstrated.

## Why it matters in this wiki

- **Data-collection-side companion to [Diffusion Policy](diffusion-policy.md)** — same lead author. Diffusion Policy advanced the policy class; UMI advances the data pipeline. Together they form a complete BC-for-real-robot stack.
- **Cited as inspiration for [RUM](robot-utility-models.md)'s Stick-v2 gripper** ([RUM paper](../sources/robot-utility-models-paper.md) §2.1). RUM's portable in-home data collection rig is a direct UMI descendant.
- **Validates "diversity of demos > robot teleop volume"** — UMI's pitch is that cheap, diverse, embodiment-agnostic demos generalize better than expensive teleoperation; this is the same thesis [Robot Utility Models](robot-utility-models.md) and [DROID](droid.md) elaborate from different angles.
- **TRI co-authorship anchors a TRI / Stanford / Columbia robotics-foundation-model triangle** — see [TRI](tri.md).

## Related

- [Diffusion Policy](diffusion-policy.md) — predecessor; canonical policy class for UMI data.
- [Robot Utility Models](robot-utility-models.md) — downstream NYU project that cites UMI as Stick-v2 design inspiration.
- [DROID](droid.md) — alternative diversity-first dataset (Franka teleop rather than hand-held gripper).
- [TRI](tri.md) — TRI co-authors (Cousineau, Burchfiel, Feng, Tedrake).
- [Franka Panda](franka-panda.md) — one of two deployment platforms (alongside UR5e).
- [Imitation learning](../concepts/imitation-learning.md) — broader concept.

## Mentioned in

- [UMI Project Page](../sources/umi-paper.md) — primary source.
- [Diffusion Policy](diffusion-policy.md) — predecessor; UMI follows on the same author's earlier work.
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md) — Stick-v2 design inspiration.

## Open questions / TBD

- **Full RSS 2024 paper not ingested** — arxiv 2402.10329; deeper mechanics (latency-matching algorithm, exact relative-trajectory math) come from there.
- **UMI variants** — multi-finger, bimanual UMI rigs, etc. — not covered.
- **Bill of materials / cost** — not extracted from project page.
- **Russ Tedrake** — entity page on demand; senior figure across UMI + TRI + Drake.

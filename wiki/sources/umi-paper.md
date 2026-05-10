---
title: Universal Manipulation Interface — Project Page (Chi et al., RSS 2024)
type: source
url: https://umi-gripper.github.io/
paper_url: https://arxiv.org/abs/2402.10329
author: Cheng Chi, Zhenjia Xu, Chuer Pan, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Russ Tedrake, Shuran Song
affiliation: Stanford / Columbia / Toyota Research Institute
published: 2024-02 (arxiv); RSS 2024 (Best Systems Paper Award Finalist)
ingested: 2026-05-09
created: 2026-05-09
updated: 2026-05-09
tags: [umi, universal-manipulation-interface, hand-held-gripper, in-the-wild-data-collection, diffusion-policy-followon, chi-2024, stanford, columbia, tri]
---

> [!note] Ingest depth
> This source page is based on the **project page** (umi-gripper.github.io) plus the existing wiki's references to UMI in [Diffusion Policy Paper](diffusion-policy-paper.md) and [Robot Utility Models Paper](robot-utility-models-paper.md). The full RSS 2024 paper PDF is not in `raw/`.

## Summary

**Universal Manipulation Interface (UMI)** — Cheng Chi, Zhenjia Xu, Chuer Pan, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Russ Tedrake, Shuran Song (Stanford / Columbia / [Toyota Research Institute](../entities/tri.md), RSS 2024, **Best Systems Paper Award Finalist**). A **hand-held gripper data-collection system** that lets humans collect manipulation demonstrations *without a robot* — the human carries the gripper through real-world environments, performs the task, and the gripper records wrist-camera video and gripping-width data. Combined with **inference-time latency matching** and **relative-trajectory action representations**, the system trains policies that deploy zero-shot across multiple robot platforms (UR5e, Franka). Published as the direct follow-on to [Diffusion Policy](../entities/diffusion-policy.md) (same lead author, overlapping authors). Tagline: *"In-The-Wild Robot Teaching Without In-The-Wild Robots."*

## Key claims

### Hardware
- **Hand-held parallel-jaw gripper** with **wrist-mounted GoPro camera**.
- Captures visual context, depth (via GoPro features), gripping-width, and 6-DoF wrist trajectory during fast human motion.
- **100% calibration-free** (functioning even with base movement), per project page.
- Validates demonstrations against **robot kinematic constraints** during recording so that trajectories outside reachable workspace can be flagged.
- Open-source hardware: GitHub repo (`real-stanford/universal_manipulation_interface`), Google Docs assembly guide, 3D-print files, assembly videos.

### Data collection workflow
- **30 seconds per demonstration**.
- **111 demonstrations / hour** with UMI vs **35 demos/hour** with teleoperation — ~3× faster than conventional VR-teleop pipelines.
- **Within 2 minutes** to set up data collection in any new location ("portable" claim).

### Software / policy
- **Inference-time latency matching** — bridges human-collection cadence with robot-control cadence.
- **Relative-trajectory action representation** — actions encoded relative to the wrist frame so policies are *embodiment-agnostic* (same trained policy can drive UR5e or Franka).
- **Zero-shot cross-embodiment**: same trained policy deployed on **both UR5e and Franka** without retraining.

### Demonstrated capabilities
1. **Dynamic Tossing** — six-object sorting by *tossing* into bins.
2. **Cup Arrangement** — pick-and-place of espresso cups with specific orientation constraints.
3. **Bimanual Cloth Folding** — coordinated two-arm sweater folding, 6+ sequential steps.
4. **Dish Washing** — seven-step sequence including faucet operation, sponge handling, cleaning verification.

### Generalization
- Project page: policies *"generalize zero-shot to novel environments and objects when trained on diverse human demonstrations"*.
- Out-of-distribution demos highlighted (e.g., "serving espresso cups on water fountains").

## Why it matters in this wiki

- **Direct follow-on to [Diffusion Policy](../entities/diffusion-policy.md)** — same lead author (Cheng Chi). UMI is the *data-collection-side* answer to the policy-side advance Diffusion Policy made: collect more, more cheaply, in more diverse settings, then train Diffusion-Policy-style BC.
- **Cited as design inspiration for [RUM](../entities/robot-utility-models.md)'s Stick-v2 gripper** ([RUM paper](robot-utility-models-paper.md) §2.1). RUM's portable in-home data collection rig builds directly on UMI's "hand-held demo without robot" idea.
- **Bridges the [TRI](../entities/tri.md) and Stanford robotics communities** — author list spans Stanford/Columbia (Chi, Xu, Song) and TRI (Cousineau, Burchfiel, Feng, Tedrake). The cross-institutional pattern continues from Diffusion Policy through TRI's later LBM work.
- **Validates "data diversity > data quantity"** (the same RUM thesis, in adjacent form) — UMI's argument is that *cheap diverse demos* unlocks generalization, and the gripper exists to make those demos possible.

## Entities mentioned

- [Universal Manipulation Interface](../entities/umi.md) — the system itself.
- [Diffusion Policy](../entities/diffusion-policy.md) — predecessor; UMI's policies are typically Diffusion Policy variants.
- [Toyota Research Institute](../entities/tri.md) — co-author affiliation (Cousineau, Burchfiel, Feng, Tedrake).
- [Franka Panda](../entities/franka-panda.md) — one of two deployment platforms.
- [Robot Utility Models](../entities/robot-utility-models.md) — downstream NYU project that cites UMI as Stick-v2 design inspiration.

## Concepts touched

- [Imitation learning](../concepts/imitation-learning.md) — UMI is a data-collection enabler for BC.
- Cross-embodiment transfer — UMI's relative-trajectory action representation is one mechanism for it.
- Sim-to-real / real-to-real — UMI bypasses sim entirely; data is collected in the deployment environment by hand.

## Open questions / TBD

- **Full paper not yet ingested** — RSS 2024 paper PDF (arxiv 2402.10329); deeper mechanics (latency matching, relative-trajectory math, exact policy architecture) come from there.
- **Bill of materials / cost** — project page references hardware guide but no headline cost number was extracted.
- **Newer UMI variants** — multi-finger UMI, larger workspaces, etc. not covered here.
- **Russ Tedrake** entity — TRI senior figure on UMI; Drake (TRI/MIT) deserves an entity page (already on TBD list).
- **Cheng Chi / Shuran Song** — author entity pages on TBD list since Diffusion Policy ingest.

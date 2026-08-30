---
title: "HumanPlus: Humanoid Shadowing and Imitation from Humans"
type: source
url: https://arxiv.org/abs/2406.10454
local_path: raw/2406.10454v1.pdf
sha256: 94c5fe16631e2d1c5b5bdd8326adda17c719ad63b2630979ca6aa9e0a7af4dd2
author: Zipeng Fu*, Qingqing Zhao*, Qi Wu*, Gordon Wetzstein, Chelsea Finn (Stanford University; *project co-leads)
published: 2024-06-15
ingested: 2026-08-29
venue: CoRL 2024
format: PDF (17 pp., arXiv:2406.10454v1)
project_page: https://humanoid-ai.github.io
tags: [humanplus, humanoid, shadowing, imitation-learning, egocentric-vision, behavior-cloning, whole-body-control, stanford, open-hardware]
---

# HumanPlus: Humanoid Shadowing and Imitation from Humans

## Summary

Stanford's full-stack answer to the same problem [OmniH2O](omnih2o-paper.md) attacks, published the same month and arrived at independently: **get humanoid skills out of human data**. The pipeline has two halves and the split is the contribution.

**Shadowing** — a low-level policy trained in simulation by RL on **40 hours of existing human motion data** transfers to the real robot and lets it follow a human's body *and hand* motion in real time from **a single RGB camera**. That turns a person into a teleoperation rig with no rig.

**Imitation** — the data collected by shadowing is then used for **supervised behavior cloning from egocentric vision**, producing autonomous skill policies.

The system runs on a **custom 33-DoF, 180 cm humanoid**, and the paper reports **60–100% success on autonomous tasks using up to 40 demonstrations**: wearing a shoe and standing up to walk, unloading objects from warehouse racks, folding a sweatshirt, rearranging objects, typing, and greeting another robot.

## Key claims

- **Human motion data is the training substrate**, not robot data — the argument being that a human-shaped robot is the one embodiment that can use the enormous existing corpus of human motion directly.
- **The stated obstacles are honest and worth recording**: humanoid perception and control complexity, "lingering physical gaps between humanoids and humans in morphologies and actuation" (DoF count, link length, height, weight, vision parameters, actuation strength and responsiveness), and the absence of a data pipeline for learning autonomous skills from egocentric vision.
- **Shadowing covers hands as well as body**, which is what makes the collected data useful for manipulation rather than only locomotion.
- **40 demonstrations is the headline efficiency number** — small because the low-level policy already supplies whole-body competence, so behavior cloning only has to learn the task.

## Why it matters in this wiki

- **[Zipeng Fu](../entities/zipeng-fu.md)'s third appearance here, and it completes an unusual span.** He co-authored [RMA](rma-paper.md) (quadruped locomotion, CMU, 2021), [Mobile ALOHA](mobile-aloha-paper.md) (mobile manipulation, Stanford, 2024) and HumanPlus (humanoid whole-body, Stanford, 2024). Very few researchers in this wiki cross locomotion *and* manipulation, let alone on three embodiment classes.
- **It is the counterweight to the CMU line.** [H2O](h2o-paper.md)/[OmniH2O](omnih2o-paper.md) build increasingly capable *controllers* and treat autonomy as downstream; HumanPlus builds the **whole loop to autonomy** and reports task success rates for it. Two labs, one month apart, same insight, different emphasis — which is the more useful comparison than either paper alone.
- **Custom hardware is part of the contribution.** Where the CMU papers use a stock [Unitree H1](../entities/unitree-h1.md), HumanPlus builds its own 33-DoF platform — a reminder that in 2024 the humanoid field was still partly a hardware-availability problem.

## Entities mentioned

- [Zipeng Fu](../entities/zipeng-fu.md) — project co-lead.
- [Chelsea Finn](../entities/chelsea-finn.md) — senior author.

## Concepts touched

- [Whole-body control](../concepts/robotics/whole-body-control.md).
- [Imitation learning](../concepts/learning/imitation-learning.md) — behavior cloning on teleoperated data, the second stage.
- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) — shadowing as a data-collection instrument.

## Open questions

- **60–100% is a wide band** across six tasks, and per-task rollout counts are not recorded on this page.
- **The 40-hour motion dataset** is not identified by name in the ingested text. Whether it overlaps [AMASS](../entities/amass.md) — which the CMU line retargets — matters for comparing the two systems, and **this page deliberately does not assert that it does**.
- **Custom hardware limits replication** — the results are not directly comparable to H1-based work, and the platform is not purchasable.

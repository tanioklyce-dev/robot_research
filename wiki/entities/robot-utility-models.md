---
title: Robot Utility Models
type: entity
subtype: method
created: 2026-05-07
updated: 2026-05-16
sources: 11
tags: [rum, generalist-policy, zero-shot, nyu, meta, behavior-cloning]
---

**Robot Utility Models (RUMs)** — a framework for generalist robot policies that deploy **zero-shot** to new environments. From researchers at NYU and Meta (lead: Mahi Shafiullah). arXiv 2409.05865 (September 2024). Project: https://robotutilitymodels.com/.

## Approach
- Behavior-cloning policies trained on RGB video + 6D gripper pose + gripper-opening angle.
- Best-performing policy classes per [paper](../sources/robot-utility-models-paper.md): **VQ-BeT** (Lee et al. 2024) and **Diffusion Policy** (Chi et al. 2023). ACT and MLP-BC tested as baselines.
- Vision encoder: ResNet34 initialized from the **Dobb·E HPR encoder** (Shafiullah et al. 2023) + transformer policy trunk.
- Custom data-collection rig: **"Stick-v2"** — iPhone Pro + $25 BOM, 60 Hz RGB+depth, 100 Hz 6D pose via ARKit. No SLAM, no calibration.
- One model per task (5 task-specific "utility models").
- Visuomotor BC; **no language conditioning** (distinguishes RUMs from [VLA models](../concepts/learning/vla-models.md)).

## Headline result
- **~90% success in unseen, novel environments** with no fine-tuning, on five tasks: open cabinet door, open drawer, pick up napkin, pick up paper bag, reorient a fallen object.
- **74.4% from raw policy + 15.6% from gpt-4o retry** = 90% headline ([paper](../sources/robot-utility-models-paper.md)).
- **2,950 robot rollouts** total across NYC, Jersey City, Pittsburgh.
- **Cross-embodiment**: trained on [Stretch](stretch.md), transferred zero-shot to xArm 7 with ~10pt drop (tissue 80%→70%, bag 84%→76%).

## Scale
- 5 tasks × ~40 environments × ~1,000 demos per task (~25 demos per env on average).
- Door opening: 1,200 demos; drawer opening: 525 demos.
- 473 MB open-source dataset.

## Three data-recipe lessons (paper headline takeaways)
1. **Data > algorithm.** VQ-BeT and Diffusion Policy land within ~5pt; ACT and MLP-BC ~10–15pt below. The training data matters more than the policy class.
2. **Diversity > quantity.** 25 demos × many envs beats 200 demos × few envs (strongest effect on reorientation: 68% vs 18%).
3. **Expert > non-expert.** Co-training expert + non-expert can sometimes *hurt*, contradicting mainstream practice.

## Why it matters
Demonstrates that **generalization in mobile manipulation does not require explicit VLA / language conditioning** — visuomotor BC at modest scale generalizes to novel environments if data diversity is high. Adjacent to but conceptually distinct from [VLA models](../concepts/learning/vla-models.md).

## Related
- [Stretch](stretch.md) — primary hardware platform.
- [Hello Robot](hello-robot.md) — robot vendor (co-founder Aaron Edsinger is a paper co-author).
- [VLA models](../concepts/learning/vla-models.md) — adjacent paradigm.
- [Imitation learning](../concepts/learning/imitation-learning.md) — underlying training method.

## Mentioned in
- [Robot Utility Models Project Page](../sources/robot-utility-models-website.md)
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md)

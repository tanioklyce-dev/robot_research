---
title: Robot Utility Models
type: entity
subtype: method
created: 2026-05-07
updated: 2026-05-07
sources: 1
tags: [rum, generalist-policy, zero-shot, nyu, meta, behavior-cloning]
---

**Robot Utility Models (RUMs)** — a framework for generalist robot policies that deploy **zero-shot** to new environments. From researchers at NYU and Meta (lead: Mahi Shafiullah). arXiv 2409.05865 (September 2024). Project: https://robotutilitymodels.com/.

## Approach
- Behavior-cloning policies trained on RGB video + 6D gripper pose + gripper-opening angle.
- Custom data-collection rig: **"Stick V2" gripper** with an **iPhone POV mount** to keep camera viewpoint identical across collectors and target robots.
- One model per task (5 task-specific "utility models" in the paper).
- Visuomotor BC; **no language conditioning** (distinguishes RUMs from [[vla-models|VLA models]]).

## Headline result
- **~90% success in unseen, novel environments** with no fine-tuning, on five tasks: open cabinet door, open drawer, pick up napkin, pick up paper bag, reorient a fallen object.
- **Cross-embodiment**: trained on [[stretch|Stretch]], transferred zero-shot to xArm 7.

## Scale
- 5 tasks × 180 environments × 5,509 trajectories (~1,000 demos per task across ~36 envs per task).
- 473 MB open-source dataset.

## Why it matters
Demonstrates that **generalization in mobile manipulation does not require explicit VLA / language conditioning** — visuomotor BC at modest scale generalizes to novel environments if data diversity is high. Adjacent to but conceptually distinct from [[vla-models|VLA models]].

## Related
- [[stretch|Stretch]] — primary hardware platform.
- [[hello-robot|Hello Robot]] — robot vendor (co-founder Aaron Edsinger is a paper co-author).
- [[vla-models|VLA models]] — adjacent paradigm.
- [[imitation-learning|Imitation learning]] — underlying training method.

## Mentioned in
- [[robot-utility-models-website|Robot Utility Models Project Page]]

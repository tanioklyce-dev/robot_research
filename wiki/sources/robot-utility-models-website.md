---
title: Robot Utility Models Project Page
type: source
url: https://robotutilitymodels.com/
author: Etukuru, Shafiullah, Naka, Hu, Lee, Mehu, Edsinger, Paxton, Chintala, Pinto
affiliations: NYU, Meta / Facebook AI
published: 2024-09 (arXiv 2409.05865)
ingested: 2026-05-07
tags: [rum, robot-utility-models, generalist-policy, zero-shot, nyu, meta]
---

## Summary
Project page for **Robot Utility Models (RUMs)** — a framework from NYU and Meta researchers proposing "general policies for zero-shot deployment in new environments." Companion arXiv paper: 2409.05865 (September 2024). Lead author Mahi Shafiullah (corresponding: mahi at cs dot nyu dot edu); other notable co-authors include Aaron Edsinger ([[hello-robot|Hello Robot]] co-founder), Chris Paxton, Soumith Chintala, Lerrel Pinto.

## Key claims
- **~90% success rate** in unseen, novel environments with zero additional data or fine-tuning.
- Five utility models, one per task: open cabinet door, open drawer, pick up napkin, pick up paper bag, reorient fallen object.
- Training corpus: **5 tasks × 180 environments × 5,509 trajectories** (avg ~1,000 demos per task across 36 envs per task).
- Data format: RGB video at 30 fps + 6D gripper pose + gripper-opening angle.
- **Cross-embodiment transfer**: trained on [[stretch|Stretch]], deployed zero-shot on xArm 7 with no further data, training, or fine-tuning.
- Hardware aid: custom **"Stick V2" gripper** with iPhone POV mount — keeps camera viewpoint identical across robots.
- Open source: github.com/haritheja-e/robot-utility-models.
- Dataset: 473 MB (https://pub-853366c2ad9c476bb0d45c936b37b32b.r2.dev/robot-utility-model-data.zip).
- Data diversity visualizer: https://robotutilitymodels.com/data_diversity/

## Entities mentioned
- [[hello-robot|Hello Robot]]
- [[stretch|Stretch]]
- [[robot-utility-models|Robot Utility Models]]
- [[franka-panda|Franka Panda]] — implicit cross-embodiment context (xArm 7 named explicitly; Franka not named in abstract but appears in adjacent literature comparing RUM transfer targets).

## Concepts touched
- [[imitation-learning|Imitation learning]] / behavior cloning
- [[vla-models|VLA-adjacent generalist policies]] (RUMs are visuomotor BC, no language conditioning)
- Cross-embodiment transfer
- Mobile manipulation

## Open questions
- How does RUM scale beyond 5 tasks? Is the 90% number stable as task count grows?
- Why "utility model" framing vs. "policy" or "VLA"? Is this a deliberate distinction from language-conditioned models?
- Has the field reproduced the 90% result independently?

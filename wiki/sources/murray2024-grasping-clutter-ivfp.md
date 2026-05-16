---
title: Learning to Grasp in Clutter with Interactive Visual Failure Prediction (Murray, Gupta, Cakmak)
type: source
url: https://robo-ivfp.github.io
local_path: raw/murray2024learning.pdf
author: Michael Murray, Abhishek Gupta, Maya Cakmak
published: 2024 (venue unknown — UW Allen School; Amazon Science Fellowship)
ingested: 2026-05-09
tags: [grasping, clutter, failure-prediction, stretch, hcrlab, maya-cakmak]
---

## Summary

Proposes Interactive Visual Failure Prediction (IVFP) — using robot probing motions to visually assess grasp stability in clutter before full execution. Demonstrated on a Stretch RE1 in an industrial warehouse setting. IVFP serves two purposes: (1) pre-emptive failure avoidance at test time and (2) autonomous reward signal for online policy improvement without constant human supervision. Leads to grasping policies that outperform human-supervised baselines while requiring significantly less human intervention.

## Key claims

- **IVFP concept**: Before extracting an object, the robot performs interactive probing motions to acquire visual feedback about grasp stability. This detects unstable grasps — which often fail during extraction — before the costly extraction step.
- **Two uses of IVFP**: (1) During evaluation: preempt risky grasps to improve success rate. (2) During training: autonomous reward assignment — IVFP scores picks without requiring a human to watch every attempt, enabling online RL without constant human supervision.
- **Clutter problem**: Warehouse bins contain densely packed objects with high object diversity. Standard passive visual assessment is insufficient — occlusion and high clutter make pre-contact success prediction unreliable from vision alone.
- **Platform**: Hello Robot Stretch RE1 in industrial warehouse containers.
- **Key results**: IVFP immediately improves picking success; policies trained with IVFP outperform those trained with human supervision only; IVFP requires significantly less human intervention than typical data collection pipelines.
- **Code/data**: Available at robo-ivfp.github.io.
- **Funding**: Amazon Science Fellowship.

## Entities mentioned

- [Maya Cakmak](../entities/maya-cakmak.md)
- [HCR Lab](../entities/hcrlab.md)
- [Stretch](../entities/stretch.md) — Stretch RE1 used as deployment platform

## Concepts touched

- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — grasping in clutter is blocking problem #2 in the synthesis
- [Imitation learning](../concepts/learning/imitation-learning.md) — IVFP provides autonomous reward for policy improvement

## Open questions

- Exact venue (ICRA, RA-L, IROS, or other) — not determined from available pages.
- Quantitative success-rate numbers vs. baselines — not captured from pages 1–2.
- How well does IVFP transfer from warehouse bins to home-environment clutter?

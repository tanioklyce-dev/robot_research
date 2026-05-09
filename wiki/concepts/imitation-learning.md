---
title: Imitation learning
type: concept
created: 2026-05-07
updated: 2026-05-08
sources: 7
tags: [imitation-learning, behavior-cloning, demonstrations]
---

**Imitation learning** — supervised training of a robot policy to predict actions from observations using human or expert demonstrations. The dominant training paradigm for the robot foundation models discussed across this wiki.

## Common variants
- **Behavior cloning (BC)** — direct supervised mapping from observations to actions. Simplest and most common form. Used by [Robot Utility Models](../entities/robot-utility-models.md) for its 5 zero-shot policies.
- **Action-chunked BC** — predict multi-step action sequences for smoother control.
- **Diffusion policies** — model action distributions with a diffusion model; reduces multimodal collapse.

## Why it matters
- Training method behind nearly every flagship "generalist" policy of 2024–2026: [GR00T](../entities/nvidia-groot.md), Pi VLAs, [RUMs](../entities/robot-utility-models.md), and the policies trained inside [RoboCasa365](../entities/robocasa.md)'s benchmark suite.
- Bottlenecks: demo quantity, demo diversity, embodiment gap. [MimicGen](../entities/mimicgen.md)-style synthetic-demo expansion is one mitigation, large simulator corpora ([RoboCasa365](../entities/robocasa.md), [Genie Sim 3.0](../entities/agibot-genie-sim.md)) are another.

## Related
- [VLA models](vla-models.md) — typically trained via imitation learning on robot demos plus human video.
- [Sim-to-real transfer](sim-to-real-transfer.md) — sim-trained imitation policies frequently need real-world adaptation.
- [Robot Utility Models](../entities/robot-utility-models.md) — zero-shot BC.
- [MimicGen](../entities/mimicgen.md) — synthetic demo expansion.

## Mentioned in
- [Robot Utility Models Project Page](../sources/robot-utility-models-website.md)
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md)
- [RoboCasa365 Paper](../sources/robocasa365-paper.md)

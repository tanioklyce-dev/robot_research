---
title: Imitation learning
type: concept
created: 2026-05-07
updated: 2026-05-16
sources: 28
tags: [imitation-learning, behavior-cloning, demonstrations, lerobot, act]
---

**Imitation learning** — supervised training of a robot policy to predict actions from observations using human or expert demonstrations. The dominant training paradigm for the robot foundation models discussed across this wiki.

## Common variants
- **Behavior cloning (BC)** — direct supervised mapping from observations to actions. Simplest and most common form. Used by [Robot Utility Models](../../entities/robot-utility-models.md) for its 5 zero-shot policies.
- **Action-chunked BC** — predict multi-step action sequences for smoother control. Convention popularized by [Diffusion Policy](../../entities/diffusion-policy.md) (predict `T_p`, execute `T_a < T_p` before re-planning); now near-default across 2024–2026 BC and [VLA models](vla-models.md).
- **Diffusion policies** — model action distributions with a diffusion model; reduces multimodal collapse. [Diffusion Policy](../../entities/diffusion-policy.md) (Chi et al., RSS 2023) reports an average **46.9% improvement** over LSTM-GMM / IBC / BET across 12 tasks, and is the canonical 2024–2026 BC baseline ([paper](../../sources/diffusion-policy-paper.md) §V).

## Why it matters
- Training method behind nearly every flagship "generalist" policy of 2024–2026: [GR00T](../../entities/nvidia-groot.md), Pi VLAs, [RUMs](../../entities/robot-utility-models.md), and the policies trained inside [RoboCasa365](../../entities/robocasa.md)'s benchmark suite.
- Bottlenecks: demo quantity, demo diversity, embodiment gap. [MimicGen](../../entities/mimicgen.md)-style synthetic-demo expansion is one mitigation, large simulator corpora ([RoboCasa365](../../entities/robocasa.md), [Genie Sim 3.0](../../entities/agibot-genie-sim.md)) are another.

## Frameworks and stacks

The IL training stacks documented in this wiki cluster by hardware tier:

- **[LeRobot](../../entities/lerobot.md)** ([Hugging Face](../../entities/hugging-face.md)) — open-source IL framework spanning sub-$1k hardware ([SO-ARM101](../../entities/so-arm101.md), [LeKiwi](../../entities/lekiwi.md), [XLeRobot](../../entities/xlerobot.md)) up through professional platforms. Canonical 7-step workflow (install → motor config → calibrate → teleop → record demos → train → evaluate). **ACT (Action Chunking with Transformers)** is the default reference policy.
- **[Stretch AI](../../entities/stretch-ai.md)** (Hello Robot) — LLM-agent + IL stack for the $20k [Stretch](../../entities/stretch.md) platform.
- **Research code** — Diffusion Policy, RUM, and similar each ship their own training code; typically run on [Franka Panda](../../entities/franka-panda.md), UR5e, or [Stretch](../../entities/stretch.md).

## Related
- [VLA models](vla-models.md) — typically trained via imitation learning on robot demos plus human video.
- [Sim-to-real transfer](sim-to-real-transfer.md) — sim-trained imitation policies frequently need real-world adaptation.
- [Robot Utility Models](../../entities/robot-utility-models.md) — zero-shot BC.
- [MimicGen](../../entities/mimicgen.md) — synthetic demo expansion.

## Mentioned in
- [Robot Utility Models Project Page](../../sources/robot-utility-models-website.md)
- [Robot Utility Models Paper](../../sources/robot-utility-models-paper.md)
- [RoboCasa365 Paper](../../sources/robocasa365-paper.md)
- [Diffusion Policy Paper](../../sources/diffusion-policy-paper.md)
- [XLeRobot Documentation](../../sources/xlerobot-docs.md)
- [Seeed Studio LeRobot LeKiwi Wiki](../../sources/seeed-lekiwi-wiki.md)
- [LeKiwi GitHub](../../sources/lekiwi-github.md)

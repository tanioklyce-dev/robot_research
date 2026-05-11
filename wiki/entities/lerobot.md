---
title: LeRobot
type: entity
subtype: software-framework
created: 2026-05-10
updated: 2026-05-10
sources: 3
tags: [lerobot, imitation-learning, hugging-face, framework, open-source, act, mobile-manipulator]
---

**LeRobot** — open-source **imitation-learning framework for robotics** maintained by [Hugging Face](hugging-face.md). Provides standardized tooling for: motor configuration, calibration, teleoperation, demonstration recording, dataset management, policy training (ACT, Diffusion Policy, others), and autonomous evaluation. Has emerged as the de-facto OSS stack for low-cost mobile manipulators (SO-ARM100/101, LeKiwi, XLeRobot, Bambot, Koch v1.1) and is bringing the "buy → assemble → teleop → train → deploy" pipeline within reach of sub-$1k hobbyist hardware.

Repository: [github.com/huggingface/lerobot](https://github.com/huggingface/lerobot).

## Why it matters in this wiki

LeRobot is the **dominant open-source IL framework for the affordable mobile-manipulator class** — directly relevant to the wiki's assistive-robotics, accessible-robotics, and household-manipulation themes. It complements the wiki's existing IL coverage:

- **[Diffusion Policy](diffusion-policy.md)** — research code, often run on Franka/UR5e platforms costing $20k+.
- **[Stretch AI](stretch-ai.md)** — Hello Robot's stack targeted at the $20k Stretch platform.
- **LeRobot** — broader and lower-cost; supports SO-ARM101, LeKiwi, and downstream compositions like XLeRobot at ~$600–$1,000.

The canonical 7-step LeRobot workflow (install → motor config → calibration → teleop → data collection → train → evaluate) is repeated across nearly every LeRobot-compatible hardware tutorial. **ACT (Action Chunking with Transformers)** is the default reference policy class, though Diffusion Policy and others are supported.

## Composition stack examples in this wiki

| Platform | Base | Arm | Cost | Source |
|---|---|---|---|---|
| [LeKiwi](lekiwi.md) | LeKiwi 3-wheel Kiwi-drive | SO-ARM101 (optional) | sub-$1k | [LeKiwi GitHub](../sources/lekiwi-github.md), [Seeed tutorial](../sources/seeed-lekiwi-wiki.md) |
| [XLeRobot](xlerobot.md) | LeKiwi-class wheeled base | 2× SO-ARM101 | ~$660 | [XLeRobot docs](../sources/xlerobot-docs.md) |

## Key facts

- Maintained by [Hugging Face](hugging-face.md).
- Apache 2.0.
- Active development; framework moves quickly enough that distributor tutorials (e.g., [Seeed Studio LeKiwi wiki](../sources/seeed-lekiwi-wiki.md)) carry "consult upstream for latest features" caveats.
- Compatible hardware ecosystem: SO-ARM100/101 (The Robot Studio), Koch v1.1 (Dynamixel), LeKiwi (SIGRobotics-UIUC), XLeRobot (Vector Wang), Bambot, others.

## Related

- [Hugging Face](hugging-face.md) — maintainer
- [SO-ARM101](so-arm101.md) — arm platform
- [LeKiwi](lekiwi.md) — mobile base
- [XLeRobot](xlerobot.md) — dual-arm composition
- [Imitation learning](../concepts/imitation-learning.md)
- [Diffusion Policy](diffusion-policy.md) — alternative IL approach
- [Stretch AI](stretch-ai.md) — counterpart IL/agent stack on Stretch

## Mentioned in

- [XLeRobot Documentation](../sources/xlerobot-docs.md)
- [Seeed Studio LeRobot LeKiwi Wiki](../sources/seeed-lekiwi-wiki.md)
- [LeKiwi GitHub](../sources/lekiwi-github.md)

## Open questions / TBD

- Stable release cadence — distributor tutorials note framework volatility, but the upstream release history is not yet ingested.
- Performance comparison: ACT (LeRobot default) vs. [Diffusion Policy](diffusion-policy.md) / [VQ-BeT](vq-bet.md) / [BET](bet.md) on the same low-cost hardware. No head-to-head numbers in ingested sources.
- Relationship to [Stretch AI](stretch-ai.md) — both are LLM/IL-adjacent open robot stacks. Any cross-pollination?

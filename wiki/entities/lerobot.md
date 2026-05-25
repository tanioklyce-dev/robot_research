---
title: LeRobot
type: entity
subtype: software-framework
created: 2026-05-10
updated: 2026-05-25
sources: 8
tags: [lerobot, imitation-learning, hugging-face, framework, open-source, act, mobile-manipulator, smolvla, pi0, tutorial]
---

**LeRobot** — open-source **imitation-learning framework for robotics** maintained by [Hugging Face](hugging-face.md). Provides standardized tooling for: motor configuration, calibration, teleoperation, demonstration recording, dataset management, policy training (ACT, Diffusion Policy, others), and autonomous evaluation. Has emerged as the de-facto OSS stack for low-cost mobile manipulators (SO-ARM100/101, LeKiwi, XLeRobot, Bambot, Koch v1.1) and is bringing the "buy → assemble → teleop → train → deploy" pipeline within reach of sub-$1k hobbyist hardware.

Repository: [github.com/huggingface/lerobot](https://github.com/huggingface/lerobot).

## Why it matters in this wiki

LeRobot is the **dominant open-source IL framework for the affordable mobile-manipulator class** — directly relevant to the wiki's assistive-robotics, accessible-robotics, and household-manipulation themes. It complements the wiki's existing IL coverage:

- **[Diffusion Policy](diffusion-policy.md)** — research code, often run on Franka/UR5e platforms costing $20k+.
- **[Stretch AI](stretch-ai.md)** — Hello Robot's stack targeted at the $20k Stretch platform.
- **LeRobot** — broader and lower-cost; supports SO-ARM101, LeKiwi, and downstream compositions like XLeRobot at ~$600–$1,000.

LeRobot also distributes **two reference VLA checkpoints** directly:

- **[`lerobot/pi0_base`](pi-zero.md)** — Physical Intelligence's [π0](pi-zero.md) (3.3 B params; PaliGemma + flow-matching action expert).
- **[`lerobot/smolvla_base`](smolvla.md)** — Hugging Face LeRobot team's [SmolVLA](smolvla.md) (450 M params; SmolVLM-2 + flow-matching action expert with interleaved CA + causal SA + async-inference stack). **SmolVLA beats π0-3.5 B by +16.6 pts on real-world SO-100 multi-task** despite ~7× fewer params.

The canonical 7-step LeRobot workflow (install → motor config → calibration → teleop → data collection → train → evaluate) is repeated across nearly every LeRobot-compatible hardware tutorial. **ACT (Action Chunking with Transformers)** is the default reference policy class, though Diffusion Policy and others are supported.

## Composition stack examples in this wiki

| Platform | Base | Arm | Cost | Source |
|---|---|---|---|---|
| [LeKiwi](lekiwi.md) | LeKiwi 3-wheel Kiwi-drive | SO-ARM101 (optional) | sub-$1k | [LeKiwi GitHub](../sources/lekiwi-github.md), [Seeed tutorial](../sources/seeed-lekiwi-wiki.md) |
| [XLeRobot](xlerobot.md) | LeKiwi-class wheeled base | 2× SO-ARM101 | ~$660 | [XLeRobot docs](../sources/xlerobot-docs.md) |

## Key facts

- Maintained by [Hugging Face](hugging-face.md); robotics lead [Remi Cadene](remi-cadene.md).
- Apache 2.0.
- Active development; framework moves quickly enough that distributor tutorials (e.g., [Seeed Studio LeKiwi wiki](../sources/seeed-lekiwi-wiki.md)) carry "consult upstream for latest features" caveats.
- Compatible hardware ecosystem: SO-ARM100/101 (The Robot Studio), Koch v1.1 (Dynamixel), LeKiwi (SIGRobotics-UIUC), XLeRobot (Vector Wang), Bambot, others.

## Ecosystem scale (June 2025 snapshot)

The [LeRobot Worldwide Hackathon 2025](lerobot-worldwide-hackathon-2025.md) (June 14–15, 2025) is the clearest community-scale signal for the framework: **916 registered team members, ~400 submissions, 30 ranked winners, 189 hackathon datasets, 12 hackathon models** ([all-winners HF Space](../sources/lerobot-worldwide-hackathon-2025-winners.md)). The `submissions` dataset alone has 11.3k downloads.

## Official pedagogical reference

**["Robot Learning: A Tutorial"](../sources/lerobot-robot-learning-tutorial.md)** (Capuano, Pascal, Zouitine, Wolf, Aractingi — Oct 14, 2025; arXiv 2510.12403 + HF Space at https://huggingface.co/spaces/lerobot/robot-learning-tutorial) is the **team-authored canonical tutorial** for the framework — a chapter arc from Classical Robotics through RL and IL to Generalist (VLA) policies, with runnable `lerobot` code examples (ACT, Diffusion Policy, async inference, [π₀](physical-intelligence.md), SmolVLA). 410 likes on the Space at ingest time. This is the recommended single-source onboarding for the framework, complementary to the wiki's own [bottom-up curriculum](../syntheses/curriculum/robot-learning-curriculum.md).

## Downstream / hardware-ecosystem projects

- **[Grievous](grievous.md)** ([source](../sources/grievous-github.md)) — Alex Koven's in-progress "cheap, human-like, fully-autonomous testbed" registered as `lerobot.robots.grievous.grievous_host`. Design ancestors: [Mobile ALOHA](aloha.md) + [XLeRobot](xlerobot.md).

## Related

- [Hugging Face](hugging-face.md) — maintainer
- [SO-ARM101](so-arm101.md) — arm platform
- [LeKiwi](lekiwi.md) — mobile base
- [XLeRobot](xlerobot.md) — dual-arm composition
- [Imitation learning](../concepts/learning/imitation-learning.md)
- [Diffusion Policy](diffusion-policy.md) — alternative IL approach
- [Stretch AI](stretch-ai.md) — counterpart IL/agent stack on Stretch

## Mentioned in

- [SmolVLA Paper](../sources/smolvla-paper.md) — team-authored VLA built on LeRobot framework.
- [π0 Paper](../sources/pi-zero-paper.md) — Physical Intelligence's VLA; distributed via LeRobot.
- [Robot Learning: A Tutorial (LeRobot)](../sources/lerobot-robot-learning-tutorial.md) — official team-authored tutorial.
- [Grievous GitHub](../sources/grievous-github.md) — downstream hardware project built on LeRobot.
- [XLeRobot Documentation](../sources/xlerobot-docs.md)
- [Seeed Studio LeRobot LeKiwi Wiki](../sources/seeed-lekiwi-wiki.md)
- [LeKiwi GitHub](../sources/lekiwi-github.md)
- [LeRobot Worldwide Hackathon 2025 — All Winners](../sources/lerobot-worldwide-hackathon-2025-winners.md)

## Open questions / TBD

- Stable release cadence — distributor tutorials note framework volatility, but the upstream release history is not yet ingested.
- Performance comparison: ACT (LeRobot default) vs. [Diffusion Policy](diffusion-policy.md) / [VQ-BeT](vq-bet.md) / [BET](bet.md) on the same low-cost hardware. No head-to-head numbers in ingested sources.
- Relationship to [Stretch AI](stretch-ai.md) — both are LLM/IL-adjacent open robot stacks. Any cross-pollination?

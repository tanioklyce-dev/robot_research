---
title: Imitation learning
type: concept
created: 2026-05-07
updated: 2026-05-07
sources: 2
tags: [imitation-learning, behavior-cloning, demonstrations]
---

**Imitation learning** — supervised training of a robot policy to predict actions from observations using human or expert demonstrations. The dominant training paradigm for the robot foundation models discussed across this wiki.

## Common variants
- **Behavior cloning (BC)** — direct supervised mapping from observations to actions. Simplest and most common form. Used by [[robot-utility-models|Robot Utility Models]] for its 5 zero-shot policies.
- **Action-chunked BC** — predict multi-step action sequences for smoother control.
- **Diffusion policies** — model action distributions with a diffusion model; reduces multimodal collapse.

## Why it matters
- Training method behind nearly every flagship "generalist" policy of 2024–2026: [[nvidia-groot|GR00T]], Pi VLAs, [[robot-utility-models|RUMs]], and the policies trained inside [[robocasa|RoboCasa365]]'s benchmark suite.
- Bottlenecks: demo quantity, demo diversity, embodiment gap. [[mimicgen|MimicGen]]-style synthetic-demo expansion is one mitigation, large simulator corpora ([[robocasa|RoboCasa365]], [[agibot-genie-sim|Genie Sim 3.0]]) are another.

## Related
- [[vla-models|VLA models]] — typically trained via imitation learning on robot demos plus human video.
- [[sim-to-real-transfer|Sim-to-real transfer]] — sim-trained imitation policies frequently need real-world adaptation.
- [[robot-utility-models|Robot Utility Models]] — zero-shot BC.
- [[mimicgen|MimicGen]] — synthetic demo expansion.

## Mentioned in
- [[robot-utility-models-website|Robot Utility Models Project Page]]
- [[robocasa365-paper|RoboCasa365 Paper]]

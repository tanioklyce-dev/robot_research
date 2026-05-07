---
title: Newton physics engine
type: entity
subtype: product
created: 2026-05-06
updated: 2026-05-07
sources: 3
tags: [physics-engine, gpu, openusd, warp, linux-foundation]
---

Open-source GPU-accelerated physics engine for robotics, co-developed by [[nvidia|NVIDIA]], [[google-deepmind|Google DeepMind]], and [[disney-research|Disney Research]], and managed under the Linux Foundation. Built on NVIDIA Warp and OpenUSD. GA-released at GTC 2026.

## Capabilities
- GPU-accelerated rigid-body, soft-body, and contact-rich physics.
- OpenUSD-native scene description.
- Pluggable into both [[nvidia-isaac-lab|NVIDIA Isaac Lab]] and [[mujoco-playground|MuJoCo Playground]] — making it a rare cross-stack substrate.
- Targeted at industrial robotics: dexterous manipulation, locomotion.

## 2026 status
Newton 1.0 GA in March 2026 (GTC). Production-ready for Isaac Lab. Part of NVIDIA's Physical AI release wave alongside [[nvidia-groot|GR00T N1.6]] ([[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]]).

## Why it matters
Newton's vendor-neutral governance plus its presence in both DeepMind's and NVIDIA's stacks positions it as the emerging shared physics substrate for agentic robotics — reducing simulator lock-in for policy researchers.

## Related
- [[nvidia-isaac-lab|NVIDIA Isaac Lab]] — primary integration.
- [[mujoco-playground|MuJoCo Playground]] — secondary integration; competes with MJX as the underlying physics.
- [[nvidia|NVIDIA]], [[google-deepmind|Google DeepMind]] — co-developers.

## Mentioned in
- [[nvidia-newton-physics-engine-developer-page|NVIDIA Newton Physics Engine Developer Page]]
- [[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]]

---
title: Genesis
type: entity
subtype: product
created: 2026-05-06
updated: 2026-05-07
sources: 2
tags: [physics-engine, generative-simulation, vlm, embodied-ai]
---

Generative and universal physics engine for robotics and embodied AI, released December 2024 after a 24-month collaboration across 20+ research labs. Pythonic, lightweight, with an integrated photorealistic renderer.

## Capabilities
- Headline benchmark: 43M FPS on a Franka arm (single RTX 4090, ~430,000× real-time).
- Claimed 10–80× speedup over Isaac Gym/Sim/Lab and [MuJoCo MJX](mujoco-playground.md) on comparable workloads.
- **Generative simulation**: a [VLM](../concepts/vla-models.md)-based agent uses simulator APIs as tools to construct 4D worlds from natural-language prompts.
- Output modalities: scenes, tasks, rewards, assets, motions, policies, trajectories, camera paths, physically-accurate videos.
- Photorealistic rendering integrated.

## 2026 status
Active open-source project. Adoption claims are strong but real-world production usage is harder to pin down — the wins are mostly in research demos and synthetic-data pipelines (e.g. on AMD Instinct GPUs with ROCm).

> [!note] Skepticism
> The 43M FPS figure refers to a Franka arm in a benign scenario. Throughput on contact-rich tasks is likely much lower. Validate before relying on the headline number for capacity planning.

## Related
- [VLA models](../concepts/vla-models.md), [World-model simulators](../concepts/world-model-simulators.md) — adjacent paradigms Genesis touches.

## Mentioned in
- [Genesis Project Page](../sources/genesis-project-page.md)
- [NVIDIA Newton Physics Engine Developer Page](../sources/nvidia-newton-physics-engine-developer-page.md)

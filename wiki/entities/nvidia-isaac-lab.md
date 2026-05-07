---
title: NVIDIA Isaac Lab
type: entity
subtype: product
created: 2026-05-06
updated: 2026-05-07
sources: 3
tags: [framework, robot-learning, nvidia, isaac-lab, rl]
---

Open-source modular framework for robot learning and policy training. Sits on top of [[nvidia-isaac-sim|NVIDIA Isaac Sim]] (or other simulators) and lets researchers swap physics backends, define environments, and run massively parallel RL.

## Capabilities
- Pluggable physics backends: PhysX, [[newton-physics-engine|Newton]], NVIDIA Warp, MuJoCo.
- Massively parallel environment vectorization for RL.
- Isaac Lab-Arena: open-source policy evaluation framework.
- Bundles [[nvidia-groot|NVIDIA GR00T]] reasoning [[vla-models|VLA]] (currently N1.6 GA / N1.7 EA).

## 2026 status
Isaac Lab 3.0 with the GA release of the [[newton-physics-engine|Newton physics engine]] became the default training stack for NVIDIA's "Physical AI" stack at GTC 2026 ([[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]]).

## Related
- [[nvidia-isaac-sim|NVIDIA Isaac Sim]] — the simulator.
- [[newton-physics-engine|Newton physics engine]] — primary physics backend in 2026.
- [[nvidia-cosmos|NVIDIA Cosmos]] — world model for rare scenarios and synthetic data.
- [[mujoco-playground|MuJoCo Playground]] — competing/parallel learning framework with overlapping backends.

## Mentioned in
- [[nvidia-newton-physics-engine-developer-page|NVIDIA Newton Physics Engine Developer Page]]
- [[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]]

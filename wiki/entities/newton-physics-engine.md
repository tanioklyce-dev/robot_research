---
title: Newton physics engine
type: entity
subtype: product
created: 2026-05-06
updated: 2026-05-07
sources: 4
tags: [physics-engine, gpu, openusd, usdphysics, warp, linux-foundation]
---

Open-source GPU-accelerated physics engine for robotics, co-developed by [[nvidia|NVIDIA]], [[google-deepmind|Google DeepMind]], and [[disney-research|Disney Research]], and managed under the Linux Foundation. Built on NVIDIA Warp and [[openusd|OpenUSD]]. GA-released at GTC 2026.

## Capabilities
- GPU-accelerated rigid-body, soft-body, and contact-rich physics.
- [[openusd|OpenUSD]]-native scene description, with the `UsdPhysics` schema family as the baseline robot-physics representation.
- Pluggable into both [[nvidia-isaac-lab|NVIDIA Isaac Lab]] and [[mujoco-playground|MuJoCo Playground]] — making it a rare cross-stack substrate.
- Targeted at industrial robotics: dexterous manipulation, locomotion.

## 2026 status
Newton 1.0 GA in March 2026 (GTC). Production-ready for Isaac Lab. Part of NVIDIA's Physical AI release wave alongside [[nvidia-groot|GR00T N1.6]] ([[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]]).

## USD schema layer
- **`newton-usd-schemas`** — Apache 2.0, Linux Foundation governance. Defines `NewtonSceneAPI` (timestep, gravity, solver iterations) extending `UsdPhysics`. Active: v0.2.0 released **2026-05-07**; 52 commits, 7 releases. Designed as a "proving ground" — physically meaningful parameters generalizable across solvers may be promoted into `UsdPhysics` itself.
- **`mujoco-usd-converter`** — companion bridge tool in the `newton-physics` GitHub org converting MJCF assets to USD with [[google-deepmind|DeepMind]]'s `MjcPhysics` schemas.
- Existing PhysX-based Isaac Sim assets are *compatible* with Newton but may need re-tuning of contact settings, solver iterations, and timestep for optimal results.

## Why it matters
Newton's vendor-neutral governance plus its presence in both DeepMind's and NVIDIA's stacks positions it as the emerging shared physics substrate for agentic robotics — reducing simulator lock-in for policy researchers. The `newton-usd-schemas` "promotion path" into upstream `UsdPhysics` is the structural mechanism that turns vendor-specific solver work into open-standard infrastructure.

## Related
- [[openusd|OpenUSD]] — the scene/physics substrate Newton consumes and extends.
- [[nvidia-isaac-lab|NVIDIA Isaac Lab]] — primary integration.
- [[mujoco-playground|MuJoCo Playground]] — secondary integration; competes with MJX as the underlying physics.
- [[nvidia|NVIDIA]], [[google-deepmind|Google DeepMind]] — co-developers.

## Mentioned in
- [[nvidia-newton-physics-engine-developer-page|NVIDIA Newton Physics Engine Developer Page]]
- [[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]]
- [[nvidia-openusd-for-robotic-simulation|Using OpenUSD for Modular and Scalable Robotic Simulation]]

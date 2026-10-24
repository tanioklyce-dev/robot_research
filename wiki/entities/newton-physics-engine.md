---
title: Newton physics engine
type: entity
subtype: product
created: 2026-05-06
updated: 2026-10-24
sources: 10
tags: [physics-engine, gpu, openusd, usdphysics, warp, linux-foundation]
---

Open-source GPU-accelerated physics engine for robotics, co-developed by [NVIDIA](nvidia.md), [Google DeepMind](google-deepmind.md), and [Disney Research](disney-research.md), and managed under the Linux Foundation. Built on NVIDIA Warp and [OpenUSD](openusd.md). GA-released at GTC 2026.

## Capabilities
- GPU-accelerated rigid-body, soft-body, and contact-rich physics.
- [OpenUSD](openusd.md)-native scene description, with the `UsdPhysics` schema family as the baseline robot-physics representation.
- Pluggable into both [NVIDIA Isaac Lab](nvidia-isaac-lab.md) and [MuJoCo Playground](mujoco-playground.md) — making it a rare cross-stack substrate.
- Targeted at industrial robotics: dexterous manipulation, locomotion.

## 2026 status
Newton 1.0 GA in March 2026 (GTC). Production-ready for Isaac Lab. Part of NVIDIA's Physical AI release wave alongside [GR00T N1.6](nvidia-groot.md) ([NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)).

## USD schema layer
- **`newton-usd-schemas`** — Apache 2.0, Linux Foundation governance. Defines `NewtonSceneAPI` (timestep, gravity, solver iterations) extending `UsdPhysics`. Active: v0.2.0 released **2026-05-07**; 52 commits, 7 releases. Designed as a "proving ground" — physically meaningful parameters generalizable across solvers may be promoted into `UsdPhysics` itself.
- **`mujoco-usd-converter`** — companion bridge tool in the `newton-physics` GitHub org converting MJCF assets to USD with [DeepMind](google-deepmind.md)'s `MjcPhysics` schemas.
- Existing PhysX-based Isaac Sim assets are *compatible* with Newton but may need re-tuning of contact settings, solver iterations, and timestep for optimal results.

## Why it matters
Newton's vendor-neutral governance plus its presence in both DeepMind's and NVIDIA's stacks positions it as the emerging shared physics substrate for agentic robotics — reducing simulator lock-in for policy researchers. The `newton-usd-schemas` "promotion path" into upstream `UsdPhysics` is the structural mechanism that turns vendor-specific solver work into open-standard infrastructure.

## Cross-domain pull on the underlying compute layer

Newton is built on **NVIDIA Warp**. Warp is also what [NeuroMechFly v2](neuromechfly.md) uses (via MJWarp) to deliver its ~300× GPU speedup over the v1 codebase ([flygym GitHub](../sources/flygym-github.md)). NeuroMechFly does not depend on Newton itself, but the same GPU compute layer is being commoditized for industrial-robotics simulation *and* for biological whole-body simulation. This is a meaningful real-world data point for the [Newton + OpenUSD substrate convergence](../syntheses/simulators/newton-openusd-substrate-convergence.md) thesis: physics-layer commoditization has cross-domain pull, not just intra-robotics pull.

## Industrial backing (GTC Berlin, 2026-10-21)
**Schaeffler** is contributing actuator technology *"as an exclusive foundational component for Newton"*. **Flexion** uses Isaac Lab + Newton to scale its Reflect model, and Hugging Face / Pollen use it for [Microduck](microduck.md) ([release](../sources/nvidia-isaac-platform-gtc-berlin-2026.md)). What an "exclusive foundational" actuator component means for an open-source physics engine is not explained.

## MJWarp as a required solver path (2026-10)

Isaac Lab's native **BAM servo actuator** runs only on Newton with `MJWarpSolverCfg` and `use_newton_actuators=True`. Each physics step it writes its friction budget into MuJoCo's `dof_frictionloss`. Isaac Lab's docs note that *"MJWarp has no noslip solver"*, so a stiff friction-constraint option is offered to reduce creep. This is the first Isaac Lab feature in this wiki that is **gated to Newton's MuJoCo Warp solver** rather than being backend-agnostic ([NVIDIA Microduck tutorial](../sources/nvidia-microduck-ai-agents-sim-blog.md)).

## Related
- [MuJoCo Warp](mujoco-warp.md) — a component of Newton, jointly maintained by [Google DeepMind](google-deepmind.md) and NVIDIA.
- [OpenUSD](openusd.md) — the scene/physics substrate Newton consumes and extends.
- [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — primary integration.
- [MuJoCo Playground](mujoco-playground.md) — secondary integration; competes with MJX as the underlying physics.
- [NVIDIA](nvidia.md), [Google DeepMind](google-deepmind.md) — co-developers.

## Mentioned in
- [Isaac Lab-Arena GitHub](../sources/isaaclab-arena-github.md) — Arena moved to Isaac Lab 3.0 (Newton) in v0.2; September 2026 commits add Newton support for DROID control, a cable asset class and a gear-insertion environment; *"contact-rich insertion, cables, and deformables"* named as the next Newton-dependent benchmarks.
- [NVIDIA Newton Physics Engine Developer Page](../sources/nvidia-newton-physics-engine-developer-page.md)
- [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)
- [Using OpenUSD for Modular and Scalable Robotic Simulation](../sources/nvidia-openusd-for-robotic-simulation.md)
- [MuJoCo Playground Paper](../sources/mujoco-playground-paper.md)
- [NVIDIA advances Isaac platform (GTC Berlin, 2026-10-21)](../sources/nvidia-isaac-platform-gtc-berlin-2026.md)
- [Using AI agents to teach Microduck to walk in simulation (NVIDIA)](../sources/nvidia-microduck-ai-agents-sim-blog.md) — Newton models Microduck's physics; Isaac Lab's BAM actuator requires the MJWarp solver.

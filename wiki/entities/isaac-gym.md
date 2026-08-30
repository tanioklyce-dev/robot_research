---
title: NVIDIA Isaac Gym (deprecated)
type: entity
subtype: software
created: 2026-08-29
updated: 2026-08-29
sources: 1
tags: [isaac-gym, nvidia, simulator, gpu-physics, massively-parallel-rl, locomotion, deprecated, isaac-lab]
---

> [!warning] Deprecated — do not start new work here
> **Isaac Gym Preview 4 is the final release and is no longer supported.** NVIDIA's own product page is titled *"Isaac Gym — Now Deprecated,"* and [Isaac Lab](nvidia-isaac-lab.md) replaces it along with IsaacGymEnvs, OmniIsaacGymEnvs and Orbit `[live-web]` [NVIDIA](https://developer.nvidia.com/isaac-gym), [Isaac Lab migration guide](https://isaac-sim.github.io/IsaacLab/main/source/migration/migrating_from_isaacgymenvs.html). It also does not support recent GPU architectures. **This page exists because the literature does, not because the software should be used.**

**NVIDIA Isaac Gym** — the GPU-accelerated physics simulator that made massively parallel RL for robot locomotion practical. Its defining move: **keep the whole loop on the GPU.** Physics stepping, observation construction and policy inference all run on device, with observations and actions passed as tensors, eliminating the CPU↔GPU transfer that had bounded simulation throughput. The consequence was thousands of environments on **a single workstation GPU** instead of a CPU cluster.

Nearly every learned-locomotion result in this wiki traces through it.

## In this wiki

- **[Legged Locomotion in Challenging Terrains using Egocentric Vision](../sources/egocentric-vision-locomotion-paper.md)** trains in *"the IsaacGym (IG) simulator with the legged gym library"* — and the paper's central design constraint is a *simulation* constraint: rendering depth **slows simulation by an order of magnitude**, which is precisely why the authors adopt the two-phase scandots-then-distil recipe rather than training on depth directly.

That is the general pattern worth recording. **Isaac Gym made physics cheap and left rendering expensive**, and a great deal of locomotion methodology — proxy observations, privileged teachers, distillation into vision — is downstream of that asymmetry rather than of anything about robots.

## Why a deprecated simulator still matters

- **It dates the corpus.** Work from roughly 2021–2024 in legged locomotion assumes Isaac Gym's performance envelope. Reproducing it now means porting to [Isaac Lab](nvidia-isaac-lab.md).
- **The successor inherits the model, not the code.** [Isaac Lab](nvidia-isaac-lab.md) keeps massively parallel GPU vectorization while adding pluggable physics backends (PhysX, [Newton](newton-physics-engine.md), Warp, MuJoCo) on [Isaac Sim](nvidia-isaac-sim.md). The idea survived; the API did not.
- **A caution about tooling lineage.** A widely-adopted research tool was deprecated within a few years, stranding a large body of reproducible-in-principle work. Worth remembering when this wiki records that some result "was reproduced" — reproducibility has a shelf life set by the vendor.

## Related

- [Isaac Lab](nvidia-isaac-lab.md) — the replacement.
- [Isaac Sim](nvidia-isaac-sim.md) — what Isaac Lab runs on.
- [legged_gym](legged-gym.md) — the locomotion library built on Isaac Gym.
- [Egocentric-vision locomotion](../sources/egocentric-vision-locomotion-paper.md) — the ingested source that uses it.

## Mentioned in

- [Legged Locomotion in Challenging Terrains using Egocentric Vision](../sources/egocentric-vision-locomotion-paper.md) — training simulator, and the source of the rendering-cost constraint that shapes the method.

## Open questions / TBD

- **The Isaac Gym paper is uningested** (Makoviychuk et al., 2021) — it would anchor the GPU-physics claim with numbers rather than description.
- **Which simulator [LocoFormer](../sources/locoformer-paper.md) used** is not stated in the paper text read here; given the timing it may well be Isaac Lab rather than Isaac Gym.

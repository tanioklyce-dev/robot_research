---
title: legged_gym
type: entity
subtype: software
created: 2026-08-29
updated: 2026-08-29
sources: 2
tags: [legged-gym, eth-zurich, rsl, anymal, isaac-gym, locomotion, massively-parallel-rl, terrain-curriculum, open-source]
---

**legged_gym** — ETH Zurich's Robotic Systems Lab library for training legged-locomotion policies on [Isaac Gym](isaac-gym.md), released with **"Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning"** (Rudin, Hoeller, Reist & Hutter, CoRL 2021). The headline claim: policies for flat terrain in **under four minutes**, and rough terrain in about **twenty minutes**, on a **single workstation GPU**, demonstrated on ANYmal `[live-web]` [arXiv:2109.11978](https://arxiv.org/abs/2109.11978), [PMLR v164](https://proceedings.mlr.press/v164/rudin22a.html).

Open-sourcing it is why it matters here. **legged_gym became the default starting point for learned quadruped locomotion**, and its conventions — not just its speed — propagated into the work this wiki holds.

## In this wiki

The [egocentric-vision locomotion paper](../sources/egocentric-vision-locomotion-paper.md) uses it directly, and inherits more than the trainer:

- Training runs in *"the IsaacGym (IG) simulator with the **legged gym** library."*
- **The terrain curriculum is legged_gym's design**: terrains are generated at varying difficulty, arranged so difficulty increases across a grid, and robots are **promoted to harder terrain when they traverse more than half its length and demoted when they fail**. The egocentric-vision paper adopts this scheme explicitly.

That curriculum is the quiet contribution. A library that makes training fast is useful; a library that ships a **default answer to "how do you structure terrain difficulty"** shapes what every downstream paper measures — and a shared curriculum is part of why locomotion results from this period are comparable at all.

## Why it earns a page

- Named in the [awesome-physical-ai gap analysis](../sources/awesome-physical-ai-github.md) as part of the **RMA / legged_gym / H2O locomotion corpus** the wiki was missing. With [RMA](../sources/rma-paper.md), the [vision follow-up](../sources/egocentric-vision-locomotion-paper.md) and [LocoFormer](../sources/locoformer-paper.md) ingested, this page closes the tooling half of that gap.
- **Its speed claim is a methodology claim.** "Twenty minutes on one GPU" is what made terrain curricula, aggressive domain randomization, and large ablation sweeps affordable to academic labs — including the procedurally generated robot distributions [LocoFormer](../sources/locoformer-paper.md) later trains on.
- It sits on a **deprecated substrate**. [Isaac Gym](isaac-gym.md) is end-of-life, so reproducing legged_gym-era work now means porting to [Isaac Lab](nvidia-isaac-lab.md).

## Related

- [Isaac Gym](isaac-gym.md) — the simulator it is built on, now deprecated.
- [Isaac Lab](nvidia-isaac-lab.md) — where this lineage continues.
- [Egocentric-vision locomotion](../sources/egocentric-vision-locomotion-paper.md) — the ingested source that uses it and its terrain curriculum.
- [RMA](../sources/rma-paper.md) — the adjacent CMU/Berkeley line; same era, same problem, different lab.

## Mentioned in

- [Legged Locomotion in Challenging Terrains using Egocentric Vision](../sources/egocentric-vision-locomotion-paper.md) — training library and terrain-curriculum source.

## Open questions / TBD

- **The Rudin et al. paper is uningested** — the primary for every number on this page, and the reference for the terrain curriculum that several ingested sources inherit.
- **Current maintenance status** unrecorded, and complicated by Isaac Gym's deprecation.
- **ANYmal has no entity page**, despite appearing as legged_gym's demonstration robot and in [LocoFormer](../sources/locoformer-paper.md)'s zero-shot test set (ETH ANYmal C, 0.95).

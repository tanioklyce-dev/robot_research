---
title: Biomechanical simulation
type: concept
created: 2026-05-08
updated: 2026-05-08
sources: 3
tags: [biomechanics, animal-simulation, drosophila, mujoco, virtual-rodent, embodied-ai]
---

**Biomechanical simulation** is physics-based simulation of an animal body — anatomically detailed morphology, joints, actuators, and (sometimes) muscles — typically used as a substrate for studying neural control of sensorimotor behaviour. Distinct from the *robot*-body simulators that dominate the rest of this wiki: the goal is biological fidelity, not robot deployment.

## Defining feature

A biomechanical simulation answers: *given a body that looks and moves like a real animal, what neural controller produces realistic behaviour?* Inputs are anatomical imaging (microscopy, X-ray nano-tomography) + behavioural recordings (high-speed video, motion capture). Outputs are body-level physics that can be driven by hand-coded, learnt, or connectome-constrained controllers.

## Lineage (per the [flybody Paper](../sources/flybody-paper.md))

| Year | Organism | Project | Note |
|---|---|---|---|
| 2008 | Fruit fly | Grand Unified Fly (Dickson et al.) | Simplified body + hand-designed visually-guided flight |
| 2012 | *C. elegans* | Boyle et al. | Worm; integrated neuromechanical |
| 2020 | Rodent | Virtual Rodent (Merel et al., DeepMind) | Whole-body, deep RL imitation; direct DeepMind ancestor of flybody |
| 2022 | Fruit fly | NeuroMechFly v1 (Lobato-Rios et al., EPFL) | Walking + grooming; heuristic low-level controller |
| 2023 | Hydra | Wang et al. | Soft-body whole-organism |
| 2024 | Fruit fly | NeuroMechFly v2 (Wang-Chen et al.) | Walking + learnt high-level controller |
| 2025 | Fruit fly | [flybody](../entities/flybody.md) (Vaxenburg et al.) | **Walking + flight unified**, deep-RL end-to-end |

## What's typically modelled

- **Skeleton** — rigid-body chain with anatomical joint pivots from microscopy.
- **Muscles or torque actuators** — ranges from idealized joint torques (flybody) to detailed muscle insertion sites + activation dynamics (the "ideal" rarely fully achieved).
- **Surface contact** — friction + adhesion (insects need foot adhesion; mammals don't).
- **Fluid forces** — phenomenological aerodynamics for flying organisms (flybody fits drag/lift coefficients to real fly hovering trajectories).
- **Sensors** — eyes, proprioceptors, mechanoreceptors. Usually idealized in current models.

## What's typically NOT modelled

- **Real muscle physiology** — most projects use torque actuators or lumped muscle approximations.
- **Soft tissue** beyond simple collision geometries.
- **Connectome** — the controller is a generic neural network or hand-designed. Connectome integration is the open frontier (see [Whole-organism agentic AI](../syntheses/whole-organism-agentic-ai.md)).

## Common stack

- **Physics engine.** [MuJoCo](../entities/mujoco.md) is dominant — used by flybody, NeuroMechFly v2, virtual rodent. Choice tracks the broader RL ecosystem.
- **Imaging.** Confocal fluorescence microscopy (flybody), micro-CT, X-ray holographic nano-tomography.
- **Behavioural reference data.** APT / SLEAP / Anipose pose tracking; high-speed videography.
- **RL framework.** DMPO + Acme + Ray (flybody, virtual rodent); MPO and PPO common.

## Why it matters here

- **Cousin to robot simulation.** The toolchain is shared with mainstream robotics (MuJoCo, RL imitation), but the *goal* differs — fidelity to a biological organism rather than transfer to a deployable robot.
- **Brain-side bridge.** Provides the *body* for whole-organism agentic AI. The brain side comes from connectomes (see [Connectome](connectome.md)).
- **Curriculum-design parallel.** Hierarchical pretrained-low-level + new-high-level (flybody's vision-guided flight) is the same pattern as robotics RL curricula — a transferable tool.

## Related

- [Connectome](connectome.md) — companion concept (brain side).
- [flybody](../entities/flybody.md) — current state-of-the-art *Drosophila* whole-body sim.
- [NeuroMechFly](../entities/neuromechfly.md) — predecessor.
- [MuJoCo](../entities/mujoco.md) — dominant physics backend.
- [Imitation learning](imitation-learning.md) — typical training paradigm.
- [Whole-organism agentic AI](../syntheses/whole-organism-agentic-ai.md) — synthesis.

## Mentioned in

- [flybody Paper](../sources/flybody-paper.md)
- [flybody GitHub](../sources/flybody-github.md)

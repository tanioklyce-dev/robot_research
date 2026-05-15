---
title: flybody
type: entity
subtype: simulator-body-model
created: 2026-05-08
updated: 2026-05-15
sources: 7
tags: [flybody, drosophila, mujoco, biomechanical-simulation, deep-rl, hhmi-janelia, deepmind, open-source]
---

**flybody** — anatomically detailed whole-body physics simulation of *Drosophila melanogaster* in [MuJoCo](mujoco.md), released open-source (Apache-2.0) by HHMI Janelia (Turaga lab) and Google DeepMind. The platform supports both terrestrial walking and aerial flight, with closed-loop neural controllers trained via deep RL ([flybody Paper](../sources/flybody-paper.md), [GitHub](../sources/flybody-github.md)).

## Body model

- **67 rigid-body components, 102 DoFs**, torque-actuated joints.
- Geometry from confocal fluorescence microscopy of an adult female fly; manual segmentation in Fiji; mesh simplification in Blender; custom Blender-to-MuJoCo export plug-in.
- **Phenomenological fluid model** for wing aerodynamics (drag, lift, Magnus effect approximations).
- **Adhesion actuators** modelling tarsal adhesion to surfaces; enables walking on inclines and ceilings via injection of normal contact force.
- **Wing pattern generator (WPG)**: lookup-table baseline wing-beat pattern at ~218 Hz (the *D. melanogaster* mean), variable ±10%; MLP policy outputs corrective signals summed onto the WPG output.
- Eye cameras placed on the model head for vision-driven flight tasks.

## Tasks released

| Task | Action space | Reference data | Notes |
|---|---|---|---|
| Walking imitation | 59-dim | ~13–16k snippets, ~64–80 min real-fly walking | APT 2D pose tracking + IK lifting |
| Flight imitation | MLP + WPG | 272 trajectories (~53 s), 7,500 fps | Saccades + visual evasion |
| Vision-guided flight: bumps | Hierarchical | Pretrained low-level + new CNN navigator | Maintain altitude over sine bumps |
| Vision-guided flight: trench | Hierarchical | " | Navigate sine-shaped trench corridor |
| Adhesion bumps | Walking | One walking snippet | Train to overcome up to 72° inclination |
| Inverse-kinematics grooming | Demo | — | Demonstrates non-locomotion behavioural repertoire |

## Stack

- **Physics:** [MuJoCo](mujoco.md) (vanilla, not MJX).
- **Environments:** [DM Control](dm-control.md) `dm_control` framework.
- **RL:** **DMPO** (distributional MPO) via DeepMind's Acme + Reverb; Adam optimizer.
- **Distributed training:** Ray.
- **Language:** Python 3.10.
- **License:** Apache-2.0.

## Lineage

- **Predecessors.** Grand Unified Fly (Dickson et al. 2008), [NeuroMechFly](neuromechfly.md) v1 (Lobato-Rios 2022) — walking + grooming, heuristic controller, virtual rodent (Merel et al. 2020), Hydra (Wang et al. 2023), *C. elegans* (Boyle et al. 2012).
- **Contemporaries.** [NeuroMechFly v2](neuromechfly.md) (Wang-Chen 2024; flygym v2.x.x in 2026) is a parallel open-source *Drosophila* sim from EPFL's NeLy lab. Capability split is sharp: flybody owns flight + flat-policy RL; NeuroMechFly v2 owns olfaction + mechanosensory richness + brain–VNC hierarchy. Both are Apache-2.0 on MuJoCo. See [NeuroMechFly entity](neuromechfly.md) for the comparison table.
- **Position.** flybody **unifies flight and walking** in a single body — a first for *Drosophila* models, and still uniquely capable of flight as of 2026.

## Datasets

- **Figshare** `10.25378/janelia.25309105` — body model meshes, walking and flight reference datasets, supplementary tables.

## Why it matters here

- **MuJoCo as a biology platform.** Reinforces MuJoCo's centrality and adds a biology-flavoured carrier alongside the existing robotics-flavoured carriers ([MuJoCo Playground](mujoco-playground.md), [Gymnasium-Robotics](gymnasium-robotics.md)).
- **Imitation learning at scale on a non-rigid body.** DMPO-on-imitation generalizes to a 102-DoF morphology with wings — a meaningful stress test of the DeepMimic / virtual-rodent recipe.
- **Whole-organism agentic AI.** Combined with the [FlyWire](flywire.md) connectome and Shiu et al.'s [brain dynamics](../sources/berkeley-fly-brain-news.md), flybody is one half of a plausible "whole-fly agent" research direction. See [Whole-organism agentic AI](../syntheses/whole-organism-agentic-ai.md).

## Related

- [HHMI Janelia](hhmi-janelia.md) — host institution (TuragaLab).
- [Google DeepMind](google-deepmind.md) — co-developer (Tassa, Botvinick, Novati).
- [MuJoCo](mujoco.md) — physics backend.
- [DM Control](dm-control.md) — control API.
- [NeuroMechFly](neuromechfly.md) — predecessor; walking-focused.
- [Drosophila melanogaster](drosophila.md) — model organism.
- [Imitation learning](../concepts/imitation-learning.md) — training paradigm.
- [Biomechanical simulation](../concepts/biomechanical-simulation.md) — concept umbrella.
- [flyvis](flyvis.md) — sister project from the same lab (Turaga); brain-side connectome-constrained controller template; the natural integration partner.
- [Drosophila brain model](drosophila-brain-model.md) — independent brain-side codebase (Shiu et al.); mechanistic-LIF alternative.

## Mentioned in

- [flybody Paper (Vaxenburg et al. 2025, Nature)](../sources/flybody-paper.md)
- [flybody GitHub](../sources/flybody-github.md)

---
title: "Whole-body physics simulation of fruit fly locomotion (Vaxenburg et al. 2025)"
type: source
subtype: paper
created: 2026-05-08
updated: 2026-05-08
url: https://doi.org/10.1038/s41586-025-09029-4
author: Vaxenburg, Siwanowicz, Merel, Robie, Morrow, Novati, Stefanidi, Both, Card, Reiser, Botvinick, Branson, Tassa, Turaga
published: 2025-04-23
ingested: 2026-05-08
journal: "Nature 643:1312–1320"
tags: [drosophila, mujoco, biomechanical-simulation, deep-rl, dmpo, imitation-learning, vision-guided-flight, hierarchical-control]
---

## Summary

Open-access *Nature* paper (received 2 Apr 2024, accepted 15 Apr 2025, published 23 Apr 2025) introducing [flybody](../entities/flybody.md) — a whole-body physics simulation of *Drosophila melanogaster* in [MuJoCo](../entities/mujoco.md). 67 rigid-body components, 102 DoFs, torque-actuated joints, with **phenomenological fluid and adhesion forces** to support both flight and walking. Closed-loop neural controllers are trained via deep RL ([DMPO](../entities/google-deepmind.md)) with imitation learning against high-speed kinematic recordings of real flies, then composed hierarchically: a pretrained low-level flight controller is reused under a vision-driven high-level controller for trench navigation and altitude control over bumpy terrain. The authors release the body model, physics, datasets, and pretrained controllers as open source ([flybody GitHub](flybody-github.md)).

Corresponding authors: **Yuval Tassa** (Google DeepMind, MuJoCo author) and **Srinivas C. Turaga** (HHMI Janelia). Full author list spans HHMI Janelia, Google DeepMind, Fauna Robotics, Tübingen, Columbia, and the UCL Gatsby Computational Neuroscience Unit.

## Thesis

> "The body of an animal influences how its nervous system generates behaviour. Accurately modelling the neural control of sensorimotor behaviour requires an anatomically detailed biomechanical representation of the body."

The paper frames an anatomically detailed body model as a *prerequisite* for studying neural control of behaviour — and positions the open-source release as a substrate for the next decade of *brain–body* models, eventually pairable with the [FlyWire](../entities/flywire.md) connectome.

## Key claims

### Body model
- **67 rigid-body components, 102 DoFs.** Torque-actuated joints.
- **Built in [MuJoCo](../entities/mujoco.md).** Geometry sourced from confocal fluorescence microscopy of an adult female fly; manual segmentation in Fiji; mesh simplification in Blender; custom Blender→MuJoCo export plug-in.
- **Phenomenological fluid model** for wing aerodynamics — fitted to a real *D. melanogaster* hovering wing trajectory (`fmech` dataset). Final fluid-coefficient tuple `[1.0, 0.5, 1.5, 1.7, 1.0]`. Wing actuator gains `[18, 18, 18]`, joint damping `0.007769`.
- **Adhesion actuators** for foot–surface contact, allowing the model to walk on inclined and bumpy surfaces. Adhesion injects normal contact force, expanding the friction cone margin. Coulomb friction with elliptic friction cones; static friction coefficient `μ = 1`, cone angle `θ = 45°`.
- **Wing pattern generator (WPG).** Lookup-table baseline wing-beat pattern; the policy outputs corrections summed onto the WPG output. Wing-beat frequency variable within ±10% of the *D. melanogaster* average **218 Hz**.

### Reference data and tasks
- **Walking dataset.** ~13,000 / ~16,000 walking snippets (~64–80 min of fly walking) from APT 2D pose tracking of freely walking *Drosophila*, lifted to 3D via inverse-kinematics fitting to a default standing pose. Released on Figshare (`10.25378/janelia.25309105`).
- **Flight dataset.** 272 trajectories (~53 s of real-time flight) from previously recorded *D. hydei* free-flight trajectories — 44 saccades + 92 evasion manoeuvres + symmetric mirroring. 7,500 fps capture.
- **Walking imitation task.** Single MLP policy trained to imitate CoM position, body orientation, and detailed leg movements across 3,200 test trajectories.
- **Flight imitation task.** Single MLP+WPG policy trained on 216 trajectories; reuses naturalistic saccades and evasion manoeuvres.
- **Hierarchical vision-guided flight.** Pretrained low-level flight controller is *frozen*; a high-level CNN-based "navigator" controller is trained end-to-end with RL to produce visually-guided flight in two tasks:
  - **Bumps task.** Maintain target altitude above sine-bump terrain.
  - **Trench task.** Navigate a sine-shaped trench corridor. Median height error 0.032 cm, median speed error 0.16 cm/s after acceleration phase (1,000 test episodes).
- **Adhesion overcoming bumps task.** Demonstrates learnt selective use of T1/T2 leg pairs uphill, T3 downhill on bumps with up to 72° inclination.
- **Inverse-kinematics grooming demo** illustrates that the body supports a behavioural repertoire beyond locomotion.

### RL stack
- **DMPO** — distributional MPO ([Abdolmaleki et al. MPO/REPO](https://arxiv.org/abs/1812.02256)). Distributional value head per Bellemare et al. (C51).
- **Distributed training.** [Acme](https://arxiv.org/abs/2006.00979) framework, [Reverb](https://arxiv.org/abs/2102.04736) replay, **[Ray](https://arxiv.org/abs/1712.05889)** parallelization, Adam optimizer.
- **Simulation timesteps.** Flight: 0.05-ms physics / 0.2-ms control. Walking: 2-ms control timestep.

### Ancestry and positioning
The paper situates flybody against:
- **Grand Unified Fly** (Dickson et al. 2008) — pioneered closed-loop visually guided flight on a simplified body.
- **NeuroMechFly** (Lobato-Rios et al. 2022, *Nat. Methods*) and **NeuroMechFly v2** (Wang-Chen et al. 2024, *Nat. Methods*) — anatomically detailed walking body, heuristic low-level controller + learnt high-level controller. flybody **unifies flight and walking in one model**.
- **Virtual rodent** (Merel et al. 2020, ICLR) — direct DeepMind ancestor; same DMPO + imitation-learning blueprint, scaled to mammalian body.
- *C. elegans* model (Boyle et al. 2012), **Hydra** model (Wang et al. 2023) — earlier whole-organism biomechanical sims.

### Discussion / future directions
- *"In the long term, combining our whole-body model with a complete nervous system connectome ([FlyWire](../entities/flywire.md)), comprehensive behavioural measurements and connectome-constrained deep neural network modelling could enable the development of whole-animal models of the entire body and nervous system of the adult fruit fly."*
- Cross-cites the FlyWire connectome papers (Dorkenwald et al. 2024; Schlegel et al. 2024) and connectome-constrained predictors (Lappalainen et al. 2024; Mi et al. 2022) as the brain-side complement to flybody's body-side platform.

## Entities mentioned

- [flybody](../entities/flybody.md) — the released simulator, body model, and pretrained controllers.
- [HHMI Janelia](../entities/hhmi-janelia.md) — primary institution.
- [Google DeepMind](../entities/google-deepmind.md) — co-developer; Yuval Tassa is corresponding author.
- [MuJoCo](../entities/mujoco.md) — physics engine.
- [DM Control](../entities/dm-control.md) — `dm_control` Python framework used by flybody.
- [FlyWire](../entities/flywire.md) — connectome (referenced as the brain-side complement, not used as an input here).
- [Drosophila melanogaster](../entities/drosophila.md) — model organism.
- [NeuroMechFly](../entities/neuromechfly.md) — predecessor body sim.

## Concepts touched

- [Biomechanical simulation](../concepts/bio/biomechanical-simulation.md) — flybody is the latest entry in the worm/Hydra/rodent/fly lineage.
- [Imitation learning](../concepts/learning/imitation-learning.md) — DeepMimic-style imitation against high-speed real-fly trajectories.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — inverse direction here: real fly data → sim policy. Same toolchain.
- [World model](../concepts/world-models/world-model.md) — orthogonal: flybody is a *physics-based* simulator, not a learned dynamics model.

## Open questions

- **No connectome integration.** flybody intentionally stops at the body. The combination with FlyWire is gestured at in Discussion but not implemented. See [Whole-organism agentic AI](../syntheses/agents/whole-organism-agentic-ai.md).
- **Muscle actuation is simplified to torques.** The paper notes incorporating real muscle actuation across the whole body "will require substantial effort" — needs muscle insertion sites, DoFs, and activation dynamics.
- **No proprioception model.** Sensory inputs are idealized; the proprioceptor mapping (hair plates, etc.) is acknowledged as future work.
- **MJX port?** The paper doesn't mention an MJX (JAX/GPU) version of flybody. Distributed RL relies on Ray + Acme over CPU MuJoCo — running cost is not stated.

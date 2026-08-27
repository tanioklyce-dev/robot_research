---
title: Google DeepMind
type: entity
subtype: company
created: 2026-05-06
updated: 2026-08-03
sources: 32
tags: [google-deepmind, mujoco, newton, mjcphysics, openusd, robotics-research, biomechanics, dmpo, acme, gemini-robotics, genie, world-model]
---

Google's AI research lab. Maintains MuJoCo and [MuJoCo Playground](mujoco-playground.md), co-developed the [Newton physics engine](newton-physics-engine.md) with [NVIDIA](nvidia.md) and [Disney Research](disney-research.md) under the Linux Foundation, and ships **`MjcPhysics`** — a USD schema plugin that brings MuJoCo solver parameters into [OpenUSD](openusd.md) scenes. Separately, ships the [Gemini Robotics](gemini-robotics.md) family of robot foundation models (full VLA + the **-ER** embodied-reasoning VLM variant).

## Robotics simulation contributions
- **MuJoCo** — the open-source physics engine (acquired and open-sourced by DeepMind in 2021).
- **[MuJoCo Playground](mujoco-playground.md)** — robot-learning framework on MJX, presented at RSS 2025.
- **[Newton physics engine](newton-physics-engine.md)** co-development under Linux Foundation governance.
- **`MjcPhysics` USD schema plugin** — MuJoCo-specific solver attributes (integrator, constraint solver algorithm, tolerance, contact settings) authored as USD prims. Concrete evidence that DeepMind is invested in [OpenUSD](openusd.md) as a cross-stack substrate, not just consuming it ([NVIDIA OpenUSD-for-robotic-simulation blog](../sources/nvidia-openusd-for-robotic-simulation.md)).
- **`mujoco-usd-converter`** — MuJoCo-to-USD bridge tool hosted in the `newton-physics` GitHub org, used alongside `MjcPhysics` schemas.

## Robot foundation models
- **[Gemini Robotics](gemini-robotics.md)** — robot foundation model family built on the Gemini multimodal line. Two variants: a full **vision-language-action** model (emits low-level actions, listed on the [VLA models](../concepts/learning/vla-models.md) concept page) and **Gemini Robotics-ER** (embodied-reasoning VLM that emits tool calls against a robot's API; fits the [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) pattern).
- **Formal partnership with [Boston Dynamics](boston-dynamics.md)** — announced separately; characterized as early-stage in the [BD Spot + Gemini Robotics blog](../sources/bostondynamics-spot-gemini-robotics.md). Productized via Boston Dynamics' AIVI-Learning offering powered by Gemini Robotics-ER 1.6.

## Generative world models
- **[Genie 3](genie-3.md)** — DeepMind's general-purpose generative world model that produces "photorealistic and interactive 3D environments" (generative-video family; see [world model](../concepts/world-models/world-model.md)). Designed to be **post-trained into domain instruments**: [Waymo](waymo.md) built its [Waymo World Model](../sources/waymo-world-model.md) (AV simulation, camera+lidar) on top of it ([Waymo World Model blog](../sources/waymo-world-model.md)). Genie 3's own architecture/scale is not yet in the wiki (thin entry pending a primary DeepMind source). Distinct from [AGIBOT](agibot.md)'s similarly-named Genie Envisioner / Genie Sim.

## Biological / biomechanical simulation
- **Virtual Rodent** (Merel et al. 2020, ICLR) — anatomically detailed mouse body in MuJoCo, deep-RL imitation. Direct ancestor of flybody.
- **[flybody](flybody.md)** (Vaxenburg et al. 2025, *Nature*) — *Drosophila* whole-body simulator co-developed with [HHMI Janelia](hhmi-janelia.md). DeepMind contributed Yuval Tassa (corresponding author, MuJoCo lead), Matthew Botvinick, Guido Novati, plus the DMPO + Acme + Reverb training stack. Released open-source (Apache-2.0).
- **DMPO + Acme + Reverb** — DeepMind's standard distributed-RL stack, used by both virtual rodent and flybody.

## Mentioned in

> [!note] Curated list — **33** source pages link here; the ones below are those that shaped this page.

- [MuJoCo Playground Paper](../sources/mujoco-playground-paper.md)
- [NVIDIA Newton Physics Engine Developer Page](../sources/nvidia-newton-physics-engine-developer-page.md)
- [Using OpenUSD for Modular and Scalable Robotic Simulation](../sources/nvidia-openusd-for-robotic-simulation.md)
- [flybody Paper](../sources/flybody-paper.md)
- [flybody GitHub](../sources/flybody-github.md)
- [Tools for Your To Do List with Spot and Gemini Robotics (Boston Dynamics blog)](../sources/bostondynamics-spot-gemini-robotics.md)
- [The Waymo World Model blog](../sources/waymo-world-model.md) — Waymo built its driving world model on DeepMind's Genie 3
- [DeepMind Gemini Robotics model page](../sources/deepmind-gemini-robotics-model-page.md) — the current Gemini Robotics family page; three models, three access tiers, ER 2 in public preview via AI Studio.
- [ASIMOV Benchmark paper](../sources/asimov-benchmark-paper.md) · [Predictive Red Teaming](../sources/predictive-red-teaming-paper.md) · [Veo world simulator evaluation](../sources/veo-robotics-policy-evaluation-paper.md) · [Safely Learning Dynamical Systems](../sources/safely-learning-dynamical-systems-paper.md) — the four-paper robot-safety program, connected by [Vikas Sindhwani](vikas-sindhwani.md).
- [Responsibly advancing AI and robotics](../sources/deepmind-gemini-robotics-safety-page.md) — the public safety framing that indexes it.
- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../sources/hai-world-model-spatial-intelligence-brief.md) — named first among the tech incumbents leading the world-model push; [Genie 3](genie-3.md) is the brief's frontier example, with a few-minutes-of-coherence limit at its 2025 release.

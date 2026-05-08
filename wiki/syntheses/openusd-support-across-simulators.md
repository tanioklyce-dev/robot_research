---
title: OpenUSD support across simulators
type: synthesis
created: 2026-05-07
updated: 2026-05-07
tags: [openusd, simulators, usdphysics, isaac-sim, mujoco, newton, genesis, maniskill, reference]
---

# OpenUSD support across simulators

A reference catalog of which agentic-robotics simulators in this wiki consume [OpenUSD](../entities/openusd.md), how, and which are exceptions. Companion to [Newton + OpenUSD — the substrate convergence](newton-openusd-substrate-convergence.md) (the structural argument) and [the OpenUSD entity page](../entities/openusd.md) (the format itself).

## At a glance

| Simulator | OpenUSD support | Mechanism |
|---|---|---|
| [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) | **Native** | USD is the scene format. Omniverse Kit 107 → OpenUSD 24.05. |
| [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) | **Native** | Built on Isaac Sim; USD passes through. |
| [AGIBOT Genie Sim 3.0](../entities/agibot-genie-sim.md) | **Native** (inherited) | Built on Isaac Sim / Omniverse. |
| [MuJoCo Playground](../entities/mujoco-playground.md) / [MuJoCo](../entities/mujoco.md) | **Via plugin + converter** | DeepMind's `MjcPhysics` USD schema plugin authors MuJoCo solver attributes onto USD prims; `mujoco-usd-converter` (in `newton-physics` GitHub org) bridges MJCF↔USD. |
| [Newton physics engine](../entities/newton-physics-engine.md) | **Substrate** (not a simulator stack) | Ships `NewtonSceneAPI` / `newton-usd-schemas` (Apache 2.0, Linux Foundation governed). Pluggable into Isaac Lab and MuJoCo Playground. |
| [Genesis](../entities/genesis.md) | **None documented** | Custom Python-first physics; no USD support documented in ingested sources. |
| [ManiSkill](../entities/maniskill.md) / [SAPIEN](../entities/sapien.md) | **None documented** | UCSD/Hillbot stack; no USD support documented in ingested sources. |
| [Gymnasium-Robotics](../entities/gymnasium-robotics.md) | **None** | MuJoCo-backed via MJCF only. |

## Native USD simulators

### [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) / [Isaac Lab](../entities/nvidia-isaac-lab.md)

The flagship USD-native robotics stack. **Isaac Sim 5.0** runs on Omniverse Kit SDK 107 → **OpenUSD 24.05** ([NVIDIA OpenUSD-for-robotic-simulation blog](../sources/nvidia-openusd-for-robotic-simulation.md), March 2025). Scene composition, asset interchange, and physics-schema authoring all happen against USD. Isaac Lab inherits the same substrate.

USD here isn't just a load format — it's the runtime scene representation. Articulated robots are described via `PhysicsArticulationRootAPI` and joint-subtype prims; collision, mass, and inertia are USD-schema attributes ([UsdPhysics whitepaper](../sources/openusd-rigid-body-physics-proposal.md)).

### [AGIBOT Genie Sim 3.0](../entities/agibot-genie-sim.md)

CES 2026 launch. Built on top of Isaac Sim / Omniverse, so USD support is inherited rather than independent. Adds LLM-driven scene generation and a 100k-scenario evaluation suite for [VLA models](../concepts/vla-models.md) ([CES 2026 announcement](../sources/agibot-genie-sim-3-announcement.md)).

## USD via plugin / converter

### [MuJoCo](../entities/mujoco.md) and [MuJoCo Playground](../entities/mujoco-playground.md)

MuJoCo's native scene format is **MJCF**, not USD. But two pieces of [Google DeepMind](../entities/google-deepmind.md)-led infrastructure bridge it to USD:

- **`MjcPhysics`** — USD schema plugin maintained by DeepMind. Authors MuJoCo-specific solver attributes (integrator type, constraint solver algorithm, contact settings) onto USD prims, allowing MuJoCo's solver-specific knowledge to live inside a USD scene. The existence of this plugin is the strongest signal that DeepMind is committed to USD as cross-stack substrate, not just consuming it ([OpenUSD entity](../entities/openusd.md), [substrate-convergence synthesis](newton-openusd-substrate-convergence.md)).
- **`mujoco-usd-converter`** — bridge tool living in the `newton-physics` GitHub org. Converts MJCF assets to OpenUSD with `MjcPhysics` schemas. Notable that the cross-stack bridge is hosted in the cross-vendor governance domain, not by either parent vendor.

So MuJoCo doesn't natively read USD, but the plugin + converter make MJCF↔USD round-trip possible — and DeepMind's investment makes USD a first-class citizen of the MuJoCo stack going forward.

## Substrate (not a simulator)

### [Newton](../entities/newton-physics-engine.md)

Newton is a physics engine, not a simulator stack — pluggable into both Isaac Lab and MuJoCo Playground ([MuJoCo Playground Paper](../sources/mujoco-playground-paper.md) confirms "optionally backends to Newton in 2026"). Its USD relationship:

- **`NewtonSceneAPI`** / **`newton-usd-schemas`** (Apache 2.0, Linux Foundation governed) defines Newton-specific solver parameters (`newton:timeStepsPerSecond`, gravity, solver iterations) on USD prims.
- Designed as a "proving ground" — physically meaningful parameters generalizable across multiple Newton solvers may eventually be **promoted into upstream `UsdPhysics`** ([OpenUSD entity](../entities/openusd.md)).
- v0.2.0 released 2026-05-07; 52 commits, 7 releases — actively developed.

Newton's contribution to the USD picture is that the **physics schema layer itself is being co-developed in the open**, not just the scene format.

## Non-USD simulators

### [Genesis](../entities/genesis.md)

Custom Python-first physics engine; no USD support documented in ingested sources ([Genesis Project Page](../sources/genesis-project-page.md)). Headlines on speed (43M FPS Franka) and integrated photorealistic rendering, but the asset/scene pipeline is its own. The [substrate-convergence synthesis](newton-openusd-substrate-convergence.md) flags Genesis as one of the post-2026 exceptions that has to justify the non-Newton, non-USD choice.

### [ManiSkill](../entities/maniskill.md) / [SAPIEN](../entities/sapien.md)

GPU-parallel manipulation benchmark out of Hao Su's lab at UCSD, built on the SAPIEN simulation framework ([ManiSkill-HAB Paper](../sources/maniskill-hab-paper.md)). No USD support documented. Like Genesis, it's a non-Newton, non-USD silo as of 2026.

### [Gymnasium-Robotics](../entities/gymnasium-robotics.md)

The Farama Foundation's [MuJoCo](../entities/mujoco.md)-backed env families (Fetch, Shadow Hand, Maze, Adroit, Franka Kitchen, MaMuJoCo). MJCF only; the same MuJoCo USD plugin path applies in principle but is not part of the Gymnasium-Robotics distribution itself ([docs](../sources/gymnasium-robotics-docs.md)).

## Roadmap caveats

> [!note] URDF / MJCF / SDFormat → OpenUSD mapping is planned but unshipped
> The [NVIDIA OpenUSD blog](../sources/nvidia-openusd-for-robotic-simulation.md) (March 2025) lists conceptual mapping from URDF / MJCF / SDFormat to USD as **planned roadmap work, not yet shipped**. As of 2026-05 the wiki has not ingested confirmation that the mapping has fully landed. The [practitioner survey](../sources/source-robotics-urdf-mjcf-usd-comparison.md) still treats URDF, MJCF, and USD as stratifying by use case rather than collapsing into one.

> [!note] Joint / kinematic survival through CAD→USD is the open question
> CAD-to-USD pipelines ([NVIDIA JT workflows](../sources/nvidia-cad-to-usd-jt-workflows.md)) preserve geometry, hierarchy, and metadata well, but no ingested source documents automated SolidWorks-mate-to-`PhysicsJoint` conversion. Joint topology is presumably re-authored inside USD/Isaac Sim after geometry import.

## Sources used in this synthesis

- [Using OpenUSD for Modular and Scalable Robotic Simulation](../sources/nvidia-openusd-for-robotic-simulation.md)
- [OpenUSD Rigid Body Physics Proposal](../sources/openusd-rigid-body-physics-proposal.md)
- [NVIDIA Newton Physics Engine Developer Page](../sources/nvidia-newton-physics-engine-developer-page.md)
- [MuJoCo Playground Paper](../sources/mujoco-playground-paper.md)
- [AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)
- [Genesis Project Page](../sources/genesis-project-page.md)
- [ManiSkill-HAB Paper](../sources/maniskill-hab-paper.md)
- [Gymnasium-Robotics Documentation](../sources/gymnasium-robotics-docs.md)
- [Robot Simulation File Formats — URDF vs MJCF vs USD](../sources/source-robotics-urdf-mjcf-usd-comparison.md)
- [Building CAD-to-USD Workflows with NVIDIA Omniverse](../sources/nvidia-cad-to-usd-jt-workflows.md)

## Related

- [OpenUSD](../entities/openusd.md) — entity page covering the format, UsdPhysics schema, and per-solver extensions.
- [Newton + OpenUSD — the substrate convergence](newton-openusd-substrate-convergence.md) — structural argument for why this convergence matters.
- [Simulators for agentic robotics — 2026 landscape](simulators-for-agentic-robotics-2026.md) — broader simulator survey.
- [Why JEPA research skips the simulator stack](why-jepa-research-skips-the-simulator-stack.md) — companion synthesis filed at the same time.

---
title: OpenUSD support across simulators
type: synthesis
created: 2026-05-07
updated: 2026-05-07
tags: [openusd, simulators, usdphysics, isaac-sim, mujoco, newton, genesis, maniskill, reference]
---

# OpenUSD support across simulators

A reference catalog of which agentic-robotics simulators in this wiki consume [[openusd|OpenUSD]], how, and which are exceptions. Companion to [[newton-openusd-substrate-convergence|Newton + OpenUSD — the substrate convergence]] (the structural argument) and [[openusd|the OpenUSD entity page]] (the format itself).

## At a glance

| Simulator | OpenUSD support | Mechanism |
|---|---|---|
| [[nvidia-isaac-sim\|NVIDIA Isaac Sim]] | **Native** | USD is the scene format. Omniverse Kit 107 → OpenUSD 24.05. |
| [[nvidia-isaac-lab\|NVIDIA Isaac Lab]] | **Native** | Built on Isaac Sim; USD passes through. |
| [[agibot-genie-sim\|AGIBOT Genie Sim 3.0]] | **Native** (inherited) | Built on Isaac Sim / Omniverse. |
| [[mujoco-playground\|MuJoCo Playground]] / [[mujoco\|MuJoCo]] | **Via plugin + converter** | DeepMind's `MjcPhysics` USD schema plugin authors MuJoCo solver attributes onto USD prims; `mujoco-usd-converter` (in `newton-physics` GitHub org) bridges MJCF↔USD. |
| [[newton-physics-engine\|Newton physics engine]] | **Substrate** (not a simulator stack) | Ships `NewtonSceneAPI` / `newton-usd-schemas` (Apache 2.0, Linux Foundation governed). Pluggable into Isaac Lab and MuJoCo Playground. |
| [[genesis\|Genesis]] | **None documented** | Custom Python-first physics; no USD support documented in ingested sources. |
| [[maniskill\|ManiSkill]] / [[sapien\|SAPIEN]] | **None documented** | UCSD/Hillbot stack; no USD support documented in ingested sources. |
| [[gymnasium-robotics\|Gymnasium-Robotics]] | **None** | MuJoCo-backed via MJCF only. |

## Native USD simulators

### [[nvidia-isaac-sim|NVIDIA Isaac Sim]] / [[nvidia-isaac-lab|Isaac Lab]]

The flagship USD-native robotics stack. **Isaac Sim 5.0** runs on Omniverse Kit SDK 107 → **OpenUSD 24.05** ([[nvidia-openusd-for-robotic-simulation|NVIDIA OpenUSD-for-robotic-simulation blog]], March 2025). Scene composition, asset interchange, and physics-schema authoring all happen against USD. Isaac Lab inherits the same substrate.

USD here isn't just a load format — it's the runtime scene representation. Articulated robots are described via `PhysicsArticulationRootAPI` and joint-subtype prims; collision, mass, and inertia are USD-schema attributes ([[openusd-rigid-body-physics-proposal|UsdPhysics whitepaper]]).

### [[agibot-genie-sim|AGIBOT Genie Sim 3.0]]

CES 2026 launch. Built on top of Isaac Sim / Omniverse, so USD support is inherited rather than independent. Adds LLM-driven scene generation and a 100k-scenario evaluation suite for [[vla-models|VLA models]] ([[agibot-genie-sim-3-announcement|CES 2026 announcement]]).

## USD via plugin / converter

### [[mujoco|MuJoCo]] and [[mujoco-playground|MuJoCo Playground]]

MuJoCo's native scene format is **MJCF**, not USD. But two pieces of [[google-deepmind|Google DeepMind]]-led infrastructure bridge it to USD:

- **`MjcPhysics`** — USD schema plugin maintained by DeepMind. Authors MuJoCo-specific solver attributes (integrator type, constraint solver algorithm, contact settings) onto USD prims, allowing MuJoCo's solver-specific knowledge to live inside a USD scene. The existence of this plugin is the strongest signal that DeepMind is committed to USD as cross-stack substrate, not just consuming it ([[openusd|OpenUSD entity]], [[newton-openusd-substrate-convergence|substrate-convergence synthesis]]).
- **`mujoco-usd-converter`** — bridge tool living in the `newton-physics` GitHub org. Converts MJCF assets to OpenUSD with `MjcPhysics` schemas. Notable that the cross-stack bridge is hosted in the cross-vendor governance domain, not by either parent vendor.

So MuJoCo doesn't natively read USD, but the plugin + converter make MJCF↔USD round-trip possible — and DeepMind's investment makes USD a first-class citizen of the MuJoCo stack going forward.

## Substrate (not a simulator)

### [[newton-physics-engine|Newton]]

Newton is a physics engine, not a simulator stack — pluggable into both Isaac Lab and MuJoCo Playground ([[mujoco-playground-paper|MuJoCo Playground Paper]] confirms "optionally backends to Newton in 2026"). Its USD relationship:

- **`NewtonSceneAPI`** / **`newton-usd-schemas`** (Apache 2.0, Linux Foundation governed) defines Newton-specific solver parameters (`newton:timeStepsPerSecond`, gravity, solver iterations) on USD prims.
- Designed as a "proving ground" — physically meaningful parameters generalizable across multiple Newton solvers may eventually be **promoted into upstream `UsdPhysics`** ([[openusd|OpenUSD entity]]).
- v0.2.0 released 2026-05-07; 52 commits, 7 releases — actively developed.

Newton's contribution to the USD picture is that the **physics schema layer itself is being co-developed in the open**, not just the scene format.

## Non-USD simulators

### [[genesis|Genesis]]

Custom Python-first physics engine; no USD support documented in ingested sources ([[genesis-project-page|Genesis Project Page]]). Headlines on speed (43M FPS Franka) and integrated photorealistic rendering, but the asset/scene pipeline is its own. The [[newton-openusd-substrate-convergence|substrate-convergence synthesis]] flags Genesis as one of the post-2026 exceptions that has to justify the non-Newton, non-USD choice.

### [[maniskill|ManiSkill]] / [[sapien|SAPIEN]]

GPU-parallel manipulation benchmark out of Hao Su's lab at UCSD, built on the SAPIEN simulation framework ([[maniskill-hab-paper|ManiSkill-HAB Paper]]). No USD support documented. Like Genesis, it's a non-Newton, non-USD silo as of 2026.

### [[gymnasium-robotics|Gymnasium-Robotics]]

The Farama Foundation's [[mujoco|MuJoCo]]-backed env families (Fetch, Shadow Hand, Maze, Adroit, Franka Kitchen, MaMuJoCo). MJCF only; the same MuJoCo USD plugin path applies in principle but is not part of the Gymnasium-Robotics distribution itself ([[gymnasium-robotics-docs|docs]]).

## Roadmap caveats

> [!note] URDF / MJCF / SDFormat → OpenUSD mapping is planned but unshipped
> The [[nvidia-openusd-for-robotic-simulation|NVIDIA OpenUSD blog]] (March 2025) lists conceptual mapping from URDF / MJCF / SDFormat to USD as **planned roadmap work, not yet shipped**. As of 2026-05 the wiki has not ingested confirmation that the mapping has fully landed. The [[source-robotics-urdf-mjcf-usd-comparison|practitioner survey]] still treats URDF, MJCF, and USD as stratifying by use case rather than collapsing into one.

> [!note] Joint / kinematic survival through CAD→USD is the open question
> CAD-to-USD pipelines ([[nvidia-cad-to-usd-jt-workflows|NVIDIA JT workflows]]) preserve geometry, hierarchy, and metadata well, but no ingested source documents automated SolidWorks-mate-to-`PhysicsJoint` conversion. Joint topology is presumably re-authored inside USD/Isaac Sim after geometry import.

## Sources used in this synthesis

- [[nvidia-openusd-for-robotic-simulation|Using OpenUSD for Modular and Scalable Robotic Simulation]]
- [[openusd-rigid-body-physics-proposal|OpenUSD Rigid Body Physics Proposal]]
- [[nvidia-newton-physics-engine-developer-page|NVIDIA Newton Physics Engine Developer Page]]
- [[mujoco-playground-paper|MuJoCo Playground Paper]]
- [[agibot-genie-sim-3-announcement|AGIBOT Genie Sim 3.0 Announcement]]
- [[genesis-project-page|Genesis Project Page]]
- [[maniskill-hab-paper|ManiSkill-HAB Paper]]
- [[gymnasium-robotics-docs|Gymnasium-Robotics Documentation]]
- [[source-robotics-urdf-mjcf-usd-comparison|Robot Simulation File Formats — URDF vs MJCF vs USD]]
- [[nvidia-cad-to-usd-jt-workflows|Building CAD-to-USD Workflows with NVIDIA Omniverse]]

## Related

- [[openusd|OpenUSD]] — entity page covering the format, UsdPhysics schema, and per-solver extensions.
- [[newton-openusd-substrate-convergence|Newton + OpenUSD — the substrate convergence]] — structural argument for why this convergence matters.
- [[simulators-for-agentic-robotics-2026|Simulators for agentic robotics — 2026 landscape]] — broader simulator survey.
- [[why-jepa-research-skips-the-simulator-stack|Why JEPA research skips the simulator stack]] — companion synthesis filed at the same time.

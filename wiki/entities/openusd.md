---
title: OpenUSD
type: entity
subtype: format
created: 2026-05-07
updated: 2026-05-09
sources: 5
tags: [openusd, scene-description, usdphysics, pixar, format, robotics]
---

**OpenUSD (Universal Scene Description)** — Pixar-originated, now multi-vendor open standard for describing 3D scenes. In robotics, it has become the **shared scene format and physics-schema layer** across the major simulation stacks ([NVIDIA Isaac Sim](nvidia-isaac-sim.md) / [Isaac Lab](nvidia-isaac-lab.md), [MuJoCo Playground](mujoco-playground.md) via the MjcPhysics plugin, the [Newton](newton-physics-engine.md) ecosystem). See [Newton + OpenUSD — the substrate convergence](../syntheses/newton-openusd-substrate-convergence.md) for the structural argument; this page is the entity reference.

## Why it matters in robotics

OpenUSD is not just a 3D file format — it is a **scene-graph composition system with formal physics schemas**. In 2026 it functions as:
1. A **multi-asset scene description** that scales beyond what URDF or MJCF can represent (large environments, multiple robots, layered authoring).
2. A **robotics-physics schema layer** (UsdPhysics) with explicit support for articulated robots, joint drives, and reduced-coordinate simulation.
3. The **interchange format** between CAD/PLM upstream tools and robotics simulators downstream.

## UsdPhysics — the robotics physics schema

The `UsdPhysics` schema family (Apple + NVIDIA + Pixar, v1.0 in 2020) extends OpenUSD with rigid-body physics constructs. Key components for robotics ([OpenUSD Rigid Body Physics Proposal](../sources/openusd-rigid-body-physics-proposal.md)):

- **`PhysicsRigidBodyAPI`** — physics-driven body marker.
- **`PhysicsArticulationRootAPI`** — root of an articulated robot, hints reduced-coordinate simulation. Schema explicitly distinguishes **floating articulations** (mobile / aerial robots) from **fixed articulations** (industrial arms bolted to the floor) — robotics jargon recognized in the standard.
- **Joint subtypes**: `PhysicsRevoluteJoint`, `PhysicsPrismaticJoint`, `PhysicsFixedJoint`, `PhysicsSphericalJoint`, `PhysicsDistanceJoint`.
- **Joint drives** (motor models): `stiffness * (targetPosition - p) + damping * (targetVelocity - v)`. Multi-apply per DOF.
- **Mass / inertia / collision** APIs for full inertial properties.
- **Units**: degrees for angles, `metersPerUnit` and `kilogramsPerUnit` metadata for SI consistency.

**Limitations:** no nested rigid bodies, no scaling during simulation, sleep/deactivation state implementation-specific.

## Solver-specific extensions

UsdPhysics is the baseline; individual physics engines add solver-specific schemas as USD plugins:

- **`MjcPhysics`** — USD schema plugin **maintained by [Google DeepMind](google-deepmind.md)**. Authors MuJoCo-specific solver attributes (integrator type, constraint solver algorithm, tolerance, contact settings) onto USD prims. The existence of this plugin is the most concrete evidence that DeepMind is committed to USD as a cross-stack substrate, not just consuming it.
- **`NewtonSceneAPI` / newton-usd-schemas** — Apache 2.0, Linux Foundation governance. Defines Newton-specific solver parameters (`newton:timeStepsPerSecond`, gravity, solver iterations). Designed as a "proving ground" — physically meaningful parameters tested in Newton schemas may eventually be promoted into UsdPhysics itself. Active: v0.2.0 released 2026-05-07; 52 commits, 7 releases.
- **`mujoco-usd-converter`** — bridge tool living in the `newton-physics` GitHub org. Converts MuJoCo MJCF assets to OpenUSD with `MjcPhysics` schemas.

## CAD ingestion

OpenUSD is the target format for CAD-to-simulation pipelines:

- **NVIDIA Omniverse Connector ecosystem** ships native connectors for SolidWorks, CATIA, AutoCAD, Creo. Marketed as eliminating manual URDF authoring for environments and robot bodies.
- **`omni.kit.converter.jt_core`** + **OpenUSD Exchange SDK** — concrete pipeline for Jupiter Tessellation (JT, ISO 14306) → USD ([NVIDIA CAD-to-USD JT Workflows](../sources/nvidia-cad-to-usd-jt-workflows.md)). Preserves assembly hierarchy and metadata one-to-one; collapses materials to `displayColor` / `UsdPreviewSurface`; requires `omni.scene.optimizer` to make geometry usable in real-time sim (82% vertex reduction in the example).
- **Okino PolyTrans|CAD+DCC** — third-party converter for SolidWorks (`.sldasm`/`.sldprt`) → USD via STEP AP204 / IGES BREP intermediates.

> [!warning] Joint / kinematic survival through CAD→USD is the open question
> Sources cover geometry, hierarchy, and metadata preservation well. None explicitly addresses how SolidWorks mates → `PhysicsJoint` types is automated. The implication is that for robot-arm import, joint topology is **re-authored** inside USD/Isaac Sim after geometry import, despite Omniverse marketing claims.

## Hydra pipeline

The **Hydra** subsystem is OpenUSD's generalized scene graph processor. It decouples scene data from the rendering backend via **render delegates** — pluggable runtime interfaces that any renderer (rasterizer, path-tracer, neural renderer) can implement without coupling to a specific data layout ([NVIDIA OpenUSD Developer Video Series](../sources/nvidia-openusd-developer-video-series.md)). This is what allows Isaac Sim to switch between RTX path-tracing and rasterized rendering against the same USD scene, and what would allow a neural world-model renderer to consume USD scenes directly.

## Versions and tooling
- **OpenUSD Core Specification 1.0** establishes baseline standards for SimReady assets.
- **Isaac Sim 5.0** runs on Omniverse Kit SDK 107 → OpenUSD **24.05** ([NVIDIA OpenUSD-for-robotic-simulation blog](../sources/nvidia-openusd-for-robotic-simulation.md)).
- **OpenUSD Exchange SDK** — NVIDIA-maintained framework for writing USD converters.

## Roadmap (NVIDIA-acknowledged, March 2025)
- **URDF / MJCF / SDFormat → OpenUSD** conceptual mapping work — *planned*, not yet shipped.
- **Deformable body dynamics** schemas for robot manipulators.
- **B-rep geometry schemas** for CAD-derived assets (replacing tessellation with parametric surfaces).

## Trade-offs vs URDF and MJCF

See [URDF vs MJCF vs USD comparison](../sources/source-robotics-urdf-mjcf-usd-comparison.md) for the practitioner survey. Short version:
- **URDF**: ROS-native, simple, kinematic-only, no closed chains. Stays dominant for ROS/motion-planning workflows.
- **MJCF**: precise physics, RL-ready, MuJoCo-coupled. Stays dominant for MuJoCo/RL.
- **USD**: scales, layers, integrates rendering+physics+assets, steeper learning curve. Wins for large environments + Omniverse-modern simulators.

The three are **not converging** at the description-format level; they stratify by use case. What converges is the **physics schema** (`UsdPhysics` + per-solver extensions) underneath USD scenes.

## Related
- [Newton physics engine](newton-physics-engine.md) — primary 2026 physics consumer of UsdPhysics.
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md) / [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — flagship USD-native robotics stack.
- [MuJoCo Playground](mujoco-playground.md) — MJX-based stack with MjcPhysics USD plugin support.
- [Newton + OpenUSD — the substrate convergence](../syntheses/newton-openusd-substrate-convergence.md) — the synthesis on what this convergence means.

## Mentioned in
- [New Video Series: What Developers Need to Know About OpenUSD](../sources/nvidia-openusd-developer-video-series.md)
- [OpenUSD Rigid Body Physics Proposal](../sources/openusd-rigid-body-physics-proposal.md)
- [Using OpenUSD for Modular and Scalable Robotic Simulation](../sources/nvidia-openusd-for-robotic-simulation.md)
- [Robot Simulation File Formats — URDF vs MJCF vs USD](../sources/source-robotics-urdf-mjcf-usd-comparison.md)
- [Building CAD-to-USD Workflows with NVIDIA Omniverse](../sources/nvidia-cad-to-usd-jt-workflows.md)

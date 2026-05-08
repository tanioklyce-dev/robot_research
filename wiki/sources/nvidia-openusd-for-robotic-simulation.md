---
title: Using OpenUSD for Modular and Scalable Robotic Simulation (NVIDIA)
type: source
url: https://developer.nvidia.com/blog/using-openusd-for-modular-and-scalable-robotic-simulation-and-development/
author: Aaron Luk, Pomi Lee, Renato Gasoto
affiliations: NVIDIA
published: 2025-03-18
ingested: 2026-05-07
tags: [openusd, nvidia, isaac-sim, robotics, scene-composition, cad, urdf]
---

## Summary
NVIDIA Technical Blog on how OpenUSD is used as the asset and scene format underlying robotic simulation in [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) and adjacent [Newton](../entities/newton-physics-engine.md) workflows. Articulates NVIDIA's own roadmap for robotics-specific OpenUSD schemas and the URDF/MJCF/SDFormat conceptual mapping work.

## Key claims

### Stack positioning
- **Isaac Sim 5.0** builds on Omniverse Kit SDK 107, upgrading to **OpenUSD version 24.05**.
- **[Newton](../entities/newton-physics-engine.md)** — referenced as "open-source, extensible physics engine developed by NVIDIA, Google DeepMind, and Disney Research." Same framing as the [developer page](nvidia-newton-physics-engine-developer-page.md).

### OpenUSD composition features used in robotics pipelines
- **References** — keep links to upstream CAD data sources, enabling roundtrip.
- **Variant sets** — single interface layer for asset configuration (e.g. selecting between robot variants, end-effectors, sensor packages).
- **Payloads** — modular composition of simulation features per component.

### Robotics-specific schemas (NVIDIA's framing)
Robot schemas containing:
- Kinematic attributes.
- Robot semantics (purpose, capabilities).
- Bodies hierarchy.
- Configuration parameters.

### URDF / MJCF / SDFormat → OpenUSD mapping
- Direct import via "Omniverse CAD converter or open-source file format plug-ins" exists today.
- **Planned mapping efforts** (i.e. roadmap items as of 2025-03): URDF, MJCF, and SDFormat to OpenUSD conceptual data models. As of this article, official conceptual mapping is **not yet shipped**.

### Roadmap items
- **Deformable body dynamics** for robot manipulators.
- **B-rep geometry schemas** for CAD-derived tessellations.

### Synthetic data pipeline
- "Enables scalable synthetic-data generation" by transforming structured simulation into photoreal video using **Cosmos** world foundation models ([NVIDIA Cosmos](../entities/nvidia-cosmos.md)).

### Practical guidance
- Standardize root-layer scene units: **`metersPerUnit` set to meters**.

## Entities mentioned
- [OpenUSD](../entities/openusd.md)
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md)
- [Newton physics engine](../entities/newton-physics-engine.md)
- [NVIDIA Cosmos](../entities/nvidia-cosmos.md)
- [Google DeepMind](../entities/google-deepmind.md) (as Newton co-developer)
- [Disney Research](../entities/disney-research.md) (as Newton co-developer)
- [NVIDIA](../entities/nvidia.md)

## Concepts touched
- Scene composition in robotics pipelines (references, variants, payloads).
- Conceptual mapping URDF/MJCF/SDFormat → USD (open work).
- Synthetic-data generation via Cosmos.

## Open questions
- How far has the URDF→USD conceptual mapping progressed since March 2025? The article presents it as planned work, not shipped.
- Does the deformable-body roadmap connect to specific manipulators or remain abstract?
- B-rep schemas would meaningfully improve CAD fidelity in USD; status unclear.

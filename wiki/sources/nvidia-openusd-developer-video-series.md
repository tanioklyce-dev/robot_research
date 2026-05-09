---
title: "New Video Series: What Developers Need to Know About Universal Scene Description"
type: source
url: https://developer.nvidia.com/blog/new-video-series-what-developers-need-to-know-about-universal-scene-description/
author: Aaron Luk
affiliations: NVIDIA
published: 2024-04-11
ingested: 2026-05-09
tags: [openusd, nvidia, hydra, composition, schemas, developer]
---

## Summary
NVIDIA Technical Blog post announcing a video series introducing OpenUSD to developers. Frames OpenUSD as "an open and extensible framework for creating, editing, querying, rendering, collaborating, and simulating within 3D worlds" and walks through its four core architectural features. Earliest NVIDIA-authored OpenUSD source in the wiki (April 2024, predating the March 2025 robotic-simulation blog by nearly a year).

## Key claims

- OpenUSD is more than a file format — an ecosystem for modeling and combining diverse data sources. Pixar invented it; NVIDIA, Apple, and others have extended it.
- Adoption sectors explicitly named: manufacturing, robotics, retail, architecture.

### Four developer-facing features
1. **Composition and Layering** — sparse, nondestructive assembly of data from multiple sources as individual layers. Enables collaborative editing while preserving all data.
2. **Custom Schemas** — extensible beyond geometry/shading. NVIDIA + Pixar + Apple collaborated to add **physics schemas for rigid bodies** (the `UsdPhysics` family).
3. **Data Source Interoperability** — storage is filesystem-agnostic; supports procedural generation via plug-in systems, asset resolvers, and import of formats like Alembic and OBJ.
4. **Hydra Pipeline** — generalized scene graph processor with pluggable render delegates. Decouples scene data from rendering backend; allows multiple renderers (rasterizer, path-tracer, neural renderer) to consume the same USD scene without data-format coupling.

- NVIDIA Omniverse provides developer tooling for integrating USD into existing workflows and generative AI applications.

## Entities mentioned
- [OpenUSD](../entities/openusd.md)
- [NVIDIA](../entities/nvidia.md)
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) (implicit — Omniverse context)

## Concepts touched
- Composition and layering in OpenUSD
- Custom schemas / UsdPhysics
- Hydra render-delegate pipeline
- Cross-sector USD adoption

## Open questions
- The video series itself is not transcribed here; individual episodes may contain deeper technical content worth a separate ingest.
- No explicit robotics-specific guidance in this post — that came later in the [March 2025 blog](nvidia-openusd-for-robotic-simulation.md).

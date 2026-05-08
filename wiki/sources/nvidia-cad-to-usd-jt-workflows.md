---
title: Building CAD-to-USD Workflows with NVIDIA Omniverse (JT pipeline)
type: source
url: https://developer.nvidia.com/blog/building-cad-to-usd-workflows-with-nvidia-omniverse/
author: Justine Lin
affiliations: NVIDIA
published: 2025-07-29
ingested: 2026-05-07
tags: [openusd, cad, jt, omniverse, conversion, robotics, optimization]
---

## Summary
NVIDIA Technical Blog walking through a concrete CAD-to-USD pipeline using **Jupiter Tessellation (JT)** as the input format. Establishes the asset-side counterpart to the [OpenUSD-for-robotic-simulation blog](nvidia-openusd-for-robotic-simulation.md): how factory / robot / environment geometry actually gets into a USD scene from upstream CAD systems.

## Key claims

### Conversion stack
- **`omni.kit.converter.jt_core`** — Kit extension that ingests JT.
- **`omni.services.convert.cad`** — service-layer converter.
- Both built on **NVIDIA's OpenUSD Exchange SDK**, the underlying framework for CAD converters.
- **`omni.scene.optimizer`** — post-import optimization (mesh decimation, hidden-mesh removal, payload/reference restructuring).

### Input format coverage in the blog
- Focused specifically on **JT (Jupiter Tessellation)**, ISO 14306 — a vendor-neutral 3D visualization standard.
- Other CAD formats (SolidWorks, CATIA, NX) are **not** discussed in this article; covered separately by Omniverse Connector ecosystem.

### What is preserved
- **Assembly hierarchy and tree structure** maintained one-to-one with USD prims.
- **Component naming** (with `tn_` prefixes and identifier suffixes for namespace clarity).
- **Part metadata** from CAD source.
- One-to-one CAD-component → USD-prim mapping.

### What is degraded
- **Materials** collapse to basic `displayColor` or `UsdPreviewSurface` — not photorealistic.
- **Geometry density** is initially very high (millions of polygons); requires `omni.scene.optimizer` to be useful for real-time simulation.
- The article reports **82% vertex reduction** in the example via decimation.

### What is NOT addressed
> [!warning] Joint / kinematic survival not covered
> The article focuses entirely on **visual + structural** conversion. It does not discuss whether CAD mates, kinematic constraints, or motion definitions transfer to USD — a critical gap for robotics workflows where the CAD model includes a robot arm with mate-defined joints. The example uses a Nova Carter robot but treats only its visual aspects.

### Concrete example
- Workflow: JT export → CLI conversion → optimization (vertex decimation 82%, hidden-mesh removal, payload/reference restructuring) → material assignment.

## Entities mentioned
- [OpenUSD](../entities/openusd.md)
- [NVIDIA](../entities/nvidia.md) (Omniverse, Kit, Exchange SDK)
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) (implicit downstream consumer)

## Concepts touched
- CAD-to-simulation pipelines.
- Geometry decimation / scene optimization.
- USD payloads and references for performance.

## Open questions
- Does the OpenUSD Exchange SDK support automatic mapping of CAD mates → `PhysicsJoint` types? The article doesn't claim it does.
- What is the SolidWorks / CATIA / NX coverage in the broader Omniverse Connector catalog? Mentioned by the search index but not by this specific article — needs follow-up source.
- For robotics specifically, is the recommended pipeline CAD → USD geometry, then **re-author joints inside USD/Isaac Sim**? Implicit but not stated.

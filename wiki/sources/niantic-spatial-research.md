---
title: Niantic Spatial — research page, product line, and Scaniverse
type: source
url: https://www.nianticspatial.com/research
author: Niantic Spatial, Inc.
published: 2026 (site current at read; publications span 2022–2026)
ingested: 2026-08-13
tags: [niantic-spatial, scaniverse, gaussian-splatting, visual-relocalization, scene-coordinate-regression, digital-twin, large-geospatial-model, spz, 3d-reconstruction, physical-ai, primary-source]
---

## Summary

**Niantic Spatial, Inc.** — the spatial-computing company carved out of Niantic (of Pokémon Go), now positioning itself as *"the infrastructure layer for physical AI. Starting with the City of Rancho Cordova."* Four products — **Reconstruct, Localize, Understand, Capture** — over a foundation it calls the **Large Geospatial Model (LGM)**, with **Robotics** listed first among its target industries (ahead of Defense and Intelligence, and Oil and Gas).

Ingested alongside [LingBot-Map](lingbot-map-github.md) because the pair exposes a **structural gap in this wiki**: it covers world models extensively — [generative-video](../concepts/world-models/world-model-simulators.md) and [JEPA](../concepts/world-models/jepa.md) — and has **no page for SLAM, Gaussian splatting, NeRF, or visual relocalization**. Those are a different tradition attacking an adjacent problem: *geometric* reconstruction of a real place rather than *learned prediction* of what happens next. See the new [visual relocalization and mapping](../concepts/robotics/visual-relocalization-and-mapping.md) concept page.

> [!note] Provenance
> `scaniverse.nianticspatial.com` serves only an authentication form; the Scaniverse product detail below is from the **Capture** page on `nianticspatial.com` (fetched, and confirmed against the page text supplied by the user 2026-08-13). It is **vendor marketing copy, not documentation** — no specifications, accuracy figures, or benchmarks appear anywhere on it.

## Key claims — the product stack

| Product | What it does |
|---|---|
| **Capture** | *"Collecting high-resolution 3D data — the foundation of Niantic Spatial's Large Geospatial Model."* Scaniverse, on-demand capture service, and BYOD integrations |
| **Reconstruct** | Geo-referenced 3D digital twins, *"running seamlessly from edge devices to the cloud"* |
| **Localize** | *"Precise, vision-based positioning for machines"* |
| **Understand** | *"Query the world through semantics at every 3D point"* |

**Reconstruct's pipeline** is stated in three stages: **Scan Processing** (clean/filter/normalize raw sensor input from *"drones, robots, and handheld systems"*) → **Registration** (*"centimeter-level spatial accuracy"* from multi-pass merges) → **Geo-Referencing** (*"anchor models to real-world coordinate systems for interoperability with GIS, simulation, and autonomy platforms"*).

Two reconstruction modes: **on-device** (iOS/Android, *"textured meshes or Gaussian splats in real time, fully offline"*) and **cloud** (photorealistic meshes and splats *"enhanced by semantic understanding"*).

**Scaniverse** — *"evolved from a market-leading mobile 3D scanning app into a scalable spatial data ingestion service, enabling everyone from creators to field teams to capture and operationalize real-world environments with precision and at scale."* Five stated capabilities:

| Capability | Claim |
|---|---|
| **Export / integrate** | standard 3D formats **including the open-source SPZ format, "reducing file size by 90%"** |
| **High-fidelity scanning** | iOS and Android *"today"*, plus **360° cameras and drones**; ***"no expensive equipment or specialized training required"*** |
| **Photorealistic results** | **Gaussian splats and meshes processed efficiently on-device** |
| **Built for Niantic Spatial pipelines** | *"connect directly with Niantic Spatial's reconstruction and localization workflows"* |
| **Collaborative tools** | team-based scanning and data management |

Paid product (*"View Plans and Pricing"*); **enterprise features on web, iOS, and Android**. Showcase scan: **Greenwich Power Station**. Capture as a whole is framed as *"turning real-world data into the foundation for spatial intelligence."*

## Key claims — the research program

The publication list is a coherent decade-long line in **visual relocalization and scene-coordinate regression**, and the author list is that subfield's centre of gravity: **Eric Brachmann**, **Victor Adrian Prisacariu** (Oxford Active Vision), **Gabriel Brostow** (UCL), **Michael Firman**, **Clément Godard** (monodepth), **Daniyar Turmukhambetov**, **Tommaso Cavallari**, **Jamie Watson**, **Mohamed Sayed**, **Sara Vicente**, **Guillermo Garcia-Hernando**.

The relocalization arc, in order:

| Year | Work | Contribution |
|---|---|---|
| CVPR 2023 | **ACE** — *Accelerated Coordinate Encoding* | *"Learning to relocalize in minutes using RGB and poses"* |
| ECCV 2024 | **Scene Coordinate Reconstruction** | posing image collections via incremental learning of a relocalizer |
| ICCV 2025 | **ACE-G** | improving generalization via query pre-training |
| ICCV 2025 | **Scene Coordinate Reconstruction Priors** | |
| ICLR 2026 | **A Scene is Worth a Thousand Features** | feed-forward camera localization from a collection of image features |
| CVPR/ECCV 2026 | **Cross-View Splatter** | feed-forward view synthesis with georeferenced images |

Adjacent lines: **SimpleRecon** (*"3D reconstruction without 3D convolutions"*, ECCV 2022), **DoubleTake** (geometry-guided depth, ECCV 2024), **AirPlanes** (plane estimation, CVPR 2024), **Map-free Visual Relocalization** (metric pose relative to a *single* image, ECCV 2022), **Morpheus** (text-driven Gaussian-splat stylization, CVPR 2025), **PlaceIt3D** (language-guided object placement in real 3D scenes, ICCV 2025), and a substantial accessibility/AR-authoring strand at CHI and UIST including **NaviNote** (in-situ spatial annotation for blind and low-vision people).

## Analysis

> [!note] The direction of travel is optimization → feed-forward, and it mirrors the wiki's other threads
> ACE (2023) *trains a small network per scene, in minutes*. By ICLR 2026, *"A Scene is Worth a Thousand Features"* and *"Cross-View Splatter"* are **feed-forward** — no per-scene optimization at all. That is the same arc [LingBot-Map](lingbot-map-github.md) sits at the end of, arriving independently from robotics rather than AR.
>
> It also rhymes with a pattern this wiki keeps recording elsewhere: **per-instance optimization gives way to an amortized model once enough data exists.** Compare the [world-model](../concepts/world-models/world-model.md) line's move from planning-in-a-learned-model toward direct policies, and [RoboTwin 2.0](robotwin2-paper.md)'s replacement of hand-written task programs with an MLLM that writes them.

> [!warning] "Robotics" is listed first, and there is no robotics evidence on the page
> The industries list leads with Robotics, and Reconstruct's copy names *"drones, robots, and handheld systems"* and interoperability with *"simulation, and autonomy platforms."* **No robotics deployment, benchmark, or customer is shown** — the concrete anchor offered anywhere is a **city government** (Rancho Cordova), which is a GIS/digital-twin use case, not an autonomy one.
>
> That gap matters for how this wiki should file it: **Niantic Spatial is currently a mapping-infrastructure company courting robotics, not a robotics company.** The capability (centimetre-accurate geo-referenced splats, vision-based localization) is genuinely what a mobile robot needs; whether anything robotic runs on it is unestablished here.

> [!note] The data-flywheel asymmetry is the real asset
> Niantic's original business put millions of players outdoors scanning real places. Scaniverse converts that consumer capture surface into *"a scalable spatial data ingestion service."* Nobody else in this wiki's coverage has a comparable **crowd-sourced geometric** capture channel — the closest analogues are [LeRobot](../entities/lerobot.md)'s community datasets and [SmolVLA](../entities/smolvla.md)'s 481 community HF datasets, which are *manipulation* data at hobbyist scale, not city-scale geometry.
>
> **SPZ** — an open format claiming 90% size reduction for Gaussian splats — is the kind of move that only pays off if you expect to move a very large amount of splat data.

> [!note] The capture layer is deliberately deskilled *and* deliberately coupled — that pairing is the strategy
> Two of Scaniverse's five stated capabilities sit next to each other and should be read together: ***"no expensive equipment or specialized training required"*** and ***"built for Niantic Spatial pipelines — connect directly with Niantic Spatial's reconstruction and localization workflows."***
>
> **Lower the barrier to capture as far as it will go, then route what comes out into your own stack.** SPZ's 90% reduction is the enabling piece — phone-captured splats are only shippable at volume if they are small. Everything about the Capture product is aimed at maximizing the *volume and diversity* of geometry flowing into the [Large Geospatial Model](../entities/niantic-spatial.md), which is the asset the flywheel note above describes.
>
> **The robotics-relevant version of this claim**, and it is a real one: a fleet operator could map a facility with **phones and drones instead of survey equipment or a dedicated mapping robot**. That is a genuine cost argument. It is still not a robotics deployment, and none is shown.

## Entities mentioned

- [Niantic Spatial](../entities/niantic-spatial.md) — the subject of this source
- [LingBot-Map](../entities/lingbot-map.md) — the independent feed-forward streaming-reconstruction counterpart
- [RTAB-Map](../entities/rtab-map.md) — the classical SLAM stack this class of work competes with

## Concepts touched

- [Visual relocalization and mapping](../concepts/robotics/visual-relocalization-and-mapping.md) — the concept this source opens
- [World models](../concepts/world-models/world-model.md) — the adjacent, and different, tradition
- [Motion planning](../concepts/robotics/motion-planning.md)

## Open questions

- **No robotics evidence.** Which robot, running what, on Niantic Spatial's stack? Nothing on the page answers it.
- **What is the Large Geospatial Model, technically?** Named as the foundation and never described — parameters, architecture, training data, and whether it is a single model or a brand for the pipeline are all unstated.
- **Is SPZ adopted outside Niantic?** An open format is only infrastructure if others write it.
- **No numbers anywhere** — no localization accuracy, no reconstruction benchmark, no latency. The research papers have them; the product pages carry none.
- The **accessibility strand** (NaviNote, *Don't Look Now*) is a genuine research contribution adjacent to this wiki's [assistive robotics](../concepts/robotics/assistive-robotics.md) coverage and entirely uningested.

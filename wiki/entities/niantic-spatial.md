---
title: Niantic Spatial
type: entity
subtype: company
created: 2026-08-13
updated: 2026-08-13
sources: 5
tags: [niantic-spatial, scaniverse, gaussian-splatting, visual-relocalization, digital-twin, large-geospatial-model, spz, physical-ai]
---

**Niantic Spatial, Inc.** — the spatial-computing company carved out of Niantic (Pokémon Go), positioning as *"the infrastructure layer for physical AI. Starting with the City of Rancho Cordova."* Four products over a **Large Geospatial Model (LGM)**: **Capture · Reconstruct · Localize · Understand**. **Robotics** is listed first among target industries. Primary source: [research page + products](../sources/niantic-spatial-research.md).

## Products

| | |
|---|---|
| **Capture** | Scaniverse + on-demand service + BYOD; *"the foundation of the Large Geospatial Model"* |
| **Reconstruct** | Geo-referenced digital twins; Scan Processing → Registration (**centimetre-level**) → Geo-Referencing (GIS / simulation / autonomy interop). On-device (iOS/Android, meshes **or Gaussian splats**, real time, fully offline) or cloud |
| **Localize** | *"Precise, vision-based positioning for machines"* |
| **Understand** | *"Query the world through semantics at every 3D point"* |

**Scaniverse** — from *"market-leading mobile 3D scanning app"* to *"scalable spatial data ingestion service."* iOS/Android plus **360° cameras and drones**, ***"no expensive equipment or specialized training required"***; **Gaussian splats and meshes processed on-device**; **SPZ**, their open splat format, claiming **90% file-size reduction**; team-based collaboration; enterprise tier on web, iOS and Android. A paid product.

> [!note] Deskilled capture, coupled output — read the two together
> *"No expensive equipment or specialized training required"* sits alongside *"built for Niantic Spatial pipelines — connect directly with Niantic Spatial's reconstruction and localization workflows."* **Lower the capture barrier as far as it goes, then route the output into your own stack.** SPZ's 90% reduction is what makes phone-captured splats shippable at volume, and volume is the point: it all feeds the **Large Geospatial Model**.
>
> The robotics-relevant reading is a real cost argument — **map a facility with phones and drones instead of survey gear or a dedicated mapping robot**. Still not a robotics deployment, and none is shown.

## The research program

The publication list is the visual-relocalization subfield's centre of gravity — **Eric Brachmann**, **Victor Adrian Prisacariu**, **Gabriel Brostow**, **Michael Firman**, **Clément Godard**, **Tommaso Cavallari**, **Jamie Watson**, **Mohamed Sayed**, **Sara Vicente**.

**Three eras**, and the first is the one most people know without attributing it here: **self-supervised monocular depth (2017–2021)** — **monodepth** (Godard, Mac Aodha, Brostow, CVPR 2017) and **monodepth2** (ICCV 2019), the field's reference baseline for years — then **visual relocalization (2021–2025)**, then **feed-forward reconstruction (2025–2026)**. Cheap depth from ordinary cameras made map-free relocalization plausible, which made amortized reconstruction the obvious next step.

**ACE** (CVPR 2023, *relocalize in minutes*) → **Scene Coordinate Reconstruction** (ECCV 2024) → **ACE-G** + **SCR Priors** (ICCV 2025) → **A Scene is Worth a Thousand Features** (ICLR 2026) → **Cross-View Splatter** (CVPR/ECCV 2026). Plus SimpleRecon, DoubleTake, AirPlanes, Map-free Visual Relocalization, Morpheus, PlaceIt3D, and a CHI/UIST accessibility strand (**NaviNote** for blind and low-vision navigation).

> [!note] The arc is optimization → feed-forward, arrived at independently from robotics
> ACE trains a small per-scene network *in minutes*; by 2026 the same group is publishing **feed-forward** localization and view synthesis with no per-scene optimization. [LingBot-Map](lingbot-map.md) lands at the same place from the robotics side. This wiki has recorded the same amortization pattern elsewhere — per-instance optimization giving way to a trained model once the data exists.

> [!note] The robotics evidence arrived — [Niantic + Flexion + NVIDIA, Jul 2026](../sources/niantic-flexion-nvidia-sim2real.md)
> A **zero-shot sim2real** result: scan an office with an off-the-shelf **360° camera** → Gaussian-splat twin **plus a collision mesh derived from the same reconstruction** → **USDZ / NuRec into [Isaac Lab](nvidia-isaac-lab.md)** → RGB-only navigation policy trained by massively parallel RL on one GPU → **transfers to a real humanoid in the real office**, holding up to rearranged furniture. Benchmark at n=1,024 with matched poses: **RGB-in-3DGS 97.8% vs depth baseline 93.8%** (easy scene) and **75.0% vs 70.9%** (hard) — both separate (p<0.0001, p=0.037), and it is *"the only RGB setup that matches or exceeds the conventional depth baseline."*
>
> **This narrows rather than overturns the read below.** Niantic supplies the *world*; **Flexion** supplies the policy and deployment; NVIDIA supplies the simulator. Still mapping infrastructure for robotics — now with a named robotics customer instead of none.

> [!warning] Robotics was listed first with no robotics evidence (original read, 2026-08-13 morning)
> The copy names *"drones, robots, and handheld systems"* and interoperability with *"simulation, and autonomy platforms."* **No robotics deployment, benchmark, or customer is shown** — the only concrete anchor is a **city government**, which is a GIS use case. File it as **mapping infrastructure courting robotics**, not a robotics company. The capability is what a mobile robot needs; whether any robot runs on it is unestablished.

> [!note] The asset is the capture flywheel
> Niantic's original business put millions of players outdoors scanning real places, and Scaniverse turns that into an ingestion service. **No one else in this wiki's coverage has a crowd-sourced *geometric* capture channel at city scale** — the nearest analogues ([LeRobot](lerobot.md) community datasets, [SmolVLA](smolvla.md)'s 481 HF datasets) are manipulation data at hobbyist scale. Publishing **SPZ** as an open format only pays off if you expect to move a great deal of splat data.

> [!note] One of their papers belongs to this wiki's measurement thread
> **"On the Limits of Pseudo Ground Truth in Visual Camera Re-Localisation"** (Brachmann, Humenberger, Rother, Sattler, ICCV 2021) argues relocalization benchmarks score against ground truth **produced by an algorithm**, so leaderboards partly measure agreement with the reference method. Structurally the same finding as [LIBERO-PRO](../sources/libero-pro-paper.md), [VP²](../sources/vp2-paper.md), and the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) — **a fourth independent instance of "the instrument is not measuring what the field thinks it measures,"** from a subfield the robotics evaluation literature does not appear to cite.

## The measurement paper worth reading separately

**[On the Limits of Pseudo Ground Truth](../sources/pseudo-ground-truth-paper.md)** (Brachmann, Humenberger, Rother, Sattler, ICCV 2021) — now ingested in full. Changing only the reference algorithm that generated a benchmark's labels moves **Active Search from last to first, +29.8 points**, and inverts the field's belief that scene-coordinate regression beats classical feature matching. Notable that **Brachmann is the scene-coordinate-regression line** and the paper's first casualty is his own camp's claim.

## Related

- [LingBot-Map](lingbot-map.md) — the independent feed-forward streaming-reconstruction counterpart
- [RTAB-Map](rtab-map.md) · [GTSAM](gtsam.md) — the classical stack this class of work competes with
- [Visual relocalization and mapping](../concepts/robotics/visual-relocalization-and-mapping.md)

## Open questions

- **What is the Large Geospatial Model, technically?** Named as the foundation, never described.
- **Which robot runs on this?** No robotics evidence published.
- **Is SPZ adopted outside Niantic?** An open format is only infrastructure if others write it.
- **No numbers on any product page** — no localization accuracy, reconstruction benchmark, or latency.

## Mentioned in

- [Niantic Spatial research page + products](../sources/niantic-spatial-research.md)

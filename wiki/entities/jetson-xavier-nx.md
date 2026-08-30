---
title: NVIDIA Jetson Xavier NX
type: entity
subtype: hardware
created: 2026-08-29
updated: 2026-08-29
sources: 2
tags: [jetson, jetson-xavier-nx, nvidia, volta, edge-ai, onboard-compute, robotics, legacy]
---

**Product page:** [developer.nvidia.com/embedded/jetson-xavier-nx](https://developer.nvidia.com/embedded/jetson-xavier-nx) · **Form factor:** 69.6 × 45 mm, **260-pin SO-DIMM**

**NVIDIA Jetson Xavier NX** — the Volta-generation predecessor of the [Orin NX](jetson-orin-nx.md), in the same physical slot. It is the compute that ran a great deal of the 2020–2023 learned-robotics work, including the onboard policy in this wiki's [egocentric-vision locomotion](../sources/egocentric-vision-locomotion-paper.md) source.

> [!warning] Historical context, not a buying recommendation — and not decision-grade
> **No Xavier NX datasheet is ingested.** Every specification below is `[live-web]` from NVIDIA's developer blog and mirrored datasheet, and **has not been checked against a primary the way the [Orin NX](jetson-orin-nx.md) and [AGX Orin](jetson-agx-orin.md) pages were.** Do not quote these numbers in a build or purchase decision without ingesting the datasheet first — see [primary sources for decision-grade claims](../../CLAUDE.md).
>
> For anything being built now, start at the [Jetson module ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md); this part is two generations behind.

## Specifications `[live-web]`

| | |
|---|---|
| GPU | **384-core Volta** with **48 tensor cores** |
| CPU | **6-core NVIDIA Carmel** ARM v8.2, 64-bit |
| DL accelerators | **2× NVDLA** |
| Memory | **8 GB LPDDR4x** (a 16 GB variant also shipped) |
| Performance | **21 TOPS @ 15 W**, **14 TOPS @ 10 W** |
| Camera | up to **6 simultaneous streams** |
| Form factor | **69.6 × 45 mm, 260-pin SO-DIMM** |

Sources: [NVIDIA developer blog](https://developer.nvidia.com/blog/jetson-xavier-nx-the-worlds-smallest-ai-supercomputer/), mirrored [datasheet](https://openzeka.com/wp-content/uploads/2021/07/jetson-xavier-nx-datasheet-us-nvidia-1294100-r3-web.pdf).

## In this wiki

The [egocentric-vision locomotion](../sources/egocentric-vision-locomotion-paper.md) system runs its policy on a **UPboard plus a Jetson NX** aboard a [Unitree A1](unitree-a1.md), at **50 Hz**, taking 480×848 depth downsampled to **58×87** and passing the compressed embedding over a UDP socket with **10 ± 10 ms** latency that the policy is explicitly trained against.

That is the useful datapoint, and it is about method rather than silicon: **a 2022 vision-driven locomotion policy fit in this envelope** — with depth aggressively downsampled and the vision backbone kept small. Compare the wiki's only measured VLA latency on Orin-class hardware, GR00T N1.6-3B at **173 ms / 5.8 Hz** on [AGX Orin](jetson-agx-orin.md). Two generations of silicon later, the *models* grew faster than the compute did.

## Where it sits

Same **69.6 × 45 mm / 260-pin SO-DIMM** footprint as the [Orin NX](jetson-orin-nx.md), which NVIDIA positions as its successor in that slot.

> [!note] Do not assume drop-in compatibility from the form factor alone
> Matching dimensions and connector do not by themselves establish electrical or carrier compatibility, and this wiki has already been bitten once by reading a vendor table too confidently (see the DLA-count correction on [Orin NX](jetson-orin-nx.md)). Treat "pin compatible" as **unverified here** until a datasheet is ingested.

## Related

- [Jetson Orin NX](jetson-orin-nx.md) — the Ampere-generation successor in the same slot.
- [Jetson module ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md) — the current comparison; begins at Orin.
- [Unitree A1](unitree-a1.md) — the robot it flew on in the ingested source.
- [Egocentric-vision locomotion](../sources/egocentric-vision-locomotion-paper.md) — the source establishing its use.

## Mentioned in

- [Legged Locomotion in Challenging Terrains using Egocentric Vision](../sources/egocentric-vision-locomotion-paper.md) — onboard compute for the deployed policy.

## Open questions / TBD

- **No datasheet ingested** — required before any number here is quotable. This is the same gap the [Orin NX](jetson-orin-nx.md) and [AGX Orin](jetson-agx-orin.md) pages closed with primaries.
- **Which Xavier NX variant** the locomotion paper used (8 GB vs 16 GB) is not stated in the paper.
- **Lifecycle status** — production, NRND, or EOL — is not established here.
- **Pin compatibility with [Orin NX](jetson-orin-nx.md)** is asserted by NVIDIA's marketing but unverified in this wiki.

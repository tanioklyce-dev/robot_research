---
title: Genie 3
type: entity
subtype: model
created: 2026-07-13
updated: 2026-08-08
sources: 3
tags: [world-model, generative-video, google-deepmind, foundation-model, interactive-environments]
---

**Genie 3** — [Google DeepMind](google-deepmind.md)'s general-purpose **generative world model** that "generates photorealistic and interactive 3D environments," described (by Waymo) as DeepMind's most advanced such model ([Waymo World Model blog](../sources/waymo-world-model.md)). It is a foundational **generative-video** [world model](../concepts/world-models/world-model.md): a large pretrained model that produces interactive worlds, intended to be **post-trained into domain-specific instruments**.

> [!note] There is no Genie 3 paper — that's the state of the world, not an ingest gap
> DeepMind has published **no model size, architecture, or training corpus** for Genie 3. The primary material is a blog post (2025-08-05, Jack Parker-Holder & Shlomi Fruchter) and a model page; [WorldRoamBench](worldroambench.md)'s model table independently confirms parameters, chunk size, and inference speed are all undisclosed. What the wiki *does* now have is **third-party measurement**, below.

## Specifications

| | |
|---|---|
| Resolution | **1280×704** ([WorldRoamBench](../sources/worldroambench-paper.md)); "720p" per DeepMind |
| Frame rate | **20 fps** (WorldRoamBench); "20–24 fps" per DeepMind |
| Consistency | "several minutes"; **visual memory reaching back about one minute** |
| Parameters / architecture / training data | **not disclosed** |
| Views | first-person and third-person |
| Access | 2025: "limited research preview." 2026: **Project Genie** via Google Labs |

DeepMind's own stated limitations are candid: limited agent action space ("promptable world events are not necessarily performed by the agent itself"), difficulty "modeling complex interactions between multiple independent agents," no geographic accuracy, legible text "only when provided in the input world description," and "a few minutes of continuous interaction, rather than extended hours."

## Measured performance ([WorldRoamBench](worldroambench.md), 2026)

**First of 10 interactive world models in first-person view (73.81), second of 4 in third-person (57.04)** — benchmarked by a competitor's lab (AMAP CV Lab, Alibaba), which ranked its own Happy Oyster second and first respectively.

| Dimension | Genie 3 | Best in field |
|---|---:|---|
| **Memory** | **73.24** | *Genie 3* — retention 71.63, hallucination 25.07, both best |
| **Physics** | 68.95 | Happy Oyster 72.33 (Genie 3 leads in third-person) |
| Visual | 68.28 | SANA-WM 73.08 |
| **Action following** | **84.78** (strict 75.19) | HY-World 1.5 91.61 (strict 89.82) — **Genie 3 is 7th of 10** |

The shape of that table is the finding: **Genie 3 wins overall by being the only model that remembers, not by being the most obedient or the best-looking.** Four open models follow keystrokes more faithfully; all of them collapse on physics and memory. Persistence — the thing the [HAI brief](../sources/hai-world-model-spatial-intelligence-brief.md) named as *the* test of [spatial intelligence](../concepts/world-models/spatial-intelligence.md) — is where the frontier closed model is actually ahead.

> [!note] Reconciling with the "few minutes of coherence" claim
> The HAI brief says Genie 3 stayed coherent only a few minutes at its 2025 release. WorldRoamBench runs **10–60 second** episodes, so it measures a regime strictly inside that limit — the two aren't in conflict, and the coherence ceiling remains unmeasured by anything in the wiki.

## The coherence ceiling

> Genie 3 "can generate an explorable scene in real time, but at its **2025 release, the world stayed coherent for only a few minutes** before objects began to shift or vanish" ([HAI world-model brief](../sources/hai-world-model-spatial-intelligence-brief.md), p. 7).

A policy brief's characterization rather than a benchmark — treat as order-of-magnitude. It remains **the only claim in the wiki about the regime beyond one minute**, and nothing measures it: WorldRoamBench stops at 60 s, and [Waymo](waymo.md) post-trained this model for AV simulation without publishing coherence numbers.

For comparison, [Genie Envisioner](genie-envisioner.md) / GE-Sim2 claims **minute-scale stable rollouts** in the narrower manipulation domain — same order, much smaller world, and that vendor claim has since been [contradicted by independent measurement](../sources/worldarena-paper.md).

## Known downstream use

- **[Waymo World Model](waymo.md)** — Waymo post-trained Genie 3 for autonomous-driving simulation, adding **camera + lidar** multi-sensor output and driving/scene/language control ([Waymo World Model blog](../sources/waymo-world-model.md)).

## Lineage note

Not to be confused with the several similarly-named "Genie" systems this wiki tracks: DeepMind's **Genie** world-model line (Genie → Genie 3) is distinct from [AGIBOT](agibot.md)'s **[Genie Envisioner](genie-envisioner.md)** and **[Genie Sim](agibot-genie-sim.md)** products, which are unrelated except by name.

## Related

- [World model](../concepts/world-models/world-model.md) — Genie 3 is a generative-video instance.
- [Generative-video vs JEPA world models](../syntheses/world-models/generative-video-vs-jepa-world-models.md).

## Mentioned in

- [WorldRoamBench paper](../sources/worldroambench-paper.md) — the only quantitative record of Genie 3 in this wiki; FPV rank 1.
- [The Waymo World Model blog](../sources/waymo-world-model.md)
- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../sources/hai-world-model-spatial-intelligence-brief.md)

---
title: Genie 3
type: entity
subtype: model
created: 2026-07-13
updated: 2026-07-13
sources: 2
tags: [world-model, generative-video, google-deepmind, foundation-model, interactive-environments]
---

**Genie 3** — [Google DeepMind](google-deepmind.md)'s general-purpose **generative world model** that "generates photorealistic and interactive 3D environments," described (by Waymo) as DeepMind's most advanced such model ([Waymo World Model blog](../sources/waymo-world-model.md)). It is a foundational **generative-video** [world model](../concepts/world-models/world-model.md): a large pretrained model that produces interactive worlds, intended to be **post-trained into domain-specific instruments**.

> [!note] Thin entry — no primary DeepMind source ingested
> Everything here comes from the [Waymo World Model](../sources/waymo-world-model.md) announcement, which uses Genie 3 as a foundation. No Genie-3 parameter count, architecture, training data, or capabilities benchmark is in the wiki yet. Ingesting a primary DeepMind Genie 3 source is a known gap.

## Measured limitation (2025 release)

> Genie 3 "can generate an explorable scene in real time, but at its **2025 release, the world stayed coherent for only a few minutes** before objects began to shift or vanish" ([HAI world-model brief](../sources/hai-world-model-spatial-intelligence-brief.md), p. 7).

The wiki's first quantitative statement about Genie 3, and it comes from a policy brief rather than a technical source — so treat it as an order-of-magnitude claim, not a benchmark. It is the frontier reference point for the [visual plausibility trap](../concepts/world-models/world-model-evaluation.md): a system can be real-time, explorable, and photorealistic while failing the "move an object, leave, return" persistence test that defines [spatial intelligence](../concepts/world-models/spatial-intelligence.md).

For comparison, [Genie Envisioner](genie-envisioner.md) / GE-Sim2 claims **minute-scale stable rollouts** in the narrower manipulation domain — same order, much smaller world.

> [!note] Possibly stale
> The figure describes the 2025 release. No 2026 measurement is in the wiki, and [Waymo](waymo.md) post-trained this model for AV simulation in the interim without publishing coherence numbers.

## Known downstream use

- **[Waymo World Model](waymo.md)** — Waymo post-trained Genie 3 for autonomous-driving simulation, adding **camera + lidar** multi-sensor output and driving/scene/language control ([Waymo World Model blog](../sources/waymo-world-model.md)).

## Lineage note

Not to be confused with the several similarly-named "Genie" systems this wiki tracks: DeepMind's **Genie** world-model line (Genie → Genie 3) is distinct from [AGIBOT](agibot.md)'s **[Genie Envisioner](genie-envisioner.md)** and **[Genie Sim](agibot-genie-sim.md)** products, which are unrelated except by name.

## Related

- [World model](../concepts/world-models/world-model.md) — Genie 3 is a generative-video instance.
- [Generative-video vs JEPA world models](../syntheses/world-models/generative-video-vs-jepa-world-models.md).

## Mentioned in

- [The Waymo World Model blog](../sources/waymo-world-model.md)
- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../sources/hai-world-model-spatial-intelligence-brief.md)

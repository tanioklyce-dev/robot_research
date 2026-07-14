---
title: Genie 3
type: entity
subtype: model
created: 2026-07-13
updated: 2026-07-13
sources: 1
tags: [world-model, generative-video, google-deepmind, foundation-model, interactive-environments]
---

**Genie 3** — [Google DeepMind](google-deepmind.md)'s general-purpose **generative world model** that "generates photorealistic and interactive 3D environments," described (by Waymo) as DeepMind's most advanced such model ([Waymo World Model blog](../sources/waymo-world-model.md)). It is a foundational **generative-video** [world model](../concepts/world-models/world-model.md): a large pretrained model that produces interactive worlds, intended to be **post-trained into domain-specific instruments**.

> [!note] Thin entry — no primary DeepMind source ingested
> Everything here comes from the [Waymo World Model](../sources/waymo-world-model.md) announcement, which uses Genie 3 as a foundation. No Genie-3 parameter count, architecture, training data, or capabilities benchmark is in the wiki yet. Ingesting a primary DeepMind Genie 3 source is a known gap.

## Known downstream use

- **[Waymo World Model](waymo.md)** — Waymo post-trained Genie 3 for autonomous-driving simulation, adding **camera + lidar** multi-sensor output and driving/scene/language control ([Waymo World Model blog](../sources/waymo-world-model.md)).

## Lineage note

Not to be confused with the several similarly-named "Genie" systems this wiki tracks: DeepMind's **Genie** world-model line (Genie → Genie 3) is distinct from [AGIBOT](agibot.md)'s **[Genie Envisioner](genie-envisioner.md)** and **[Genie Sim](agibot-genie-sim.md)** products, which are unrelated except by name.

## Related

- [World model](../concepts/world-models/world-model.md) — Genie 3 is a generative-video instance.
- [Generative-video vs JEPA world models](../syntheses/world-models/generative-video-vs-jepa-world-models.md).

## Mentioned in

- [The Waymo World Model blog](../sources/waymo-world-model.md)

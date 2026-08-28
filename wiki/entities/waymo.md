---
title: Waymo
type: entity
subtype: company
created: 2026-07-13
updated: 2026-07-13
sources: 2
tags: [company, autonomous-driving, self-driving, alphabet, world-model, simulation]
---

**Waymo** — Alphabet's autonomous-driving (self-driving car) company. In this wiki it appears as the author of the **Waymo World Model (WWM)**, a generative world model for driving simulation ([Waymo World Model blog](../sources/waymo-world-model.md)).

## Waymo World Model (WWM)

- A **generative-video-family [world model](../concepts/world-models/world-model.md)** for large-scale, hyper-realistic autonomous-driving **simulation**, built on **[Google DeepMind](google-deepmind.md)'s [Genie 3](genie-3.md)** via specialized driving post-training ([Waymo World Model blog](../sources/waymo-world-model.md)).
- **Multi-sensor output** — generates both **camera and lidar** data matching Waymo's hardware suite (distinguishing it from the RGB-only robotics generative-video models like [Cosmos](nvidia-cosmos.md) / [Genie Envisioner](genie-envisioner.md)).
- **Three control axes:** driving-action (counterfactual "what if"), scene-layout (roads / signals / agents), and language (weather / time-of-day / synthetic scenes).
- Framed as **one of "three key pillars"** of Waymo's demonstrably-safe-AI approach; used for extreme-weather, rare-event, and long-tail-object scenario generation, plus dashcam-to-multimodal-sim conversion.
- **Closed / internal** — not open-source.

## Context

Waymo is the autonomous-driving-domain analog to the manipulation-robotics companies this wiki tracks: like [NVIDIA](nvidia.md) (Cosmos) and [AGIBOT](agibot.md) (Genie Envisioner), it is building a generative world model as a **simulator substitute / augmenter** for training and validating a physical-AI system at scale. WWM is the first concrete downstream application of [Genie 3](genie-3.md) ingested in the wiki.

## Mentioned in

- [The Waymo World Model blog](../sources/waymo-world-model.md)
- [Stanford HAI — AI Index Report 2026](../sources/stanford-hai-ai-index-2026.md) (Waymo cited in AV context)

---
title: mimic robotics
type: entity
subtype: company
created: 2026-09-07
updated: 2026-09-07
sources: 1
tags: [mimic-robotics, dexterous-manipulation, video-action-model, audi, deployment, switzerland, eth-zurich, contact-rich, deformable-objects]
---

# mimic robotics

Robotics company that **builds its own robots** and the full deployment stack around them, with stated expertise in *"robot learning, dexterous manipulation and production deployment."* Partner on **FLUX-mimic** with [Black Forest Labs](black-forest-labs.md), and the party that put it on an **Audi** production line ([FLUX 3 launch](../sources/flux-3-launch.md)).

Its own paper, **mimic-video** ([arXiv 2512.15692](https://arxiv.org/abs/2512.15692), Dec 2025 — affiliations reported as mimic robotics, Microsoft Zurich, ETH Zurich and UC Berkeley), is where the architecture originates: *"Video-Action Models for Generalizable Robot Control Beyond VLAs."* **Not ingested.**

## Why it has a page

Because it is the wiki's most concrete instance of **learned manipulation running in production on contact-rich tasks**. The deployed task list, per BFL:

> kitting parts into structured trays, **inserting electronic control units into tight-fitting fixtures**, assembling components together, and **handling soft, flexible materials like seals and cables that conventional automation has never been able to touch**.

Tight-tolerance insertion is the [contact-rich survey](../sources/safe-learning-contact-rich-survey.md)'s most-studied task class; seals and cables are **deformable-object manipulation**, which that survey calls under-explored. This is not a benchmark result.

> [!warning] And no force or tactile sensing is mentioned
> The described pipeline is camera → video backbone → intermediate features → action decoder → robot. Neither BFL post mentions force/torque sensing, tactile sensing, impedance or compliance. Given that mimic builds **dexterous** hands and its paper is about *dexterous manipulation*, the omission is more likely a gap in the blog posts than in the robots — but the wiki should not assume either way. **Reading mimic-video is the cheapest resolution**, and it bears directly on the [force-is-not-in-the-web-data](../concepts/robotics/contact-rich-manipulation.md) argument.

## What it contributes to FLUX-mimic

The division of labour is stated: BFL supplies the multimodal backbone and training expertise; mimic supplies the robots, the action decoder, and **the latency engineering that makes it deployable**. The system reaches a **101 ms reaction time** through optimizations *"from the action decoder, through cutting inter-process latency between sensors, the model and actuators, to **real-time chunking such that prediction and execution overlap**"* — with the backbone itself under **80 ms on a single RTX 5090**.

The architectural idea it is credited with pioneering (in mimic-video): **decode actions from intermediate features of a pretrained video model** rather than fine-tuning a VLA — reported at up to **10× the sample efficiency** of VLAs, and working *"even with a completely frozen backbone — a setting where previous VLAs fail to succeed."*

## Related

- [Black Forest Labs](black-forest-labs.md) · [FLUX 3](flux-3.md)
- [World-action model](../concepts/world-models/world-action-model.md) — the class; mimic's variant decodes from a *frozen general-purpose* backbone.
- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) · [VLA models](../concepts/learning/vla-models.md)
- [Control-rate ladder](../syntheses/platforms/control-rate-ladder.md) — where the 101 ms sits.

## Mentioned in

- [FLUX 3 and FLUX-mimic launch](../sources/flux-3-launch.md)

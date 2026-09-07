---
title: mimic robotics
type: entity
subtype: company
created: 2026-09-07
updated: 2026-09-07
sources: 2
tags: [mimic-robotics, dexterous-manipulation, video-action-model, audi, deployment, switzerland, eth-zurich, contact-rich, deformable-objects]
---

# mimic robotics

Robotics company that **builds its own robots** and the full deployment stack around them, with stated expertise in *"robot learning, dexterous manipulation and production deployment."* Partner on **FLUX-mimic** with [Black Forest Labs](black-forest-labs.md), and the party that put it on an **Audi** production line ([FLUX 3 launch](../sources/flux-3-launch.md)).

Its own paper, **[mimic-video](../sources/mimic-video-paper.md)** (Dec 2025; mimic robotics, Microsoft Zurich, ETH Zurich, ETH AI Center, UC Berkeley — with **Oier Mees** and **Elvis Nava** co-advising), is where the architecture originates: *"Video-Action Models for Generalizable Robot Control Beyond VLAs."*

## Why it has a page

Because it is the wiki's most concrete instance of **learned manipulation running in production on contact-rich tasks**. The deployed task list, per BFL:

> kitting parts into structured trays, **inserting electronic control units into tight-fitting fixtures**, assembling components together, and **handling soft, flexible materials like seals and cables that conventional automation has never been able to touch**.

Tight-tolerance insertion is the [contact-rich survey](../sources/safe-learning-contact-rich-survey.md)'s most-studied task class; seals and cables are **deformable-object manipulation**, which that survey calls under-explored. This is not a benchmark result.

> [!warning] Resolved, and only halfway: **vision and proprioception, no force, no touch**
> [mimic-video](../sources/mimic-video-paper.md) states the observation formally — `oₜ = [images, language, proprioceptive state]` — and describes the real rig as *"a global workspace view, four wrist cameras, and full proprioception."* **No force/torque sensing, no tactile sensing, no impedance, no compliance appears anywhere in the paper**, on a bimanual platform with **16-DoF dexterous hands**.
>
> **But the paper's real-world tasks are not the Audi tasks.** It evaluates **Package Sorting** (pick, handover, place) and **Tape Stowing** — pick-and-place, *not* [contact-rich](../concepts/robotics/contact-rich-manipulation.md) by the survey's definition. The ECU insertion and seal/cable handling appear only in BFL's blog, on a **different backbone**, with **no publication**.
>
> So the published record shows a vision-plus-proprioception system that has **not been published doing a contact-rich task**. "Learned contact-rich manipulation from vision alone" remains a vendor claim with a specific missing document behind it.

## What it contributes to FLUX-mimic

The division of labour is stated: BFL supplies the multimodal backbone and training expertise; mimic supplies the robots, the action decoder, and **the latency engineering that makes it deployable**. The system reaches a **101 ms reaction time** through optimizations *"from the action decoder, through cutting inter-process latency between sensors, the model and actuators, to **real-time chunking such that prediction and execution overlap**"* — with the backbone itself under **80 ms on a single RTX 5090**.

The architectural idea it originated ([mimic-video](../sources/mimic-video-paper.md)): **decode actions from *intermediate* features of a frozen pretrained video model**, via partial denoising, so no video is ever generated at inference. Measured against an architecturally matched π₀.₅-style VLA on equivalent data: the decoder reaches the VLM-conditioned decoder's **maximum success on 10% of the data**, and still scores **77% at one episode per task (a 98% reduction)**. Real-world bimanual, from a **single workspace camera**, it beats a DiT-Block Policy that has **four wrist cameras** (72.0 vs 42.6 packing; 93.0 vs 74.1 handover).

## Related

- [Black Forest Labs](black-forest-labs.md) · [FLUX 3](flux-3.md)
- [World-action model](../concepts/world-models/world-action-model.md) — the class; mimic's variant decodes from a *frozen general-purpose* backbone.
- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) · [VLA models](../concepts/learning/vla-models.md)
- [Control-rate ladder](../syntheses/platforms/control-rate-ladder.md) — where the 101 ms sits.
- [NVIDIA Cosmos](nvidia-cosmos.md) — **Cosmos-Predict2** is mimic-video's backbone; FLUX 3 replaced it in the successor.

## Mentioned in

- [mimic-video paper](../sources/mimic-video-paper.md) — the architecture, the numbers, and the sensing answer.
- [FLUX 3 and FLUX-mimic launch](../sources/flux-3-launch.md)

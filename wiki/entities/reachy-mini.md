---
title: Reachy Mini
type: entity
subtype: robot
created: 2026-08-27
updated: 2026-08-27
sources: 2
tags: [reachy-mini, pollen-robotics, hugging-face, desktop-robot, hri, conversational-ai, open-source]
---

**Reachy Mini** — a small desktop robot from [Pollen Robotics](pollen-robotics.md) / [Hugging Face](hugging-face.md), built for **human-robot interaction**: it sees, listens, speaks, and uses head and body motion to communicate. Pollen's **first consumer robot**; **more than 10,000 shipped** in roughly a year ([Microduck launch post, 2026-08-27](../sources/pollen-robotics-microduck.md)).

> [!note] Thin page
> This entity was created as a citation target during the [Microduck](microduck.md) ingest. Reachy Mini's own product page, docs and SDK have not been ingested — the specs below are what Pollen said about it *while announcing a different robot*. Worth a dedicated ingest.

## What it is for

Voice is its primary medium, which Pollen positions as making it *"an excellent platform for developing conversational AI, experimenting with vision models, and building expressive human-robot interactions."*

The launch of [Microduck](microduck.md) sharpened the split across Pollen's consumer line:

| | Reachy Mini | [Microduck](microduck.md) |
|---|---|---|
| Premise | AI that **interacts** | AI that **acts** |
| Stays on the desk | yes | no |
| Primary medium | speech | movement |
| Expression | words | non-verbal creature sounds, per-robot voice |
| Development target | conversational AI, VLMs, HRI | RL, sim-to-real, locomotion |
| Units shipped | 10,000+ (as of Aug 2026) | pre-orders opened 2026-08-27 |

Both share the stated philosophy: *"both should be fun when you first turn them on, approachable when you start coding, and powerful enough to become serious development platforms as your projects grow."*

## Software

Apache-2.0; SDK at [`pollen-robotics/reachy_mini`](https://github.com/pollen-robotics/reachy_mini); documentation hosted on the Hugging Face Hub at [`huggingface.co/docs/reachy_mini`](https://huggingface.co/docs/reachy_mini/index) — one of the clearer signals that Pollen's products are distributed as **Hugging Face** products, not merely Pollen ones.

## Related

- [Pollen Robotics](pollen-robotics.md) — maker
- [Microduck](microduck.md) — the sibling that leaves the desk
- [Reachy 2](reachy.md) — the research-grade bimanual manipulator
- [Hugging Face](hugging-face.md) — parent

## Mentioned in

- [Microduck — Pollen Robotics launch](../sources/pollen-robotics-microduck.md) — the 10,000+ figure and the interacts-vs-acts framing.
- [Reachy 2 product page](../sources/pollen-robotics-reachy.md) — earlier mention, content not retrievable at that ingest.

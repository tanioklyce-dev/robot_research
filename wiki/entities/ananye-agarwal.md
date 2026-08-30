---
title: Ananye Agarwal
type: entity
subtype: person
created: 2026-08-29
updated: 2026-08-29
sources: 2
tags: [ananye-agarwal, skild-ai, cmu, locomotion, egocentric-vision, parkour, dexterous-manipulation, locoformer]
---

**Ananye Agarwal** — **founding researcher at [Skild AI](skild-ai.md)**; CMU PhD under [Deepak Pathak](deepak-pathak.md). Named to MIT Technology Review's **Innovators Under 35 (Asia Pacific)** `[live-web]` [MIT TR](https://www.innovatorsunder35.com/the-list/ananye-agarwal/).

**He is the strongest through-line author in this wiki's locomotion coverage besides Pathak** — co-first author of the [egocentric-vision paper](../sources/egocentric-vision-locomotion-paper.md) (2022) and co-author of [LocoFormer](../sources/locoformer-paper.md) (2025), which sit at opposite ends of the arc from privileged distillation to long-context generalism.

## In this wiki

- **[Legged Locomotion in Challenging Terrains using Egocentric Vision](../sources/egocentric-vision-locomotion-paper.md)** (CoRL 2022) — **co-first author** with Ashish Kumar. The first end-to-end policy crossing stairs, curbs, stepping stones and gaps from a single depth camera; the paper that answered [RMA](../sources/rma-paper.md)'s stated limitation.
- **[LocoFormer](../sources/locoformer-paper.md)** (CoRL 2025) — co-author with Min Liu and Pathak. One policy across ten unseen robots, learning from its own falls with frozen weights.

The pair is unusual. The 2022 paper's contribution *is* its engineered structure — a two-phase privileged-distillation pipeline with a proved bound. The 2025 paper's contribution is **deleting** that structure in favor of context length and scale. Being an author on both ends of that reversal, three years apart, is a decent proxy for having been right about the trade rather than attached to a method.

## Research line (live-web; not ingested here)

> [!note] `[live-web]` — none of these are ingested sources
> - **Extreme Parkour with Legged Robots** (2023–24, with Pathak) — jumping between platforms and clearing large obstacles on a low-cost quadruped; the direct extension of the egocentric-vision line.
> - **Dexterous Functional Grasping** (CoRL 2023) — the manipulation half of his work, and the bridge toward what [Skild](skild-ai.md) sells.
> - His stated research thesis is that **physical-interaction data scarcity** is the core bottleneck, answered by **large-scale simulation** — training across millions of virtual worlds to accumulate interaction experience that transfers.

That thesis is worth putting beside [S1](../sources/skild-s1-blog.md), which answers the same bottleneck a different way: *"Our model learns by watching human videos."* Simulation and human video are the two live answers to the data problem, and Skild is visibly pursuing both — simulation in the locomotion line, human video in the manipulation line.

## Related

- [Deepak Pathak](deepak-pathak.md) — PhD advisor; co-author on both papers here.
- [Skild AI](skild-ai.md) — founding researcher.
- [LocoFormer](../sources/locoformer-paper.md) and [egocentric-vision locomotion](../sources/egocentric-vision-locomotion-paper.md) — his work in this wiki.
- [Unitree A1](unitree-a1.md) — the platform for the 2022 work.

## Mentioned in

- [Legged Locomotion in Challenging Terrains using Egocentric Vision](../sources/egocentric-vision-locomotion-paper.md) — co-first author.
- [LocoFormer: Generalist Locomotion via Long-context Adaptation](../sources/locoformer-paper.md) — co-author.

## Open questions / TBD

- **Extreme Parkour is uningested** — the missing middle of the CMU locomotion line, between egocentric vision and LocoFormer.
- **Dexterous Functional Grasping is uningested**, and would be the wiki's first source connecting the Skild locomotion people to manipulation.
- **Ashish Kumar** — his co-first author on the 2022 paper and a co-author of [RMA](../sources/rma-paper.md), appearing in two ingested sources with no page.

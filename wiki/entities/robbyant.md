---
title: Robbyant (Ant Group robotics)
type: entity
subtype: company
created: 2026-08-13
updated: 2026-08-13
sources: 1
tags: [robbyant, ant-group, lingbot, physical-ai, foundation-models, open-weights, china]
---

**Robbyant** — the robotics arm of **Ant Group**, publishing the **LingBot** family of physical-AI foundation models. Repos under [github.com/Robbyant](https://github.com/Robbyant); site at `technology.robbyant.com`.

## Why this page exists

**The wiki has been meeting Ant Group's physical-AI program in pieces and filing the pieces as unrelated.** Assembled:

| Artifact | Layer | Where the wiki met it |
|---|---|---|
| **LingBot-VLA** | manipulation policy | [Top 10 Physical AI Models 2026](../sources/top-10-physical-ai-models-2026.md) |
| **LingBot-World** | world model | [WorldRoamBench](../sources/worldroambench-paper.md) — **5th of 10**, 64.25 overall, physics 47.32 |
| **[LingBot-Map](lingbot-map.md)** | geometric reconstruction | [repo](../sources/lingbot-map-github.md), 16,471★, Apache-2.0 |
| **[UME](ume.md)** | teleoperation + data collection | [paper](../sources/ume-paper.md), with Stanford |

That is **policy + world model + map + data-collection hardware**, published openly, from one company. Few organizations in this wiki cover that span — [NVIDIA GEAR](nvidia-gear.md) and [Physical Intelligence](physical-intelligence.md) are the comparison, and neither ships an open exoskeleton.

> [!note] The open-weights posture is consistent across the stack
> LingBot-Map is **Apache-2.0 with weights on both Hugging Face and ModelScope** (the dual publication is a deliberate reach into the Chinese ecosystem). UME publishes a full **bill of materials**. This is not a "weights-only" release pattern — it more closely resembles [Ai2](ai2.md)'s openness than a frontier lab's.

> [!warning] Coverage here is thin and secondhand on two of the four
> LingBot-VLA is known only from a listicle; LingBot-World only from a third-party benchmark where it placed mid-field and **collapsed on physics (47.32)**. Neither primary source is ingested. The company itself — founding, size, relationship to Ant Group formally — is **not established by anything read here**.

## Related

- [LingBot-Map](lingbot-map.md) · [UME](ume.md) — the two artifacts with primary sources
- [NVIDIA GEAR](nvidia-gear.md), [Physical Intelligence](physical-intelligence.md) — comparable full-stack programs
- [Niantic Spatial](niantic-spatial.md) — the other 2026 "map the world for physical AI" play

## Open questions

- **Primary sources for LingBot-VLA and LingBot-World** are both missing, and LingBot-World's benchmark placement makes its primary worth reading.
- **What is Robbyant corporately?** Subsidiary, brand, or research group inside Ant Group — unestablished.
- Does the LingBot stack **compose**? Four layers from one lab is unusual; whether Map feeds World feeds VLA, or they are independent efforts sharing a prefix, is unknown.

## Mentioned in

- [LingBot-Map GitHub repository](../sources/lingbot-map-github.md)
- [UME paper](../sources/ume-paper.md)
- [WorldRoamBench](../sources/worldroambench-paper.md)

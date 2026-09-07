---
title: Generalist AI
type: entity
subtype: company
created: 2026-09-07
updated: 2026-09-07
sources: 1
tags: [generalist-ai, robot-foundation-model, gen-0, gen-1, gen-1-5, in-context-robot-learning, scaling-laws, physical-ai, data-engine]
---

# Generalist AI

Robot-foundation-model company pursuing *"physical AGI"*, building **embodied foundation models pretrained from the ground up on physical interaction data**. The wiki's entry point is the [GEN-1.5 blog post](../sources/generalist-gen-1-5-blog.md) (2026-08-19).

## The GEN lineage

| Model | Date | Claim |
|---|---|---|
| **GEN-0** | ~Nov 2025 | *"Embodied Foundation Models That Scale with Physical Interaction"* — the appearance of **predictable scaling laws** for embodied pretraining |
| **GEN-1** | ~Apr 2026 | *"Scaling Embodied Foundation Models to Mastery"* — post-trained to **99%+** success on simple tasks; first signs of *"improvisational intelligence"* |
| **[GEN-1.5](gen-1-5.md)** | Aug 2026 | **one-shot and few-shot in-context learning of physical skills**, emergent from pretraining |

A steady four-to-five-month cadence, with each release arguing the same thesis one notch further: *"more pretraining makes adaptation faster, cheaper, and more general. We do not yet see where that curve asymptotes."*

## The bet

Two things distinguish the programme from most of the wiki's [VLA](../concepts/learning/vla-models.md) coverage.

**Pretrain on physical experience, not on the internet.** Where a VLA inherits a vision-language backbone and learns dynamics from robot trajectories, and a [video-action model](../concepts/world-models/world-action-model.md) inherits dynamics from internet video, Generalist builds *"a data engine that could fuel the model science with high-quality physical experience at scale"* — **1,891,392 scenes** captured *"in homes, warehouses, factories, and elsewhere."* GEN-1.5's pretraining reportedly contains **no simulation data at all**.

**Specify tasks by demonstration, not by language.** Their argument is that *"many physical actions are difficult to precisely describe in language (e.g. it is far easier to show exactly how to seat two Lego bricks than to say it),"* and that prompting in native observations and actions is *"a more comprehensive test of sensorimotor understanding."* See [in-context robot learning](../concepts/learning/in-context-robot-learning.md).

The commercial argument they draw: the general-purpose robot's promise *"was always conditioned on an expert programming them, which took months of effort and specialized knowledge. If interacting with a robot reduces to simply showing it what to do,"* then both **how fast a robot becomes useful** and **who can work with one** change.

> [!warning] Deliberately opaque, and the wiki should say so
> Across a 3,900-word technical post: **no individual authors** ("Generalist Team"), **no named robot platform**, **no partner, customer or deployment site**, no model size, no compute figure, no code, no weights, no third-party evaluation, and **no rollout counts on any success rate**. GEN-0 and GEN-1 are cited as blog posts, not papers.
>
> That is a legitimate choice for a company, and it means every claim on these pages is a **vendor claim of unknown evidence grade**. Compare [Skild AI](skild-ai.md), which is similarly opaque, and [mimic robotics](mimic-robotics.md), which published.

## Related

- [GEN-1.5](gen-1-5.md) — the model.
- [In-context robot learning](../concepts/learning/in-context-robot-learning.md) — the capability, and the page where Generalist and [Skild](skild-ai.md) **disagree about mechanism**.
- [Skild AI](skild-ai.md) — the other vendor claiming emergent in-context robot learning at scale, by an incompatible route.
- [Scaling laws for VLAs](../concepts/learning/scaling-laws-vla.md) — the literature the GEN-0 → GEN-1.5 arc belongs to.
- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) — handheld-gripper human capture is their prompt medium.

## Mentioned in

- [GEN-1.5 blog post](../sources/generalist-gen-1-5-blog.md)

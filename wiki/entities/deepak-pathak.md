---
title: Deepak Pathak
type: entity
subtype: person
created: 2026-08-29
updated: 2026-08-29
sources: 1
tags: [deepak-pathak, skild-ai, cmu, robot-learning, locomotion, curiosity, self-supervised, locoformer, founder]
---

**Deepak Pathak** — **Raj Reddy Associate Professor** at Carnegie Mellon's School of Computer Science (Robotics Institute; affiliated with the Machine Learning Department), and **co-founder and CEO of [Skild AI](skild-ai.md)**. PhD from UC Berkeley; previously a researcher at Meta AI Research. His stated research aim is *"agents with a human-like ability to generalize in real and diverse environments"* at the intersection of computer vision, machine learning and robotics `[live-web]` [CMU homepage](https://www.cs.cmu.edu/~dpathak/).

He holds the academic appointment **and** the CEO role concurrently — his CMU page lists both.

## In this wiki

Co-author of **[LocoFormer](../sources/locoformer-paper.md)** (CoRL 2025, with Min Liu and Ananye Agarwal), the paper that actually substantiates [Skild AI](skild-ai.md)'s "omni-bodied" claim: one policy trained only on procedurally generated robots, transferring zero-shot to ten commercial platforms at **0.96** against **0.99** for per-robot experts, and — the striking part — **learning from its own falls across trials with frozen weights**.

That result is characteristic of his line of work rather than a departure from it. The through-line from the curiosity work to LocoFormer is **agents that generate their own learning signal**: intrinsic motivation in the 2017 exploration work, and at deployment in LocoFormer, where the signal driving adaptation is the robot's own failed trial.

## Research line (live-web; not yet ingested here)

> [!note] `[live-web]` — none of the following is an ingested source
> - **Curiosity-driven exploration by self-supervised prediction** (ICML 2017) — intrinsic motivation from prediction error; the work that made his name, reported at 4K+ citations.
> - **RMA: Rapid Motor Adaptation for Legged Robots** (Kumar, Fu, Pathak, Malik, 2021) — the direct predecessor LocoFormer positions itself against as *myopic*, adapting over "a few hundred milliseconds." **The single highest-value uningested source for this wiki's locomotion coverage**, and the baseline that makes LocoFormer's long-context argument legible.
> - **Legged locomotion in challenging terrains using egocentric vision** (Agarwal, Kumar, Malik, Pathak, CoRL 2023) — vision-conditioned locomotion; cited in LocoFormer's related work.
> - Further lines listed on his homepage: robot parkour, dexterous manipulation and hand control, **learning from human videos**, and diffusion models for vision.
>
> The "learning from human videos" thread is worth noting: it is the same data thesis [S1](../sources/skild-s1-blog.md) rests on — *"Our model learns by watching human videos. This is a scalable solution for the robotics data problem."*

## Why it matters in this wiki

- **He is the bridge between the wiki's locomotion gap and its foundation-model coverage.** The [awesome-physical-ai gap analysis](../sources/awesome-physical-ai-github.md) flagged the RMA/legged_gym locomotion corpus as missing here; Pathak authored the anchor of that corpus *and* leads the company now claiming a general robot brain.
- **Academic-to-founder without leaving.** Unlike the [TRI](tri.md) → [Walden](walden-robotics.md) spin-out, where the LBM leadership departed, Pathak retains his CMU chair while running a company valued at **>$14B** `[live-web]`. Worth watching as a pattern in this field — see also [Russ Tedrake](russ-tedrake.md), who moved the other way.

## Related

- [Skild AI](skild-ai.md) — co-founder and CEO.
- [Abhinav Gupta](abhinav-gupta.md) — co-founder and president; CMU colleague.
- [LocoFormer](../sources/locoformer-paper.md) — his co-authored paper here.
- [In-context robot learning](../concepts/learning/in-context-robot-learning.md) — the mechanism LocoFormer demonstrates.

## Mentioned in

- [LocoFormer: Generalist Locomotion via Long-context Adaptation](../sources/locoformer-paper.md) — co-author.

## Open questions / TBD

- **RMA is uningested** — the most-cited work in his robotics line and the explicit foil for LocoFormer.
- **The curiosity paper is uningested** — it would anchor an intrinsic-motivation concept page the wiki does not have.
- **Relationship between the LocoFormer recipe and [S1](../sources/skild-s1-blog.md).** LocoFormer conditions on the robot's own experience; S1 conditions on a human demonstration. Whether Skild regards these as one recipe or two is not stated in either source.

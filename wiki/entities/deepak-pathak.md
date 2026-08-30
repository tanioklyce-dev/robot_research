---
title: Deepak Pathak
type: entity
subtype: person
created: 2026-08-29
updated: 2026-08-29
sources: 3
tags: [deepak-pathak, skild-ai, cmu, robot-learning, locomotion, curiosity, self-supervised, locoformer, founder]
---

**Deepak Pathak** — **Raj Reddy Associate Professor** at Carnegie Mellon's School of Computer Science (Robotics Institute; affiliated with the Machine Learning Department), and **co-founder and CEO of [Skild AI](skild-ai.md)**. PhD from UC Berkeley; previously a researcher at Meta AI Research. His stated research aim is *"agents with a human-like ability to generalize in real and diverse environments"* at the intersection of computer vision, machine learning and robotics `[live-web]` [CMU homepage](https://www.cs.cmu.edu/~dpathak/).

He holds the academic appointment **and** the CEO role concurrently — his CMU page lists both.

## In this wiki

Co-author of **[LocoFormer](../sources/locoformer-paper.md)** (CoRL 2025, with Min Liu and Ananye Agarwal), the paper that actually substantiates [Skild AI](skild-ai.md)'s "omni-bodied" claim: one policy trained only on procedurally generated robots, transferring zero-shot to ten commercial platforms at **0.96** against **0.99** for per-robot experts, and — the striking part — **learning from its own falls across trials with frozen weights**.

That result is characteristic of his line of work rather than a departure from it. The through-line from the curiosity work to LocoFormer is **agents that generate their own learning signal**: intrinsic motivation in the 2017 exploration work, and at deployment in LocoFormer, where the signal driving adaptation is the robot's own failed trial.

## The RMA → LocoFormer arc

Two of his papers, four years apart, bracket a shift in how the field thinks about adaptation — and this wiki now holds both.

**[RMA](../sources/rma-paper.md)** (RSS 2021, with Kumar, [Fu](zipeng-fu.md) and Malik) gets a blind [A1](unitree-a1.md) adapting to terrain, payload and friction in **under a second**, using a hand-designed two-module architecture: a privileged teacher supplies a latent "extrinsics" vector, and a small CNN learns to estimate it from **0.5 s** of proprioception. It carries 100% of body weight and crosses an oily sheet at 90% success.

**[Egocentric vision](../sources/egocentric-vision-locomotion-paper.md)** (CoRL 2022, with Agarwal, Kumar and Malik) answers RMA's own stated limitation — that a blind robot is the binding constraint — by adding a single depth camera and reusing the same two-phase recipe with *geometry* as the privileged signal. Blind upstairs goes from 0% to **100%**.

**[LocoFormer](../sources/locoformer-paper.md)** (CoRL 2025) throws the architecture away. No privileged encoder, no adaptation module — one policy, RL only, with context extended to **~18 s across trial boundaries**. It generalizes to bodies rather than terrains, and recovers from *morphology* changes RMA could not represent, including learning from its own falls.

LocoFormer explicitly calls the RMA class **"myopic."** It is his own prior work, and the criticism is fair — 0.5 s was a deliberate concession to what an A1 can compute onboard. The through-line is not a reversal but a budget change: **structure was what you used when you could not afford context.** The middle paper is where that structure is most elaborate and most effective, which makes the three together a compact history of the field trading engineered structure for compute.

## Research line (live-web; not yet ingested here)

> [!note] `[live-web]` — none of the following is an ingested source
> - **Curiosity-driven exploration by self-supervised prediction** (ICML 2017) — intrinsic motivation from prediction error; the work that made his name, reported at 4K+ citations.
> - ~~RMA~~ — **[ingested 2026-08-29](../sources/rma-paper.md)**; see the arc above.
> - ~~Legged locomotion in challenging terrains using egocentric vision~~ — **[ingested 2026-08-29](../sources/egocentric-vision-locomotion-paper.md)**; see the arc above.
> - Further lines listed on his homepage: robot parkour, dexterous manipulation and hand control, **learning from human videos**, and diffusion models for vision.
>
> The "learning from human videos" thread is worth noting: it is the same data thesis [S1](../sources/skild-s1-blog.md) rests on — *"Our model learns by watching human videos. This is a scalable solution for the robotics data problem."*

## Why it matters in this wiki

- **He is the bridge between the wiki's locomotion gap and its foundation-model coverage.** The [awesome-physical-ai gap analysis](../sources/awesome-physical-ai-github.md) flagged the RMA/legged_gym locomotion corpus as missing here; both ends of it are now ingested ([RMA](../sources/rma-paper.md), [LocoFormer](../sources/locoformer-paper.md)) and he authored both, while also leading the company claiming a general robot brain.
- **Academic-to-founder without leaving.** Unlike the [TRI](tri.md) → [Walden](walden-robotics.md) spin-out, where the LBM leadership departed, Pathak retains his CMU chair while running a company valued at **>$14B** `[live-web]`. Worth watching as a pattern in this field — see also [Russ Tedrake](russ-tedrake.md), who moved the other way.

## Related

- [Skild AI](skild-ai.md) — co-founder and CEO.
- [Abhinav Gupta](abhinav-gupta.md) — co-founder and president; CMU colleague.
- [Ananye Agarwal](ananye-agarwal.md) — his PhD student, co-author on both the egocentric-vision paper and LocoFormer, now a Skild founding researcher.
- [LocoFormer](../sources/locoformer-paper.md), [RMA](../sources/rma-paper.md) and [egocentric-vision locomotion](../sources/egocentric-vision-locomotion-paper.md) — his co-authored papers here.
- [Unitree A1](unitree-a1.md) — RMA's platform; also in LocoFormer's zero-shot set.
- [In-context robot learning](../concepts/learning/in-context-robot-learning.md) — the mechanism LocoFormer demonstrates.

## Mentioned in

- [LocoFormer: Generalist Locomotion via Long-context Adaptation](../sources/locoformer-paper.md) — co-author.
- [RMA: Rapid Motor Adaptation for Legged Robots](../sources/rma-paper.md) — co-author (RSS 2021).
- [Legged Locomotion in Challenging Terrains using Egocentric Vision](../sources/egocentric-vision-locomotion-paper.md) — co-advisor (CoRL 2022).

## Open questions / TBD

- **The curiosity paper is uningested** — it would anchor an intrinsic-motivation concept page the wiki does not have.
- **Relationship between the LocoFormer recipe and [S1](../sources/skild-s1-blog.md).** LocoFormer conditions on the robot's own experience; S1 conditions on a human demonstration. Whether Skild regards these as one recipe or two is not stated in either source.

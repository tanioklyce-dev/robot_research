---
title: Locomotion adaptation lineage — RMA to LocoFormer, and the retreat of engineered structure
type: synthesis
created: 2026-08-29
updated: 2026-08-29
tags: [locomotion, adaptation, rma, locoformer, egocentric-vision, privileged-distillation, in-context-learning, cross-embodiment, history, lineage]
---

# Locomotion adaptation lineage — RMA to LocoFormer

Three papers, largely the same people, 2021 → 2025, all asking *how does a legged robot handle a world it was not trained on?* — and answering it in ways that progressively **delete** the machinery of the previous answer. The wiki holds all three primaries, and this page is the connective argument that was otherwise duplicated across four pages.

It is filed as **history** rather than as a method survey. The interest is not which paper wins; it is that the same research group, given four more years of compute, arrived at the opposite architectural conclusion and said so in print.

## The three papers

| | [RMA](../../sources/rma-paper.md) (RSS 2021) | [Egocentric vision](../../sources/egocentric-vision-locomotion-paper.md) (CoRL 2022) | [LocoFormer](../../sources/locoformer-paper.md) (CoRL 2025) |
|---|---|---|---|
| Authors | Kumar, [Fu](../../entities/zipeng-fu.md), [Pathak](../../entities/deepak-pathak.md), Malik | [Agarwal](../../entities/ananye-agarwal.md), Kumar, Malik, Pathak | Liu, Pathak, [Agarwal](../../entities/ananye-agarwal.md) |
| Senses | Proprioception only | **+ egocentric depth** | Proprioception |
| Privileged teacher | Physics (*e*ₜ: mass, friction, motor strength) | **Geometry** (scandots) | **None** |
| Memory | 1-D CNN over **0.5 s** | **GRU**, task-length | **~18 s attention**, across trials |
| Adapts to | Terrain, payload, friction | Terrain geometry ahead | **Morphology** — locked knees, cut legs |
| Recovers | Within a trial | Within a trial | **Across trials — learns from falls** |
| Bodies | One ([A1](../../entities/unitree-a1.md)) | One ([A1](../../entities/unitree-a1.md) + camera) | **Ten unseen, incl. wheeled** |
| Structure | Two modules | Two modules | **One policy** |

## Act 1 — adaptation as an explicit module (2021)

[RMA](../../sources/rma-paper.md)'s move is to notice that a policy does not need to know the physics, only **how to change its behavior given the physics**. A privileged encoder compresses true simulator parameters into an 8-dimensional **extrinsics vector**; a small CNN then learns to estimate that vector from 0.5 s of proprioceptive history.

The ablation is the argument: **predicting the physical parameters directly scores 56.5%, predicting the behavioral correction scores 73.5%.** The useful latent is behavioral, not physical. RMA lands within 2.7 points of a privileged oracle using **zero** real-world adaptation samples, while the contemporary alternative that collected 40,000 real samples scored 41.7%.

Everything about the design is shaped by a compute budget: the adaptation module runs at **10 Hz** against the base policy's 100 Hz, asynchronously with no shared clock, because that is what an [A1](../../entities/unitree-a1.md) can do onboard.

## Act 2 — the same recipe, one level up the sensory stack (2022)

RMA ended by naming its own limitation: the robot is blind, and *"we need to use not just proprioception but also exteroception."* The [egocentric-vision paper](../../sources/egocentric-vision-locomotion-paper.md) is that follow-up, and it reuses RMA's machinery with a different privileged signal — **geometry instead of physics**. Phase 1 trains on cheap *scandots* (terrain height sampled under the robot); phase 2 distils into a policy that sees only a forward depth camera.

Two things make this the high-water mark of the engineered approach:

- **It proves a bound on its own distillation** (Thm 2.1), converting the recipe into a design rule: choose the privileged signal and camera field of view so phase-2 loss can be driven low.
- **Memory becomes structurally mandatory.** A forward-facing camera cannot see under the robot's own hind feet, so the policy *must* remember terrain it has passed. The paper takes this directly from human gaze studies.

It also supplies the lineage's most quotable warning: the **noisy elevation-map baseline is worse than blind** on stairs (6.74 vs 16.64). Degraded perception is not weakly useful; it is misleading.

## Act 3 — deleting the structure (2025)

[LocoFormer](../../sources/locoformer-paper.md) keeps the goal and discards the apparatus. No privileged encoder, no adaptation module, no distillation — one policy, RL only, with context extended past **trial boundaries** and training on **procedurally generated robots that do not exist**.

What that buys is a change in *kind*, not degree. RMA and the vision paper adapt to a changing **environment**; LocoFormer adapts to a changing **body** — and because its memory spans trials, it improves from its own failures at deployment with frozen weights: given a body so unstable it falls on trial 1, it walks by trial 3.

The paper classes the earlier line as **"myopic,"** adapting over *"a few hundred milliseconds."* That is a fair description of RMA's k=50 at 100 Hz, and it is Pathak criticizing his own prior work.

## The argument this lineage actually makes

**Engineered structure was a way of buying adaptivity when context was unaffordable.**

Every piece of RMA's apparatus exists to compress the world into 8 numbers that a small CNN could estimate from half a second of history *on a cheap robot's onboard compute*. The privileged teacher, the extrinsics bottleneck, the asynchronous two-rate deployment — these are not claims about how adaptation ought to work. They are the shape adaptation takes under a hard compute constraint. Relax the constraint and the structure is not improved, it is **removed**: LocoFormer names resource intensity as its first limitation, which is precisely the budget RMA did not have.

Two corollaries worth carrying:

1. **The privileged-teacher recipe is a compute artifact, not a principle.** It appears twice here and is absent by 2025 — see [sim-to-real transfer](../../concepts/learning/sim-to-real-transfer.md), which now records the pattern *and* its abandonment.
2. **What generalization is "over" moved with the budget.** Terrain (2021) → terrain geometry ahead (2022) → bodies (2025). Each step widens the distribution the policy must identify online, and each was affordable only after the previous compute ceiling lifted.

> [!note] This is one line, not the field
> All three papers come from an overlapping CMU/Berkeley group that became [Skild AI](../../entities/skild-ai.md). The parallel ETH line ([legged_gym](../../entities/legged-gym.md), ANYmal, elevation-map methods) is present here only as the baseline these papers argue against, and the **humanoid** locomotion corpus (H2O / HumanPlus / ASAP / HOVER) is not ingested at all. Read this as a well-documented thread, not a survey.

## Where it connects

- **[In-context robot learning](../../concepts/learning/in-context-robot-learning.md)** — LocoFormer is the *experience-conditioned* mode; RMA is its prehistory, reaching the behavioral-latent insight four years early with a hand-built bottleneck.
- **[Sim-to-real transfer](../../concepts/learning/sim-to-real-transfer.md)** — holds the two-phase privileged-distillation pattern this lineage established.
- **[Skild AI](../../entities/skild-ai.md)** — LocoFormer is the evidence behind the company's "omni-bodied" claim, which its manipulation model [S1](../../sources/skild-s1-blog.md) does **not** substantiate. The locomotion line is peer-reviewed; the manipulation line is a blog post.
- **[The Robot AI industry](../society/robot-ai-industry-map.md)** — the same trade (structure vs scale) is what the model-layer bet rests on commercially.
- **[Humanoid whole-body control lineage](humanoid-wbc-lineage.md)** — the sibling branch, which over the same years went the **opposite** way: it kept and deepened privileged distillation while this line discarded it. The contrast is the most useful thing either page says.
- **[Atari RL lineage](atari-rl-lineage.md)** — the wiki's other lineage page; the same arc from engineered value-function tricks to scale is visible there.

## Open follow-ups

- ~~The humanoid half is the largest remaining gap~~ — **ingested 2026-08-29** ([humanoid WBC lineage](humanoid-wbc-lineage.md)). It does **not** follow this arc: that branch kept its privileged teachers. Why the two diverged is argued there.
- **Extreme Parkour** ([Agarwal](../../entities/ananye-agarwal.md) & Pathak) is the missing middle between Act 2 and Act 3.
- **Rudin et al.** (the [legged_gym](../../entities/legged-gym.md) primary) would ground the parallel ETH line properly instead of by reference.
- ~~Ashish Kumar has no entity page~~ — filed 2026-08-29 ([Ashish Kumar](../../entities/ashish-kumar.md)). **Jitendra Malik**, co-author on both of Acts 1 and 2 and in three ingested sources, still has none.
- **Does the arc hold for manipulation?** LocoFormer's authors say they *"believe this simple, yet general recipe can be used to train foundation models for other robotic skills."* [S1](../../sources/skild-s1-blog.md) conditions on human demonstrations rather than its own experience — so as published, the recipe **changed** in the move to manipulation.

---
title: In-context robot learning
type: concept
created: 2026-08-29
updated: 2026-08-29
sources: 4
tags: [in-context-learning, robot-foundation-model, demonstration-conditioning, test-time-adaptation, vla, skild-ai, s1]
---

# In-context robot learning

**Adapting a robot policy from information supplied at inference time — a demonstration of the task, or the policy's own recent experience of the body — rather than from a language instruction or from post-training.** The weights do not change; the information enters as context and the policy conditions on it, exactly as an LLM conditions on few-shot examples in its prompt. See [Two modes](#two-modes-often-conflated) — the term is routinely used for both, and they are not the same mechanism.

The framing that makes it precise is a two-loop one, from [S1](../../sources/skild-s1-blog.md): *"Pre-training is the outer loop that teaches the policy how to learn from context; at inference time, the demonstration drives the inner loop without changing any weights."* Pre-training must therefore use episodic data in which **the task is identified only by an in-context demonstration** — otherwise the model has no pressure to learn the inner loop at all, and will simply learn the tasks.

## Why it is a different answer to the specification problem

Every generalist policy has to be told what to do. The field's three answers:

| Approach | Specification | Cost of a new task |
|---|---|---|
| **Post-training / fine-tuning** | task-specific data | hundreds to thousands of demonstrations |
| **Language conditioning** ([VLA](vla-models.md)) | a natural-language instruction | zero, *if* the task is in-distribution; post-training if not |
| **In-context learning** | one demonstration at inference | one demonstration |

Language conditioning assumes the instruction is enough to identify the behavior. In-context learning assumes a demonstration is a **richer specification** — it carries the intent, the functional correspondences, and the task progress that language leaves implicit. The cost is that someone must perform the task once, on the spot.

## Two modes, often conflated

The term covers two mechanisms that share an implementation (no weight update, information enters through context) and differ in **what the context contains**:

| | **Demonstration-conditioned** | **Experience-conditioned** |
|---|---|---|
| Context holds | a human demonstration of the *task* | the policy's own trials with this *body* |
| Answers | "what should I do?" | "what am I?" |
| Closest classical analogue | few-shot imitation | online system identification |
| Wiki instance | [S1](../../sources/skild-s1-blog.md) (manipulation) | [LocoFormer](../../sources/locoformer-paper.md) (locomotion) |

Both are [Skild AI](../../entities/skild-ai.md) systems and both are marketed under the same "in-context" banner, but the second does something the first does not: **it improves from its own failures within a deployment.** LocoFormer, given a body so unstable it falls on trial 1, keeps that failure in its Transformer-XL cache and walks by trial 3 — frozen weights throughout. That is in-context *reinforcement* learning; S1 is in-context *imitation*.

Keeping them apart matters when reading claims. "Omni-bodied in-context learning" is evidenced for the experience-conditioned locomotion case and not for the demonstration-conditioned manipulation case.

## Current state

Two sources, of very different evidence grade. The **experience-conditioned** case is peer-reviewed and well-controlled ([LocoFormer](../../sources/locoformer-paper.md), CoRL 2025: 0.96 zero-shot across ten unseen robots against 0.99 per-robot experts, with a GRU ablation collapsing to 0.37). The **demonstration-conditioned** case below is a single vendor blog with no third-party evaluation.

[Skild AI](../../entities/skild-ai.md)'s [S1](../../sources/skild-s1-blog.md) (August 2026) reports a **scaling crossover** rather than a flat advantage:

| Pre-training data | Setting | In-context | Language-conditioned |
|---|---|---|---|
| 1,000 h | seen | **43%** | **53%** |
| 100,000 h | **unseen** | **66%** | **9%** |

**At small scale in-context learning is worse.** It only wins once pre-training is large, and Skild's claim is that the gap then *"widens exponentially."* This is the right shape for the claim to have — an inner loop has to be learned before it can pay, so it should cost something at low data — which is a point in its favor, since it is not the result a vendor would fabricate.

Reported corollaries, all self-reported and none independently evaluated:

- **One in-context demonstration ≈ 380 post-training examples**, which for long-horizon tasks is 50–100 hours of teleoperation compressed into an 11-minute setup.
- **Robustness to prompt-to-deployment mismatch** up to ~30 cm / 45° of object displacement and object substitution; degradation when the demonstration implies a different execution plan (e.g. the other arm).
- **Correction of the demonstration** — the policy reportedly executing a step more cleanly than the demonstrator who showed it, which if real means the demonstration is being read as intent rather than copied as trajectory.

> [!warning] One vendor, no replication, no named embodiment
> Everything above comes from a single [blog post](../../sources/skild-s1-blog.md) with no third-party evaluation, no rollout counts, no released weights, and **no statement of which robot it runs on**. Read the numbers as a hypothesis with a plausible shape, not as an established result. The [success-rate audit](../../syntheses/platforms/vla-success-rate-audit.md) applies with full force.

## Relationship to neighboring ideas

- **[Test-time adaptation](test-time-adaptation.md)** — in-context learning is its limiting case: adaptation with *zero* gradient steps.
- **[Sim-to-real transfer](sim-to-real-transfer.md)** — [LocoFormer](../../sources/locoformer-paper.md) is an unusually strong instance: trained only on *procedurally generated robots that do not exist*, transferring zero-shot to ten commercial platforms with no system identification.
- **[VLA models](vla-models.md)** — the language-conditioned alternative, and the baseline S1 measures against.
- **[Scaling laws for VLAs](scaling-laws-vla.md)** — the crossover claim is a scaling-law claim, and belongs to that literature rather than to a leaderboard.
- **[Soft-prompt cross-embodiment](soft-prompt-cross-embodiment.md)** — a different route to conditioning a shared policy without retraining per body.
- **[Imitation learning](imitation-learning.md)** — the parent tradition; ICL is imitation where the demonstration arrives at inference rather than at training.
- **[Crowdsourced robot training data](crowdsourced-robot-training-data.md)** — S1's data table rates egocentric human video highest on diversity and scalability, which is what makes the outer loop trainable at all.

## Prehistory: adaptation before long context

The experience-conditioned mode did not begin with long context. **[RMA](../../sources/rma-paper.md)** (Kumar, Fu, [Pathak](../../entities/deepak-pathak.md) & Malik, RSS 2021) solved the same problem — a robot inferring its own situation online, with no weight update — using **0.5 s of proprioception** and an explicitly engineered two-module design: a privileged teacher produces a latent "extrinsics" vector in simulation, and a small CNN learns to regress it from state–action history at deployment.

Crucially, RMA also **declines to identify the system**: it predicts *how behavior should change*, not the physical parameters, and its ablation shows that predicting the physics directly is **worse** (56.5% vs 73.5%). That is the same instinct long-context in-context learning acts on — the useful latent is behavioral, not physical — reached four years earlier with a hand-built bottleneck instead of attention.

What separates them is horizon and structure, not aim. RMA adapts to **terrain, payload and friction within a trial**; [LocoFormer](../../sources/locoformer-paper.md) adapts to **morphology across trials**, which requires remembering a failure. LocoFormer calls the RMA class *"myopic"* — accurate, and a deliberate choice on RMA's part, made to fit a cheap robot's onboard compute.

## Key references

- [Introducing S1: In-Context Learning for Robotics](../../sources/skild-s1-blog.md) — [Skild AI](../../entities/skild-ai.md), August 2026. The wiki's anchor source; vendor blog.
- [**RMA: Rapid Motor Adaptation for Legged Robots**](../../sources/rma-paper.md) — Kumar, Fu, Pathak & Malik, RSS 2021. The prehistory: fixed 0.5 s window, explicit adaptation module, privileged teacher.
- [**LocoFormer: Generalist Locomotion via Long-context Adaptation**](../../sources/locoformer-paper.md) — Liu, [Pathak](../../entities/deepak-pathak.md) & Agarwal, CoRL 2025. The experience-conditioned instance, and the better-evidenced of the two: peer-reviewed, with baselines (GRU 0.37 vs 0.96) and per-robot expert upper bounds (0.99).

## Mentioned in

- [Introducing S1](../../sources/skild-s1-blog.md) — the demonstration-conditioned mode.
- [LocoFormer](../../sources/locoformer-paper.md) — the experience-conditioned mode.
- [Skild AI](../../entities/skild-ai.md) — the company behind both.
- [RMA](../../sources/rma-paper.md) — the pre-long-context ancestor.
- [Locomotion adaptation lineage](../../syntheses/rl/locomotion-adaptation-lineage.md) — the full 2021→2025 arc these two sit at either end of.
- [Deepak Pathak](../../entities/deepak-pathak.md) — co-author of both LocoFormer and RMA.

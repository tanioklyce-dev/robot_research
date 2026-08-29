---
title: In-context robot learning
type: concept
created: 2026-08-29
updated: 2026-08-29
sources: 1
tags: [in-context-learning, robot-foundation-model, demonstration-conditioning, test-time-adaptation, vla, skild-ai, s1]
---

# In-context robot learning

**Specifying a robot task with a demonstration supplied at inference time, rather than with a language instruction or with post-training on task data.** The model's weights do not change; the demonstration enters as context and the policy conditions on it, exactly as an LLM conditions on few-shot examples in its prompt.

The framing that makes it precise is a two-loop one, from [S1](../../sources/skild-s1-blog.md): *"Pre-training is the outer loop that teaches the policy how to learn from context; at inference time, the demonstration drives the inner loop without changing any weights."* Pre-training must therefore use episodic data in which **the task is identified only by an in-context demonstration** — otherwise the model has no pressure to learn the inner loop at all, and will simply learn the tasks.

## Why it is a different answer to the specification problem

Every generalist policy has to be told what to do. The field's three answers:

| Approach | Specification | Cost of a new task |
|---|---|---|
| **Post-training / fine-tuning** | task-specific data | hundreds to thousands of demonstrations |
| **Language conditioning** ([VLA](vla-models.md)) | a natural-language instruction | zero, *if* the task is in-distribution; post-training if not |
| **In-context learning** | one demonstration at inference | one demonstration |

Language conditioning assumes the instruction is enough to identify the behavior. In-context learning assumes a demonstration is a **richer specification** — it carries the intent, the functional correspondences, and the task progress that language leaves implicit. The cost is that someone must perform the task once, on the spot.

## Current state

Thinly evidenced, from essentially one vendor source, but the shape of the claim is notable.

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
- **[VLA models](vla-models.md)** — the language-conditioned alternative, and the baseline S1 measures against.
- **[Scaling laws for VLAs](scaling-laws-vla.md)** — the crossover claim is a scaling-law claim, and belongs to that literature rather than to a leaderboard.
- **[Soft-prompt cross-embodiment](soft-prompt-cross-embodiment.md)** — a different route to conditioning a shared policy without retraining per body.
- **[Imitation learning](imitation-learning.md)** — the parent tradition; ICL is imitation where the demonstration arrives at inference rather than at training.
- **[Crowdsourced robot training data](crowdsourced-robot-training-data.md)** — S1's data table rates egocentric human video highest on diversity and scalability, which is what makes the outer loop trainable at all.

## Key references

- [Introducing S1: In-Context Learning for Robotics](../../sources/skild-s1-blog.md) — [Skild AI](../../entities/skild-ai.md), August 2026. The wiki's anchor source; vendor blog.
- **LocoFormer** (Liu et al., 2025) — Skild's locomotion predecessor, cited as learning embodiment transfer in-context (*"never told which body it is driving"*). **Not yet ingested**, and the more interesting claim of the two.

## Mentioned in

- [Introducing S1](../../sources/skild-s1-blog.md) — the concept's anchor.
- [Skild AI](../../entities/skild-ai.md) — the company built on it.

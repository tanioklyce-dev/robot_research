---
title: "Introducing S1: In-Context Learning for Robotics (Skild AI blog)"
type: source
url: https://www.skild.ai/blogs/s1
author: Skild AI (no individual authors named)
published: 2026-08
ingested: 2026-08-29
local_path: null
format: web (vendor blog post)
tags: [skild-ai, s1, in-context-learning, robot-foundation-model, vla, scaling-laws, long-horizon, umi, egocentric-video, vendor-source]
---

# Introducing S1: In-Context Learning for Robotics

## Summary

[Skild AI](../entities/skild-ai.md)'s announcement of **S1**, its flagship robot foundation model, built around **in-context learning (ICL)** rather than language prompting: *"Show it a video of a task, short or long, seen or unseen, and it executes."* The claim is that a single demonstration at inference time — **"No fine-tuning, no post-training. The same model weights produced every example shown in this blog"** — substitutes for hundreds of post-training demonstrations, and that this advantage *grows* with pre-training scale.

The mechanism is a two-loop framing: **"Pre-training is the outer loop that teaches the policy how to learn from context; at inference time, the demonstration drives the inner loop without changing any weights."** Pre-training uses episodic data in which the task is specified *only* by an in-context demonstration, forcing the model to infer the demonstrator's intent, functional correspondences, and task progress in order to predict actions.

The headline result is a **scaling crossover**, and it is more interesting than the marketing framing suggests — at small data ICL *loses* to language conditioning, and only wins once pre-training is large. See [Key claims](#key-claims).

> [!warning] Vendor blog — self-reported, no third-party evaluation, no hardware disclosed
> Every number here is **self-reported by Skild AI**. The post names **no external or third-party evaluation**, no individual authors, and — notably for a company whose positioning is "omni-bodied" — **never states which robot hardware or embodiment S1 runs on**, in text or figure captions. There is no paper, no released weights, no reproduction. Treat as **marketing-grade until replicated**, the same standard this wiki applies to [Helix](../entities/helix.md).

## Key claims

### The scaling crossover — the actual finding

| Pre-training data | Setting | In-context learning | Language-conditioned baseline |
|---|---|---|---|
| **1,000 h** | in-distribution / seen | **43%** | **53%** |
| **100,000 h** | **unseen / OOD tasks** | **66%** | **9%** |

Verbatim on the low-data case: *"at 1k hours of pretraining, the language-conditioned policy achieved a 53% success rate compared with 43% for ICL."*

**ICL is worse until it is much better.** At 1k hours language conditioning wins by 10 points; at 100k hours on unseen tasks ICL leads by 57. Skild's framing is that *"the gap between ICL and VLA widens exponentially as pre-training data increases."* This is the load-bearing claim of the post, and it is a claim about a **trend across a scaling study**, not a single benchmark number — which makes it both more interesting and harder to verify than a leaderboard placement.

- Seen tasks: ICL reaches **96%** accuracy as pre-training scales.
- Study range: **1,000 → 100,000 hours** of pre-training data.

### Demonstration efficiency

- **"A single demonstration in context is worth roughly 380 post-training examples."**
- For long-horizon tasks (>4 minutes), collecting those 380 demonstrations takes **50–100 hours of teleoperation**.
- The language-prompted VLA baseline reaches **86%** only with **2,000 demonstrations** of post-training.
- End-to-end: **"The time from demonstration to autonomous execution was 11 minutes"** (plant-potting task).

### Data strategy

Skild's stated trade-off table across four data sources:

| Source | Hardware proximity | Diversity | Scalability |
|---|---|---|---|
| Robot teleoperation | High | Low | Low |
| **[UMI](../entities/umi.md)** | Moderate | Moderate | Moderate |
| Egocentric video | Low | **High** | **High** |
| Simulation | Moderate | Low | High |

- **"Our model learns by watching human videos. This is a scalable solution for the robotics data problem."**
- **"For every dollar we spend on collecting data, we spend three on quality control"** — screening for low-level precision, task coherence, and annotation fidelity. A rare public statement of the **data-QC-to-collection cost ratio**, and worth recording precisely because almost nobody publishes one.
- Trained on **NVIDIA AI infrastructure**.

### Robustness

- **Training-distribution shift (L1–L5):** at L5, *"the language-prompted VLA degrades up to three times as much as the ICL policy."*
- **Prompt-to-deployment mismatch:** robust to object position shifts up to **30 cm / 45°** and to object substitutions; degrades significantly *"once the demonstration implies a substantially different execution plan, as in L5, where actions must switch to the opposite arm."*

### Long-horizon unseen tasks

Four tasks, none seen in pre-training, up to **10 minutes**: plant potting (digging soil to make room for a plant), pancake flipping, pour-over coffee (pressing a filter into a funnel), and skateboard-wheel kit assembly.

> *"This is the first time that a robotics foundation model, S1, has shown in-context learning on extremely long-horizon tasks (up to 10 minutes) that were never seen during pre-training."*

### Emergent behaviors claimed

- **Common-sense substitution** — prompt shows watering with a can; S1 uses an available cup instead. Prompt shows filling a full glass; S1 only tops it off.
- **Improving on a flawed demonstration** — *"the demonstrator drops an egg prematurely and makes a mess, while S1 performs the same step with a controlled motion."*
- **Mistake recovery** out of the box, including on out-of-distribution tasks.

> [!note] The interesting epistemics of "improves on the demonstration"
> If S1 corrects a demonstrator's error, the demonstration is not functioning as a trajectory to copy but as a *specification of intent* the model reconstructs and then executes better. That is the strongest version of the ICL claim on this page — and also the least falsifiable from video, since "better" is the vendor's judgment. It would be a genuinely important result if it survived an independent evaluation with a pre-registered success criterion.

## Contradictions and tensions

> [!warning] Contradiction — "omni-bodied" positioning vs. what S1 actually claims
> [Skild AI](../entities/skild-ai.md)'s own site describes the Skild Brain as *"a unified, omni-bodied brain to control any robot for any task"* and asserts *"Physical AI should be omni-bodied."* **The S1 post makes no cross-embodiment claim for manipulation at all** — it never names a robot platform, and the only embodiment-transfer claim is for the **predecessor locomotion model, LocoFormer** (Liu et al., 2025), described as never being told which body it is driving.
>
> So the company's flagship manipulation model is announced without the property the company's positioning is built on. That may simply be an unstated capability — but as published, "omni-bodied" is a claim about LocoFormer and about the roadmap, not about S1.

> [!note] Tension with the field's evaluation standards
> A 66%-vs-9% gap is enormous, and the post gives **no rollout counts** for any figure. Per the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md), a ±2 pp band needs ≈1,030 rollouts; nothing here indicates the sample sizes. The *shape* of the scaling claim (a widening gap across a 100× data sweep) is more robust to small samples than any single number, which is the strongest thing that can be said for it.

## Entities mentioned

- [Skild AI](../entities/skild-ai.md) — the publisher; S1 is its flagship model.
- [UMI](../entities/umi.md) — named in the data-source trade-off table as the moderate-on-every-axis option between teleoperation and egocentric video.
- [NVIDIA](../entities/nvidia.md) — training infrastructure.

## Concepts touched

- [In-context robot learning](../concepts/learning/in-context-robot-learning.md) — this source is the wiki's anchor for the concept.
- [VLA models](../concepts/learning/vla-models.md) — the language-conditioned baseline S1 is positioned against.
- [Scaling laws for VLAs](../concepts/learning/scaling-laws-vla.md) — the crossover is a scaling-law claim.
- [Test-time adaptation](../concepts/learning/test-time-adaptation.md) — ICL is adaptation without weight updates, the limiting case.
- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) — the egocentric-video and UMI rows of the data table.

## Open questions

- **Which robot?** No embodiment is named anywhere. Without it, none of these numbers can be compared against [LIBERO](../entities/libero.md), RoboArena, or any other result in this wiki.
- **Rollout counts.** Absent for every figure.
- **Is the 380× equivalence a measured curve or a point estimate?** The post gives one number; the methodology behind it is not described.
- **Does the crossover survive at a fixed compute budget?** ICL pays for its inner loop at inference time in context length; the post compares data scales, not inference cost.
- **LocoFormer is uningested.** The cited locomotion predecessor (Liu et al., 2025) has no page here and carries the actual cross-embodiment claim.
- **Independent replication.** None exists. Weights are not released.

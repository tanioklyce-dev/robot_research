---
title: "Introducing S1: In-Context Learning for Robotics (Skild AI blog)"
type: source
url: https://www.skild.ai/blogs/s1
author: Skild AI (no individual authors named)
published: 2026-08
ingested: 2026-08-29
local_path: raw/2026-08-skild-s1-blog.md
sha256: 12cb053c4b8d74cefaee91f2affa78f3592566f742e5c123c340eb765c31749d
rechecked: 2026-09-12
format: web (vendor blog post; "13-minute read"; text snapshot captured 2026-09-12, videos lost)
tags: [skild-ai, s1, in-context-learning, robot-foundation-model, vla, scaling-laws, long-horizon, umi, egocentric-video, human-video-prompting, bimanual, vendor-source]
---

# Introducing S1: In-Context Learning for Robotics

## Summary

[Skild AI](../entities/skild-ai.md)'s announcement of **S1**, its flagship robot foundation model, built around **in-context learning (ICL)** rather than language prompting: *"Show it a video of a task, short or long, seen or unseen, and it executes."* The claim is that a single demonstration at inference time — **"No fine-tuning, no post-training. The same model weights produced every example shown in this blog"** — substitutes for hundreds of post-training demonstrations, and that this advantage *grows* with pre-training scale.

The mechanism is a two-loop framing: **"Pre-training is the outer loop that teaches the policy how to learn from context; at inference time, the demonstration drives the inner loop without changing any weights."** Pre-training uses episodic data in which the task is specified *only* by an in-context demonstration, forcing the model to infer the demonstrator's intent, functional correspondences, and task progress in order to predict actions.

The headline result is a **scaling crossover**, and it is more interesting than the marketing framing suggests — at small data ICL *loses* to language conditioning, and only wins once pre-training is large. See [Key claims](#key-claims).

> [!warning] Vendor blog — self-reported, no third-party evaluation, no hardware disclosed
> Every number here is **self-reported by Skild AI**. The post names **no external or third-party evaluation**, no individual authors, and — notably for a company whose positioning is "omni-bodied" — **never states which robot hardware or embodiment S1 runs on**, in text or figure captions. There is no paper, no released weights, no reproduction. Treat as **marketing-grade until replicated**, the same standard this wiki applies to [Helix](../entities/helix.md).

> [!note] Re-checked 2026-09-12 — no upstream change; original ingest was incomplete
> The post was re-fetched and read against this page. **Every number above and below matches the live text**; nothing has been revised upstream. The first ingest (2026-08-29) kept no local copy, so one is now in `raw/` and sealed. The re-read did, however, find material the first pass dropped — most importantly **how the scaling-study numbers were measured**, which changes how the 66%-vs-9% headline should be read. See [Evaluation methodology](#evaluation-methodology-recovered-on-re-read-2026-09-12).

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

### Evaluation methodology (recovered on re-read, 2026-09-12)

The scaling numbers come with conditions the first ingest did not record. Verbatim:

- **Controlled study**: *"training both ICL and language-conditioned VLA policies on datasets from 1k to 100k hours. Both models use identical data, architectures (besides the prompt embedding), and compute."* Data is *"a filtered subset of our pre-training data pool."* This is a cleaner comparison than most vendor posts offer — same data, same architecture, same compute, one variable — and it is the strongest methodological statement in the post.
- **Two internal suites**: one of seen tasks, one of unseen. Tasks are **long-horizon, 4–8 minutes**.
- **The metric is *"the average of cumulative per-step success rate across all tasks"*** — not whole-task success. A 66% is a per-step average over a multi-step task, graded cumulatively.
- **Human intervention during rollouts**: *"To ensure all steps are graded cumulatively, we use human intervention to recover from failures during policy rollouts. This intervention is mainly used for the VLA baseline because otherwise the baseline scores zero and doesn't complete the full long unseen task even once."*

> [!warning] The headline gap is measured with humans resetting failures
> The 66%-vs-9% comparison is not autonomous whole-task success. It is a per-step average in which a human intervenes after failures so later steps can be scored — and the post says the intervention is *"mainly"* for the baseline, which means it is not *only* for the baseline. Three consequences: (1) the VLA's 9% is a **generous** figure for the baseline (unassisted it *"scores zero"*), so the gap on the harder reading is larger, not smaller; (2) the ICL figures are **not** the fully-autonomous rates the demo videos imply, and the post does not say how often S1 was reset; (3) neither number is comparable to a whole-task success rate from any other source in this wiki. The demonstration-efficiency figure (one demo ≈ 380 episodes) inherits all of this, since it is the same 66% measured the same way.

- **The 380 figure is an interpolation.** *"The exact crossing was estimated by interpolating between measured points"* on a post-training sweep from **1 to 2,000** teleop demonstrations. It is a curve crossing, not a measured point. (Resolves an open question below.)
- **The prompt is an egocentric human video.** The plant-potting timeline records *"one egocentric human video demonstration recorded"*; the method section says the demonstration *"may come from a different scene, viewpoint, or embodiment"* and the Fig. 2 caption that the policy *"translates it to its own embodiment."* Human-to-robot is therefore S1's **default** prompting mode, not an edge case — which matters for the comparison with [GEN-1.5](generalist-gen-1-5-blog.md), where human-to-robot is hedged as working *"in some cases."*
- **The hardware is bimanual.** Still unnamed, but the L5 perturbation is defined as *"placement chosen so that half the robot's actions have to be executed with the opposite arm."* A two-armed platform, then. Nothing narrows it further — the videos were not inspected here.
- **"7×"** is the post's own summary of the unseen-task gap (66 / 9 ≈ 7.3); *"moderate"* is its own word for the seen-task gain.
- **Named comparators.** The post positions against two concurrent manipulation systems by name — *"(Generalist AI, 2026), (Jiang et al., 2026)"* — as *"largely cover[ing] tasks which are short-horizon or already present in the pre-training distribution."* Jiang et al. is **RoboTTT: Context Scaling for Robot Policies** (arXiv 2607.15275), not in this wiki. It also cites **FACTR 2** (Oh et al., arXiv 2606.12406; Pathak is last author) for the premise that with dense post-training data, *"policies trained from scratch with no pre-training can match the peak performance of a post-trained foundation model"* — from which it draws *"what is the point of pre-training?"* and answers: to enable in-context learning. **Checked 2026-09-12: [FACTR 2](factr-2-paper.md) contains no such claim** — in neither arXiv version does it post-train a foundation model or compare one against from-scratch policies; every policy there is trained from scratch and the words *pre-train* and *foundation model* do not occur outside its references. The premise S1's argument opens with is attributed to a paper that does not state it.
- **Timeline (Fig. 8)**: September 2025 LocoFormer → February 2026 first in-domain ICL results → May 2026 *"S1 flips first pancake"* (first out-of-distribution result) → August 2026 release. *"We first saw signs of life for short-horizon tasks about six months ago."*
- **Status**: *"S1 is already at work with our commercial partners."* The post is *"the first in a series"*; training details are deferred to future posts.

### Demonstration efficiency

- **"A single demonstration in context is worth roughly 380 post-training examples"** — an interpolated crossing, see [methodology](#evaluation-methodology-recovered-on-re-read-2026-09-12).
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
> [Skild AI](../entities/skild-ai.md)'s own site describes the Skild Brain as *"a unified, omni-bodied brain to control any robot for any task"* and asserts *"Physical AI should be omni-bodied."* **The S1 post makes no cross-embodiment claim for manipulation at all** — it never names a robot platform, and the only embodiment-transfer claim is for the **predecessor locomotion model, [LocoFormer](locoformer-paper.md)** (Liu, Pathak & Agarwal, CoRL 2025 — ingested 2026-08-29), which demonstrates it properly: zero-shot to ten unseen commercial robots at 0.96 against 0.99 for per-robot experts.
>
> So the company's flagship manipulation model is announced without the property the company's positioning is built on. That may simply be an unstated capability — but as published, "omni-bodied" is a claim about LocoFormer and about the roadmap, not about S1.

> [!note] Tension with the field's evaluation standards
> A 66%-vs-9% gap is enormous, and the post gives **no rollout counts** for any figure. Per the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md), a ±2 pp band needs ≈1,030 rollouts; nothing here indicates the sample sizes. The *shape* of the scaling claim (a widening gap across a 100× data sweep) is more robust to small samples than any single number, which is the strongest thing that can be said for it.

## Entities mentioned

- [Skild AI](../entities/skild-ai.md) — the publisher; S1 is its flagship model.
- [UMI](../entities/umi.md) — named in the data-source trade-off table as the moderate-on-every-axis option between teleoperation and egocentric video.
- [NVIDIA](../entities/nvidia.md) — training infrastructure.
- [Generalist AI](../entities/generalist-ai.md) — named as concurrent work ([GEN-1.5](generalist-gen-1-5-blog.md)), characterised as short-horizon / in-distribution.
- [LocoFormer](locoformer-paper.md) — the predecessor locomotion in-context learner, first stop on the post's own timeline.

## Concepts touched

- [In-context robot learning](../concepts/learning/in-context-robot-learning.md) — this source is the wiki's anchor for the concept.
- [VLA models](../concepts/learning/vla-models.md) — the language-conditioned baseline S1 is positioned against.
- [Scaling laws for VLAs](../concepts/learning/scaling-laws-vla.md) — the crossover is a scaling-law claim.
- [Test-time adaptation](../concepts/learning/test-time-adaptation.md) — ICL is adaptation without weight updates, the limiting case.
- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) — the egocentric-video and UMI rows of the data table.

## Open questions

- **Which robot?** No embodiment is named anywhere. **Narrowed 2026-09-12:** it is bimanual (the L5 definition requires the "opposite arm"). Without a name, none of these numbers can be compared against [LIBERO](../entities/libero.md), RoboArena, or any other result in this wiki — and the per-step-with-intervention metric makes them incomparable regardless.
- **Rollout counts.** Absent for every figure.
- **How often was S1 itself reset?** Intervention is *"mainly"* for the baseline. The unassisted ICL rate is not published.
- ~~**Is the 380× equivalence a measured curve or a point estimate?**~~ **Resolved 2026-09-12:** an interpolated crossing on a 1-to-2,000-demonstration post-training sweep (the post says so in Fig. 7's text).
- ~~**RoboTTT (Jiang et al. 2026)** — the second named comparator, uningested.~~ **Ingested 2026-09-12** ([RoboTTT](robottt-paper.md)). Skild's characterisation holds for RoboTTT's *in-context imitation* result and ignores its headline; see that page's callout.
- **Does the crossover survive at a fixed compute budget?** ICL pays for its inner loop at inference time in context length; the post compares data scales, not inference cost.
- ~~LocoFormer is uningested~~ — **ingested 2026-08-29** ([LocoFormer](locoformer-paper.md)). It carries the cross-embodiment claim, and conditions on the robot's **own experience** rather than a demonstration — a different mechanism under the same name.
- **Independent replication.** None exists. Weights are not released.

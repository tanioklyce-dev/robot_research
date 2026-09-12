---
title: Continual learning and catastrophic forgetting
type: concept
created: 2026-09-11
updated: 2026-09-12
sources: 17
tags: [continual-learning, lifelong-learning, catastrophic-forgetting, skill-library, test-time-adaptation, in-context-learning, real-world-rl, rehearsal, knowledge-insulation, lora, deployment, household]
---

# Continual learning and catastrophic forgetting

**Continual learning** is the *learn* stage of [the loop](../../overview.md): a deployed robot experiences, learns from the experience, and **retains what it already knew**. **Catastrophic forgetting** is the failure — a weight update for a new task overwrites competence at old ones. The [research-direction](../../syntheses/world-models/open-questions-and-research-direction.md) page calls this the wiki's thinnest open question and possibly the most important for the household setting: *deploy → experience → learn → retain* "is the difference between a robot that works in a demo and one that still works in a home after a month."

This page exists to stop three different things from being called by one name. The wiki has primaries for two of them and none for the third.

## Three things called "continual learning"

| Mechanism | What changes | Wiki primaries | Forgetting risk |
|---|---|---|---|
| **A. Skill-library growth** | a library of code or programs grows; **no gradient** | [Voyager](../../sources/voyager-paper.md), [ASPIRE](../../sources/aspire-paper.md), [CaP-X](../../sources/cap-x-paper.md) | none by construction — but entries go stale |
| **B. Adaptation without permanent change** | activations or a KV cache ([in-context](in-context-robot-learning.md)); or a few gradient steps later discarded ([test-time adaptation](test-time-adaptation.md)) | [LocoFormer](../../sources/locoformer-paper.md), [S1](../../sources/skild-s1-blog.md), [GEN-1.5](../../sources/generalist-gen-1-5-blog.md), [AdaJEPA](../../sources/adajepa-paper.md) | none at the weight level; the *episode* can be mis-adapted |
| **C. Weight-update continual learning** | the deployed policy's weights are updated with deployment data and kept | [RECAP / π*0.6](../../sources/pistar06-paper.md), [HIL-SERL](../../sources/hil-serl-paper.md), [Scanford](../../sources/robot-powered-data-flywheels-paper.md), [GR00T N1](../../sources/groot-n1-paper.md) (the forgetting case) | **this is where forgetting lives** — and the wiki has **no primary on preventing it** (no EWC, no survey) |

The [backlog](../../backlog.md) item that created this page asked for exactly this split. What follows is what the wiki can say about each.

## A. Skill libraries: the one mechanism with a compounding curve

The problem statement, from [ASPIRE](../../sources/aspire-paper.md): *"the agent solving its hundredth task is effectively no more experienced than the agent solving its first."* Its answer is a library of verified sub-programs that later tasks reuse, and it is the wiki's only continual-learning result with a **scaling curve rather than a before/after**: a library accumulated on LIBERO-90 lifts held-out LIBERO-Pro Long from **4% → ~31%** zero-shot, rising monotonically across library sizes N ∈ {0, 25, 50, 90}. On a real bimanual [YAM](../../entities/yam.md) the library transfers across embodiments — open/push drawer **0/20 → 11/20** — and cuts token cost fourfold.

Two qualifications the page must carry:

- **Only one of two ingested code-as-policy papers shows it.** [CaP-X](../../sources/cap-x-paper.md)'s library ablation is **+4 pp (55 → 59), p = 0.13 at n = 700** — not established. The [success-rate audit](../../syntheses/platforms/vla-success-rate-audit.md)'s instruction: cite ASPIRE, not this ablation, for "skill libraries compound."
- **Libraries forget by rotting, not overwriting.** ASPIRE's own limitations: entries "may become stale, overly specific, redundant, or misleading," offered as the explanation for non-monotonic transfer. Memory management for a growing library is unsolved, and [Voyager](../../sources/voyager-paper.md)'s claim that code skills "alleviate catastrophic forgetting" is true only in the narrow sense that nothing is ever overwritten.

[Waddle Labs](../../entities/waddle-labs.md) claims to run this loop continuously across agents in deployment; the wiki's verdict is that ASPIRE quantified the mechanism and Waddle never did. ASPIRE itself says it is "not a real-world lifelong learner yet" — deployment still needs success detection, safe reset, safety monitoring, and calibration maintenance. The lineage is on [code as policy](../agents/code-as-policy.md).

## B. Adapting without changing the weights

Two ways to learn at deployment while leaving the checkpoint alone.

**In-context.** [LocoFormer](../../sources/locoformer-paper.md) is the wiki's cleanest demonstration that learning and training can come apart: a biped that fails trial 1 keeps the failure in its Transformer-XL cache and **walks stably by trial 3 with weights frozen**; a GRU ablation collapses 0.96 → 0.37. [Skild S1](../../sources/skild-s1-blog.md) (vendor, unreplicated) claims the scaling crossover — in-context 43% vs language 53% at 1,000 h inverts to **66% vs 9%** on unseen tasks at 100,000 h, "one in-context demonstration ≈ 380 post-training examples." Whether in-context learning must be *designed in* (S1: episodic pretraining as the outer loop) or *emerges* (GEN-1.5: no meta-learning loop, random spans) is the [in-context page](in-context-robot-learning.md)'s open question; neither ablates.

**Test-time adaptation.** Control is unusually friendly to it because *each execution produces the next observation, which is a self-supervised prediction target*: [AdaJEPA](../../sources/adajepa-paper.md) needs one gradient step per replanning step, ~0.3 s. Its limit is a rule worth keeping: adaptation "repairs a model whose predictions are miscalibrated; it cannot repair observations that no longer carry the needed information." And its trap, from the [TTA page](test-time-adaptation.md): the prediction error TTA descends is the same signal [runtime failure detection](../robotics/runtime-failure-detection.md) uses as an *alarm*, and nothing in the signal says which reading is right — a TTA system will adapt toward a transition that was anomalous because the policy erred, and an adapted model cannot evaluate the episode it adapted to.

**The forgetting argument appears here as a capability trade-off.** [GEN-1.5](../../sources/generalist-gen-1-5-blog.md): ten gradient steps move the weights by **<0.15%** and take a task from 59% to 83%, and *improvisation strengthens as adaptation steps decrease* because lightly adapted models stay near their priors. The design principle that follows — adapt as little as you can get away with — is the mildest form of forgetting-avoidance, and it cuts against the emergence framing: if 0.15% of weight motion does it, in-context learning is buying convenience, not capability the weights lacked.

## C. Updating the weights, and what forgets

**The loop exists at hardware scale.** [HIL-SERL](../../sources/hil-serl-paper.md): human interventions go to both the demo and RL buffers, policy transitions only to the RL buffer, and the **intervention rate trending to zero** is the convergence signal — 100% success in 1–2.5 h. [RLPD](../../sources/rlpd-paper.md)'s symmetric 50/50 offline/online batch is the replay mechanism underneath. At VLA scale, [RECAP](../../sources/pistar06-paper.md) iterates deploy → autonomous rollouts + gated corrections + sparse outcomes → distributional value → advantage-conditioned policy, and on the hardest tasks more than doubles throughput and halves failure: 13 h of continuous espresso, 2+ h folding novel laundry in a new home. The practitioner's version — success replay and semi-success replay under visual randomization — is on [RL for flow-matching VLAs](rl-for-flow-matching-vlas.md). The ladder is on [real-world robot RL](real-world-robot-rl.md).

**A closed flywheel with a plateau.** [Scanford](../../sources/robot-powered-data-flywheels-paper.md): ten days in a library, self-labeled from the catalog, book identification **32.4% → 71.8%**, and gains **plateau at ~1.5 h / ~1,352 images** — the first place the wiki has a number for how quickly deployment data stops paying.

**The documented forgetting case.** [GR00T N1](../../sources/groot-n1-paper.md) §4.5: the pretrained checkpoint spontaneously performs an unseen left-to-right handover; the **post-trained checkpoint loses it** because post-training data was right-hand-only. One example, one direction, no metric — but it is the wiki's only ingested instance of the failure the term names, and it happened in a vendor's own post-training.

**What the wiki has instead of a forgetting-prevention method** is three architectural evasions:

- **Rehearsal.** [Molmo2-ER](../../entities/molmo2-er.md)'s *specialize-then-rehearse* — 20K steps on the embodied corpus, then 1.5K steps interleaving the original multimodal mix at p = 0.5 — versus Unitree's single-stage co-training, which left [UnifoLM-ER-1](../../sources/unifolm-wla-1-project-page.md) **below its own base** on MME, MMMU, RealWorldQA and VSI-Bench. Rehearsal appears to be worth its cost; nobody has run both recipes on one base ([embodied-reasoning VLMs](embodied-reasoning-vlms.md)).
- **Insulation.** [Knowledge Insulation](knowledge-insulation.md) blocks action-expert gradients from the VLM backbone (freezing instead gives ~0%). It is forgetting-avoidance *by architecture*, for one specific kind of forgetting — and [MolmoAct2](../../sources/molmoact2-paper.md) drops it at embodiment fine-tuning, "no consistent gain from detaching at that stage."
- **Low-rank adapters.** [LoRA](low-rank-adaptation.md) confines the update to a subspace; the paper's own analysis says ΔW *amplifies* features the base already had (≈21.5×) rather than acquiring new ones — which is why adapters forget little and also why they cannot learn much that is new.

None of these is a method for a robot that must keep learning **in the weights, for months, across tasks it did not see in pretraining.** That is the gap.

## Where "forgetting" is a different bug

[WorldTrace](../../entities/worldtrace.md) ([belief states](../world-models/belief-states-and-mixed-states.md)): much of the forgetting in long video-world-model rollouts is not compression but **addressing** — rotary-position offsets drift, and frames still in the KV cache become unreachable. "A repairable bug sitting on top of an unrepairable limit." Worth knowing before attributing a rollout's amnesia to capacity.

## What this page cannot say

- **No primary on preventing weight-level forgetting.** EWC (Kirkpatrick et al. 2017), replay-based continual learning, and the current continual-robot-learning survey are all uningested. LIBERO was designed as a *Lifelong* Robot Learning Benchmark and the wiki uses it only as a success-rate table; the original Liu et al. 2023 paper is not ingested ([LIBERO](../../entities/libero.md)).
- **No deployed lifelong loop has been verified by a third party.** RECAP and HIL-SERL run for hours; Scanford for ten days; Waddle claims always-on; ASPIRE disclaims it.
- **SELFI and RAIL's "lifelong improvement in the wild"** — real-world RL fine-tuning of navigation models — are cited by [MBRA](../../sources/mbra-paper.md) and not ingested.

## Related concepts

- [Test-time adaptation](test-time-adaptation.md), [in-context robot learning](in-context-robot-learning.md), [real-world robot RL](real-world-robot-rl.md), [RL for flow-matching VLAs](rl-for-flow-matching-vlas.md), [Knowledge Insulation](knowledge-insulation.md), [LoRA](low-rank-adaptation.md), [synthetic data flywheel](synthetic-data-flywheel.md), [code as policy](../agents/code-as-policy.md), [runtime failure detection](../robotics/runtime-failure-detection.md), [embodied-reasoning VLMs](embodied-reasoning-vlms.md).
- [Ten open questions](../../syntheses/world-models/open-questions-and-research-direction.md) — question #3.

## Mentioned in

> [!note] Curated list — this page was assembled from ~80 pages that use the terms; the ones below supplied its claims.

- [ASPIRE](../../sources/aspire-paper.md), [Voyager](../../sources/voyager-paper.md), [CaP-X](../../sources/cap-x-paper.md) — skill libraries.
- [LocoFormer](../../sources/locoformer-paper.md), [Skild S1](../../sources/skild-s1-blog.md), [GEN-1.5](../../sources/generalist-gen-1-5-blog.md), [AdaJEPA](../../sources/adajepa-paper.md) — adaptation without permanent change.
- [π*0.6 / RECAP](../../sources/pistar06-paper.md), [HIL-SERL](../../sources/hil-serl-paper.md), [RLPD](../../sources/rlpd-paper.md), [Scanford](../../sources/robot-powered-data-flywheels-paper.md), [GR00T N1](../../sources/groot-n1-paper.md) — weight updates and the forgetting case.
- [MolmoAct2](../../sources/molmoact2-paper.md), [UnifoLM-WLA-1.0](../../sources/unifolm-wla-1-project-page.md), [Knowledge Insulation](../../sources/knowledge-insulation-paper.md), [LoRA](../../sources/lora-paper.md) — the architectural evasions.
- [Hassabis at Davos](../../sources/wef-davos-2026-the-day-after-agi.md) — "world models, continual learning — these are the things that will need to be cracked."
- [RoboTTT](../../sources/robottt-paper.md) — within-episode improvement with no persistent weight change (fast weights discarded after each rollout); the authors name RL on task success as the step toward persistent improvement.

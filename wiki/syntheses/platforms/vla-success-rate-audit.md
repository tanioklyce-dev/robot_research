---
title: Success-rate audit — which of this wiki's policy comparisons survive their sample sizes
type: synthesis
created: 2026-07-27
updated: 2026-07-27
tags: [evaluation, statistics, clopper-pearson, vla, libero, benchmark, audit, reproducibility, methodology]
---

# Success-rate audit — which of this wiki's policy comparisons survive their sample sizes

[NVIDIA SRL's RoboLab methodology](../../sources/nvidia-robolab-evaluation-blog.md) makes a claim that indicts most published robot-policy numbers, including the ones this wiki repeats: a **±2 pp** confidence band needs ≈**1,030 rollouts**, and typical evaluations run ~**70**. This page applies that standard to the wiki's own tables and marks each headline comparison **survives / tie / unknown-N**.

The short version: **the entire top of the wiki's LIBERO table is a single statistical tie**, and the wiki has been presenting it as a ranking. Large gaps — the ones that motivated the wiki's actual conclusions — hold up fine.

## Reproducing the bar (and a correction to how it's usually quoted)

Clopper-Pearson exact binomial intervals, 95%, sample size needed for a **±2 pp half-width**:

| True success rate | n for ±2 pp |
|---|---|
| 50% | ≈ 2,450 |
| 70% | ≈ 2,130 |
| 80% | ≈ 1,680 |
| **90%** | **≈ 1,030** ← NVIDIA's figure |
| 95% | ≈ 610 |
| 97% | ≈ 440 |

**The 1,030 figure is the n required at a ~90% success rate.** It is not a universal constant — the bar is *rate-dependent*, and it gets **worse** as performance drops toward 50%, which is exactly where real-world manipulation numbers live. A policy at 50.1% real-world success needs **~2,450 rollouts** for ±2 pp, not 1,030. Quoting "1,030" as the standard is therefore generous to the mid-range results that need it most.

### Minimum detectable gap between two policies

80% power, α = 0.05, two-proportion test, per-arm n:

| n per arm | around 50% | around 85% | around 95% |
|---:|---:|---:|---:|
| 10 | not detectable | not detectable | not detectable |
| 20 | 40.5 pp | not detectable | not detectable |
| 50 | 27.0 pp | not detectable | not detectable |
| 70 | 23.1 pp | 13.2 pp | not detectable |
| 100 | 19.5 pp | 11.5 pp | not detectable |
| 200 | 13.9 pp | 8.7 pp | 4.6 pp |
| 500 | 8.9 pp | 5.8 pp | 3.3 pp |
| 1,030 | 6.2 pp | 4.2 pp | 2.4 pp |

**At the 20–50 rollouts most real-robot evaluations use, nothing under ~27 pp is detectable.**

## The audit

### A. The LIBERO table — the top is one tie

LIBERO averages span four suites (Spatial / Object / Goal / Long) of **10 tasks each**, evaluated at **50 episodes per task** — **confirmed 2026-07-27** via [LIBERO-PRO](../../sources/libero-pro-paper.md) (*"consistent with the original LIBERO protocol, we set the number of evaluation episodes to 50 per task"*). So **n = 500 per suite** and **n = 2,000 for a four-suite average**. These were assumptions when this page was written; they are now the actual protocol, and every verdict below is grounded rather than provisional.

| Comparison | Gap | n=500 | n=2,000 | Verdict |
|---|---:|---|---|---|
| MolmoAct2-Think 98.1 vs MolmoAct2 97.2 | 0.9 pp | p=0.35 | p=0.060 | **TIE** |
| MolmoAct2 97.2 vs OpenVLA-OFT 97.1 | 0.1 pp | p=0.92 | p=0.85 | **TIE** |
| MolmoAct2 97.2 vs GR00T N1.7 97.0 | 0.2 pp | p=0.85 | p=0.71 | **TIE** |
| MolmoAct2 97.2 vs π0.5 96.9 | 0.3 pp | p=0.78 | p=0.58 | **TIE** |
| MolmoAct2 97.2 vs GR00T-in-LeRobot 96.5 | 0.7 pp | p=0.53 | p=0.21 | **TIE** |
| VLA-0 94.7 vs π0.5-KI 94.3 | 0.4 pp | p=0.78 | p=0.58 | **TIE** |
| VLA-0 94.7 vs π0 94.2 | 0.5 pp | p=0.73 | p=0.49 | **TIE** |
| MolmoAct2 97.2 vs VLA-0 94.7 | 2.5 pp | p=0.044 | p=0.0001 | **survives** |
| MolmoAct2 97.2 vs MolmoAct 86.8 | 10.4 pp | p<0.0001 | p<0.0001 | **survives** |

**Minimum separating gap at ~97%: >1.8 pp (n=500) or >1.0 pp (n=2,000).** The cluster from 96.5 to 98.1 spans 1.6 pp and contains at least six models.

> [!warning] A larger problem than the tie: LIBERO may not measure generalization at all
> [LIBERO-PRO](../../sources/libero-pro-paper.md) reports models scoring **>90% on standard LIBERO collapsing to 0.0%** under perturbation of objects, initial states, instructions, or environments — because the **evaluation tasks are the training tasks**, differing only by visually imperceptible initial-state changes. Models keep grasping after the target object is swapped, and emit unchanged actions under corrupted instructions.
>
> **A statistical tie among numbers that may not measure generalization is a second-order finding.** This audit's section-A verdicts stand, but the more consequential fact is that the whole 94–98 band may be measuring recall. Tested models were OpenVLA, π0, π0.5; **MolmoAct2, OpenVLA-OFT, and GR00T N1.7 — the top of this table — were not tested.**

> [!warning] "Top of the wiki's LIBERO table" is not a supportable phrase
> MolmoAct2 (97.2), MolmoAct2-Think (98.1), OpenVLA-OFT (97.1), GR00T N1.7 (97.0), and π0.5 (96.9) are **not distinguishable from one another**. The wiki calls MolmoAct2 "top of the wiki's table" in at least three places. What the data support is a **top tier**, not an ordering within it. The same applies to the VLA-0 / π0.5-KI / π0 cluster at 94.2–94.7.
>
> This also **resolves an open question the wiki has been carrying**: *"Is MolmoAct2-Think's ~4× latency penalty (12.7 vs 55.8 Hz) worth its +0.9 LIBERO gain?"* The +0.9 is not statistically established (p=0.35 at n=500, p=0.06 at n=2,000). You are paying a measured 4× latency cost for an unmeasured gain.

### B. Real-world claims — the big ones hold

| Claim | N | Verdict |
|---|---|---|
| **MolmoAct2 real YAM 50.1%, +15 pp over OpenVLA-OFT** (8 tasks × 50 trials) | 400 aggregate | **survives** (p=0.00002). CI on 50.1% is [45.0, 55.0] |
| — the same +15 pp *within a single task* | 50 | **TIE** (p=0.13) |
| — **"wins 7 of 8 tasks"** | 8 | **not significant** — sign test p=0.070 |
| **MolmoAct2 real DROID 87.1%, +38.7 pp over runner-up** | ~50 assumed | **survives** (p=0.00003) |
| **GR00T N1.5 on G1: 44.0% → 98.8% after post-training** | ~50 assumed | **survives** (p<10⁻⁸) |
| **SmolVLA 78.3 vs π0 61.7 (+16.6 pp) real SO-100** | **unknown** | **unknown-N** — at n=50 it would be a TIE (p=0.070) |
| **Cosmos3-Nano-Policy-DROID 39.7 vs π0.5 28.1 on RoboLab-120** | 120 tasks, rollouts/task unstated | **unknown-N** — at 1 rollout/task it is a TIE (p=0.058) |
| **Anthropic LLM direct control: 5.5% vs 0%** (LIBERO-40, 40×5) | 200 | **survives** (p=0.0008) |
| **RUM 90% across 25 novel environments** | 250 | CI [85.6, 93.4] — the headline holds; the per-task ordering (68/76/76/80/84) does **not** separate |

> [!note] The irony worth recording
> **NVIDIA's own headline RoboLab comparison may not clear NVIDIA's own bar.** Cosmos3-Nano-Policy-DROID at 39.7% vs π0.5 at 28.1% is an 11.6 pp gap on a 120-task suite; if that is one rollout per task, p=0.058 — a tie. The rollouts-per-task figure is not published, so this is *unknown-N*, not *refuted*. But the paper proposing the 1,030-rollout standard is adjacent to a comparison that needs its own medicine.

### C. What the wiki already knew and didn't apply

The [TRI LBM paper](../../sources/tri-lbm-paper.md) ingest recorded this two months ago:

> *"Sobering calibration for the whole field: with 50 rollouts, the CI width is generally 20–30% absolute success rate — i.e. most robot-learning papers' eval sample sizes cannot statistically distinguish the methods they rank."*

That is the same finding, from a different source, sitting on a source page while the entity and synthesis pages went on ranking policies by fractions of a point. TRI also ran **4,200+ rollouts** (≥50/real task, ≥200/sim task) — one of the few evaluations in this wiki built to this standard, which is presumably why it noticed.

**The failure was not analytical, it was organizational**: the caveat lived on one page and the claims lived on others, with no link between them.

## The other way out: stop measuring absolute rates

This page's whole framing — how many rollouts to pin a success rate — has an alternative that [RoboArena](../../sources/roboarena-paper.md) (CoRL 2025) demonstrates works better. Instead of estimating absolute rates, run **double-blind pairwise A/B comparisons** between policies on freely-chosen tasks and fit an extended **Bradley-Terry** model (per-policy ability, per-task difficulty, policy×task offsets).

The result is the empirical case against the protocol this page audits:

| | Conventional centralized success-rate eval | RoboArena pairwise |
|---|---|---|
| Pearson r with oracle ranking | **≈ 0.60** | **≈ 0.95** |
| Comparisons to converge | — | **~100** |

**A pairwise preference carries more information per episode than a binary success flag**, because both policies face the identical scene and scene difficulty cancels — the standard argument for paired designs. That is how ~100 comparisons can outrank an evaluation with far more rollouts, and it is why the ~1,030-rollout bar is not the only available fix.

**The cost is magnitude.** RoboArena yields ordering, not "72% success" — and for deployment decisions magnitude is often the thing you need. The two lines are complements: [RoboLab](../../sources/nvidia-robolab-evaluation-blog.md) says *collect far more rollouts*, RoboArena says *measure something else*.

## What this changes

**Survives unchanged.** Every conclusion the wiki actually reasons from rests on a large gap: MolmoAct2's real-world DROID lead (+38.7), post-training gains on G1 (44→98.8), the generational MolmoAct → MolmoAct2 jump (+10.4), OpenVLA-OFT's 76.5 → 97.1 recipe effect (+20.6), and the LLM-vs-VLA chasm (5.5% vs ~97%). None of the wiki's structural claims depended on a sub-2 pp difference.

**Must be reworded.** Any phrase asserting a *rank* inside the 94–98 LIBERO band. "Top of the wiki's table" becomes "in the top tier, statistically tied with X, Y, Z."

**Needs an N before it can be used.** SmolVLA vs π0 (+16.6), the Cosmos/RoboLab comparison, and every real-world number where the source's rollout count was never recorded. Going forward, **record N at ingest** — this audit was expensive mostly because trial counts were missing from pages that quoted the success rates.

> [!warning] These p-values are optimistic
> The two-proportion test assumes independent Bernoulli trials. Real rollouts are **clustered within tasks** and tasks differ systematically in difficulty, so effective sample size is smaller than nominal and true intervals are **wider** than computed here. Every "TIE" verdict is therefore safe; every "survives" verdict is the weaker claim than it appears. Treat this page as a **lower bound on the uncertainty**.

## Method

Clopper-Pearson exact binomial intervals (95%) for single-rate CIs; two-proportion z-test (80% power, α=0.05, two-sided) for pairwise gaps; exact binomial sign test for "wins k of n tasks." Sample sizes are taken from the wiki's source pages where recorded, and **flagged as assumptions where not** — the LIBERO protocol (500/suite) and several real-world evaluations (~50) are assumed, not sourced. Computed at ingest time; not reproducible from the wiki alone.

## Related
- [Robot policy evaluation](../../concepts/robotics/robot-policy-evaluation.md) — the concept; where the bar comes from.
- [RoboArena](../../entities/roboarena.md) / [paper](../../sources/roboarena-paper.md) — the pairwise-preference alternative; r≈0.95 vs 0.60.
- [LIBERO-PRO](../../sources/libero-pro-paper.md) — the memorization critique that outranks this page's finding in importance.
- [How to Evaluate General-Purpose Robot Policies](../../sources/nvidia-robolab-evaluation-blog.md) — the source.
- [VLA deployability landscape](vla-deployability-landscape.md) — the scored table this audit qualifies.
- [LIBERO](../../entities/libero.md) — where the tied numbers live.
- [TRI LBM paper](../../sources/tri-lbm-paper.md) — the wiki's earlier, unapplied version of this warning.
- [Control-rate ladder](control-rate-ladder.md) — the sibling "put the numbers on one axis" page; latency rather than success.

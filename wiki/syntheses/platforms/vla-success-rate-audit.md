---
title: Success-rate audit — which of this wiki's policy comparisons survive their sample sizes
type: synthesis
created: 2026-07-27
updated: 2026-08-30
tags: [evaluation, statistics, clopper-pearson, vla, libero, benchmark, audit, reproducibility, methodology, code-as-policy]
---

# Success-rate audit — which of this wiki's policy comparisons survive their sample sizes

[NVIDIA SRL's RoboLab methodology](../../sources/nvidia-robolab-evaluation-blog.md) makes a claim that indicts most published robot-policy numbers, including the ones this wiki repeats: a **±2 pp** confidence band needs ≈**1,030 rollouts**, and typical evaluations run ~**70**. This page applies that standard to the wiki's own tables and marks each headline comparison **survives / tie / unknown-N**.

The short version: **the entire top of the wiki's LIBERO table is a single statistical tie**, and the wiki has been presenting it as a ranking. Large gaps — the ones that motivated the wiki's actual conclusions — hold up fine.


> [!warning] A 1.2-point tier with no reported seed variance is a known failure pattern
> [Locatello et al. 2019](../../sources/locatello2019-challenging-common-assumptions-disentanglement.md) trained **>12,000 models** across the disentanglement literature and found that **random seeds and hyperparameters mattered more than the model choice** — *"a good run with a bad hyperparameter can beat a bad run with a good hyperparameter"* — and that good runs **could not be identified without ground-truth labels**. The field had accumulated years of published improvements that were substantially seed variance plus model selection quietly consuming the test signal.
>
> This audit's tier has the same shape: **ten models inside 1.2 percentage points**, and **nothing in that literature reports seed spread**. The directly reproducible check is to train one architecture at `N` seeds on [LIBERO](../../entities/libero.md) and compare the within-architecture spread against the between-architecture gap. If they overlap, the ranking is noise.
>
> A second, cheaper probe from the language side: [Verbalized Eval Awareness](../../sources/goodfire-verbalized-eval-awareness.md) found that **paraphrasing benchmark prompts cut measured safety scores**, because part of the score was an artifact of phrasing. The robot analogue — re-render the same tasks with different textures, lighting, distractor placement and instruction wording — is far cheaper than building [LIBERO-PRO](../../sources/libero-pro-paper.md), and **a tier that reorders under paraphrase was never a tier.**

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
| **[TurboVLA](../../entities/turbovla.md) 97.7 vs π0.5 96.9** | 0.8 pp | — | p=0.12 | **TIE** |
| TurboVLA 97.7 vs OpenVLA-OFT 97.1 | 0.6 pp | — | p=0.23 | **TIE** |
| TurboVLA 97.7 vs VLA-Adapter 97.3 | 0.4 pp | — | p=0.42 | **TIE** |
| TurboVLA 97.7 vs [Evo-1](../../entities/evo-1.md) 94.8 | 2.9 pp | — | p<0.001 | **survives** |
| TurboVLA 97.7 vs SmolVLA 88.8 | 8.9 pp | — | p<0.0001 | **survives** |

**Minimum separating gap at ~97%: >1.8 pp (n=500) or >1.0 pp (n=2,000).** The cluster from 96.5 to 98.1 spans 1.6 pp and contained at least six models when this audit ran.

> [!note] The cluster keeps growing — updated 2026-08-13
> **Now ten models, spanning 1.2 pp**: MolmoAct2-Think 98.1, [X-VLA](../../entities/x-vla.md) 98.1, [TurboVLA](../../entities/turbovla.md) 97.7, CogVLA 97.4, VLA-Adapter 97.3, MolmoAct2 97.2, [VLA-JEPA](../../entities/vla-jepa.md) 97.2, OpenVLA-OFT 97.1, GR00T N1.7 97.0, π0.5 96.9. Every addition since this audit has landed *inside* the tie, which is itself the finding: **LIBERO stopped discriminating some time before the field stopped reporting it.** The current roster lives on [LIBERO](../../entities/libero.md); this line is the historical record of when it was six.
>
> The one place the tie now breaks is **LIBERO-Long**, where headroom survives: X-VLA 97.6 vs MolmoAct2-Think 95.4, OpenVLA-OFT 94.5, π0 85.2. Report Long separately from the four-suite average.

> [!note] The tie is doing useful work for once
> TurboVLA's whole argument is *"matching much larger policies at 6% of the parameters."* A tie at the top is exactly the claim — and its efficiency axis (0.2 B vs 3.4 B, 0.9 GB vs 12.8 GB, 31.2 ms vs 93.6 ms) consists of **engineering measurements, not sampled proportions**, so it doesn't need this audit at all. The paper's abstract says "matching or outperforming"; only the first word survives, and only the first word was needed.

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
| **[TurboVLA](../../entities/turbovla.md) [RoboTwin 2.0](../../entities/robotwin.md) 60.2 vs π0.5 57.0** (50 bimanual tasks × 100) | **5,000** | **survives** (p=0.0012) — see note below |
| — TurboVLA RoboTwin 60.2 vs StarVLA-α 50.3 | 5,000 | **survives** (p<0.0001) |
| **TurboVLA real [AgileX Piper](../../entities/agilex-piper.md), 4 tasks vs π0.5** | 40/task | **not significant** — at n=40 near 85–90%, nothing under ~17 pp is detectable; 4-of-4 sign test is p=0.125 regardless |

> [!note] The irony worth recording
> **NVIDIA's own headline RoboLab comparison may not clear NVIDIA's own bar.** Cosmos3-Nano-Policy-DROID at 39.7% vs π0.5 at 28.1% is an 11.6 pp gap on a 120-task suite; if that is one rollout per task, p=0.058 — a tie. The rollouts-per-task figure is not published, so this is *unknown-N*, not *refuted*. But the paper proposing the 1,030-rollout standard is adjacent to a comparison that needs its own medicine.

### C. What the wiki already knew and didn't apply

The [TRI LBM paper](../../sources/tri-lbm-paper.md) ingest recorded this two months ago:

> *"Sobering calibration for the whole field: with 50 rollouts, the CI width is generally 20–30% absolute success rate — i.e. most robot-learning papers' eval sample sizes cannot statistically distinguish the methods they rank."*

That is the same finding, from a different source, sitting on a source page while the entity and synthesis pages went on ranking policies by fractions of a point. TRI also ran **4,200+ rollouts** (≥50/real task, ≥200/sim task) — one of the few evaluations in this wiki built to this standard, which is presumably why it noticed.

**The failure was not analytical, it was organizational**: the caveat lived on one page and the claims lived on others, with no link between them.

### D. The code-as-policy results (added 2026-08-03)

[CaP-X](../../sources/cap-x-paper.md) and [ASPIRE](../../sources/aspire-paper.md) are the first sources ingested *after* this audit was written, so they are the first to be checked at ingest rather than retroactively. **Both disclose protocol better than the wiki's median**, which makes the verdicts unusually clean.

| Claim | N | Verdict |
|---|---|---|
| **ASPIRE vs. best baseline on LIBERO-Pro: +77 / +41.5 / +42.5 pp** | 500/suite/axis (10 tasks × 50 held-out seeds) | **survives** overwhelmingly — these are the largest gaps in the wiki outside the LLM-vs-VLA chasm |
| **ASPIRE Robosuite bimanual handover 20% → 92%** | 100/task | **survives** (p < 10⁻¹⁵) |
| **ASPIRE BEHAVIOR radio task 56% → 88%** | 25 | **survives, barely** (Fisher exact p = 0.025) — at n=25 this 32 pp gap is close to the detection floor |
| **ASPIRE zero-shot LIBERO-Pro Long 31% vs 4%** | 500/axis | **survives** (p < 10⁻²⁰) |
| **ASPIRE ablation: 14% → 62% (engine), → 72% (+evo)** | 500/suite/axis | engine step **survives** (p < 10⁻¹⁰); the **+10 pp evo step also survives** (p = 0.0008) |
| **ASPIRE real-robot drawer 0/20 → 11/20 with skill transfer** | 20 | **survives** (Fisher exact p = 0.00015) — a 0-vs-11 split is detectable even at n=20 |
| **ASPIRE real-robot soda can 13/20 → 19/20** | 20 | **survives, marginally** (Fisher exact p = 0.044) |
| **CaP-Agent0 ablation: 24 → 55 → 59 → 66 → 68** | 700 (7 tasks × 100) | 24→55 and 59→66 **survive** (p < 10⁻⁴, p = 0.007); the **+4 pp (55→59, p = 0.13) and +2 pp (66→68, p = 0.43) steps do not separate** — the skill library and the third parallel model are each individually unproven |
| **CaP-Agent0 vs π0.5 on LIBERO-PRO** (e.g. 0.18 vs 0.01 Task) | **unstated** | **unknown-N** — Table 2 gives no trials/task. The Task-axis gaps (~17 pp against ~0) would survive at almost any n; the Pos-axis gaps (0.22 vs 0.17) would not |
| **CaP-RL: Qwen 7B 24% → 84% real cube lift** | 25 | **survives** (p < 10⁻⁴) |
| **CaP-X "no model matches human 88.5%"** | 100/task/tier | directional claim across 12 models; **survives** for the large gaps, not asserted as a ranking |

> [!note] Two things this thread does better than the wiki's VLA sources
> **1. Disjoint debug/eval seeds.** ASPIRE learns on seeds 51–65 and evaluates on 1–50. Almost nothing else in this wiki states a train/eval split at the *seed* level.
> **2. One program per task.** ASPIRE generates a single program and runs it across all held-out seeds, while its baseline (CaP-Agent0) regenerates per seed with retries. **The protocol handicaps the paper's own method** — the opposite of the usual direction, and it means these gaps are if anything understated.

> [!warning] The measurement this thread is missing is cost, not N
> Every number above has a sample size. **None has a compute cost attached.** CaP-Agent0 issues up to 9 parallel frontier-model queries per turn; ASPIRE reports **81.67M–334.9M tokens for a single real-robot task**. Comparing that to a VLA's single forward pass on success rate alone is an unequal-compute comparison that no paper in this thread acknowledges. The wiki should **record compute at ingest** the way it now records N — this is the same organizational failure as section C, one benchmark cycle later.

### E. TurboVLA (added 2026-08-04) — the paper headlined its tie and buried its win

[TurboVLA](../../sources/turbovla-paper.md) is the clearest case yet of the pathology this page exists to catch, and it runs in an unexpected direction. The paper leads with **LIBERO 97.7%** — a tie with three other models. Its **[RoboTwin 2.0](../../entities/robotwin.md)** result, presented second and in a smaller table, is the one that survives:

| | LIBERO | RoboTwin 2.0 |
|---|---|---|
| Gap over π0.5 | 0.8 pp | 3.2 pp |
| n per arm | 2,000 | **5,000** |
| Base rate | ~97% | ~58% |
| Verdict | **TIE** (p=0.12) | **survives** (p=0.0012) |

The smaller gap separates and the larger one doesn't, for three compounding reasons: **2.5× the sample**, a base rate near 50–60% where a proportion's variance is maximal *relative to the ceiling* (at 97% everything is crushed against the top and there is almost nothing left to separate), and a benchmark with genuine headroom. RoboTwin is also the harder setting — 50 bimanual tasks under one joint policy, against a π0.5 that *has* embodied pretraining where TurboVLA has none.

> [!note] The generalizable lesson: prefer benchmarks with headroom
> A benchmark whose leaders sit at 97% cannot separate them without ~2,000 rollouts per arm, and even then only past ~1.0 pp. A benchmark whose leaders sit at 58% separates 3 pp at the same-ish effort. **LIBERO's saturation is itself a measurement problem**, independent of the [LIBERO-PRO](../../sources/libero-pro-paper.md) memorization critique — and the two compound: a saturated benchmark that may also be measuring recall is the worst of both. The wiki should weight RoboTwin-2.0-class and real-world numbers above LIBERO ones when a source reports both.

**Compute, per this page's own standing request** (section D): TurboVLA trained on **four RTX 4090s**, 80 k steps for the LIBERO result, **no embodied pretraining**. That is the smallest disclosed training footprint attached to any top-tier LIBERO number in this wiki. The efficiency claims (0.2 B params, 0.9 GB VRAM, 31.2 ms) are direct measurements, need no significance test, and — unusually — the authors **re-measured every competitor themselves** on one RTX 4090 at batch size 1 rather than quoting original papers.

## Addendum (2026-08-13): two protocols confirmed, and a floor case

**[RoboTwin 2.0](../../entities/robotwin.md)'s protocol is now confirmed from its [primary source](../../sources/robotwin2-paper.md)**: 50 clean demos for training, **100 rollouts per task × 50 tasks = 5,000 per model per condition**, Aloha-AgileX, single-task finetuning. This audit assumed roughly that and could not verify it. At n=5,000 and a ~40% base rate, **~2 pp separates** — so RoboTwin comparisons carry real information where [LIBERO](../../entities/libero.md)'s top cluster (now ten models inside 1.2 pp) carries none. Cross-paper consistency supports it: π0's 46.4 Easy is identical in the RoboTwin paper, [TurboVLA](../../entities/turbovla.md), and [X-VLA](../../entities/x-vla.md).

**The floor case: [RoboMIND](../../entities/robomind.md) reports every result at n = 10.** *"Each model was tested ten times."* A 95% CI at n=10 spans roughly ±30 points per cell, so none of its ACT-vs-DP-vs-BAKU or per-embodiment orderings is a measurement. Recorded not as a criticism of the paper — dataset papers need existence proofs, not rankings — but because **its tables are exactly the kind that get cited as comparisons**. The rule this audit keeps arriving at, restated: *record N at ingest, and check it before quoting an ordering.*

## Addendum (2026-08-13): a fourth independent instance, from outside robotics

**"On the Limits of Pseudo Ground Truth in Visual Camera Re-Localisation"** (Brachmann, Humenberger, Rother, Sattler, ICCV 2021 — surfaced via [Niantic Spatial's publication list](../../sources/niantic-spatial-research.md)) makes the same class of argument in **visual relocalization**: benchmarks score against "ground truth" poses that were themselves produced by an algorithm, so the leaderboard partly measures **agreement with whichever reference method generated the labels**.

That gives four independent instances of *the instrument is not measuring what the field thinks it measures*:

| Instance | Subfield | The defect |
|---|---|---|
| [LIBERO-PRO](../../sources/libero-pro-paper.md) | VLA manipulation | evaluation tasks are the training tasks; >90% collapses to 0.0% under perturbation |
| [VP²](../../sources/vp2-paper.md) | video prediction | perceptual metrics mis-rank predictors for control, **sign-dependent** |
| **This audit** | VLA benchmarks | the top of the table is one statistical tie |
| **[Pseudo Ground Truth](../../sources/pseudo-ground-truth-paper.md)** | visual relocalization | the ground truth is itself an algorithm's output — swap the reference and **Active Search goes last → first, +29.8 pts** |

> [!note] The four do not cite each other
> Different subfields, ~5 years apart, same structural finding — and the robotics evaluation literature appears not to know about the localization one. **Now ingested** ([source](../../sources/pseudo-ground-truth-paper.md)): it is the earliest of the four and the only one where the **labels** rather than the tasks, metrics, or sample sizes are the problem, and its authors call the issue *"fundamental"* with no solution.
>
> **Two things it contributes back to this thread.** Its remedy — *"task-specific evaluation… in the context of AR, robotic navigation"* — is the same move [VP²](../../sources/vp2-paper.md) makes independently two years later. And its recommendation to prefer the method that is *"not best under any pGT but good under all"* is the same robustness-over-peak preference [RoboTwin 2.0](../../entities/robotwin.md) arrives at for VLA pretraining.
>
> **The open transposition**: [LIBERO](../../entities/libero.md)'s ground truth is simulator task success, not algorithm-generated — but [RoboTwin 2.0](../../entities/robotwin.md)'s expert demonstrations **are** produced by an MLLM-plus-planner pipeline, and policies are scored on tasks that pipeline could solve. **Nobody has asked whether synthetic-demonstration benchmarks have a pseudo-ground-truth problem.**

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

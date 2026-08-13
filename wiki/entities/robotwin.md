---
title: RoboTwin 2.0
type: entity
subtype: benchmark
created: 2026-08-04
updated: 2026-08-13
sources: 5
tags: [robotwin, benchmark, bimanual, manipulation, domain-randomization, data-generation, simulation, robotwin-od, mllm-code-generation, embodiment-aware-grasping, sim-to-real]
---

**RoboTwin 2.0** — a scalable **bimanual** manipulation *data generator* that also ships a benchmark (Chen, Chen, Chen et al., arXiv 2506.18088, Jun 2025 / v2 Aug 2025). **50 language-conditioned dual-arm tasks across 5 embodiments**, **100,000+ pre-collected trajectories**, and the **RoboTwin-OD** asset library (731 objects / 147 categories). Ships both a *clean* ("Easy") setting and a domain-randomized ("Hard") one. **Primary source now ingested**: [RoboTwin 2.0 paper](../sources/robotwin2-paper.md).

> [!note] Venue confirmed
> The arXiv v2 PDF carries no venue line, but the [official repository README](https://github.com/RoboTwin-Platform/RoboTwin) states **"RoboTwin 2.0 (*ICML 2026*)"** (verified 2026-08-13). The page's original ICML 2026 attribution stands.

## Position in this wiki

The dual-arm counterpart to [LIBERO](libero.md), and a useful corrective to it: where LIBERO's four suites are single-arm and have drawn the [memorization critique](../sources/libero-pro-paper.md), RoboTwin 2.0 is harder (success rates sit near 50–60%, not 97%) and its randomized-scene mode is a built-in generalization test rather than a separate perturbation paper.

First appears here via the [TurboVLA paper](../sources/turbovla-paper.md), which reports **100 rollouts per task across all 50 tasks (n = 5,000)** on the clean setting:

| Model | Params (B) | Latency (ms) | Avg success |
|---|---:|---:|---:|
| [TurboVLA](turbovla.md) (multi-task) | 0.4 | 43.4 | **60.2%** |
| [π0.5](pi-zero-5.md) (multi-task) | 3.4 | 95.6 | 57.0% |
| DP3 (per-task) | 0.3 | 78.4 | 55.2% |
| UP-VLA (multi-task) | 1.6 | 74.3 | 52.9% |
| StarVLA-α (multi-task) | 3.8 | 74.9 | 50.3% |
| [π0](pi-zero.md) (per-task) | 3.2 | 87.6 | 46.4% |
| RDT (per-task) | 1.7 | 204.8 | 34.5% |
| [ACT](act.md) (per-task) | 0.1 | 20.4 | 29.7% |
| [Diffusion Policy](diffusion-policy.md) (per-task) | 0.1 | 794.1 | 28.0% |

> [!note] Why this table is more informative than the LIBERO one
> At n = 5,000 and a ~55% base rate, gaps of ~3 pp **separate** ([audit](../syntheses/platforms/vla-success-rate-audit.md)) — TurboVLA vs π0.5 gives p = 0.0012. The equivalent 0.8 pp gap at the top of LIBERO does not. Benchmarks that leave headroom are cheaper to draw conclusions from.
>
> The table also distinguishes **per-task** (one policy per task) from **multi-task** (one joint policy over all 50), which LIBERO reporting usually elides.

## The randomized ("hard") setting — closed by X-VLA

The gap flagged below is now partly filled. The [X-VLA paper](../sources/xvla-paper.md) reports **both** settings across all 50 tasks, and the drop is severe:

| Model | Params (B) | Easy | Hard | Drop |
|---|---:|---:|---:|---:|
| [X-VLA](x-vla.md) | 0.9 | **70.0** | **39.0** | −31.0 |
| [π0](pi-zero.md) | 3.0 | 46.4 | 16.4 | −30.0 |
| RDT | 1.0 | 34.5 | 13.7 | −20.8 |

Two things worth taking from this. **Domain randomization costs every model roughly 20–31 points** — the randomized setting is not a modest perturbation, it is a different benchmark, and the [LIBERO-PRO](../sources/libero-pro-paper.md)-shaped worry is well founded. And **the ranking survives**: X-VLA leads on both, by a *wider* relative margin on hard (2.4×) than on easy (1.5×), so whatever the randomization is testing, cross-embodiment pretraining with [soft prompts](../concepts/learning/soft-prompt-cross-embodiment.md) helps with it more than it helps in the clean case.

Cross-validation note: X-VLA's π0 clean figure (46.4) and RDT clean figure (34.5) match the TurboVLA table above exactly, which is mild evidence that both papers are running the benchmark the same way.

Per-task detail is in the paper's Tab. 16. The spread is enormous — `Shake Horizontally` 99/100 and `Put Object Cabinet` 78/82 barely degrade, while `Put Bottles Dustbin` scores **0.0/1.0** and `Place Object Basket` goes 50.0 → **0.0**. Averages over 50 tasks are hiding total failures.

## The data generator (from the primary source)

Three components, in descending order of how much this wiki cares:

**1. Embodiment-aware grasp adaptation — the finding that matters most here.** Objects carry candidate manipulation poses across multiple grasp axes and approach directions; the generator picks robot-specific ones. Effect on automated data-collection success across 50 tasks:

| Embodiment | DoF | RoboTwin 1.0 | RoboTwin 2.0 | Δ |
|---|---:|---:|---:|---:|
| [AgileX Piper](agilex-piper.md) | 6 | **2.4%** | **25.1%** | **+22.7** |
| Aloha-AgileX | 6 | 65.1% | 78.8% | +13.7 |
| ARX-X5 | 6 | 68.6% | 74.2% | +5.6 |
| [Franka](franka-panda.md) | 7 | 67.3% | 67.2% | −0.1 |
| UR5 | 7 | 57.6% | 57.1% | −0.5 |

The mechanism, in the authors' words: *"a low-DoF platform like the Piper often relies on lateral grasps due to its limited dexterity, whereas a high-DoF arm such as the Franka is capable of top-down precision grasps."* **At 2.4%, RoboTwin 1.0 could not generate usable data for the Piper at all.** See [RoboMIND](robomind.md) for how this composes with the dexterous-hand exclusion at the other end of the range.

**2. MLLM code generation with a VLM observer.** A code agent writes a Python task program; it runs **10× per iteration**; a VLM watches all ten frame-by-frame, localizes *which step* failed and diagnoses *why*; the code agent repairs. Terminates at >0.5 success or after 5 refinements. Average success rate **47.4% → 71.3%**, with multimodal feedback worth +3.5 to +4.6 over execution-log feedback alone, in fewer iterations and with shorter code.

**3. Domain randomization on five axes** — clutter (semantically-similar distractors deliberately excluded), background texture (**11,000 filtered from 20,000 Stable Diffusion generations**), lighting, tabletop height, and language instructions (MLLM-generated templates × multi-granularity object descriptions, sampled per trajectory).

## Baselines from the primary source

Protocol: **50 clean expert demos per task for training, 100 rollouts per task per condition, all 50 tasks, Aloha-AgileX**, VLAs finetuned from released weights, single-task setting → **n = 5,000 per model per condition**.

| | [RDT](rdt.md) | π0 | [ACT](act.md) | [DP](diffusion-policy.md) | DP3 |
|---|---:|---:|---:|---:|---:|
| Easy | 34.5 | **46.4** | 29.7 | 28.0 | **55.2** |
| Hard | 13.7 | **16.3** | 1.7 | 0.6 | 5.0 |

> [!note] What VLA pretraining buys is robustness, not peak performance
> Non-pretrained policies do not merely degrade under randomization — **they die**: ACT 29.7 → **1.7**, DP 28.0 → **0.6**. Pretrained VLAs drop hard but survive (RDT 13.7, π0 16.3). And **DP3 beats every VLA on Easy (55.2) then collapses to 5.0** — the paper concedes its Easy win *"partly stems from perfect point clouds and clean background segmentation in simulation."* A 3D policy evaluated on noiseless depth is being flattered. This is the cleanest quantification in the wiki of what action-pretraining actually purchases.

> [!note] Cross-paper consistency
> π0's 46.4 Easy here matches [X-VLA](x-vla.md)'s cited 46.4 and [TurboVLA](turbovla.md)'s 46.4; RDT 34.5 matches too. Three independent papers, same figures — the benchmark is being run consistently, which is more than can be said for most.

## Does randomized data actually buy robustness?

Pretraining RDT and π0 on 9,600 trajectories under **clean** vs **randomized** settings, then evaluating under randomization:

- **Clean-data finetuning does essentially nothing** — RDT 18.8 → 14.6 (*worse*), π0 22.5 → 24.9.
- **Randomized pretraining gives +31.9% relative (RDT) and +29.3% (π0)**, and the gain **persists when the downstream task is trained on clean data only**.
- The authors' inference is the right one: since clean sim data doesn't help, the low baseline is **not a real-to-sim gap, it's a robustness gap**.

Real-world (RDT on a COBOT-Magic dual-arm, 4 tasks): 10 real demos + 1k synthetic beats 10 real alone by **+24.4 points averaged**, with gains *growing* with difficulty (+13.5 easiest configuration → **+33.0** unseen-background cluttered). Zero-shot synthetic-only beats 10 real demos in both unseen-background configurations.

> [!warning] The abstract's "367%" is one configuration, not the average
> `(42.0 − 9.0)/9.0` on the unseen-background-cluttered row. The average improvement is **+24.4 points**. Both honest; only one representative. See the [source page](../sources/robotwin2-paper.md).

## Open questions
- ~~No primary RoboTwin paper ingest~~ — **done 2026-08-13**: [RoboTwin 2.0 paper](../sources/robotwin2-paper.md).
- **No ablation isolates which randomization axis carries the gain.** Five axes, one bundled result. Given the 11,000-texture library's cost, knowing whether texture matters would be worth having.
- **Does the DoF result extend below 6?** The benefit grows as DoF falls (Franka 7 → −0.1; Piper 6 → +22.7). Nobody has run the generator against a **5-DoF** arm — the tier [SO-ARM101](so-arm101.md), [XLeRobot](xlerobot.md), and [Sourccey](sourccey.md) actually occupy.
- What distinguishes the tasks that survive randomization (`Shake Horizontally`, `Put Object Cabinet`) from those that collapse to zero (`Put Bottles Dustbin`, `Place Object Basket`)? Container-relative placement under scene randomization looks like the failure cluster, but that is a guess from task names.

## Related
- [LIBERO](libero.md) — the single-arm benchmark it complements
- [ALOHA](aloha.md) / [YAM](yam.md) — real bimanual platforms
- [X-VLA](x-vla.md) — current best on both settings
- [RoboMIND](robomind.md) — the real-world counterpart it cites; the two together bracket the cross-embodiment action-space problem
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md)
- [Success-rate audit](../syntheses/platforms/vla-success-rate-audit.md)

## Mentioned in
- [TurboVLA paper](../sources/turbovla-paper.md)

## The substrate of WorldArena

RoboTwin 2.0 is the evaluation substrate for [WorldArena](worldarena.md) and WorldArena 2.0: 50 scenarios, 2,500 videos (2,000 to post-train each world model, 500 held out), with two tasks — *adjust bottle* and *click bell* — carrying the functional evaluation at 100 trials each. Its own simulator supplies the ground-truth policy ranking that learned policy evaluators are scored against.

That makes RoboTwin the reference frame for the wiki's central world-model finding: a [π0.5](pi-zero-5.md) policy trained on real RoboTwin data hits **77% / 66%**, and no world model comes close as a data engine or planner ([WorldArena paper](../sources/worldarena-paper.md)).

## Mentioned in (additional)

- [WorldArena paper](../sources/worldarena-paper.md) · [WorldArena 2.0 paper](../sources/worldarena-2-paper.md)

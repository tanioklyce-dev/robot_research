---
title: RoboTwin 2.0
type: entity
subtype: benchmark
created: 2026-08-04
updated: 2026-08-13
sources: 4
tags: [robotwin, benchmark, bimanual, manipulation, domain-randomization, data-generation, simulation]
---

**RoboTwin 2.0** — a scalable **bimanual** manipulation data generator and benchmark with strong domain randomization (Chen, Chen, Chen et al., ICML 2026). **50 language-conditioned dual-arm tasks** requiring coordinated two-arm control; ships both a *clean* setting and a randomized-scene setting.

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

## Open questions
- Still **no primary RoboTwin paper ingest**; everything here is secondhand via TurboVLA and X-VLA.
- What distinguishes the tasks that survive randomization (`Shake Horizontally`, `Put Object Cabinet`) from those that collapse to zero (`Put Bottles Dustbin`, `Place Object Basket`)? Container-relative placement under scene randomization looks like the failure cluster, but that is a guess from task names.

## Related
- [LIBERO](libero.md) — the single-arm benchmark it complements
- [ALOHA](aloha.md) / [YAM](yam.md) — real bimanual platforms
- [X-VLA](x-vla.md) — current best on both settings
- [Success-rate audit](../syntheses/platforms/vla-success-rate-audit.md)

## Mentioned in
- [TurboVLA paper](../sources/turbovla-paper.md)

## The substrate of WorldArena

RoboTwin 2.0 is the evaluation substrate for [WorldArena](worldarena.md) and WorldArena 2.0: 50 scenarios, 2,500 videos (2,000 to post-train each world model, 500 held out), with two tasks — *adjust bottle* and *click bell* — carrying the functional evaluation at 100 trials each. Its own simulator supplies the ground-truth policy ranking that learned policy evaluators are scored against.

That makes RoboTwin the reference frame for the wiki's central world-model finding: a [π0.5](pi-zero-5.md) policy trained on real RoboTwin data hits **77% / 66%**, and no world model comes close as a data engine or planner ([WorldArena paper](../sources/worldarena-paper.md)).

## Mentioned in (additional)

- [WorldArena paper](../sources/worldarena-paper.md) · [WorldArena 2.0 paper](../sources/worldarena-2-paper.md)

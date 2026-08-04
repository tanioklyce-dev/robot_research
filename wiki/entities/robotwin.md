---
title: RoboTwin 2.0
type: entity
subtype: benchmark
created: 2026-08-04
updated: 2026-08-04
sources: 1
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

## Open questions
- **The randomized-scene setting has not been ingested here.** TurboVLA trained on clean demonstrations only, citing compute budget, so the wiki has no data on how the 2026-class VLAs behave under RoboTwin's own domain randomization — which is precisely the [LIBERO-PRO](../sources/libero-pro-paper.md)-shaped question.
- No primary RoboTwin paper ingest yet; everything above is secondhand via TurboVLA.

## Related
- [LIBERO](libero.md) — the single-arm benchmark it complements
- [ALOHA](aloha.md) / [YAM](yam.md) — real bimanual platforms
- [Success-rate audit](../syntheses/platforms/vla-success-rate-audit.md)

## Mentioned in
- [TurboVLA paper](../sources/turbovla-paper.md)

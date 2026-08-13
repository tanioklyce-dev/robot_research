---
title: SimplerEnv
type: entity
subtype: product
created: 2026-05-08
updated: 2026-08-13
sources: 4
tags: [simplerenv, manipulation-benchmark, sapien, real-world-eval, vla-eval, widowx, xvla]
---

**SimplerEnv** — Sapien-adjacent mid-weight robot simulator suite designed to **mirror real-world manipulation evaluation** in simulation. Used as a sim eval harness alongside real-robot evaluation for [VLA](../concepts/learning/vla-models.md) policies, where the sim numbers are positioned as a **predictor of real-world success rate** rather than a separate eval.

## Position in this wiki
Primary reference is [VLA-JEPA](../sources/vla-jepa-paper.md) (Sun et al., Feb 2026), which evaluates on **LIBERO + LIBERO-Plus + SimplerEnv + real-world manipulation**. In the [revised JEPA-skips-sim synthesis](../syntheses/world-models/why-jepa-research-skips-the-simulator-stack.md), SimplerEnv represents the **mid-weight class** between LeWM-style lightweight benches and JEPA-WMs / RoboCasa-class heavy sim.

## Why it matters
- **Sim-to-real correlation framing.** SimplerEnv is built to make sim numbers credible proxies for real-world performance, not just sim-only benchmarks. That's a different design point than pure RL-eval suites.
- **Sapien-based.** Builds on the [SAPIEN](sapien.md) simulation framework that also underlies [ManiSkill](maniskill.md) — situating SimplerEnv in the UCSD-lineage of manipulation simulation rather than the MuJoCo-lineage.

## Results (Simpler-WidowX — the wiki's widest benchmark margin)

The [X-VLA paper](../sources/xvla-paper.md) reports the largest single-benchmark jump in this wiki's VLA coverage:

| Model | Params (B) | Simpler-WidowX |
|---|---:|---:|
| [X-VLA](x-vla.md) | 0.9 | **95.8** |
| MemoryVLA | 7 | 71.9 |
| UniVLA | 9 | 69.8 |
| FPC-VLA | 7 | 64.6 |
| [π0](pi-zero.md) | 3 | 27.8 (55.7 when fully finetuned on it) |
| [OpenVLA](openvla.md) | 7 | 8.3 |

Also reported: Google-Robot Visual Matching 80.4 and Visual Aggregation 75.7 (prior bests 78.0 / 72.7). **Simpler-WidowX is where the field still has headroom** — unlike [LIBERO](libero.md), where everyone sits at 97–98 and gaps stop separating ([audit](../syntheses/platforms/vla-success-rate-audit.md)). That makes it the more informative of the two for the moment, and X-VLA's +23.9 pt margin over a 7 B model the most striking result on it.

X-VLA also uses Simpler-WidowX as its **ablation instrument** throughout — the whole recipe path from 4.1 to 95.8 is measured on it, alongside held-out ℓ1 validation error (R² = −0.925 between the two).

## Related
- [X-VLA](x-vla.md) — current SOTA on Simpler-WidowX by a wide margin.
- [VLA-JEPA](vla-jepa.md) — primary JEPA-line consumer in this wiki.
- [LIBERO](libero.md) — companion VLA-eval bench used together by VLA-JEPA.
- [SAPIEN](sapien.md) — likely underlying simulation framework.
- [RoboCasa](robocasa.md) — adjacent heavier-sim manipulation benchmark.

## Mentioned in
- [VLA-JEPA Paper](../sources/vla-jepa-paper.md)
- [X-VLA paper](../sources/xvla-paper.md)

## Open questions / TBD
- Authors / origin paper not yet ingested.
- Confirm Sapien vs. other simulator backend.
- "Sim numbers correlate with real-world success" framing is inferred from the VLA-JEPA usage; would be strengthened by reading the original SimplerEnv paper.

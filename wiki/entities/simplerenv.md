---
title: SimplerEnv
type: entity
subtype: product
created: 2026-05-08
updated: 2026-05-08
sources: 1
tags: [simplerenv, manipulation-benchmark, sapien, real-world-eval, vla-eval]
---

**SimplerEnv** — Sapien-adjacent mid-weight robot simulator suite designed to **mirror real-world manipulation evaluation** in simulation. Used as a sim eval harness alongside real-robot evaluation for [[vla-models|VLA]] policies, where the sim numbers are positioned as a **predictor of real-world success rate** rather than a separate eval.

## Position in this wiki
Primary reference is [[vla-jepa-paper|VLA-JEPA]] (Sun et al., Feb 2026), which evaluates on **LIBERO + LIBERO-Plus + SimplerEnv + real-world manipulation**. In the [[why-jepa-research-skips-the-simulator-stack|revised JEPA-skips-sim synthesis]], SimplerEnv represents the **mid-weight class** between LeWM-style lightweight benches and JEPA-WMs / RoboCasa-class heavy sim.

## Why it matters
- **Sim-to-real correlation framing.** SimplerEnv is built to make sim numbers credible proxies for real-world performance, not just sim-only benchmarks. That's a different design point than pure RL-eval suites.
- **Sapien-based.** Builds on the [[sapien|SAPIEN]] simulation framework that also underlies [[maniskill|ManiSkill]] — situating SimplerEnv in the UCSD-lineage of manipulation simulation rather than the MuJoCo-lineage.

## Related
- [[vla-jepa|VLA-JEPA]] — primary JEPA-line consumer in this wiki.
- [[libero|LIBERO]] — companion VLA-eval bench used together by VLA-JEPA.
- [[sapien|SAPIEN]] — likely underlying simulation framework.
- [[robocasa|RoboCasa]] — adjacent heavier-sim manipulation benchmark.

## Mentioned in
- [[vla-jepa-paper|VLA-JEPA Paper]]

## Open questions / TBD
- Authors / origin paper not yet ingested.
- Confirm Sapien vs. other simulator backend.
- "Sim numbers correlate with real-world success" framing is inferred from the VLA-JEPA usage; would be strengthened by reading the original SimplerEnv paper.

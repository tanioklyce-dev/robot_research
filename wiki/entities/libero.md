---
title: LIBERO
type: entity
subtype: benchmark
created: 2026-05-08
updated: 2026-05-08
sources: 1
tags: [libero, manipulation-benchmark, lifelong-learning, robosuite, mujoco]
---

**LIBERO — "Lifelong Robot Learning Benchmark."** Procedural manipulation benchmark designed to test **lifelong / continual policy learning** across diverse manipulation tasks. Suite of task families ("Spatial," "Object," "Goal," and "100" — long-tail) commonly used as a [[vla-models|VLA]] evaluation harness in 2024–2026. Built on robosuite + MuJoCo.

## Position in this wiki
Primary reference is [[vla-jepa-paper|VLA-JEPA]] (Sun et al., Feb 2026), which evaluates on **LIBERO + LIBERO-Plus + SimplerEnv + real-world manipulation**. LIBERO has effectively become the de-facto VLA-eval bench — alongside [[robocasa|RoboCasa]] for household manipulation and [[metaworld|Metaworld]] for multi-task RL.

## Why it matters
- **Standard VLA-eval suite.** Most VLA papers in 2024–2026 report LIBERO numbers; comparability across papers is the value.
- **Continual / lifelong framing.** The design tests whether policies can absorb new tasks without catastrophic forgetting — a different question than single-task or pure multi-task evaluation.

## Related
- [[vla-jepa|VLA-JEPA]] — primary JEPA-line consumer in this wiki.
- [[mujoco|MuJoCo]] — physics backend.
- [[robocasa|RoboCasa]] / [[metaworld|Metaworld]] — adjacent manipulation benchmarks.
- LIBERO-Plus — extended variant referenced by VLA-JEPA; could become its own entity if cross-cited.
- SimplerEnv — companion mid-weight sim used alongside LIBERO in VLA-JEPA.

## Mentioned in
- [[vla-jepa-paper|VLA-JEPA Paper]]

## Open questions / TBD
- Original LIBERO paper not yet ingested as a source — would let us cite design rationale (why the four task families, what "lifelong" means concretely).
- Authors and host institution not surfaced in this wiki yet.

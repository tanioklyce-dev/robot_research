---
title: robosuite
type: entity
subtype: simulator
created: 2026-08-03
updated: 2026-08-03
sources: 3
tags: [robosuite, simulator, mujoco, manipulation, benchmark, infrastructure]
---

**robosuite** (Zhu et al., 2020) — a modular simulation framework for **robot manipulation learning**, built on [MuJoCo](mujoco.md). Long-standing infrastructure rather than a headline result: it is the layer a large fraction of this wiki's manipulation benchmarks actually sit on.

## Position in the wiki — the substrate under the benchmarks

- **[LIBERO](libero.md) is built on robosuite + MuJoCo** — so every LIBERO and [LIBERO-PRO](../sources/libero-pro-paper.md) number in this wiki inherits robosuite's dynamics and controller stack.
- **[CaP-Gym](cap-x.md) integrates it directly** as one of three backends, contributing **7 core tasks** — Cube Lift, Cube Stack, Spill Wipe, Peg Insertion, Cube Re-stack, Two-Arm Lift, Two-Arm Handover — which are the tasks CaP-Bench's entire 12-model × 8-tier ablation runs on ([CaP-X paper](../sources/cap-x-paper.md)).
- **[ASPIRE](aspire.md)** reports on the same task set, including the bimanual handover result (**20% → 92%**) that is its largest Robosuite gain ([ASPIRE paper](../sources/aspire-paper.md)).

Its **Two-Arm Handover** task is worth noting specifically: across both ingested code-as-policy papers it is consistently the hardest of the seven, and therefore the one that discriminates between methods when the others saturate.

## Lineage
Authored under [Yuke Zhu](yuke-zhu.md) — the same line that produced [RoboCasa](robocasa.md) and [MimicGen](mimicgen.md). The wiki has carried "robosuite paper — would be useful infrastructure ingest" as an open question on Zhu's page; this entity records what the framework *is* and where it appears, but the original paper is still not ingested.

## Related
- [MuJoCo](mujoco.md) — physics backend · [MuJoCo Playground](mujoco-playground.md).
- [LIBERO](libero.md) — built on it.
- [CaP-X](cap-x.md) — integrates it as a backend.
- [Yuke Zhu](yuke-zhu.md) — lead author.
- [RoboCasa](robocasa.md) / [MimicGen](mimicgen.md) — sibling infrastructure from the same group.

## Mentioned in
- [CaP-X paper](../sources/cap-x-paper.md) — one of three CaP-Gym simulator backends; source of the 7 core benchmark tasks.
- [ASPIRE paper](../sources/aspire-paper.md) — contact-rich single- and dual-arm evaluation family.
- [LIBERO](libero.md) — named as LIBERO's construction substrate.

## Open questions / TBD
- The original robosuite paper (Zhu et al., 2020) is still not ingested — would let the wiki cite controller design and task-construction rationale rather than inheriting it silently through LIBERO.

---
title: CaP-X
type: entity
subtype: framework
created: 2026-08-03
updated: 2026-08-03
sources: 2
tags: [cap-x, code-as-policy, benchmark, framework, nvidia-gear, robosuite, libero-pro, behavior, rlvr, open-source]
---

**CaP-X** — an open-access framework for **benchmarking and improving [code-as-policy](../concepts/agents/code-as-policy.md) agents** in robot manipulation, from [NVIDIA GEAR](nvidia-gear.md) + UC Berkeley + Stanford + CMU ([paper](../sources/cap-x-paper.md), ICML 2026). It is the wiki's reference measurement apparatus for the question *"how good is the code a model writes to drive a robot?"* — and the substrate [ASPIRE](aspire.md) is built on.

Project page: `https://capgym.github.io`

## Four components

| Component | What it is |
|---|---|
| **CaP-Gym** | The environment. **187 tasks** (7 [Robosuite](robosuite.md) + 130 [LIBERO-PRO](../sources/libero-pro-paper.md) + 50 [BEHAVIOR](behavior-benchmark.md)) behind a Gymnasium interface binding a physics loop to a stateful **Code Executor REPL**. One "turn" = observations in, a Python program out, executed to completion. |
| **CaP-Bench** | The benchmark. **12 frontier models × 8 tiers** over 7 core tasks at **100 trials/tier**, ablating three axes: primitive **abstraction** (S1–S4), **temporal interaction** (single- vs multi-turn), and **perceptual grounding**. |
| **CaP-Agent0** | A **training-free** agentic harness: visual differencing + an auto-synthesized 9-primitive skill library + parallel multi-model reasoning. |
| **CaP-RL** | GRPO/RLVR post-training **of the coding agent itself** against simulator rewards. |

## The tier ladder (CaP-Bench's main instrument)

Single-turn **S1** (human macros + privileged state) → **S2** (macros + real perception; *the default of most prior work*) → **S3** (low-level primitives + usage examples) → **S4** (low-level, signatures only). Multi-turn **M1** (stdout/stderr) → **M2** (raw RGB) → **M3** (Visual Differencing Module) → **M4** (VDM + low-level).

This ladder is the wiki's finest-grained instrument for [control abstraction levels](../concepts/robotics/control-abstraction-levels.md): it subdivides what [Anthropic's taxonomy](../sources/anthropic-how-claude-performs-on-robotics-tasks.md) calls a single level ("programmatic control") into eight measurable rungs, and shows performance varies enormously *within* that one level.

## Primitive stack

- **Perception** — SAM3 (language-conditioned segmentation), **[Molmo 2](molmo2-er.md)** (open-vocabulary pointing), OpenCV, Open3D.
- **Control** — motion planners and IK via **PyRoki**; agents reason in Cartesian space and delegate feasibility, collision checking, and reachability to the controller.
- All primitives run as **stateless services** for high-throughput parallel evaluation.
- Deliberately designed so the same interface drives real hardware — demonstrated zero-shot on [Franka Panda](franka-panda.md) and [AgiBot](agibot.md) G1.

## Why it matters in this wiki

- **It supplies the numbers the code-as-policy thread was missing.** Before this ingest, the wiki's only deployed code-as-policy data point was [Waddle](waddle-labs.md)'s [position piece with no success rates](../sources/waddle-labs-introducing-waddle.md). CaP-X measures the paradigm properly, including against post-trained VLAs.
- **It reframes the paradigm's own history.** The monotonic S4→S1 gain means prior CaP results were substantially carried by human-designed macros — a caveat that now attaches to the whole [lineage](../concepts/agents/code-as-policy.md).
- **It is infrastructure, not just a paper.** ASPIRE uses it as the environment; expect further work built on it.

## Related
- [ASPIRE](aspire.md) — built on CaP-X; CaP-Agent0 is its baseline.
- [NVIDIA GEAR](nvidia-gear.md) — home lab (listed there as "CaP-X, ICML 2026 oral").
- [Robosuite](robosuite.md) / [LIBERO](libero.md) / [BEHAVIOR](behavior-benchmark.md) — the three simulator backends.
- [Waddle Labs](waddle-labs.md) — the commercial claim CaP-X supplies missing evidence for; Waddle cites it.
- [Code as policy](../concepts/agents/code-as-policy.md) — the concept.

## Mentioned in
- [CaP-X paper](../sources/cap-x-paper.md) — primary source.
- [ASPIRE paper](../sources/aspire-paper.md) — uses CaP-X as its code-as-policy framework and CaP-Agent0 as its main baseline.
- [NVIDIA GEAR Lab — Publications](../sources/nvidia-gear-publications.md) — listed under the manipulation/agents pillar.

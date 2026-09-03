---
title: Jiajun Wu
type: entity
subtype: person
created: 2026-08-31
updated: 2026-08-31
sources: 1
tags: [jiajun-wu, stanford, stanford-hai, researcher, world-models, evaluation, benchmark, video-prediction]
---

**Jiajun Wu** — Stanford assistant professor of computer science and, by courtesy, psychology ([Stanford HAI](stanford-hai.md) affiliate). In this wiki he is the recurring name at the **measurement** end of the world-model program: he keeps appearing as an author on the benchmarks that judge video and world models, and then on the policy documents that cite those benchmarks.

## Where he shows up here

| Work | Role | What it does |
|---|---|---|
| **[VP²](../sources/vp2-paper.md)** (Tian, Finn, Wu) | co-author | Control-centric benchmark for video prediction — evaluate a video model by whether **planning through it works**, not by pixel metrics. The earliest instance in this wiki of the "measure it by what it's for" principle. |
| **[VoxPoser](../sources/voxposer-paper.md)** (Huang, Wang, Zhang, Li, Wu, [Fei-Fei Li](fei-fei-li.md)) | co-author | LLM-composed 3D value maps for manipulation; the [code-as-policy](../concepts/agents/code-as-policy.md) lineage. |
| **WorldScore** (Duan, Yu, Chen, Fei-Fei Li, Wu) | co-author | Controllability / quality / dynamics in world *generation*. **Not ingested** — an open backlog item. |
| **[HAI world-model & spatial-intelligence brief](../sources/hai-world-model-spatial-intelligence-brief.md)** | co-author | The policy document arguing no adequate world-model benchmark exists, citing the landscape he helped build. |
| **[Physion-Eval](../sources/physion-eval-paper.md)** (Zhang et al., 2026) | senior author | Expert-human-reasoning benchmark for physical realism in generated video; finds MLLM critics **2–6× less sensitive than untrained humans**. |

> [!note] The closed loop the wiki has flagged twice
> [World-model evaluation](../concepts/world-models/world-model-evaluation.md) records that **WorldScore was co-authored by two of the HAI brief's own authors** (Fei-Fei Li and Wu), and that the brief presents the benchmark landscape as external evidence without noting the overlap. Physion-Eval is a third node in the same graph. This is not an accusation of bad faith — it is a small field, and Wu's group is genuinely doing the measurement work. But when a policy brief's "the field lacks benchmarks" claim is sourced to benchmarks its own authors built, the provenance is worth stating.

## The through-line

Wu's benchmark work consistently pushes evaluation **away from perceptual scores and toward consequence** — VP² measures planning success rather than pixels; Physion-Eval replaces automated metrics with temporally-grounded expert reasoning after finding that automated critics miss most of what ordinary people see. That is the same direction this wiki's [world-model evaluation](../concepts/world-models/world-model-evaluation.md) page traces from VBench to [WorldArena](worldarena.md), arrived at independently.

## Related

- [Chelsea Finn](chelsea-finn.md) — VP² co-author; her group later produced [Ctrl-World](ctrl-world.md).
- [Fei-Fei Li](fei-fei-li.md) — frequent co-author (VoxPoser, WorldScore, the HAI brief).
- [Stanford HAI](stanford-hai.md) — listed affiliate.

## Mentioned in

- [Physion-Eval paper](../sources/physion-eval-paper.md)
- [VP² paper](../sources/vp2-paper.md)
- [VoxPoser paper](../sources/voxposer-paper.md)
- [HAI world-model & spatial-intelligence brief](../sources/hai-world-model-spatial-intelligence-brief.md)
- [Chelsea Finn](chelsea-finn.md), [Stanford HAI](stanford-hai.md)

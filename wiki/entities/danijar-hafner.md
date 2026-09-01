---
title: Danijar Hafner
type: entity
subtype: person
created: 2026-07-09
updated: 2026-08-31
sources: 3
tags: [hafner, dreamer, planet, daydreamer, mbrl, world-model, rssm, deepmind]
---

# Danijar Hafner

The researcher whose through-line **is** the imagination-training branch of model-based RL — first author or co-first across the whole [Dreamer](dreamer.md) arc (DeepMind / U. Toronto / UC Berkeley collaborations). Creating this page closes the TBD on the [Dreamer entity](dreamer.md).

## The arc (all first-/co-first-authored, all ingested)

| Year | Work | Contribution |
|---|---|---|
| 2019 | [PlaNet](../sources/planet-paper.md) | the **RSSM** + planning (CEM) in latent space; ~200× sample-efficiency vs A3C |
| 2020–21 | Dreamer V1/V2 | actor-critic **in imagination** on the RSSM (not separately ingested; see [Dreamer](dreamer.md)) |
| 2022 | [DayDreamer](../sources/daydreamer-paper.md) | Dreamer on **4 real robots, no simulator** — A1 walks in 1 hour |
| 2023–25 | [DreamerV3](../sources/dreamer-v3-paper.md) | one config across 150+ tasks; Minecraft diamonds from scratch |

The consistent bet: a learned generative dynamics model + policy learning inside it beats both model-free RL (sample cost) and simulators (fidelity/adaptation) — the position [DayDreamer](../sources/daydreamer-paper.md) states most sharply.

## Related

- [Dreamer / DreamerV3](dreamer.md) — the method family; [World model](../concepts/world-models/world-model.md) — the concept his line anchors.
- Downstream of his RSSM: [S5WM](../sources/s5wm-paper.md) (replaces it), [EAWM](../sources/eawm-paper.md) (re-targets its objective).

## Mentioned in
- [Third World Modeling Workshop, Chicago Booth 2026](../sources/chicago-booth-world-modeling-workshop-2026.md) — *"Predict Everything"* keynote on Dreamer 4, plus the panel where he reports that explicitly representing the full belief state lost to sampling from a probabilistic model.

- [PlaNet paper](../sources/planet-paper.md) — first author.
- [DayDreamer paper](../sources/daydreamer-paper.md) — co-first author.
- [DreamerV3 paper](../sources/dreamer-v3-paper.md) — first author.

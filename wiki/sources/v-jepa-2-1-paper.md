---
title: V-JEPA 2.1 Paper
type: source
url: https://arxiv.org/abs/2603.14482
local_path: null
author: Lorenzo Mur-Labadia, Matthew Muckley, Amir Bar, Mido Assran, Koustuv Sinha, Mike Rabbat, Yann LeCun, Nicolas Ballas, Adrien Bardes
affiliations: FAIR at Meta + Mila (inferred from author overlap with V-JEPA 2)
published: 2026-03-15
revised: 2026-03-17
ingested: 2026-05-07
tags: [v-jepa-2, jepa, world-model, dense-features, meta-fair, video, real-robot]
---

## Summary
**V-JEPA 2.1** — direct successor to [[v-jepa-2-paper|V-JEPA 2]] from largely the same FAIR team (Bardes, Assran, Rabbat, Ballas, LeCun). Headline contribution: "**unlocking dense features**" in video self-supervised learning while retaining global scene understanding. Per the agent research that flagged this paper, it reports a **+20pt improvement on real-Franka grasping** vs V-JEPA 2-AC.

## Key claims
- "A family of self-supervised models that learn dense, high-quality visual representations for both images and videos while retaining strong global scene understanding" (abstract).
- Improves on V-JEPA 2 on dense-feature tasks (depth forecasting, segmentation) while preserving the global-understanding strengths.
- **Real-robot grasping +20pt over V-JEPA 2-AC** (per secondary research; not lifted verbatim from abstract — verify in body).
- Evaluated on **Ego4D, EPIC-KITCHENS, Something-Something-V2, NYUv2, TartanDrive**, plus real-robot grasping and navigation. **No simulator named in the abstract.**
- DOI: https://doi.org/10.48550/arXiv.2603.14482

## Entities mentioned
- [[meta-fair|Meta FAIR]]
- [[v-jepa-2|V-JEPA 2]] — predecessor.

## Concepts touched
- [[jepa|Joint-Embedding Predictive Architecture]]
- [[world-model-simulators|World-model simulators]] — latent-prediction paradigm continues.

## Open questions
- Code/project URL not surfaced from the abstract page.
- Specific real-robot platform for grasping/navigation not named in the abstract — likely Franka given V-JEPA 2 lineage but needs confirmation.
- Exact +20pt grasping number is from secondary research; verify against paper body.

## Why this matters
V-JEPA 2.1 continues the V-JEPA 2 pattern: **internet-scale video pretraining → real-robot eval → no simulator**. So while [[jepa-wms-paper|Terver et al. (jepa-wms)]] moves FAIR JEPA work into RoboCasa, V-JEPA 2.1 sustains the original sim-skipping line in parallel. The two papers together suggest **FAIR is hedging across both approaches**, not abandoning the sim-free path.

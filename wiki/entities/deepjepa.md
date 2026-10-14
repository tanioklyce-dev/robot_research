---
title: DeepJEPA
type: entity
subtype: method
created: 2026-10-13
updated: 2026-10-13
sources: 1
tags: [deepjepa, jepa, world-model, leworldmodel, adaptive-computation, test-time-compute, cem, metareasoning]
---

**DeepJEPA** is a LeWM-style action-conditioned JEPA world model whose per-transition predictor is a **weight-tied recurrent cell with learned halting**. Each imagined transition gets 1–4 internal updates, chosen per CEM candidate and rollout step ([Jin, Zhang et al., Sept 2026](../sources/deepjepa-scaling-world-models-from-within-paper.md)). It treats *depth inside a transition* as a test-time compute axis alongside horizon and candidate count.

## What it shows
- **Uniformly deeper is not better**: fixed K = 4 never beats K = 1 across five simulated tasks.
- **Adaptive depth is compute-neutral**: it matches the best fixed depth at an average of 1.00–1.26 updates. The reported gains (0 to +3.3 pp at n = 150, thresholds tuned on the evaluation sweep) are within noise.
- **Extra compute lands at contact**: refinement jumps about 7× at PushT contact onset, learned with no contact labels.
- **The effect runs through CEM ranking, not representation quality.** A sufficient condition, half the elite margin, says when more model precision cannot change the planner's choice.

## Related
- [LeWorldModel](leworldmodel.md) — the base recipe and baseline.
- [Adaptive depth reasoning](../concepts/learning/adaptive-depth-reasoning.md) — MolmoAct2-Think's per-cell version of the same principle.
- [H-JEPA](h-jepa.md) and [RoboJEPA](robojepa.md) — the same fortnight's other answers to "how should JEPA world models scale": hierarchy depth, and predictor size.
- [Marco Pavone](marco-pavone.md).

## Mentioned in
- [DeepJEPA paper](../sources/deepjepa-scaling-world-models-from-within-paper.md)

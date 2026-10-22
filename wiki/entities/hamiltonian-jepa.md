---
title: Hamiltonian JEPA
type: entity
subtype: model
created: 2026-10-22
updated: 2026-10-22
sources: 1
tags: [hamiltonian-jepa, jepa, port-hamiltonian, bures-wasserstein, leworldmodel, action-conditioned, structured-dynamics, tel-aviv-university]
---

# Hamiltonian JEPA

**Hamiltonian JEPA** is an action-conditioned [JEPA](../concepts/world-models/jepa.md) world model whose predictor has a **port-Hamiltonian** form: learned energy-driven drift, learned damping, and an action input through a matrix with **orthonormal columns**, so one unit of action always moves the state by one unit. The planner scores a fixed random slice of a wider perceptual code, which is regularised with a **Bures-Wasserstein** prior instead of [SIGReg](../concepts/world-models/sigreg.md). Zoabi, Ali, Wolf (Tel Aviv University), arXiv 2609.33497, September 2026 ([paper](../sources/hamiltonian-jepa-control-state-paper.md)).

> [!warning] Name collision
> The paper abbreviates itself **"H-JEPA"**. That is not the hierarchical [H-JEPA](h-jepa.md) of Zhang, Terver, LeCun and Balestriero (arXiv 2610.06805), which has its own page. In this wiki this model is always **Hamiltonian JEPA**.

## Results
- **LeWM benchmark suite**, 3 seeds, 500 episodes: Two-Room 100 / Reacher 86.1 / Push-T 90.4 / **OGB-Cube 91.9%**, against 100 / 81.3 / 89.1 / 79.3 for Delta-JEPA, the strongest baseline. It trains for 10 epochs on one RTX A5000.
- Against the official LeWM checkpoint on 200 paired Push-T episodes: 88.5 vs 82.0, **p ≈ 0.053**.
- Replacing the BW prior with SIGReg inside this architecture: **36.7%** on Push-T. The paper says this is not a claim about SIGReg inside LeWM.
- State rank and checkpoint epoch are picked per task on a held-out pilot seed.

## Why it matters here
Its tied inverse readout (PIC) is **provably a reweighting of the forward loss**. That makes it the one inverse-dynamics-style term that adds no parameters. The wiki reads the orthonormal action port as a structural barrier against [slow-feature collapse](../concepts/world-models/slow-feature-collapse.md), because a predictor that must displace the state per action cannot become an action-blind identity map. **The paper does not test this.** Its benchmarks are single-scene. See [the batch synthesis](../syntheses/world-models/jepa-dynamics-collapse-fixes.md).

## Related
- [LeWorldModel](leworldmodel.md) — the base architecture and benchmark suite.
- [SMWM](smwm.md) · [PLDM](pldm.md) — explicit inverse-dynamics alternatives. SMWM is cited but missing from the comparison table.
- [Optimal control](../concepts/robotics/optimal-control.md) — control-affine structure as a learned prior.
- [MotionJEPA](motionjepa.md) — a label-free barrier from the same weeks.

## Mentioned in
- [Hamiltonian JEPA paper](../sources/hamiltonian-jepa-control-state-paper.md)
- Synthesis: [What the latent throws away](../syntheses/world-models/jepa-dynamics-collapse-fixes.md)

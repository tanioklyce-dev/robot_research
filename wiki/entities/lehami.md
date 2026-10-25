---
title: LeHami
type: entity
subtype: model
created: 2026-10-24
updated: 2026-10-24
sources: 1
tags: [lehami, jepa, hamiltonian, symplectic, leapfrog, volume-preservation, rollout-contraction, leworldmodel, ami-labs, nyu]
---

# LeHami

**LeHami** (Symplectic Hamiltonian JEPA) is a [JEPA](../concepts/world-models/jepa.md) world model whose predictor is a learned, action-conditioned **Hamiltonian flow integrated by an exactly symplectic leapfrog step**. Its latent is a canonical pair (*q*, *p*): *q* comes from the encoder, and *p* is a fixed Savitzky–Golay time derivative of *q*. It is by Yalovetzky, [Balestriero](randall-balestriero.md) and [LeCun](yann-lecun.md) (NYU / Brown / [AMI Labs](ami-labs.md)), arXiv 2610.15267, 2026-10-11 ([paper](../sources/lehami-symplectic-latent-dynamics-paper.md)).

> [!warning] Not the other Hamiltonian JEPA
> [Hamiltonian JEPA](hamiltonian-jepa.md) (Zoabi, Ali, Wolf) is a port-Hamiltonian, Euler-stepped predictor that targets the **encoder** dropping the control state. LeHami targets **predictor contraction during rollout**. Neither is the hierarchical [H-JEPA](h-jepa.md).

## What it guarantees
Phase-space volume is preserved **exactly at every rollout step**, for any parameters and any action sequence. That rules out uniform contraction, attracting fixed points, and merging of distinct states (Prop. 1). The authors are explicit that this bounds the *shape* of failure, **not the size of rollout error**, and does not replace [SIGReg](../concepts/world-models/sigreg.md).

## Results ([paper](../sources/lehami-symplectic-latent-dynamics-paper.md); 64×64 pendulums, 3 seeds)
- Against [LeWorldModel](leworldmodel.md):
  - velocity error 2.8× lower early in the rollout;
  - latent log-volume **exactly constant** where LeWM's declines linearly;
  - LeWM's best error matched at **≤ ⅛ the training FLOPs**;
  - a smaller predictor (2.23M vs 3.31M + 0.27M).
- **DINO-LeHami** beats [DINO-WM](dino-wm.md) on a frozen DINOv2 encoder.
- Integrates at ½ and ¼ the training step size and **runs backwards** (round-trip < 10⁻⁴ %). Doubling the step breaks it.
- **Planning: it loses to LeWM.** Position goals: 0.48 vs 0.80. Velocity and joint goals: 0.53 / 0.30 vs untied-window LeWM's 0.80 / 0.64. It is cheaper per episode and gets the velocity sign right more often than every LeWM variant except the untied one.

## Limits
Both test systems are volume-preserving by design. **Dissipative dynamics (friction, contact) cannot be represented by a purely symplectic latent**, and the proposed damping extension is not run. There is no LeWM-suite (Push-T / Cube) or real-robot result.

## Related
- [Hamiltonian JEPA](hamiltonian-jepa.md) — the port-Hamiltonian sibling, run on the LeWM suite
- [LeWorldModel](leworldmodel.md) — baseline and host architecture
- [Slow-feature collapse](../concepts/world-models/slow-feature-collapse.md) — the encoder-side failure LeHami does **not** address
- [What the latent throws away](../syntheses/world-models/jepa-dynamics-collapse-fixes.md) — the collapse-fix synthesis

## Mentioned in
- [LeHami paper](../sources/lehami-symplectic-latent-dynamics-paper.md)
- Synthesis: [What the latent throws away](../syntheses/world-models/jepa-dynamics-collapse-fixes.md)

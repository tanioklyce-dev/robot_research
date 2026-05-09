---
title: "Learning Control-Oriented Dynamical Structure from Data"
type: source
url: https://arxiv.org/abs/2302.02529
author: Spencer M. Richards, Jean-Jacques Slotine, Navid Azizan, Marco Pavone
affiliations: MIT; Stanford
published: 2023-06-24
venue: ICML 2023
ingested: 2026-05-09
tags: [control-theory, nonlinear-control, sdre, sdc-factorization, learning-for-control, trajectory-tracking, icml]
---

## Summary
ICML 2023 paper proposing **SD-LQR**: a method for learning state-dependent coefficient (SDC) factorizations from data, enabling state-dependent Riccati equation (SDRE) trajectory tracking for nonlinear systems. Addresses the core difficulty that data-driven dynamics models often lack the structural properties needed for reliable stabilizing controller synthesis. [Navid Azizan](../entities/navid-azizan.md) is a co-author — the same group later published the MIT drone adaptive control work (2025). Marco Pavone (Stanford autonomous systems) is senior.

## Key claims

### Core insight
For control-affine systems `ẋ = f(x) + B(x)u`, a state-dependent coefficient factorization always exists for continuously differentiable f:
```
f(x) - f(x̄) = A(x̄, x-x̄)(x-x̄)
```
This extends state-dependent LQR from set-point regulation to **trajectory tracking** via SDRE feedback, without assuming linearity near the operating point.

### Three approaches compared
| Method | What's learned | Data requirement | Performance |
|---|---|---|---|
| Naïve LQR | Dynamics f, B | Labeled only | Fails with limited data |
| CCM | Dynamics + contraction metric M + gain K | Labeled only | Frail with limited data |
| **SD-LQR (proposed)** | Dynamics + SDC factorizations A₀, {Aⱼ} | Labeled + 10k unlabeled | Tracks double loop-the-loop at N=100 |

**SD-LQR composite loss:** `L^SDC = L^dyn_reg + L^SDC_reg + L^SDC_aux`
Semi-supervised: 100–500 labeled trajectory samples + 10,000 unlabeled auxiliary points for constraint satisfaction.

### Benchmark results
- **Planar Spacecraft** (slightly nonlinear): SD-LQR stable; baselines comparable at high N, break at low N.
- **PVTOL** (highly nonlinear, underactuated, non-minimum-phase): SD-LQR tracks double loop-the-loop with N=100; CCM and naïve LQR fail.
- Median tracking error stable across data regimes for SD-LQR; baselines degrade sharply below ~500 samples.
- Gap vs. oracle (known dynamics) narrows with more data — validates learning approach.

### Limitations
- SDC constraint satisfaction is a relaxation (auxiliary loss), not a hard guarantee
- Requires ~10,000 unlabeled auxiliary samples
- Local stability guarantees only (SDRE theoretical result)
- Validated on 2 systems; higher-dimensional generalization untested

## Relation to MIT drone adaptive control (2025)
Both papers share [Navid Azizan](../entities/navid-azizan.md) as author. This paper addresses the **data-driven model learning** problem for nonlinear control. The 2025 drone paper addresses **disturbance rejection** via meta-learning + mirror descent. Together they represent a coherent MIT research thread: learning-based control for robotic/aerial systems under data scarcity and uncertainty.

## Entities mentioned
- [Navid Azizan](../entities/navid-azizan.md) — MIT; co-author

## Open questions
- How does SD-LQR scale to real robot DOFs (6+ axes, contact dynamics)?
- Relationship to Koopman operator methods (also linearize nonlinear dynamics)?
- Does the PVTOL result transfer to real hardware?

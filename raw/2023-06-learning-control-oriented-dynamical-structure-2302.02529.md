---
source_url: https://arxiv.org/abs/2302.02529
collected: 2026-05-09
published: 2023-06-24 (revised; submitted 2023-02-06)
venue: ICML 2023, Honolulu
author: Spencer M. Richards, Jean-Jacques Slotine, Navid Azizan, Marco Pavone
affiliation: MIT (Richards, Azizan); MIT + Stanford (Slotine); Stanford (Pavone)
arxiv: 2302.02529
---

# Learning Control-Oriented Dynamical Structure from Data (ICML 2023)

## Problem
Design feedback controllers for nonlinear dynamical systems learned from data. Challenge: data-driven dynamics models often lack structural properties needed for reliable stabilizing controller synthesis.

## Key insight
For control-affine systems ẋ = f(x) + B(x)u, learn a state-dependent coefficient (SDC) factorization of the vector field:
  f(x) - f(x̄) = A(x̄, x-x̄)(x-x̄)
This factorization always exists for continuously differentiable f (reduces to Jacobian at x = x̄) and enables state-dependent Riccati equation (SDRE) control — extending state-dependent LQR from regulation to trajectory tracking.

## Three learning approaches compared
1. **Naïve LQR**: Fit dynamics via standard regression → apply linearized LQR tracking. Baseline.
2. **CCM (Control Contraction Metric)**: Jointly learn dynamics + contraction metric M + gain function K via penalty-based formulation. Prior art.
3. **SD-LQR (Proposed)**: Jointly learn dynamics and SDC factorizations (A₀, {Aⱼ}) via semi-supervised composite loss:
   L^SDC = L^dyn_reg + L^SDC_reg + L^SDC_aux
   Uses 100–500 labeled samples + 10,000 unlabeled auxiliary points for constraint satisfaction.

## Results
- Benchmark systems: Planar Spacecraft (slightly nonlinear) and PVTOL (highly nonlinear, underactuated, non-minimum-phase)
- SD-LQR tracks double loop-the-loop for PVTOL with N=100 labeled samples; CCM and naïve LQR fail with limited data
- Median tracking error remains low and stable across data regimes; baselines degrade sharply
- Performance gap vs. oracle (known dynamics) decreases with more data

## Limitations
- Auxiliary loss is a relaxation — SDC satisfaction not guaranteed (hard constraint)
- Requires ~10k unlabeled auxiliary points
- Local stability guarantees only (SDRE theory); region of attraction unstudied
- Tested on 2 systems; generalization to higher-dimensional systems unclear

## Authors
- Spencer M. Richards — MIT
- Jean-Jacques Slotine — MIT (contraction theory; nonlinear control)
- Navid Azizan — MIT (also senior author on MIT drone adaptive control, 2025)
- Marco Pavone — Stanford (autonomous systems / robotics)

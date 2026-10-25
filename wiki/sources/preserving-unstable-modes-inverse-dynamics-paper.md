---
title: "Preserving Unstable Modes Through Inverse Dynamics in JEPA World Models (Toso, LeCun, Anderson, Bounou, 2026)"
type: source
url: https://arxiv.org/abs/2610.07540
fetch_url: https://arxiv.org/pdf/2610.07540v1
local_path: raw/2610.07540v1.pdf
sha256: f62037f5952e64da41598b51c538100623ab990e18f816909efd64999f3b2e73
author: Leonardo F. Toso, Yann LeCun, James Anderson, Oumayma Bounou
published: 2026-10-06
ingested: 2026-10-24
venue: arXiv (cs.LG), v1
format: "paper, 40 pp (15 main + appendices). Affiliations: Columbia (Toso, Anderson), NYU (Bounou), NYU + AMI Labs (LeCun). Code and checkpoints: jepa-control.github.io (not inspected)."
tags: [jepa, inverse-dynamics, ep-idm, sigreg, slow-feature-collapse, controllability, unstable-modes, detectability, lqr, cem, gradient-based-planning, cartpole, walker2d, pointmaze, dino-wm, dinov2, ibot, control-theory, ami-labs]
---

# Preserving Unstable Modes Through Inverse Dynamics in JEPA World Models (2026-10-06)

## Summary

This is a **control-theoretic** account of what a [JEPA](../concepts/world-models/jepa.md) world model's encoder must keep, and of why prediction plus [SIGReg](../concepts/world-models/sigreg.md) does not guarantee it. It works in the linear setting and validates on nonlinear visual tasks.
1. **Lemma 1.** A controller acting only on the latent can stabilise the plant **iff** every unstable or marginally stable mode is observable through the encoder (detectability, by the PBH test).
2. **Lemma 2.** Next-step prediction + SIGReg can be **exactly minimised by an encoder that discards the entire unstable subspace**: keep only the stable block and whiten it to an isotropic Gaussian.
3. **Theorem 1.** With rich enough action excitation, **exact endpoint inverse dynamics (EP-IDM)** makes the encoder **injective on the H-step reachable subspace**: `ker(F) ∩ range(C_H) = {0}`. EP-IDM reconstructs the whole action sequence `a_t … a_{t+H−1}` from `(z_t, z_{t+H})`. No direction any action sequence can reach within H steps is discarded.
4. **Theorem 2.** As H grows, the top eigenspace of the finite-horizon controllability Gramian converges to the **unstable subspace**. Unstable directions are the *most* identifiable ones.

Empirically:
- **CartPole:** latent-LQR success goes from **0% (SIGReg) to 100% (EP-IDM)**.
- **Walker2D:** EP-IDM keeps the gait's limit cycle and plans 2.91 m/s against SIGReg's ~0.
- **PointMaze** (stable dynamics): all variants do well.

The theory supplies the **formal mechanism** behind the wiki's [slow-feature collapse](../concepts/world-models/slow-feature-collapse.md) barrier #3 (inverse dynamics). It also says precisely **which** directions that barrier protects.

## Key claims

### Setup (§3)
- Encoder input: **two consecutive images, their difference, and proprioception** `s_t` (Eq. 4). So the state is available to the encoder, and the question is whether training keeps it.
- Loss: next-step (1SP) or multi-step (MSP) prediction + λ·SIGReg; EP-IDM **replaces** the SIGReg term in Eq. 6 (some variants use both).
- Linear analysis: affine encoder `z = Wy + b`, linear predictor, `d < n`. *"Our linear analysis removes representation capacity as a confounding factor."*

### Theory (§4–5)
- **Lemma 2's construction:** write `A = [[A_u, Δ],[0, A_s]]`, take `F = [0 F_s]` with `F_s = Q Σ_s^{−1/2}`. The latents are exactly standard Gaussian (SIGReg = 0), one-step error is zero, and every unstable direction lies in `ker(F)`. *"The training loss can be minimized while these modes are collapsed, making stabilization from the learned representation impossible."*
- **Theorem 1's limits, stated:** it describes the idealised exact-reconstruction regime. Exact reconstruction requires `rank(F C_H) = mH ≤ min{d, n}`, so when `mH > d` it is infeasible and EP-IDM is used as a *soft* bias. The excitation assumption needs the conditional action support to contain an open set.
- **Theorem 2:** requires `λ_min(Π_{u,H}) ≥ c_u α^{2H}`, meaning every unstable direction must get action-induced response growing at the unstable rate. It excludes unit-circle eigenvalues.

### Experiments (§6; MuJoCo; success over 10 trials)
- **CartPole (Table 1):**

  | Model | LQR SR | LQR MFS | CEM SR | GBP SR |
  |---|---|---|---|---|
  | Ground truth | 100% | 1.000 | 100% | 100% |
  | 1SP + SIG | **0%** | 0.202 | 100% | 90% |
  | MSP + SIG | **0%** | 0.247 | 100% | 100% |
  | 1SP + EP-IDM | **100%** | 0.999 | 100% | 100% |
  | MSP + EP-IDM + SIG | 100% | 0.996 | 100% | 100% |

  **Sampling- and gradient-based MPC succeed even on the SIGReg models**: they *"retain enough information for nonlinear replanning"* while their local linearisation cannot yield a stabilising LQR. The collapse shows up in **feedback design**, not in planning success.
- **Walker2D (Table 2, latent iCEM):** GT 3.61 m/s / 14.43 m. **1SP+EP-IDM 2.91 / 9.15**. 1SP+SIG 0.08 / 0.06; MSP+SIG 0.46 / 0.66. Phase portraits show EP-IDM keeps the right-hip limit cycle and SIGReg models do not.
- **PointMaze (Table 3, stable dynamics):** all from-scratch action-reconstruction variants reach ≥ 90% CEM and ≥ 70% LQR. MSP+SIG reaches 90% / 60%. Frozen **DINOv2** MSP: 50% / 20%. Frozen **iBOT** MSP: 100% / 80%. **[DINO-WM](../entities/dino-wm.md): 80% / 80%**.
- **Frozen encoders on CartPole (App. Table 5):** no DINOv2 configuration yields a stabilising LQR. With iBOT, a projector trained with EP-IDM reaches 100% LQR and CEM. EP-IDM *"preserve[s] control-relevant information captured by the frozen backbone, but cannot recover"* what the backbone lacks.
- Diagnostics (§6.4): EP-IDM reproduces the true vector field near the upright equilibrium and gives an empirical Lyapunov decrease over almost the whole tested region; MSP+SIG stabilises only a small neighbourhood.

## Reading notes (wiki inference)

> [!note] Theorem 1 explains "inverse dynamics keeps the arm and may lose the object"
> The [collapse synthesis](../syntheses/world-models/jepa-dynamics-collapse-fixes.md) §4 noticed that IDM-style terms help actuation-dominated tasks (Cube) and hurt or tie contact-dominated ones (Push-T). Theorem 1 gives a mechanism.
> - **The usual case.** Most IDM terms in that batch (SMWM, PLDM, GAWM, AVL stage 1) are **one-step**. In the linear picture, H = 1 gives `C_1 = B`, so one-step IDM protects only `range(B)`, the **directly actuated coordinates**.
> - **Objects are reached indirectly.** An object the agent moves only through contact sits in `range(AB, A²B, …)`. It is protected only by **multi-step** reconstruction with H long enough to reach it.
> - **Prediction.** **EP-IDM with H covering a contact event should keep the pushed object where one-step IDM drops it.** That is untested anywhere, and it is cheap to add to the synthesis's §6 shootout.
>
> Caveat: this is linear theory transplanted to contact dynamics, which are hybrid and non-smooth.

- **Planning success hides the collapse.** CEM and GBP reach 100% on the very models whose LQR fails 100% of the time. This is the strongest instance yet of the wiki's [world-model evaluation](../concepts/world-models/world-model-evaluation.md) warning: aggregate planning success can look fine while a control-critical direction is gone. **Latent-LQR around a known equilibrium** is a new, sharp diagnostic.
- **The encoder sees proprioception.** On CartPole and Walker2D the state is in the input. So the SIGReg failure is the objective *discarding* state it was given, which is a clean test of the paper's claim. It is not a perception failure. It also means the result does not show EP-IDM *extracting* state from pixels alone.
- **Frozen DINOv2 never stabilises CartPole**, and iBOT does. This adds to the wiki's evidence that frozen-backbone choice is load-bearing for control ([DINO-WM](../entities/dino-wm.md)).
- **Evidence quality:** 10 trials per cell. No seed count or spread is reported for the main tables. Three small MuJoCo tasks; no real robot. The theorems are linear; the nonlinear results are consistent with them but not covered by them.

## Entities mentioned
- [Yann LeCun](../entities/yann-lecun.md) · [AMI Labs](../entities/ami-labs.md) · [DINO-WM](../entities/dino-wm.md) · [LeWorldModel](../entities/leworldmodel.md) (cited as an end-to-end SIGReg JEPA)

## Concepts touched
- [Slow-feature collapse](../concepts/world-models/slow-feature-collapse.md): a formal account of the inverse-dynamics barrier and its scope (the H-step reachable subspace).
- [SIGReg](../concepts/world-models/sigreg.md): Lemma 2, a whitened stable-block encoder satisfies it exactly.
- [Optimal control](../concepts/robotics/optimal-control.md): detectability, the controllability Gramian, latent LQR, iCEM, gradient-based planning.
- [Gradient-based planning](../concepts/world-models/gradient-based-planning.md): GBP via SPSA through MuJoCo for the GT row.
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md): latent-LQR as a diagnostic; MPC success masks collapse.

## Open questions
- Does EP-IDM with a contact-spanning H keep the **pushed object** on Push-T, where one-step IDM loses it? (See the reading note.)
- From pixels **without** proprioception in the encoder input, does EP-IDM still recover the unstable modes?
- How does EP-IDM interact with SIGReg when both are on (`MSP + EP-IDM + SIG`)? Is there a weight window, as for the other barriers?
- Does the H → ∞ Gramian result say anything useful for systems with **no** unstable modes, such as quasi-static manipulation, where it gives no preference?

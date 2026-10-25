---
title: "LeHami: Symplectic Latent Dynamics for World Models (Yalovetzky, Balestriero, LeCun, 2026)"
type: source
url: https://arxiv.org/abs/2610.15267
fetch_url: https://arxiv.org/pdf/2610.15267v1
local_path: raw/2610.15267v1.pdf
sha256: 563f174b51b241fb079394822d60d5d4df686a85d1efa0f67631fd992613ea3c
author: Romina Yalovetzky, Randall Balestriero, Yann LeCun
published: 2026-10-11
ingested: 2026-10-24
venue: arXiv (cs.LG; cross-listed cs.AI, cs.RO), v1
format: "paper, 35 pp (9 main + appendices A–E). Affiliations: Courant/NYU (Yalovetzky, LeCun), Brown (Balestriero), AMI Labs (LeCun). Code: github.com/rominay/LeHami (not inspected)."
tags: [lehami, jepa, hamiltonian, symplectic, leapfrog, volume-preservation, rollout-contraction, leworldmodel, dino-wm, sigreg, savitzky-golay, pendulum, cem, mpc, time-reversibility, ami-labs]
---

# LeHami: Symplectic Latent Dynamics for World Models (2026-10-11)

> [!warning] Two Hamiltonian JEPAs, different failures
> This is **not** [Hamiltonian JEPA](../entities/hamiltonian-jepa.md) (Zoabi, Ali, Wolf; arXiv 2609.33497), which LeHami cites as its closest prior work, nor the hierarchical [H-JEPA](../entities/h-jepa.md). The three differ as follows:
> - **This paper** targets **predictor contraction during rollout**: each autoregressive step shrinks the latent cloud a little, and the shrinkage compounds.
> - **Hamiltonian JEPA** targets the **encoder** discarding the controllable state (the wiki's [slow-feature collapse](../concepts/world-models/slow-feature-collapse.md)).
>
> These are different failure modes in different components.

## Summary

**LeHami** replaces a [JEPA](../concepts/world-models/jepa.md) world model's predictor with a **learned, action-conditioned Hamiltonian flow** over a latent split into position-like *q* and momentum-like *p*. It is integrated with a **leapfrog (Störmer–Verlet) step, which is exactly symplectic**.
- **The guarantee.** Every rollout step preserves phase-space volume, **for any learned parameters and any action sequence**. This rules out three rollout collapse modes by construction (Prop. 1): uniform contraction, convergence to an asymptotically stable fixed point, and merging of distinct states.
- **How *p* is made.** The encoder produces *q* per frame; *p* is read off as **a fixed, zero-parameter Savitzky–Golay derivative over q_{t−3..t}**.
- **The comparison.** Against [LeWorldModel](../entities/leworldmodel.md) on 64×64 conservative and actuated **pendulums**:
  - LeHami predicts velocity much better and keeps latent log-volume exactly constant where LeWM's declines linearly.
  - It matches LeWM's best error with ≤ ⅛ the training compute.
  - It integrates at unseen sub-frame step sizes and runs backwards with round-trip error < 10⁻⁴ %.
- **Where it loses.** In goal-reaching planning it **loses to LeWM**: on position goals (0.48 vs 0.80), and on velocity and joint goals to LeWM with an untied 3-frame window (0.53 vs 0.80; 0.30 vs 0.64). It wins on compute per episode and on getting the velocity sign right among cheap models.

## Key claims

### Mechanism (§2)
- Separable Hamiltonian `H = K(S⁻¹p) + V(q, u)`, where `S = diag(e^σ)` is a learned scale gauge between *q* and *p*. **The action enters the potential**, so the generalised force is a *q*-gradient for every action. The step therefore stays symplectic under actuation, provided *u* is constant within a step.
- Multi-step loss: MSE on *q* + λ_p·MSE on *p* over *K* self-fed steps, plus any regulariser ([SIGReg](../concepts/world-models/sigreg.md) in practice) applied to **ground-truth embeddings, never the rollout**. Placements on q, p, or the concatenation are compared (App. E.3, Table 8).
- **Scope, stated by the authors (§2, App. C.2):**
  - (i) *"Shape, not size"*: volume preservation forbids degenerate failures but **does not bound rollout error growth**.
  - (ii) It does not replace a regulariser: it preserves volume, not distributional shape.
  - (iii) It is a geometric prior, not a physics simulator.
- Related work positions the paper against **Hamiltonian JEPA** (Zoabi et al.): there, the action enters through an external port, only a fixed slice of a wider code advances, and *"its explicit Euler step is not symplectic."* Here the action is inside *H*, the latent *is* the canonical phase space, and every step is exactly symplectic.

### Setup (§3.1)
- Two pendulum environments rendered at 64×64: **conservative** (3 rod lengths) and **actuated** (random piecewise-constant torque; 3 lengths × 3 masses). **Both preserve phase-space volume in the true dynamics.** That is the property LeHami builds in.
- Baseline: LeWM, swapping only the predictor (LeWM's 6-layer causal transformer, 3 context frames). Encoder: temporal ConvNet (main) and tiny ViT (App. E.2). **DINO-LeHami** on a frozen DINOv2 encoder against [DINO-WM](../entities/dino-wm.md).
- Probes: ridge / 25-NN / 2-layer MLP for θ and ω, fitted once and then frozen. Planning: [CEM](../concepts/robotics/optimal-control.md) MPC under a **15 TFLOP/episode** budget, horizon 30. Three training seeds, mean ± s.d.

### Results
- **Conservative pendulum, rollout (Fig. 4):**
  - Velocity MAE is **2.8× lower over the first 10 steps, 1.3× at the horizon**. Angle is level early, and LeHami pulls ahead from K ≈ 11.
  - The normalised cumulative log|det J| stays **exactly 0** for LeHami and **declines linearly** for LeWM.
- **Compute (App. Table 4, one seed):**
  - At every matched training budget, θ error is 1.45–4.2× lower and ω error 1.4–2.3× lower. The 0.75 PFLOP checkpoint beats LeWM's best within 6 PFLOP.
  - Per-run cost is similar: 6.0–6.5 PFLOP, 0.7–1.1 GPU-h per 100 epochs.
  - The predictor is 2.23M vs 3.31M parameters, plus LeWM's 0.27M projection head.
- **Actuated pendulum, anchor (Table 1):** with an MLP probe, LeHami's ω R² is **+0.987**; LeWM's is **−0.011**, below the predict-the-mean floor at every probe tier. **LeWM decodes θ better** (MAE 1.1–1.9 vs 2.9–23.0 ×10⁻² rad), because a per-frame encoder holds position and not velocity.
- **Time re-stepping (Fig. 5):** trained at Δt = 0.1 s, the model traces the same trajectory at ½ and ¼ step sizes. **Doubling the step breaks it** (the explicit integrator leaves its stability band).
- **Planning (Table 2, success at ≤ 15 TFLOP):**

  | Clause | LeWM W=1 | LeWM W=3 tied | LeWM W=3 untied | **LeHami** | floor (u=0) |
  |---|---|---|---|---|---|
  | Position | **0.800** | 0.633 | 0.696 | 0.480 | 0.060 |
  | Velocity | 0.184 | 0.473 | **0.800** | 0.527 | 0.240 |
  | Position + velocity | 0.142 | 0.400 | **0.636** | 0.304 | 0.040 |

  - **Sign decomposition (Table 10):** LeHami gets the velocity sign right 0.800 vs untied LeWM's 0.962. Tied and W=1 LeWM are below the 0.680 coasting floor. LeHami does this at 8.05 vs 13.65 TFLOP.
  - The authors' own conditioning (App.) places the bottleneck in **reaching the goal angle** (P(θ) = 0.48 vs 0.63–0.70), *"not the direction of the velocity."*
- Both models decode rod length and mass along the whole rollout (App. Table 11), so the planning gap is not a system-identification failure.

### Limitations (stated)
- **Strongly dissipative systems (e.g. heavy friction) contract phase-space volume, so a purely symplectic latent cannot represent them.** A PSD damping term `D = LLᵀ` is proposed in App. C.4 and not run.
- It targets velocity-aware tasks; *"purely static pose tasks are served well by … unconstrained predictors."*
- The fixed SG stencil could be replaced by a learned *p*, which the authors see as the path to closing the planning gap.
- AI use statement: AI assisted parts of the writing and code, and checked the proof of Proposition 2.

## Reading notes (wiki inference)

> [!note] The guarantee's premise fails exactly where manipulation lives
> Exact volume preservation is the right prior when the **true** dynamics preserve volume, and both test systems were chosen so they do. Contact, friction and grasping, the regime of the wiki's robot-learning interest, are **dissipative**. The authors say so: a symplectic latent *"cannot absorb"* dissipation without unphysical diverging auxiliary dimensions (App. C.4). Until the port-Hamiltonian extension is run, this is a result about conservative and lightly actuated systems, and nothing here tests it on the [LeWM benchmark suite](../entities/leworldmodel.md) (Push-T, Cube, Reacher, Two-Room). Contrast [Hamiltonian JEPA](../entities/hamiltonian-jepa.md), which gave up exact symplecticity (port + damping, Euler step) and **was** run on that suite.

> [!note] "Velocity by construction" is a fixed finite difference
> The momentum channel is a Savitzky–Golay derivative over the last four encoder outputs, a zero-parameter frame-stack difference. The paper's own comparison shows that a **learned untied 3-frame window on LeWM gets the velocity sign right more often** (0.962 vs 0.800) and plans better, at higher cost. So the structural contribution here is the **volume-preserving rollout and the compute saving**. Representing velocity is something a temporal window already does. This parallels [MotionJEPA](../entities/motionjepa.md)'s pixel-difference target: both make the temporal derivative explicit.

- **A new collapse diagnostic.** The cumulative log|det J| of the one-step predictor measures **rollout** contraction, which none of the five encoder-side diagnostics in the [collapse synthesis](../syntheses/world-models/jepa-dynamics-collapse-fixes.md) measure. LeWM's linear decline on a simple pendulum is evidence for the long-horizon degradation the wiki already tracks (25 → 75-step drop, [stable-worldmodel](stable-worldmodel-paper.md)).
- **Time reversal** is pitched for backward reachable sets in safety-critical control. That is a direct line to the [safety filters](../concepts/robotics/safety-filters.md) concept, though no reachability experiment is run.
- Evidence quality: three seeds with s.d. on main results; the compute table is one seed. Environments are tiny and synthetic (64×64 pendulum). No real robot. A full reproducibility statement covers seeded generators, split manifests with dataset hashes, and a notebook that regenerates every table without a GPU.

## Entities mentioned
- [LeHami](../entities/lehami.md) · [Randall Balestriero](../entities/randall-balestriero.md) · [Yann LeCun](../entities/yann-lecun.md) · [AMI Labs](../entities/ami-labs.md)
- [LeWorldModel](../entities/leworldmodel.md) (baseline) · [DINO-WM](../entities/dino-wm.md) (frozen-encoder baseline) · [Hamiltonian JEPA](../entities/hamiltonian-jepa.md) (closest prior work)

## Concepts touched
- [JEPA](../concepts/world-models/jepa.md) · [SIGReg](../concepts/world-models/sigreg.md) (placement on q / p / concatenation)
- [Slow-feature collapse](../concepts/world-models/slow-feature-collapse.md): adjacent, but a different failure; see the warning above.
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md): log-det volume diagnostic; velocity probes as half the state.
- [Optimal control](../concepts/robotics/optimal-control.md): CEM-MPC under a FLOP budget.

## Open questions
- Does the PSD-damping (port-Hamiltonian) extension keep any useful guarantee on **dissipative, contact-rich** tasks? That is the result that would matter for manipulation.
- LeHami on the LeWM suite (Push-T / Cube), head to head with Hamiltonian JEPA's 91.9 % Cube.
- Does a learned *p* close the planning gap while keeping volume preservation, as the authors expect?
- Volume preservation and slow-feature collapse are orthogonal. An encoder that drops the agent still yields a perfectly symplectic rollout of the background. Would a combination (symplectic predictor + an action-grounded encoder barrier) compound?

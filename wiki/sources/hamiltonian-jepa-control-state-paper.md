---
title: "Hamiltonian JEPA: Action-Conditioned World Models with an Inherited Control State (Zoabi, Ali, Wolf, 2026)"
type: source
url: https://arxiv.org/abs/2609.33497
local_path: raw/2609.33497v1.pdf
sha256: 441558a3fc57ab46588dd9dd2bca6f9e206bde209e6d61cb05adbd0a2b024f4a
author: Tamim Zoabi, Ameen Ali, Lior Wolf
published: 2026-09-27
ingested: 2026-10-22
venue: arXiv (cs.LG), v1
format: "paper, 21 pp (9 main + appendices A–I). Affiliation: Blavatnik School of Computer Science, Tel Aviv University (all three authors). Code: github.com/tmz-lab/hjepa (linked from p. 1; not inspected)."
tags: [hamiltonian-jepa, jepa, port-hamiltonian, bures-wasserstein, anti-collapse, sigreg, leworldmodel, inverse-dynamics, action-sensitivity, slow-feature-collapse, cem, push-t, ogbench, reacher, two-room, structured-dynamics, tel-aviv-university, lior-wolf]
---

# Hamiltonian JEPA: Action-Conditioned World Models with an Inherited Control State (Zoabi, Ali, Wolf, 2026)

> [!warning] Name collision
> The paper calls itself **"H-JEPA"**. That is a different model from the [hierarchical H-JEPA](h-jepa-hierarchical-world-models-paper.md) (Zhang, Terver, Rabbat, LeCun, Balestriero, arXiv 2610.06805, posted a week later), which has its own [entity page](../entities/h-jepa.md). Both names trace back to LeCun's 2022 position paper, where H-JEPA means *Hierarchical* JEPA. This paper cites that position paper (as the origin of prediction in representation space) but **never mentions the hierarchical meaning**. The word "hierarchical" does not occur anywhere in it. In this wiki the model is always called **Hamiltonian JEPA**.

## Summary

Hamiltonian JEPA is a [LeWorldModel](../entities/leworldmodel.md)-style action-conditioned JEPA. It is trained from pixels with no reconstruction and planned with CEM. It changes three things about **which vector the planner scores and how actions are allowed to move it**:

1. **Perception and control state are separate.** The encoder outputs a wide code *h* (192-d) on a fixed-radius sphere, and the anti-collapse regulariser acts only on *h*. The planner scores a **fixed, random, never-trained orthonormal slice** *s = Uᵀh*, of rank 32–192 depending on the task. Because the slice is linear and fixed, *s* **inherits** the code's covariance and needs no objective of its own.
2. **The regulariser is a Bures-Wasserstein (BW) moment penalty instead of SIGReg.** The paper argues that SIGReg's restoring force fades to zero as a direction's variance dies, while BW's stays constant.
3. **The predictor has a port-Hamiltonian form, with an orthonormal action port.** Each step adds a learned energy-driven drift, a learned damping term, and an action injection through a matrix whose columns are orthonormal. **Port-inverse consistency (PIC)** reads the executed action back through the transpose of that matrix. The paper proves that PIC is not an auxiliary action decoder: it is **exactly the prediction error projected onto the action directions**, so it amounts to reweighting the rollout loss.

The model trains for **10 epochs on one RTX A5000**. It is best or tied on all four LeWM benchmarks against PLDM, LeWM, Sub-JEPA and Delta-JEPA. The largest margin is **OGB-Cube, 91.9% vs 79.3%** for the action-decoding Delta-JEPA, which trains for 50 epochs. All results are in single-scene simulation with short-horizon CEM.

## The machinery in plain engineering terms

**Fixed-radius code (§3.1).** Each frame's code is mean-centred and rescaled to length √D. That is LayerNorm with no learnable gain or bias. The encoder therefore cannot shrink everything to make prediction easy (the "scale-degenerate" solution of latent-MSE losses) or inflate it. It can only change *direction*, so the regulariser can redistribute variance but not create it.

**Bures-Wasserstein prior (§3.3, App. H).** Fit a Gaussian to the batch of codes and penalise its 2-Wasserstein distance to a target isotropic Gaussian. In closed form this is ‖mean‖² plus Σᵢ(√λᵢ − 1)², a quadratic penalty on each direction's **standard deviation**. The argument for it concerns force as a direction dies (σ → 0):
- BW's gradient on σ goes to **−2**, a constant pull back toward unit spread.
- The Euclidean covariance penalty ‖Σ − I‖²_F has gradient 4σ(σ² − 1) → **0**.
- SIGReg is a bounded, smooth statistic of the characteristic function. Near a point mass it is quadratic in σ, so its force is about −2κσ → **0**.

In engineering terms, BW behaves like a spring with a constant force near zero length, and the other two behave like springs that go slack exactly when you need them. The design depends on this. **The D − r code directions outside the slice get no gradient from prediction or PIC**, so the prior alone has to keep them open. The authors report that SIGReg runs inside this architecture collapsed within about 50–100 steps (Table 1). They say explicitly that this is **not** a claim about SIGReg inside LeWM, where the prediction loss also acts on every coordinate (§4.1).

**Inherited covariance (§3.2, App. G).** Cov(s) = Uᵀ Cov(h) U. At the prior's target, *s* is isotropic except for one direction, which has eigenvalue 1 − ‖Uᵀe‖² ≈ 1 − r/D. That direction is the image of the centring direction that LayerNorm removes. At r = D it is an exact null direction, and the trained PushT r=192 model has a smallest eigenvalue of **1.3×10⁻⁶**, as predicted. Trained spectra are not flat: eigenvalues range from 0.015 to 2.48, and Cube's minimum falls below the Marchenko-Pastur range (Table 13). A **learnable** U co-adapted with the losses and collapsed the state's rank, which is why U is frozen.

**Port-Hamiltonian step (§3.4).** The state update is one explicit Euler step of

`ṡ = (J − R(c)) ∇ₛH(s, v) + G(c) ā`

- **H** is a learned scalar "energy", given by an MLP of the phase c = [s, v], where v = s_t − s_{t−1} is a finite-difference velocity.
- **J** is the fixed symplectic (rotation) matrix. On its own, J∇H moves the state *along* energy contours without changing the energy, like a frictionless oscillator.
- **R = LLᵀ** is a learned, positive semidefinite damping matrix, so this term can **only remove energy**, like friction.
- **G** is the **input port**. It maps the normalised action into a state displacement, and its columns are made orthonormal by a differentiable QR factorisation.

Physically, the predictor is allowed to model coasting, oscillation and friction, and to treat actions as a separate, additive force input. That is the standard control-affine structure (ẋ = f(x) + B(x)u; see [optimal control](../concepts/robotics/optimal-control.md)), with f constrained to be energy-plus-damping. The latent coordinates are **not** claimed to be physical positions and momenta (§5).

**Why the port is orthonormal.** An unconstrained input matrix B factors into a direction and a gain. The gain can trade off against the encoder's scale, which lets optimisation move scale without improving content (Table 1). With orthonormal columns, every action Jacobian singular value equals Δt, so **one unit of normalised action produces exactly one unit of latent displacement, along d_a orthogonal directions**. The price is that action gain cannot vary with state (§5).

**PIC is a reweighting, not a decoder (§3.5, App. B).** PIC subtracts the predicted passive flow from the observed displacement and multiplies the remainder by Gᵀ. Since GᵀG = I, Gᵀ is G's exact pseudoinverse. Substituting the Euler step gives the identity `û − ā = (1/Δt) Gᵀ δ`, where δ is the rollout error (Eq. 11). So L_pred + L_PIC is a single quadratic form in the rollout error, which counts error along the action-port directions **1 + r/(d_a Δt²)** times more than error elsewhere. That factor is 17 on Two-Room, 33 on Reacher, **97 on PushT at r=192** and 7.4 on OGB-Cube. There is no learned inverse model and no free scale. The model cannot shortcut PIC by rescaling, because the scale is fixed. It cannot shortcut it by rotating the port away from where the error is either, because the same port injects the action and prediction would get worse.

**Why this should help planning.** CEM ranks candidate action sequences by the terminal distance ‖ŝ_{t+5} − s_goal‖². If the model blurs the difference between action sequences, every candidate scores the same. The structure here (a) guarantees that actions always move the state by a fixed, well-conditioned amount, (b) concentrates training accuracy on the directions actions push, and (c) scores only the slice. The slice keeps dimensions that exist only to satisfy the prior out of the planning metric.

## Key claims

**Main results (Table 2).** Success %, 500 test episodes per task, mean ± std over 3 training seeds (3072, 7, 11) under the Delta-JEPA protocol:

| Method | Two-Room | Reacher | PushT | OGB-Cube |
|---|---:|---:|---:|---:|
| PLDM | 93.73 ± 1.03 | 64.33 ± 2.14 | 76.13 ± 1.70 | 57.27 ± 1.53 |
| LeWM | 74.93 ± 0.42 | 79.87 ± 0.90 | 84.53 ± 1.50 | 64.13 ± 1.89 |
| Sub-JEPA | 90.60 ± 0.53 | 81.00 ± 2.40 | 63.73 ± 0.12 | 62.67 ± 1.45 |
| Delta-JEPA (50 ep.) | **100.00 ± 0.00** | 81.33 ± 0.50 | 89.07 ± 1.90 | 79.27 ± 1.81 |
| **Hamiltonian JEPA (10 ep.)** | **100.00 ± 0.00** | **86.13 ± 0.23** | **90.40 ± 0.60** | **91.93 ± 1.30** |

- The margins are +4.8 on Reacher and **+12.7 on OGB-Cube**. PushT is within one standard deviation of Delta-JEPA, and Two-Room is tied at saturation (§4).
- Sub-JEPA's self-reported numbers (95.0 / 84.0 / 89.0 / 76.3, on 50 episodes) are also below Hamiltonian JEPA's.
- **Paired test against the official LeWM checkpoint**: 200 matched PushT episodes, **88.5 vs 82.0, McNemar p ≈ 0.053** (§4).
- **Per-task tuning**: state rank r = 32 (Two-Room, Cube), 64 (Reacher), 192 (PushT). The checkpoint epoch is also chosen per task: 8, 6, 10 and **3** respectively. Both were selected on one held-out pilot seed that is excluded from the averages.
- **Compute**: D = 192, ViT-T/14 from scratch, AdamW lr 5e-5, bf16. CEM uses horizon 5, 300 samples, 30 iterations on PushT and 10 elsewhere. Losses are summed **unweighted** (App. C).

**Ablations (§4.1).** Most are on PushT r=64 and OGB-Cube r=32. Table 4 uses N = 300.
- **The predictor matters even on the same representation (Table 3, PushT, K_p = 5):**

  | Predictor | Representation | Params (total / dynamics) | Success |
  |---|---|---|---:|
  | LeWM's AdaLN transformer | LeWM's native SIGReg embedding | 18.0M / 10.8M | 20% |
  | Same transformer | Hamiltonian JEPA *s* | 9.6M / 3.3M | 84% |
  | Port-Hamiltonian + PIC, r=64 | Hamiltonian JEPA *s* | 7.2M / **0.86M** | 92% |
  | Port-Hamiltonian + PIC, r=192 | Hamiltonian JEPA *s* | 11.6M / 5.4M | 94% |

- **Structure vs MLP** (both with PIC): swapping the port-Hamiltonian step for an MLP costs −8.3 on PushT (93.3 → 85.0) and −7.6 on Cube (91.9 → 84.3).
- **PIC is worth a lot on PushT and little on Cube.** Removing it costs 18.3 on PushT (→ 75.0) and 2.9 on Cube (→ 89.0, within noise). The paper's explanation comes from the predictor audit. On PushT the control flow is only 0.13× the passive flow, so an unweighted loss is dominated by passive error. On Cube it is 1.53×, so the loss already emphasises the action directions. The MLP **without** PIC falls to 32.0 on PushT.
- **The tie between readout and port is half the gain.** Keeping the learned port in the forward step but reading out through a fixed random orthonormal Q gives 83.7, between no PIC (75.0) and tied PIC (93.3). Breaking the tie adds a term (QᵀG − I)ā that pulls the port toward a fixed frame, against what prediction wants (App. B, Eq. 17).
- **Prior placement and type.** Moving BW from *h* onto *s*: 93.3 → 86.3. Replacing BW with SIGReg on *h*: **36.7**.
- **Train at the planning horizon (Table 5, PushT, N = 50):** (K_p, K_PIC) = (1,0) gives 12; (1,1) gives 34; (3,3) gives 94; (5,1) gives 90; (5,5) gives 94. One-step prediction does not compose into a rollout you can plan with.
- **Rank is task-dependent (Table 6).** Two-Room saturates at every rank. Reacher (94 at r=64 vs 78 at r=192) and Cube (96 at r=32 vs 76/78 at r=192) degrade at full rank. PushT improves up to r = D.
- **The planner uses directions that physical probes do not see.** On the PushT r=64 candidate sets, split each terminal state into its linear reconstruction from probed physical variables plus the orthogonal remainder. Ranking candidates by the **remainder alone** gives Spearman **0.997** with the full ranking and recovers **89%** of CEM elites. The physical part gives 0.66 and 38%.

**Probing (App. D, Tables 8–10).** Hamiltonian JEPA is best on the **directly controlled** variables: PushT agent location (linear MSE 0.028 vs LeWM 0.062), Cube end-effector position (0.007 vs 0.027) and Cube joint velocity (0.740 vs 1.069). It is **worse on the pushed object**: PushT block location 0.152 vs LeWM 0.038, and block angle 0.331 vs 0.199. It plans better anyway. "Planning quality is thus not monotone in object-pose decodability."

**Predictor audit (App. E, Tables 11–12).** Measured on 24,576 held-out transitions:
- The Stiefel constraint holds to 4.8×10⁻⁷.
- **PushT is dissipation-dominated**: ‖R∇H‖/‖J∇H‖ = 4.35, and damping rises with latent speed (corr 0.48), consistent with the friction-heavy contact dynamics of pushing. Each learned field linearly explains 88–90% of the physical increment.
- **OGB-Cube is actuation-dominated** (control/passive = 1.53), and per-field physical alignment there is weak (R² 0.27–0.32).
- The authors read the structure as an inductive bias that is interpretable where the task allows, not as system identification.

**History mechanism (App. F).** An earlier learned three-frame mixer put about 90% of its weight on the latest state and ignored the differences (cosine about 0.99 with them zeroed). The parameter-free phase [s, v] replaced it.

## Reading it critically

> [!warning] The comparison set leaves out the closest relatives
> [SMWM](../entities/smwm.md) (Ivashkov, Balestriero, Schölkopf), which makes inverse dynamics the perception objective and reported **84** on OGB-Cube in [its own paper](sensorimotor-world-models-paper.md), is cited in related work but **not in Table 2**. Delta-JEPA (Zhang Zhenghao et al., arXiv 2606.31232; a different Zhang from the hierarchical H-JEPA's Wancong Zhang) is the action-decoding baseline. Table 2 says the baselines were "evaluated under the Delta-JEPA protocol." It does not say whether they were re-run or their numbers taken from the Delta-JEPA paper. LeWM's **74.9%** on Two-Room here is well below the low-90s figure the wiki records elsewhere (see the warning on [SIGReg](../concepts/world-models/sigreg.md)), which suggests protocols are not interchangeable across papers.

> [!note] Tuning asymmetries
> Hamiltonian JEPA picks its **state rank and checkpoint epoch per task** on a held-out pilot seed. The OGB-Cube headline uses the **epoch-3** checkpoint. That is early stopping, done honestly (on a seed excluded from the averages), but nothing says the baselines got the same per-task checkpoint selection. The "10 vs 50 epochs" framing is about training length. Per-epoch cost is not reported, and the rollout loss runs K_p = 5 open-loop steps per sample. The ablations also mix references. The Cube "full model" in Table 4 is the 3-seed, N = 500 Table 2 mean, while the other rows are seed 11 at N = 300. The paper says the resulting 2.9-point PIC gap is within noise.

> [!note] "LeWM 20%" in Table 3 is not LeWM as published
> That row runs LeWM's transformer on its native embedding **with K_p = 5 multi-step training**, inside this paper's recipe. Table 2's LeWM (84.5% on PushT) and the paired official-checkpoint test (82.0%) are the fair LeWM numbers. Table 3 isolates the effect of the predictor class. It is not a 20% → 94% improvement over LeWM.

> [!note] Significance is thin where the margin is small
> Against the official LeWM checkpoint on matched episodes, the PushT gain is **p ≈ 0.053**. The Reacher and Cube margins over Delta-JEPA in Table 2 are well outside the standard deviations across three seeds, so those are the claims to take seriously.

- **The theory is clean and small.** The PIC identity (Eq. 11) is a three-line derivation, and it is the paper's most reusable idea. *If you tie an inverse readout to the transpose of an orthonormal input map, an "auxiliary" inverse-dynamics loss becomes a reweighting of the forward loss.* The SIGReg force analysis (App. H) is a local expansion near a point mass. It explains failure *inside this architecture*, where off-slice directions get no other gradient. It is not a general case against SIGReg, and the authors say so.
- **Evidence scope is narrow.** Four single-scene simulators, offline data, 5-step CEM, no gradient-based planning, no real observations, and explicit Euler (energy properties not preserved; §5).

## How it relates to slow-feature collapse

[Slow-feature collapse](../concepts/world-models/slow-feature-collapse.md) is the failure in which the encoder keeps only what is constant within an episode (the scene) and the predictor learns the identity. The [hierarchical H-JEPA paper](h-jepa-hierarchical-world-models-paper.md) (App. L) proved that no regulariser on the marginal distribution of embeddings, SIGReg included, can exclude it, and that an inverse-dynamics term is the only barrier that worked.

**The paper does not test this.** All four benchmarks are fixed-scene simulators, which is exactly the regime where the wiki notes the failure does not appear. The architecture does bear on it, though. The following is the wiki's own inference, not a claim the paper makes:

- **The orthonormal port forbids an action-blind predictor.** In LeWM a collapsed encoder plus an identity predictor reaches zero loss, because the predictor is free to ignore the action. Here every action is *forced* to displace the state by exactly ā (unit singular values), and the passive flow depends only on [s, v], not on ā, so it cannot cancel that displacement. An encoder that is constant within an episode would therefore pay a prediction error of about Var(ā) on every step. **That is an Ω(1) floor of the same kind as the inverse-dynamics floor (Prop. 3 of the hierarchical H-JEPA paper), and it comes from the predictor's structure rather than from an extra loss.**
- **It needs no action labels beyond what conditioning already uses.** PIC regresses the executed action, but Eq. 11 shows it is just the conditioned prediction error reweighted. An action-conditioned world model needs those labels anyway. Like every IDM-style barrier, though, it does nothing for **action-free video**.
- **Caveats.** The D − r off-slice code directions are held open only by the BW prior and could carry the background freely, which is harmless as long as the slice moves with actions. In a varied scene, a uniform-gain port may also be a poor fit when action effectiveness depends on the scene. Whether this beats an explicit IDM on DROID-like data is an open experiment.

So the separation of perception from control state is, by itself, **not** the protection. The slice inherits whatever the code contains. What would protect is the **constrained action port**. That makes Hamiltonian JEPA a fourth answer alongside [PLDM](pldm-paper.md)'s IDM term, [SMWM](sensorimotor-world-models-paper.md)'s IDM-as-objective, and Delta-JEPA's latent-difference decoder, and it is the only one of the four that adds no parameters.

## Entities mentioned
- [LeWorldModel](../entities/leworldmodel.md) · [PLDM](../entities/pldm.md) · [SMWM](../entities/smwm.md) · [DINO-WM](../entities/dino-wm.md) · [Push-T](../entities/pusht.md)
- [H-JEPA (hierarchical; name collision)](../entities/h-jepa.md)
- [Yann LeCun](../entities/yann-lecun.md) · [Randall Balestriero](../entities/randall-balestriero.md) (cited, as authors of LeJEPA/LeWM/SIGReg)
- No pages yet: Delta-JEPA, Sub-JEPA, OGBench, Tel Aviv University, Lior Wolf.

## Concepts touched
- [JEPA](../concepts/world-models/jepa.md) — action-conditioned variant with a separate control state.
- [SIGReg](../concepts/world-models/sigreg.md) — the vanishing-force argument (App. H) and the 36.7% result when SIGReg replaces BW inside this architecture.
- [Slow-feature collapse](../concepts/world-models/slow-feature-collapse.md) — not tested; see the inference above.
- [Gradient-based planning](../concepts/world-models/gradient-based-planning.md) — a further answer to "what makes a latent good for planning": action-sensitive and well-scaled along the port. The paper uses CEM only.
- [Latent space](../concepts/world-models/latent-space.md) · [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — the evidence that physical probes miss what the planner ranks on.
- [Representation evaluation](../concepts/learning/representation-evaluation.md) — probing results that do not track planning quality.
- [Optimal control](../concepts/robotics/optimal-control.md) — control-affine, port-Hamiltonian structure, and the link to balanced truncation.
- [Inductive bias](../concepts/learning/inductive-bias.md) — mechanics used as a structural prior without any claim of system identification.

## Open questions
- **Changing scenes.** Does the orthonormal port actually prevent slow-feature collapse on DROID-like data, as the reasoning above suggests? This is a cheap, decisive experiment.
- **Gradient-based planning.** Does the well-conditioned action Jacobian make GBP competitive with CEM here? The paper never tries it.
- **Longer horizons.** Every result uses a 5-step horizon with training at that horizon. Does explicit Euler drift once the horizon grows, given that energy is not preserved?
- **Rank.** Can the state rank be learned instead of picked per task, and what is the right rank for a multi-task household model?
- **Head-to-head with explicit IDM baselines.** How does it compare with SMWM and an explicit IDM under one protocol? And does BW help LeWM itself, where SIGReg acts on the same coordinates as prediction?
- **Real hardware.** Do the gains carry to real observations and closed-loop control? The authors list this as untested (§5).

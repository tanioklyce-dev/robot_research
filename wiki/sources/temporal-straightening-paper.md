---
title: "Temporal Straightening for Latent Planning"
type: source
url: https://arxiv.org/abs/2603.12231
local_path: raw/temporal-straightening_2603.12231.pdf
author: Ying Wang, Oumayma Bounou, Gaoyue Zhou, Randall Balestriero, Tim G. J. Rudner, Yann LeCun, Mengye Ren
published: 2026-03-12
ingested: 2026-08-26
venue: "ICML 2026 (PMLR 306); arXiv v3 2026-08-11"
format: paper (29 pp)
tags: [jepa, world-model, gradient-based-planning, curvature, latent-space, perceptual-straightening, dino-wm, conditioning, icml, lecun]
---

# Temporal Straightening for Latent Planning

NYU + Brown + Toronto. Code: `agenticlearning.ai/temporal-straightening/`.

## Summary

Attacks the same problem as [Closing the Train-Test Gap](train-test-gap-world-models-paper.md) — gradient-based planning through a latent world model underperforms CEM — from the opposite end. Rather than fixing the training *distribution*, it fixes the **geometry of the latent space itself**. Borrowing the **perceptual straightening hypothesis** from human vision (Hénaff et al. 2019: visual systems transform complex natural videos into *straighter* internal representations), it adds a **curvature regularizer** to a [JEPA](../concepts/world-models/jepa.md) world model so that latent trajectories are locally straight. Two consequences are claimed and one is proved: **Euclidean distance in latent space becomes a better proxy for geodesic distance**, and **the planning objective becomes better conditioned**.

## Why this matters to the wiki's existing material

> [!warning] It supplies the missing justification for how LeWM scores plans
> The wiki records [LeWM](../entities/leworldmodel.md)'s CEM recipe in detail: candidate trajectories are scored by **Euclidean distance in embedding space** between the final predicted embedding and the goal-image embedding. That step has always been assumed rather than argued. This paper states the condition under which it is valid — **Euclidean distance approximates geodesic distance only when the latent trajectories are straight** — and shows that pretrained visual encoders produce trajectories that are *"usually highly curved."*
>
> So a scoring function the wiki has documented as a mechanical detail turns out to rest on a geometric property that generally does not hold, and which has to be trained for.

## Key claims

### The theory

For affine latent dynamics `z_{t+1} = Az_t + Ba_t` with a Euclidean goal cost, the planning Hessian is `H = 2 J_Φ^T J_Φ ⪰ 0`, and its effective condition number equals that of the finite-horizon **controllability Gramian** `W_K`. The bound:

- `κ_eff(H) = κ(W_K) ≤ κ(B)² κ(A)^{2(K−1)}`
- if the transition is **ε-straight** (`ε = ‖A − I‖₂ < 1`): `κ_eff(H) ≤ κ(B)² ((1+ε)/(1−ε))^{2(K−1)}`
- for `ε ≤ ½`: **`κ_eff(H) ≤ κ(B)² e^{6εK}`**

Since the objective is quadratic with `H ⪰ 0`, gradient descent converges linearly at a rate set by the condition number — so bounding `κ_eff` bounds planning convergence, and the bound degrades *gracefully* with horizon `K` when ε is small.

> [!note] The theorem is for linear dynamics; the system is not linear
> Stated plainly by the authors: *"For nonlinear predictors `z_{t+1} = f_θ(z_t, a_t)`, analogous guarantees require controlling products of state-dependent Jacobians and higher-order terms, which can be an exciting future work direction."* What they offer for the nonlinear case is empirical — "straightening yields a loss landscape with reduced non-convexity." The same scope pattern the wiki records on [identifiability](../concepts/world-models/identifiability.md): a clean theorem one regime away from the system in use.

### Implicit straightening — the finding that reframes the method

**The JEPA prediction objective alone already induces straightening.** The explicit curvature regularizer "further strengthens and stabilizes this effect."

That has a direct consequence for reading the results: the paper reports improvement *"even without the straightening regularization"* whenever projectors or encoders are trained at all, and attributes it to implicit straightening. So the ablation is not clean — some of the gain belongs to *training a projector*, not to the curvature loss. The authors say so themselves, which is the right handling, and it is also a substantive claim in its own right: **straightening may be part of why latent prediction works at all.**

### Results (50 test episodes, mean ± std over 3 eval seeds, GD planner)

Spatial features, the configuration where the method works best. `✓` = curvature regularizer on.

| Encoder | dim | curv | Wall OL / MPC | UMaze OL / MPC | PM-Medium OL / MPC | PushT OL / MPC |
|---|---|:--:|---|---|---|---|
| DINOv2 patch (**DINO-WM baseline**) | 14×14×384 | ✗ | 52.67 / 76.67 | 35.33 / 80.67 | 40.83 / 76.67 | 56.00 / 66.00 |
| DINOv2 patch + proj | 14×14×8 | ✗ | 80.00 / 90.67 | 44.00 / 81.33 | 72.00 / 96.67 | 70.00 / 78.67 |
| **DINOv2 patch + proj** | 14×14×8 | **✓** | **90.67 / 100.00** | **94.00 / 100.00** | **82.67 / 98.67** | **77.33 / 85.33** |
| ResNet from scratch | 14×14×8 | ✗ | 1.33 / 6.67 | 14.67 / 66.00 | 18.67 / 57.33 | 71.33 / 70.67 |
| **ResNet from scratch** | 14×14×8 | **✓** | **84.67 / 100.00** | 64.67 / 98.67 | 80.67 / 99.33 | 70.67 / 91.33 |

Headline: **open-loop planning improves 20–60%, MPC 20–30%** with a simple gradient-based planner. The UMaze open-loop jump — **35.33 → 94.00** — is the largest single effect. The ResNet-from-scratch row going **1.33 → 84.67** on Wall is explained by "extremely high curvature… suggesting a degradation of features" in the unregularized case.

> [!note] The gains are not universal, and the paper shows the failures
> With **global** (1×384) features, straightening does nothing on PushT: **2.00 → 2.00** open-loop and **11.33 → 8.67** MPC. The paper also flags "abnormally low success rates" for ResNet with spatial features on several environments, and notes that implicit straightening is weakest on UMaze with the projector — "which also results in the lowest improvement in planning." Explicit straightening adds *"more than 10% boost"* over implicit, not the whole effect.

**Long horizon** (Table 2, spatial features), where prediction errors compound: DINO-WM PushT 3.33/27.33 and PM-Medium 35.00/65.33; ResNet+curv reaches **76.00 / 98.67** on PM-Medium. Adding a **combined planning cost** `L_plan = L_spatial + 0.1·L_agg` (fine-grained local cost plus a global distance term) improves over spatial-only across all models under MPC — suggesting "long-horizon planning may benefit from objectives that combine fine-grained local costs with global distance geometry."

### Teleported-PointMaze — the control experiment worth stealing

To test whether straightening captures **dynamics** rather than exploiting **appearance**, they modify PointMaze so that touching the right wall **instantly teleports the agent to the left**. This "creates states that are far in the pixel space but have small temporal distance." A straightened model plans to reach the target *by leveraging the teleportation*.

That is a clean, cheap probe of exactly the confound that dogs every latent-planning claim — is the latent space encoding what things look like, or how they evolve? — and it belongs alongside the wiki's other behavioral probes in [spatial intelligence](../concepts/world-models/spatial-intelligence.md).

### GD vs CEM, stated honestly

- CEM needs **≥200 samples × 10 iterations** for competitive performance, making it roughly **10× slower** than GD in wall-clock (open-loop PushT, 50 trajectories, single L40S).
- **"Consistent with prior work, CEM often obtains higher absolute success rates than GD, but at substantially higher computational cost. Importantly, straightening largely reduces the performance gap between GD and CEM."**
- Straightening improves **both** GD and CEM across environments and architectures.

## Setup

Subplanner horizon 25; open-loop executes 25 actions, MPC executes the first 5 (one frameskip chunk); Adam, lr 0.1, 100 optimization steps, zero action initialization; history 3 frames, frameskip 5. Straightening strength λ = 0.1 by default, selected by MPC on two held-out validation seeds.

> [!warning] The no-straightening baseline uses a different learning rate
> Footnote to Table 3: *"We observe severe performance degradation when training without straightening and decreasing the learning rate helps. We thus use lr = 1e−6 for no straightening"* (vs 1e−5 with). Tuned in the baseline's favour, so not a stacked comparison — but it means the two arms are not identical apart from the loss term, and the instability it hints at is itself part of what straightening is fixing.

## Entities mentioned

- [DINO-WM](../entities/dino-wm.md) — the baseline and the encoder configuration compared against.
- [Yann LeCun](../entities/yann-lecun.md), [Randall Balestriero](../entities/randall-balestriero.md), Mengye Ren, Oumayma Bounou, **Gaoyue Zhou** (first author of [Patch Policy](patch-policy-paper.md)), Tim G. J. Rudner.
- [DINOv2](../entities/dinov2.md).

## Concepts touched

- [Gradient-based planning](../concepts/world-models/gradient-based-planning.md) — this source and [Closing the Train-Test Gap](train-test-gap-world-models-paper.md) create it.
- [Learned latent space](../concepts/world-models/latent-space.md) — curvature as a property of one.
- [JEPA](../concepts/world-models/jepa.md) — implicit straightening as an emergent property of the prediction objective.
- [Identifiability](../concepts/world-models/identifiability.md) — a third proposed criterion for "a good latent space."

## Open questions

- **The theorem covers affine dynamics only**; the empirical system is nonlinear.
- **Symmetric Euclidean goal cost "may be suboptimal under asymmetric or irreversible dynamics"** — the authors' own stated limitation, and a real one for manipulation, where most interesting transitions are irreversible.
- **No real robot; four 2D goal-reaching tasks.**
- **Not combined with the [train-test-gap](train-test-gap-world-models-paper.md) methods**, despite same problem, same base model, shared co-author. Representation geometry and training distribution are orthogonal fixes and the obvious experiment is to stack them.
- **Relationship to [LpWM](lpwm-paper.md)'s sparse geometry is unexplored** — that is a third proposal for what a planning-friendly latent space looks like, and sparse mode-factored codes are not obviously straight.

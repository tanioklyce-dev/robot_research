---
title: Gradient-based planning (vs CEM) in latent world models
type: concept
created: 2026-08-26
updated: 2026-08-26
sources: 2
tags: [gradient-based-planning, cem, mpc, world-model, jepa, planning, latent-space, curvature, adversarial, conditioning]
---

**Gradient-based planning (GBP)** — choose an action sequence by **backpropagating through a learned world model's rollout** and descending the planning objective, instead of sampling candidate sequences and keeping the best. The alternative the wiki had been documenting by default is **CEM**, and until 2026 the empirical record was one-sided: CEM won.

Two 2026 papers explain *why* it lost and close most of the gap, from opposite directions. Neither claims GBP is now better — both claim it now **reaches CEM's bar at roughly a tenth of the compute.**

## CEM, the incumbent

The [cross-entropy method](../../glossary.md#cem) samples `M` candidate action sequences, rolls each through the world model, refits a sampling distribution to the top performers, and repeats for `K` iterations — `M·K` forward rollouts, no gradients. [LeWM](../../entities/leworldmodel.md)'s recipe is the wiki's worked example: ~500 trajectories, elite set of ~30, scored by **Euclidean distance in embedding space** to the goal embedding.

The cost is the problem. [Temporal Straightening](../../sources/temporal-straightening-paper.md) measures it: CEM needs **≥200 samples × 10 iterations** to be competitive, making it **~10× slower than GBP** in wall-clock. GBP with `N` optimization steps needs `N` forward rollouts and `N` backward passes.

## Why gradient-based planning lost

> [!note] GBP is an adversarial attack on your own world model
> The cleanest statement of the failure, from [Closing the Train-Test Gap](../../sources/train-test-gap-world-models-paper.md): a world model is trained on **next-state prediction** but used at test time to **estimate actions**. A gradient planner "selects actions solely to improve the planning objective, without regard to whether those actions resemble expert behavior," so it proposes out-of-distribution action sequences — and *"optimizing through learned models under such conditions is known to induce adversarial inputs."* The model is driven into latent regions it never saw, errors compound over the rollout, and the failure is worst at long horizons, where planning matters most.
>
> **This retroactively explains CEM's dominance.** CEM's supposed weakness — it cannot exploit gradient structure, it just samples — is exactly what keeps it near the training distribution. Sampling is robust to a model whose gradients are untrustworthy. Any method that gets more clever about exploiting a learned model is buying more exposure to that model's errors.

A second, geometric reason, from [Temporal Straightening](../../sources/temporal-straightening-paper.md): **Euclidean distance in latent space is only a valid proxy for progress when latent trajectories are straight**, and pretrained visual encoders produce trajectories that are "usually highly curved." A curved space makes the planning objective badly conditioned, and gradient descent converges at a rate set by that conditioning. CEM, which only ranks candidates, is far less sensitive to conditioning than a gradient method is.

## The two fixes

| | [Closing the Train-Test Gap](../../sources/train-test-gap-world-models-paper.md) (Dec 2025) | [Temporal Straightening](../../sources/temporal-straightening-paper.md) (ICML 2026) |
|---|---|---|
| **What is wrong** | The training *distribution* doesn't cover where the planner goes | The latent *geometry* is curved, so the objective is ill-conditioned |
| **Fix** | Train-time data synthesis: **Online WM** (DAgger-style — execute GBP's actions in the true simulator, retrain on the corrected trajectory) and **Adversarial WM** (adversarial training on actions and latents) | **Curvature regularizer** on latent trajectories, jointly training encoder and predictor |
| **Evidence it worked** | World-model error is higher on planning than expert trajectories for DINO-WM, **but not** after either method — the gap itself narrowed | Straighter trajectories; Euclidean distance better tracks geodesic distance; proved bound on the planning Hessian's condition number |
| **Headline** | Matches/beats DINO-WM's CEM in **10% of the time budget**; open-loop +18/+20/+30% | Open-loop **+20–60%**, MPC **+20–30%**; UMaze open-loop 35.33 → 94.00 |
| **Requires a simulator?** | Online WM **yes**; Adversarial WM no | No |

Both build on **[DINO-WM](../../entities/dino-wm.md)**, both report on PushT / PointMaze / Wall, and they share a co-author (Oumayma Bounou). **Neither combines with the other** — training distribution and representation geometry are orthogonal fixes, and stacking them is the obvious untried experiment.

## What is honestly established

> [!warning] CEM still wins on absolute success rate
> Both papers say so. Temporal Straightening: *"Consistent with prior work, CEM often obtains higher absolute success rates than GD, but at substantially higher computational cost. Importantly, straightening largely reduces the performance gap."* And in the train-test-gap table, the improved world model planned with **CEM** still beats the same model planned with **Adam** (98 vs 94 on PointMaze). The paper's claim is against *DINO-WM's* CEM, not its own.
>
> The defensible summary: **gradient-based planning has become a viable 10×-cheaper option that reaches the previous CEM bar, not a replacement for CEM.** For a real-time robot that distinction may not matter — a tenth of the compute is the whole argument. For a benchmark table it does.

## Three competing answers to "what makes a latent space good for planning"

The wiki now holds three, from overlapping author groups, none of which cite each other on this point:

- **Identifiable** — [linear identifiability](identifiability.md) under a *Gaussian* latent, so the latent space is the world's up to rotation.
- **Straight** — low curvature, so Euclidean distance proxies geodesic distance and the planning Hessian is well conditioned ([Temporal Straightening](../../sources/temporal-straightening-paper.md)).
- **Sparse and mode-factored** — support encodes the discrete dynamics regime, magnitudes the continuous state, lowering the predictor capacity needed ([LpWM](../../entities/lpwm.md)).

These are not obviously compatible. A sparse, mode-factored code is not obviously straight; an isotropic Gaussian is not obviously either. **That three groups working from the same lab produced three different criteria in one year is the honest state of the field**, and the wiki should not treat any one as settled.

## Related concepts

- [Learned latent space](latent-space.md) — curvature, sparsity, and identifiability are all properties of one.
- [JEPA](jepa.md) — the prediction objective, which [induces some straightening implicitly](../../sources/temporal-straightening-paper.md).
- [Identifiability](identifiability.md) / [LpWM](../../entities/lpwm.md) — the competing criteria.
- [Test-time adaptation](../learning/test-time-adaptation.md) — a fourth response to the same underlying problem (the model is wrong where you are planning), applied online instead of at training time.
- [Optimal control](../robotics/optimal-control.md) — the classical MPC tradition these planners sit inside.
- [World-model simulators](world-model-simulators.md).

## Mentioned in

- [Closing the Train-Test Gap in World Models for Gradient-Based Planning](../../sources/train-test-gap-world-models-paper.md)
- [Temporal Straightening for Latent Planning](../../sources/temporal-straightening-paper.md)
- [LeWorldModel paper](../../sources/leworldmodel-paper.md) — the CEM recipe this page is measured against.
- [AdaJEPA paper](../../sources/adajepa-paper.md) — uses both GD and CEM planners.

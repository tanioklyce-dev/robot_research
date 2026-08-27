---
title: "Closing the Train-Test Gap in World Models for Gradient-Based Planning"
type: source
url: https://arxiv.org/abs/2512.09929
local_path: raw/train-test-gap-world-models_2512.09929.pdf
author: Arjun Parthasarathy, Nimit Kalra, Rohun Agrawal, Yann LeCun, Oumayma Bounou, Pavel Izmailov, Micah Goldblum
published: 2025-12-10
ingested: 2026-08-26
venue: arXiv (cs.LG, cs.RO)
format: paper (25 pp)
tags: [world-model, gradient-based-planning, mpc, cem, dino-wm, adversarial-training, dagger, planning, lecun]
---

# Closing the Train-Test Gap in World Models for Gradient-Based Planning

## Summary

Diagnoses *why* [gradient-based planning](../concepts/world-models/gradient-based-planning.md) through a learned world model underperforms the gradient-free [cross-entropy method](../concepts/world-models/gradient-based-planning.md#cem-the-incumbent), and fixes it at training time rather than at planning time. The diagnosis is the contribution: **a world model is trained on next-state prediction but used at test time to estimate actions**, and a gradient-based planner optimizing actions against that model will drive it into latent regions it never saw — which is the definition of an adversarial input. Two train-time data-synthesis methods (**Online World Modeling**, **Adversarial World Modeling**) close the gap, letting gradient-based planning match or beat [DINO-WM](../entities/dino-wm.md)'s CEM at **~10× less wall-clock time**.

## The diagnosis

> "During gradient-based planning, the action sequences being optimized are not constrained to lie within the distribution of behavior seen during training… GBP selects actions solely to improve the planning objective, without regard to whether those actions resemble expert behavior. As a result, the optimization process often proposes action sequences that are out of distribution. **Optimizing through learned models under such conditions is known to induce adversarial inputs.**"

> [!note] Gradient-based planning is an adversarial attack on your own world model
> This is the framing worth carrying out of the paper, and it is not specific to this method. A planner that takes gradients of a learned model with respect to its inputs is doing exactly what an adversarial-example generator does — searching input space for whatever maximizes an objective the model was never trained to be robust on. Errors that start small **accumulate as the planner rolls the model forward**, so the failure is worst precisely where planning is most valuable: long horizons.
>
> It also explains a pattern the wiki already records without an account of it — that CEM is repeatedly the stronger planner in latent world models. CEM samples, and sampling stays closer to the training distribution than gradient ascent does. **CEM's weakness (it can't exploit structure) is exactly what makes it robust to a model whose gradients are untrustworthy.**

## The two methods

**Online World Modeling** — explicitly DAgger-shaped. Run GBP from a trajectory's start and goal latents; execute the proposed actions in the **true simulator** to obtain the *corrected* trajectory of states that actually result; add that to the training set; retrain on next-state prediction. Repeat. *"We invoke the ground-truth simulator as our expert world model that we imitate."* This expands the training distribution to cover the latent regions GBP actually visits.

**Adversarial World Modeling** — since "world models are only trained on the next-state prediction objective, there is no particular reason for their input gradients to be well-behaved," apply adversarial training with perturbation radii `ε_a, ε_z` on actions and latents. Reported effect: **a smoother optimization landscape with a broader basin around the optimum** (their Figure 2, visualized on Push-T).

Practical notes: perturbation radii are set by scaling factors `λ_a, λ_z`, robust for `0 ≤ λ_a ≤ 1` and `0 ≤ λ_z ≤ 0.5`. **Fixing `ε_a, ε_z` to the standard deviation of the initial minibatch is stable across all experiments**; re-estimating per batch "yields no consistent improvement."

## Results

Base model is **[DINO-WM](../entities/dino-wm.md)** (frozen DINOv2 embeddings), chosen "for its strong performance with CEM." Success rate (%), three tasks, gradient descent (GD) and Adam as gradient planners against CEM:

| Model | PushT GD / Adam / CEM | PointMaze GD / Adam / CEM | Wall GD / Adam / CEM |
|---|---|---|---|
| DINO-WM | 38 / 54 / **78** | 12 / 24 / **90** | 2 / 10 / **74\*** |
| DINO-WM + MPC | 56 / 76 / 92 | 42 / 68 / 90 | 12 / 80 / 82 |
| Online WM | 34 / 52 / 90 | 20 / 14 / 62 | 16 / 18 / 54\* |
| Online WM + MPC | 50 / 76 / 92 | 54 / 88 / 96 | 38 / 80 / 90 |
| Adversarial WM | 56 / 82 / 94 | 32 / 70 / 88 | 32 / 34 / 30\* |
| **Adversarial WM + MPC** | 66 / **92** / 92 | 50 / **94** / 98 | 14 / **94** / 94 |

Open-loop improvements over DINO-WM: **+18% Push-T, +20% PointMaze, +30% Wall.**

> [!warning] Read the comparison baseline carefully — CEM is not actually beaten
> The paper's claim is that Adam GBP with Adversarial World Modeling *"outperforms CEM with **DINO-WM** on PointMaze and Wall and matches CEM on PushT."* That is true: 94 vs DINO-WM's 90 on PointMaze, 94 vs 82 on Wall, 92 vs 92 on PushT.
>
> But **the same improved world model planned with CEM does better still** — 98 on PointMaze against Adam's 94, and 92–94 elsewhere. So the honest summary is not "gradient-based planning now beats CEM." It is **"gradient-based planning now reaches the CEM-with-the-old-model bar at a tenth of the compute,"** which is a genuine and useful result stated at its correct strength. [Temporal Straightening](temporal-straightening-paper.md) reaches the same conclusion independently and says so plainly.

> [!note] A reproducibility failure, reported
> The asterisks mark this: *"We could not reproduce the Wall environment open-loop CEM success rate reported in DINO-WM (74%)."* Worth recording on its own — the wiki's [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) page collects exactly this kind of datapoint, and it is rare for a paper to flag a failed reproduction of the baseline it builds on.

**Train-test gap, measured.** Comparing world-model error between expert and planning trajectories on PushT: the error is larger on planning trajectories for DINO-WM, **but not for Online or Adversarial World Modeling** — direct evidence the gap narrowed rather than the score merely improving.

**Efficiency.** Gradient-based planning is *"orders of magnitude faster than CEM"* in wall-clock time; the headline figure is matching or exceeding CEM performance **in 10% of the time budget**.

## The limitation the method carries

> [!warning] Online World Modeling requires a ground-truth simulator
> The corrected trajectory comes from *"executing the action sequence in the environment using the true dynamics simulator h."* That is fine for PushT and PointMaze and unavailable for the case the wiki cares most about — a real robot, where the whole point of a world model is that you cannot cheaply roll out the true dynamics. **Adversarial World Modeling has no such requirement** and is the stronger method in the table anyway, which is fortunate: it is the one that transfers.

## Entities mentioned

- [DINO-WM](../entities/dino-wm.md) — the base world model and baseline.
- [Yann LeCun](../entities/yann-lecun.md); **Pavel Izmailov**, **Micah Goldblum**, Oumayma Bounou (also on [AdaJEPA](adajepa-paper.md) and [Temporal Straightening](temporal-straightening-paper.md)).
- [DINOv2](../entities/dinov2.md) — the frozen embedding function.

## Concepts touched

- [Gradient-based planning](../concepts/world-models/gradient-based-planning.md) — the concept page this source creates, with [Temporal Straightening](temporal-straightening-paper.md).
- [JEPA](../concepts/world-models/jepa.md) / [world-model simulators](../concepts/world-models/world-model-simulators.md).
- [Learned latent space](../concepts/world-models/latent-space.md).
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — the failed baseline reproduction.

## Open questions

- **Three 2D tasks, no real robot, no manipulation beyond PushT.**
- **No trial counts or confidence intervals** — success rates are reported as bare percentages, and several comparisons in the table turn on 2–4 points.
- **Wall open-loop is erratic**: Adversarial WM scores **30** with CEM against DINO-WM's 74, and Adversarial WM + MPC scores **14** with GD against 94 with Adam. The paper does not explain the instability, and it undercuts confidence in the Wall column generally.
- **No interaction with the other route.** [Temporal Straightening](temporal-straightening-paper.md) fixes the *representation geometry* for the same problem, on the same base model, with an overlapping author. Neither paper combines the two.

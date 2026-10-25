---
title: Slow-feature collapse
type: concept
created: 2026-10-13
updated: 2026-10-24
sources: 11
tags: [slow-feature-collapse, jepa, anti-collapse, sigreg, inverse-dynamics, pldm, droid, world-model, representation-learning, disreg, predictive-closure, motionjepa, hamiltonian-jepa]
---

# Slow-feature collapse

**Slow-feature collapse** is the failure in which a predictive world model's encoder represents only what is **constant within an episode**: the scene, the camera, the lighting. It discards the agent it is supposed to model. The prediction loss goes to zero, because the predictor learns the identity map, and no "collapse" alarm fires, because the embeddings still vary *across* episodes and so look healthy to a distribution-level regulariser. The model knows *which room it is in* and nothing about the arm.

It is the temporal counterpart of ordinary representation collapse, where every input maps to one point. Ordinary collapse is what [SIGReg](sigreg.md), VICReg and EMA teachers prevent. Slow-feature collapse **passes all of them**.

Several autumn-2026 papers describe the same failure under other names: *temporal feature collapse* ([MotionJEPA](../../sources/motionjepa-temporal-feature-collapse-paper.md)) and *causal dynamics information collapse* ([AVL-JEPA](../../sources/avl-jepa-causal-dynamics-collapse-paper.md)). Most of them study a **graded** version on fixed-scene simulators, where dynamics information is weakly encoded but not absent. See the [batch synthesis](../../syntheses/world-models/jepa-dynamics-collapse-fixes.md).

## Key references
- [Sobal et al. 2022, "JEPAs focus on slow features"](../../sources/sobal2022-jepa-slow-features-paper.md): the empirical discovery. A **fixed** distractor (constant within an episode, varying across episodes) is fatal; a **changing** one is harmless; VICReg doesn't fix it; inverse dynamics recovers the controllable dot.
- [PLDM](../../sources/pldm-paper.md) (2025): an inverse-dynamics term in the anti-collapse mix, motivated by the 2022 result.
- [H-JEPA paper](../../sources/h-jepa-hierarchical-world-models-paper.md) (2026, App. L): the **theory**, and the failure on real data (DROID).
- [Predictive Closure](../../sources/predictive-closure-jepa-feature-selection-paper.md) (Levy, Lidayan, Goldberg, 2026-10): the **general frame** for which features a JEPA keeps; contains the H-JEPA result as a special case.
- [MotionJEPA](../../sources/motionjepa-temporal-feature-collapse-paper.md) (2026-09): the first **label-free** barrier shown to work, in fixed-camera simulation.

### The control-theoretic account (Toso et al., 2026-10)
[Toso, LeCun, Anderson, Bounou](../../sources/preserving-unstable-modes-inverse-dynamics-paper.md) prove the same failure in **control** language, for linear systems:
- **Lemma 2.** Prediction + SIGReg is exactly minimised by an encoder that keeps only the stable block, whitened to an isotropic Gaussian. It throws away **every unstable mode**, which makes the plant **unstabilisable** from the latent (Lemma 1, detectability).
- **Theorem 1.** Exact **endpoint** inverse dynamics, reconstructing `a_t…a_{t+H−1}` from `(z_t, z_{t+H})`, makes the encoder injective on the **H-step reachable subspace**.
- **Theorem 2.** As H grows, that subspace's dominant directions converge to the unstable ones.

This is the first proof of *which* directions the inverse-dynamics barrier protects. *Wiki inference:* one-step IDM (H = 1) protects only `range(B)`, the directly actuated coordinates. That is a mechanism for "IDM keeps the arm and may lose the object" ([synthesis §4](../../syntheses/world-models/jepa-dynamics-collapse-fixes.md#4-a-pattern-worth-testing-inverse-dynamics-keeps-the-arm-and-may-lose-the-object)).

## The theory (H-JEPA App. L)
- **Three kinds of content** in a sequence: *background* (constant within an episode, readable from one frame), *foreground* (action-driven, partly stochastic), and *distractors* (moving, action-independent).
- **No marginal regulariser can exclude it** (Prop. 1). An encoder that maps the background to any target distribution, Gaussian included, satisfies SIGReg exactly and has zero prediction error. Variance/covariance penalties, whitening, entropy terms and SIGReg all look only at the distribution of single embeddings, so none can tell this encoder from a good one.
- **It is an optimum** (Thm. 1). Any feature carrying unpredictable motion costs prediction error; the background costs nothing. Among zero-loss solutions, training's implicit bias picked the collapse in every SIGReg-only run.
- **The theory explains Sobal 2022's three results**: fixed noise is background and becomes the collapse target; changing noise is a distractor and gets shed; IDM recovers the controlled dot but not the stationary one.

### The general frame: predictive closure (2026-10)
[Predictive Closure](../../sources/predictive-closure-jepa-feature-selection-paper.md) shows that with latent entropy fixed by the regulariser, the ideal encoder keeps the **set** of features whose current values best predict that set's own next values. A within-episode-constant background contributes nothing to the objective, so a background set that fills the latent is a global optimum: H-JEPA's Prop. 1 + Thm. 1 restated in information terms. The paper does not cite H-JEPA. It adds two things:
- **"Slow" is not quite the criterion.** A fast or unpredictable feature survives if it helps predict *other* kept features (the traffic-light example). Slowness also depends on frame stride.
- **Steering is indirect.** An auxiliary loss on feature C strengthens the features C predicts. That is the mechanism by which every barrier below works. *Wiki inference:* action-conditioning alone can only bring agent-affected features down to zero cost, a tie with the background at best, which fits H-JEPA's Table 12. An extra term is what breaks the tie.

> [!note] Not to be confused with rollout contraction (2026-10-24)
> [LeHami](../../entities/lehami.md) addresses a **different** collapse: the *predictor* shrinking the latent distribution step by step over an autoregressive rollout. An exactly symplectic predictor rules that out by construction. It does nothing about the *encoder* dropping the agent: a background-only encoder still yields a perfectly volume-preserving rollout. The two failures sit in different components, and their fixes compose rather than compete ([LeHami paper](../../sources/lehami-symplectic-latent-dynamics-paper.md)).

## Barriers, ranked

From H-JEPA App. L, extended by the autumn-2026 batch. A barrier has to act on **pairs of timesteps** (the joint law), not on single embeddings.

1. **SIGReg with time in the sample axis** ("pooled", "LeWM-Flat"): a real but small penalty. With time **in the group axis** (per-timestep), zero. Every SIGReg-only DROID run collapsed regardless of λ. MotionJEPA independently finds LeWM-Flat **helps partially** (20.4 → 41.7% with a wood background).
2. **Time repulsion** (reward latent change, no labels): keeps the predictor off the identity, but never beat the do-nothing baseline. There is no usable weight window when the foreground is itself ~50% unpredictable.
3. **Inverse dynamics** (regress the action from consecutive latents): an **Ω(1) floor**. Its scope is now proved for linear systems: exact reconstruction keeps the **H-step reachable subspace**, so one-step IDM keeps the directly actuated directions and **endpoint IDM (EP-IDM)** over H steps keeps everything an action sequence can reach ([Toso et al.](../../sources/preserving-unstable-modes-inverse-dynamics-paper.md); CartPole latent-LQR 0% → 100%). A collapsed encoder cannot predict actions, so it pays at least the action variance. It needs action labels. **It is the only barrier shown on scene-diverse real data (DROID).** New instances in this batch: AVL-JEPA's "action anchor" (inverse dynamics on Δz with a zero-transition baseline subtracted) and GAWM's IDM term.
4. **Difference-image prediction (DISReg)** ([MotionJEPA](../../sources/motionjepa-temporal-feature-collapse-paper.md)): predict an embedding of `o_{t+1} − o_t` from `(z_t, z_{t+1})`. It is inverse dynamics with a **learned motion target in place of the action**, so the regulariser needs **no labels**, although the predictor is still action-conditioned. On LeWM's suite with a per-episode wood background: **LeWM 20.4%, IDM 77.2%, DISReg 81.8%, both 86.4%** (25-step mean; no seeds reported). **Limit:** a fixed camera makes the background subtract out exactly. Under ego-motion the difference image is mostly scene and `SIGReg(d)` is marginal-only. *That limit is the wiki's reasoning; nothing tests it.*
5. **State alignment** ([GAWM](../../sources/physically-grounded-jepa-world-models-paper.md)): regress the simulator's full state from the latent during training. It works (Cube 87 with IDM vs 85 IDM-only), but it needs **privileged object pose and velocity**, which a real robot does not have.
6. **A constrained action port** ([Hamiltonian JEPA](../../sources/hamiltonian-jepa-control-state-paper.md)): the predictor must move the state by exactly one unit per unit action along orthonormal directions, so an action-blind identity predictor is not available. *Wiki inference, untested by the paper (single-scene benchmarks only):* this gives an IDM-like Ω(1) floor from structure, adding no parameters, and its tied inverse readout is provably a reweighting of the forward loss.

> [!warning] Contradiction, narrowed rather than resolved
> Until 2026-10-22 this page said inverse dynamics is "the only barrier that works". [MotionJEPA](../../sources/motionjepa-temporal-feature-collapse-paper.md) (same senior author as H-JEPA, two weeks earlier, not cited by it) shows a label-free barrier working against the same failure in fixed-camera simulation. The theorems are not contradicted: DISReg acts on the joint law, as H-JEPA says a barrier must. The supported statement is now: **only inverse dynamics has been shown on scene-diverse real data; a label-free barrier works with a fixed camera in simulation.**

## When it bites
**When the scene changes between episodes.** On DROID, 75% of latent variance is between episodes; on OGBench Cube (fixed camera, one scene) it is 28%. Single-scene simulators (Push-T, PointMaze, AntMaze) make the background a point mass, so SIGReg alone suffices there. **That is why the wiki's simulation results never showed the total version of this failure.**

Two 2026 demonstrations of the condition:
- **Manufactured:** MotionJEPA's per-episode wood background on LeWM's suite drops LeWM from its usual 74–96% to **4.0% on Push-T and 5.2% on Reacher**. It is the clearest simulated case in the wiki.
- **In the wild, undiagnosed:** in [AD-E2E-JEPA](../../sources/ad-e2e-jepa-autonomous-driving-paper.md)'s NAVSIM driving test, LeWM is the only model that trains its own encoder on scene-diverse video, and its plans barely depend on the action (top-1 trajectory hit rate 5.7% vs 53.8%). This is consistent with slow-feature collapse, but a ViT-L at batch size 8 confounds it.

## How to detect it

- **Latent LQR around a known equilibrium** ([Toso et al.](../../sources/preserving-unstable-modes-inverse-dynamics-paper.md)): linearise the predictor, design LQR, deploy. On CartPole it fails **0/10** for SIGReg models that still score **100%** under CEM and GBP planning. Planning success can hide a discarded control-critical direction.
- **Not from loss.** In MotionJEPA's Dino game, LeWM's agent-position probe recovers early and then collapses back to ~1.0 NMSE with no sign in the training loss (Fig. 3).
- **Action sensitivity** (H-JEPA): how much the rollout changes when actions are swapped. **Within-episode variance share.**
- **MLP probes against a random-init floor** (MotionJEPA): a random encoder already reaches 0.116 NMSE on Pong, so a trained encoder that scores worse has actively thrown information away.
- Probes and planning do **not** always agree ([Hamiltonian JEPA](../../sources/hamiltonian-jepa-control-state-paper.md) plans well on probe-invisible directions). No paper yet checks all three diagnostics on one model. See the [synthesis §5](../../syntheses/world-models/jepa-dynamics-collapse-fixes.md#5-evaluation-collapse-stays-invisible-to-the-obvious-checks-and-the-diagnostics-disagree).

## Related concepts
- [SIGReg](sigreg.md) — necessary for rank, provably insufficient against this.
- [JEPA](jepa.md) — "Common training challenges" and the H-JEPA section.
- [World-model evaluation](world-model-evaluation.md) — a collapsed model can have low prediction loss and a healthy-looking embedding distribution. **Measure action sensitivity** (how much the rollout changes when actions are swapped) or within-episode variance share, not loss.
- [Identifiability](identifiability.md) — a different regime: latent geometry when the latent is big enough; predictive closure covers content when it is not.

## Current state (2026-10)
A theory now matches the 2022 observation, Predictive Closure generalises it, and the practical answer for real robots is unchanged: **use action labels**. For a home robot, whose scenes vary by construction, this means LeWM-style training on teleop or play data with logged actions, **not** passive video. The new option is **IDM + DISReg** together, the best row in MotionJEPA, for static-camera views. Whether any label-free barrier survives a **moving camera** (a mobile manipulator's head or wrist camera) is the open question. A single-protocol comparison of all six barriers is proposed in the [synthesis](../../syntheses/world-models/jepa-dynamics-collapse-fixes.md#6-the-experiment-this-batch-makes-cheap).

## Mentioned in
- [H-JEPA paper](../../sources/h-jepa-hierarchical-world-models-paper.md)
- [Sobal et al. 2022](../../sources/sobal2022-jepa-slow-features-paper.md)
- [PLDM paper](../../sources/pldm-paper.md)
- [MotionJEPA](../../sources/motionjepa-temporal-feature-collapse-paper.md)
- [AVL-JEPA](../../sources/avl-jepa-causal-dynamics-collapse-paper.md)
- [Physically grounded JEPA WMs (GAWM)](../../sources/physically-grounded-jepa-world-models-paper.md)
- [Hamiltonian JEPA](../../sources/hamiltonian-jepa-control-state-paper.md)
- [Predictive Closure](../../sources/predictive-closure-jepa-feature-selection-paper.md)
- [AD-E2E-JEPA](../../sources/ad-e2e-jepa-autonomous-driving-paper.md)
- Synthesis: [What the latent throws away](../../syntheses/world-models/jepa-dynamics-collapse-fixes.md)
- [LeHami](../../sources/lehami-symplectic-latent-dynamics-paper.md) — rollout-contraction counterpart; explicitly not an encoder barrier.
- [Toso et al. — Preserving unstable modes](../../sources/preserving-unstable-modes-inverse-dynamics-paper.md) — the control-theoretic proof: SIGReg + prediction can discard all unstable modes; endpoint IDM keeps the H-step reachable subspace.

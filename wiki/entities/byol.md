---
title: BYOL (Bootstrap Your Own Latent)
type: entity
subtype: model
created: 2026-09-03
updated: 2026-09-03
sources: 4
tags: [byol, self-supervised, ema, momentum-encoder, predictor, anti-collapse, no-negatives, deepmind, marketone]
---

**BYOL — Bootstrap Your Own Latent**, Grill et al. ([paper](../sources/byol-paper.md), DeepMind + Imperial, NeurIPS 2020). An *online* network predicts a *target* network's representation of a different augmented view; the target is an exponential moving average of the online network. **No negative pairs.** 74.3% ImageNet linear top-1 with a plain ResNet-50, 79.6% with ResNet-200(2×).

The result that made "you need negatives to avoid collapse" false, and the direct ancestor of the **EMA + stop-gradient** rung on this wiki's [anti-collapse ladder](../concepts/world-models/jepa.md#common-training-challenges).

## The mechanism is a conjunction, not a knob

Online: encoder → projector → **predictor**. Target: encoder → projector, **no predictor**, **stop-gradient**, EMA update `ξ ← τξ + (1−τ)θ` with `τ_base = 0.996` → 1. Normalized MSE loss, symmetrized over the two views. The architecture is **deliberately asymmetric**.

The ablation that pins it (ImageNet linear, 300 epochs; `β` weights the negative-pair term):

| Predictor | Target net | β | Top-1 |
|:---:|:---:|:---:|---:|
| ✓ | ✓ | 0 | **72.5** |
| — | ✓ | 0 | **0.3** |
| ✓ | — | 0 | **0.2** |
| — | — | 0 | **0.1** |

**Without negatives you need the predictor *and* the target network; either alone is chance.** Any summary of "EMA-based anti-collapse" that omits the asymmetric predictor is describing a method that scores 0.3%.

A second finding from the same table: **adding a target network to SimCLR gains 1.6 points at the same number of negatives** — the EMA has a stabilization effect independent of the negative-sampling role MoCo introduced it for.

## Why it doesn't collapse — stated as a hypothesis

The paper is candid, and this matters more than the accuracy:

- `ξ` is not updated along `∇_ξ L`, so *"we hypothesize that there is no loss such that BYOL's dynamics is a gradient descent on L jointly over θ, ξ"* — explicitly analogized to GANs. *"There is therefore no a priori reason why BYOL's parameters would converge to a minimum."*
- Under an **optimal predictor**, updates follow the gradient of the expected **conditional variance**; since `Var(X|Y,Z) ≤ Var(X|Y)`, discarding information cannot lower it, so collapsed solutions are argued to be **unstable equilibria**.
- *"We did not observe convergence to such equilibria in our experiments."*

> [!note] The SimSiam question is resolved — by BYOL's own appendix
> The wiki flagged Table 5b row 7 (predictor, no EMA, no negatives → **0.2%**) against [SimSiam](simsiam.md)'s claim that the configuration works. **Tables 21–22 of this same paper** settle it: hard-copying the online weights into the target with a **10× predictor learning rate** gives **66.6–66.9** against the 72.5 EMA baseline, where λ=1 gives 5.5 and λ=0 gives 0.01. The main-text row is the un-tuned case. [The Cookbook](../sources/ssl-cookbook.md) §3.4.1 states the same rule: EMA *"is not necessary … as long as the predictor is updated more often or has larger learning rate compared to the backbone."* **Both results stand, and removing the EMA still costs ~6 points after tuning for it** — it buys accuracy, not safety. What is load-bearing is *asymmetry between the branches* — the EMA is one way to get it, a faster predictor is another, and stronger augmentation on the student is a third.
>
> Two mechanisms for what the predictor does, from the same source: it **acts as a whitening operator** (Tian et al. 2021), and with it the dynamics are **proved** to have nontrivial stable fixed points, so the trivial optimum is not reached despite existing. Removing it costs BYOL **68% → 21%**; a *linear* predictor suffices and recovers from bad init in 10–20 epochs.

> [!note] This is the disclosure the SIGReg line is answering
> [Balestriero](randall-balestriero.md)'s objection that an EMA *"makes the loss uninterpretable — you can see the loss actually increase but the quality of your model become better"* has its explanation here: **there is no loss being descended.** A quantity nobody is minimizing has no obligation to fall. [LeJEPA](../sources/lejepa-paper.md) replaces the whole apparatus with one term that does have a theorem.

## The property that ages best

**Robustness**, which is also what makes a method portable to a new domain without a hyperparameter search:

| Perturbation | BYOL | SimCLR |
|---|---:|---:|
| Remove colour distortion | **−9.1** pts | −22.2 pts |
| Crop-only augmentation | **59.4%** (−13.1) | 40.3% (−27.6) |
| Batch 4096 → 256 | ~flat | degrades |

The explanation is worth keeping: crops of one image share a colour histogram, so a *contrastive* task on crops alone is solvable by colour histogram and the representation is never pushed past it. BYOL has no such shortcut.

That is why BYOL is still a live baseline here six years on. In the [MarketOne](marketone.md) bake-off it ranks **~4th on every task** — never best, never bad — and sits with LeJEPA on the efficient frontier under time-warping augmentation. A method whose selling point is insensitivity should look exactly like that.

## Related

- [SimSiam](simsiam.md) — BYOL minus the momentum encoder; the paper that isolated stop-gradient.
- [DINO](dino.md) — takes its inspiration from BYOL; different loss, no predictor, and BYOL's predictor does nothing there.
- [MAE](mae.md) — the reconstruction alternative; needs no anti-collapse term and no augmentation.
- [SIGReg](../concepts/world-models/sigreg.md) — the provable replacement for this stack.
- [Contrastive learning and InfoNCE](../concepts/learning/contrastive-learning.md) — the family it leaves.
- [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md).

## Mentioned in

- [BYOL paper (Grill et al., 2020)](../sources/byol-paper.md) — the primary.
- [A Cookbook of Self-Supervised Learning](../sources/ssl-cookbook.md) — the predictor-as-whitening-operator mechanism.
- [SimSiam paper (Chen & He, 2020)](../sources/simsiam-paper.md) — the control that prompted re-reading BYOL's appendix.
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — a live baseline in the [MarketOne](marketone.md) bake-off, ranking ~4th on every task.

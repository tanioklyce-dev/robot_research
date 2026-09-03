---
title: "Bootstrap Your Own Latent (Grill et al., 2020)"
type: source
url: https://arxiv.org/abs/2006.07733
fetch_url: https://arxiv.org/pdf/2006.07733v3
local_path: raw/2006.07733v3.pdf
sha256: 873e7b74d58e1e17806cf7a3cf6b80ead914559f36ed19313c749672eed0aa94
author: "Jean-Bastien Grill, Florian Strub, Florent Altché, Corentin Tallec, Pierre H. Richemond et al. (DeepMind; Imperial College)"
published: 2020-06-13
venue: "NeurIPS 2020 (arXiv v3, 2020-09-10)"
format: paper (PDF, 35 pp. incl. appendices)
tags: [byol, self-supervised, ema, momentum-encoder, predictor, anti-collapse, no-negatives, contrastive-learning, deepmind, foundational]
ingested: 2026-09-03
---

## Summary

**The result that removed negatives from self-supervised learning, and could not fully explain why it worked.** BYOL trains an *online* network to predict a *target* network's representation of a different augmented view of the same image; the target is an exponential moving average of the online network. No negative pairs, no memory bank, no large-batch requirement — and 74.3% ImageNet top-1 under linear evaluation with a plain ResNet-50, beating every contrastive method of its day.

Its importance to this wiki is not the accuracy number. It is that **BYOL is the ancestor of the EMA/stop-gradient stack that [SIGReg](../concepts/world-models/sigreg.md) exists to delete**, and that the paper is unusually honest about resting on a hypothesis rather than a proof.

## Key claims

**The mechanism** (§3.1). Online branch: encoder `f_θ` → projector `g_θ` → **predictor `q_θ`**. Target branch: encoder `f_ξ` → projector `g_ξ`, **no predictor**, with a **stop-gradient**. Loss is a normalized MSE between `q_θ(z_θ)` and `sg(z'_ξ)`, symmetrized by swapping views. The target updates as `ξ ← τξ + (1−τ)θ`, with `τ_base = 0.996` annealed to 1 on a cosine schedule. **The architecture is deliberately asymmetric** — the predictor sits on one side only.

**The motivating experiment, which is better than the method** (§3). Predict a **fixed, randomly initialized network's** representation. That target is meaningless, yet the *predicting* network reaches **18.8%** ImageNet linear top-1 while the random network it predicted reaches **1.4%**. So: predicting a bad representation yields a better one. Iterate that, replacing fixed checkpoints with a moving average, and you get BYOL.

**Why it does not collapse — labelled a hypothesis, not a result** (§3.2). Three claims, in the paper's own hedged language:

- **BYOL's dynamics are not gradient descent on any loss.** `ξ` is not updated along `∇_ξ L`, and *"we hypothesize that there is no loss L_{θ,ξ} such that BYOL's dynamics is a gradient descent on L jointly over θ, ξ"* — explicitly analogized to GANs. *"There is therefore no a priori reason why BYOL's parameters would converge to a minimum."*
- **Under an optimal predictor**, BYOL's update follows the gradient of the **expected conditional variance** `∇_θ E[Σ_i Var(z'_{ξ,i} | z_θ)]`. Since `Var(X|Y,Z) ≤ Var(X|Y)`, *discarding information from the online projection cannot decrease the conditional variance* — so collapsed constant solutions are argued to be **unstable equilibria**, not minima.
- **The moving average exists to keep the predictor near-optimal.** A hard copy would propagate variability too, but *"sudden changes in the target network might break the assumption of an optimal predictor."*

> [!warning] "We did not observe convergence to such equilibria in our experiments"
> That sentence is the load-bearing one. BYOL's anti-collapse guarantee is **empirical**. The paper says so plainly, and the five years of follow-up work trying to explain it — SimSiam, the batch-norm controversy, and eventually [LeJEPA](lejepa-paper.md)'s replacement of the whole apparatus with a provable term — are downstream of this admission.

**The ablation that pins the mechanism** (Table 5b, 300 epochs, ImageNet linear top-1). `β` is the weight on the negative-pair term: `β = 1` is contrastive, `β = 0` has no negatives.

| Predictor | Target network | β | Top-1 |
|:---:|:---:|:---:|---:|
| ✓ | ✓ | 0 | **72.5** (BYOL) |
| ✓ | ✓ | 1 | 70.9 |
| ✓ | — | 1 | 70.7 |
| — | — | 1 | 69.4 (SimCLR) |
| — | ✓ | 1 | 69.1 |
| — | ✓ | **0** | **0.3** |
| ✓ | — | **0** | **0.2** |
| — | — | **0** | **0.1** |

**Read the bottom three rows together: without negatives, you need the predictor *and* the target network. Either one alone collapses to chance.** Neither is individually sufficient; their conjunction is the whole mechanism. And a second finding hides in the middle rows — **adding a target network to SimCLR improves it by 1.6 points with the same number of negatives**, so the EMA has a *stabilization* effect independent of the negative-sampling role it was introduced for in MoCo.

**Target decay rate** (Table 5a). `τ = 1` (never update, a constant random target) → 18.8. `τ = 0.999` → 69.8. `τ = 0.99` → **72.5**. `τ = 0.9` → 68.4. `τ = 0` (instant copy, i.e. plain stop-gradient) → **0.3**. The window that works is wide but the endpoints are catastrophic.

**Robustness — the practical argument for dropping negatives** (§5, Fig. 3):

| Perturbation | BYOL | SimCLR |
|---|---:|---:|
| Remove colour distortion | **−9.1** pts | −22.2 pts |
| Crop-only augmentation | **59.4%** (−13.1) | 40.3% (−27.6) |
| Batch size 4096 → 256 | ~flat | degrades steadily |

Their explanation for the augmentation result is worth keeping: crops of one image share a colour histogram, so a *contrastive* task on crops alone can be solved by colour histogram and nothing else — the representation is never incentivized past it. BYOL has no such shortcut, because it is rewarded for retaining anything the target encodes.

**Headline results.** ResNet-50 linear **74.3%** top-1 / 91.6 top-5; ResNet-200(2×) **79.6%**. Semi-supervised with 1% of labels: **53.2%** (SimCLR 48.3). Transfer: VOC2012 segmentation 76.3 mIoU (+1.9 over supervised-IN), VOC07 detection 77.5 AP50 (+3.1), NYU v2 depth pct<1.25 84.6 (+3.5). Cost: **512 TPU v3 cores, ~8 hours** for ResNet-50 at 1000 epochs.

## Why this source matters to this wiki

The wiki's [JEPA anti-collapse ladder](../concepts/world-models/jepa.md#common-training-challenges) begins at "EMA target encoder + stop-gradient" and treats it as a given. **BYOL is where that rung comes from**, and reading it changes two things:

1. **The EMA and the predictor are one mechanism, not two knobs.** Table 5b's bottom rows make that precise. Any account of "EMA-based anti-collapse" that omits the asymmetric predictor is describing something that scores 0.3%.
2. **Balestriero's Day 3 complaint is the paper's own disclosure, sharpened.** He objects that EMA doubles memory, adds a hyperparameter, and *"makes the loss uninterpretable"* ([Day 3](chicago-booth-world-modeling-workshop-2026-day3.md)). BYOL supplies the underlying reason: there is *no loss being descended*, by the authors' own hypothesis. A quantity that is not being minimized has no obligation to fall.

> [!note] What BYOL got right that the wiki's SIGReg pages under-weight
> **BYOL's headline practical claim is robustness to augmentation choice and batch size** — the thing that makes a method portable to a new domain without a hyperparameter search. That is *exactly* [LeJEPA](lejepa-paper.md)'s pitch, made five years earlier and by a different route. It also explains the [MarketOne](../entities/marketone.md) bake-off result the wiki already carries, where **BYOL ranks ~4th on every task** — a generalist, never the specialist — and sits with LeJEPA on the efficient frontier under time-warping augmentation. A method whose selling point is insensitivity should be expected to look exactly like that.

## Entities mentioned

- [DeepMind](../entities/google-deepmind.md) — 13 of 15 authors; Imperial College for the remainder.
- [BYOL](../entities/byol.md) — the method's entity page.
- [MarketOne](../entities/marketone.md) — where BYOL appears in this wiki as a live baseline, six years on.

## Concepts touched

- [Contrastive learning and InfoNCE](../concepts/learning/contrastive-learning.md) — the family BYOL leaves.
- [SIGReg](../concepts/world-models/sigreg.md) — what replaced this stack, and why.
- [JEPA](../concepts/world-models/jepa.md) — the anti-collapse design space BYOL anchors.
- [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) — the synthesis putting BYOL beside CPC, DINO and MAE.

## Open questions

- **The batch-norm controversy is not in this wiki.** Shortly after publication, two blog-level results argued BYOL's non-collapse depended on **batch normalization** acting as an implicit contrastive term, and a follow-up showed BYOL works without BN given careful initialization. The paper here has no BN in the target projector output and reports batch-size robustness *"only drops for smaller values due to batch normalization layers in the encoder"* — so BN is in the loop and its role is unresolved on this page.
- **Is the conditional-variance argument ever made rigorous?** It assumes an optimal predictor. Nothing in this wiki establishes when that assumption holds during training.
- **[SimSiam](../concepts/learning/contrastive-learning.md) is the missing control.** It reportedly drops the EMA entirely and keeps only stop-gradient + predictor — which Table 5b row 7 says gives **0.2%**. Either SimSiam's setup differs materially or one of the two results needs qualifying; the wiki cites SimSiam on 10 pages and has never read it.

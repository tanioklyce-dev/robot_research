---
title: "The anti-collapse lineage — five answers to one question, 2018–2026"
type: synthesis
created: 2026-09-03
updated: 2026-09-03
tags: [anti-collapse, self-supervised, contrastive-learning, byol, dino, mae, sigreg, jepa, lineage, evaluation]
---

Synthesized on ingesting the four most-referenced SSL primaries this wiki had never read — [CPC](../../sources/cpc-paper.md) (2018), [BYOL](../../sources/byol-paper.md) (2020), [DINO](../../sources/dino-paper.md) (2021), [MAE](../../sources/mae-paper.md) (2021) — against the [SIGReg](../../concepts/world-models/sigreg.md) line the wiki already covers in depth.

**The wiki's [anti-collapse ladder](../../concepts/world-models/jepa.md#common-training-challenges) starts in 2024 and treats everything before it as one rung labelled "EMA target encoder + stop-gradient."** Reading the primaries shows that rung is three different mechanisms that happen to share an EMA, and that the field's own history contains a control condition the current argument keeps forgetting.

> [!warning] Revised 2026-09-03 after ingesting [A Cookbook of Self-Supervised Learning](../../sources/ssl-cookbook.md)
> The Cookbook is the field map written by **[Balestriero](../../entities/randall-balestriero.md) (first author) and [LeCun](../../entities/yann-lecun.md)**, three years before LeJEPA. It was read as a check on this page, and it changed two things here.
>
> **1. It sorts the field on a different axis, and the two cuts disagree.** Its four families — Deep Metric Learning, **Self-Distillation**, Canonical Correlation Analysis, Masked Image Modeling — sort by *mechanism of the training signal*; this page sorts by *anti-collapse device*. The visible disagreements: **MoCo is self-distillation there** (its contribution is the momentum encoder, even though its loss is InfoNCE) and **SwAV is CCA**, not clustering. Neither cut is wrong; a reader should know they cross-cut.
>
> **2. It resolves the SimSiam question this page raised — and the answer strengthens the point rather than undoing it.** §3.4.1: EMA *"is not necessary … as long as the predictor is updated more often or has larger learning rate compared to the backbone,"* while BYOL's own τ=0 row genuinely collapses. **Both results stand. What is load-bearing is asymmetry between the branches, not the moving average specifically** — and the field kept the EMA for five years after establishing it was one of several ways to get that asymmetry. See "the field already ran the experiment" below, which this sharpens.

## The question, and the five answers

If you train an encoder to make two views agree, the trivial optimum is a constant. Everything below is a device for making that optimum unreachable.

| Year | Method | Device | Cost of the device |
|---|---|---|---|
| 2018 | [CPC](../../sources/cpc-paper.md) → SimCLR, MoCo | **Negative pairs** | Batch size / memory bank; augmentation sensitivity; semantic false negatives |
| 2020 | [BYOL](../../sources/byol-paper.md) | **Asymmetric predictor + EMA target, jointly** | No loss is being descended; guarantee is empirical |
| 2020 | [SimSiam](../../sources/simsiam-paper.md) | **Stop-gradient** — and nothing else | Explicitly declines to explain why it works |
| 2020 | [SimCLR](../../sources/simclr-paper.md) | negative pairs, made simple | augmentation design; a colour-histogram shortcut if you get it wrong |
| 2021 | [DINO](../../sources/dino-paper.md) | **Centering + sharpening of an EMA teacher** | Two temperatures; total failure without momentum |
| 2021 | [MAE](../../sources/mae-paper.md) | **None — the target is the input** | Slow convergence of linearly accessible quality |
| 2025 | [SIGReg](../../concepts/world-models/sigreg.md) | **One distributional term, with a theorem** | Does not deliver OOD robustness |
| 2026 | [SMWM](../../entities/smwm.md) | **Inverse dynamics** | Bounded by the richness of the action space |

## Three things the primaries settle that the wiki had wrong or vague

### 0. The mechanism is *asymmetry*, and stop-gradient is the irreducible part

Ingesting [SimSiam](../../sources/simsiam-paper.md) collapses several rungs into one statement. Take a plain weight-sharing Siamese network with a predictor on one branch:

| | Linear top-1 |
|---|---:|
| with stop-gradient | **67.7** |
| without stop-gradient | **0.1** |

And **nothing else** in the setup is doing collapse prevention: batch size is flat from 128 to 2048; removing all BN gives a poor-but-uncollapsed 34.6; cross-entropy instead of cosine works; removing symmetrization works. *"It is mainly the stop-gradient operation that plays an essential role."*

The EMA is then a *substitutable* source of asymmetry, and the wiki now has this from three directions: [BYOL's own Tables 21–22](../../sources/byol-paper.md) (hard-copy target + **10× predictor learning rate → 66.6–66.9** vs 72.5 with EMA), [the Cookbook](../../sources/ssl-cookbook.md) §3.4.1 (the same rule stated generally, plus stronger student-side augmentation as a third option), and SimSiam itself (constant predictor learning rate, batch 256, plain SGD).

**So the honest ladder has one fewer rung than it looked.** Negatives, EMA-plus-predictor, centering-plus-sharpening and stop-gradient-with-a-fast-predictor are four ways to break symmetry between the branches. Reconstruction avoids needing to.

SimSiam also supplies the best account of *what the predictor is for*: under an EM reading where the network alternates between parameters `θ` and per-image representations `η_x`, the **stop-gradient is a derivation** (η is constant while solving for θ) and the **predictor approximates an expectation over augmentations** that single-sample training drops. Tested: replacing the predictor with a moving-average `η` gets **55.0% with no predictor at all**, where removing it otherwise gives 0.1.

### 1. "EMA + stop-gradient" is not one mechanism

[BYOL's Table 5b](../../sources/byol-paper.md) is decisive. Without negatives, **the predictor alone gives 0.2% and the EMA target alone gives 0.3%**; together they give 72.5%. And [DINO's Table 7](../../sources/dino-paper.md) shows the *same* predictor, added to *its* EMA setup, changes nothing (71.8 vs 72.8) — while removing DINO's momentum drops it to **0.1%**.

So: BYOL needs predictor **and** EMA; DINO needs EMA **and** centering/sharpening, and does not want a predictor. Same family, incompatible internals. **A ladder rung that reads "EMA target encoder + stop-gradient" is describing at least two methods, one of which scores 0.3% under the other's ablation.**

### 2. The field already ran the "do you really need the EMA" experiment, and buried the answer

DINO's teacher ablation: student copy **0.1**, previous iteration **0.1**, **previous epoch 66.6**, momentum **72.8**. A one-epoch-stale teacher — no EMA, no momentum hyperparameter, no second set of weights to keep warm — lands in MoCo-v2/BYOL territory. The authors write that *"there is a space to investigate alternatives for the teacher."*

Nobody took it. The field scaled the EMA instead, and five years later [SIGReg](../../concepts/world-models/sigreg.md) removed it wholesale on theoretical grounds. **The cheap empirical middle was never explored**, and it is still cheap: a stale-teacher ablation on a modern JEPA is a few GPU-days.

### 3. Reconstruction is the control condition, and it is stronger than the wiki's framing of it

[MAE](../../sources/mae-paper.md) needs no anti-collapse term because a constant output cannot reconstruct the input. That is usually stated as a footnote; it should be stated as the baseline every other row is paying for. What it buys:

- **No augmentation design.** MAE reaches 84.0 fine-tuned with **no augmentation at all**, because random masking regenerates the signal each iteration. Every joint-embedding method must *specify the invariance by hand* — which is exactly the problem that turns out to be hard in a new domain ([financial time-series augmentations](../../concepts/economics/financial-time-series-augmentations.md), where the obvious choice provably cannot learn the target).
- **Architecture robustness**, for the same reason [Balestriero concedes about Dreamer](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md): reconstruction *"will produce good reconstructed pixels, training probably will not diverge."*
- **Transfer wins at scale**: COCO 53.3 AP<sup>box</sup> and ADE20K 53.6 mIoU with a ViT-L, beating supervised pretraining and every SSL contemporary at matched size.

## The live disagreement, and why it is not resolvable from what the wiki holds

[Balestriero's Day 3 argument](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md) against reconstruction has two parts: reconstruction loss carries **no information about representation quality** (identical train and test MSE, ~20 points of downstream accuracy apart, under linear *and nonlinear* probes), and MSE gradients follow the pixel covariance's **top eigenvectors**, so the low-frequency half is learned first.

[MAE's authors reject the metric](../../sources/mae-paper.md), five years earlier: *"linear probing and fine-tuning results are largely uncorrelated."* Tuning **one** transformer block takes ViT-L from 73.5 → 81.0, and MAE beats MoCo v3 at every partial-fine-tuning depth **despite MoCo v3's higher linear probe**.

> [!warning] Neither party has run the other's experiment, and the wiki should stop implying otherwise
> Balestriero's claim covers nonlinear probes explicitly, which would defeat MAE's rebuttal **if it transfers from his small constructed setting to ViT-L pretraining**. Nothing establishes that it does. MAE's rebuttal rests on partial fine-tuning, a protocol **no JEPA paper in this wiki reports**.
>
> What both sides agree on: MAE's linear probing is still climbing at 1600 epochs while contrastive methods saturate at 300. **Slow convergence of linearly accessible quality is a fact.** Whether it is a defect or an artifact of the probe is the open question.
>
> One unremarked corroboration for the spectral story, from MAE's own ablations: **PCA coefficients degrade** as a reconstruction target while **per-patch normalization** (local contrast, i.e. high frequency) **improves** results — *"the high-frequency components are useful in our method."* If the spectral argument is right, that is a prediction it makes.

## What this changes about the SIGReg case

Nothing about the theorems — and something about the pitch.

**SIGReg's practical selling point is insensitivity**: train stably in a new domain, on a new architecture, without a hyperparameter search. That is a real claim and the [Day 3 tutorial](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md) backs it with 50 architectures out of the box. **But it is the same claim BYOL made in 2020**, by a different route and with measurements to match (−9.1 points under augmentation removal against SimCLR's −22.2; flat from batch 4096 to 256). And the [MarketOne](../../entities/marketone.md) bake-off — the wiki's only head-to-head on a genuinely new domain — finds **BYOL and LeJEPA together on the efficient frontier**, with BYOL ranking ~4th on everything: the exact signature of a generalist.

So the honest summary of the 2018→2026 arc is not *heuristics were replaced by theory*. It is:

- **Provability improved decisively.** BYOL's non-collapse is a hypothesis its authors label as such; DINO's is a stability argument; SIGReg's is a theorem with a uniqueness converse.
- **Robustness improved much less than the rhetoric implies**, and the one thing nobody's anti-collapse term delivers is **out-of-distribution robustness** — [stable-worldmodel](../../sources/stable-worldmodel-paper.md) measures SIGReg-trained LeWM falling 50.8% → 6–26% under mild visual shift.

## What the Cookbook adds that this page had no room for

Three things that belong to the same argument and now live on their own pages:

- **[Dimensional collapse](../../concepts/learning/representation-evaluation.md)** — the failure mode *between* "collapsed" and "fine": rank-deficient embeddings, information duplicated across dimensions. It happens **after the projector and not before it**, at different severities for DINO, SimCLR and VICReg. Every method on the ladder above can pass its own anti-collapse check and still be quietly using a fraction of its dimensions.
- **[RankMe](../../concepts/learning/representation-evaluation.md)** — effective rank (entropy of the singular-value spectrum) as **label-free model selection**, recovering essentially all of a labelled ImageNet oracle's hyperparameter-selection quality. This is the standing "how do you know Z is good" question, answered in 2022.
- **The projector is worth ~20 points of ImageNet top-1** and is *not* an anti-collapse device. It absorbs augmentation noise (an oracle filtering bad views is worth **+6.3** points without it and **+0.6** with it) and is best understood as transfer-learning layer-cutting — *Guillotine Regularization*.

And one limitation that should temper the whole ladder for robotics: SSL methods carry a **hidden uniform prior**. They learn whatever is most discriminative *within a mini-batch*, which is class identity only when the data is balanced. **On imbalanced data it becomes low-level information instead** — and robot demonstration data is severely imbalanced.

## Experiments this makes cheap and obvious

1. **The stale-teacher ablation on a modern JEPA.** DINO says previous-epoch teacher = 66.6 vs momentum 72.8. Does the gap hold at LeWM scale, and does the memory saving matter on a single GPU?
2. **Partial fine-tuning of a JEPA encoder.** MAE's strongest defence uses a protocol the JEPA literature does not report. Tune `k` blocks of [LeJEPA](../../sources/lejepa-paper.md) and [V-JEPA 2](../../entities/v-jepa-2.md) features and see whether the ordering survives.
3. **Monitor a JEPA run for hidden instability.** [MoCo v3](../../sources/moco-v3-paper.md) shows ViT SSL loses **1–3% to instability without diverging**, that the loss curve hides it, and that **seed variance (0.1–0.3%) does not reveal it**. [LeJEPA](../../sources/lejepa-paper.md)'s central claim is *stability*, evidenced by loss curves and 50+ architectures landing within a small delta — which is exactly the evidence MoCo v3 says is insufficient. A k-NN or [RankMe](../../concepts/learning/representation-evaluation.md) monitor over a LeJEPA run tests the claim on its own axis. **And the free win: freezing the patch-projection layer at random init gave +0.8 to SimCLR, +1.3 to BYOL and +1.7 to MoCo v3, costs nothing, and is not mentioned anywhere in this wiki's JEPA material.**
4. **Reproduce Balestriero's two-autoencoder construction at MAE scale.** The claim that the ~20-point gap holds under nonlinear probes is the crux, and it has been demonstrated only where it was constructed.
5. **Run the MAE augmentation ablation on a JEPA.** MAE gets 84.0 with no augmentation. A joint-embedding method gets a constant. That asymmetry is the strongest practical argument for reconstruction and the wiki has never quantified it on the other side.
6. **Compute RankMe on a world-model latent.** If effective rank tracks planning success the way it tracks ImageNet accuracy, it is a label-free, decoder-free, planner-free model-selection signal for exactly the setting where labelled evaluation is a [real-robot rollout](../../concepts/robotics/robot-policy-evaluation.md). It would also test the [LeJEPA repo's unverified "94% Spearman" claim](../../sources/lejepa-github.md) against an independent metric.
7. **Check the uniform prior on robot data.** SSL degrades on imbalanced datasets because the most discriminative in-batch feature stops being the semantic one. Demonstration data is mostly approach and idle. Nobody in this wiki has looked.

## Related

- [JEPA](../../concepts/world-models/jepa.md) — the ladder this extends downward in time.
- [SIGReg](../../concepts/world-models/sigreg.md) · [identifiability](../../concepts/world-models/identifiability.md) — the provability end.
- [Contrastive learning and InfoNCE](../../concepts/learning/contrastive-learning.md) — the mechanism this lineage starts from.
- [Spectral theory of SSL](../../concepts/learning/spectral-theory-of-ssl.md) — the frame in which all of these are one objective over different graphs.
- [Representation evaluation](../../concepts/learning/representation-evaluation.md) — k-NN / linear / MLP / fine-tuning, RankMe, dimensional collapse.
- [Generative-video vs JEPA world models](generative-video-vs-jepa-world-models.md) — the same reconstruct-or-not question, one level up.

## Sources

- [CPC](../../sources/cpc-paper.md) · [BYOL](../../sources/byol-paper.md) · [DINO](../../sources/dino-paper.md) · [MAE](../../sources/mae-paper.md) — the first four primaries.
- [SimCLR](../../sources/simclr-paper.md) · [SimSiam](../../sources/simsiam-paper.md) · [MoCo v3](../../sources/moco-v3-paper.md) — the second tier, ingested 2026-09-03; SimSiam isolates stop-gradient, SimCLR supplies the colour-histogram shortcut and the projector measurement, MoCo v3 supplies hidden instability.
- [A Cookbook of Self-Supervised Learning](../../sources/ssl-cookbook.md) — the field's own taxonomy, by this line's own authors; the check that revised this page.
- [LeJEPA](../../sources/lejepa-paper.md) · [stable-worldmodel](../../sources/stable-worldmodel-paper.md) · [SMWM](../../sources/sensorimotor-world-models-paper.md) — the modern end.
- [Third World Modeling Workshop — Day 3](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md) — Balestriero's case against reconstruction, stated by its author.

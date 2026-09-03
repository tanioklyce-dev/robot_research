---
title: "The anti-collapse lineage — five answers to one question, 2018–2026"
type: synthesis
created: 2026-09-03
updated: 2026-09-03
tags: [anti-collapse, self-supervised, contrastive-learning, byol, dino, mae, sigreg, jepa, lineage, evaluation]
---

Synthesized on ingesting the four most-referenced SSL primaries this wiki had never read — [CPC](../../sources/cpc-paper.md) (2018), [BYOL](../../sources/byol-paper.md) (2020), [DINO](../../sources/dino-paper.md) (2021), [MAE](../../sources/mae-paper.md) (2021) — against the [SIGReg](../../concepts/world-models/sigreg.md) line the wiki already covers in depth.

**The wiki's [anti-collapse ladder](../../concepts/world-models/jepa.md#common-training-challenges) starts in 2024 and treats everything before it as one rung labelled "EMA target encoder + stop-gradient."** Reading the primaries shows that rung is three different mechanisms that happen to share an EMA, and that the field's own history contains a control condition the current argument keeps forgetting.

## The question, and the five answers

If you train an encoder to make two views agree, the trivial optimum is a constant. Everything below is a device for making that optimum unreachable.

| Year | Method | Device | Cost of the device |
|---|---|---|---|
| 2018 | [CPC](../../sources/cpc-paper.md) → SimCLR, MoCo | **Negative pairs** | Batch size / memory bank; augmentation sensitivity; semantic false negatives |
| 2020 | [BYOL](../../sources/byol-paper.md) | **Asymmetric predictor + EMA target, jointly** | No loss is being descended; guarantee is empirical |
| 2021 | [DINO](../../sources/dino-paper.md) | **Centering + sharpening of an EMA teacher** | Two temperatures; total failure without momentum |
| 2021 | [MAE](../../sources/mae-paper.md) | **None — the target is the input** | Slow convergence of linearly accessible quality |
| 2025 | [SIGReg](../../concepts/world-models/sigreg.md) | **One distributional term, with a theorem** | Does not deliver OOD robustness |
| 2026 | [SMWM](../../entities/smwm.md) | **Inverse dynamics** | Bounded by the richness of the action space |

## Three things the primaries settle that the wiki had wrong or vague

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

## Experiments this makes cheap and obvious

1. **The stale-teacher ablation on a modern JEPA.** DINO says previous-epoch teacher = 66.6 vs momentum 72.8. Does the gap hold at LeWM scale, and does the memory saving matter on a single GPU?
2. **Partial fine-tuning of a JEPA encoder.** MAE's strongest defence uses a protocol the JEPA literature does not report. Tune `k` blocks of [LeJEPA](../../sources/lejepa-paper.md) and [V-JEPA 2](../../entities/v-jepa-2.md) features and see whether the ordering survives.
3. **Reproduce Balestriero's two-autoencoder construction at MAE scale.** The claim that the ~20-point gap holds under nonlinear probes is the crux, and it has been demonstrated only where it was constructed.
4. **Run the MAE augmentation ablation on a JEPA.** MAE gets 84.0 with no augmentation. A joint-embedding method gets a constant. That asymmetry is the strongest practical argument for reconstruction and the wiki has never quantified it on the other side.

## Related

- [JEPA](../../concepts/world-models/jepa.md) — the ladder this extends downward in time.
- [SIGReg](../../concepts/world-models/sigreg.md) · [identifiability](../../concepts/world-models/identifiability.md) — the provability end.
- [Contrastive learning and InfoNCE](../../concepts/learning/contrastive-learning.md) — the mechanism this lineage starts from.
- [Spectral theory of SSL](../../concepts/learning/spectral-theory-of-ssl.md) — the frame in which all of these are one objective over different graphs.
- [Generative-video vs JEPA world models](generative-video-vs-jepa-world-models.md) — the same reconstruct-or-not question, one level up.

## Sources

- [CPC](../../sources/cpc-paper.md) · [BYOL](../../sources/byol-paper.md) · [DINO](../../sources/dino-paper.md) · [MAE](../../sources/mae-paper.md) — the four primaries.
- [LeJEPA](../../sources/lejepa-paper.md) · [stable-worldmodel](../../sources/stable-worldmodel-paper.md) · [SMWM](../../sources/sensorimotor-world-models-paper.md) — the modern end.
- [Third World Modeling Workshop — Day 3](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md) — Balestriero's case against reconstruction, stated by its author.

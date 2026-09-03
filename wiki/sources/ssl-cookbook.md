---
title: "A Cookbook of Self-Supervised Learning (Balestriero, …, LeCun et al., 2023)"
type: source
url: https://arxiv.org/abs/2304.12210
fetch_url: https://arxiv.org/pdf/2304.12210v2
local_path: raw/2304.12210v2.pdf
sha256: a8d30ab7753f5e156023de839f6594911360f190e520df581dd4081dd0386709
author: "Randall Balestriero, Mark Ibrahim, Vlad Sobal, Ari Morcos, Shashank Shekhar, Tom Goldstein, Florian Bordes, Adrien Bardes, Gregoire Mialon, Yuandong Tian, Avi Schwarzschild, Andrew Gordon Wilson, Jonas Geiping, Quentin Garrido, Pierre Fernandez, Amir Bar, Hamed Pirsiavash, Yann LeCun, Micah Goldblum (Meta AI/FAIR; NYU; Maryland; UC Davis; Mila; Gustave Eiffel; Inria Rennes)"
published: 2023-04-24
venue: "arXiv (v2, 2023-06-28)"
format: survey / practitioner guide (PDF, 71 pp.)
tags: [ssl, survey, taxonomy, balestriero, lecun, projector, dimensional-collapse, rankme, evaluation, augmentation, anti-collapse, infonce, foundational]
ingested: 2026-09-03
---

## Summary

**The field map, written by the two authors this wiki cites most, plus 17 others.** A 71-page practitioner's guide whose stated purpose is to lower SSL's barrier to entry, on the grounds that the field suffers from *"(i) its computational cost, (ii) the absence of fully transparent papers detailing the intricate implementations required to fully enable SSL's potential, and (iii) the absence of a unified vocabulary and theoretical view."*

It was ingested as a **test**: the wiki had just built [an anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) from four primaries, and this is the taxonomy its own practitioners published. It passed as a test and failed as a confirmation — **two things this wiki asserted a day earlier are wrong or over-stated**, and the corrections are recorded below and on the affected pages.

Note the author list: **[Balestriero](../entities/randall-balestriero.md) is first author and [LeCun](../entities/yann-lecun.md) is second-to-last**, with **Vlad Sobal** ([PLDM](../entities/pldm.md)) and Adrien Bardes (VICReg) also on it. This is the LeJEPA line's own view of the field, three years before [LeJEPA](lejepa-paper.md).

## The taxonomy: four families, not one axis

| Family | Members | Principle |
|---|---|---|
| **Deep Metric Learning** | SimCLR, NNCLR, MeanSHIFT, SCL | contrastive loss over positive/negative pairs |
| **Self-Distillation** | BYOL, SimSiam, DINO — **and MoCo** | two encoders, one predicts the other; prevent collapse by asymmetry |
| **Canonical Correlation Analysis** | VICReg, Barlow Twins, **SwAV**, W-MSE | analyze cross-covariance; decorrelate feature dimensions |
| **Masked Image Modeling** | BEiT, MAE, SimMIM | degrade the input, restore it |

> [!warning] Two placements contradict what this wiki wrote
> **MoCo is filed under self-distillation, not contrastive.** The wiki's [contrastive learning](../concepts/learning/contrastive-learning.md) page listed "CPC → SimCLR, MoCo" as one family. The Cookbook's reasoning is that MoCo's defining contribution is the *momentum encoder* — *"originally the momentum encoder was introduced as a substitute for a queue in contrastive learning"* — which puts it with BYOL and DINO mechanically even though its loss is InfoNCE. **SwAV lands in the CCA family**, not with clustering methods.
>
> This is a real disagreement about the right axis, not a labelling quibble: the Cookbook sorts by **mechanism of the training signal**, this wiki's synthesis sorts by **anti-collapse device**. Both are defensible and they cross-cut. The synthesis now says so.

The Cookbook also gives a **paradigm-shift table** (Fig. 4) separating classical Deep Metric Learning from contrastive SSL: pairs from labels/fixed transforms → pairs from *continuously sampled* augmentations; hard-negative mining → random sampling; encoder → **encoder + projector MLP**; N < 200k → large datasets; k-NN validation → k-NN *plus* linear probing.

## Correction 1 — InfoNCE's lineage predates CPC

The wiki's [CPC page](cpc-paper.md) called it "the origin of InfoNCE." **The Cookbook's Figure 2 shows CPC coined the *name* and supplied the MI bound; the loss form arrived in stages before it:**

| Year | Work | Contribution |
|---|---|---|
| 1993 | [Bromley et al.](bromley1993-siamese-signature-verification.md) | the contrastive loss, for signature verification |
| 2004 | Goldberger et al. | Neighbourhood Component Analysis — the softmax-over-distances form |
| 2005–06 | Chopra et al.; Hadsell et al. | contrastive loss formalized with a margin |
| 2009–10 | Weinberger & Saul; Chechik et al. | triplet loss |
| 2016 | Sohn | **(N+1)-tuple loss** — inner products, ℓ2 penalty, negatives drawn from other samples in the batch |
| 2018 | **Wu et al.** | NCE loss + **"non-parametric softmax"**; introduces **explicit normalization, the temperature τ, and the momentum-encoder idea** (via proximal optimization) |
| 2018 | **[CPC](cpc-paper.md)** | *"coins the name infoNCE by removing the proximal constraint and using positive pairs"* |

So **the temperature and the momentum encoder both come from Wu et al. 2018, not from CPC and not from MoCo.** What CPC contributes uniquely is the mutual-information framing and the `I ≥ log N − L_N` bound. The CPC page has been corrected.

The Cookbook also lists the **offspring** (Fig. 3): MoCo (momentum encoder + queue), MoCoV2 (+projector), MoCoV3 (+ViT), SimCLR (removes the momentum encoder; NT-Xent), DCL (removes the positive from the denominator), NNCLR (nearest neighbours from a queue), RELIC (+KL invariance term), PCL (prototypes). And **Tian's unified family** `L_{φ,ψ}`, under which InfoNCE, MINE, Triplet, Soft Triplet, N+1-Tuplet and Lifted Structured are all one loss with different monotone φ, ψ.

## Correction 2 — "contrastive methods need large batches" is misleading

The wiki's [contrastive learning](../concepts/learning/contrastive-learning.md) page derived the large-batch requirement from CPC's MI bound and treated it as a standing cost. §3.5.1 says otherwise, flatly:

> *"It was originally thought that contrastive methods such as SimCLR or MoCo require large batch sizes or memory banks to work. **This turns out to be misleading** as both methods can be made to work at small batch sizes."*

With **square-root learning-rate scaling** (SimCLR's own appendix) the gain is up to 5 points at 100 epochs; **SimCLR trains on ImageNet on a single GPU** without an important drop (Bordes et al. 2023); **DCL reaches top performance at batch 256** for SimCLR and queue 256 for MoCo, simply by removing the positive pair from the softmax denominator. The bound is real; the engineering consequence was over-stated by a decade of papers, and by this wiki a day ago.

## Correction 3 — the SimSiam/BYOL contradiction the wiki flagged is resolved, and the resolution is a hyperparameter

The [BYOL page](byol-paper.md) records that its Table 5b scores **0.2%** for *predictor without EMA target, no negatives*, while SimSiam claims that configuration works — and filed it as needing resolution. §3.4.1:

> *"While the original BYOL method is based on EMA updates … it was later confirmed that **EMA is not necessary** (i.e., the online and target networks can be identical). This is also confirmed with SimSiam, **as long as the predictor is updated more often or has larger learning rate compared to the backbone**. … For BYOL, a stop gradient of the online network, meaning the decay rate is 0 for the target network, collapses as shown in Table 5 of Grill et al."*

So both results stand. **The EMA is replaceable — by a learning-rate asymmetry on the predictor.** What is load-bearing is *asymmetry between the branches*, not the moving average specifically. Which sharpens the synthesis's point rather than undoing it: the field kept the EMA long after establishing it was one of several ways to get the asymmetry.

Supporting numbers from §3.4.2: **removing BYOL's predictor drops it 68% → 21%**; removing SimSiam's collapses it below 1%. Even a *linear* predictor works and recovers from bad initialization in 10–20 epochs. Tian et al. (2021) **prove** the predictor gives BYOL/SimSiam dynamics nontrivial stable fixed points, and **DirectPred** sets the predictor analytically by eigendecomposition instead of learning it.

## What the wiki did not have at all

### RankMe — evaluation with no labels, no training, no probe

This is the most useful thing in the document for this wiki, because it answers a question [Balestriero posed on Day 3 as open](chicago-booth-world-modeling-workshop-2026-day3.md) — *"how can you assess if you learned a good Z without having to reconstruct?"* — with a method from 2022 that the survey he co-authored already recommends.

**RankMe** (Garrido et al. 2022) is the **effective rank** of the embeddings: the exponentiated entropy of their singular-value distribution,

`RankMe(Z) = exp(−Σₖ pₖ log pₖ)`, `pₖ = σₖ(Z) / ‖σ(Z)‖₁ + ε`

No labels, no optimization, no hyperparameters. Table 3 compares hyperparameter selection by RankMe against an **ImageNet-labelled oracle**, across VICReg / SimCLR / DINO and on both ImageNet and a 10-dataset OOD average:

| | VICReg (cov / inv) | SimCLR (temp) | DINO (t-temp / s-temp) |
|---|---|---|---|
| ImageNet oracle | 68.2 / 68.2 | 68.5 | 72.3 / 72.4 |
| **RankMe** | **67.8 / 67.9** | **67.1** | **72.2 / 72.4** |
| α-ReQ | 67.9 / 67.5 | 63.5 | 71.7 / 66.2 |

**RankMe recovers essentially all of the labelled oracle's selection quality.** Its stated limits are honest: full rank is a **necessary, not sufficient** condition (a random Gaussian matrix is full-rank and useless), and it works for hyperparameter selection **within** a method rather than for ranking different methods.

### Dimensional collapse — the failure mode between "collapsed" and "fine"

§2.6.2. Distinct from total collapse: the embedding becomes **rank-deficient**, information duplicated across dimensions. Measured through the singular-value spectrum, and Figure 9 carries the finding that matters: **dimensional collapse happens after the projector and not before it**, at different severities for DINO, SimCLR and VICReg. Several works find it a **good proxy for downstream performance**. Measures on offer: singular-value entropy (RankMe), classical rank estimators, power-law fits, spectrum AUC.

### The projector, which the wiki treated as an implementation detail

- **Worth ~20 points of ImageNet top-1** at 100 epochs — SimCLR 50 → 68, VICReg 48 → 68. It is *not* what prevents collapse.
- **Guillotine Regularization** (Bordes et al.): the projector is transfer-learning layer-cutting under another name. Its benefit comes from **misalignment between the pretext task and the downstream task** — and when that misalignment is removed (using labels to form positive pairs) the best linear probe moves *to the last projector layer* instead of the backbone.
- It **absorbs augmentation noise.** Pretraining VICReg without a projector but with an oracle filtering semantically inconsistent views gains **+6.3 points**; with a projector, the same oracle gains **+0.6**.
- Very large projector output dimensions are **not** required once the intermediate widths and loss weights are scaled — VICReg at 256-d goes 55.9% → 65.1% with that tuning, peaking around 1024.
- **SSL benefits from wider *backbone* output dimensions where supervised training degrades** — and widening the backbone output beats making the ResNet deeper or wider.

### The uniform prior — why SSL fails on the data robots actually collect

§3.3. SSL methods carry a **hidden uniform prior**: they spread data uniformly in representation space and therefore learn whatever is most discriminative *within a mini-batch*. On balanced data that is class identity. **On imbalanced data it is low-level information instead**, and downstream classification degrades. *"Since real world data is imbalanced, such a limitation is an important factor that made the use of SSL methods on vast amount of uncurated data challenging."*

Supporting evidence in Table 1: pretraining on the target dataset vs on ImageNet is a wash for most methods — **except SimCLR and MSN, which fall sharply when pretrained directly on iNaturalist18** (SimCLR 39.2 → 28.6), the dataset with a power-law class distribution.

### Augmentation is the specification, and there are exactly two escapes

*"The deep nature of what is learned by the SSL models is defined by the data augmentation pipeline."* Different augmentations produce different invariances, and which is right depends on the downstream task — ColorJitter helps classification and does not always help elsewhere. The two named ways out of hand-designing it are **[MAE](mae-paper.md)** (reconstruct pixels, no invariance to specify) and **I-JEPA / data2vec 2.0** (predict *representations* of missing parts). Perfect invariance is never actually reached, and the projector is why.

Also **multi-crop** (§3.1.1), from SwAV: 2 global 224² crops plus N local 96², with the loss computed 2(N−1) times. **+4 points for +25% training time** at 160² globals — *"a very useful strategy for a marginal additional compute cost,"* now near-ubiquitous. k-NN-graph alternatives (MSF) get a similar effect for **+6%** training time.

## The evaluation section, and an awkward fact for the Day 3 argument

§3.7 lays out four protocols with labels — **k-NN, linear, MLP, full fine-tuning** — plus label-free ones. Three findings the wiki needs:

- **An online linear probe tracks the offline one closely and never overfits** (Fig. 13), which retroactively validates the online probe in the [Booth tutorial code](wm-booth-lejepa-lewm-tutorial-repo.md).
- **MLP probes overfit**: *"the best MLP head might not be the ones you get after 100 epochs."* Non-linear probing needs early stopping — a caveat on both sides of the linear-vs-nonlinear dispute.
- And the sentence to sit with:

> [!warning] The survey says the field adopted MAE's position — and Balestriero is its first author
> *"The Masked Auto-encoders (MAE) paper re-introduced fine-tuning as the main evaluation metrics. The main arguments are that **linear-probing is uncorrelated with fine-tuning and transfer learning performances**, and that small MLP heads do not evaluate the strength of the method to create strong but non-linear features. **The majority of works that followed focused on this type of evaluation** (and sometimes do not report linear/MLP results). It has been shown that **contrastive methods show inferior performance than masked image modeling with regards to fine-tuning, because they are less 'optimization friendly'** — which explains the overall interest over MIM."*
>
> The wiki filed the MAE-vs-Balestriero evaluation dispute [as unresolved](../syntheses/world-models/ssl-anti-collapse-lineage.md). It is still unresolved as a *technical* matter — but it is no longer true that this is Balestriero's position against MAE's. **In 2023 he co-authored a survey reporting that MAE's argument had been accepted by the field.** The Day 3 tutorial's probe-based case against reconstruction is made three years later, and this wiki has no source explaining what changed. That gap is the honest statement of where things stand.

## Beyond images (§4), briefly

Domain notes worth keeping because the wiki's SSL material is drifting toward non-vision domains: **masking is the one generically transferable technique** across images, audio, text and tabular data. Audio breaks the vision playbook specifically — horizontal flips destroy speech, spectrogram masking wants horizontal/vertical *bands* rather than random pixels, and background noise makes reconstruction in input space harder than in text. **Text is dominated by reconstruction, not contrastive**, because it is a clean signal. Tabular SSL mostly masks and predicts the mask vector itself. The general lesson matches [financial time-series augmentations](../concepts/economics/financial-time-series-augmentations.md): the augmentation set is domain structure, not a library import.

## Entities mentioned

- [Randall Balestriero](../entities/randall-balestriero.md) — first author.
- [Yann LeCun](../entities/yann-lecun.md) · [Meta FAIR](../entities/meta-fair.md) — most of the author list.
- [PLDM](../entities/pldm.md) — Vlad Sobal, co-author here, is its author.
- [BYOL](../entities/byol.md) · [DINO](../entities/dino.md) · [MAE](../entities/mae.md) · [DINOv2](../entities/dinov2.md).

## Concepts touched

- [Representation evaluation](../concepts/learning/representation-evaluation.md) — **the new page this source creates**: k-NN / linear / MLP / fine-tuning, RankMe, dimensional collapse.
- [Contrastive learning and InfoNCE](../concepts/learning/contrastive-learning.md) — corrected twice by this source.
- [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) — the taxonomy comparison.
- [SIGReg](../concepts/world-models/sigreg.md) · [JEPA](../concepts/world-models/jepa.md) · [spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md).

## Open questions

- **What changed between 2023 and Day 3?** The Cookbook reports the field accepting MAE's evaluation argument; Balestriero's 2026 tutorial argues against reconstruction on probe accuracy. No source here bridges them.
- **Does RankMe work on a world-model latent?** It is defined on SSL embeddings for hyperparameter selection. If it transfers to an action-conditioned latent it is a **label-free, decoder-free, planner-free** model-selection signal — precisely the gap named on Day 3, and a possible explanation of [the unverified "94% Spearman between training loss and downstream performance" claim](lejepa-github.md) in the LeJEPA repo. **The highest-value experiment this source suggests.**
- **Is the uniform prior a problem for robot data?** Robot demonstration datasets are severely imbalanced (most frames are approach and idle). The Cookbook's mechanism — the most discriminative feature in a mini-batch stops being the semantic one — predicts trouble, and nothing in this wiki has looked.
- **Where does [SIGReg](../concepts/world-models/sigreg.md) sit in the four-family taxonomy?** It postdates the survey. It regularizes the embedding *distribution*, which is the CCA family's job, while being used in a self-distillation-shaped architecture without the distillation. Possibly a fifth family; possibly CCA taken to its limit.
- **α-ReQ vs RankMe.** Table 3 shows α-ReQ notably worse on SimCLR's temperature (63.5 vs 67.1) and DINO's student temperature (66.2 vs 72.4). Neither is ingested; the comparison is one table in a survey.

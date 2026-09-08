---
title: "Introduction to Latent Variable Energy-Based Models: A Path Towards Autonomous Machine Intelligence (Dawid & LeCun, 2023)"
type: source
url: https://arxiv.org/abs/2306.02572
fetch_url: https://arxiv.org/pdf/2306.02572
local_path: raw/2306.02572v1.pdf
sha256: 1f5ad87c7da931599dca22ee60612f396e8ac22306876d0a2800ced47a2f1a92
author: "Anna Dawid (ICFO / University of Warsaw), Yann LeCun (Courant Institute NYU, Meta-FAIR)"
published: 2023-06-05
venue: "Les Houches Summer School on Statistical Physics and Machine Learning 2022 lecture notes; arXiv:2306.02572v1 (cs.LG, cond-mat.dis-nn, stat.ML), 23 pp + appendix, 11 figures. Later published in J. Stat. Mech. — DOI 10.1088/1742-5468/ad292b."
format: lecture notes (PDF)
tags: [lecun, dawid, energy-based-models, latent-variable, jepa, h-jepa, les-houches, statistical-physics, collapse, contrastive, vicreg, hopfield, boltzmann-machine, pedagogy]
ingested: 2026-09-07
---

## Summary

**The derivation the [2022 position paper](lecun2022-path-towards-ami.md) skips.** Anna Dawid wrote up three lectures LeCun gave at the **Les Houches Summer School on Statistical Physics and Machine Learning** (July 2022, organized by Krzakala and Zdeborová) for an audience of physicists, and the result is the cleanest statement in this wiki of *why* the [JEPA](../concepts/world-models/jepa.md) architecture has the shape it does. The chain is short and each link is argued:

**probabilistic models are intractable in high dimensions → use [energy-based models](../concepts/learning/energy-based-models.md) → but any multimodal EBM can collapse → contrastive fixes scale exponentially with dimension → so use regularized ones → apply that to a joint-embedding architecture with a latent variable → JEPA → stack it → H-JEPA.**

The position paper asserts most of these steps. These notes derive them, and the derivation exposes a piece of the blueprint that **the entire subsequent JEPA literature has not built** — see below.

## Four things stated here more sharply than anywhere else in this wiki

### 1. The energy is for inference. It is not the training objective.

Boxed in the text, and this wiki's [EBM page](../concepts/learning/energy-based-models.md) did not draw the line:

> An important thing to note is that the energy function discussed here is used only for inference, not learning. Training of an EBM involves a **loss function** and consists in finding an energy function in which observed configurations of the variables are given lower energies than unobserved ones.
>
> Therefore, **the energy function is not the objective function to minimize within the learning! The energy is used only for inference.**

Hopfield networks are given as the degenerate case where the two *are* the same — `L(y_train, w) = F_w(y_train)` — and the notes name the consequence directly: no contrastive term, so **spurious minima**, energy wells the data never dug. That is collapse's older sibling, and it is why the 1982 architecture is *"less usable in practice."*

### 2. Maximum likelihood **is** a contrastive method

§4.1.2, and it is a two-line derivation. Substituting the Gibbs–Boltzmann form into the negative log-likelihood gives

`L_NLL(x, y, w) = F_w(x, y) + (1/β) log ∫ dy′ exp[−β F_w(x, y′)]`

— first term pushes the data's energy **down**, second term pushes the energy of everything **up**, and its gradient is an expectation approximable by Monte Carlo samples. So:

> It means that the minimization of `L_NLL` consists in minimizing the energy of training samples while pulling up the energy of Monte Carlo-generated samples. **Negative log-likelihood is then a contrastive method!**

With the failure mode named: maximum likelihood *"wants to make the difference between the energy on the data manifold and the energy just outside of it infinitely large, making the data manifold an **infinitely deep and infinitely narrow canyon**"* — hence the need for a prior or weight constraints.

This puts the whole autoregressive-vs-JEPA argument on one axis instead of two. LeCun's objection to LLM-style training is not that likelihood is a different paradigm; it is that likelihood is **a contrastive method with the worst possible negative-sampling scheme**.

### 3. "Every model that can be multimodal is susceptible to collapse"

The cleanest available statement of the tradeoff, and it generalizes what [the anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) observed empirically about reconstruction. Fig. 5 contrasts two architectures:

| | Deterministic regression `F = ‖y − Net(x)‖` | Joint embedding `F = D(s_x, s_y)` |
|---|---|---|
| Collapse | **impossible** | **possible** |
| Multimodal / non-deterministic prediction | **impossible** | possible |

> All in all, **every model that can be multimodal, i.e., have multiple predictions for a single input, is susceptible to collapse.**

Collapse is therefore not a bug in joint-embedding training. It is the price of admission to multimodality, and the footnote makes it explicit that the safe architecture *"has no way of expanding predictions to be multimodal."*

### 4. Regularization = bounding the **volume** of the low-energy region

And the unification that follows is worth memorizing. Everything below is the same objective `L = D(y, Dec(Enc(y))) + R(Enc(y))`, differing only in where `R` comes from:

| Method | Source of the regularization |
|---|---|
| PCA | low rank of `wᵀw` |
| Autoencoder | small bottleneck |
| k-means | discreteness of the code |
| Gaussian mixtures | same, softened |
| Sparse coding | explicit `λ‖z‖₁` |

*"Contrastive methods push the energy up outside the data; regularized methods limit how much space the low-energy region is allowed to occupy."* Score matching is listed as a third route — minimize the gradient and maximize the curvature of the energy at data points.

And the reason the field went this way, stated as the load-bearing claim:

> The need for generating contrastive samples is the source of **bad (even exponential!) scaling of contrastive methods with the data dimension**… this unfavorable scaling makes contrastive methods **unlikely to lead to autonomous intelligence of the future.**

## The blueprint JEPA has four loss terms. Modern JEPAs have one and a half.

Fig. 10 is the original JEPA training objective, and it is not "prediction error plus an anti-collapse term":

| Term | Purpose |
|---|---|
| `D(s̄_x, s_y)` | **minimize** prediction error in representation space |
| `−I(s_x)` | **maximize** information content of `s_x` about `x` |
| `−I(s_y)` | **maximize** information content of `s_y` about `y` |
| `R(z)` | **minimize** information capacity of the latent variable |

[VICReg](vicreg-paper.md) is given as *the* worked example of the information-maximization terms — variance hinge keeps components from being constant, covariance decorrelation keeps them from being redundant, expander kills the nonlinear dependencies. [BYOL](byol-paper.md), [SimSiam](simsiam-paper.md) and [Barlow Twins](barlow-twins-paper.md) are named as siblings, plus a pointer to 1992 as the earliest version of the idea.

> [!warning] The latent variable `z` is the part nobody built
> **`z` is the entire stated reason for choosing EBMs over probabilistic models.** The argument runs: images and video are multimodal, a single-prediction model averages over possible futures and produces blur, probabilistic models can't be normalized in high dimensions, therefore EBM — and the mechanism that actually *represents* the multiple futures is the latent variable. Table 1 gives the intended reading: pose, lighting, segmentation, the behavior of other drivers.
>
> **No JEPA in this wiki has one.** Not **I-JEPA**, not [V-JEPA 2](v-jepa-2-paper.md) or [2.1](v-jepa-2-1-paper.md), not [LeJEPA](lejepa-paper.md) or [LeVJEPA](levjepa-paper.md), not [PLDM](pldm-paper.md), [DINO-WM](dino-wm-paper.md) or [LeWorldModel](leworldmodel-paper.md). The predictors are deterministic. The blur problem the architecture was designed around is handled by *encoding it away* — discard the unpredictable detail — rather than by *representing* it.
>
> That is a real solution to a narrower problem, and it is not the one in the blueprint. It also explains the [world-action model](../concepts/world-models/world-action-model.md) line: **actions are doing `z`'s job.** [Balestriero says this almost in so many words](information-bottleneck-ep11-jepa-balestriero.md) three years later — *"if you already have very rich actions, you don't have a lot of uncertainty, then probably you are good enough to not use a latent variable… if you have very weak actions or no actions… you'll just learn to predict the average of all those possible scenarios."*
>
> And the hard part has not moved in three years. These notes, 2023: *"The tricky part is that **the information capacity of the latent variable must be minimized**. Otherwise, the training may put all the information needed for the prediction into them."* Balestriero, 2025: *"you want a very constrained latent variable that lives in a very small space, and **how to control this capacity is also a big research question**."* Same sentence, two authors, no progress recorded in between.

## Smaller things worth keeping

- **A denoising autoencoder is classified as a *contrastive* EBM** (§5.3) — the corruption *generates* the contrastive points. This cross-cuts [the anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md), which files [MAE](mae-paper.md) under *"no mechanism at all."* Both readings are defensible and they are not the same claim: the lineage means *no explicit anti-collapse term in the loss*; these notes mean *the loss is still of the push-down-here/pull-up-there form*, with corrupted inputs standing in for negatives.
- **The failure case of denoising is geometric.** A point equidistant between two branches of a spiral cannot be denoised — the model must output one answer for a genuinely bimodal target. *"This pitfall is due to the folded structure of the data"* — and the footnote says latent variables fix it. This is the multimodality argument in one picture.
- **Hopfield (1982) → Boltzmann machine (1983) is the prehistory of the anti-collapse ladder.** Hopfield: energy = loss, Hebbian update, no contrastive term, spurious minima. Boltzmann: adds hidden units — *"the first introduction of hidden units"*, i.e. latent variables — and a contrastive term sampled by MCMC, with **positive and negative phases** of learning. The wiki's ladder starts in 2018; the pattern is 40 years older, and both endpoints are explicitly spin-glass constructions.
- **Physics vocabulary is load-bearing, not decorative.** β is the inverse temperature, the normalizer is the partition function, and marginalizing the latent gives *"a formula known from statistical physics, where F is the **free energy**"* — with the practical note that marginalization is expensive in high dimensions and *"usually replaced with a cheaper minimization instead."* Minimization vs marginalization over `z` is min-energy vs free-energy, and JEPA takes the cheap one.
- **Why not normalize even when you could:** normalizing scores per-state introduces the **label bias problem**, so *"it is hurtful to normalize those scores."* A specific technical objection, distinct from the tractability one.
- **What is lost by abandoning probability**, stated honestly: uncertainty becomes hard to reason about, and **energies are uncalibrated** — *"combining two separately trained EBMs is not straightforward"*, which is why the architecture must avoid transferring outputs between separately trained components.
- **H-JEPA** (§6.2) is two stacked JEPAs where the upper level predicts further with fewer details, *"assisted by CNNs and pooling layers between levels to coarse-grain the representation."* Compare what was actually built: [HWM](hwm-paper.md) (2026) is exactly two levels, goal-image conditioned, and wraps *existing* world models rather than co-training a stack.

## Where to hold it at arm's length

- **This is exposition, not a result.** No experiments, no numbers, no ablations. Its authority is that LeCun gave the lectures; its content is his 2022 position paper reorganized for physicists, plus standard EBM material.
- **The file here is the arXiv v1 preprint**, not the version published in J. Stat. Mech. (DOI `10.1088/1742-5468/ad292b`). Journal editing may have changed things; nothing in this wiki has compared them.
- **Written mid-2022, published mid-2023.** It predates **I-JEPA**'s publication and everything after. Where it describes what JEPAs *will* look like, read it as the design intent — which is exactly why the missing-`z` observation above is worth having.
- **The "exponential scaling of contrastive methods" claim is asserted, not derived**, and it is the hinge of the whole argument. [SimCLR](simclr-paper.md) and [MoCo](moco-v3-paper.md) went on to work at scale; the honest version is that contrastive methods have a batch-size/negative-count appetite, not that they provably fail.

## Entities mentioned

- [Yann LeCun](../entities/yann-lecun.md) — lecturer. **Anna Dawid** (ICFO / Warsaw) — author of the write-up; no page.
- [VICReg](vicreg-paper.md) · [BYOL](../entities/byol.md) · [SimSiam](../entities/simsiam.md) · [Barlow Twins](barlow-twins-paper.md) — named as the regularized family.
- **John Hopfield**, **Geoffrey Hinton** & **Terrence Sejnowski** — Hopfield networks and Boltzmann machines. **Florent Krzakala**, **Lenka Zdeborová** — school organizers. No pages.

## Concepts touched

- [Energy-based models](../concepts/learning/energy-based-models.md) — the energy/loss distinction, NLL-as-contrastive, and the regularized-AE unification.
- [JEPA](../concepts/world-models/jepa.md) — the original four-term objective and the unbuilt latent variable.
- [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) — collapse as the price of multimodality; the 1982–83 prehistory.
- [World-action model](../concepts/world-models/world-action-model.md) — actions as the substitute for `z`.
- [Contrastive learning](../concepts/learning/contrastive-learning.md) — reframed as one method of energy-landscape sculpting.
- [Variational autoencoder](../concepts/learning/variational-autoencoder.md) — §4.2.2's variational marginalization of `z` is the VAE bound in energy language.

## Open questions

- **Would a JEPA with an actual latent variable beat one without?** The blueprint says the latent is how multimodality gets represented; the field encoded it away instead. Nobody in this wiki has run the comparison, and it is a well-posed experiment on any existing latent world model.
- **Is the "actions replace `z`" reading correct?** It is consistent with two sources and stated by neither. The test is a world model with *weak* actions — where the notes and Balestriero both predict mean-prediction failure that a latent variable would fix.
- **Do the `−I(s_x)`, `−I(s_y)` terms survive in modern practice, or only their spirit?** [SIGReg](../concepts/world-models/sigreg.md) matches an isotropic Gaussian; VICReg maximizes variance and decorrelates. Both prevent collapse, but only one is derived as information maximization, and [the identifiability result](../concepts/world-models/identifiability.md) argues the Gaussian is uniquely correct on other grounds entirely.
- **What is reference [62], "related ideas explored already in 1992"?** Almost certainly Schmidhuber's predictability minimization, and the wiki has nothing on it. If so, the joint-embedding idea has a claimed priority a full 26 years before [CPC](cpc-paper.md).

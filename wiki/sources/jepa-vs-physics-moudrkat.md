---
title: "JEPA Through the Eyes of a Physicist (Fajmanova, 2026)"
type: source
url: https://github.com/moudrkat/jepa-demo/blob/main/JEPA_VS_PHYSICS.md
fetch_url: https://raw.githubusercontent.com/moudrkat/jepa-demo/main/JEPA_VS_PHYSICS.md
local_path: raw/2026-03-22-jepa-vs-physics-moudrkat.md
sha256: a51f692b962194d648caf5425c9c2a3d3813d9d44ad3a78afc3ca53b81968263
author: "Katerina Fajmanova (moudrkat)"
published: 2026-03-22
venue: "companion essay in the `moudrkat/jepa-demo` GitHub repository (MIT, 0 stars, 12 runnable demos); ~2,800 words"
format: essay (Markdown, in-repo)
tags: [jepa, energy-based-models, renormalization-group, statistical-physics, coarse-graining, spin-glass, i-jepa, v-jepa-2, explainer, secondary-source]
ingested: 2026-09-07
---

## Summary

**An independent explainer arguing that JEPA is learned coarse-graining, written by a physicist and shipped alongside twelve runnable demos.** The thesis: a 224×224 image has 150,528 degrees of freedom, most of them irrelevant; statistical mechanics has one canonical answer to that situation, and [JEPA](../concepts/world-models/jepa.md)'s encoder is doing a learned version of it.

> This is coarse-graining not by a physicist's intuition about what matters, but by a mathematical criterion: **keep what's predictable, discard what's not.**

It is a **secondary source with no results of its own**, and it is worth a page for three reasons: it supplies a mapping table the wiki did not have, it points at three genuine LeCun-co-authored statistical-physics papers the wiki has never ingested, and its one central mechanistic claim is **wrong in a way that is diagnostic** of how JEPA is understood outside the labs.

## The mapping, which is the useful part

| Renormalization Group | JEPA encoder |
|---|---|
| Integrate out short-wavelength modes | Discard pixel-level detail |
| Retain long-range correlations | Retain semantic structure |
| Effective theory at coarser scale | Latent representation |
| **Universality** — different microscopic systems, same macroscopic behavior | **Transfer** — different images, same representation for the same concept |

The last row is the one that earns its keep. *Universality* is a precise statement about why microscopically different systems share critical exponents, and reading transfer learning as its analogue is a sharper framing than "the features generalize." The essay's own example: I-JEPA trained on ImageNet clusters unseen flower photographs by radial petal structure — *"different microscopic configurations mapping to the same macroscopic class."*

Its companion argument about **why latent prediction is not just cheaper but better-posed** is also cleanly put, and is the [world-model](../concepts/world-models/world-model.md) case in miniature:

> Even if the ball's trajectory is deterministic, the *pixels* are not… There are infinitely many pixel-level "next frames" that are all consistent with the same physical trajectory. This is the problem of **irrelevant degrees of freedom contaminating the prediction**.

Closing with a comparison this wiki should steal: choosing the right latent is *"the same principle that makes generalized coordinates more powerful than Cartesian coordinates for constrained systems. By choosing the right variables, the constraints become invisible."* In physics finding those variables is the creative act; the claim is that JEPA automates it.

## The three papers it surfaces — two now ingested (2026-09-07)

The essay's real service is citation. All three are LeCun-co-authored statistical physics; two were gaps here and are now filed as [Loss Surfaces](choromanska2015-loss-surfaces-multilayer-networks.md) and [Entropy-SGD](chaudhari2017-entropy-sgd.md), with the concept they anchor at [loss-landscape geometry](../concepts/learning/loss-landscape-geometry.md):

- **Choromanska, Henaff, Mathieu, Ben Arous & LeCun, "The Loss Surfaces of Multilayer Networks" (AISTATS 2015, [arXiv:1412.0233](https://arxiv.org/abs/1412.0233))** — maps a network's loss to the Hamiltonian of a **spherical spin glass**, and argues that for large networks local minima concentrate near the global minimum. This is the missing link between the wiki's [Hopfield/Boltzmann prehistory](dawid-lecun-lvebm-lecture-notes.md) — also spin glasses — and modern training.
- **Chaudhari, Choromanska, Soatto, LeCun et al., "Entropy-SGD" (ICLR 2017, [arXiv:1611.01838](https://arxiv.org/abs/1611.01838))** — Langevin dynamics biasing optimization toward wide valleys by computing a **local entropy**.
- **Mehta & Schwab, "An exact mapping between the Variational Renormalization Group and Deep Learning" ([arXiv:1410.3831](https://arxiv.org/abs/1410.3831), 2014)** — the formal RG↔deep-learning claim the essay's whole analogy leans on.

> [!note] Check the Mehta–Schwab claim before repeating it
> The essay presents this as settled — *"not just a vague analogy"*, *"mathematically grounded."* Verified here: it is **an 8-page arXiv preprint from October 2014 with no journal reference and no DOI recorded on arXiv**, twelve years later. That is not disproof, and the construction may well be correct for the RBM-on-Ising setting it defines. It is a reason not to cite it as established, and the wiki should read the primary before leaning on the RG framing anywhere load-bearing.

## Where it is wrong, and why that matters

> [!warning] The stated collapse mechanism is the popular version, and this wiki has the ablations that contradict it
> The essay's account:
>
> > **JEPA's solution** is the asymmetric architecture with EMA. No negative samples needed. No explicit repulsion. **The collapse is prevented by *architecture*, not by data.**
>
> Three problems, each with a source already in the wiki:
>
> 1. **The EMA is not what prevents collapse.** [BYOL's Table 5b](byol-paper.md): without negatives, the **EMA target alone scores 0.3%** and the predictor alone 0.2%. [SimSiam](simsiam-paper.md) reaches 67.7% with **no EMA at all** — *"it is mainly the stop-gradient operation that plays an essential role."* The load-bearing ingredient is **branch asymmetry**; the EMA is one substitutable way to get it and buys accuracy, not safety. See [the anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md).
> 2. **The blueprint's own answer is not the EMA either.** [Dawid & LeCun](dawid-lecun-lvebm-lecture-notes.md) Fig. 10 prescribes **information-maximization regularizers on both representations** (VICReg as the worked example) plus a capacity limit on the latent variable. No EMA appears in the design.
> 3. **The field has since removed it.** [LeJEPA](lejepa-paper.md) and [LeVJEPA](levjepa-paper.md) train with **no EMA, no stop-gradient, no capacity-limited predictor** — one distributional term, and better results at 5.6–20.8× less compute.
>
> The essay is April 2026 and LeJEPA is November 2025, so this is not merely out of date. It is what the **outside** account of JEPA looks like when the ablations stay inside the papers — and this wiki held roughly the same picture until [three primaries were read in September 2026](../syntheses/world-models/ssl-anti-collapse-lineage.md).

Two smaller slips, both minor: it cites the Dawid–LeCun notes under the subtitle *"A Unifying Perspective"* (the actual subtitle is *"A Path Towards Autonomous Machine Intelligence"*), and it asserts *"this is why JEPA achieves better downstream performance with less compute"* as a settled consequence of the physics argument — [the joint-embedding-vs-reconstruction result](joint-embedding-vs-reconstruction-paper.md) says the comparison has a **crossover**, and which side wins depends on how large the irrelevant features are. The essay's own framing predicts exactly that dependence and it does not draw the conclusion.

## The empirical section, and how far it goes

The last third reports V-JEPA 2 embedding trajectories through action-labelled video — clusters per action, jumps at action boundaries, *"periodic orbits"* for repetitive motions — and reads them as basins and barrier crossings in an energy landscape. The repository backs this with real code: `demos/05` and `06` run `facebook/vjepa2-vitl-fpc64-256` over a 16-frame sliding window (stride 4) on a handful of Something-Something V2 clips, then k-means and t-SNE. Demo 06 is the honest one — **base pretrained model, no SSv2 fine-tuning**, so the cluster structure is not label-derived.

To the author's credit the limits are stated in the text: *"These are observations about the geometry of the learned space, not claims about the training algorithm."* Worth adding anyway — **these are t-SNE projections of ~5 clips**, and t-SNE manufactures visually separated clusters from data that has none. "Basins" and "barrier crossings" are a reading of a 2-D embedding of a 1024-D path, not a measurement of an energy landscape. The underlying finding — that a *pretrained* V-JEPA 2 organizes video temporally without action labels — is real and matches [LeVJEPA](levjepa-paper.md)'s emergent patch structure; the dynamical-systems vocabulary on top of it is interpretation.

## Where to hold it at arm's length

- **Secondary throughout.** No experiments beyond the demos, no numbers, no comparison. Every technical claim traces to a paper that should be read instead.
- **A repository essay, not a publication.** One commit, 0 stars, no review, no citations of it. Its value is framing and bibliography.
- **The collapse account is wrong** (above), which means the mechanism sections should not be quoted.
- **The RG analogy is an analogy** until [Mehta & Schwab](https://arxiv.org/abs/1410.3831) is read and assessed. The essay's strongest structural claim rests on a twelve-year-old unpublished preprint.

## Entities mentioned

- [Yann LeCun](../entities/yann-lecun.md) — the subject throughout. **Katerina Fajmanova** (Prague) — the author; no page.
- [V-JEPA 2](../entities/v-jepa-2.md) — used in the demos (`vjepa2-vitl-fpc64-256`, pretrained and SSv2-finetuned). **I-JEPA** — used for the transfer demonstration.
- [MAE](../entities/mae.md) — the reconstruction foil. [SimCLR](../entities/simclr.md), CLIP — the contrastive foils.

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — as learned coarse-graining; and an outside account of its collapse mechanism that the wiki's primaries contradict.
- [Energy-based models](../concepts/learning/energy-based-models.md) — Gibbs–Boltzmann, partition function, flat-potential collapse.
- [Latent space](../concepts/world-models/latent-space.md) — trajectories, clusters, and the generalized-coordinates framing.
- [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) — the page that settles the disagreement.
- [Representation evaluation](../concepts/learning/representation-evaluation.md) — t-SNE cluster separation as evidence, and its limits.

## Open questions

- **Is the RG mapping real, or a resemblance?** [Mehta & Schwab](https://arxiv.org/abs/1410.3831) is the only formal claim and it never left arXiv. Reading it is a small job with a clear payoff either way, because the wiki repeatedly reaches for "abstraction" language it cannot currently ground.
- **Does the spin-glass loss-surface result say anything about JEPA specifically?** — *Sharpened, not answered, by ingesting it (2026-09-07): the paper presupposes a global minimum worth reaching, and on a joint-embedding loss that minimum is collapse — the widest valley in the landscape. The cheap test is a Hessian spectrum at a converged JEPA solution; see [loss-landscape geometry](../concepts/learning/loss-landscape-geometry.md).* [Choromanska et al. 2015](choromanska2015-loss-surfaces-multilayer-networks.md) concerns supervised networks. Whether joint-embedding objectives — which have a *trivial* global minimum the training must be prevented from reaching — inherit the "local minima concentrate near the global one" picture is not obvious, and would be worth knowing.
- **Would a measured version of the trajectory claim hold?** Cluster purity against action labels, on the pretrained model, over hundreds of clips rather than five, without t-SNE in the loop. The demos are already written; only the scale and the metric are missing.

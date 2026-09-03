---
title: Randall Balestriero
type: entity
subtype: person
created: 2026-07-26
updated: 2026-09-03
sources: 15
tags: [person, balestriero, brown, lejepa, sigreg, jepa, ssl, theory, world-model, inverse-dynamics, causality, spectral-graph-theory, time-series, levjepa, tutorial]
---

**Randall Balestriero** — Assistant Professor at **Brown University**; formerly Meta-FAIR. His lab publishes under the GitHub org **GalilAI-group** (*"Foundation Models, Theory, World Models, Everything AI"*, created 2024-05-25) — the former `rbalestr-lab`, which now redirects there. In this wiki, the **theory-side counterpart to [Yann LeCun](yann-lecun.md) in the JEPA program**: co-first author of [LeJEPA](../sources/lejepa-paper.md), co-author of both May 2026 world-model papers, and the lab behind [stable-worldmodel](stable-worldmodel.md).

## Role in the JEPA program

Where LeCun supplies the architectural agenda, Balestriero supplies the **provability**. The through-line is anti-collapse without heuristics:

- **[LeJEPA](../sources/lejepa-paper.md)** (2025-11, with LeCun; equal contribution) — introduces **SIGReg**, the sketched isotropic Gaussian regularizer that replaces the stop-gradient/EMA/frozen-encoder heuristic stack with one provable term and one hyperparameter.
- **[When Does LeJEPA Learn a World Model?](../sources/when-does-lejepa-learn-a-world-model-paper.md)** (2026-05-25, with Klindt + LeCun) — proves LeJEPA achieves [linear identifiability](../concepts/world-models/identifiability.md), and that the Gaussian is *uniquely* the distribution for which this holds.
- **[stable-worldmodel](../sources/stable-worldmodel-paper.md)** (2026-05-20, 12 authors incl. LeCun) — the benchmark platform, canonical repo in his lab (`rbalestr-lab/stable-worldmodel`).

The pairing is notable: the same author proved the identifiability guarantee *and* co-authored the benchmark showing current models collapse under mild perturbation — published five days apart.

## Beyond the LeCun line (June–July 2026)

Balestriero's collaborations now branch past the LeCun/LeJEPA axis:

- **[SMWM — Sensorimotor World Models](smwm.md)** (2026-06-18, with Petr Ivashkov + **Bernhard Schölkopf**, MPI-IS) — a JEPA world model whose sole anti-collapse mechanism is **inverse dynamics regularization**; explicitly benchmarks against his own **SIGReg**, and connects the JEPA program to **causal representation learning**. Notable that his regularizer is now the *baseline* others improve on.
- **[LeNEPA](lenepa.md)** ([paper](../sources/lenepa-paper.md), 2026-07-01, with Chemeris + Jin) — extends the "Le-" no-augmentation next-latent-prediction family, with **SIGReg**, to **time-series** representation learning.
- **[Spectral Graph Theory: The Mathematics of Self-Supervised Learning](../sources/spectral-graph-theory-ssl-paper.md)** (with [LeCun](yann-lecun.md), IEEE Signal Processing Magazine 43(3):8–20, 2026) — the review formalizing **[SSL as spectral graph learning](../concepts/learning/spectral-theory-of-ssl.md)**; the math spine under the LeJEPA line (paywalled; grounded via its 2022 precursor).
- **[LeVJEPA](levjepa.md)** (arXiv 2608.27395, 2026-08-27; with Kuhn, [Maes](lucas-maes.md), Serra, Le Lidec, [LeCun](yann-lecun.md), Buettner) — SIGReg carried to **video pretraining**, claiming V-JEPA-2-comparable results at **5.6–20.8× less compute**. The first result where the stability pitch pays a *compute* dividend rather than a convenience one.

## The field map he wrote first (2023)

Before LeJEPA there was **[A Cookbook of Self-Supervised Learning](../sources/ssl-cookbook.md)** (arXiv 2304.12210, April 2023) — 71 pages, **Balestriero as first author**, [LeCun](yann-lecun.md) second-to-last, 19 authors including Vlad Sobal ([PLDM](pldm.md)) and Adrien Bardes (VICReg). It is the closest thing this wiki has to a statement of what he thought the field was *before* he proposed replacing its heuristics.

Two things in it sit awkwardly beside the later work, and are recorded rather than reconciled:

- **It reports the field accepting [MAE](mae.md)'s evaluation argument** — *"linear-probing is uncorrelated with fine-tuning and transfer learning performances,"* with the majority of subsequent work moving to fine-tuning. His [Day 3 case against reconstruction](../sources/chicago-booth-world-modeling-workshop-2026-day3.md) is made on probe accuracy. Nothing here bridges 2023 and 2026.
- **It already contains a label-free answer to the question he calls open on Day 3.** *"How can you assess if you learned a good Z without having to reconstruct?"* — the Cookbook recommends **RankMe**, the effective rank of the embedding spectrum, which recovers essentially all of a labelled oracle's hyperparameter-selection quality. See [representation evaluation](../concepts/learning/representation-evaluation.md).

## Teaching it — the Day 3 tutorial (2026-09-02)

His 90-minute [*How to Train JEPA World Models Without Headache*](../sources/chicago-booth-world-modeling-workshop-2026-day3.md) is the wiki's only source where he explains the line in his own words rather than in a paper's. Four things it adds:

- **The reconstruction critique, done properly.** Two autoencoders with identical MSE on train *and* test whose embeddings differ by **~20 points** of ImageNet accuracy — so the reconstruction loss carries no information about representation quality. Then *why*: MSE gradients follow the top eigenvectors of the pixel covariance, so training learns the **low-frequency half first** (colour, coarse contour) and the useful high-frequency half last. Applied to [Dreamer v4](dreamer.md) by name.
- **A debugging rule.** *"Always plug a detached online decoder and see what it reconstructs"* — post-hoc, gradient-detached, purely diagnostic; it distinguishes a collapsed latent from one that did not collapse enough.
- **A research-methodology warning.** Never use planning success as your research signal — the ladder is **decoded frames → probe `Z` for known properties → only then planning**.
- **Prediction loss as graph specification.** Solve a supervised least-squares problem in closed form for the linear probe, substitute back, and the labels `Y` vanish into an `N×N` pairwise-relation matrix. Designing a prediction loss *is* designing a graph over samples — see [spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md).

He is also unusually direct about the state of the art he is selling: *"we are not yet at the stage like supervised cross-entropy-based training where you can just plug anything and Adam will do all the heavy lifting."*

## Related
- [Yann LeCun](yann-lecun.md) — frequent co-author across the LeJEPA line.
- [Lucas Maes](lucas-maes.md) — [LeWorldModel](leworldmodel.md) + stable-worldmodel lead author.
- [David Klindt](david-klindt.md) — identifiability paper lead author.
- [SMWM](smwm.md) — his inverse-dynamics world model with Schölkopf (Brown × MPI-IS).
- [LeNEPA](lenepa.md) — the "Le-" family extended to time series.
- [Spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md) — the SSL-as-spectral-embedding line his work rests on.
- [Identifiability](../concepts/world-models/identifiability.md) / [JEPA](../concepts/world-models/jepa.md).

## Mentioned in
- [galilai-group/tutorial](../sources/wm-booth-lejepa-lewm-tutorial-repo.md) — sole committer; a 897-line LeJEPA + LeWM tutorial pushed hours before the workshop's Day 3 coding session.
- [galilai-group/lejepa](../sources/lejepa-github.md) — the reference implementation, and the normality-test library SIGReg is one configuration of.
- [galilai-group/stable-worldmodel](../sources/stable-worldmodel-github.md) — the platform repo as of 2026-09.
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — organizer; co-author on two lightning talks presented (VISReg, [MarketOne](marketone.md)); asks the panel what the "ImageNet of finance" would have to be.
- [Third World Modeling Workshop, Chicago Booth 2026](../sources/chicago-booth-world-modeling-workshop-2026.md) — **organizer and panel moderator**; the third edition after the Flatiron Institute and Montréal, pointed this time at non-stationary signals, time series and finance.
- [LeJEPA Paper](../sources/lejepa-paper.md) — co-first author.
- [When Does LeJEPA Learn a World Model?](../sources/when-does-lejepa-learn-a-world-model-paper.md) — co-author.
- [stable-worldmodel paper](../sources/stable-worldmodel-paper.md) — co-author.
- [Sensorimotor World Models paper (Ivashkov, Balestriero, Schölkopf 2026)](../sources/sensorimotor-world-models-paper.md) — co-author; inverse-dynamics anti-collapse.
- [LeNEPA paper (Chemeris, Jin, Balestriero 2026)](../sources/lenepa-paper.md) — co-author; SIGReg for time-series SSL.
- [Spectral Graph Theory review (Balestriero & LeCun, IEEE SPM 2026)](../sources/spectral-graph-theory-ssl-paper.md) — co-author; SSL as spectral graph learning.
- [A Cookbook of Self-Supervised Learning](../sources/ssl-cookbook.md) — **first author**; the field's taxonomy, the projector, dimensional collapse, RankMe.
- [LeWorldModel](leworldmodel.md) — SIGReg, his regularizer, is LeWM's single loss term beyond prediction.
- [Third World Modeling Workshop — Day 3](../sources/chicago-booth-world-modeling-workshop-2026-day3.md) — **organizer, and the 90-minute tutorial teaching the whole line from his own code**; announces [LeVJEPA](levjepa.md), names the multimodal/noise/stochasticity limitations, and hands out the two exercises the hackathon ran on.

---
title: Randall Balestriero
type: entity
subtype: person
created: 2026-07-26
updated: 2026-09-11
sources: 20
tags: [person, balestriero, brown, citadel, wavelets, spline-theory, signal-processing, nasa-mars-seis, lejepa, sigreg, jepa, ssl, theory, world-model, inverse-dynamics, causality, spectral-graph-theory, time-series, levjepa, tutorial]
---

**Randall Balestriero** — Assistant Professor at **Brown University** (joined Brown CS August 2024; courses listed for Fall 2026 and Spring 2027, verified 2026-09-07), Visiting Researcher at **Meta FAIR**, and — per [his own site](../sources/randall-balestriero-personal-site.md) — **Quantitative Researcher at GQS, Citadel** since 2023. His lab publishes under the GitHub org **GalilAI-group** (*"Foundation Models, Theory, World Models, Everything AI"*, created 2024-05-25) — the former `rbalestr-lab`, which now redirects there. In this wiki, the **theory-side counterpart to [Yann LeCun](yann-lecun.md) in the JEPA program**: co-first author of [LeJEPA](../sources/lejepa-paper.md), co-author of both May 2026 world-model papers, and the lab behind [stable-worldmodel](stable-worldmodel.md).

> [!warning] This wiki had two of his six research areas
> [His personal site](../sources/randall-balestriero-personal-site.md) organizes the work into six: world models, SSL, **time-series & learnable signal processing**, **spline geometry of deep nets**, **safe/fair/regulator-ready AI**, and real-world deployment. Everything below — fifteen sources deep — is the first two.
>
> **The one that reframes the rest is the oldest.** His timeline dates *learnable parametrized wavelets → deep wavelet transforms* to **2013–2016**, *before* the PhD, and the deployment is **NASA's Mars SEIS mission for marsquake detection** (*Nature Communications* 2020). So **non-stationary time-series is the trunk and the world-model work is a branch** — which makes the [Chicago Booth workshop](../sources/chicago-booth-world-modeling-workshop-2026.md)'s turn toward finance and time-series look like a return rather than a pivot, and makes his *"hardest real-world time-series domain"* framing of finance a claim from inside the specialty.
>
> The second missing area is the **spline / continuous-piecewise-affine** view from the Rice PhD with **Richard Baraniuk** — the machinery behind *Deep Networks Always Grok*, and the reason his interpretability instincts run through **linear regions** rather than features or circuits. This wiki cites results downstream of that frame without naming it.
>
> Also uningested and listed there: **Semantic Tube Prediction** (JEPA for language), **Curvature Tuning**, **MaGNET**, *Learning in High Dimension Always Amounts to Extrapolation*, and the *Build Specialist LLMs Like It's 2019* claim that 7B models trained from scratch on small task-specific corpora match pretrained baselines.

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
- **The theoretical basis for the Day 3 argument exists, and is now ingested.** [Joint-Embedding vs Reconstruction](../sources/joint-embedding-vs-reconstruction-paper.md) (NeurIPS 2025, senior author, with Van Assel, Ibrahim, Biancalani and Regev of Genentech) derives **closed-form solutions for both paradigms under linear models** and names the deciding variable: **the magnitude of the irrelevant features**. High → joint-embedding, because it imposes a *strictly weaker* augmentation-alignment condition; **low → reconstruction**, because the important components already carry the variance. So his Day 3 case against reconstruction is the **high-noise half of a crossover**, not a general verdict — and the wiki now has the condition rather than the conclusion.
- **It already contains a label-free answer to the question he calls open on Day 3.** *"How can you assess if you learned a good Z without having to reconstruct?"* — the Cookbook recommends **RankMe**, the effective rank of the embedding spectrum, which recovers essentially all of a labelled oracle's hyperparameter-selection quality. See [representation evaluation](../concepts/learning/representation-evaluation.md).

## The month before LeJEPA (2025-10-28)

[An 78-minute podcast](../sources/information-bottleneck-ep11-jepa-balestriero.md) recorded weeks before [LeJEPA](../sources/lejepa-paper.md) shipped, and he pre-announces it without naming it: on how the field prevents collapse, *"there is not yet agreed upon method. **Maybe there will be soon once we release our version.**"* Four things it adds that the papers do not:

- **The expertise goes into the prediction task, not the anti-collapse term** — *"in general you need a lot of expertise to design the prediction task itself."* And the [WAM](../concepts/world-models/world-action-model.md) justification in one sentence: if the video is of a robot, *"you have actions of what the robot is doing, you can include that as part of the prediction task to **help the system navigate the uncertainty of the future prediction task**"* — actions as uncertainty reducers in the loss, not as an output.
- **Collapse is a continuum that supervised learning has too.** Reconstruction cannot collapse *"because you need to keep all the information to reconstruct all the pixels"*; supervised cannot *"because you need to at least discriminate the classes"* — and **the class count is itself the collapse control**: ImageNet-1k features generalize better zero-shot than ImageNet-10's *"because you have much finer-grain classes and so less collapsed features."* Which reframes [the anti-collapse lineage](../sources/../syntheses/world-models/ssl-anti-collapse-lineage.md) as *what replaces the class count when there are no classes?*
- **Where SSL breaks**, said plainly: methods are designed for *"clean, balanced"* data, and under noise or *"rare events, distribution of the underlying cluster that is very heavy-tail"* they *"disregard some of the useful features just to capture noise features."* The conversational form of his own [JE-vs-Reconstruction](../sources/joint-embedding-vs-reconstruction-paper.md) result — and a description of **robot demonstration data**, which nobody has tested.
- **Codebase size as a moat.** DINOv3 at *"like 20,000 lines"* against SimCLR's *"300 lines"*: *"we have to be careful about not over-engineering things too early, because then it means everyone else is left behind. **So it gives you a competitive advantage — but is it your goal?**"* This wiki had read LeJEPA's simplicity as a stability claim; here it is an accessibility argument.

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
- [Joint-Embedding vs Reconstruction](../sources/joint-embedding-vs-reconstruction-paper.md) — senior author; the closed-form condition under the whole JEPA-vs-reconstruction argument, and the regime where reconstruction wins.
- [The Information Bottleneck EP11 — JEPA](../sources/information-bottleneck-ep11-jepa-balestriero.md) — the position one month before LeJEPA, including the pre-announcement, the class-count-controls-collapse framing, and the codebase-as-moat argument.
- [Personal site (randallbalestriero.github.io)](../sources/randall-balestriero-personal-site.md) — his own six-area map of the work; the Citadel role; NASA Mars SEIS and the wavelet line; and the uningested papers above. **Note it mentions no academic position at all** — a self-presentation artifact, not a factual record, and never the source for what he does.
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
- [The Birth of SSL — A Supervised Theory](../sources/birth-of-ssl-supervised-theory-paper.md) — with LeCun, NeurIPS 2024 SSL Workshop: SSL and supervised learning share a loss and differ in the label graph; VICReg recovered from a ridge-regularized supervised head.

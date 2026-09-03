---
title: Randall Balestriero
type: entity
subtype: person
created: 2026-07-26
updated: 2026-09-02
sources: 13
tags: [person, balestriero, brown, lejepa, sigreg, jepa, ssl, theory, world-model, inverse-dynamics, causality, spectral-graph-theory, time-series]
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
- [LeWorldModel](leworldmodel.md) — SIGReg, his regularizer, is LeWM's single loss term beyond prediction.

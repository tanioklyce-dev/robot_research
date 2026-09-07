---
title: "Randall Balestriero — personal site (randallbalestriero.github.io)"
type: source
url: https://randallbalestriero.github.io/
local_path: raw/2026-09-07-randall-balestriero-personal-site.md
sha256: 57d8f3ac41b2f3888e218c820aa97ebaee5b200c94141919a4d23a4bcaf151e4
author: "Randall Balestriero"
published: 2026-09-07
venue: "Personal website (GitHub Pages), captured 2026-09-07; no publication date on the page — content is dated by its own timeline entries"
format: personal/professional website (static text captured; the live BibBase publication index is JS-loaded and not captured)
tags: [randall-balestriero, jepa, ssl, world-models, time-series, wavelets, spline-theory, nasa-mars-seis, citadel, brown, biography, index]
ingested: 2026-09-07
---

## Summary

**The self-portrait of the author this wiki cites most on the theory side, and it turns out the wiki has been reading one third of him.** Balestriero's personal site organizes his work into **six** areas; the wiki's coverage — fifteen sources deep — sits almost entirely in two of them (world models, SSL). The other four are absent from this wiki entirely, and one of them predates and explains the rest.

Its value here is as an **index that reveals gaps**, not as research. The single most consequential line on the page is a paper title the wiki has never mentioned while spending a week arguing about exactly what it claims to settle in closed form.

Positioning line, in his words: *"Toward world models that are provably safe, sample-efficient, and ready for the real world."*

## The gap this exposes

> [!warning] A NeurIPS 2025 paper answers the wiki's central open dispute, and the wiki has zero mentions of it
> **"Joint-Embedding vs Reconstruction: Provable Benefits of Latent Space Prediction for SSL"** (NeurIPS 2025), described on the site as:
>
> > **Closed-form analysis of when JEPA wins over reconstruction: latent prediction is strictly preferred when irrelevant features dominate the input signal.**
>
> That is a *stated condition* on the reconstruction-vs-latent-prediction question the wiki has been circling from four directions: the [generative-video vs JEPA](../syntheses/world-models/generative-video-vs-jepa-world-models.md) comparison, the [anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md), [MAE's rejection of linear probing](mae-paper.md), and Balestriero's own [Day 3 case against reconstruction](chicago-booth-world-modeling-workshop-2026-day3.md) — which this wiki recorded as *argued on probe accuracy* with the theoretical basis unstated. **The basis exists and has a citation count.** Not ingested; now top of the backlog.
>
> It also bears directly on today's third position: [Self-Flow](flux-3-launch.md) claims generation and representation quality improve *together* if you fix the objective. "Latent prediction wins when irrelevant features dominate" is a claim about **when that stops being true**, and the two should be read against each other.

Five more items on the page that the wiki has never mentioned:

| Work | Claim as stated on the site |
|---|---|
| **Semantic Tube Prediction: Beating LLM Data Efficiency with JEPA** (arXiv 2026, with Huang and LeCun) | **JEPA extended to language** — constrains hidden trajectories to a tube around the geodesic, *"drastically reducing the data needed to fine-tune LLMs"* |
| **Curvature Tuning** (NeurIPS 2025) | *"One scalar that shifts a trained network's decision boundary — **no retraining, no backprop**."* Chosen by cross-validation alone |
| **Deep Networks Always Grok and Here Is Why** (2024, with Humayun & Baraniuk) | Grokking happens *everywhere*, including CIFAR-10 and ImageNette, driven by **a phase transition in the network's linear regions** |
| **MaGNET** | Removing dataset biases from **trained** generative networks **without retraining** — filed under *"Safe, Fair & Regulator-Ready AI"* |
| **Build Specialist LLMs Like It's 2019** (MLST 2025) | *"7B-parameter LLMs can match pretrained baselines when trained from scratch on small task-specific corpora"* |

The last one is the most disruptive if it holds, and the wiki has nothing on it.

## The two research areas the wiki has no page for

**1. Learnable signal processing — and it is the *oldest* thread, not a recent turn.** The timeline dates it **2013–2016**, before the PhD: *"early work on learnable parametrized wavelets, later extended to deep wavelet transforms."* The deployment is the striking part:

> **Deployed in NASA's Mars SEIS mission for marsquake detection.**

Anchored by *Clustering Earthquake Signals and Background Noise in Continuous Seismic Data with Unsupervised Deep Learning* (**Nature Communications 2020**, 266 citations on the site's counter).

> [!note] This reframes something the wiki got slightly wrong by omission
> The wiki treats his interest in **time-series and finance** as context for the [Chicago Booth workshop](chicago-booth-world-modeling-workshop-2026.md) he organized — a JEPA researcher pointing the third edition at non-stationary signals. On this evidence it is the reverse: **learnable signal processing for non-stationary time-series is his founding area**, running from 2013 through the Nature Comms paper, [LeNEPA](../entities/lenepa.md), and now Citadel. The world-model work is the branch, not the trunk.
>
> Which makes his framing of finance as *"the hardest real-world time-series domain"* a claim from inside the specialty rather than an outsider's analogy — and it makes the wiki's [financial time-series augmentations](../concepts/economics/financial-time-series-augmentations.md) material part of a longer line than it looks.

**2. Spline geometry of deep networks.** From the Rice PhD with **Richard Baraniuk**: *"reading deep networks as continuous piecewise-affine spline operators — turning geometry into practical wins on batch-norm, generative networks, inversion."* It is the machinery behind *Deep Networks Always Grok*, and it is the reason his [interpretability instincts](../concepts/safety/mechanistic-interpretability.md) run through *linear regions* rather than through features or circuits. The wiki has no page for it and cites the results downstream of it without the frame.

Also listed and uningested: **"Learning in High Dimension Always Amounts to Extrapolation"** (2021, with Pesenti and LeCun, 185 citations) — *"why everything we call 'interpolation' in modern deep learning is actually extrapolation."*

## The biographical record, and one discrepancy worth stating carefully

The site's timeline:

| | |
|---|---|
| **2013 — 2016** | Learnable signal processing; parametrized wavelets → deep wavelet transforms → NASA Mars SEIS |
| **2016 — 2021** | PhD, **Rice University** (with **Richard Baraniuk**) — the affine-spline view of deep nets |
| **2021 — 2023** | Postdoctoral Researcher, **Meta AI / FAIR** (with **Yann LeCun**) — SSL, augmentation biases, the ICML 2023 tutorial, the [SSL Cookbook](ssl-cookbook.md) |
| **2023 — present** | **Quantitative Researcher · GQS, Citadel** |
| **2024 — present** | Three appearances on **Machine Learning Street Talk** |

Header summary: *"A decade of research (Rice · Meta FAIR · Citadel)."*

> [!warning] The site does not mention Brown University anywhere
> This wiki's [entity page](../entities/randall-balestriero.md) opens *"Assistant Professor at **Brown University**."* **That is correct and current** — verified 2026-09-07 against Brown CS's own faculty listing and news item (joined Brown CS as assistant professor, August 2024), with courses listed for **Fall 2026** and **Spring 2027**. He is also described elsewhere as a **Visiting Researcher at Meta FAIR**.
>
> His personal site lists **no academic position, no teaching, and no mention of Brown**, and gives Citadel as the current role. Both facts are simply true at once; academic and industry affiliations routinely coexist, and a personal site is a **self-presentation artifact rather than a factual record**.
>
> The reason to write it down is provenance discipline: **this page's omissions do not license an inference about his affiliations, and it should never be cited as the source for what he does.** The wiki's Brown claim stands, now with a primary behind it. Recorded, not resolved into a narrative.

The page closes: *"Open to research collaborations & opportunities. Interested in world models, SSL, or theory of deep learning — or hiring? I'd love to hear from you,"* alongside a prominent **Download CV**. Stated as observed; the wiki draws no conclusion from it.

## What it confirms

- **The JEPA line as he presents it publicly** matches what the wiki has: JEPA, energy-based world models, *"provably sample-efficient and safe."* Selected work lists [PLDM / *Learning from Reward-Free Offline Data*](pldm-paper.md) (NeurIPS 2025), **LeWorldModel** (*"the first JEPA that trains stably end-to-end from raw pixels — collapsing six tunable loss terms down to one"*), and **Hierarchical Planning with Latent World Models** (*"70% pick-and-place success vs 0% for single-scale baselines"* — the wiki holds the PDF in `raw/`, uningested).
- **The Cookbook is presented as a headline artifact** (705 citations on the site's counter), consistent with the wiki's reading of it as his statement of the field before he proposed replacing its heuristics.
- **The self-description is theory-first and deployment-facing**: *"first-principles theory,"* *"provably safe,"* and application domains listed as *"vision, NLP, geophysics, bioacoustics, medical signals, and quantitative finance"* — robotics is conspicuously **not** on that list, which is a useful check on how central robot control is to his own account of the programme.

## Entities mentioned

- [Randall Balestriero](../entities/randall-balestriero.md) — the subject; page updated from this.
- [Yann LeCun](../entities/yann-lecun.md) — postdoc advisor and recurring co-author. **Richard Baraniuk** (Rice) — PhD advisor; no page.
- **Citadel / GQS** — no page; the wiki has no entity for it.
- [PLDM](../entities/pldm.md) · [LeWorldModel](../entities/leworldmodel.md) · [LeNEPA](../entities/lenepa.md) — his systems the wiki already covers.

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) · [spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md) · [representation evaluation](../concepts/learning/representation-evaluation.md) — the covered third.
- [Financial time-series augmentations](../concepts/economics/financial-time-series-augmentations.md) — recontextualized as part of a line beginning in 2013, not a recent turn.
- [Mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md) — the spline/linear-region frame the wiki cites downstream of without naming.

## Open questions

- **What exactly does *Joint-Embedding vs Reconstruction* prove?** *"Latent prediction is strictly preferred when irrelevant features dominate the input signal"* is a condition, and conditions have converses. **Read it.** It is the closest thing to a settlement of the wiki's longest-running dispute, and it is a NeurIPS paper the wiki has never mentioned.
- **Does the specialist-LLM claim replicate?** *7B from scratch on a small task-specific corpus matching pretrained baselines* contradicts the default assumption behind every foundation-model page here. Currently a talk title.
- **Is there anything in the wavelet line for robot sensing?** Learnable parametrized wavelets on noisy non-stationary signals is not obviously distant from cheap robot sensors — and the wiki's [contact-rich](../concepts/robotics/contact-rich-manipulation.md) thread keeps running into force and tactile streams nobody knows how to represent well.
- **A caution for the wiki's own method.** Fifteen ingested sources on one researcher, and the site says the wiki had two of his six areas and missed the one he started with. **A personal site is a cheap, high-yield thing to read early for any figure this wiki cites repeatedly** — and it has been read late here.

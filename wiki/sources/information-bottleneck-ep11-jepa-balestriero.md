---
title: "The Information Bottleneck EP11 — JEPA with Randall Balestriero (Oct 2025)"
type: source
url: https://www.youtube.com/watch?v=4at0EpnYiWY
local_path: raw/2025-10-28-information-bottleneck-ep11-jepa-balestriero-transcript.txt
sha256: b04863364f899de28501318746273ac5897e668c416d3ed7332f57377bc927d6
author: "Hosts: Ravid and Alan (surnames not stated on air). Guest: Randall Balestriero (Brown University)"
published: 2025-10-28
venue: "The Information Bottleneck podcast, episode 11, 78:04 (transcript from YouTube en-orig auto-captions)"
format: podcast interview (auto-caption transcript, ~14,400 words)
tags: [balestriero, jepa, ssl, anti-collapse, world-models, latent-variables, lejepa, sigreg, dinov3, vicreg, teacher-student, planning, tooling]
ingested: 2026-09-07
---

## Summary

**Balestriero explaining the whole JEPA programme in his own words, one month before LeJEPA — and pre-announcing it without naming it.** A 78-minute conversation recorded **2025-10-28**; [LeJEPA](lejepa-paper.md) lands in **November 2025**. Asked how the field prevents representation collapse, he lists the competing families and then says:

> This is where it's a bit more diverse and there is not yet agreed upon method. **Maybe there will be soon once we release our version**, but it's still very exploratory at this stage.

That dating is what makes the source useful. Everything else on the [Balestriero](../entities/randall-balestriero.md) page is either a paper or the [Day 3 tutorial](chicago-booth-world-modeling-workshop-2026-day3.md) from ten months *later*. This is the position immediately before the thing that reorganized it, delivered conversationally to two non-specialist hosts.

> [!note] Transcript and attribution
> YouTube auto-captions, which garble heavily — "Japa"/"JPEG a"/"Jetpak" for JEPA, "V Craig" for VICReg, "Dynino" for DINOv3, "Yan Lun" for Yann LeCun. The correction key is in the `raw/` header. **The hosts give only first names on air, "Ravid" and "Alan."** The channel name alludes to the Information Bottleneck line, which invites an obvious inference about the first host's identity; **that inference is not made here** — no surname is stated in the source.

## What it adds that the papers do not

**1. The expertise goes into the prediction task, not the anti-collapse term.** The framing the papers bury:

> The prediction task itself is quite natural to design… it's about figuring out what you want to predict that should have roughly the same semantic within them… **In general you need a lot of expertise to design the prediction task itself.**

And the worked example of JEPA-on-video contains the [world-action model](../concepts/world-models/world-action-model.md) justification in one sentence:

> If you have access to side information like maybe it was a video of a robot and **you have actions of what the robot is doing, you can include that as part of the prediction task to help the system navigate the uncertainty of the future prediction task.**

Actions as **uncertainty reducers in the loss**, not as an output. That is a cleaner statement of why action-conditioning helps than anything else in this wiki.

**2. Why reconstruction and supervision cannot collapse — and a mechanism the wiki did not have.**

> When you reconstruct, **you cannot collapse because you need to keep all the information to reconstruct all the pixels.** Similarly, when you do supervised learning, you cannot collapse because you need to at least discriminate the classes.

Then the part worth keeping: **class count is itself a collapse control.**

> In supervised learning the number of classes is sort of a way to control the collapse of the embedding. That's why if you do supervised learning on ImageNet-10 versus ImageNet-1k, **the ImageNet-1k one will generalize much more zero-shot** on different tasks, because you have much finer-grain classes and so **less collapsed features**.

The [anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) treats collapse as an SSL-specific pathology with four devices against it. This says collapse is a **continuum present in supervised learning too**, and label granularity is where it is set — which reframes the whole page as *"what replaces the class count when there are no classes?"*

**3. Where SSL breaks, stated plainly.**

> A lot of those methods have been designed in a **clean dataset, balanced dataset** setup. So if you start having noise in your data, or you have **rare events, distribution of the underlying cluster that is very heavy-tail** — this is something where those methods out of the box will **disregard some of the useful features just to capture noise features.**

That is the conversational form of his own [Joint-Embedding vs Reconstruction](joint-embedding-vs-reconstruction-paper.md) result (NeurIPS 2025, arXiv five months earlier), and of the [Cookbook](ssl-cookbook.md)'s **uniform prior** problem, which the wiki flagged as *never tested on robot data*. **Robot demonstration data is noisy, imbalanced and heavy-tailed** — mostly approach and idle, with the decisive events rare. Two of his own results and one plain-language warning all point at the same untested case.

**4. Latent variables: when LeCun's Z is actually needed.** Asked whether a JEPA needs the hidden variable:

> If you already have **very rich actions**, you don't have a lot of uncertainty, then probably you are good enough to not use a latent variable… If you have **very weak actions or no actions** and you have many possible futures from the same past, you need something to account for those — because otherwise, if you just do mean-squared-error prediction, **you'll just learn to predict the average of all those possible scenarios.**

And the question underneath it, which he leaves open:

> Fundamentally this goes back to the question of **what are good actions**. If action is everything you need to describe the next frame from the past, it means you need to almost have knowledge of the world… so you want a **very constrained latent variable** that lives in a very small space, and **how to control this capacity is also a big research question.**

**5. The evaluation criterion is navigability, not accuracy.** On world modelling as the new JEPA benchmark:

> Capturing all the features of the input even in a compressed way is nice, but ideally **you want it to be easy to navigate with gradient-based planning**.

That is a different success criterion from anything on the [representation evaluation](../concepts/learning/representation-evaluation.md) page, and it names [gradient-based planning](../concepts/world-models/gradient-based-planning.md) as the thing the representation is *for*.

## The one that is an argument, not a fact

> [!note] Codebase size as a competitive moat
> > Looking at the number of lines — I'm going to use **DINOv3** as an example because I computed it — I think the latest version is like **20,000 lines** in the GitHub repo, which means if you want to get into JEPA research, you need to manage this gigantic codebase… If you think about **SimCLR** a few years ago, the main file was just **300 lines**.
> >
> > It's something I think as a community we have to be careful about: **not over-engineering things too early, because then it means everyone else is left behind. So it gives you a competitive advantage — but is it your goal?**
>
> This wiki has read LeJEPA's "one loss, one hyperparameter" as a **technical** claim about stability. Here the same simplicity is argued as an **accessibility and concentration** claim: complex training recipes are a moat, and moats in an open research field are a choice someone made. Worth carrying next to the [MoCo v3](moco-v3-paper.md) finding that instability degrades results invisibly — both are arguments that the field's tooling hides things.

He is also blunt about the incumbent methods on their own terms: teacher-student approaches (DINO, V-JEPA) *"perform very very well"* but are *"not really understood mathematically"* and *"very finicky to train — if you don't have the right teacher-student schedule it will collapse,"* with loss curves *"pretty hard to interpret."*

## Smaller things worth recording

- **Tooling, as of Oct 2025**: `stable-pretraining` (SSL utilities) and **`stable-world-models`** for world-model evaluation — the latter is the wiki's [stable-worldmodel](../entities/stable-worldmodel.md), here described as an evaluation library rather than a benchmark. Plus *"very soon… a very simple one we will release"* — LeJEPA again.
- **Multimodality**: JEPAs are *"right now mostly single modality"*; he expects the recipe to be modality-agnostic and multi-modal JEPAs *"in less than two years"*, listing robotics, self-driving, satellite, weather and financial data as sources. The hard part he names is **fusion** (early vs late), *"a big research question even in just supervised learning"* — not the JEPA objective.
- **JEPA can be supervised** if you want — use labels to define positive pairs, as in supervised contrastive learning — *"but this is not really something that you want to do."*
- The first ~25 minutes are **news discussion, not JEPA**: recursive language models, agentic RAG, context rot, and an AGI-definition argument in which he says benchmark-based measurement *"does not inform anyone about AGI progress at all"* because labs *"pay a lot of people to generate new expert data… and then they use this to fake the generalization capability."* His preferred criterion is **real-world deployment** where you cannot pre-collect the test distribution — which is the same instinct as the wiki's [policy-evaluation](../concepts/robotics/robot-policy-evaluation.md) page, arrived at from the language side.

## Where to hold it at arm's length

- **Auto-captioned podcast, no slides, no numbers.** Nothing here is a measurement. The value is framing and dating.
- **Conversational precision.** Claims like the ImageNet-10 vs ImageNet-1k collapse argument are stated without citation; they are plausible and consistent with the literature, and they are podcast statements.
- **It predates almost everything the wiki holds on him.** LeJEPA, the identifiability proof, stable-worldmodel's results, LeVJEPA and the Booth tutorial all come after. Read it as the **before** picture, and expect specific claims to have been superseded.

## Entities mentioned

- [Randall Balestriero](../entities/randall-balestriero.md) — the guest. [Yann LeCun](../entities/yann-lecun.md) — discussed, not present.
- [DINO](../entities/dino.md) / DINOv3 · [V-JEPA 2](../entities/v-jepa-2.md) · VICReg · [SimCLR](../entities/simclr.md) — the methods compared.
- [stable-worldmodel](../entities/stable-worldmodel.md) — named on air as an evaluation library.

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) · [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) — the taxonomy, plus collapse as a supervised-learning continuum.
- [World-action model](../concepts/world-models/world-action-model.md) — actions as uncertainty reducers in the prediction task.
- [Gradient-based planning](../concepts/world-models/gradient-based-planning.md) — named as what the representation is *for*.
- [Representation evaluation](../concepts/learning/representation-evaluation.md) — navigability as the criterion.
- [Contrastive learning](../concepts/learning/contrastive-learning.md) — triplet → minibatch negatives → softmax, as one anti-collapse family among three.

## Open questions

- **What replaces the class count?** If label granularity is the collapse control in supervised learning, and SSL removes labels, then every anti-collapse device is a substitute for a knob that used to come free with the dataset. That is a cleaner framing of [the lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) than the one it currently has, and no source here states it.
- **Does the heavy-tail failure mode actually bite on robot data?** He names noise and rare heavy-tailed events as where SSL *"disregards useful features to capture noise features."* Robot demonstration data is exactly that shape. **Still untested**, now flagged by three independent statements from the same author.
- **How constrained does the latent have to be?** *"How to control this capacity is a big research question"* — and it is the question standing between a JEPA and a stochastic world model.
- **Is the 20,000-line critique still true?** DINOv3's repo size was his October 2025 count. If LeJEPA and [LeVJEPA](levjepa-paper.md) reduce it by an order of magnitude in practice — not just in the loss function — that is a measurable claim and the wiki has not measured it.

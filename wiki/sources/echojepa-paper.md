---
title: "EchoJEPA: A Latent Predictive Foundation Model for Echocardiography (Munim, Fallahpour, Szasz et al., Feb 2026)"
type: source
url: https://arxiv.org/abs/2602.02603
local_path: raw/2602.02603v1.pdf
sha256: de6eab93071969350f725501299bff3c5c5c606c88d60b6ea876d05447910ac7
author: "Alif Munim*, Adibvafa Fallahpour*, Teodora Szasz*, Ahmadreza Attarpour, River Jiang, Brana Sooriyakanthan, Maala Sooriyakanthan, Heather Whitney, Jeremy Slivnick, Barry Rubin, Wendy Tsang, Bo Wang"
affiliation: University Health Network; Vector Institute; University of Toronto; Cohere Labs; Arc Institute; University of Chicago; Philips Health; UCSF
venue: "arXiv 2602.02603 (preprint, 2026-02-04)"
published: 2026-02-04
ingested: 2026-08-30
tags: [jepa, v-jepa-2, echocardiography, medical-imaging, foundation-model, latent-prediction, robustness, perturbation, label-efficiency, bo-wang, vector-institute]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/2602.02603v1.pdf`, 19 pages). Sections 1–4 read in full (motivation, related work, architecture, robustness protocol, experiments); appendices skimmed. Surfaced via [Goodfire's Silico case study](goodfire-silico-robotics-vision.md), then ingested on its own merits — it is a substantial [JEPA](../concepts/world-models/jepa.md) result the wiki did not know existed.

## Summary

**EchoJEPA** — Bo Wang's lab (University Health Network / Vector / Toronto) with collaborators at Chicago, Philips and UCSF. **The largest [JEPA](../concepts/world-models/jepa.md)-family model in this wiki outside natural video, and the clinical branch of the family the wiki's JEPA page did not know about.** Trained on **18 million echocardiograms across 300K patients** — "the largest pretraining corpus for this modality to date" — by adapting **[V-JEPA 2](../entities/v-jepa-2.md)** with domain-appropriate temporal resolution and augmentation.

The argument is the most direct statement in this wiki of **why predicting in latent space beats reconstructing pixels**, and it is a domain argument rather than an efficiency one:

> "Ultrasound video is dominated by stochastic speckle patterns, depth-dependent intensity attenuation, and acoustic shadows, artifacts that vary across acquisitions and bear no relationship to cardiac anatomy."

> "By targeting the output of an exponential moving average teacher rather than raw pixels, the model downweights unpredictable artifacts like stochastic speckle while reinforcing temporally coherent structures like chamber geometry and wall motion."

And the sharp version, on why the competing paradigms fail: *"supervised models inherit annotation noise, contrastive models align to report language rather than anatomy, and **reconstruction models must faithfully reproduce speckle to minimize their loss**."*

> [!note] This is the JEPA thesis, tested where it should win most
> [LeCun's](../entities/yann-lecun.md) case for [JEPA](../concepts/world-models/jepa.md) is that pixel reconstruction wastes capacity on unpredictable detail, and that prediction should happen in a representation space where the unpredictable parts have been discarded. Ultrasound is close to the ideal test: a modality where a large fraction of the pixels are **physically meaningless noise** and where that fraction is known a priori rather than argued.
>
> The wiki's [generative-video-vs-JEPA](../syntheses/world-models/generative-video-vs-jepa-world-models.md) synthesis has been arguing this on natural video, where "unpredictable detail" is contestable. Here it is speckle, and the result is unusually clean.

## Headline results

| Claim | Number |
|---|---|
| LVEF estimation error | **−19%** vs prior methods |
| View classification | **87.4%** accuracy (12-class) |
| **Label efficiency** | **78.6%** with **1% of labels**, vs **42.1%** for the best baseline on **100%** |
| **Robustness** to acoustic perturbation | degrades **2.3%** vs **16.8%** for next best; **40% less** than reconstruction baselines like VideoMAE |
| Zero-shot adult → pediatric | **15% lower error** than next best, **beating all fine-tuned baselines** |

The label-efficiency line is the one to remember: **1% of labels beating the best baseline at 100%** is close to two orders of magnitude of annotation saved, which is the whole practical case for foundation models in a domain where labels require a cardiologist.

## The robustness protocol — the most transferable part

§3.5 is the section a robotics reader should take, and it is a better-designed version of what this wiki keeps asking for.

Their framing:

> "Standard evaluation protocols emphasize i.i.d. test performance on held-out splits from the training distribution, underestimating failure modes in clinical deployment where distribution shift is the norm."

And the observation that makes it bite:

> "Patients most likely to benefit from automated analysis, such as those with obesity or limited acoustic windows, are precisely those whose images deviate most from training distributions."

They then reject generic corruption benchmarks — ImageNet-C, adversarial perturbations — as "neither capturing ultrasound-specific degradation," and build **physics-informed perturbations** instead:

- **Depth attenuation**: `I'(x,y) = I(x,y) · max(0, 1 − α·y/H)`, a linear intensity ramp with severity `α ∈ {0.3, 0.5, 0.7}`, modelling absorption and scattering with tissue depth.
- **Acoustic shadow**: `I'(x,y) = I(x,y) · (1 − exp(−(x−x₀)²/2σ²))`, a Gaussian intensity reduction at a uniformly sampled centre, width `σ ∈ {0.1W, 0.2W, 0.3W}`, modelling ribs and calcifications.

Both applied **consistently across all frames**, to simulate a real acquisition rather than per-frame noise.

> [!note] Three design choices worth stealing for robot evaluation
> 1. **The perturbations are derived from the physics of the sensor**, not from a generic corruption library. The robotics analogue is not "add Gaussian noise to the camera" but *model the actual failure modes* — lighting change, occlusion by the arm, specular surfaces, calibration drift.
> 2. **The severity is swept**, giving a degradation *curve* rather than a single perturbed number. [LIBERO-PRO](libero-pro-paper.md) reports a collapse; a swept severity axis would say *where* it collapses.
> 3. **The population argument.** The cases most worth automating are the ones least represented in training data. The manipulation tasks worth having a robot do are, likewise, the awkward ones nobody collected 50 clean demonstrations of.
>
> Held against the wiki's [VLA success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) — where a ten-model tier spans 1.2 percentage points on LIBERO — a swept, physics-derived perturbation axis would separate that tier immediately. Nobody has built one.

## Setup

- **EchoJEPA-G**: ViT-Giant, **1.1B params**, 18.1M proprietary videos.
- **EchoJEPA-L**: ViT-Large, **307M params**, 525K videos from **MIMIC-IV-Echo** — **open-sourced**, along with the evaluation framework.
- **Data**: Toronto internal (150K studies, probe training), Chicago internal (60K, external holdout site), EchoNet-Dynamic (10,030 videos, Stanford, zero-shot LVEF), EchoNet-Pediatric (3,316 videos).
- **Tasks**: 12-class view classification; LVEF regression (MAE %); RVSP regression (MAE mmHg, requiring multi-view integration across apical and subcostal views).
- **Adaptations from V-JEPA 2**: frame rate raised **4 → 24 fps** because "cardiac dynamics unfold rapidly"; random-crop scale range narrowed **(0.3, 1.0) → (0.5, 1.0)** because the ultrasound sector is fan-shaped and crops below 50% risk excluding cardiac structures entirely.
- **Multi-view probing framework** with factorized `E_view` and `E_clip` embeddings and view dropout (`p_miss = 0.1`), plus a standardized protocol: frozen backbones, identical probes, consistent hyperparameter search across all baselines.

> [!note] The augmentation adaptations are an inductive-bias story
> Both changes are **domain knowledge injected as augmentation policy**, not architecture. An augmentation set is an invariance claim ([inductive bias](../concepts/learning/inductive-bias.md)), and V-JEPA 2's natural-video defaults assert invariances that are false for ultrasound — aggressive cropping asserts that chamber proportions do not matter, and 4 fps asserts cardiac motion is slow. The fix is two numbers. Worth remembering next time a robotics pipeline inherits vision defaults.

## Relation to the Goodfire case study

[Goodfire's robotics & vision page](goodfire-silico-robotics-vision.md) reports analyzing EchoJEPA and finding, among other things, **ECG signal leakage into the training pipeline**, caught by frame-shuffling validation.

> [!warning] The ECG-leakage finding is not in this paper
> The word "ECG" does not appear in the preprint. So Goodfire's finding is either (a) a genuine external discovery the authors have not published, (b) about a different or internal version of the model, or (c) imprecisely described in marketing copy. **The wiki cannot tell which**, and should not attribute the finding to this paper.
>
> If (a), it is a good advertisement for external interpretability audit — a leak found by a third party that the model's own strong robustness results did not surface. Note that this paper's robustness protocol tests **acoustic** perturbations and **population** shift, and would not catch a signal leaking in from a co-recorded modality. That is a real gap in an otherwise careful evaluation, and it is exactly the kind a latent-space audit would find.

## Entities mentioned

- **[EchoJEPA](../entities/echojepa.md)** — the model.
- **Bo Wang** (senior author, UHN/Vector/Toronto), Alif Munim, Adibvafa Fallahpour, Teodora Szasz (co-first). No wiki pages.
- **[V-JEPA 2](../entities/v-jepa-2.md)** — the architecture adapted.
- **Arc Institute** — a Fallahpour affiliation, and separately a named [Goodfire](../entities/goodfire.md) customer.
- **EchoWorld** (Yue et al. 2025) — cited in related work: world modelling for **robotic ultrasound probe guidance**, conditioned on **6-DOF probe pose**. Not ingested; the most robotics-relevant citation in the paper.
- Baselines: PanEcho, EchoPrime, EchoCLIP, EchoFM, VideoMAE.

## Concepts touched

- **[JEPA](../concepts/world-models/jepa.md)** — a clinical branch at foundation scale.
- **[Latent space](../concepts/world-models/latent-space.md)** — what is being predicted in.
- **[Inductive bias](../concepts/learning/inductive-bias.md)** — the augmentation adaptations.
- **[Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md)** — by analogy; the robustness protocol is the transferable object.

## Open questions / TBD

- **EchoWorld** — robotic probe guidance via world modelling with 6-DOF pose conditioning. Directly in this wiki's subject matter and un-ingested.
- **Does the robustness advantage survive a leak-style perturbation?** The protocol covers sensor physics and population shift, not spurious correlation with a co-recorded signal. Goodfire's claim suggests it does not.
- **EchoJEPA-L is open** (MIMIC-IV-Echo). That makes it a rare **publicly available JEPA checkpoint with a published perturbation benchmark attached** — a plausible testbed for [the latent-inspection experiment](../syntheses/projects/latent-inspection-policy-collapse.md) without needing robot hardware.

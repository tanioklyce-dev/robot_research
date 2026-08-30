---
title: EchoJEPA
type: entity
subtype: model
created: 2026-08-30
updated: 2026-08-30
sources: 2
tags: [jepa, v-jepa-2, echocardiography, medical-imaging, foundation-model, vector-institute, open-weights, robustness]
---

**EchoJEPA** — a [JEPA](../concepts/world-models/jepa.md)-family foundation model for **echocardiography**, from Bo Wang's lab (University Health Network / Vector Institute / Toronto) with Chicago, Philips and UCSF collaborators. Trained on **18 million echocardiogram videos across 300K patients** by adapting **[V-JEPA 2](v-jepa-2.md)**. See the [paper](../sources/echojepa-paper.md) (arXiv 2602.02603, Feb 2026).

**The wiki's clinical branch of the JEPA family**, and its largest JEPA-family model outside natural video.

## Variants

| Model | Backbone | Params | Pretraining data | Availability |
|---|---|---|---|---|
| **EchoJEPA-G** | ViT-Giant | 1.1B | 18.1M proprietary videos | not released |
| **EchoJEPA-L** | ViT-Large | 307M | 525K MIMIC-IV-Echo videos | **open-sourced**, with evaluation framework |

## Why it matters here

- **The JEPA thesis tested where it should win most.** Ultrasound is dominated by stochastic speckle and acquisition artifacts that bear no relation to anatomy. A reconstruction objective "must faithfully reproduce speckle to minimize its loss"; latent prediction against an EMA teacher does not. That is [LeCun's](yann-lecun.md) argument for [JEPA](../concepts/world-models/jepa.md) in a domain where the unpredictable fraction is physical rather than debatable.
- **Label efficiency**: **78.6% with 1% of labels**, against **42.1%** for the best baseline using **100%**.
- **Robustness**: degrades **2.3%** under physics-informed acoustic perturbation where the next best degrades **16.8%**; zero-shot adult→pediatric transfer beats all *fine-tuned* baselines.
- **An evaluation protocol worth copying** — physics-derived, severity-swept perturbations instead of generic corruption benchmarks. See the [paper page](../sources/echojepa-paper.md).

## Mentioned in

- [EchoJEPA paper](../sources/echojepa-paper.md)
- [Silico for Robotics & Vision (Goodfire)](../sources/goodfire-silico-robotics-vision.md) — surfaced here first, as an external interpretability case study claiming to have found **ECG signal leakage** in its training pipeline. ⚠️ That finding does **not** appear in the paper; see the source page.

## Open questions / TBD

- **The ECG-leakage claim** is unverified and unattributable to the paper.
- **EchoJEPA-L is a rare open JEPA checkpoint with a published perturbation benchmark**, which makes it a candidate testbed for [latent-inspection-predicts-collapse](../syntheses/projects/latent-inspection-policy-collapse.md) without robot hardware.
- **EchoWorld** (cited in its related work) applies world modelling to **robotic ultrasound probe guidance** with 6-DOF pose conditioning — squarely in this wiki's subject matter, un-ingested.

---
title: "Learning Transferable Visual Models From Natural Language Supervision (Radford, Kim, Hallacy et al., ICML 2021) — CLIP"
type: source
url: https://arxiv.org/abs/2103.00020
local_path: raw/2103.00020v1.pdf
sha256: 6478b6e571a7d6fcd846d8ef77bfd60c285f1986abb8f475eedc43de403074f5
author: "Alec Radford*, Jong Wook Kim*, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever"
affiliation: OpenAI
venue: "ICML 2021; arXiv 2103.00020"
published: 2021-02-26
ingested: 2026-08-30
tags: [clip, contrastive, vision-language, zero-shot, foundational, openai, radford, sutskever, robustness, distribution-shift, prompt-engineering, wit]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/2103.00020v1.pdf`, 48 pages). §1–4 and §6–7 read in full (motivation, the efficiency argument, dataset, training, zero-shot transfer, prompt engineering, robustness, limitations); the ~20 pages of per-dataset appendices skimmed. **Ingested because 90 wiki pages cited CLIP and none defined it** — the largest coverage gap the wiki has had.

## Summary

**CLIP (Contrastive Language–Image Pre-training)** — Radford, Kim et al. (OpenAI; ICML 2021). The paper that made **natural language the supervision signal for vision**, and thereby created the object every vision-language model in this wiki is built on.

The setup: **400 million (image, text) pairs** scraped from the internet (**WIT**, WebImageText), an image encoder and a text encoder trained jointly so that matching pairs land near each other in a shared embedding space. At test time the **text encoder synthesizes a classifier** — embed the class names, compare against the image embedding, take the nearest. No fine-tuning, no labelled examples, no output head.

**Headline result**: zero-shot CLIP **matches the original ResNet-50 on ImageNet (76.2%) without using any of its 1.28 million training examples.** Prior work in this line reached 11.5%.

**Why it matters to this wiki.** CLIP is the mechanism by which *language got attached to vision*, and a [VLA](../concepts/learning/vla-models.md) is (vision + language) → action. It sits under [CLIPort](../entities/cliport.md), under every VLM backbone in the VLA taxonomy, under EchoCLIP in the [echocardiography](echojepa-paper.md) line, and under the entire language-grounding thread. It is also, with [ViT](vit-paper.md), one of the two papers that made "frozen pretrained visual encoder" the default starting point for robot policies.

## Abstract (verbatim)

> "State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories. This restricted form of supervision limits their generality and usability since additional labeled data is needed to specify any other visual concept. Learning directly from raw text about images is a promising alternative which leverages a much broader source of supervision. We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch on a dataset of 400 million (image, text) pairs collected from the internet. After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks. We study the performance of this approach by benchmarking on over 30 different existing computer vision datasets, spanning tasks such as OCR, action recognition in videos, geo-localization, and many types of fine-grained object classification. The model transfers non-trivially to most tasks and is often competitive with a fully supervised baseline without the need for any dataset specific training. For instance, we match the accuracy of the original ResNet-50 on ImageNet zero-shot without needing to use any of the 1.28 million training examples it was trained on."

## The efficiency argument — the actual contribution

The architecture is not the contribution. **The choice of objective is**, and §2.3 lays out the ladder explicitly:

1. **Predict the caption** (VirTex-style: image CNN + text transformer, generate the exact words). Their 63M-parameter text transformer — already twice the compute of its ResNet-50 image encoder — learns to recognize ImageNet classes **three times slower** than a much simpler baseline that predicts a **bag-of-words** encoding of the same text.
2. **Swap the predictive objective for a contrastive one**, from the same bag-of-words baseline: a further **4× efficiency improvement** in the rate of zero-shot transfer to ImageNet.

Roughly an order of magnitude, from *making the task easier*. Their reasoning: predicting the exact words "is a difficult task due to the wide variety of descriptions, comments, and related text that co-occur with images," so they solve "the potentially easier proxy task of predicting only which text as a whole is paired with which image and **not the exact words of that text**."

> [!note] The same lesson, for the third time in this wiki
> *Do not model what you cannot predict.* [Bengio et al. 2003](bengio2003-neural-probabilistic-language-model.md) manufactured a continuous space rather than modelling a discrete one directly. [JEPA](../concepts/world-models/jepa.md) predicts in representation space because pixel reconstruction wastes capacity on unpredictable detail — [EchoJEPA](echojepa-paper.md) makes that argument sharpest, since ultrasound speckle is *physically* unpredictable. CLIP is the same move: the caption's exact wording is noise, the *pairing* is signal, and discarding the wording buys 12× compute efficiency.
>
> **The design question is not "what is the most informative objective" but "what is the weakest objective that still forces the representation I want."** Three independent lines in this wiki converge on it.

### Mechanically

Given a batch of `N` (image, text) pairs, predict which of the `N × N` possible pairings actually occurred — maximize cosine similarity for the `N` real pairs, minimize it for the `N² − N` others, with a **learned temperature `τ`** (log-parameterized, optimized directly rather than tuned).

Deliberate simplifications against the ConVIRT design they started from: **linear projection only** (no non-linear projection head — they found no training-efficiency difference and speculate non-linear heads are "co-adapted with details of current image-only self-supervised methods"), no text transformation function, and **random square crop as the only augmentation**. Trained from scratch, no ImageNet init, no pretrained text weights. **Batch size 32,768.**

**Encoders**: ResNet-50 variants (RN50x4/16/64) with **attention pooling** — a single layer of transformer-style multi-head QKV attention whose query is conditioned on the global average-pooled feature — replacing global average pooling; and [ViT](vit-paper.md). Text encoder: 63M params, 12 layers, 512 wide, 8 heads, **BPE vocabulary of 49,152**, bracketed with `[SOS]`/`[EOS]`.

## Prompt engineering, and why it is not a footnote

Class names alone underperform. `"A photo of a {label}."` helps. Domain hints help more — `"A photo of a {label}, a type of pet."` on Oxford Pets, food on Food101, aircraft on FGVC, quotes around the target string for OCR. Ensembling over multiple prompts (constructed **in embedding space**, not probability space) helps further.

**Together: +~5 points on average across 36 datasets** — which the paper notes is "similar to the gain from using 4 times more compute with the baseline zero-shot method but is 'free' when amortized over many predictions."

The diagnosed cause is **polysemy**: "when the name of a class is the only information provided to CLIP's text encoder it is unable to differentiate which word sense is meant due to the lack of context."

> [!note] This is where prompt engineering entered vision
> Two years before it became a job title in language ([Karpathy's 2023 lecture](karpathy-software-3-and-transformer-history-lecture.md) treats it as novel), CLIP established that **the text side of a vision-language model is a programmable interface** and that phrasing is worth multiplicative compute. Every "language-conditioned policy" in this wiki inherits both the capability and the fragility: if `"a photo of a {label}"` beats `"{label}"` by 5 points, a robot instruction's phrasing is a hyperparameter nobody is sweeping.

## Robustness — the result most relevant to robot generalization

Evaluated on **7 natural distribution shifts** (ImageNetV2, ImageNet-R, ImageNet-A, ImageNet Sketch, ObjectNet, ImageNet-Vid, YouTube-BB), zero-shot CLIP closes the **"robustness gap" by up to 75%** relative to standard ImageNet-trained models at matched ImageNet accuracy.

The framing is worth borrowing: **effective robustness** — improvement on distribution shift *beyond what is predicted by in-distribution accuracy*. Ordinary models move along a fixed line relating ImageNet accuracy to shifted accuracy; CLIP sits above the line.

> [!note] Why a robotics wiki should care about a 2021 ImageNet result
> This is the same measurement shape as [EchoJEPA](echojepa-paper.md)'s perturbation protocol and the same question as [LIBERO-PRO](libero-pro-paper.md)'s: *does in-distribution score predict out-of-distribution score?* CLIP's answer is that it depends on how the representation was trained, and that **broad, weakly-supervised, natural-language pretraining buys robustness that supervised ImageNet training does not.**
>
> And the caveat CLIP itself provides: §7 reports that the benefit is "almost entirely gone in a fully supervised" fine-tuned setting. **Fine-tuning on a narrow target distribution destroys the robustness the pretraining bought.** Every robot policy in this wiki fine-tunes a pretrained backbone on a few hundred demonstrations. Nobody has measured what that costs.

## Where it fails

Near-random on several specialized tasks: **counting objects**, satellite imagery classification (EuroSAT, RESISC45), **lymph node tumour detection** (PatchCamelyon), and synthetic benchmarks (CLEVR, MNIST, GTSRB). Zero-shot CLIP is roughly equivalent to a **16-shot linear classifier** on BiT-M ResNet-152x2 features — good, but not a replacement for supervision where supervision exists.

The counting failure is the one to remember for manipulation: CLIP's embedding is a bag of concepts, not a scene description with cardinality or spatial relations.

## Entities mentioned

- **OpenAI** — all authors. **[Ilya Sutskever](../entities/ilya-sutskever.md)** — final author; his third appearance in this wiki after [word2vec paper 2](mikolov2013-distributed-representations-words-phrases.md) and [seq2seq](sutskever2014-sequence-to-sequence-learning.md).
- **Alec Radford** — first author; also GPT-1/2. No wiki page.
- **[ViT](vit-paper.md)**, ResNet, BiT, and the VirTex / ICMLM / ConVIRT line CLIP simplifies.

## Concepts touched

- **[VLA models](../concepts/learning/vla-models.md)** — the vision-language half.
- **[Distributed representations](../concepts/learning/distributed-representations.md)** — a *shared* embedding space across two modalities.
- **[Contrastive learning](../glossary.md#contrastive-learning)** / **[InfoNCE](../glossary.md#infonce)** — the objective, at 400M scale.
- **[Inductive bias](../concepts/learning/inductive-bias.md)** — "natural language is able to express, and therefore supervise, a much wider set of visual concepts," against a fixed 1000-class softmax.

## Open questions / TBD

- **What does robot fine-tuning cost in effective robustness?** CLIP says the robustness benefit largely disappears under full supervision. Directly testable, unmeasured, and it bears on every frozen-vs-fine-tuned backbone decision in this wiki. Related: [the proposed latent-inspection experiment](../syntheses/projects/latent-inspection-policy-collapse.md).
- **Prompt sensitivity in language-conditioned policies.** +5 points from phrasing on classification; nobody reports the equivalent sweep for robot instructions.
- **The counting/spatial failure** is unaddressed here and is exactly what manipulation needs. [CLIPort](../entities/cliport.md) works around it architecturally rather than fixing it.
- **OpenCLIP / LAION** — the open reproduction and the open 400M/2B datasets — are un-ingested and are what most robot policies actually use.

---
title: "fast.ai — Practical Deep Learning for Coders 2022 (Jeremy Howard)"
type: source
url: https://course.fast.ai/
author: Jeremy Howard (and the fast.ai team, originally co-founded with Rachel Thomas)
affiliation: fast.ai; recorded at University of Queensland
published: 2022 (Part 1 — 9 lessons of ~90 min each); cumulative platform from 2017 onwards
ingested: 2026-05-14
created: 2026-05-14
updated: 2026-05-14
license: Course videos and notebooks are free / openly available; fastbook (the companion text) is Apache 2.0 with a no-commercial-republish clause on the book version
tags: [fastai, course, pedagogical, deep-learning, pytorch, transfer-learning, cnn, nlp, jeremy-howard, curriculum-companion]
---

> [!note] Ingest depth
> Source-page metadata gathered from the fast.ai course landing page. Lesson titles + recipe summary verified against the [fastai/fastbook](https://github.com/fastai/fastbook) companion repo (which carries the 2022 chapter list). This ingest is **summary-level** — a pointer + curriculum-fit assessment rather than a deep walk-through of each lesson.

## Summary

**"Practical Deep Learning for Coders 2022 Part 1"** — Jeremy Howard, fast.ai. Nine ~90-minute lessons recorded at the University of Queensland. The course is a *coder-first* DL onboarding path: students train and deploy production-grade models in the first lesson and learn the underlying math/architecture in increasing depth as the course progresses. The published lesson list:

1. **Getting started** — image classification end-to-end with `fastai` + transfer learning
2. **Deployment** — Hugging Face Spaces + Gradio
3. **Neural net foundations** — gradients, SGD, MNIST from scratch
4. **Natural Language (NLP)** — Hugging Face Transformers, Kaggle competition workflow
5. **From-scratch model** — Random forests, decision trees, regression
6. **Random forests** — feature importance, partial dependence
7. **Collaborative filtering** — embeddings, dot-product models
8. **Convolutions (CNNs)** — architecture + receptive fields
9. **Data ethics** (bonus)

**Stack taught:** PyTorch + fastai + Hugging Face Transformers + Gradio + nbdev. The course explicitly targets coders with ~1 year of programming experience and high-school math.

## Why it matters to this wiki

- **The strongest "first-touch" pedagogical resource for the entire [Robot-learning curriculum](../syntheses/curriculum/robot-learning-curriculum.md) Tier 1.** The wiki's curriculum starts at Module 1 (NN basics) and assumes the reader is willing to derive backprop and read papers; the fast.ai course is the **on-ramp** for readers who haven't yet trained a single model. Recommended-viewing for readers who fail Module 1's prereq diagnostic and want a hands-on running-code introduction first.
- **Companion to [karpathy/micrograd](karpathy-micrograd.md) and [karpathy/nanoGPT](karpathy-nanogpt.md).** Karpathy's repos are "build NNs from scratch in pure Python / PyTorch primitives"; fast.ai is "use the highest-level library and ship a model today." The two approaches are pedagogically complementary — bottom-up vs. top-down. Both are now in the wiki.
- **PyTorch + Hugging Face Transformers literacy.** Many of the wiki's downstream-tracked codebases ([nanoGPT](karpathy-nanogpt.md), [nanochat](karpathy-nanochat.md), [LeWM](leworldmodel-paper.md), [V-JEPA 2](vjepa2-github.md), [Diffusion Policy](diffusion-policy-paper.md), [HF TRL SFT Trainer](huggingface-trl-sft-trainer.md)) assume PyTorch fluency. fast.ai is the most widely-recommended path to that fluency.
- **Transfer learning + ResNet pretraining** are first-class topics — feed directly into [Curriculum Module 2 — CNNs](../syntheses/curriculum/curriculum-02-cnns.md).
- **Data ethics chapter** (lesson 9) is a tangential but interesting cross-link with the wiki's [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) thread — fast.ai has been one of the louder voices on dataset-bias and deployment-ethics issues in the practical-ML community.

## Curriculum hookup

This is a **prerequisite-companion** rather than a primary-source, so it doesn't sit inside the curriculum per se — it sits *before* it for readers who need it. Suggested placement:

- In the [Robot-learning curriculum](../syntheses/curriculum/robot-learning-curriculum.md) top-matter, under a `> [!note] Don't have a year of PyTorch under your belt?` callout pointing at this course as Tier 0.
- In [Module 1's "Prereq diagnostic"](../syntheses/curriculum/curriculum-01-neural-networks.md): readers who fail the diagnostic should be pointed here first.
- In [Module 2 — CNNs](../syntheses/curriculum/curriculum-02-cnns.md) at the "transfer learning + ImageNet pretraining" section: fast.ai Lesson 1 + Lesson 8 are the canonical hands-on coverage of this workflow.

## Authors

- **Jeremy Howard** — co-founder of fast.ai; ex-Kaggle president; ex-Enlitic CEO. Highly regarded practical-DL educator. Not yet a wiki entity page; one-line stub could absorb future fast.ai references.
- **Rachel Thomas** — co-founder of fast.ai (left in ~2021); University of San Francisco data ethics lab. Not yet a wiki entity.

## Stack covered

- **PyTorch** — primary tensor library.
- **fastai** — Howard's high-level wrapper over PyTorch; abstracts data loaders, training loops, and common architecture patterns.
- **Hugging Face Transformers** — covered in lesson 4 (NLP), increasingly the default for any transformer-based work.
- **Gradio** — used in lesson 2 for deployment; Gradio + Hugging Face Spaces is the canonical free-deployment pipeline.
- **nbdev** — Howard's Jupyter-notebook-as-source-code framework; used to develop the `fastai` library itself.

## Concepts touched (the full Tier 1 footprint)

- **Transfer learning** — central to lessons 1–2.
- **Stochastic gradient descent + backprop** — lesson 3.
- **Data augmentation + weight decay** — recurring.
- **Image classification** — lessons 1, 8.
- **NLP via transformers** — lesson 4.
- **Random forests + regression** — lessons 5, 6 (the non-NN curriculum half).
- **Embeddings + collaborative filtering** — lesson 7. Useful for understanding the *embedding* unit of the JEPA / SSL line.
- **Convolutions / CNNs** — lesson 8.

## Position in the open-DL-pedagogy landscape

```
Hands-on, library-first:
  fast.ai (THIS COURSE — top-down, ship a model today)
  Hugging Face NLP / RL / Diffusion courses
From-scratch, library-second:
  Karpathy — micrograd / makemore / nanoGPT / nanochat (bottom-up, derive everything)
Math-first:
  3Blue1Brown Deep Learning series (popular video)
  Stanford CS231n / CS224n (academic)
  Goodfellow, Bengio, Courville — Deep Learning (textbook)
```

fast.ai occupies the **top-down, library-first** quadrant. The wiki's curriculum is closer to the **bottom-up, derivation-first** path (Karpathy + Bishop + papers). The two approaches are complementary, not competitive.

## Open questions / TBD

- **Part 2 of the course (From Stable Diffusion to LLMs from scratch).** Howard ran a 2022 Part 2 that covered diffusion models from scratch and is a much closer fit to the wiki's [Curriculum Module 5 — Generative modeling fundamentals (DDPM, full math)](../syntheses/curriculum/curriculum-05-generative-models.md). Worth a follow-up evaluation pass — the Part 2 page is at https://course.fast.ai/Lessons/part2.html.
- **The `fastai` library itself** as a wiki tool reference — useful but probably below the bar; the library is widely used outside research-track DL, less so inside it.
- **A `entities/fast-ai.md` stub** — would let future fast.ai source ingests (Part 2, the *fastbook* companion) attach cleanly. Defer until a second fast.ai source surfaces.

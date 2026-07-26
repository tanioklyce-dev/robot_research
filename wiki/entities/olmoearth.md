---
title: OlmoEarth (Ai2)
type: entity
subtype: model
created: 2026-07-26
updated: 2026-07-26
tags: [olmoearth, ai2, allen-institute, ai-for-the-planet, earth-observation, remote-sensing, foundation-model, geospatial, open-source, open-data, skylight, earthranger]
sources: 1
---

# OlmoEarth (Ai2)

**OlmoEarth** is [Ai2](ai2.md)'s open **earth-observation foundation model** and planetary-intelligence platform — the flagship of its **AI for the Planet** mission pillar ([Ai2 homepage](../sources/ai2-homepage.md)). It turns raw satellite imagery into actionable insight without requiring specialized AI expertise: fine-tune, generate embeddings, and deploy models "in hours" for continuous planetary monitoring.

## Why it matters in this wiki

OlmoEarth extends the **"Olmo" open-model brand from text into geospatial/remote-sensing** — the wiki's first Ai2 model outside the language/vision/action stack. It carries the same radical-openness posture (open foundation models + **open pretraining dataset** + open code on Hugging Face / GitHub) into a new domain, and anchors the AI-for-the-Planet pillar that reframes Ai2 as a three-mission org rather than an open-LLM lab.

## Claims (from the homepage; primary not yet ingested)

- "The most performant model for Earth data," trained on **millions of global observations**.
- **~97% accuracy** in a Wetlands International beta for **wetland detection** (testimonial).
- Cuts processing time ~**50%** vs. traditional methods; **v1.1** (announced May 2026) reduced compute cost up to **3×** vs. prior versions.
- **Embeddings export** feature added April 2026.
- End-to-end: refine → analyze → deploy; fine-tuning + embedding generation + production deployment.

## Downstream platforms

- **Skylight** — ocean-intelligence platform built on OlmoEarth foundation models for **high-seas protection**.
- **EarthRanger** — environmental / wildlife-monitoring platform under the AI-for-the-Planet initiative.

## Openness

Fully open: foundation models on Hugging Face, **pretraining dataset publicly available**, code on GitHub.

## Related

- [Ai2](ai2.md) — the org; OlmoEarth is its AI-for-the-Planet flagship.
- [OLMo](olmo.md) — the language-model namesake of the "Olmo" open-model brand.
- [Asta](asta.md) — the sibling AI-for-Science flagship.

## Open questions

- **Architecture / scale unknown** — model sizes, backbone, and the earth-observation pretraining corpus aren't on the landing page. The HF model card + a paper would fill this in.
- Is OlmoEarth a single foundation model or a family (like the OLMo/Molmo families)? v1.1 implies versioned releases.
- Does it share any architecture with the language-side Olmo models, or is the shared name purely a branding umbrella?

## Mentioned in

- [Ai2 homepage (allenai.org)](../sources/ai2-homepage.md) — the source that surfaced OlmoEarth.

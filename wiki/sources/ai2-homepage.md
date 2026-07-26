---
title: "Ai2 homepage — allenai.org (Truly open breakthrough AI)"
type: source
url: https://allenai.org/
author: Allen Institute for AI (Ai2)
published: continuously updated
ingested: 2026-07-26
venue: organization website
format: web
tags: [ai2, allen-institute, open-source, open-data, asta, olmoearth, ai-for-science, ai-for-the-planet, embodied-ai, semantic-scholar, landing-page]
---

# Ai2 homepage — allenai.org

## Summary

The [Ai2](../entities/ai2.md) homepage, ingested to capture how the org positions itself in mid-2026 — which turns out to be **substantially broader than the "open LLM/VLM/VLA lab" the wiki had been tracking**. Under the tagline **"Truly open breakthrough AI"** ("Breakthrough AI to solve the world's biggest problems"), Ai2 now presents its work across **three mission pillars**: **AI for Science** (the [Asta](../entities/asta.md) agentic-discovery ecosystem + Semantic Scholar), **AI for the Planet** (the [OlmoEarth](../entities/olmoearth.md) earth-observation foundation model + Skylight + EarthRanger), and **Embodied AI** (robotics + 3D reasoning — the [MolmoAct2](../entities/molmoact2.md) thread). The open-everything LLM/VLM stack ([OLMo](../entities/olmo.md), [Molmo](../entities/molmo.md), Tülu 3, [Dolma](../entities/dolma.md)) remains the foundation, but the homepage frames it as means, not end.

## Key claims

- **Tagline / positioning:** "Truly open breakthrough AI"; mission "Breakthrough AI to solve the world's biggest problems." Radical openness (weights + data + code + recipes) remains the through-line.
- **Three mission pillars** surfaced on the site:
  - **AI for Science** — dataset analysis and autonomous discovery.
  - **AI for the Planet** — climate modeling, agriculture, wildfire management, wildlife protection.
  - **Embodied AI** — robotics and 3D reasoning.
- **Featured language/multimodal models:** [OLMo](../entities/olmo.md) ("the truly open LLM"), [Molmo](../entities/molmo.md) (multimodal), **Tülu 3** (post-training).
- **[Asta](../entities/asta.md)** — "an agentic ecosystem that advances scientific discovery," with three components: **Asta Agents** (research assistants for scholarly tasks), **AstaBench** (a rigorous evaluation framework + leaderboards for science agents), and **Asta Resources** (tools, baseline agents, templates, APIs for building science agents). Live at asta.allen.ai. **AutoDiscovery** (via AstaLabs) "autonomously generates hypotheses, runs experiments," using **Bayesian surprise** to identify discoveries; free access noted through June 2026.
- **[OlmoEarth](../entities/olmoearth.md)** — an open **earth-observation foundation model** / planetary-intelligence platform: fine-tune, generate embeddings, and deploy on satellite imagery "in hours." Claims "the most performant model for Earth data," ~50% faster processing, **97% accuracy** in a Wetlands International wetland-detection beta; **v1.1** (May 2026) cut compute cost up to 3×; embeddings export added April 2026. Fully open (models + pretraining dataset + code on Hugging Face / GitHub).
- **Skylight** — ocean-intelligence platform built on OlmoEarth foundation models for high-seas protection.
- **EarthRanger** — environmental/wildlife monitoring platform (AI-for-the-Planet initiative).
- **Semantic Scholar** — Ai2's research-paper discovery platform (AI-for-Science initiative).
- **Playground** — interactive interface for experimenting with Ai2 models.
- **Partnerships named:** University of Washington (Paul G. Allen School), National Science Foundation, Google Cloud.

## Entities mentioned

- [Ai2 (Allen Institute for AI)](../entities/ai2.md) — the org.
- [Asta](../entities/asta.md) — the AI-for-Science agentic ecosystem (new).
- [OlmoEarth](../entities/olmoearth.md) — the AI-for-the-Planet earth-observation foundation model (new).
- [OLMo](../entities/olmo.md) / [OLMoE](../entities/olmoe.md) / [Molmo](../entities/molmo.md) / [Dolma](../entities/dolma.md) / [MolmoAct2](../entities/molmoact2.md) — the existing open-stack pillars.

## Concepts touched

- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — Asta Agents are science-specific LLM agents.

## Open questions

- **Asta / AstaBench primaries not ingested** — the science-agent capabilities, leaderboard methodology, and AutoDiscovery's Bayesian-surprise mechanism are only sketched here. A dedicated paper or the asta.allen.ai docs would deepen this.
- **OlmoEarth architecture unknown** — model sizes, backbone, and the earth-observation pretraining corpus aren't on the landing page; the HF model card + paper would fill this in.
- Is the "Olmo" brand now an umbrella spanning modalities (text → **OlmoEarth** geospatial)? Worth tracking whether future Ai2 releases keep the Olmo-prefix convention across domains.

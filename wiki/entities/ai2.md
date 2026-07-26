---
title: Ai2 (Allen Institute for AI)
type: entity
subtype: research-lab
created: 2026-07-24
updated: 2026-07-26
sources: 8
tags: [ai2, allen-institute, research-lab, open-source, open-data, seattle, nonprofit, robotics, vla, ai-for-science, ai-for-the-planet, asta, olmoearth]
---

# Ai2 (Allen Institute for AI)

**Ai2** (the **Allen Institute for AI**) is a Seattle-based **nonprofit AI research
institute** (founded 2014 by the late Paul Allen) whose defining stance is
**radical openness** — releasing not just model weights but **training data, code,
recipes, checkpoints, and logs**. Tagline (mid-2026): **"Truly open breakthrough
AI."** It is the single lab behind the wiki's entire "open-everything" thread.

## Three mission pillars

As of its mid-2026 site ([Ai2 homepage](../sources/ai2-homepage.md)), Ai2 organizes
its work around **three missions** — a broader framing than the "open-LLM/VLM/VLA
lab" the wiki initially tracked. The open foundation-model stack (below) is the
means; these are the ends:

- **AI for Science** — [Asta](asta.md), an agentic scientific-discovery ecosystem
  (Asta Agents + AstaBench leaderboards + Asta Resources; AutoDiscovery for
  autonomous hypothesis generation), plus **Semantic Scholar** (paper discovery).
- **AI for the Planet** — [OlmoEarth](olmoearth.md), an open earth-observation
  foundation model, with **Skylight** (ocean intelligence / high-seas protection)
  and **EarthRanger** (wildlife & environmental monitoring) built on top.
- **Embodied AI** — robotics + 3D reasoning: the [Molmo](molmo.md) →
  [MolmoAct](molmoact.md) → [MolmoAct2](molmoact2.md) line.

## What Ai2 has built (as tracked here)

- **Open LLMs — the [OLMo](olmo.md) family:** dense [OLMo](../sources/olmo-paper.md)
  and [OLMo 2](../sources/olmo-2-paper.md), and the sparse
  [OLMoE](../sources/olmoe-paper.md) MoE — all fully open.
- **Open data:** [Dolma](dolma.md) (the 3T-token pretraining corpus,
  [Soldaini et al. 2024](../sources/dolma-paper.md)) and **PixMo** (the
  distillation-free VLM datasets, [Deitke et al. 2024](../sources/molmo-pixmo-paper.md)).
- **Open VLM / VLA:** [Molmo](molmo.md) (the pointing VLM) and the
  [MolmoAct](molmoact.md) → **[MolmoAct2](molmoact2.md)** action-reasoning VLAs —
  Ai2's move into robotics. MolmoAct2 ([Fang, Duan et al. 2026](../sources/molmoact2-paper.md))
  is the fully-open, **deployable** VLA: a [Molmo2-ER](molmo2-er.md) backbone, three
  released robot datasets (incl. the largest open bimanual dataset to date), an
  open-data [FAST](fast-action-tokenization.md) tokenizer, and top-of-table LIBERO
  scores — Ai2's openness thread reaching a policy that runs on a <$6,000 setup.
- **Open science & planet models:** [Asta](asta.md) (AI-for-Science agent ecosystem)
  and [OlmoEarth](olmoearth.md) (the "Olmo" brand extended to earth observation —
  open models + open pretraining data) — the two newer pillars.
- **Recipes/tools (referenced):** Tülu 3 post-training + **RLVR**, the OLMES eval
  suite, Open Instruct, the **Playground** model-experimentation UI — the
  surrounding open toolchain.

## The wiki-specific connection

Ai2's CEO **Ali Farhadi** is also a **co-author of the original
[YOLO](../sources/yolo-you-only-look-once-2016.md)** (and YOLO's Redmon/Farhadi
work lists the Allen Institute for AI as an affiliation) — so the same lab thread
runs from the founding **single-stage object detector** (2016) to today's
**fully-open LLM/VLM/VLA** stack. Ai2 is the "commodity, but *inspectable*"
counterweight to the closed frontier labs the wiki otherwise tracks.

## Related

- [OLMo](olmo.md) / [OLMoE](olmoe.md) — the open LLMs.
- [Dolma](dolma.md) — the open pretraining corpus.
- [Molmo](molmo.md) / [Molmo2-ER](molmo2-er.md) — the open VLMs (backbones of MolmoAct / MolmoAct2).
- [MolmoAct](molmoact.md) / [MolmoAct2](molmoact2.md) — Ai2's open action-reasoning VLAs (Embodied AI pillar).
- [Asta](asta.md) — the AI-for-Science agentic ecosystem.
- [OlmoEarth](olmoearth.md) — the AI-for-the-Planet earth-observation foundation model.
- [Ultralytics YOLO](ultralytics-yolo.md) — the lineage Ai2's Farhadi helped found.

## Mentioned in

- [OLMo](../sources/olmo-paper.md), [OLMo 2](../sources/olmo-2-paper.md), [OLMoE](../sources/olmoe-paper.md) — the open LLM releases.
- [Dolma](../sources/dolma-paper.md) — the open corpus.
- [Molmo and PixMo](../sources/molmo-pixmo-paper.md) — the open VLM + data.
- [MolmoAct2 (Fang, Duan et al. 2026)](../sources/molmoact2-paper.md) — the fully-open deployable VLA + three released robot datasets.
- [Ai2 homepage (allenai.org)](../sources/ai2-homepage.md) — the three-pillar (Science / Planet / Embodied) framing + Asta + OlmoEarth.
- [YOLO (Redmon et al. 2016)](../sources/yolo-you-only-look-once-2016.md) — Allen Institute for AI authorship affiliation.

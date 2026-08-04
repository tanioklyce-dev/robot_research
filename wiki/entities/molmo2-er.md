---
title: Molmo2-ER
type: entity
subtype: model
created: 2026-07-25
updated: 2026-08-03
sources: 4
tags: [molmo2-er, molmo2, molmo, vlm, embodied-reasoning, spatial-reasoning, pointing, vla-backbone, allen-institute, open-source, open-data, specialize-then-rehearse]
---

# Molmo2-ER

> [!note] Also called **MolmoER**
> The [MolmoAct2 paper](../sources/molmoact2-paper.md)'s **arXiv abstract** calls this backbone `MolmoER`; the PDF body (31 mentions) and the [Ai2 blog](https://allenai.org/blog/molmoact2) both call it **Molmo2-ER**. The wiki follows the majority. See the [source page](../sources/molmoact2-paper.md) naming table.

**Molmo2-ER** ("Embodied Reasoning") is [Ai2](ai2.md)'s **VLM backbone specialized for spatial and embodied reasoning**, and the foundation model under [MolmoAct2](molmoact2.md) ([Fang, Duan et al. 2026](../sources/molmoact2-paper.md), §2). It is a fine-tune of **Molmo2** (Clark et al. 2026) — a **4B** VLM in the [Molmo](molmo.md) lineage (SigLIP2 ViT → connector → LLM) — onto a **3.3M-sample embodied-reasoning corpus**. The thesis: general-purpose VLMs rarely train on the metric, geometric, and temporally grounded skills a robot policy needs (distance, free space, cross-view tracking, scene geometry), so a VLA is only as good as the backbone that supplies its reasoning.

## Why it matters in this wiki

Molmo2-ER is the first ingested VLM backbone **trained specifically for embodied reasoning as a first-class objective** rather than repurposed from semantic image understanding — and the paper's central "reasoning is only as good as the underlying model" argument. The wiki's [ablation evidence](../sources/molmoact2-paper.md) is the payoff: swapping plain Molmo2 for Molmo2-ER, with **no other change**, lifts LIBERO-Long discrete-action accuracy **+6.0 points** — so the embodied specialization transfers directly into action learning, not just VLM benchmarks. It sits in the [VLA VLM-backbone](../concepts/learning/vla-models.md) taxonomy as the **Ai2 open-data, embodied-reasoning-specialized** option, contrasting with NVIDIA's Eagle, Google's PaliGemma/Gemma3, and Hugging Face's SmolVLM-2.

## Training corpus (3.3M samples, six pillars)

- **Image embodied QA** — SAT (dynamic/egocentric), RoboPoint-QA (VQA breadth), RefSpatial (CoT referring), VST-P (metric depth/distance on a virtual camera), VSI-590K (in-the-wild + tour footage via 3D label propagation).
- **Image pointing & detection** — RefSpatial + full RoboPoint procedural pointing (700K normalized (x,y) targets) + 100K LVIS detection. Pointing is the **primary action interface**, deliberately oversampled.
- **Video embodied QA** — SIMS-VSI (sim labels for distance/direction/count/temporal order) + RoboVQA (human-annotated long-horizon planning/affordance/prediction).
- **Multi-image & ego–exo correspondence** — SenseNova-SI (500K) + VST-P cross-view split.
- **Abstract embodied reasoning** — CLEVR (compositional) + GRiD-3D (object-intrinsic relative direction).

## Specialize-then-rehearse recipe

Rather than re-run Molmo2's full multimodal training, it builds on the released Molmo2-4B mid-training checkpoint in two stages:
- **Stage 1 (specialize):** 20K steps on the embodied corpus + 8% Tulu-3 text (to preserve language competence). Pointing, video QA, and multi-image reasoning improve sharply.
- **Stage 2 (rehearse):** 1.5K steps interleaving the embodied corpus with Molmo2's original multimodal data. A sweep of the embodied/general split finds **p=0.5** is the best Pareto trade-off; longer 16,384-token sequences accommodate long multi-image/video examples.

## Reported numbers

- **13 embodied-reasoning benchmarks** (Point-Bench, RefSpatial, RoboSpatial, Where2Place, BLINK, CV-Bench, ERQA, EmbSpatial, MindCube, SAT, OpenEQA, VSI-Bench): **63.8% overall avg** — best open-weight on **9 of 13**.
- Beats runner-up **Gemini-ER 1.5 Thinking** (61.3) by 2.5, and surpasses **GPT-5** (57.9) and **Gemini 2.5 Pro** (57.1).
- **+17 points over its Molmo2 base** (46.8 → 63.8).
- **+6.0** LIBERO-Long over Molmo2 as a discrete-action backbone (ablation, before any continuous action expert).

## Related

- [MolmoAct2](molmoact2.md) — the VLA built on Molmo2-ER; the reason this entity exists.
- [Molmo](molmo.md) — the VLM lineage; Molmo2 is the base Molmo2-ER fine-tunes from.
- [VLA models](../concepts/learning/vla-models.md) — VLM-backbone taxonomy.
- [Chain-of-thought](../concepts/learning/chain-of-thought.md) — pointing / spatial CoT as the bridge from language to action.

## Open questions

- **Molmo2 primary (Clark et al. 2026) not ingested** — the base VLM's exact architecture, scale, and pretraining data are only summarized via the MolmoAct2 paper.
- How much of Molmo2-ER's 13-benchmark lead is pointing-specific (Ai2's signature capability) vs. broad spatial reasoning?

## Mentioned in

- [MolmoAct2 paper (Fang, Duan et al. 2026)](../sources/molmoact2-paper.md) — the primary source.
- [CaP-X paper](../sources/cap-x-paper.md) — Molmo 2 is one of CaP-Gym's perception primitives, providing open-vocabulary pointing alongside SAM3.
- [MolmoAct2-SO100_101 model card](../sources/molmoact2-so100-101-model-card.md) — restates the architecture independently of the paper: a flow-matching continuous action expert "conditions on the VLM key-value cache through a per-layer connection" on top of Molmo2-ER.
- [MolmoAct2 GitHub repo](../sources/molmoact2-github-repo.md) — Molmo2-ER is released as a standalone base checkpoint.

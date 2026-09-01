---
title: Physion-Eval
type: entity
subtype: benchmark
created: 2026-08-31
updated: 2026-08-31
sources: 1
tags: [physion-eval, benchmark, world-model-evaluation, physical-realism, video-generation, mllm-critic, human-annotation, egocentric, physion-labs]
---

**Physion-Eval** — a benchmark of **expert human reasoning** for diagnosing physical-realism failures in AI-generated video. 10,990 adjudicated reasoning traces over 12,718 generated videos from five TI2V models, spanning 22 physical categories across egocentric and exocentric viewpoints. Released by **Physion Labs** with Stanford / MIT / Harvard / Character AI co-authors ([paper](../sources/physion-eval-paper.md), March 2026); dataset at `huggingface.co/datasets/PhysionLabs/Physion-Eval`.

Distinct from most of the [world-model evaluation](../concepts/world-models/world-model-evaluation.md) landscape in that its ground truth is **people, not a metric or a model judge** — and its most consequential result is about the judges rather than the generators.

## What it measures

Each generated video is a "twin" of a real clip depicting a clear physical process — the real video's caption and first non-black frame are the conditioning inputs. Annotations carry four parts: **glitch presence**, **temporal grounding at 0.1 s precision**, a **taxonomy category**, and a **natural-language explanation** of the violated principle, plus a 1–5 severity score.

Taxonomy: contact/interaction failures, object-permanence violations, temporal-coherence breakdowns, causal-sequence violations, force-and-motion inconsistencies, material/state inconsistencies, geometric/collision violations, and others.

## Headline numbers

- **83.3% exocentric / 93.5% egocentric** of generated videos contain ≥1 human-identifiable physical glitch, at 1.28–1.56 glitches per video and mean severity 3.10–3.32.
- **Untrained humans beat every MLLM critic tested.** Youden's J: humans 24.9–37.1% (exo) and 48.4–61.8% (ego); best of ten critics 19.1% and 9.8%. Gemini 3.0 Pro misses >74.4% (exo) / >90.1% (ego) of clearly-glitched videos.
- **Neither more frames nor more "thinking" closes the gap** — denser temporal sampling is non-monotonic and sometimes *worse*; explicit reasoning moves J by <2.0 points.
- **The open-source model wins egocentric.** Wan 2.2 has the lowest egocentric failure rate (83.5%) while Sora 2, Kling 2.5 and Veo 3.1 Fast all sit at 96–97.5%.

## Why it matters to this wiki

The [world-model evaluation](../concepts/world-models/world-model-evaluation.md) page traces a progression from *how it looks* toward *what it is good for*. Physion-Eval opens a third axis — *can the evaluator even see the failure?* — and answers no for the current automated critics. That converges from a different direction on [WorldArena](worldarena.md)'s finding that its perceptual score correlates only **r = 0.360** with action-planning utility: **the measurement layer is a weaker link than the models are.**

It also puts a number on something several synthetic-data pipelines in this wiki assume away. [DreamGen](dreamgen.md) and [Cosmos](nvidia-cosmos.md)-style pipelines fine-tune a video model and train policies on its rollouts; Physion-Eval says those rollouts violate physics in the large majority of physics-critical clips. Whether policies inherit that is unmeasured.

## Limits

Single dominant physical interaction per scenario; visually observable cues only (force, energy, entropy inferred only indirectly); annotation noise expected, since perceptual physical realism is partly subjective. Audio is stripped, so audio-visual physical cues are out of scope.

> [!note] Not the 2021 Physion
> The name echoes **Physion** (Bear et al., 2021), a physical-*prediction* benchmark comparing humans and models on future-state prediction. Physion-Eval is a different task — diagnosing realism failures in *generated* video — with a different population and metric. Neither Physion nor Physion++ is ingested here.

## Related

- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — the landscape page it joins.
- [WorldArena](worldarena.md) / [WorldRoamBench](worldroambench.md) — the wiki's other two ingested world-model benchmarks; both measure utility and stability, neither measures human detectability.
- [Veo](veo.md) — Veo 3.1 Fast is one of the five generators measured.
- [Jiajun Wu](jiajun-wu.md) — senior author; the recurring name at this wiki's measurement end.

## Mentioned in

- [Physion-Eval paper](../sources/physion-eval-paper.md)

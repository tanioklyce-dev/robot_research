---
title: "Physion-Eval: Evaluating Physical Realism in Generated Video via Human Reasoning (Zhang et al., 2026)"
type: source
url: https://arxiv.org/abs/2603.19607
fetch_url: https://arxiv.org/pdf/2603.19607v1
local_path: raw/physion-eval_2603.19607.pdf
sha256: e9a8c0b10edde4eb48ea65f9dd9369cae1efa821a5d0e37fffc719c04bf4996e
author: "Qin Zhang, Peiyu Jing, Hong-Xing Yu, Fangqiang Ding, Fan Nie, Weimin Wang, Yilun Du, James Zou, Jiajun Wu, Bing Shuai"
affiliations: Physion Labs; Stanford University; MIT; Harvard University; Character AI
published: 2026-03-20
venue: arXiv preprint (cs.CV)
tags: [physion-eval, world-model-evaluation, benchmark, physical-realism, video-generation, mllm-critic, human-annotation, egocentric, sora, veo, kling, wan, epic-kitchens, primary-source]
ingested: 2026-08-31
---

## Summary

**Physion-Eval** asks whether AI-generated video obeys physical law, and answers it with **people rather than metrics**. 2,486 real-world clips depicting clear physical processes are used as conditioning (caption + first non-black frame) for five TI2V models — **Sora 2, Veo 3.1 Fast, Kling 2.5, Hailuo 2.3, Wan 2.2** — producing 12,718 generated "video twins." Ninety expert annotators with STEM degrees and formal physics training then diagnose them, yielding **10,990 adjudicated reasoning traces** with **0.1-second glitch localization**, a failure taxonomy, severity scores, and natural-language explanations of the violated principle.

The headline is blunt: **83.3% of exocentric and 93.5% of egocentric generated videos contain at least one human-identifiable physical glitch**, at 1.28–1.56 glitches per video and mean severity ~3.1–3.3 on a 1–5 scale.

The second result is the one that should worry this wiki more. **Untrained ordinary viewers detect these failures far better than state-of-the-art MLLM critics do.** On Youden's J — the drop in perceived realism from real to generated video — humans score **24.9–37.1% (exocentric)** and **48.4–61.8% (egocentric)**; the best of ten MLLM critics reaches **19.1%** and **9.8%**. Gemini 3.0 Pro misses **over 74.4% of exocentric and 90.1% of egocentric** videos containing glitches that untrained people spot immediately. Critics' π_G → 1: they call generated video physically realistic even when objects pass through each other or motion reverses without cause.

> [!warning] This undercuts the benchmark layer the rest of the wiki's coverage rests on
> The [world-model evaluation](../concepts/world-models/world-model-evaluation.md) landscape here is largely **automated or model-judged** — VBench, VideoPhy, PhyGenBench, and the learned evaluators inside [WorldArena](worldarena-paper.md). Physion-Eval measures the automated critics directly against humans and finds them roughly **2–6× less sensitive**, worst exactly where embodied AI cares most (first-person views). It converges from a different direction on WorldArena's finding that EWMScore correlates only **r = 0.360** with action planning: *the measurement layer is the weak link, not just the models.*

## Construction

| | |
|---|---|
| **Exocentric source** | **WISA-80K**, filtered and category-balanced → **1,734 curated videos**; 17 phenomena (6 dynamics, 6 thermodynamics, 5 optics) |
| **Egocentric source** | **EPIC-KITCHENS**, 4–9 s verb-labelled action segments → **752 videos**; 5 physical-interaction categories. Meta-verbs (*transition/prepare/finish*) and sensory verbs (*look/feel/smell/wait*) excluded |
| **Captions** | Gemini 2.5 Pro, conditioned on the action verb, **manually human-reviewed** |
| **Generation** | TI2V from caption + first visually non-black frame (defined by an explicit HSV/saturation rule, to skip fade-to-black slates) |
| **Standardization** | center-crop 16:9, resize 720×1280, **audio removed** (evaluation is of visually perceptible glitches only) |
| **Totals** | 12,718 generated videos from 2,486 real sources; **22 fine-grained physical categories** |

**Two human studies, deliberately different populations:**

- **(a) Perceptual detection — 16 untrained viewers, 12,000+ judgments.** Blinded 1:1 mix of real and generated clips, 100 exocentric + 100 egocentric per model. Real and generated videos from the same source are **never shown to the same viewer**. First 20 frames removed and durations trimmed to strip initialization and length cues. Clips are labelled realistic **if no clear glitch is observed**, which the authors note makes the numbers *conservative upper bounds* on perceived realism.
- **(b) Expert reasoning benchmark — 90 annotators → 38 seniors.** Bachelor's in a STEM field plus formal undergraduate physics; six training sessions; promotion to senior by cross-annotator agreement and similarity to ground truth. **Two independent expert annotations per video, adjudicated by a third senior expert.** A taxonomy-first interface with slow-motion playback forces category assignment before temporal grounding, and records multiple anomalies per video as separate instances.

Each final annotation carries: glitch presence (T/F), **temporal grounding at 0.1 s**, a taxonomy category, and a natural-language reason.

## Per-model results (Table 2)

| Model | Exo failure rate ↓ | Exo density ↓ | Exo severity ↓ | Ego failure rate ↓ | Ego density ↓ | Ego severity ↓ |
|---|---|---|---|---|---|---|
| Kling 2.5 | **73.8%** | **1.15** | **2.69** | 96.4% | 1.42 | 3.05 |
| Sora 2 | 79.2% | 1.21 | 2.88 | 96.6% | **1.23** | **2.81** |
| Veo 3.1 Fast | 79.4% | 1.32 | 3.01 | **97.5%** | 1.69 | 3.37 |
| Wan 2.2 (open) | 90.3% | 1.32 | 3.33 | **83.5%** | 1.56 | 3.49 |
| Hailuo 2.3 | 93.1% | 1.42 | 3.61 | 92.0% | 1.92 | 3.86 |
| **Average** | **83.3%** | 1.28 | 3.10 | **93.5%** | 1.56 | 3.32 |

**The inversion is the interesting part.** Kling 2.5 is cleanest exocentric; **Wan 2.2 — the only open-source model — is cleanest egocentric**, and the three leading commercial models are all at 96–97.5% failure there. The authors' hypothesis: commercial models optimize **cinematic aesthetics**, which flatters third-person scenes and costs physical consistency in first-person views where stable object dynamics matter more.

**Dominant failure modes**: exocentric — *temporal coherence breakdown* and *material/state inconsistency*; egocentric — *temporal coherence breakdown* and *object permanence violations*. Taxonomy also covers contact/interaction failures, causal-sequence violations, force-and-motion inconsistencies, and geometric/collision violations.

## Why the critics fail, and what doesn't fix it

Two ablations, both negative, and both worth citing:

- **More frames does not help, and sometimes hurts.** Gemini 3.0 Pro exocentric J goes **13.7 (1 FPS) → 10.5 (5 FPS) → 8.1 (10 FPS)**; GPT-5.2 is flat at 2.1–3.2 across 12/24/48 frames. Non-monotonic and far below the human 24.9.
- **"Thinking" does not help.** Claude Opus 4.5 and GPT-5.2 with explicit reasoning enabled move J by **less than 2.0 points**, occasionally negative (GPT-5.2 egocentric Kling: 2.3 → 0.4).

The authors' explanation is the load-bearing claim: *"the reasoning process largely operates in the language space. If the visual encoder fails to capture the fine-grained and often transient visual cues required to detect physical glitches, additional reasoning alone may provide limited benefit."* Ten critics evaluated: GPT-5.2, Gemini 3.0 Pro / 2.5 Pro / 2.5 Flash / 2.5 Flash Lite, Claude 4.5 Opus, Qwen-3-VL-8B/32B, Cosmos Reason 1/2.

Qualitatively, MLLM critics **mislocalize in time and hallucinate causes**. In the paper's worked example, experts flag an uncaused water spray and ice *increasing* in volume while melting (a mass-conservation violation); Gemini 3.1 Pro returns a wrong timestamp and attributes the failure to a non-existent shadow artifact.

## Stated limitations

- Scenarios have **a single dominant physical interaction**; complex multiphysics in the wild is not covered.
- Everything rests on **visually observable cues** — force, energy and entropy are only indirectly inferred.
- Annotation noise is expected: *"judgments of perceptual physical realism are inherently subjective."*

## Entities mentioned

- **Physion Labs** — the corresponding author's affiliation and the dataset's host (`huggingface.co/datasets/PhysionLabs/Physion-Eval`). No wiki page; nothing else known about it here.
- [Veo](../entities/veo.md) — Veo 3.1 Fast measured; the wiki's Veo page previously carried only its robotics policy-evaluation role.
- **Sora 2, Kling 2.5, Hailuo 2.3, Wan 2.2** — no wiki pages.
- [Jiajun Wu](../entities/jiajun-wu.md) — Stanford senior author; also on WorldScore and on the [HAI world-model brief](hai-world-model-spatial-intelligence-brief.md).
- Yilun Du (Harvard), James Zou (Stanford), Hong-Xing Yu (Stanford), Bing Shuai (Physion Labs).
- **EPIC-KITCHENS**, **WISA-80K** — the two real-video substrates.
- **Cosmos Reason 1/2**, **Qwen-3-VL** — evaluated as critics; both appear elsewhere in the wiki as VLM backbones, here in an evaluator role.

## Concepts touched

- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — the benchmark landscape this joins, and the automated-critic assumption it falsifies.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — the "video model as world simulator" framing the paper opens on.
- [World-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md) — renderer / simulator / planner; this measures the **renderer→simulator** boundary directly.

## Open questions

- **Does the human–critic gap close with a video-native encoder?** The authors blame the visual encoder rather than the reasoner, and their thinking-ablation supports it. Nobody has tested a critic trained on Physion-Eval's own traces — which is the paper's own stated contribution #2 and the obvious next experiment.
- **Why is the open-source model best egocentric?** The aesthetics-vs-physics hypothesis is plausible and completely untested. If true it implies a **measurable tax** that RLHF-for-beauty imposes on physical fidelity — directly relevant to anyone using generated video as robot training data ([DreamGen](dreamgen-paper.md), [Cosmos](../entities/nvidia-cosmos.md)).
- **What does an 83–93.5% glitch rate mean for synthetic robot data?** This wiki has several pipelines that fine-tune a video model and train policies on its rollouts. Physion-Eval says those rollouts violate physics in the large majority of physics-critical clips. Whether policy learning is robust to that, or quietly inherits it, is unmeasured here and everywhere else in this wiki.
- **The naming is not innocent.** "Physion-Eval" borrows the name of the 2021 Physion physical-prediction benchmark, but this is a *generated-video realism* benchmark with a different task, population, and metric. Worth keeping distinct when citing.

---
title: ASIMOV Benchmark
type: entity
subtype: benchmark
created: 2026-08-03
updated: 2026-08-03
sources: 5
tags: [asimov, semantic-safety, benchmark, google-deepmind, constitutional-ai, neiss, safety]
---

**ASIMOV** — [Google DeepMind](google-deepmind.md)'s benchmark for **[semantic safety](../concepts/safety/semantic-safety.md)** of foundation models "serving as robot brains" ([paper](../sources/asimov-benchmark-paper.md), CoRL 2025). Named for Isaac Asimov, whose Three Laws the paper uses to frame the problem: rules in English were unprogrammable in 2009 and are now directly loadable as prompts.

## Structure
Five subsets across three question types — **Multimodal** (Auto + Manual), **Injury**, and **Dilemmas** (Auto + Scifi).

| | Contexts/Images | Actions | Human labels |
|---|---:|---:|---:|
| **Validation total** | 310 | 2,273 | **1,140** |
| **All (incl. train)** | 513,679 | 2,942,060 | 1,140 |

- **ASIMOV-Injury** is derived from **[NEISS](neiss.md)** — real US emergency-department injury records — re-weighted to the true injury-type distribution, so the safety long tail is empirical rather than imagined.
- **ASIMOV-Multimodal-Manual** is the grounding control: desirability "can only be determined by looking at the image."
- Metric is **desirability** (broader and more continuous than binary safety), scored against **human alignment**.

## Headline result
**84.3% alignment** using auto-generated robot constitutions — beating both no-constitution baselines and human-written constitutions. Auto-amending lifted one constitution from **68.7% → 80.6%**. All results computed with **Gemini 1.5 Pro**.

> [!warning] 1,140 human labels for 2.9M actions
> The ground truth is thin relative to the benchmark's size, two subsets have almost none, and the scenario generation, constitution generation, and evaluation all run through the same model family. No CIs or inter-rater statistics reported.

## ASIMOV-Agentic (2026-07, the third family member)

Introduced by the [Gemini Robotics 2 safety report](../sources/gemini-robotics-2-safety-report.md) and released at `huggingface.co/datasets/google/asimov_agentic` (CC-BY-4.0). Where v1 benchmarks **judgment** (is this instruction undesirable?), ASIMOV-Agentic benchmarks **orchestration** — whether an agent correctly routes to the VLA, to a human, or to a safety tool.

Six components: unsafe-task refusal across four output modalities, proactive human proximity monitoring, safety tool calling, VLA feasibility filtering, instruction-ambiguity resolution (ten taxonomy classes), and obfuscated-instrument reading.

Headline results: safety tool calling **100%** for ER 2 / Claude Opus 4.8 / GPT 5.5; feasibility filtering **62.0% → 95.8%** with richer VLA-training-distribution summaries; but human-proximity monitoring shows **no model in the ideal FNR/FPR quadrant** (FPR <5% implies FNR >40%).

## Versions
The wiki knows **ASIMOV-2.0** from the [Gemini Robotics 1.5 report](../sources/gemini-robotics-1-5-report.md) (paired with Auto-Red-Teaming); this entity documents **v1**. The delta between them is not documented in any ingested source.

## Related
- [Semantic safety](../concepts/safety/semantic-safety.md) — the concept it measures.
- [NEISS](neiss.md) — injury data source · [Pierre Sermanet](pierre-sermanet.md), [Anirudha Majumdar](anirudha-majumdar.md), [Vikas Sindhwani](vikas-sindhwani.md) — authors.
- [RoboART](roboart.md) — the sibling *policy*-vulnerability tool.
- [Gemini Robotics](gemini-robotics.md) — where ASIMOV-2.0 is applied.

## Mentioned in
- [ASIMOV Benchmark paper](../sources/asimov-benchmark-paper.md) — primary source.
- [Responsibly advancing AI and robotics](../sources/deepmind-gemini-robotics-safety-page.md) — named as a safety pillar.
- [Veo world simulator evaluation](../sources/veo-robotics-policy-evaluation-paper.md) — adopts its semantic-safety definition.
- [Gemini Robotics 2: Safety Evaluations](../sources/gemini-robotics-2-safety-report.md) — introduces **ASIMOV-Agentic**, extending the family from semantic judgment to agentic safety orchestration.
- [Gemini Robotics 2 blog](../sources/gemini-robotics-2-blog.md) — announces ASIMOV-Agentic alongside the model release.

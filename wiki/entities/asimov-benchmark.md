---
title: ASIMOV Benchmark
type: entity
subtype: benchmark
created: 2026-08-03
updated: 2026-08-03
sources: 3
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

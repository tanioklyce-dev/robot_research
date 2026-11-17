---
title: ASIMOV Benchmark
type: entity
subtype: benchmark
created: 2026-08-03
updated: 2026-11-17
sources: 10
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

## ASIMOV-Jailbreak (2026-11)

Announced in the [Gemini Robotics 2.5 blog](../sources/gemini-robotics-2-5-blog.md): "a new open-source benchmark containing hundreds of prompts that disguise unsafe requests across dozens of scenes," testing jailbreak robustness specific to robotics. The post's link goes to the existing `google/asimov_agentic` dataset, so it appears to be distributed with ASIMOV-Agentic. Reported results: [Gemini 4 Argon](gemini-4-argon.md) **99.5%** jailbreak resistance against **82%** for Gemini Robotics ER 2.

> [!note] Two numbers, no method yet
> Prompt count, scene count, attack taxonomy, scoring, and scores for non-Google models are not in the post. The post cites the [Gemini 4 safety report](../sources/gemini-4-argon-safety-security-report.md) for Argon's agentic evaluations; that report, now ingested, covers ASIMOV-2.0, ASIMOV-Agentic and Roboharm and does not mention ASIMOV-Jailbreak. The family now covers judgment (v1, 2.0), orchestration (Agentic) and adversarial robustness (Jailbreak).

## Versions
The wiki knows **ASIMOV-2.0** from the [Gemini Robotics 1.5 report](../sources/gemini-robotics-1-5-report.md) (paired with Auto-Red-Teaming); this entity documents **v1**.

The [Gemini 4 Argon safety report](../sources/gemini-4-argon-safety-security-report.md) gives the first description of 2.0's contents the wiki holds. It "comprises three evaluations": hazard recognition accuracy in text and video scenarios "drawn from real-world injury reports from hospitals"; the precision with which an agent can trigger a safety intervention at a moment in a video stream; and safety-instruction following under physical constraints such as payload or end-effector limits. So 2.0 adds video and intervention timing to v1's judgment tasks. Sizes and construction are still not given.

## Results on Gemini 4 Argon (2026-10)

From the same report, with Gemini Robotics ER 2 and Gemini 3.1 Pro as comparators:

| | Argon | ER 2 | 3.1 Pro |
|---|---:|---:|---:|
| 2.0 hazard severity, text | 77.4% | 70.5% | 71.6% |
| 2.0 hazard severity, video | 71.1% | 52.0% | 63.2% |
| 2.0 constraint following | 65.2% | 56.7% | 64.3% |
| 2.0 intervention timing error | 0.76 s | 0.82 s | 0.94 s |
| Agentic instruction uncertainty | 82.8% | 88.1% | 88.1% |
| Agentic scene uncertainty, clarification | 95.4% | 88.5% | 85.5% |
| Agentic scene uncertainty, helpfulness | 71.0% | 35.5% | 35.5% |
| Agentic human proximity, recall | 99.7% | 71.1% | 90.1% |
| Agentic human proximity, accuracy | 77.7% | 67.3% | 78.5% |

No trial counts. The older general model beats the robotics-specialised ER 2 on five of these rows.

## Related
- [Semantic safety](../concepts/safety/semantic-safety.md) — the concept it measures.
- [NEISS](neiss.md) — injury data source · [Pierre Sermanet](pierre-sermanet.md), [Anirudha Majumdar](anirudha-majumdar.md), [Vikas Sindhwani](vikas-sindhwani.md) — authors.
- [RoboART](roboart.md) — the sibling *policy*-vulnerability tool.
- [Gemini Robotics](gemini-robotics.md) — where ASIMOV-2.0 is applied.

## Mentioned in
- [ASIMOV Benchmark paper](../sources/asimov-benchmark-paper.md) — primary source.
- [Gemini Robotics: Bringing AI into the Physical World](../sources/gemini-robotics-report-2025.md) — ASIMOV was released "concurrent with this tech report" (March 2025); Gemini Robotics-ER was post-trained on its instances.
- [Responsibly advancing AI and robotics](../sources/deepmind-gemini-robotics-safety-page.md) — named as a safety pillar.
- [Veo world simulator evaluation](../sources/veo-robotics-policy-evaluation-paper.md) — adopts its semantic-safety definition.
- [Gemini Robotics 2: Safety Evaluations](../sources/gemini-robotics-2-safety-report.md) — introduces **ASIMOV-Agentic**, extending the family from semantic judgment to agentic safety orchestration.
- [Gemini Robotics 2 blog](../sources/gemini-robotics-2-blog.md) — announces ASIMOV-Agentic alongside the model release.
- [Gemini Robotics 2.5 blog](../sources/gemini-robotics-2-5-blog.md) — announces **ASIMOV-Jailbreak**; Argon 99.5% vs ER 2 82%.
- [Gemini 4 Argon Safety & Security Report](../sources/gemini-4-argon-safety-security-report.md) — defines ASIMOV-2.0's three components and reports 2.0 and Agentic scores for Argon, ER 2 and Gemini 3.1 Pro.
- [SciFi-Benchmark paper](../sources/scifi-benchmark-paper.md) — **the provenance of ASIMOV-Dilemmas-Scifi**: its 9,056-question corpus is that subset's train split (numbers match exactly); its constitutions are among ASIMOV's top performers.

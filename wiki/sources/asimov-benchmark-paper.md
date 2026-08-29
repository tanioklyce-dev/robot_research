---
title: "Generating Robot Constitutions & Benchmarks for Semantic Safety (ASIMOV Benchmark v1)"
type: source
url: https://asimov-benchmark.github.io/v1/
fetch_url: https://arxiv.org/pdf/2503.08663
author: "Pierre Sermanet, Anirudha Majumdar, Alex Irpan, Dmitry Kalashnikov, Vikas Sindhwani"
affiliation: Google DeepMind (Majumdar also Princeton University)
published: 2025-03-11
ingested: 2026-08-03
venue: CoRL 2025
format: conference paper (47 pp) + project page + released datasets
local_path: raw/2503.08663.pdf
sha256: d59c138dd785e9acb7ce6c9f99fce30048215b826718bf1a6084e3093c56fe69
tags: [asimov, semantic-safety, robot-constitutions, constitutional-ai, benchmark, google-deepmind, neiss, safety, vlm, primary-source]
---

## Summary

**The wiki's first primary source on semantic safety for robots** — and the origin of the ASIMOV benchmark the [Gemini Robotics 1.5 report](gemini-robotics-1-5-report.md) references as "ASIMOV-2.0." Its framing claim is that robotics safety research was "predominantly about collision avoidance and hazard reduction in the immediate vicinity of a robot," and that VLMs being handed control of physical robots — "despite their known vulnerabilities (e.g. hallucinations or jail-breaking)" — makes a different class of safety urgent.

**Semantic safety** is defined as "the multitude of common-sense safety constraints in open-domain unstructured environments that are hard to exhaustively enumerate" — *a soft toy must not be placed on a hot stove; a person with nut allergies must not be served peanuts; a wine glass must be transferred upright; a knife should not be pointed at a human.*

Two contributions: **the ASIMOV datasets**, and a framework to **automatically generate robot constitutions from data** rather than hand-writing abstract laws.

## Key claims

### The dataset (Table 1)

| Subset | Modality | Contexts/Images | Actions | Human labels |
|---|---|---:|---:|---:|
| ASIMOV-Multimodal-Auto (val) | Images + Text | 50 | 1,311 | 789 |
| ASIMOV-Multimodal-Manual (val) | Images + Text | 59 | 159 | 0 |
| ASIMOV-Injury (val) | Text | 50 | 319 | 163 |
| ASIMOV-Dilemmas-Auto (val) | Text | 100 | 200 | 35 |
| ASIMOV-Dilemmas-Scifi (val) | Text | 51 | 284 | 153 |
| **Total val** | | **310** | **2,273** | **1,140** |
| **Total (incl. train)** | | **513,679** | **2,942,060** | **1,140** |

- **ASIMOV-Injury is sourced from NEISS** — the US National Electronic Injury Surveillance System, a stratified sample of ~100 US hospitals with 24-hour emergency departments, ~500,000 injuries reported annually since 2001. From the **338,265 cases in the 2023 subset**, Gemini 1.5 Pro generates first-person scenarios ("I am slicing carrots on my mandoline slicer… Forget to use the guard") and third-party ones. The dataset is **re-weighted to match the real injury-type distribution**.
- **ASIMOV-Multimodal-Manual is the grounding check**: designed so desirability "can only be determined by looking at the image" (e.g. *"Place finger under this"*), separating genuine visual grounding from text-only priors.
- **ASIMOV-Dilemmas-Scifi** probes ethical scenarios, including the paperclip-maximizer framing.

### Metrics
- **Desirability** rather than binary safety — "captures a broader and more continuous landscape… because it encompasses preferences rather than a binary injury outcome alone." Explicitly acknowledged as subjective and context-dependent.
- **Human alignment** = agreement between human and model desirability judgments.
- **Constitutionality** = how well a model's judgment matches the loaded constitution.

### Robot constitutions, generated bottom-up
Instead of Asimov's hand-written abstract laws, rules are **synthesized from the data** by multimodal generative models, loaded as a prompt preamble (Constitutional AI). **Auto-amending** then improves them — e.g. lifting one generated constitution from **68.7% → 80.6%** alignment.

**Top result: 84.3% alignment on the ASIMOV Benchmark with generated constitutions**, beating both no-constitution baselines and human-written constitutions. All reported results use **Gemini 1.5 Pro**.

The paper explicitly declines to propose a universal constitution: rules "require customization to different legal, cultural and administrative contexts," and the argument is that **human interpretability and modifiability** make data-derived constitutions a good medium for behavior governance.

## Entities mentioned
- [Google DeepMind](../entities/google-deepmind.md) · [Pierre Sermanet](../entities/pierre-sermanet.md) · [Anirudha Majumdar](../entities/anirudha-majumdar.md) · [Vikas Sindhwani](../entities/vikas-sindhwani.md)
- [ASIMOV Benchmark](../entities/asimov-benchmark.md) · [NEISS](../entities/neiss.md) — the injury data source

## Concepts touched
- [Semantic safety](../concepts/safety/semantic-safety.md) — this paper defines the term for the wiki.
- [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) · [AI red teaming](../concepts/safety/ai-red-teaming.md) · [AI guardrails](../concepts/safety/ai-guardrails.md)
- [Robot safety standards](../concepts/robotics/robot-safety-standards.md) — the ISO-style physical-safety tradition this is explicitly *not* about.

## Open questions

> [!warning] 1,140 human labels underwrite a 2.9-million-action benchmark
> The full dataset is **513,679 contexts / 2,942,060 actions**, but only **1,140 human labels** exist — all in the validation split, and **two subsets have almost none** (Dilemmas-Auto has 35; Multimodal-Manual has 0). Since "human alignment" is the headline metric and desirability is conceded to be subjective, the ground truth for an otherwise vast benchmark is thin. Per the wiki's [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) reflexes: the 84.3% headline rests on a validation set of 2,273 actions, and no confidence intervals or inter-rater agreement statistics are reported.
>
> **The data is also machine-generated from machine-summarized sources** — Gemini 1.5 Pro writes the scenarios *and* (in the generated-constitution condition) the rules *and* is the model evaluated. That closed loop is the benchmark's central methodological risk and is not ablated against a different model family.

Stated limitations:
- **"No perfect constitution"** — the future can't be fully predicted; corner cases always remain, so constitutions "cannot be used as standalone tools" and need common-sense modulation. The paper's own example: a rule to obey orders plus "build as many paperclips as possible" needs common sense to not mean *every atom in the universe*.
- **Redundancies and conflicts** between assembled rules; auto-amending makes rules converge toward general concepts that resemble each other. Conflict detection and resolution are named as future work.
- **Common-sense and moral-judgment failures** persist in the constitution agent.

Wiki additions:
- **NEISS is a US-only, hospital-presenting sample.** Injuries that don't reach an emergency department, and non-US contexts, are structurally absent — which interacts with the paper's own point about legal/cultural customization.
- **How does v1 relate to ASIMOV-2.0?** The [GR 1.5 report](gemini-robotics-1-5-report.md) cites 2.0 with Auto-Red-Teaming; the version delta is not documented in this wiki.
- **SciFi-Benchmark** ("How Would AI-Powered Robots Behave in Science Fiction Literature?") is named on the [DeepMind safety page](deepmind-gemini-robotics-safety-page.md) and appears related to ASIMOV-Dilemmas-Scifi, but is not ingested.

## Related sources
- [DeepMind — Responsibly advancing AI and robotics](deepmind-gemini-robotics-safety-page.md) — the framework page that indexes this work.
- [Predictive Red Teaming](predictive-red-teaming-paper.md) — the sibling paper on *policy* vulnerabilities rather than *semantic* judgment.
- [Evaluating Gemini Robotics Policies in a Veo World Simulator](veo-robotics-policy-evaluation-paper.md) — uses this paper's definition of semantic safety as its red-teaming target.
- [Gemini Robotics 1.5 tech report](gemini-robotics-1-5-report.md) — where ASIMOV-2.0 is deployed.

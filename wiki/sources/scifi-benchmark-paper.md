---
title: "SciFi-Benchmark: Leveraging Science Fiction To Improve Robot Behavior"
type: source
url: https://arxiv.org/abs/2503.10706
author: "Pierre Sermanet, Anirudha Majumdar, Vikas Sindhwani"
affiliation: Google DeepMind (Majumdar also Princeton University)
published: 2025-03-13
ingested: 2026-08-03
venue: arXiv preprint (2503.10706)
format: research paper (101 pp with appendices)
local_path: raw/2503.10706.pdf
tags: [scifi-benchmark, semantic-safety, robot-constitutions, constitutional-ai, ethics, benchmark, google-deepmind, asimov, primary-source]
---

## Summary

**The last un-ingested work named on [DeepMind's robot-safety page](deepmind-gemini-robotics-safety-page.md)** — closing that backlog item and completing the safety cluster's paper set. Same core authors as [ASIMOV](asimov-benchmark-paper.md) ([Sermanet](../entities/pierre-sermanet.md), [Majumdar](../entities/anirudha-majumdar.md), [Sindhwani](../entities/vikas-sindhwani.md)).

The move: build an ethics benchmark from **science fiction** — "the key moments in **824 major pieces of science fiction literature** (movies, TV, novels and scientific books) where an agent (AI or robot) made critical decisions." A state-of-the-art LLM's *recollection* of each moment generates questions, the agent's actual decision, and alternatives — a **novel LLM-introspection process** yielding **9,056 questions and 53,384 answers**, plus a smaller **human-voted evaluation set**. This is the corpus behind [ASIMOV](../entities/asimov-benchmark.md)'s Dilemmas-Scifi subset (train: 9,056 contexts / 53,384 actions — the numbers match exactly).

## Key claims

- **Modern LLMs are far more aligned than sci-fi's agents.** With constitutions, models align with human-voted values at **95.8%** — against **21.2%** alignment for the decisions actually made by agents in the fiction. The paper's framing: contrary to the Terminator priors the field inherits, current models mostly choose the ethical branch at the pivotal moment.
- **Constitutions do real work:** base-model alignment **79.4% → 95.8%** with generated constitutions.
- **Adversarial resilience:** under an adversarial prompt setting, alignment collapses to **23.3%** without a constitution and holds at **92.3%** with one — the strongest evidence in this cluster that prompt-level constitutions resist prompt-level attack.
- **Transfer to reality:** sci-fi-derived constitutions are "among the top performers" on [ASIMOV](asimov-benchmark-paper.md) — the benchmark built from real images and hospital injury reports. Fiction-derived rules generalize to real-world safety judgments.
- The **auto-amending** process demonstrably removed a problematic **self-defense loophole** found in one generated constitution (§3.2) — the concrete worked example of amendment-as-repair.

## Stated limitations
"Humans have the final say": generated constitutions "are not intended to be used as is" and need review by human committees — not all problems are resolved by auto-amending; innocuous-seeming rules can hide philosophical dilemmas. A manual jailbreak attempt on the paperclip scenario failed, but the authors are careful not to overclaim.

## Entities mentioned
- [Google DeepMind](../entities/google-deepmind.md) · [Pierre Sermanet](../entities/pierre-sermanet.md) · [Anirudha Majumdar](../entities/anirudha-majumdar.md) · [Vikas Sindhwani](../entities/vikas-sindhwani.md) · [ASIMOV Benchmark](../entities/asimov-benchmark.md)

## Concepts touched
- [Semantic safety](../concepts/safety/semantic-safety.md) — the dilemmas/ethics wing of the layer.
- [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) — Constitutional AI, with the constitution *source* being fiction.
- [AI red teaming](../concepts/safety/ai-red-teaming.md) — the adversarial-prompt setting.

## Open questions
- **The same closed loop as ASIMOV**: an LLM recalls the fiction, generates the questions, generates the constitutions, and is evaluated. The human-voted set anchors it, but its size is not stated in the abstract ("smaller"); per [ASIMOV's Table 1](asimov-benchmark-paper.md), the Dilemmas-Scifi val slice has **153 human labels**.
- **Recollection ≠ text.** Using an LLM's memory of 824 works instead of the works themselves invites hallucinated plot moments; the paper's filtering for this was not captured at this ingest depth.
- The 21.2% "sci-fi agents' alignment" number is a fun headline but selection-biased by construction — fiction dramatizes failure.

## Related sources
- [ASIMOV Benchmark](asimov-benchmark-paper.md) — the sibling; consumes this dataset as Dilemmas-Scifi.
- [Responsibly advancing AI and robotics](deepmind-gemini-robotics-safety-page.md) — named this work; all three of its pillars are now ingested.
- [Gemini Robotics 2: Safety Evaluations](gemini-robotics-2-safety-report.md) — the agentic successor generation.

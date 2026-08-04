---
title: "Responsibly advancing AI and robotics — Google DeepMind"
type: source
url: https://deepmind.google/models/gemini-robotics/responsibly-advancing-ai-and-robotics/
author: Google DeepMind
affiliation: Google DeepMind
published: 2025
ingested: 2026-08-03
venue: deepmind.google (Gemini Robotics safety page)
format: vendor safety-framework page
tags: [gemini-robotics, safety, semantic-safety, asimov, red-teaming, swiss-cheese-model, google-deepmind, iso-15066, vendor-source]
---

## Summary

DeepMind's public framing of robot safety, and — more usefully for this wiki — **the index to its robotics safety research program**. The page names three works, **all now ingested**: [ASIMOV](asimov-benchmark-paper.md), [SciFi-Benchmark](scifi-benchmark-paper.md), and [Predictive Red Teaming](predictive-red-teaming-paper.md).

## Key claims

### The three-layer "Swiss cheese" safety model

| Layer | What it covers |
|---|---|
| **Semantic safety** | Common sense in human-robot interaction — "they mustn't hand a boiling drink to a young child, or pass a very heavy box to a human" |
| **Physical safety** | Lower-level safety mechanisms integrated with VLA models; safe data collection and evaluation practice |
| **Operational safety** | Human-robot interaction safeguards — gestures, speech, actions aligned with Gemini safety policies |

The Swiss-cheese framing (independent imperfect layers whose holes shouldn't align) is standard in aviation and medical safety; its application here is the claim that **no single layer is expected to be sufficient** — which is consistent with [ASIMOV's](asimov-benchmark-paper.md) own admission that "constitutions cannot be used as standalone tools."

### Mechanisms
- **Continuous vulnerability search** — "systems that continuously search for vulnerabilities within our robotics models."
- **Thinking-based decision making.** Gemini Robotics 1.5 uses explicit reasoning for transparency: assessing object weight before lifting, identifying hazards (e.g. electric shock risk), detecting human proximity and pausing.

### Named research
- **ASIMOV-Benchmark** — "Generating Robot Constitutions & Benchmarks for Semantic Safety" → [ingested](asimov-benchmark-paper.md)
- **SciFi-Benchmark** — "Leveraging Science Fiction To Improve Robot Behavior" → [ingested 2026-08-03](scifi-benchmark-paper.md)
- **Predictive Red Teaming** — "Breaking Policies Without Breaking Robots" → [ingested](predictive-red-teaming-paper.md)
- The **Gemini Robotics 1.5 Tech Report**, for "scalable adversarial evaluations" → [ingested](gemini-robotics-1-5-report.md)

### Deployment posture
The framework "remains under research." Waitlist joiners are told: **"It's your responsibility to use our models (and any equipment) safely and appropriately."**

## Entities mentioned
- [Google DeepMind](../entities/google-deepmind.md) · [Gemini Robotics](../entities/gemini-robotics.md) · [ASIMOV Benchmark](../entities/asimov-benchmark.md) · [RoboART](../entities/roboart.md)

## Concepts touched
- [Semantic safety](../concepts/safety/semantic-safety.md) — the page is where DeepMind defines the layer publicly.
- [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) · [AI red teaming](../concepts/safety/ai-red-teaming.md) · [AI guardrails](../concepts/safety/ai-guardrails.md)
- [Robot safety standards](../concepts/robotics/robot-safety-standards.md) — the physical layer; the [GR 1.5 report](gemini-robotics-1-5-report.md) cites ISO 15066 alignment, which this page does not repeat.

## Open questions

> [!warning] The page describes 1.5, not 2
> Its worked example is **Gemini Robotics 1.5**, and the linked tech report is the 1.5 one — even though the [model page](deepmind-gemini-robotics-model-page.md) has moved to a **"2" generation**. Either this safety page has not been updated for GR 2, or the GR 2 safety story lives in the separate *Gemini Robotics 2: Safety Technical Report* the wiki has [backlogged](../backlog.md). **Do not read this page as describing GR 2's safety posture.**

- **No numbers.** No benchmark results, no evaluation counts, no incident data. The quantitative content is entirely in the three linked papers.
- **The formal-methods line is absent.** [Safely Learning Dynamical Systems](safely-learning-dynamical-systems-paper.md) shares an author ([Vikas Sindhwani](../entities/vikas-sindhwani.md)) with both named papers but does not appear in the public framing — so the "physical safety" layer is described without reference to the lab's own work on provable safe exploration.
- **"Continuously search for vulnerabilities" is unelaborated** — whether this is [RoboART](../entities/roboart.md), the [Auto-Red-Teaming](gemini-robotics-1-5-report.md) attacker/target/autorater game, or something else is not stated.
- **The liability framing is worth recording**: responsibility for safe use is explicitly assigned to the user, while the safety layers are described as research-stage. Compare the [guardrails thread](../syntheses/agents/guardrails-for-robot-agents.md), where the wiki has repeatedly found the enforcement layer to be the thin one.

## Related sources
- [ASIMOV Benchmark](asimov-benchmark-paper.md) · [Predictive Red Teaming](predictive-red-teaming-paper.md) · [Veo world simulator](veo-robotics-policy-evaluation-paper.md) · [Safely Learning Dynamical Systems](safely-learning-dynamical-systems-paper.md) — the research this page indexes (the last two implicitly).
- [Gemini Robotics 1.5 tech report](gemini-robotics-1-5-report.md) — ASIMOV-2.0, Auto-Red-Teaming, ISO 15066.
- [Gemini Robotics model page](deepmind-gemini-robotics-model-page.md) — the sibling product page, already on generation 2.

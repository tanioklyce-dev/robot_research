---
title: "Gemini Robotics — Google DeepMind model page"
type: source
url: https://deepmind.google/models/gemini-robotics/
author: Google DeepMind
affiliation: Google DeepMind
published: 2026-07-30
ingested: 2026-08-03
venue: deepmind.google (product / model page)
format: vendor model page
tags: [gemini-robotics, google-deepmind, vla, embodied-reasoning, on-device, whole-body-control, humanoid, multi-robot, apptronik, boston-dynamics, version-check, vendor-source]
---

## Summary

**This ingest's main result is a version discovery: the family has moved to a "2" generation that the wiki did not have.** The wiki's deepest Gemini Robotics source is the [GR 1.5 tech report](gemini-robotics-1-5-report.md), with **ER 1.6** known only as a Boston Dynamics productization variant. The current DeepMind model page lists **Gemini Robotics 2**, **Gemini Robotics ER 2**, and **Gemini Robotics On-Device 2** — a full generation ahead of everything on the [entity page](../entities/gemini-robotics.md).

As a source it is **thin**: a vendor product page with **no benchmark numbers, no success rates, no release dates, and no parameter counts**. Its value is the family structure, the access tiers, and the capability claims — which are checkable against the wiki's existing threads.

> [!warning] Attribution boundary
> Everything in **Key claims** below is from the DeepMind page itself. The **date (2026-07-30)**, the **~200-examples** figure, and the **Apollo 2** demonstration come from *secondary press coverage* found while dating the release, and are marked as such. The primary artifacts — a **Gemini Robotics 2 blog post** and a **Gemini Robotics 2: Safety Technical Report** — are **not yet ingested**.

## Key claims (from the page)

### Three models, three access tiers

| Model | What the page says |
|---|---|
| **Gemini Robotics 2** | "Our most advanced vision-language-action model (VLA) that converts vision and language input into motor control"; handles "a variety of tasks – even if it hasn't been trained on them before" |
| **Gemini Robotics ER 2** | "capable of reasoning within physical spaces to make detailed plans, coordinating with humans and other robots"; **public preview via Google AI Studio** |
| **Gemini Robotics On-Device 2** | "A lightweight version of our VLA model, **optimized to run locally on robotic hardware**" |

The VLA / embodied-reasoning split is unchanged from 1.5 — [GR-ER](../entities/gemini-robotics.md) remains the planner that emits tool calls, GR the policy that emits motor control. **On-Device is the structurally new tier.**

### Claimed capabilities
- **Whole-body control of humanoid robots**
- **"Advanced dexterity… like screwing in a light bulb and tying knots"**
- **Multi-robot collaboration and coordination**
- Adaptation to unfamiliar situations
- Compatible with **"any bi-arm robot in just a few hours"**

### Availability
- ER 2 in **public preview** through Google AI Studio.
- **100+ "trusted testers"** program for enterprise and startup partners; waitlist signup.
- Named partners: **[Agile Robots](../entities/agile-robots.md)**, **[Apptronik](../entities/apptronik-apollo.md)**, **[Boston Dynamics](../entities/boston-dynamics.md)** — all three already entities in this wiki.

## Entities mentioned
- [Google DeepMind](../entities/google-deepmind.md) · [Gemini Robotics](../entities/gemini-robotics.md)
- [Agile Robots](../entities/agile-robots.md) · [Apptronik Apollo](../entities/apptronik-apollo.md) · [Boston Dynamics](../entities/boston-dynamics.md)

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) · [Whole-body control](../concepts/robotics/whole-body-control.md) · [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md)
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — the GR / GR-ER split is the taxonomy's level-1-2 vs level-3 boundary, productized.

## Analysis

### "Any bi-arm robot in a few hours" — the honest version of a claim the wiki just flagged
Two days ago the wiki [flagged Waddle's](waddle-labs-introducing-waddle.md) "works with any arms, grippers, and camera setups **without new data collection**" as overstated, on the strength of [ASPIRE's](aspire-paper.md) admission that a predefined API bounds what an agent can express.

DeepMind's claim is the same shape but **materially weaker and better specified**: *hours*, not zero, and — per secondary coverage — **typically under 200 examples** for a new bi-arm embodiment. That is a fine-tuning claim, not a zero-shot one. **It is the version of "cross-embodiment generality" the wiki finds credible**, and it makes the Waddle framing look worse by comparison rather than better.

### On-Device 2 is the entry the wiki's edge thread has been waiting for
The [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) records that "almost no 2026-class VLA has an on-Jetson number," with [Cosmos 3 Edge](nvidia-cosmos3-edge-hf-blog.md)'s 15 Hz on Thor the only entry — and, as of today's [MolmoAct2 repo ingest](molmoact2-github-repo.md), MolmoAct2 ships **no Jetson support at all**. A first-party VLA "optimized to run locally on robotic hardware," motivated (per coverage) by "network latency or internet connectivity" constraints, is the third data point in that band.

**But the page publishes no rate, no hardware target, and no memory footprint**, so it cannot be placed on the ladder yet. That is the specific thing to look for in the tech report.

> [!note] A possible continuity worth watching, not asserting
> The [GR 1.5 report](gemini-robotics-1-5-report.md) recorded a stated weakness: **"dexterity ≈ prior generation."** GR 2 leads with dexterity claims (light bulbs, knots), while at least one press headline framed the release as still *"struggling with dexterity."* Whether 1.5's dexterity ceiling was actually lifted is a real question and the page does not answer it. Flagged, not concluded — the wiki has no primary evidence either way.

## Open questions
- **No numbers of any kind on the page.** Against the wiki's [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) standard this is anecdote-grade, exactly like the [Waddle](waddle-labs-introducing-waddle.md) ingest — with the difference that a tech report is known to exist.
- **On-Device 2's deployment envelope is the highest-value missing fact**: parameter count, memory footprint, target hardware, and control rate. Would go straight onto the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) and the [Jetson ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md).
- **Is there a GR 2 equivalent of Motion Transfer and Embodied Thinking** — the two mechanisms that carried the 1.5 report? Whole-body control is new framing; its relationship to Motion Transfer is unstated.
- **What happened to 1.6?** The wiki knows ER 1.6 as Boston Dynamics' AIVI-Learning engine. Whether 1.6 was a full family release or an ER-only increment is still unresolved, and now sits between two documented generations.
- **Apollo 2** (per coverage, the whole-body demonstration platform) is a version the [Apptronik Apollo](../entities/apptronik-apollo.md) entity does not have.

## Follow-ups (filed to [backlog](../backlog.md))
1. **Ingest the Gemini Robotics 2 blog post** (`deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/`) — the substantive primary announcement.
2. **Ingest the Gemini Robotics 2: Safety Technical Report** — would also extend the wiki's [ASIMOV / safety](../concepts/safety/ai-safety-alignment.md) thread, which currently ends at ASIMOV-2.0 in the 1.5 report.

## Related sources
- [Gemini Robotics 1.5 tech report](gemini-robotics-1-5-report.md) — the generation this supersedes; still the wiki's only substantive GR source.
- [Boston Dynamics × Gemini Robotics](bostondynamics-spot-gemini-robotics.md) — the ER 1.5/1.6 integration path.
- [Introducing Waddle](waddle-labs-introducing-waddle.md) — the cross-embodiment claim this one is the disciplined version of.

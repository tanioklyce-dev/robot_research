---
title: "Gemini Robotics 2 brings whole body intelligence to robots (DeepMind blog)"
type: source
url: https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
author: Google DeepMind
affiliation: Google DeepMind
published: 2026-07-30
ingested: 2026-08-03
venue: deepmind.google blog
format: model announcement with benchmark tables
tags: [gemini-robotics, gemini-robotics-2, vla, on-device, whole-body-control, dexterity, humanoid, multi-robot, apptronik, sharpawave, so-arm101, vendor-source]
---

## Summary

The substantive announcement of the **Gemini Robotics 2** generation (2026-07-30), and the source that finally puts numbers on it — the [model page](deepmind-gemini-robotics-model-page.md) ingested earlier today carried none. Three models: **Gemini Robotics 2** (VLA), **Gemini Robotics ER 2** (the "high-level brain"), and **Gemini Robotics On-Device 2** (efficient VLA for local execution).

**This retires the "wiki is a generation behind" warning** on the [Gemini Robotics](../entities/gemini-robotics.md) entity.

## Key claims

### Benchmarks — and they are unusually candid

**General whole-body manipulation** ([Apollo 2](../entities/apptronik-apollo.md) with Inspire hands):

| Task | Success |
|---|---:|
| Pick up from shelf | **76.3%** |
| Pick up from table | 68.4% |
| Pick up from floor | **45.7%** |

**Multi-finger dexterity** (Apollo with **[SharpaWave](../entities/sharpa-wave.md)** hands — five-fingered, **22 DoF**):

| Task | Success |
|---|---:|
| Unscrew bulb | **92%** |
| Tie trash bag | 44% |
| Ziplock | 40% |
| Screw bulb | **36%** |
| Dustpan | **32%** |

**Gripper dexterity** ([Franka](../entities/franka-panda.md) Duo):

| Task | Success |
|---|---:|
| Precise insertion tasks | **89.6%** |
| Diverse tool kitting | 78.9% |
| General pick and place | 74.2% |

> [!note] This answers a question the wiki was carrying — and the answer is "partly"
> The [GR 1.5 report](gemini-robotics-1-5-report.md)'s stated weakness was **"dexterity ≈ prior generation"**, and the wiki [flagged but declined to conclude](deepmind-gemini-robotics-model-page.md) whether GR 2 lifted that ceiling. The numbers say: **gripper work is strong (74–90%), multi-finger dexterous work is not (32–44% on four of five tasks).**
>
> The sharpest single data point is **unscrew bulb 92% vs screw bulb 36%** — the same object and hand, a **2.5× gap**, separating *removal* from *threaded insertion*. Alignment-under-constraint is where five-fingered manipulation still fails, and DeepMind published the unflattering half rather than only the 92%.

### Whole-body control
Humanoids "walk, crouch, stretch, and manipulate objects to clean up a cluttered room" — the worked example is retrieving a watering can and placing it on a shelf, requiring coordinated locomotion *and* manipulation. This is the generation's headline capability and is new relative to 1.5's Motion Transfer framing.

### Multi-robot collaboration
ER 2 "now supports inter-robot coordination" — different *types* of robot communicating "to solve complex workflows a single robot could not do alone."

### On-Device 2
"Fast adaptation to completely new robot embodiments with a few hours of data" — **typically fewer than 200 examples** — across robots with "drastically different shapes, sensors and degrees of freedom."

> [!note] The disciplined version of a claim the wiki flagged
> This is a **fine-tuning** claim, not zero-shot, and it is quantified. Compare [Waddle's](waddle-labs-introducing-waddle.md) "works with any arms, grippers, and camera setups **without new data collection**", which the wiki flagged as overstated. ~200 examples is a real number that a reader can plan around.

### Supported platforms
[Apptronik Apollo 2](../entities/apptronik-apollo.md) (with SharpaWave and Inspire hands), **Franka Duo** with Robotiq gripper, **Dexmate**, **[SO101](../entities/so-arm101.md)**, and **Trossen**.

> [!note] SO-101 is a first-class target
> A DeepMind frontier VLA family lists **SO101** among its supported platforms — the same low-cost arm class this wiki's own projects use ([XLeRobot](../entities/xlerobot.md), [LeKiwi](../entities/lekiwi.md)), and the same class [MolmoAct2 ships a checkpoint for](molmoact2-so100-101-model-card.md). Two independent frontier labs now target this hardware tier.

### Availability
- **ER 2** — Google AI Studio, plus private preview via Gemini Enterprise Agent Platform.
- **VLA and On-Device 2** — early-access partners by application.
- Trusted Tester program open.

### Safety
Introduces **ASIMOV-Agentic**, a benchmark for "agentic safety orchestration and uncertainty resolution." The model can "detect when humans are nearby, trigger safety tool calls and bring the robot to a safe stop if someone approaches too closely." Detailed in the [safety technical report](gemini-robotics-2-safety-report.md).

## Entities mentioned
- [Google DeepMind](../entities/google-deepmind.md) · [Gemini Robotics](../entities/gemini-robotics.md)
- [Apptronik Apollo](../entities/apptronik-apollo.md) (Apollo 2) · [SharpaWave](../entities/sharpa-wave.md) · [Franka Panda](../entities/franka-panda.md) (Franka Duo) · [SO-ARM101](../entities/so-arm101.md)
- [ASIMOV Benchmark](../entities/asimov-benchmark.md) — ASIMOV-Agentic is the new family member

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) · [Whole-body control](../concepts/robotics/whole-body-control.md) · [Semantic safety](../concepts/safety/semantic-safety.md)
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — ER 2 as the orchestrator tier
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — the ER/VLA split is levels 3 and 1–2, productized

## Open questions
- **On-Device 2's deployment envelope is still unpublished** — no parameter count, memory footprint, target hardware, or control rate. This was the backlog's "highest-value single fact" and **the blog does not supply it**; it remains the missing third entry in the on-device band of the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md).
- **No N anywhere.** Every percentage above lacks a trial count, so per the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) none of these is separable from its neighbours. The 92%-vs-36% bulb gap is large enough to survive almost any n; the 44/40/36/32 cluster is not.
- **No baselines.** Nothing is compared against GR 1.5, π0.5, or any external model, so "advanced dexterity" is unquantified as an improvement.
- **What is "Inspire hands" vs SharpaWave?** Two different hand vendors on the same Apollo 2, used for different benchmark tables — the reason for the split is unstated.
- **Was 1.6 a full family release or ER-only?** Still unresolved; the blog does not mention 1.6.

## Related sources
- [Gemini Robotics 2: Safety Evaluations](gemini-robotics-2-safety-report.md) — the companion technical report; ASIMOV-Agentic in detail.
- [Gemini Robotics model page](deepmind-gemini-robotics-model-page.md) — the numberless product page this supersedes.
- [Gemini Robotics 1.5 tech report](gemini-robotics-1-5-report.md) — the previous generation.

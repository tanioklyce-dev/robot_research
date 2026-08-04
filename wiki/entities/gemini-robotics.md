---
title: Gemini Robotics
type: entity
subtype: model
created: 2026-05-09
updated: 2026-08-03
sources: 7
tags: [gemini-robotics, google-deepmind, vlm, vla, embodied-reasoning, foundation-model]
---

**Gemini Robotics** — [Google DeepMind](google-deepmind.md)'s family of robotics-targeted foundation models, built on the Gemini multimodal model line.

> [!warning] The wiki is a generation behind (noted 2026-08-03)
> The [DeepMind model page](../sources/deepmind-gemini-robotics-model-page.md) now lists a **"2" generation** — **Gemini Robotics 2**, **Gemini Robotics ER 2**, and a structurally new **Gemini Robotics On-Device 2** — released **2026-07-30** (date from press coverage; the page itself is undated). Everything below is grounded in **1.5** (plus ER 1.6 as a productization variant).
>
> **Nothing on this page has been re-verified against GR 2**, and the model page carries no numbers, so the 1.5 figures below remain the wiki's only quantitative evidence. A **GR 2 blog post** and a **Gemini Robotics 2: Safety Technical Report** exist and are [backlogged](../backlog.md) — those are the ingests that would actually update this page.

## The "2" generation (structure only, no numbers)

| Model | Role | Access |
|---|---|---|
| **Gemini Robotics 2** | VLA — vision + language → motor control | Trusted testers (100+), waitlist |
| **Gemini Robotics ER 2** | Embodied reasoning — plans, coordinates with humans and other robots | **Public preview in Google AI Studio** |
| **Gemini Robotics On-Device 2** | Lightweight VLA "optimized to run locally on robotic hardware" | Trusted testers |

Claimed: whole-body humanoid control ("feet to fingertips", per coverage), advanced dexterity (screwing in a light bulb, tying knots), multi-robot collaboration, and compatibility with **"any bi-arm robot in just a few hours"** — reportedly under ~200 examples, i.e. a *fine-tuning* claim, not zero-shot. Named partners: [Agile Robots](agile-robots.md), [Apptronik](apptronik-apollo.md), [Boston Dynamics](boston-dynamics.md).

**On-Device 2 is the notable addition** — a first-party VLA built for local execution, which the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) has been short of data points for. No rate, hardware target, or footprint published yet.

---

The 1.5-generation family contains two distinct variants:

- **Gemini Robotics** — full vision-language-**action** model (VLA); emits low-level robot actions directly. Listed alongside [NVIDIA GR00T](nvidia-groot.md) and [Physical Intelligence π0/π0.6](physical-intelligence.md) on the [VLA models concept page](../concepts/learning/vla-models.md).
- **Gemini Robotics-ER** ("ER" = embodied reasoning) — vision-language model (VLM) that provides high-level reasoning over visual input and emits *tool calls*, not motor actions. Designed to be plugged into a robot's existing API (i.e. acts as the planner in an [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md), not as the policy). Versions 1.5 and 1.6 referenced below.

## Gemini Robotics 1.5 (primary report now ingested)

The [Gemini Robotics 1.5 tech report](../sources/gemini-robotics-1-5-report.md) is the wiki's first deep DeepMind-robotics source. It pairs **GR 1.5** (a multi-embodiment VLA controlling [ALOHA](aloha.md) 2 / bi-arm [Franka](franka-panda.md) / [Apollo](apptronik-apollo.md) humanoid with **one checkpoint**) and **GR-ER 1.5** (the embodied-reasoning orchestrator), both on **Gemini 2.5**. Three headline mechanisms:
- **Motion Transfer** — cross-embodiment recipe giving **zero-shot skill transfer** across dissimilar robots (success 0.40–0.58 where single-embodiment baselines are ~0).
- **Embodied Thinking** — "think before acting": interleaves actions with NL reasoning traces; lifts multi-step ALOHA progress 0.26→0.55, with emergent success-detection + error-recovery replanning.
- **Agentic orchestration** — GR-ER 1.5 orchestrator + GR 1.5 action model roughly **halves total failure (22% vs 44.5%)** vs a generic Gemini-2.5-Flash orchestrator; the biggest gain is planning. Lesson: dedicated embodied reasoning matters, not just a strong VLA + off-the-shelf VLM.
- **Safety**: ASIMOV-2.0 benchmark + Auto-Red-Teaming; ISO 15066 alignment. **Stated weakness: dexterity ≈ prior generation.**

## Gemini Robotics-ER (the variant most documented in the wiki)

### What it does
Takes a natural-language goal plus visual input from a robot's cameras, identifies relevant objects, and sequences calls to a tool library that the integrator exposes via the robot's SDK.

### Documented integration: Spot + ER 1.5 (Boston Dynamics hackathon, 2025)
- Two [Boston Dynamics](boston-dynamics.md) Spot-team engineers wired ER 1.5 into [Spot](spot.md) via a thin layer over the Spot SDK ([source](../sources/bostondynamics-spot-gemini-robotics.md)).
- Tools exposed: `GoTo`, `TakePicture`, object identification, `Pickup`, `PutDown`.
- Demo: shoes/cans cleanup in a residential living room from handwritten task lists.
- Quote: "Gemini Robotics functioned as both the operator and the tablet sending commands to the robot."
- Engineers report **prompt engineering still matters** — tool docstrings had to encode hardware-specific facts (e.g. that the gripper camera is the most informative initial view; that front cameras sit too low to photograph elevated surfaces).
- Safety property: "Gemini Robotics has strict boundaries in this scenario. It can't invent new capabilities or control Spot beyond what is available through the API." The SDK / tool schema is the safety surface — see [AI safety and alignment](../concepts/safety/ai-safety-alignment.md).

### Productization: AIVI-Learning + ER 1.6
Boston Dynamics' **AIVI-Learning** product is described as "the next evolution" powered by Gemini Robotics-ER 1.6, providing "a new level of visual intelligence" to [Spot](spot.md) and Orbit with automatic model upgrades ([source](../sources/bostondynamics-spot-gemini-robotics.md)).

## Position in the foundation-model landscape

- **Architecturally distinct from a VLA when used in -ER mode.** Gemini Robotics-ER is closer in spirit to GPT-4o-as-planner inside [stretch_ai](stretch-ai.md) or to [Qwen](qwen.md) driving [OpenClaw](openclaw.md) on a ROSOrin Pro: the model emits structured tool calls; classical perception/manipulation primitives execute them. Compare with [NVIDIA GR00T](nvidia-groot.md) (true VLA, emits actions) and the V-JEPA family (latent-prediction world models, not policies at all).
- **Two-product strategy is unusual.** Most foundation-model providers ship a single robotics offering. Google's split (full VLA *and* embodied-reasoner-with-tools) lets them serve both end-to-end research and integration-into-existing-robots use cases.
- **Hardware-agnostic ambitions.** The -ER variant explicitly does *not* assume a particular embodiment — anything with a camera and a callable API surface is a target.

## Related

- [Google DeepMind](google-deepmind.md) — developer.
- [Boston Dynamics](boston-dynamics.md) / [Spot](spot.md) — the documented integration partner in the wiki.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the design pattern Gemini Robotics-ER fits.
- [VLA models](../concepts/learning/vla-models.md) — where the *full* Gemini Robotics (not -ER) sits.
- [Embodied reasoning](../concepts/agents/llm-agent-architecture.md) — the framing Google uses for -ER; functionally a synonym for "LLM-agent planner with vision."

## Mentioned in

- [Gemini Robotics 1.5 tech report](../sources/gemini-robotics-1-5-report.md) — **primary technical source** (GR 1.5 VLA + GR-ER 1.5).
- [Tools for Your To Do List with Spot and Gemini Robotics (Boston Dynamics blog)](../sources/bostondynamics-spot-gemini-robotics.md)
- [DeepMind Gemini Robotics model page](../sources/deepmind-gemini-robotics-model-page.md) — the **2** generation (GR 2 / ER 2 / On-Device 2), access tiers, and partner list. No numbers.
- [Responsibly advancing AI and robotics](../sources/deepmind-gemini-robotics-safety-page.md) — the safety framework page. **Note it still describes GR 1.5**, not the 2 generation.
- [Veo world simulator evaluation](../sources/veo-robotics-policy-evaluation-paper.md) — 8 Gemini Robotics checkpoints evaluated in a generative simulator against 1600+ real evaluations.

## Open questions / TBD

- ~~Primary technical source not yet ingested~~ — filed 2026-07-04: [Gemini Robotics 1.5 report](../sources/gemini-robotics-1-5-report.md). (Exact model sizes / action-decoder details still undisclosed by DeepMind; appendices not in the PDF.)
- **ER 1.6** — the AIVI-Learning productization variant post-dates the 1.5 report; no dedicated source.
- **Open weights?** No; both variants appear to be closed / API-only.
- **Latency and cost.** Not documented in the BD blog; likely cloud-API-bound.
- **Other documented integrations besides Spot.** Apptronik (NVIDIA-aligned) has been mentioned in DeepMind press; needs a primary-source ingest.

---
title: Gemini Robotics
type: entity
subtype: model
created: 2026-05-09
updated: 2026-05-09
sources: 1
tags: [gemini-robotics, google-deepmind, vlm, vla, embodied-reasoning, foundation-model]
---

**Gemini Robotics** — [Google DeepMind](google-deepmind.md)'s family of robotics-targeted foundation models, built on the Gemini multimodal model line. The family contains at least two distinct variants:

- **Gemini Robotics** — full vision-language-**action** model (VLA); emits low-level robot actions directly. Listed alongside [NVIDIA GR00T](nvidia-groot.md) and [Physical Intelligence π0/π0.6](physical-intelligence.md) on the [VLA models concept page](../concepts/vla-models.md).
- **Gemini Robotics-ER** ("ER" = embodied reasoning) — vision-language model (VLM) that provides high-level reasoning over visual input and emits *tool calls*, not motor actions. Designed to be plugged into a robot's existing API (i.e. acts as the planner in an [LLM-agent architecture](../concepts/llm-agent-architecture.md), not as the policy). Versions 1.5 and 1.6 referenced below.

## Gemini Robotics-ER (the variant most documented in the wiki)

### What it does
Takes a natural-language goal plus visual input from a robot's cameras, identifies relevant objects, and sequences calls to a tool library that the integrator exposes via the robot's SDK.

### Documented integration: Spot + ER 1.5 (Boston Dynamics hackathon, 2025)
- Two [Boston Dynamics](boston-dynamics.md) Spot-team engineers wired ER 1.5 into [Spot](spot.md) via a thin layer over the Spot SDK ([source](../sources/bostondynamics-spot-gemini-robotics.md)).
- Tools exposed: `GoTo`, `TakePicture`, object identification, `Pickup`, `PutDown`.
- Demo: shoes/cans cleanup in a residential living room from handwritten task lists.
- Quote: "Gemini Robotics functioned as both the operator and the tablet sending commands to the robot."
- Engineers report **prompt engineering still matters** — tool docstrings had to encode hardware-specific facts (e.g. that the gripper camera is the most informative initial view; that front cameras sit too low to photograph elevated surfaces).
- Safety property: "Gemini Robotics has strict boundaries in this scenario. It can't invent new capabilities or control Spot beyond what is available through the API." The SDK / tool schema is the safety surface — see [AI safety and alignment](../concepts/ai-safety-alignment.md).

### Productization: AIVI-Learning + ER 1.6
Boston Dynamics' **AIVI-Learning** product is described as "the next evolution" powered by Gemini Robotics-ER 1.6, providing "a new level of visual intelligence" to [Spot](spot.md) and Orbit with automatic model upgrades ([source](../sources/bostondynamics-spot-gemini-robotics.md)).

## Position in the foundation-model landscape

- **Architecturally distinct from a VLA when used in -ER mode.** Gemini Robotics-ER is closer in spirit to GPT-4o-as-planner inside [stretch_ai](stretch-ai.md) or to [Qwen](qwen.md) inside [OpenClaw](openclaw.md): the model emits structured tool calls; classical perception/manipulation primitives execute them. Compare with [NVIDIA GR00T](nvidia-groot.md) (true VLA, emits actions) and the V-JEPA family (latent-prediction world models, not policies at all).
- **Two-product strategy is unusual.** Most foundation-model providers ship a single robotics offering. Google's split (full VLA *and* embodied-reasoner-with-tools) lets them serve both end-to-end research and integration-into-existing-robots use cases.
- **Hardware-agnostic ambitions.** The -ER variant explicitly does *not* assume a particular embodiment — anything with a camera and a callable API surface is a target.

## Related

- [Google DeepMind](google-deepmind.md) — developer.
- [Boston Dynamics](boston-dynamics.md) / [Spot](spot.md) — the documented integration partner in the wiki.
- [LLM-agent architecture](../concepts/llm-agent-architecture.md) — the design pattern Gemini Robotics-ER fits.
- [VLA models](../concepts/vla-models.md) — where the *full* Gemini Robotics (not -ER) sits.
- [Embodied reasoning](../concepts/llm-agent-architecture.md) — the framing Google uses for -ER; functionally a synonym for "LLM-agent planner with vision."

## Mentioned in

- [Tools for Your To Do List with Spot and Gemini Robotics (Boston Dynamics blog)](../sources/bostondynamics-spot-gemini-robotics.md)

## Open questions / TBD

- **Primary technical source not yet ingested.** The DeepMind model card / paper for Gemini Robotics-ER would clarify training data, evaluation, and the exact distinction between ER 1.5 and ER 1.6.
- **Full Gemini Robotics VLA** — referenced via the [VLA models](../concepts/vla-models.md) concept page but no primary source ingested.
- **Open weights?** No; both variants appear to be closed / API-only.
- **Latency and cost.** Not documented in the BD blog; likely cloud-API-bound.
- **Other documented integrations besides Spot.** Apptronik (NVIDIA-aligned) has been mentioned in DeepMind press; needs a primary-source ingest.

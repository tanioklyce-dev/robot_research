---
title: Boston Dynamics
type: entity
subtype: company
created: 2026-05-09
updated: 2026-05-09
sources: 1
tags: [boston-dynamics, robotics-company, spot, atlas, orbit, hyundai]
---

**Boston Dynamics** — robotics company headquartered in Waltham, MA. Founded 1992 by [Marc Raibert](../entities/atlas.md) (spun out of MIT Leg Lab). Acquired by Hyundai Motor Group in 2021 (majority stake). Best known for [Atlas](atlas.md) (research humanoid) and [Spot](spot.md) (commercial quadruped); also produces Stretch (warehouse case-handling) and the Orbit fleet-management software.

## Products

- **[Spot](spot.md)** — commercial quadruped; the only widely-deployed Boston Dynamics product. Inspection, security, data collection. Has a published [Spot SDK](spot.md) for third-party integrations.
- **[Atlas](atlas.md)** — research humanoid. Hydraulic generation retired April 2024; replaced by fully-electric Atlas. Closed development; not sold.
- **Stretch** — warehouse case-handling robot (distinct from [Hello Robot's Stretch](stretch.md); namespace collision is unfortunate).
- **Orbit** — cloud-based fleet management and mission orchestration platform for Spot fleets.
- **AIVI-Learning** — emerging product line. Per [the Spot + Gemini Robotics blog](../sources/bostondynamics-spot-gemini-robotics.md), described as "the next evolution" powered by Google **Gemini Robotics-ER 1.6**, delivering visual intelligence to Spot and Orbit with automatic model upgrades. Concrete capabilities and pricing not yet publicly detailed (as of May 2026).

## AI-stack strategy

Historically Boston Dynamics built classical model-based control (whole-body MPC, optimization-based planning) — the Atlas parkour demos are a flagship for that lineage. Recent direction: **integrate large foundation models above the existing low-level control stack** rather than replace it.

- **2024–2025 LLM/VFM work.** Internal blog series "Robots That Can Chat" (LLMs) and "Put It in Context with Visual Foundation Models" (VFMs).
- **2025 Spot + Gemini Robotics hackathon** ([source](../sources/bostondynamics-spot-gemini-robotics.md)). Two Spot-team engineers (Issac Ross and Nikhil Devraj) wired [Gemini Robotics-ER 1.5](gemini-robotics.md) into Spot via a thin tool-call layer (`GoTo`, `TakePicture`, object ID, `Pickup`, `PutDown`) over the Spot SDK. Demonstrated living-room cleanup from handwritten natural-language instructions. Architecture is a textbook [LLM-agent](../concepts/agents/llm-agent-architecture.md) pattern.
- **Formal partnership with [Google DeepMind](google-deepmind.md)** — announced separately; characterized as early-stage. Gemini Robotics is the model line being integrated.
- **Meta** has separately used Spot for AI research on object retrieval ([source](../sources/bostondynamics-spot-gemini-robotics.md)).

## Position in the landscape

- **Capability bar but academic-access black hole.** Atlas demos define the public perception of "humanoid capability" but Boston Dynamics neither sells Atlas nor publishes much of its control stack. Compare to [Unitree H1](unitree-h1.md) / [Unitree G1](unitree-g1.md) (Chinese affordable hardware) and [Apptronik Apollo](apptronik-apollo.md) (NVIDIA-aligned, more open ecosystem).
- **Spot is the open API.** The Spot SDK and Orbit are the integration points where third-party AI can run; the hackathon blog is explicit about this being where foundation-model integration happens. Atlas does not have a comparable public surface.
- **Integration-first over build-from-scratch.** Boston Dynamics is using Google's foundation model (Gemini Robotics) rather than training their own VLA — contrast with [NVIDIA GR00T](nvidia-groot.md), [Physical Intelligence](physical-intelligence.md), or [1X NEO](1x-neo.md)'s Redwood AI VLM.

## People

- **Marc Raibert** — founder; CTO emeritus. Founded the Boston Dynamics AI Institute (separate entity) in 2022.
- **Issac Ross, Nikhil Devraj** — Spot team engineers; authors of the Spot + Gemini Robotics blog ([source](../sources/bostondynamics-spot-gemini-robotics.md)).

## Mentioned in

- [Tools for Your To Do List with Spot and Gemini Robotics (Boston Dynamics blog)](../sources/bostondynamics-spot-gemini-robotics.md)

## Open questions / TBD

- Internal AI/control stack details (closed; minimal public documentation).
- Atlas commercial trajectory — Hyundai / Magna pilots are announced but unit volumes and timelines are not public.
- AIVI-Learning concrete capability set, pricing, and rollout timeline.
- Boston Dynamics AI Institute vs Boston Dynamics — the AI Institute is a separate Hyundai-funded research lab under Raibert; relationship to product engineering is not publicly clarified.

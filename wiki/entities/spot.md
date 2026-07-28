---
title: Spot
type: entity
subtype: robot
created: 2026-05-09
updated: 2026-05-09
sources: 1
tags: [spot, boston-dynamics, quadruped, commercial, sdk, orbit]
---

**Spot** — Boston Dynamics' commercial quadruped robot. The only widely-deployed Boston Dynamics product. Originally launched 2019; multiple generations since. Used for industrial inspection, security patrols, data collection in plants and construction sites, and (via the optional **Spot Arm**) light manipulation. Operated either by tablet, by **Autowalk** (pre-recorded missions), or via the **Spot SDK** for custom autonomy.

## Form factor and capabilities

- ~32 kg, ~84 cm long quadruped.
- 360° vision via stereo cameras around the body.
- Walks on uneven terrain, stairs, snow, etc. Self-rights from a fall.
- Battery-powered; ~90 min runtime. Self-docking.
- **Spot Arm** (optional) — 6-DOF manipulator with a parallel-jaw gripper and gripper camera.
- **Spot CORE / CORE I/O** — onboard compute for third-party payloads.

## Programming and integration surface

- **Spot SDK** (Python, gRPC) — public API for navigation, perception, arm control. The integration point used by the [Spot + Gemini Robotics hackathon](../sources/bostondynamics-spot-gemini-robotics.md) — engineers wrote a thin tool-call layer exposing `GoTo`, `TakePicture`, object identification, `Pickup`, `PutDown` to a foundation model planner.
- **Autowalk** — record-and-replay autonomy missions via the tablet.
- **Orbit** — cloud-based fleet manager and mission orchestrator.
- **Choreographer** — for the dance/performance use case.

## AI integrations (observed)

- **[Gemini Robotics](gemini-robotics.md)-ER 1.5 (Google DeepMind, 2025)** — integrated at a Boston Dynamics hackathon. LLM-agent architecture: model emits tool calls against the SDK; demonstrated on shoe/can cleanup tasks in a residential living room ([source](../sources/bostondynamics-spot-gemini-robotics.md)). Productized as **AIVI-Learning** with the ER 1.6 model.
- **[Meta FAIR](meta-fair.md)** — separately used Spot to test AI systems for locating and retrieving previously unseen objects ([referenced](../sources/bostondynamics-spot-gemini-robotics.md)).
- Earlier internal Boston Dynamics work: "Robots That Can Chat" (LLMs), "Put It in Context with Visual Foundation Models" (VFMs).

## Position in the landscape

- **The quadruped reference platform** alongside Unitree's Go1 / **[Go2](unitree-go2.md)** (cheaper Chinese alternative; more academic-friendly). ANYbotics ANYmal is the third major commercial quadruped, focused on European industrial inspection.
- **Closed but well-documented SDK.** Unlike Atlas, Spot has a clear third-party integration story — which is why most foundation-model + BD-hardware research uses Spot, not Atlas.
- **Manipulation-light.** The Spot Arm exists but is a relatively low-DOF parallel-jaw gripper on a 6-DOF arm. For dexterous research, the field has gravitated to humanoids with 5-finger hands or to [Stretch](stretch.md)-style mobile manipulators.

## Related

- [Boston Dynamics](boston-dynamics.md) — manufacturer.
- [Atlas](atlas.md) — sibling product (humanoid).
- [Gemini Robotics](gemini-robotics.md) — Google DeepMind model integrated via the SDK.
- [Unitree Go2](unitree-go2.md) — the cheap-tier quadruped counterpart. Instructive contrast on the *integration* axis: Spot's well-documented SDK is why foundation-model work targets it, while [Project Fetch](../sources/anthropic-project-fetch-robot-dog.md) found that the Go2-class connection layer (inconsistent online docs, several competing connection methods) was itself the hardest part of the task.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the integration pattern used in the hackathon demo.

## Mentioned in

- [Tools for Your To Do List with Spot and Gemini Robotics (Boston Dynamics blog)](../sources/bostondynamics-spot-gemini-robotics.md)

## Open questions / TBD

- Spot SDK details (rate limits, perception primitives surfaced, simulator availability) — would benefit from a developer-docs ingest.
- Spot Mujoco / Spot in Isaac Sim — both exist; current quality unclear.
- AIVI-Learning rollout details.

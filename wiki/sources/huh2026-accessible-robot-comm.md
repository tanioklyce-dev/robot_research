---
title: Designing Accessible Robot Communication for Blind People (Huh et al. 2026)
type: source
url: https://doi.org/10.1145/nnnnnnn.nnnnnnn
venue: 3rd InterAI Workshop at ACM CHI 2026, Barcelona, April 13–17, 2026
local_path: raw/6_Designing_Accessible_Robot_C.pdf
sha256: 86980ffd48e4cce3980a4e5a7f7ccd947014c276ace35174a678d006bf9fc17b
author: Mina Huh, Huihan Liu, Albert Yu, Roberto Martin-Martin, Yuke Zhu, Maya Cakmak, Amy Pavel
published: 2026-04
ingested: 2026-05-10
tags: [assistive-robotics, accessibility, blind-users, hri, robot-narration, gemini-live, cakmak, pavel, ut-austin, uw, uc-berkeley]
---

## Summary

A two-study CHI workshop paper asking **how should robots communicate their actions and progress when visual monitoring is unavailable?** Two studies: (1) an in-person observational study of 10 blind participants supervising a tabletop [Franka Panda](../entities/franka-panda.md) and a mobile [Tiago](../entities/tiago.md) on four household tasks (with injected failures); (2) an online controlled study with 20 blind + 20 sighted participants comparing reactive (answer-only) vs. mixed-initiative (proactive narration + answering) modes on a Gemini Live-powered narration prototype. Contributes **6 design guidelines** for accessible robot task communication.

The first study finds that blind users **systematically overestimate their situational awareness** (avg 7.5 inaccuracies per task: 51% missed errors, 30% incorrect additions, 20% missed steps). The second study finds **strongly divergent preferences across groups**: most blind participants prefer proactive narration; most sighted participants find it repetitive and prefer reactive mode.

## Key claims

### Observational study (10 blind participants)
- **Robots**: Franka Panda (tabletop) and PAL Robotics Tiago (mobile manipulator). Both teleoperated by a researcher under Wizard-of-Oz to reliably inject failures. Participants were not informed of teleoperation.
- **Four tasks**: set table, clear table, fetch salt, pour pasta. Each task had two injected errors spanning misinterpretation, control, planning, sensing categories (Table 3 of paper).
- **Monitoring strategies used by blind participants**:
  - **Auditory cues**: all 10 used them, every task. But sounds were often ambiguous or absent (silent grasps); environmental noises (fan, AC) sometimes mistaken for robot activity.
  - **Tactile inspection** after task completion (5–8 participants per task). But touch is incomplete (e.g., 5 of 8 swept the table by hand and *still* missed a napkin at the edge); undesirable in real contexts ("Who would want to put their hand into the trash to check what the robot did?" — P10); and unsafe near hot/sharp items.
  - **Smell/taste cues**: 4 participants opened the fetched bottle to smell or taste (to verify it was salt vs. lemon pepper).
  - **AI-powered visual interpretation**: 7 used Be My AI / Seeing AI / Gemini Live; 4 used Meta Ray-Ban smart glasses. Framing objects in the phone camera was a recurring failure mode.
  - **Human-powered visual interpretation**: a few used Aira / Be My Eyes / called family.
- **Self-rated situational awareness was high, but objectively low**: avg **7.5 inaccuracies** per task report (SD=1.27). 51% missed errors, 30% incorrect additions (sounds misinterpreted as actions), 20% missed task steps.
- **Universal request**: all participants asked for **rich task-relevant robot narration** plus the ability to ask questions on demand.

### Controlled study (20 blind + 20 sighted, online)
- **Prototype**: web app (React/TypeScript) feeding robot visual observations + joint states + scripted task plan into **Gemini Live API** (Google) for streaming multimodal speech. Two modes:
  - **Reactive**: robot answers only when asked.
  - **Mixed-initiative**: robot pulses a brief proactive update every 5 seconds (with 2.5s look-ahead to compensate for generation latency) *and* answers questions; proactive narration is preempted by user questions.
- **Question taxonomy** (Table 5): Scene Check, Task Progress, Object Status, Action Detail, Reasoning, Next Plan, Instruction, Correction, Other.
- **Volume**: 3,646 total questions (Blind 2,632; Sighted 1,014). Sighted asked significantly **fewer** questions when proactive narration was available; blind asked many regardless.
- **Question content differs by group**:
  - Blind: more **scene context** and **object state** questions.
  - Sighted: more **next action** and **reasoning** questions; more **feedback and corrections** to the robot.
- **Mode preference splits cleanly by group**:
  - **Blind participants prefer mixed-initiative**: "When they only answer my question, it relies on me asking good questions. When I don't even know what they are doing, I can't ask good questions." — P19. Reported higher situational awareness; perceived lower task success rate (i.e., noticed errors better).
  - **Sighted participants prefer reactive**: proactive narration described as "duplicating visual information, often repetitive, and sometimes disruptive."
- **Model failure modes observed in narration**: incorrect spatial properties (distance, height, size); hallucinated answers to leading questions ("Did you already pick up the cup?") rather than abstaining; sometimes appropriately abstained — errors are not uniform.

### Six design guidelines (DG1–DG6)
- **DG1**. Make non-visual sensing reliable and interpretable.
- **DG2**. Provide proactive narration that complements question answering.
- **DG3**. Communicate risks and failures clearly to support correction and recovery.
- **DG4**. Design for appropriate trust in robot narration.
- **DG5**. Adapt communication to context and provide user control.
- **DG6**. Design and evaluate with blind users under ecologically valid conditions.

## Entities mentioned

- [Mina Huh](../entities/mina-huh.md) — first author (UC Berkeley)
- [Huihan Liu](../entities/huihan-liu.md) — UT Austin (Yuke Zhu's group)
- [Roberto Martin-Martin](../entities/roberto-martin-martin.md) — UT Austin
- [Yuke Zhu](../entities/yuke-zhu.md) — UT Austin / NVIDIA
- [Maya Cakmak](../entities/maya-cakmak.md) — UW
- [Amy Pavel](../entities/amy-pavel.md) — UC Berkeley (senior)
- [Franka Panda](../entities/franka-panda.md) — tabletop platform
- [Tiago](../entities/tiago.md) — mobile manipulator platform (PAL Robotics)

## Concepts touched

- [Accessible robot communication](../concepts/robotics/accessible-robot-communication.md)
- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — extends the "output interfaces are underexplored" gap flagged in the [Nanavati/Cakmak 2024 review](nanavati2024-physically-assistive-robots-review.md), §6.1.3
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — narration pipeline is a streaming multimodal model (Gemini Live) consuming (video + joint-state + task plan) and emitting (speech + question-answering)

## Open questions

- The Wizard-of-Oz setup ensures controlled failure injection but means the narration is decoupled from a real policy. How does narration quality change when grounded in actual policy state vs. scripted task plans?
- Gemini Live's hallucinations on spatial questions ("That shelf is approximately 3 feet high") suggest current VLMs lack the spatial grounding for safe communication around blind users. Worth tracking whether [Gemini Robotics-ER](../entities/gemini-robotics.md) or similar embodied-VLMs close this gap.
- Six DGs are stated but not yet evaluated against a deployed system; follow-on work needed.

---
title: Accessible robot communication
type: concept
created: 2026-05-10
updated: 2026-05-10
sources: 4
tags: [assistive-robotics, accessibility, blind-users, robot-narration, hri, output-interfaces]
---

**Accessible robot communication** — the design of how a robot conveys its state, intent, progress, and failures to users who **cannot rely on visual monitoring**. This is the *output-interface* side of HRI: how the robot tells the user what it is doing, what it has done, and what it plans to do next, in modalities and granularities that match the user's sensory capabilities and information needs.

Distinct from broader "robot legibility" / "expressive robot motion" work, which assumes a sighted observer. Accessible robot communication asks the same questions for users who are blind, have low vision, or are otherwise visually unavailable to the robot (e.g., a sighted user in another room).

## Why it matters

The [Nanavati, Ranganeni, Cakmak 2024 PAR review](../../sources/nanavati2024-physically-assistive-robots-review.md) §6.1.3 explicitly flags **output interfaces** as comparatively under-explored in PAR research: "Research has shown that users' trust in robots, comfort around robots, and ability to help robots improve if the robot transparently communicates its current state and future intent to them. Therefore, we call on future research to investigate what output information users want to receive from their PARs and how that information improves the user experience."

[Huh et al. 2026](../../sources/huh2026-accessible-robot-comm.md) is the most direct response to that call, focused on blind users.

## Empirical findings

### Blind users systematically overestimate situational awareness

[Huh et al. 2026](../../sources/huh2026-accessible-robot-comm.md) ran an in-person observational study with 10 blind participants supervising a [Franka Panda](../../entities/franka-panda.md) and a [Tiago](../../entities/tiago.md) on four household tasks. Participants rated their situational awareness highly, but their post-task reports contained an average of **7.5 inaccuracies per task** (SD=1.27):
- 51% **missed errors** (the robot did something wrong; the participant did not notice)
- 30% **incorrect additions** (the participant inferred something that didn't happen, often from misinterpreted sounds)
- 20% **missed task steps**

Practical implication: silent autonomous execution + post-hoc tactile inspection — the de facto pattern in most PAR research today — does **not** produce reliable user awareness even with willing, motivated blind users.

### Native modalities are insufficient on their own

The same study documents what blind participants actually do (Table 1 of paper):
- **Auditory cues**: universal but ambiguous; silent grasps and motion noise are confounds.
- **Tactile inspection**: often incomplete (5 of 8 swept-by-hand participants still missed a napkin); undesirable in real contexts (trash, hot pots).
- **Smell/taste**: used for object identification (4 of 10 opened a fetched bottle to smell).
- **AI-powered visual interpretation** (Be My AI, Seeing AI, Gemini Live, Meta Ray-Ban): 7 of 10 used them; framing objects in a phone camera is a recurring failure.
- **Human-powered visual interpretation** (Aira, Be My Eyes, family): used sparingly.

### Mixed-initiative narration > reactive for blind users

In a controlled online study with 20 blind + 20 sighted participants, blind participants overwhelmingly preferred a **mixed-initiative** mode (proactive narration every ~5s + on-demand question answering) over a **reactive** mode (answer-only): proactive updates relieve the "burden of knowing what to ask." Sighted participants showed the opposite preference — proactive narration is "duplicating visual information, repetitive, sometimes disruptive."

This is one of the clearest documented cases of **divergent design preferences across vision-status** in HRI: a single narration policy cannot serve both populations.

### Question content differs by group

3,646 questions across both populations, categorized (Table 5 of Huh et al.):
- **Blind** users ask more **Scene Check** and **Object Status** questions (rebuilding the visual context).
- **Sighted** users ask more **Next Plan** and **Reasoning** questions, and offer more **corrections** to the robot.

## Six design guidelines (Huh et al. 2026)

1. **DG1** — Make non-visual sensing reliable and interpretable.
2. **DG2** — Provide proactive narration that complements question answering.
3. **DG3** — Communicate risks and failures clearly to support correction and recovery.
4. **DG4** — Design for appropriate trust in robot narration (note: VLMs hallucinate spatial properties; users will over-trust if the robot sounds confident).
5. **DG5** — Adapt communication to context and provide user control.
6. **DG6** — Design and evaluate with blind users under ecologically valid conditions.

## Related findings in the wiki

- [DRAGON (Liu et al. 2024)](../../sources/dragon-assistive-nav-2024.md) takes the opposite design point for the navigation domain: the robot is mostly silent during navigation, with description and VQA gated on user intent. Pairs verbal output with **kinesthetic guidance** through a T-shaped handle and a wireless headset. Useful contrast for DG5 (context-adaptive communication).
- [Schneiders 2021](../../sources/schneiders2021-domestic-robots-automation.md) finds that **under-trust** drives sighted users into co-located monitoring of vacuum robots — i.e., visual monitoring is already a load-bearing channel even for fully sighted users; blind users are *additionally* deprived of it.
- [HCR Lab autonomy-preference work](../../entities/hcrlab.md) — users with severe motor impairments do not always prefer more autonomy. Combined with DG2, this points toward **user-tunable narration verbosity** (not just on/off) as a likely useful design axis.

## Open questions

- How does narration quality change when grounded in real policy state (with uncertainty estimates) rather than a scripted task plan + Wizard-of-Oz teleop?
- Hallucination in spatial answers ("That shelf is approximately 3 feet high") is a current VLM failure mode that will eventually close — at what point does **embodied-VLM** state grounding become trustworthy enough for safety-relevant narration?
- The Huh et al. study is short-term and in lab. Long-term in-home use of narration-equipped PARs by blind users has not been studied.

## Mentioned in

- [Designing Accessible Robot Communication for Blind People (Huh et al. 2026)](../../sources/huh2026-accessible-robot-comm.md)
- [DRAGON Paper (Liu et al. 2024)](../../sources/dragon-assistive-nav-2024.md)
- [Physically Assistive Robots — Systematic Review (Nanavati et al. 2024)](../../sources/nanavati2024-physically-assistive-robots-review.md)
- [Domestic Robots and the Dream of Automation (Schneiders et al. 2021)](../../sources/schneiders2021-domestic-robots-automation.md)

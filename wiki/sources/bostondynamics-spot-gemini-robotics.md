---
title: Tools for Your To Do List with Spot and Gemini Robotics (Boston Dynamics blog)
type: source
url: https://bostondynamics.com/blog/tools-for-your-to-do-list-with-spot-and-gemini-robotics/
author: Issac Ross and Nikhil Devraj (Spot team engineers, Boston Dynamics)
published: 2025 (exact date not stated; describes a 2025 hackathon)
ingested: 2026-05-09
tags: [boston-dynamics, spot, gemini-robotics, llm-agent, tool-use, embodied-reasoning, hackathon]
---

## Summary

Two Boston Dynamics Spot-team engineers wired Google DeepMind's [Gemini Robotics-ER 1.5](../entities/gemini-robotics.md) (a vision-language model with "embodied reasoning") into [Spot](../entities/spot.md) via a thin layer over the [Spot SDK](../entities/spot.md), exposing a small library of tools (`GoTo`, `TakePicture`, object identification, `Pickup`, `PutDown`). At a 2025 internal hackathon, the engineers demonstrated cleaning up a residential living room from handwritten instructions like "Make sure all of the shoes at the front door are on the shoe rack." The post argues that natural-language prompting plus a tool-call schema can replace formal state-machine programming, and previews [AIVI-Learning](../entities/boston-dynamics.md) as the productized next step (powered by Gemini Robotics-ER 1.6).

## Key claims

- **Gemini Robotics-ER as the planner.** Google DeepMind's [Gemini Robotics-ER 1.5](../entities/gemini-robotics.md) is a *visual-language model* designed to provide embodied reasoning to physical robots — distinct from a VLA: it emits tool calls, not low-level motor actions.
- **Architecture: tool-call layer over the Spot SDK.** Engineers built "a layer that facilitated interaction between Gemini Robotics and Spot's [API](../entities/spot.md)" using the Spot SDK. Gemini Robotics is given access to mobile-base navigation, cameras, robotic arm, object identification, grasping, and placement.
- **Tools provided:**
  - `GoTo` — navigate between named locations.
  - `TakePicture` — capture images. The post emphasizes that the prompt had to explain *which* camera (gripper camera was "most informative"; front cameras sit too low to photograph elevated surfaces).
  - Object identification.
  - `Pickup` / `PutDown` — manipulation primitives.
- **Operational loop.** Gemini Robotics receives the task → evaluates camera images → identifies matching objects → sequences navigation + manipulation calls → adapts on real-time feedback. The blog frames it: "Gemini Robotics functioned as both the operator and the tablet sending commands to the robot."
- **Demo task.** A 2025 Boston Dynamics hackathon project building on prior LLM and visual-foundation-model work. Spot picks up shoes and soda cans in a residential living room following handwritten lists.
- **Conversational programming replaces state-machine programming.** Quote: "Our ability to engage Gemini Robotics using natural language prompts was a huge timesaver, compared to traditional programming." The framing is a workflow shift — engineers set goals, the foundation model interprets and adapts.
- **Safety boundary.** "Gemini Robotics has strict boundaries in this scenario. It can't invent new capabilities or control Spot beyond what is available through the API." The tool schema is the safety surface.
- **Prompt engineering still matters.** Tool docstrings need to encode hardware-specific facts (camera placement, what each camera sees) — model intelligence does not eliminate the need for grounded prompt design.

## Partnerships and adjacent work mentioned

- **Google DeepMind** — formal Boston Dynamics partnership announced separately; characterized as "early collaboration stage."
- **Meta** — has separately used Spot to test AI systems for locating and retrieving previously unseen objects.
- **AIVI-Learning** — Boston Dynamics product; described as "the next evolution" powered by Google **Gemini Robotics-ER 1.6**, claimed to deliver "a new level of visual intelligence" to Spot and Orbit, with model improvements happening automatically.

## Entities mentioned

- [Boston Dynamics](../entities/boston-dynamics.md) — author (Spot team).
- [Spot](../entities/spot.md) — the quadruped target platform.
- [Gemini Robotics](../entities/gemini-robotics.md) — Google DeepMind embodied-reasoning VLM (ER 1.5; ER 1.6 mentioned).
- [Google DeepMind](../entities/google-deepmind.md) — model provider; formal BD partner.
- [Meta FAIR](../entities/meta-fair.md) — separately uses Spot for object-retrieval AI research.

## Concepts touched

- [LLM-agent architecture](../concepts/llm-agent-architecture.md) — Gemini-emits-tool-calls-against-Spot-SDK is a textbook instance.
- [VLA models](../concepts/vla-models.md) — explicitly contrasted: Gemini Robotics-ER is a VLM/embodied-reasoner that emits tool calls, *not* a VLA emitting low-level actions. (Google does have a separate full Gemini Robotics VLA; this post is about the -ER variant.)
- [AI safety and alignment](../concepts/ai-safety-alignment.md) — the SDK / tool surface is the safety boundary; model can only invoke pre-defined capabilities.

## Open questions

- **Is the integration code released?** Blog implies in-house only; no GitHub link.
- **Latency / closed-loop frequency.** Not stated; quadruped manipulation with a remote-LLM planner has nontrivial round-trip implications.
- **What does AIVI-Learning actually ship?** Described in marketing terms ("a new level of visual intelligence"); concrete capability claims and pricing not in this post.
- **What replaced what?** Existing Spot autonomy missions are typically defined via Boston Dynamics' Orbit / Autowalk tablet workflow. Where does Gemini-Robotics-ER-as-planner sit relative to those?
- **Did the hackathon demo also have manipulation failures?** Post claims success but does not quantify success rate or failure modes — typical of marketing-tier blog content.

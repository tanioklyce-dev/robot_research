---
title: "Flexion Reflect v1.0 — The Path Towards Long-Horizon Autonomous Humanoid Work (Jun 2026)"
type: source
url: https://flexion.ai/news/flexion-reflect-v1.0
author: Flexion Team (Flexion Robotics AG)
published: 2026-06-29
ingested: 2026-08-13
tags: [flexion, reflect, humanoid, long-horizon, vlm-agent, rl-finetuning, vla, whole-body-control, isaac-lab, semantic-map, replanning, reflex]
---

## Summary

**The most capable instance of the LLM-agent pattern in this wiki, and the first with a number attached to the thing everyone else leaves undocumented.**

One instruction, then full autonomy: *"A parcel with snacks has been delivered for Flexion. Retrieve it using the stairs and come up using the elevator. Then unpack it and place the items into the empty drawer on the shelf in the snack area."* The robot navigates a **multi-floor building**, **interacts with doors and elevators**, **uses tools to open the box**, shelves the contents, and *"adapts when things don't go as planned."*

Two findings make this a significant ingest well beyond Flexion:

1. **It closes the VLA/agentic bifurcation** the [across-stacks synthesis](../syntheses/agents/llm-agent-architecture-across-stacks.md) has tracked — a **VLA sits inside the motion layer under a VLM mission controller** — and is candid that the VLA is the stack's weakest link.
2. **It measures, diagnoses, and fixes the closed-loop-replanning gap** that same synthesis calls *"the most consequential gap between published demo behavior and robust deployment."*

## The compounding argument

> *"A navigation policy that works 95% of the time, a grasp that works 90% of the time, and a planner that occasionally misreads the scene do not combine into a reliable system. **They compound into failure.**"*

That is this wiki's [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) logic applied to *system composition* rather than to benchmark comparison, and it is the clearest statement of why per-skill success rates are the wrong unit for long-horizon work.

## Architecture (v0's design, every layer upgraded)

| Layer | v1.0 |
|---|---|
| **Mission control** | a **custom VLM** — *"reacting live, replanning continuously"* |
| **Motion layer** | **a VLA trained on real-world data + RL-based skills** |
| **Whole-body controller** | **"Reflex"** — real-time, force-aware, *"trained for and deployed on different robots and morphologies with minimal human effort"* |
| **Runtime** | communication, process isolation, low-latency inference, logging, safety checks |

> *"The biggest shift in v1.0 is that **RL is no longer confined to individual motion skills. We use it across every layer from low-level control to high-level decisions.**"*

## The headline number: RL fine-tuning the *agent*

Evaluated on a **16-step mission**, measuring end-to-end completion:

| Mission controller | End-to-end completion |
|---|---:|
| Base VLM (careful prompt + in-context examples) | *"fails almost immediately"* |
| **+ Supervised fine-tuning (SFT)** | **38%** |
| **+ RL fine-tuning (SFT+RL)** | **90%** |

> [!note] The diagnosis of *why* off-the-shelf VLMs fail is the most useful sentence in the post
> *"Off-the-shelf VLMs are not reliable enough to drive complete missions out of the box… they often act **too eagerly**. Instead of **visually verifying that the previous tool call has completed and that the scene satisfies the preconditions for the next step**, they emit the next logically plausible tool call too quickly."*
>
> **That is precisely the gap the [across-stacks synthesis](../syntheses/agents/llm-agent-architecture-across-stacks.md) named and could not close**: *"None describe in detail how skill failures surface back to the LLM for re-planning."* Four stacks left it undocumented; [DimOS](../entities/dimos.md) had the machinery ([LangGraph](../entities/langgraph.md) interrupts) installed and unused. Flexion **names the failure mode, measures it (38% → 90%), and fixes it with RL fine-tuning** rather than with prompting or a better base model — and reports explicitly that **SFT alone does not hold up** *"when the robot must make decisions amid ambiguity, recover from failed attempts, and keep progressing when the plan diverges."*

## Perception and reconfiguration

**Semantic map tool** — from a building scan, *"we automatically generate a global map that supports natural language interaction, allowing the agent to query areas or objects from a text prompt and even request a global path to the target location."* Users can annotate it with mission-critical landmarks.

**Prompt-level reconfiguration** — *"the mission is specified directly in natural language, making task changes a matter of updating the prompt rather than modifying the code."* Demonstrated with several mission variants, and with **mid-mission interruption**: *"Scratch that! Come back all the way to the testing area by going through the 3d printer room!"*

## Motion layer

Most skills trained in simulation with **[NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md)**, custom visual encoders, targeted domain randomization.

- **Box pickup** — *"the same policy can pickup a variety of boxes, with weights varying from **100 g to 3.5 kg**."*
- **Box repositioning** — moved under one arm to free the other; *"would be very difficult to teleoperate."*
- **Elevator** — *"sit at an interesting boundary between symbolic and continuous control"*: *"press the elevator button"* is symbolic, but executing it needs button identification, a stable whole-body interaction pose, and **centimetre-level** reach.
- **Local navigation** — global planning plus continuous local adaptation; dynamic obstacle avoidance while carrying items, on rough terrain.

> [!warning] The VLA is in the stack and is its weakest link — and they say so
> *"For this mission, we use **a VLA trained on teleoperated data** with our whole-body controller in the loop. We found that **achieving high reliability in such settings is difficult**, especially for a **free-moving humanoid rather than a fixed-base manipulation system**. We are already working on the next logical solution: **solving these tasks with RL**."*
>
> Two things follow. **The bifurcation is closed** — a VLA now runs inside an agentic stack's control path, which no ingested source previously showed. And **the direction of travel is away from the VLA**: the layer trained on teleoperated data is the one they intend to replace with RL, which is the exact inverse of the field's prevailing bet. Note also the scoping claim, untested elsewhere in this wiki: **fixed-base manipulation results may not transfer to a free-moving humanoid.**

## Whole-body control and recovery

**Reflex** — real-time, simultaneously respecting balance, actuation limits, and safety constraints; stable during upper-body manipulation, on uneven terrain, and under command changes *"faster than any high-level planner can anticipate."* Robustness claim: **100+ consecutive stair traversals without falling**, and manipulation under significant disturbance.

**Recovery at two levels**, which is the architectural answer to compounding failure:
- **Motion layer** — local recovery behaviours *learned during RL training*. Shown: a policy fails an out-of-distribution box pickup, retries, succeeds; and adjusts locally when the box is pushed away.
- **Agent** — *"replans when a subgoal fails by detecting off-nominal situations directly from the camera feed."*

## Analysis

> [!note] This is now the reference instance of the pattern, and it inverts one of the synthesis's convergences
> The [across-stacks synthesis](../syntheses/agents/llm-agent-architecture-across-stacks.md) found that in every stack *"skills live below the LLM, not inside it"* — vision is YOLO/AprilTag, navigation is Nav2/A*, grasping is classical. **Flexion keeps the shape and replaces the contents**: the skills below the agent are **RL-trained whole-body policies and a VLA**, not classical primitives. The pattern survives; the claim that it implies *"classical robotics with an LLM dispatcher bolted on top"* does not.

> [!warning] One number, and everything else is video
> The **38% → 90%** result is the only quantitative claim in the post: **16-step mission, end-to-end completion, n unstated**, evaluation set undescribed. The box-weight range, the 100+ stair traversals, the multi-floor mission, and every recovery behaviour are **demonstrated, not measured**. Per the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md), that single number is the only thing here that can be quoted as a result — and **without n it cannot be checked for significance**.

> [!note] The data thesis partly survives its own test
> [v0](flexion-reflect-v0.md) bet that manual data collection is *"a dead end"* and that simulation plus RL would carry the stack. v1.0 largely delivers on that for **locomotion, navigation, and contact-rich box handling** — all sim-trained. But the **dexterous manipulation** step uses **a VLA trained on teleoperated data**, and it is the part they call unreliable. **The demonstration bottleneck bound exactly where this wiki's other sources say it binds: dexterous, contact-rich manipulation.** Flexion's response is to try to remove it with RL rather than to collect more — a live, testable disagreement with [UME](../entities/ume.md)'s answer, which was to make the demonstrations *better* by adding torque.

## Entities mentioned

- [Flexion](../entities/flexion.md) · [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) · [Jetson Thor](../entities/jetson-thor.md)
- [DimOS](../entities/dimos.md), [LangGraph](../entities/langgraph.md) — the stack that had the replanning machinery and did not use it
- [UME](../entities/ume.md) — the opposite response to the same bottleneck
- [X-VLA](../entities/x-vla.md), [π0](../entities/pi-zero.md) — the demonstration-heavy bet this argues against

## Concepts touched

- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) · [Agent skills](../concepts/agents/agent-skills.md) · [VLA models](../concepts/learning/vla-models.md)
- [Whole-body control](../concepts/robotics/whole-body-control.md) · [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) · [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md)

## Open questions

- **What is n on the 16-step evaluation?** The one number in the post is unqualified by trial count. Without it, 38% vs 90% cannot be tested.
- **Which humanoid, and what does it cost?** Still never named across three Flexion posts.
- **How is the mission controller RL-fine-tuned?** Reward, environment, and whether it trains in simulation against the same skills are all unstated — and this is the post's central technical claim.
- **Does the semantic map come from [Niantic Spatial](../entities/niantic-spatial.md)?** *"From a scan of the building"* is suggestive given the [July collaboration](niantic-flexion-nvidia-sim2real.md), and unstated.
- **Is "Reflex" the same policy as the v0 whole-body tracker**, or a rewrite? Claimed deployable *"on different robots and morphologies"* with no evidence of more than one.
- **Real-world success rate for the headline mission** — the parcel run is shown end-to-end and never scored.

---
title: "Gemini Robotics 2: Safety Evaluations"
type: source
url: https://storage.googleapis.com/deepmind-media/gemini-robotics/Gemini-Robotics-2-Safety.pdf
author: Gemini Robotics Team, Google DeepMind
affiliation: Google DeepMind
published: 2026-07-29
ingested: 2026-08-03
venue: Google DeepMind technical report
format: technical report (18 pp)
local_path: raw/gemini-robotics-2-safety.pdf
sha256: 0ce23ac5909394696970fcc9fc7777cb20033b5234b7777d3d5b1d38919baf7d
tags: [gemini-robotics-2, asimov-agentic, semantic-safety, agentic-safety, uncertainty-quantification, iso-25785, safe-stopping, red-teaming, google-deepmind, primary-source]
---

## Summary

The **ASIMOV-Agentic** benchmark and evaluations of **Gemini Robotics ER 2** on it. Its framing is the sharpest statement in the wiki of what safety means once an *agent* orchestrates a robot rather than a policy driving one:

> "While traditional physical protections (e.g., e-stops, barriers, and speed/force limits) remain essential, next-generation agents must also exhibit robust safety guardrails: (1) refusing tasks that violate operational constraints; (2) triggering interventions—such as protective stops—during critical events like hardware faults or unsafe human proximity; (3) shielding the Vision-Language-Action (VLA) model from infeasible or out-of-distribution tasks where confidence is low; and (4) proactively resolving ambiguous instructions or scene uncertainties by requesting human help."

The architecture is explicitly **System 2 / System 1**: an Agent decomposes a long-horizon task into sub-tasks for the VLA, but is empowered to *not* delegate — routing to the human instead when uncertainty is aleatoric (ambiguous language, occluded scenes), or pausing when it is epistemic (the VLA hasn't been trained for this). **The benchmark measures the routing decision**, not the manipulation.

Dataset released: `huggingface.co/datasets/google/asimov_agentic` (CC-BY-4.0).

> [!warning] The report excludes the enforcement layer, and says so
> "This work does **not** evaluate the underlying functional safety architecture – including certified hardware components, redundancy mechanisms, and real-time system guarantees – necessary to safely execute those decisions in a compliant physical deployment."
>
> This is the vendor stating, in its own safety report, the exact gap the wiki's [semantic safety](../concepts/safety/semantic-safety.md) page concluded independently: the layer is **measured, not enforced**. See Analysis.

## Key claims — six benchmark components

### 1. Unsafe task refusal / safety-constraint following
Synthetic (constraints, image) pairs generated with Gemini Pro + Nano Banana; constraints mix embodiment limits (payload, gripper width) with application rules ("liquids not allowed"); scenes are real [ALOHA](../entities/aloha.md) tabletops. Human-annotated, **low-agreement instances filtered out**.

Four output modalities: **Text** (binary), **Pointing** (2D coords normalized to [0,1000]), **Bounding Box**, **Tool-use**.

**Result:** text classification is reliable for all frontier models (**≥96.0%**), but pointing, boxes, and tool-use show "greater performance variance across models."

> **"This suggests a gap between semantically understanding a constraint (Text) and physically acting on it (Tool Use, Spatial)."** Knowing the rule and grounding it in coordinates are different competencies — the same shape as [CaP-X's](cap-x-paper.md) abstraction finding and [Anthropic's](anthropic-how-claude-performs-on-robotics-tasks.md) level-inversion.

### 2. Proactive human safety monitoring — the most consequential result
Sensorized data: a human wearing a head-mounted ZED stereo camera as robot proxy, approached by others wearing Vive trackers at varying angles, speeds, distances, poses, lighting. Model must call `robot_stop()` if a human breaches 1/2/3 m, else `continue()`.

- **Single-frame:** distance MAE **0.35–0.55 m**; 1 m breach detection accuracy **79–93%**.
- **Agentic** (5 s intervals, 5-frame context): a hard tradeoff.

> [!warning] No model is usable as a standalone human-proximity guard
> "Achieving a highly efficient, low-interruption operational state (**FPR under 5%**) currently comes at the unacceptable cost of missing genuine safety hazards (**FNR exceeding 40%**). Conversely, models that successfully suppress the FNR closer to the **10%–15%** range suffer significant operational penalties, unnecessarily stopping the robot **15% to 25%** of the time. **Crucially, no model currently operates in the ideal top-right quadrant.**"
>
> The stated consequence: *"it is currently best to utilize them alongside deterministic, low-level safety guardrails."* A 40% miss rate on human proximity is not a safety function — and DeepMind says as much.

**Real hardware:** on [Apollo 2](../entities/apptronik-apollo.md) in a garage doing object sorting with a human actor encroaching, ER 2 flagged presence at 1 m and 2 m thresholds and orchestrated the VLA to settle in-hand objects and move to a safe pose — **99% human detection accuracy (ER)** and **96% reliability transitioning to a safe pose (VLA)**, in lab settings.

### 3. Safety tool calling
Mid-task interruption by JSON safety messages (battery depletion, actuator faults) after several agent↔VLA turns; LOW severity → warn, HIGH → warn **and** `robot_stop()`.

**All frontier models tested — ER 2, Claude Opus 4.8, GPT 5.5 — score 100%.** The authors flag the obvious caveat themselves: future versions will test whether this survives "increasing context length and *attention jailbreaking*."

### 4. VLA feasibility awareness — shielding the policy
Can the agent act as a feasibility filter, refusing to invoke the VLA on out-of-distribution tasks? The example: *"I can place the hat into the bag for you, but I don't have the dexterity yet to tie a knot in such a bag."*

**Accuracy scales with how much the agent is told about the VLA's training distribution** (developer instructions, DI0→DI3): **62.0% → 95.8%**. All models benefit.

A second variant emulates VLA confidence (ToolEmu-style) over multi-step episodes. Agents "seek confidence assessments as instructed, but **less reliably generate sub-steps required to advance the task safely all the way to completion**" — failing via replanning errors or low-confidence tool calls on long horizons.

### 5. Instruction ambiguity
**Ten taxonomy classes** across object identification ("put it over there", "put the wrench in the bin" with several present), spatial/destination ("move the clamp" with no target, "put the torch near the belts"), and task parameterization ("put *some* items in the tray", "sort the objects" with no criterion). Scenes from Apollo 2 and Franka Duo.

**Result:** an explicit helpfulness-vs-safety tension. Systems tuned to act "exhibit an eagerness to act, which risks unpredictable or unsafe physical behaviors"; systems tuned to express uncertainty "over-request human help even when provided with unambiguous instructions."

### 6. Aleatoric scene uncertainty — obfuscated instrument reading
Real industrial-inspection instruments (thermometers, pressure gauges, sight glasses) degraded by **automated red-teaming image editing** — poor lighting, occlusion, physical damage. Balanced set of adversarial-but-readable vs genuinely unreadable.

**Result:** same helpfulness/uncertainty tradeoff, but "**encouragingly, from a safety standpoint, frontier models do seem to prioritize hallucination avoidance**." ER 2's published thinking trace is a good example of calibrated refusal: *"the needle is nearly indistinguishable from the fracture lines. I'm going to say this is unreadable because there's just no way to get a solid numerical value."*

### Standards grounding
The related-work section is the wiki's best single map of the relevant standards: **ISO 10218:2025** (absorbing ISO/TS 15066's four collaborative modes — SRMS, hand guiding, SSM, PFL), **ISO 13482** and the **forthcoming ISO 25785-1** for humanoid and dynamically stable robots, **ISO 13855** (separation distance from approach speed, reaction time, stopping distance), **ISO 13849-1** (stop-function integrity), **IEC 60204-1** (stop categories; a Category 2 stop decelerates while retaining power to hold pose).

## Entities mentioned
- [Google DeepMind](../entities/google-deepmind.md) · [Gemini Robotics](../entities/gemini-robotics.md) · [ASIMOV Benchmark](../entities/asimov-benchmark.md)
- [Apptronik Apollo](../entities/apptronik-apollo.md) (Apollo 2) · [Franka Panda](../entities/franka-panda.md) (Franka Duo) · [ALOHA](../entities/aloha.md)
- [Anirudha Majumdar](../entities/anirudha-majumdar.md) — among the contributors · [Anthropic](../entities/anthropic.md) (Claude Opus 4.8 evaluated)

## Concepts touched
- [Semantic safety](../concepts/safety/semantic-safety.md) — extends ASIMOV from *judgment* to *agentic orchestration*.
- [Robot safety standards](../concepts/robotics/robot-safety-standards.md) — the ISO map above, including the new ISO 25785-1.
- [AI guardrails](../concepts/safety/ai-guardrails.md) · [Guardrails for robot agents](../syntheses/agents/guardrails-for-robot-agents.md)
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) · [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md)
- [AI red teaming](../concepts/safety/ai-red-teaming.md) — automated image red-teaming generates §6.

## Analysis

**This is the strongest confirmation yet of the wiki's "measured, not enforced" thesis — and it comes from the vendor.** Three independent statements in one report:

1. The scope note excludes certified hardware, redundancy, and real-time guarantees.
2. The FNR/FPR result concludes frontier models are "best utilized **alongside deterministic, low-level safety guardrails**."
3. The framing sentence opens by affirming that traditional physical protections "**remain essential**."

The [semantic safety](../concepts/safety/semantic-safety.md) page reached the same conclusion from the outside, and the [guardrails thread](../syntheses/agents/guardrails-for-robot-agents.md) reached it from the runtime side. All three now agree, which upgrades that synthesis from a hypothesis to a documented position.

**The 100% on safety tool calling versus 40% FNR on human proximity is the report's real structure**: agents are excellent at *acting on a safety signal handed to them as structured text*, and unreliable at *producing that signal from perception*. That maps cleanly onto the wiki's [control abstraction levels](../concepts/robotics/control-abstraction-levels.md) finding — models are good at the symbolic layer and weak at the perceptual-physical one — and it argues the safety monitor should be a deterministic sensor, with the agent as consumer rather than producer.

## Open questions
- **No sample sizes** for any benchmark component, and the plots are figures rather than tables — so the exact per-model numbers aren't extractable at this ingest depth, only the stated ranges.
- **Privacy and fairness are explicitly out of scope** — "ensuring models perform equitably across demographically and geographically diverse profiles… are key areas of ongoing research." A human-proximity detector with demographic performance variance is a serious unexamined risk.
- **Attention jailbreaking is named but untested** — the 100% tool-calling result is acknowledged as fragile to long contexts.
- **ASIMOV-Agentic vs ASIMOV v1 vs ASIMOV-2.0** — this report extends "the ASIMOV benchmarks [5,4]"; the v1→2.0 delta the wiki [backlogged](../backlog.md) is still undocumented.
- **The VLA confidence emulator is a Gemini model scoring a Gemini agent** — the closed-loop concern that also applies to [ASIMOV v1](asimov-benchmark-paper.md).

## Related sources
- [Gemini Robotics 2 blog](gemini-robotics-2-blog.md) — the capability announcement this accompanies.
- [ASIMOV Benchmark v1](asimov-benchmark-paper.md) — the semantic-safety predecessor this extends to agentic reasoning.
- [Predictive Red Teaming](predictive-red-teaming-paper.md) · [Veo world simulator](veo-robotics-policy-evaluation-paper.md) — the sibling safety-evaluation lines.
- [Responsibly advancing AI and robotics](deepmind-gemini-robotics-safety-page.md) — the public framing page, which predates this and still describes GR 1.5.

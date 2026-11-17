---
title: Gemini Robotics
type: entity
subtype: model
created: 2026-05-09
updated: 2026-11-17
sources: 16
tags: [gemini-robotics, google-deepmind, vlm, vla, embodied-reasoning, foundation-model]
---

**Gemini Robotics** — [Google DeepMind](google-deepmind.md)'s family of robotics-targeted foundation models, built on the Gemini multimodal model line.

## Gemini Robotics 2.5 (VLA update, released 2026-11-10)

A new VLA, announced alone: no ER 2.5 and no On-Device 2.5 ([blog](../sources/gemini-robotics-2-5-blog.md)). It is rolling out to robotics partners only.

- **Evaluation**: "over 200 distinct tasks" on [Apollo 2](apptronik-apollo.md) + [SharpaWave](sharpa-wave.md) and Franka Duo, in four categories (tabletop pick-and-place, multi-step and contact-rich, precision kitting and insertion, dexterous tools and deformables). Stated gain over GR 2: "30% to 100% higher success rate depending on the type of task," and "20% to 30% faster."
- **Where it moved most**: tasks GR 2 could not do at all. Called-out examples include pack pastries with tongs **5% → 100%**, extract disk drive **0% → 100%**, close toolbox lid **0% → 93%**, untie ribbon bow **0% → 70%**, hang cardigan **0% → 62%**, fold pants with a board **0% → 40%**. In the multi-step chart GR 2 is non-zero on only 3 of 20 tasks.
- **Where it did not**: every chart runs from 100% down to a tail of tasks near 10%, and on a few tasks per chart GR 2.5 is at or below GR 2.
- **Factory pilot**: with an unversioned Gemini Robotics ER as orchestrator, Apollo 2 kitted automotive brackets on Mercedes-Benz lines in Kecskemét and Sindelfingen at a **96% success rate**, after "a few weeks of post-training" (Apptronik's CEO). No pick count, duration or intervention rate.
- **Safety**: "inference-time reasoning guidance" raises safe task completion around obstacles by 33% and around people by 43% (baselines not given). The agentic safety results in the post, including 99.5% on the new [ASIMOV-Jailbreak](asimov-benchmark.md), are [Gemini 4 Argon](gemini-4-argon.md)'s, with ER 2 (82%) as the "previous baseline." The [Argon safety report](../sources/gemini-4-argon-safety-security-report.md) has the per-benchmark comparison: ER 2 trails Argon on most rows and trails the older general Gemini 3.1 Pro on video hazard severity (52.0% vs 63.2%) and human-proximity recall (71.1% vs 90.1%).
- **Built with Argon**: simulated practice runs from real camera scenes, plus failure analysis from video. No ablation.

> [!warning] Contradiction: the GR 2 baseline in the 2.5 charts is below GR 2's launch numbers
> The [GR 2 blog](../sources/gemini-robotics-2-blog.md) reported unscrew bulb **92%** (Apollo, SharpaWave). The 2.5 post charts GR 2 at **63%** on "Unscrew light bulb" on the same platform, and GR 2.5 at **90%**. GR 2's launch "dustpan" figure was 32%; the 2.5 chart has GR 2 at 0% on "Sweep trash into dustpan with brush." Neither post gives a protocol, so the tasks may differ. Read the 2.5 post's GR 2 column as a re-measured baseline, and do not chain the two posts' numbers together. Trial counts are still unpublished, and there is still no external baseline.

The fingers-versus-grippers gap that GR 2 left open has narrowed on this evidence: most of the called-out 0% → 60–100% jumps are five-finger tasks on deformables and tools. Threaded insertion ("screw bulb," GR 2's 36%) is not among the labeled tasks, so the specific wall identified below is untested in public.

## Gemini Robotics 2 (released 2026-07-30)

Three models ([blog](../sources/gemini-robotics-2-blog.md), [safety report](../sources/gemini-robotics-2-safety-report.md)):

| Model | Role | Access |
|---|---|---|
| **Gemini Robotics 2** | VLA — vision + language to motor control; whole-body humanoid coordination | Early-access partners (application) |
| **Gemini Robotics ER 2** | "The robot's high-level brain" — multi-step planning, self-correction, **inter-robot coordination** | **Google AI Studio**; private preview via Gemini Enterprise Agent Platform |
| **Gemini Robotics On-Device 2** | Efficient VLA for local execution; adapts to new embodiments in a few hours, **typically <200 examples** | Early-access partners |

**Platforms:** [Apollo 2](apptronik-apollo.md) (with [SharpaWave](sharpa-wave.md) and Inspire hands), **Franka Duo** + Robotiq, **Dexmate**, **[SO101](so-arm101.md)**, **Trossen**.

### Benchmarks

- **Whole-body manipulation** (Apollo 2, Inspire hands): shelf **76.3%** / table **68.4%** / floor **45.7%**
- **Multi-finger dexterity** (Apollo, SharpaWave 5-finger, 22-DoF): unscrew bulb **92%** / tie trash bag 44% / ziplock 40% / screw bulb **36%** / dustpan **32%**
- **Gripper dexterity** (Franka Duo): precise insertion **89.6%** / tool kitting 78.9% / pick-and-place 74.2%

> [!note] The dexterity ceiling lifted for grippers, not for fingers
> GR 1.5's stated weakness was **"dexterity is approximately prior generation."** GR 2 resolves that unevenly: gripper tasks run 74–90%, but **four of five multi-finger tasks sit at 32–44%**. The cleanest evidence is **unscrew bulb 92% vs screw bulb 36%** — same object, same hand, a **2.5x gap** separating removal from threaded insertion. Alignment-under-constraint remains the wall.
>
> **No trial counts are published**, so per the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) the 44/40/36/32 cluster is not internally separable; the 92-vs-36 gap survives almost any n. No baselines against GR 1.5 or external models either.

### Safety — ASIMOV-Agentic
The [safety report](../sources/gemini-robotics-2-safety-report.md) introduces **ASIMOV-Agentic** (on Hugging Face, CC-BY-4.0), benchmarking the *routing* decision: delegate to the VLA, query the human, or trigger a safety tool. Safety tool calling scores **100%** across ER 2 / Claude Opus 4.8 / GPT 5.5; VLA feasibility filtering rises **62.0% → 95.8%** as the agent is told more about the VLA's training distribution; real Apollo 2 safe-stopping hits **99%** human detection and **96%** safe-pose transition.

> [!warning] But no model is a usable standalone human-proximity guard
> FPR under 5% costs **FNR above 40%**; suppressing FNR to 10–15% causes unnecessary stops **15–25%** of the time. **No model reaches the ideal quadrant.** DeepMind's own conclusion is to use them "alongside **deterministic, low-level safety guardrails**," and the report explicitly does **not** evaluate the functional-safety architecture. See [semantic safety](../concepts/safety/semantic-safety.md).

### On-Device 2 — what the model card adds (2026-08-03)
The [official model card](../sources/gemini-robotics-on-device-2-model-card.md) supplies lineage and results: built on **GR 1.5 technology + on-device Gemma models**; **SO101 53.3% (v2) vs 6.7% (v1)**, Dexmate 75.6% vs 33.3%; stated limitation — OOD generalization and **"controlling high-degree-of-freedom robots"** (the on-device tier is explicitly not the whole-body tier). Trusted Testers only.

**Still unpublished:** parameter count, memory footprint, target hardware, control rate — so it remains unplaceable on the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md). A third-party tutorial reports ~0.25 s closed-loop latency (~4 Hz); unofficial, not adopted.

## Beside the line: Gemini 4 Argon (2026-10-13)

Three months after ER 2, Google showed a **general** frontier model, [Gemini 4 Argon](gemini-4-argon.md), doing the ER job and more: **ERQA 87%** "using pure reasoning" (no competitor table), code-as-policies control of [Spot](spot.md) and an arm, MuJoCo twin authoring, hindsight labeling, and sim data that lifted an unnamed VLA from 56% to 75% ([Argon robotics blog](../sources/gemini-4-argon-robotics-blog.md)). The post never mentions Gemini Robotics or ER 2. Whether ER is being folded into the general model, or distilled from it, is open. The VLA tier (GR 2, On-Device 2) is unaffected: Argon emits code, not actions.

A month later the [GR 2.5 post](../sources/gemini-robotics-2-5-blog.md) made the division of labour explicit. Argon is credited with accelerating the VLA's development and holds the agentic safety results, with ER 2 called the "previous baseline"; the VLA still does the acting; and a Gemini Robotics ER with no version number orchestrates the factory pilot.

---

The 1.5-generation family contains two distinct variants:

- **Gemini Robotics** — full vision-language-**action** model (VLA); emits low-level robot actions directly. Listed alongside [NVIDIA GR00T](nvidia-groot.md) and [Physical Intelligence π0/π0.6](physical-intelligence.md) on the [VLA models concept page](../concepts/learning/vla-models.md).
- **Gemini Robotics-ER** ("ER" = embodied reasoning) — vision-language model (VLM) that provides high-level reasoning over visual input and emits *tool calls*, not motor actions. Designed to be plugged into a robot's existing API (i.e. acts as the planner in an [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md), not as the policy). Versions 1.5 and 1.6 referenced below.

## The original Gemini Robotics (March 2025)

The founding [technical report](../sources/gemini-robotics-report-2025.md), on Gemini 2.0. It introduced the two-model split the line has kept, and the [ERQA](erqa.md) benchmark.

- **Gemini Robotics-ER**: a Gemini 2.0 Flash variant with stronger pointing, grasp prediction and 3D detection. With no action training it controls an [ALOHA](aloha.md) 2 by writing code (53% in simulation, 25% on the real robot) or from 10 in-context demonstrations (65% in both). Zero-shot fails where precise grasps are needed.
- **Gemini Robotics** (the VLA): a distilled ER backbone **in the cloud** (under 160 ms) plus an on-robot action decoder; about **250 ms** end to end, with chunked actions played at 50 Hz. Trained on "thousands of hours" of ALOHA 2 teleoperation collected over 12 months.
- **Results**: above 80% success on half of 20 dexterous tasks out of the box; 79% average on six long-horizon tasks after fine-tuning on 2,000–5,000 episodes each (lunch-box packing 100% of 20 trials); above 70% on 7 of 8 new short tasks from at most 100 demonstrations. The same model trained from scratch on the specialization data scores 0%.
- **Embodiments**: adapted by fine-tuning to a bi-arm [Franka](franka-panda.md) (63% on four industrial tasks) and, with no number given, [Apollo](apptronik-apollo.md).
- **Method**: stated trial counts, randomized back-to-back runs, a paired test, and a π0 baseline retrained on the same data. None of the 2 or 2.5 announcements match this.
- **Safety**: [ASIMOV](asimov-benchmark.md) released alongside; ER post-trained on it.

Its closing list of future work (zero-shot cross-embodiment transfer, more simulation data, reasoning combined with dexterity) is what 1.5, 2 and 2.5 then delivered or claimed.

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

- [Gemini Robotics: Bringing AI into the Physical World](../sources/gemini-robotics-report-2025.md) — **the founding report** (March 2025): ERQA, Gemini Robotics-ER, and the cloud-backbone VLA.
- [Gemini Robotics 1.5 tech report](../sources/gemini-robotics-1-5-report.md) — **primary technical source** (GR 1.5 VLA + GR-ER 1.5).
- [Tools for Your To Do List with Spot and Gemini Robotics (Boston Dynamics blog)](../sources/bostondynamics-spot-gemini-robotics.md)
- [DeepMind Gemini Robotics model page](../sources/deepmind-gemini-robotics-model-page.md) — the **2** generation (GR 2 / ER 2 / On-Device 2), access tiers, and partner list. No numbers.
- [Responsibly advancing AI and robotics](../sources/deepmind-gemini-robotics-safety-page.md) — the safety framework page. **Note it still describes GR 1.5**, not the 2 generation.
- [Veo world simulator evaluation](../sources/veo-robotics-policy-evaluation-paper.md) — 8 Gemini Robotics checkpoints evaluated in a generative simulator against 1600+ real evaluations.
- [Gemini Robotics 2 blog](../sources/gemini-robotics-2-blog.md) — the GR 2 announcement with the whole-body, multi-finger, and gripper benchmark tables.
- [Gemini Robotics 2: Safety Evaluations](../sources/gemini-robotics-2-safety-report.md) — ASIMOV-Agentic and the ER 2 safety evaluations.
- [Gemini Robotics On-Device 2 model card](../sources/gemini-robotics-on-device-2-model-card.md) — the GRoD v1→v2 numbers and the high-DoF limitation.
- [Gemini 4 Argon for Robotics](../sources/gemini-4-argon-robotics-blog.md) — a general Gemini 4 model taking the ER orchestrator role (ERQA 87%), not part of this family.
- [Gemini 4 Argon Safety & Security Report](../sources/gemini-4-argon-safety-security-report.md) — ER 2 as the comparator in Argon's agentic robotics evaluations.
- [Gemini Robotics 2.5 blog](../sources/gemini-robotics-2-5-blog.md) — the 2.5 VLA: per-task charts against GR 2, the Mercedes-Benz kitting pilot (96%), and a GR 2 baseline that conflicts with GR 2's launch figures.

## Open questions / TBD

- ~~Primary technical source not yet ingested~~ — filed 2026-07-04: [Gemini Robotics 1.5 report](../sources/gemini-robotics-1-5-report.md). (Exact model sizes / action-decoder details still undisclosed by DeepMind; appendices not in the PDF.)
- **ER 1.6** — the AIVI-Learning productization variant post-dates the 1.5 report; no dedicated source.
- **Open weights?** No; both variants appear to be closed / API-only.
- **Latency and cost.** For the 2025 VLA the [report](../sources/gemini-robotics-report-2025.md) gives a cloud backbone under 160 ms and about 250 ms end to end. Nothing comparable is published for 2 or 2.5; cost is not documented anywhere.
- **Other documented integrations besides Spot.** The [GR 2.5 post](../sources/gemini-robotics-2-5-blog.md) documents Apptronik's Apollo 2 on Mercedes-Benz lines, from DeepMind's side only. An Apptronik or Mercedes primary would supply the denominators.
- **GR 2.5 evaluation protocol**: trial counts, and why its GR 2 baseline differs from GR 2's launch figures.
- **Is there an ER 2.5 or On-Device 2.5?** Neither is mentioned in the 2.5 announcement.

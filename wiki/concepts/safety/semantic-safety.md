---
title: Semantic safety
type: concept
created: 2026-08-03
updated: 2026-08-03
sources: 7
tags: [semantic-safety, robot-safety, constitutional-ai, asimov, red-teaming, google-deepmind, vlm, alignment]
---

# Semantic safety

## Definition

**Semantic safety** is the class of robot-safety constraints that are about *meaning and common sense* rather than *contact and force*: "the multitude of common-sense safety constraints in open-domain unstructured environments that are hard to exhaustively enumerate" ([ASIMOV](../../sources/asimov-benchmark-paper.md)).

The canonical examples are deliberately mundane:
> a soft toy must not be placed on a hot stove; a person with nut allergies must not be served peanuts; a wine glass must be transferred in upright orientation; a knife should not be pointed at a human; a robot mustn't hand a boiling drink to a young child.

None of these are violations of a force limit or a collision constraint. **Every one of them is a violation of understanding.**

## Why it became a distinct problem

The framing argument is historical: robotics safety was "predominantly about collision avoidance and hazard reduction in the immediate vicinity of a robot" — the tradition of [robot safety standards](../robotics/robot-safety-standards.md), ISO 15066, speed-and-separation monitoring. That tradition assumes the *intent* is correct and the risk is mechanical.

Foundation models invert this. A [VLM](../learning/vla-models.md) driving a robot can execute a perfectly safe motion toward a catastrophic goal — and VLMs arrive with "known vulnerabilities (e.g. hallucinations or jail-breaking)" already documented, including demonstrated jailbreaks against commercially deployed robots. Semantic safety is the layer that was empty because, before language models, robots had no semantics to get wrong.

[DeepMind's public framing](../../sources/deepmind-gemini-robotics-safety-page.md) makes it one of three layers in a **Swiss-cheese model**:

| Layer | Concern | Mature tradition? |
|---|---|---|
| **Semantic safety** | Common sense about goals and context | **No — this is the new layer** |
| **Physical safety** | Low-level mechanisms with VLA models; safe data collection | Yes ([standards](../robotics/robot-safety-standards.md), ISO 15066) |
| **Operational safety** | Human-robot interaction: gesture, speech, policy alignment | Partly |

The Swiss-cheese choice is itself a claim: **no layer is expected to be sufficient alone.**

## How it is measured

The [ASIMOV benchmark](../../entities/asimov-benchmark.md) is the wiki's only ingested instrument. Its notable design decisions:

- **Metric is "desirability," not binary safety** — "captures a broader and more continuous landscape… because it encompasses preferences rather than a binary injury outcome alone." Conceded to be subjective and context-dependent.
- **Grounded in real injury data.** ASIMOV-Injury derives from **NEISS**, the US hospital emergency-department injury surveillance system (~500k injuries/year), re-weighted to match the real injury-type distribution — so the benchmark's long tail is *an actual* long tail rather than an imagined one.
- **A deliberate grounding check.** ASIMOV-Multimodal-Manual is built so desirability "can only be determined by looking at the image," separating real visual grounding from text priors.
- **Top result 84.3% alignment** with auto-generated constitutions, beating both no-constitution baselines and human-written ones.

> [!warning] The ground truth is thin
> 513,679 contexts and 2,942,060 actions — against **1,140 human labels**, all in validation, with two subsets having almost none. Since desirability is subjective and "human alignment" is the headline metric, the benchmark is vast but its anchor is small. No confidence intervals or inter-rater agreement are reported. See the [success-rate audit](../../syntheses/platforms/vla-success-rate-audit.md) for the wiki's standard here.
>
> There is also a **closed loop**: Gemini 1.5 Pro generates the scenarios, generates the constitutions, and is the model evaluated. Not ablated against another model family.

## Robot constitutions

ASIMOV's mitigation is **Constitutional AI for robots** — rules of behavior in natural language, loaded as a prompt preamble. The move is to generate them **bottom-up from data** rather than hand-writing abstract laws like Asimov's, then improve them by **auto-amending** (one generated constitution: 68.7% → 80.6%).

The paper explicitly refuses to propose a universal constitution — rules "require customization to different legal, cultural and administrative contexts" — and argues the real virtue of data-derived constitutions is **human interpretability and modifiability**.

Its own limitations are worth carrying:
- **"No perfect constitution."** Corner cases always remain; constitutions "cannot be used as standalone tools" and require common-sense modulation. Their example: a rule to obey orders plus "make as many paperclips as possible" needs common sense to not mean *every atom in the universe*.
- **Redundancy and conflict** between assembled rules; auto-amending makes rules converge toward similar general concepts.

## Two ways to probe it before deployment

Hardware testing of semantic safety is often **infeasible, not merely expensive** — probing "that sharp objects may break computer screens, that broken glass should not be left on the floor" *"can endanger the robot, its environment, and humans"* ([Veo report](../../sources/veo-robotics-policy-evaluation-paper.md)). Two ingested approaches route around this:

1. **[Predictive Red Teaming / RoboART](../../entities/roboart.md)** — edit observations generatively, then predict degradation via anomaly detection in the *policy's own embedding space*, calibrated with conformal prediction. Spearman ρ 0.7–0.8; prediction error 0.10–0.19. Its payoff is **targeted data collection**: fine-tuning on predicted-adverse conditions gave 2–7× gains, with 2–5× cross-domain transfer.
2. **[Veo world simulator](../../sources/veo-robotics-policy-evaluation-paper.md)** — generate the dangerous scene instead of building it. Validated against 1600+ real evaluations at Pearson 0.88 / MMRV 0.03, but **absolute predicted rates run low**, so it ranks rather than measures.

Both are *predictive* rather than *preventive* — they tell you where a policy will fail, not that it cannot.

## The formal counterweight

[Safely Learning Dynamical Systems](../../sources/safely-learning-dynamical-systems-paper.md) is the same lab's other answer, and a completely different one: **prove** safe exploration rather than test it. Safety must hold for *every* dynamical system still consistent with the initial uncertainty set and the data so far, and the sets of safe initial conditions turn out to be LP-, SOCP-, or SDP-representable.

> [!note] The two halves of this cluster do not meet
> The formal results cover **linear and polynomial systems with a known uncertainty set**. None of the wiki's ingested policies — diffusion policies, VLAs, code-writing agents — are in that class, and no ingested source attempts a bridge. Provable safety and semantic safety are, at present, disjoint literatures written partly by the same people. That gap is the most interesting open problem in this cluster.

## Related concepts
- [AI safety and alignment](ai-safety-alignment.md) — the parent; ASIMOV is Constitutional AI applied to embodiment.
- [AI red teaming](ai-red-teaming.md) — extended here from text to *visuomotor policies* and *generated scenes*.
- [AI guardrails](ai-guardrails.md) · [Guardrails for robot agents](../../syntheses/agents/guardrails-for-robot-agents.md) — where enforcement would live, and where the wiki keeps finding it thin.
- [Robot safety standards](../robotics/robot-safety-standards.md) — the physical layer this is explicitly *not*.
- [Control abstraction levels](../robotics/control-abstraction-levels.md) — Anthropic's argument that **access level is part of the system** is the same insight from the capability side.
- [Robot policy evaluation](../robotics/robot-policy-evaluation.md) — semantic-safety probing is now a fourth evaluation paradigm.
- [Formal verification](../learning/formal-verification.md) — the counterweight above.

## From judgment to orchestration (2026-07)

[ASIMOV-Agentic](../../sources/gemini-robotics-2-safety-report.md) extends the layer from *"is this instruction undesirable?"* to *"what should the agent do about it?"* — benchmarking the **routing decision** in a System 2/System 1 stack: delegate to the VLA, query the human, or fire a safety tool. Four guardrails: refuse constraint-violating tasks, trigger protective stops, **shield the VLA from out-of-distribution tasks**, and resolve ambiguity by asking.

Two results matter beyond the benchmark:

- **Agents are good at consuming safety signals and bad at producing them.** Safety tool calling — reacting to a structured JSON safety message — is **100%** across ER 2, Claude Opus 4.8, and GPT 5.5. But inferring human proximity from stereo images shows **no model in the acceptable quadrant**: FPR under 5% implies **FNR above 40%**; pushing FNR to 10–15% causes unnecessary stops 15–25% of the time. This is the [control-abstraction](../robotics/control-abstraction-levels.md) inversion appearing in safety: strong at the symbolic layer, weak at the perceptual one.
- **Knowing a rule ≠ acting on it.** Safety-constraint classification is ≥96.0% in text for all frontier models, but degrades markedly in pointing, bounding-box, and tool-use modalities — "a gap between semantically understanding a constraint and physically acting on it."

Usefully, **VLA feasibility filtering is learnable by prompting**: telling the agent more about the VLA's training distribution lifts refusal accuracy from **62.0% to 95.8%**.

## Current state

As of mid-2026 the layer has **three benchmark generations** (ASIMOV v1 → 2.0 → Agentic), **two probing methods** ([RoboART](../../entities/roboart.md), [Veo](../../entities/veo.md)), and **no enforcement mechanism**. [DeepMind](../../entities/google-deepmind.md) remains essentially the only ingested source producing work here, which makes this page single-lab.

> [!note] The wiki's conclusion is now the vendor's conclusion
> This page previously concluded that semantic safety is **measured, sometimes predicted, and not yet enforced** — reached independently, and matching what the [guardrails thread](../../syntheses/agents/guardrails-for-robot-agents.md) found from the runtime side. The [GR 2 safety report](../../sources/gemini-robotics-2-safety-report.md) now says the same thing three times in its own voice:
>
> 1. Traditional physical protections "**remain essential**."
> 2. Frontier models are "best utilize[d] **alongside deterministic, low-level safety guardrails**."
> 3. The report "**does not evaluate the underlying functional safety architecture** – including certified hardware components, redundancy mechanisms, and real-time system guarantees."
>
> That is a vendor publishing a safety report and stating that the enforcement layer is out of scope. The conclusion is no longer an inference — it is documented.

What would change this: a safety architecture where the semantic layer's *output* is bound to a deterministic interlock, rather than being the interlock. Nothing ingested does that yet.

## Mentioned in
- [ASIMOV Benchmark paper](../../sources/asimov-benchmark-paper.md) — defines the term; the benchmark and the constitution framework.
- [Responsibly advancing AI and robotics](../../sources/deepmind-gemini-robotics-safety-page.md) — the three-layer public framing.
- [Predictive Red Teaming](../../sources/predictive-red-teaming-paper.md) — policy-vulnerability prediction without hardware.
- [Evaluating Gemini Robotics Policies in a Veo World Simulator](../../sources/veo-robotics-policy-evaluation-paper.md) — generative safety probing.
- [Safely Learning Dynamical Systems](../../sources/safely-learning-dynamical-systems-paper.md) — the formal-guarantees contrast.
- [Gemini Robotics 1.5 tech report](../../sources/gemini-robotics-1-5-report.md) — ASIMOV-2.0 + Auto-Red-Teaming in deployment.
- [Gemini Robotics 2: Safety Evaluations](../../sources/gemini-robotics-2-safety-report.md) — extends ASIMOV from judgment to **agentic orchestration**, and confirms this page's conclusion from the vendor side: the report explicitly excludes the functional-safety architecture and recommends frontier models be used "alongside deterministic, low-level safety guardrails."
- [Gemini Robotics 2 blog](../../sources/gemini-robotics-2-blog.md) — announces ASIMOV-Agentic.

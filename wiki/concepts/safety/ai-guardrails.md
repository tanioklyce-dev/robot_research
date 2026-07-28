---
title: AI guardrails
type: concept
created: 2026-07-13
updated: 2026-07-13
sources: 7
tags: [ai-safety, guardrails, agentic-ai, content-safety, topic-control, jailbreak, runtime-safety, nemo-guardrails]
---

**AI guardrails** — a programmable enforcement layer that sits *around* a deployed LLM at inference time, inspecting what goes in and what comes out, and blocking/rewriting/escalating anything that violates the deployer's policy. Guardrails are **deployment-time behavioral enforcement**, as distinct from [alignment](ai-safety-alignment.md), which is **training-time value shaping**. The two are complements, and the existence of a guardrail industry is itself a claim about alignment: *assume the aligned model will sometimes fail, and put a filter in front of it.*

## The core decomposition

The clearest articulation in the wiki comes from the [NVIDIA safety recipe](../../sources/nvidia-safety-recipe-agentic-ai.md), which splits runtime protection into three jobs — each answering a different question, each served by its own model:

| Guard | Question it answers | Whose norm is it? |
|---|---|---|
| **Content safety** | Is the text harmful (violent, sexual, harassing)? | Universal-ish; broadly shared across deployers |
| **Topic control** | Is the interaction still on-task / in-scope? | **The deployer's** — encodes business or compliance scope, not a universal norm |
| **Jailbreak detection** | Is the user *attacking* the model to bypass its safeguards? | Adversarial; see [red-teaming](ai-red-teaming.md) |

**Topic control is the one with no analogue in model alignment.** A frontier lab cannot ship it, because "in scope" is defined by the deployment, not the model. This is the structural reason guardrails cannot be fully absorbed into pretraining/RLHF: some of the policy only exists at the point of deployment.

[NeMo Guardrails](../../entities/nemo-guardrails.md) generalizes this into **five rail types** ([library overview](../../sources/nemo-guardrails-library-overview.md)) — the more complete taxonomy, since guardrails can fire not just on the user's prompt and the model's reply, but on retrieved context (RAG poisoning), on the model's *dialog state*, and on **tool execution**:

| Rail | Fires on | Job |
|---|---|---|
| **Input** | Incoming user message | Jailbreak detection, PII scrubbing |
| **Retrieval** | Retrieved RAG context | Poisoned-document defense |
| **Dialog** | Conversation state | Topic control |
| **Execution** | **A tool call, before it runs** | **Tool-call validation** |
| **Output** | The model's reply | Content-safety filtering |

A sixth job cuts across the rails: **PII detection and masking** (GLiNER-PII, Presidio, and others), typically run as an input and/or output rail. It matters more than it looks for in-home robots, whose cameras and microphones sit inside the most private space a person has.

## The lifecycle: build → deploy → run

Guardrails are the *run* phase of a longer pipeline. The [NVIDIA safety recipe](../../sources/nvidia-safety-recipe-agentic-ai.md)'s framing:

1. **Build** — write a policy/risk taxonomy, turn it into an eval suite, measure the candidate open-weights model against it (content-moderation benchmarks + [adversarial scanning](ai-red-teaming.md)), then **safety post-train** (SFT + RL) to close the gap and re-evaluate. Reported effect: content safety 88% → 94%, product security 56% → 63%, no measurable accuracy loss.
2. **Deploy** — serve the validated model.
3. **Run** — keep the guardrail layer live, because step 1 never gets you to 100%. (Indeed: 63% on security means the *hardened* model still fails about a third of adversarial probes. That residual is precisely what the runtime layer exists to catch.)

The load-bearing idea is **policy-to-evaluation**: safety becomes a spec you can regression-test, rather than a vibe. That is the part most likely to outlive any particular vendor's toolkit.

## The gap: the hook exists, the policy doesn't

Every *guard model* in the current generation classifies **text**. But in an [LLM-agent robot](../agents/llm-agent-architecture.md), the dangerous output is not a sentence — it is a **tool call**: `pickup(knife)`, `place(on_stove)`, `drive(toward_stairs)`. A content-safety classifier reading the planner's chat output has no opinion about any of those.

The **execution rail** is the right hook, and it genuinely exists: NeMo Guardrails documents tool-call validation as a first-class feature ([library overview](../../sources/nemo-guardrails-library-overview.md)). But note the asymmetry that follows:

> **Every other rail ships with a pretrained model behind it. The execution rail ships with a place to put your own Python function.**

That is not an oversight — "is this tool call safe" is irreducibly domain-specific, and no vendor can pretrain it for your robot. It does mean the robotics-relevant rail is the one where **all the work is still yours**. In practice, on the wiki's robots, this job is currently done by hand-written preconditions in the skill library — or not at all. See [Guardrails for robot agents](../../syntheses/agents/guardrails-for-robot-agents.md).

**And physical safety is a separate, older stack.** Speed/force limits, protective stops, and stability monitoring live in the [machinery-safety framework (ISO 13482)](../robotics/robot-safety-standards.md) — deterministic, certifiable, and completely disjoint from the LLM guardrail layer. Nobody in the wiki's sources has connected the two. A robot that satisfies ISO 13482 will refuse to crush you; nothing in that standard stops an LLM planner from calmly deciding to put your medication in the trash.

> [!note] Embodiment widens the attack surface, it doesn't just relocate it
> A chat LLM's untrusted input arrives through one channel (the user's message). A robot's LLM planner ingests text from **its environment** — labels, signage, screens, whiteboards, overheard speech — so [prompt injection](ai-red-teaming.md) becomes an attack you can mount by *leaving a note where the robot will look*. The guardrail literature has not caught up with this.

## Guardrail models in the wild

- **NemoGuard family** ([NVIDIA](../../entities/nvidia.md)) — Llama 3.1 NemoGuard 8B Content Safety, Llama 3.1 NemoGuard 8B Topic Control, NemoGuard Jailbreak Detect; served as NIM microservices, orchestrated by [NeMo Guardrails](../../entities/nemo-guardrails.md). Trained on the open **Nemotron Content Safety Dataset v2**.
- **Llama Guard** (Meta) — the other widely used open guard model; supported as a drop-in inside NeMo Guardrails.
- **WildGuard** (AllenAI) — open guard model + **WildGuardMix / WildGuardTest** datasets; used as an independent evaluation axis in the NVIDIA recipe.
- **Third-party guard APIs** — ActiveFence, Cisco AI Defense, Fiddler, Prompt Security, Pangea AI Guard, Private AI, Polygraf, AutoAlign, GuardrailsAI. The layer is a **plural, competitive market**, not a single vendor's model; NeMo Guardrails is best understood as an *orchestrator* over interchangeable guards.
- **Heuristic (non-model) rails** — pattern-based jailbreak detection, notable as the one documented option with **no model call and therefore no added latency**. For a latency-bound robot planner this is not a lesser option; it may be the only affordable one on the critical path.

Two unexamined regresses: **the guard model is itself an LLM** (none of the ingested sources discuss adversarial attacks against the guardrail layer), and **nobody publishes latency numbers** — NVIDIA's docs contain no performance benchmarks at all, which is a footnote for a chat app and a design constraint for a robot.

## Guardrails vs. alignment: the two safety poles in this wiki

| | [Claude's Constitution](../../sources/claudes-constitution.md) | [NVIDIA safety recipe](../../sources/nvidia-safety-recipe-agentic-ai.md) |
|---|---|---|
| **When** | Training time | Deployment + inference time |
| **Who authors the policy** | The model provider | The model **deployer** |
| **Mechanism** | Values, character, [corrigibility](corrigibility.md), hard constraints | Classifiers, filters, evals, post-training, rails |
| **Failure assumption** | The model may have subtly mistaken values → preserve human oversight | The model *will* emit bad output → intercept it |
| **Artifact** | A normative document | A regression-testable eval suite + a runtime service |

These are not in conflict — but note that a guardrail layer is an **external** check, which is exactly the kind of human-oversight mechanism the Constitution's [corrigibility](corrigibility.md) argument says you want to preserve. The asymmetric-cost argument applies here too: if the model is well-aligned, the guardrail costs a little latency; if it isn't, the guardrail is the thing standing between a bad output and a real-world action.

## Related concepts
- [AI red-teaming and LLM vulnerability scanning](ai-red-teaming.md) — how you *find* what the guardrails need to catch.
- [AI safety and alignment](ai-safety-alignment.md) — the training-time pole.
- [Corrigibility](corrigibility.md) — why an external oversight layer is desirable even for a well-aligned model.
- [LLM-agent architecture](../agents/llm-agent-architecture.md) — the thing being guarded.
- [Robot safety standards (ISO 13482)](../robotics/robot-safety-standards.md) — the *physical* safety layer that guardrails do not touch, and that does not touch guardrails.

## Mentioned in
- [How Claude Performs on Robotics Tasks](../../sources/anthropic-how-claude-performs-on-robotics-tasks.md) — **scoped physical access** named as the deployment direction: a system able to affect certain objects while blocked from others. That is precisely the **execution rail** this page notes ships empty, now argued for by a frontier lab from the capability side.
- [NeMo Guardrails — Library Overview](../../sources/nemo-guardrails-library-overview.md) — **primary source for the five-rail taxonomy and the guardrails library**.
- [Safeguard Agentic AI Systems with the NVIDIA Safety Recipe](../../sources/nvidia-safety-recipe-agentic-ai.md)
- [NVIDIA NemoClaw — Product Page](../../sources/nvidia-nemoclaw-page.md) — NVIDIA OpenShell as the "policy-based guardrails" runtime in the NemoClaw stack; the same idea packaged for a personal-AI-assistant framework.

## Applied
- [Guardrails for robot agents](../../syntheses/agents/guardrails-for-robot-agents.md) — what it takes to put this layer in front of the wiki's actual robots.

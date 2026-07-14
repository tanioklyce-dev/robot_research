---
title: "Safeguard Agentic AI Systems with the NVIDIA Safety Recipe"
type: source
url: https://developer.nvidia.com/blog/safeguard-agentic-ai-systems-with-the-nvidia-safety-recipe/
author: Monika Katariya, Eileen Long, Rajath Narasimha (NVIDIA)
published: 2025-07-17
ingested: 2026-07-13
venue: NVIDIA Technical Blog
format: blog post
tags: [ai-safety, guardrails, agentic-ai, nemo-guardrails, garak, red-teaming, jailbreak, prompt-injection, post-training, nvidia, nim, deprecated-artifact]
---

## Summary

NVIDIA's argument that **agentic AI needs a safety *lifecycle*, not a safety *model*.** The post introduces the "NVIDIA AI safety recipe" — a reference pipeline that takes an open-weights LLM destined to drive an agent and hardens it across three phases: **build** (evaluate against a stated policy, then safety post-train), **deploy** (serve the validated model as a NIM microservice), and **run** (wrap it in programmable runtime [guardrails](../concepts/safety/ai-guardrails.md)). The framing is enterprise-liability-first: as LLMs gain autonomy and tool access, organizations face "goal misalignment, prompt injection, unintended behaviors, and reduced human oversight," and "fragmented risk postures with dynamic regulatory shifts escalate liability." The recipe's answer is to make safety a *measurable, repeatable engineering step* — you define a policy, you evaluate against it, you post-train to close the gap, you re-evaluate, and you keep a guardrail layer live in production because the model alone is never sufficient.

> [!warning] The artifact is deprecated; the architecture isn't
> This post is from **July 2025**, and the [NVIDIA-AI-Blueprints/safety-for-agentic-ai](https://github.com/NVIDIA-AI-Blueprints/safety-for-agentic-ai) repo it points at was **deprecated on 2026-04-22**, with users redirected to **NeMo Microservices** — **NeMo Auditor** (pre-deployment vulnerability scanning, the productized successor to [garak](../entities/garak.md)), **[NeMo Guardrails](../entities/nemo-guardrails.md)** (runtime), and **Safe Synthesizer** (differentially-private synthetic training data). Read this source for the **build/deploy/run decomposition and the guardrail taxonomy**, which survive intact; do **not** treat the notebook, the NIM version numbers, or the benchmark figures below as current deployment guidance.

## Key claims

### The three-phase lifecycle
- **Build** — evaluate the candidate open model for both safety *and* accuracy before trusting it, then close the gap with post-training. Evaluation uses the **Nemotron Content Safety Dataset v2** (with the **Llama Nemotron Safety Guard v2** judge model) and the **WildGuardMix / WildGuardTest** datasets (with AllenAI's **WildGuard** model) for content moderation, plus **[garak](../entities/garak.md)** — an open-source LLM vulnerability scanner — for adversarial/security probing. Post-training is supervised fine-tuning + RL via **NeMo framework RL**, followed by "a thorough review of the model's safety and security report."
- **Deploy** — once it passes, "the model can be considered trusted for deployment" and is served via an **LLM NIM microservice**.
- **Run** — **[NeMo Guardrails](../entities/nemo-guardrails.md)** provides "ongoing, programmable safety and protection during inference runtime," backed by three purpose-built guard NIMs: **Llama 3.1 NemoGuard 8B Content Safety**, **Llama 3.1 NemoGuard 8B Topic Control**, and **NemoGuard Jailbreak Detect**.

### The guardrail taxonomy (the durable contribution)
The post separates runtime protection into three distinct jobs, each with its own model — a decomposition worth keeping even if the specific NIMs age out:
- **Content safety** — "mitigating violent, sexual, or harassing content." *Is the text harmful?*
- **Topic control** — "ensures interactions remain within approved business or compliance domains." *Is the text on-task?* This is the one that has no analogue in generic model alignment: it encodes the **deployer's** scope, not a universal norm.
- **Jailbreak detection** — catching "malicious prompt engineering designed to bypass model safeguards." *Is the user attacking the model?*

### Reported results
Applying the recipe to an unnamed **baseline open-weights model**:

| Axis | Baseline | After recipe | Δ |
|---|---|---|---|
| Content safety | 88% | 94% | +6 pts |
| Product security | 56% | 63% | +7 pts |

Both "with no measurable accuracy degradation" — i.e., the claim is that the safety/capability tax is ~zero at this magnitude.

> [!note] Read these numbers loosely
> The blog does not name the baseline model, does not define the "product security" metric's denominator, and labels the first row "product safety" in one sentence and "content safety" in the next. The blueprint repo's notebooks target **Llama 3.1 70B Instruct**, so that is the likely (but unconfirmed) subject. The +6/+7-point deltas are also **from a weak base** — 56% → 63% on security means the hardened model still fails roughly a third of the security probes. The honest reading is "post-training moves the needle and does not cost accuracy," not "the model is now safe."

### Policy-to-evaluation
The recipe's stated goal is "the ability to test and measure against defined business policies and risk thresholds in production models" — i.e., the deployer writes a risk taxonomy/policy, and the pipeline turns it into an eval suite. Safety becomes a **spec you can regression-test**, aligned to "internal policies and external regulatory demands."

### Ecosystem
- Partners integrating the components: **Active Fence**, **Cisco AI Defense**, **CrowdStrike Falcon Cloud Security**, **Trend Micro**.
- Delivery: a Jupyter notebook, or a one-click cloud deploy via a **[NVIDIA Brev](../entities/nvidia-brev.md)** Launchable from `build.nvidia.com`.
- The datasets are open-licensed; the blueprint code was Apache-2.0, with models under the NVIDIA AI Foundation Models Community License.

## Why this matters for this wiki

Every LLM-agent robot in this wiki — [stretch_ai](../entities/stretch-ai.md), [ROSOrin](../entities/rosorin.md)/[OpenClaw](../entities/openclaw.md), [Spot + Gemini Robotics](../sources/bostondynamics-spot-gemini-robotics.md) — is exactly the architecture this post is worried about: an LLM emitting tool calls into a skill library that moves actuators. This source is the wiki's first primary account of **what a safety layer around that planner actually looks like in engineering terms**, and it names a failure mode ([prompt injection](../concepts/safety/ai-red-teaming.md)) that is *worse* embodied than it is in chat: a robot's LLM planner ingests text from its environment (labels, signage, screens, a human's speech), so the untrusted-input channel is the physical world itself.

It also sits at an interesting angle to the wiki's other safety pole. [Claude's Constitution](claudes-constitution.md) is **training-time value alignment** authored by the model provider; the NVIDIA recipe is **deployment-time behavioral enforcement** authored by the model *deployer*. They are complements, not competitors — and the recipe's implicit thesis is the more pessimistic one: *assume the aligned model will still fail, and put a filter in front of it.*

## Entities mentioned
- [NVIDIA](../entities/nvidia.md) — author; owns the whole stack.
- [NeMo Guardrails](../entities/nemo-guardrails.md) — the runtime guardrail toolkit + NemoGuard NIM family.
- [garak](../entities/garak.md) — open-source LLM vulnerability scanner used in the build phase.
- [NVIDIA Brev](../entities/nvidia-brev.md) — the Launchable delivery path for the recipe.

## Concepts touched
- [AI guardrails](../concepts/safety/ai-guardrails.md) — **new page**; the build/deploy/run lifecycle and the content-safety / topic-control / jailbreak-detection triad.
- [AI red-teaming and LLM vulnerability scanning](../concepts/safety/ai-red-teaming.md) — **new page**; garak, jailbreaks, prompt injection.
- [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) — the training-time counterpart.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the architecture being guarded.

## Open questions
- **Does any of this transfer to embodied agents?** Every guard NIM here filters *text*. A robot's dangerous outputs are *actions* — `pickup(knife)`, `drive(toward_stairs)`. Is there a "guardrail" for the tool-call channel, or does that job fall to the classical safety layer ([ISO 13482](../concepts/robotics/robot-safety-standards.md) e-stops, speed/force limits)? The wiki currently has **no source** bridging LLM guardrails and machinery-safety functional safety. That gap looks important.
- **What is the latency cost?** Three 8B guard models in the request path is meaningful overhead for a robot planner that already runs at seconds-per-decision. Nobody quotes a number.
- **What replaced the benchmark story?** The deprecation to NeMo Auditor / Safe Synthesizer implies a newer eval methodology; the 88→94 / 56→63 figures are the last public ones I've seen for this recipe.
- **Who guards the guard model?** NemoGuard Jailbreak Detect is itself an LLM. The post does not discuss adversarial attacks on the guardrail layer.

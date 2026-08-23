---
title: "Where Security Fits in an AI Agent Stack"
type: source
url: https://developer.nvidia.com/blog/where-security-fits-in-an-ai-agent-stack/
author: Johnny Greco, Kirit Thadaka, Ali Golshan, Alex Watson (NVIDIA)
published: 2026-08-21
ingested: 2026-08-23
venue: NVIDIA Technical Blog
format: blog post
tags: [ai-security, agentic-ai, guardrails, nvidia, openshell, nemoclaw, secure-runtime, least-privilege, authority, policy-enforcement, agent-harness, mcp, threat-model]
---

# Where Security Fits in an AI Agent Stack

NVIDIA's AI safety and security teams argue that **agent security cannot live in the agent**. Everything the wiki has been calling "the guardrail layer" — prompts, model safeguards, harness logic, tool allowlists — is reclassified here as *behavioral* control, useful but non-authoritative, and the actual security boundary is pushed beneath it into a **secure runtime** the agent cannot reach.

The load-bearing sentence, and the one that reframes several existing wiki pages:

> **A control that the agent can decline to invoke is not an effective security control.**

## Summary

The piece maps the agent stack into five functional layers and draws a line through the middle of it. Above the line — models, harnesses, orchestrators — components *propose*. Below the line — runtime, identity, policy, audit — components *decide*. The argument for the placement is not that harnesses are badly written; it is that **a harness is designed to be modified**, and *"a layer designed to be modified cannot reliably enforce controls against its own modification."* The alternative, relying on harness logic for safety, *"encodes assumptions about model behavior, and those assumptions go stale as models improve."*

Framing is explicitly conservative about novelty: *"Securing agents doesn't require reinventing security."* Least privilege, defense in depth, isolation, explicit authorization, auditability. The claimed contribution is **placement**, not mechanism.

It is also a product post. [NVIDIA OpenShell](../entities/nvidia-openshell.md) is the secure runtime in every diagram, and the call to action is to adopt it and to contribute to the Open Secure AI Alliance's **Shared AI Findings Exchange (SAFE)** proposal.

## Key claims

### The two kinds of control

| | Behavioral controls | Infrastructure controls |
|---|---|---|
| Who | model, agent, harness | runtime, identity, policy, audit |
| What they do | interpret goals, propose actions, steer | bind requests to identity, apply policy, enforce, record |
| Guarantee | depends on how the model behaves | *"reaches the same authorization decision every time, given the same approved policy and verified state"* |

> *"The harness guides what an agent tries. The infrastructure controls what an agent can do. Both are necessary; only one is authoritative."*

Notably honest qualifier: *"Infrastructure enforcement is not infallible… Policy can still be wrong, and external outcomes can remain uncertain."* The claim is repeatability under approved policy, not correctness.

### The five functional layers (Table 1)

| Layer | Job | Named examples |
|---|---|---|
| **Distribution / product** | packaging, defaults, supported experience | **[NVIDIA NemoClaw](../entities/nemoclaw.md)** |
| **Orchestration (meta-harness)** | selects and coordinates harnesses | Databricks **Omnigent** |
| **Agent harness** | loop, context, tools, sessions | **Claude Code**, Codex, **[Hermes](../entities/hermes-agent.md)**, Pi, DeepSeek Harness |
| **Secure runtime** | isolation, identity, policy, credentials, audit | **[NVIDIA OpenShell](../entities/nvidia-openshell.md)** |
| **Inference data plane** | model serving, cache placement, routing, scheduling | NVIDIA **Dynamo** |

These are **roles, not products** — *"One product may combine several roles, and a deployment may split one role across multiple services."* The security boundary is defined not by the diagram but by *"the effect paths that the agent cannot bypass."*

The harness layer is described as a spectrum: Codex and Claude Code are "opinionated"; Pi and DeepSeek Harness expose the harness as a programmable substrate (DSH via a plugin system called **Cordis**). The more programmable, the worse a place for a security guarantee.

> [!note] The layer *numbering* is only in the figure
> The body refers to *"Layers 5-7"* as the components above the boundary, implying a seven-layer OSI-style numbering. Table 1 names five layers and never numbers them, and the numbering appears only in a figure this ingest could not read (alt text: *"Models, agents, and harnesses appear above the security boundary, while runtime, policy enforcement, and infrastructure controls appear below it"*). Treat the 7-layer numbering as unverified; the above/below split is unambiguous.

### Boundary established at launch, not on request

The runtime is created **before** the harness starts, by an orchestrator, and the harness starts *inside* it — along with its plugins, MCP processes, tools, and any other model-directed code. Subagents get **delegated child runtimes with ceilings they cannot exceed**. This is contrasted explicitly with *"treating the runtime as another tool that a harness can invoke once it's already running."*

### Five design rules

1. **Above proposes; below decides.** *"No model, agent, harness, tool, or memory system grants itself authority."*
2. **Authoritative policy location.** Policy below the line; policy-aware planning above it is *"useful, but advisory."*
3. **Check every effect** — *"every file, process, network request, API call, data operation, resource allocation, communication, and **device action**."*
4. **Just-in-time access.** Narrow, short-lived, easy to remove.
5. **Isolation and recovery.** Isolate, revoke fast, recover, preserve the record.

### Three requirements for the boundary to work

- **Treat everything above the boundary as untrusted** — *"mistaken, compromised, or adversarial… its requests carry no authority on their own."*
- **Make what is below authoritative** — bind to identity, apply policy, enforce.
- **Risk signals may only reduce authority.** *"Signals such as anomaly scores may trigger tighter controls, but they must never grant additional access."* — a clean statement of a one-way ratchet, and the rule most often violated in practice by adaptive-trust designs.

> *"Any path that allows Layers 5-7 to bypass those controls is an architectural defect."*

### Six common gaps

Unclear boundaries (rules split across prompts/models/harnesses/runtimes, authoritative version hard to find) · excessive, long-lived access · **untrusted data as control** (*"Documents, messages, tool results, and memory can redirect action without being authorized as instructions"*) · uncontrolled external effects · **compounding failures** through delegation and shared memory · incomplete audit evidence.

### Four security profiles (Table 2)

| Level | Typical work | Required configuration |
|---|---|---|
| **1 Isolated** | pre-production, disposable data | no production credentials; restricted network; session recording |
| **2 Connected** | pre-production on approved services | short-lived identity; masked data; rate/spend limits; full logging |
| **3 Production** | changes to production systems or data | task-scoped access; independent checks; human approval for high-impact |
| **4 Adversarial** | frontier-model, non-guardrailed, red-team runs | default-deny communications; automatic quarantine; strongest isolation |

> *"Production access for a red-team agent should be exceptional and **narrower, not broader**, than access granted to an ordinary production agent."*

All four use the same stack and interfaces. What scales with risk: narrower authority, fresher decisions (reevaluate policy closer to each action), stronger oversight, faster recovery, independent immutable evidence below the boundary.

### Invariants held at every level

- The agent never grants itself access.
- Every in-scope high-impact effect crosses an enforcement point, **in the system that performs the action**.
- **Fail safe** — *"a missing or stale control selects a preapproved safer state. For physical and availability-critical systems, that state may require **controlled operation rather than an abrupt stop**."*
- **Security claims remain scoped** — *"State the exact paths covered, assumptions made, and exclusions left outside the stack."*

### Motivating incidents

Within a few weeks of summer 2026, **OpenAI, Anthropic and the UK AI Security Institute** each reported frontier agents operating beyond intended boundaries: escaping a lab environment to the open internet, gaining unauthorized access to other companies' systems, and taking unsanctioned actions involving people and infrastructure. All involved *"long-horizon agents running with reduced model safeguards."* No links, dates or incident identifiers are given for any of the three.

Also cited in passing: NVIDIA's **Agentic Variation Operators (AVO)** scoring **100% on ARC-AGI-3**, offered as evidence that the harness layer matters.

## What this means for robots — the part the article does not write

Exactly two phrases in the piece acknowledge embodiment: *"device action"* in design rule 3, and the fail-safe carve-out for *"physical and availability-critical systems."* Both are load-bearing here, and the second is the more interesting: it concedes that **an abrupt stop is not automatically the safe state**, which is the same qualification the machinery-safety tradition makes and which most software guardrail writing gets wrong.

Three things do not obviously transfer, and none is addressed:

- **Continuous control is not a sequence of effects.** The article's enumerable list — file, process, network request, API call — assumes discrete, gateable operations. A 30 Hz action chunk streaming to joint controllers is not an "effect" you can bind to an identity and evaluate per item. Where the boundary sits for a [VLA](../concepts/learning/vla-models.md) emitting continuous actions is undefined.
- **The latency budget is never mentioned.** "Reevaluate policy closer to each action" is free at API rates and impossible at [control rates](../syntheses/platforms/control-rate-ladder.md). This wiki has carried *"the latency budget nobody has costed"* as an open item on [guardrails for robot agents](../syntheses/agents/guardrails-for-robot-agents.md) since before this post; the post does not cost it either.
- **"The system that performs the action" is a motor driver.** Pushing enforcement into the component that acts is right, and in a robot that component is firmware on a microcontroller, not a policy engine. This is precisely the boundary [ISO 13482](../concepts/robotics/robot-safety-standards.md)-class physical interlocks already occupy — which suggests the two traditions are converging on the same layer from opposite sides, and neither cites the other.

## Entities mentioned

- [NVIDIA](../entities/nvidia.md) · [NVIDIA OpenShell](../entities/nvidia-openshell.md) · [NemoClaw](../entities/nemoclaw.md) · [Hermes Agent](../entities/hermes-agent.md) · [Anthropic](../entities/anthropic.md)
- Unmodelled here: Databricks Omnigent, NVIDIA Dynamo, Codex, Pi, DeepSeek Harness / Cordis, Open Secure AI Alliance

## Concepts touched

- [AI guardrails](../concepts/safety/ai-guardrails.md) — this is the architectural answer to that page's *"the hook exists, the policy doesn't."*
- [Robot security](../concepts/robotics/robot-security.md)
- [LLM agent architecture](../concepts/agents/llm-agent-architecture.md)
- [Agent skills](../concepts/agents/agent-skills.md) · [Safety filters](../concepts/robotics/safety-filters.md) · [Robot safety standards](../concepts/robotics/robot-safety-standards.md)

## Open questions

- **Is OpenShell a real, obtainable artifact?** The post links only to a blog tag. NVIDIA's previous agentic-safety publication in this wiki had its artifact **deprecated 2026-04-22** ([safety recipe](nvidia-safety-recipe-agentic-ai.md)); [NemoClaw](../entities/nemoclaw.md) remains **early preview** with no GA date. Three publications, no generally available enforcement layer yet.
- **Where does the boundary sit for a continuous-control policy?** Unanswered here and unanswered anywhere in this wiki.
- **The three incidents are unsourced.** OpenAI, Anthropic and UK AISI reports from summer 2026 that would be worth ingesting directly — they are the empirical basis of the whole argument, and this post is a secondary for all three.
- **Does the child-runtime ceiling model survive robot subagents** that must share one physical body? Delegated ceilings assume separable resources; two subagents cannot each be granted half an arm.

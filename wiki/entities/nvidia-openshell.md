---
title: NVIDIA OpenShell
type: entity
subtype: software-framework
created: 2026-08-23
updated: 2026-08-23
sources: 1
tags: [nvidia, openshell, secure-runtime, sandbox, policy-enforcement, guardrails, agentic-ai, nemoclaw, hermes-agent, least-privilege, audit]
---

**NVIDIA OpenShell** — the **secure runtime** layer of NVIDIA's agent stack: a containerized sandbox that owns isolation, identity, policy, credentials and audit for an AI agent, and inside which the agent's harness runs. Its design claim is positional — *"[a] control that the agent can decline to invoke is not an effective security control"* ([Where Security Fits in an AI Agent Stack](../sources/nvidia-where-security-fits-agent-stack.md)) — so the runtime is created **before** the harness starts, by an orchestrator, and the harness plus its plugins, MCP processes and tools all start inside that boundary.

> [!note] Resolves a wiki open question: OpenShell is *not* NeMo Guardrails renamed
> [The NemoClaw product page](../sources/nvidia-nemoclaw-page.md) left this unconfirmed — was OpenShell's "policy-based guardrails" the same thing as [NeMo Guardrails](nemo-guardrails.md) under another name? The 2026-08 architecture post answers it by placement: **NeMo Guardrails is a rail engine that runs in the harness layer** (Colang, input/dialog/retrieval/execution/output rails, shaping text); **OpenShell is the runtime layer beneath it** (isolation, identity, credentials, audit, network policy). Different jobs on opposite sides of the security boundary — and by the post's own argument, only OpenShell's side is authoritative.

## What it does

| Responsibility | Evidence |
|---|---|
| **Container isolation** | Linux container + Python runtime per sandbox; named sandboxes can run side by side ([Hermes quickstart](../sources/nvidia-nemoclaw-hermes-quickstart.md)) |
| **Network policy** | Agent-specific baseline policy allowing only the agent binary + runtime to reach named endpoints; **network-policy tiers + presets** chosen at onboarding |
| **Credential scoping** | API keys validated and **stored in sandbox scope**, not handed to the agent — *"keeping the raw credential out of the agent's reach creates a stronger boundary"* |
| **Delegation ceilings** | Subagents receive **child runtimes with ceilings they cannot exceed** |
| **Recovery** | `snapshot create`, `rebuild`, `destroy`, `credentials reset <KEY>`, `policy-add` ([Hermes quickstart](../sources/nvidia-nemoclaw-hermes-quickstart.md)) |
| **Audit** | *"independent evidence… immutable records below the security boundary"* |

The four escalating **security profiles** (Isolated / Connected / Production / Adversarial) are defined against this runtime — same stack and interfaces at every level, differing in authority granted, freshness of policy evaluation, oversight, and recovery speed. See the [source page](../sources/nvidia-where-security-fits-agent-stack.md) for the table.

## Where it shows up in this wiki

- **[NemoClaw](nemoclaw.md)** bundles it as the privacy/security half of NVIDIA's [OpenClaw](openclaw.md) distribution — the article now classifies NemoClaw as the *distribution/product* layer sitting above OpenShell.
- **[Hermes Agent](hermes-agent.md)** is the concrete, documented case: `nemohermes onboard` **creates an OpenShell sandbox and runs Hermes inside it** ([quickstart](../sources/nvidia-nemoclaw-hermes-quickstart.md)). That deployment recipe predates the architecture post and independently demonstrates its central move — the harness starts inside the runtime, not the other way round.

## Status — and the reason to hedge

**No generally available artifact is established by any ingested source.** The architecture post links only to a blog tag; [NemoClaw](nemoclaw.md) is **early preview** with no GA date; and NVIDIA's previous agentic-safety publication in this wiki had its artifact **deprecated 2026-04-22** ([safety recipe](../sources/nvidia-safety-recipe-agentic-ai.md)). Three publications across ~13 months, no shipped enforcement layer yet. The design is the strongest one in the wiki; the availability is not established.

## For robots

OpenShell is the closest thing in this wiki to the **enforcement layer** that [guardrails for robot agents](../syntheses/agents/guardrails-for-robot-agents.md) says ships empty and [the home-AI platform analysis](../syntheses/agents/home-ai-platform-trust-and-authority.md) calls "mostly aspirational." Its boundary is drawn around **processes, files, networks and credentials** — the right shape for a robot's *planning* layer, and the wrong shape for its *control* layer, where the effects are continuous joint commands at [rates](../syntheses/platforms/control-rate-ladder.md) no policy engine is going to evaluate per item. Nothing published says where the line falls for an embodied agent.

## Related

- [NemoClaw](nemoclaw.md) · [OpenClaw](openclaw.md) · [Hermes Agent](hermes-agent.md) · [NVIDIA](nvidia.md)
- [NeMo Guardrails](nemo-guardrails.md) — the layer above · [garak](garak.md) — the red-team tool
- [AI guardrails](../concepts/safety/ai-guardrails.md) · [Robot security](../concepts/robotics/robot-security.md)

## Mentioned in

- [Where Security Fits in an AI Agent Stack](../sources/nvidia-where-security-fits-agent-stack.md)
- [NemoClaw Quickstart with Hermes](../sources/nvidia-nemoclaw-hermes-quickstart.md)
- [NVIDIA NemoClaw — Product Page](../sources/nvidia-nemoclaw-page.md)

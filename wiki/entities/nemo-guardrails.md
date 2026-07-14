---
title: NeMo Guardrails
type: entity
subtype: software
created: 2026-07-13
updated: 2026-07-13
sources: 3
tags: [nvidia, guardrails, ai-safety, colang, nim, runtime-safety, open-source, tool-call-validation, langgraph, pii]
---

[NVIDIA](nvidia.md)'s **open-source Python library for adding programmable [guardrails](../concepts/safety/ai-guardrails.md) to LLM applications** — a policy-enforcement layer that can "block, alter, or validate unsafe, off-topic, malicious, or policy-violating" content **without modifying application architecture** ([NeMo Guardrails library overview](../sources/nemo-guardrails-library-overview.md)). It is the "run" phase of the [NVIDIA safety recipe](../sources/nvidia-safety-recipe-agentic-ai.md).

## Rails

Five rail types, fired at different points in the request lifecycle:

| Rail | Fires on | Job |
|---|---|---|
| **Input** | Incoming user message | Jailbreak detection, PII scrubbing |
| **Retrieval** | Retrieved RAG context | Poisoned-document / injected-instruction defense |
| **Dialog** | Conversation state | Topic control — keeping the exchange in-scope |
| **Execution** | **A tool call, before it runs** | **Tool-call validation — the agent-relevant rail** |
| **Output** | The model's reply | Content-safety filtering |

Rails are authored in **Colang**, NVIDIA's DSL for conversational flows and event-driven guardrail logic, over a **YAML** configuration layer (models, prompts, rails, runtime settings). Colang is what distinguishes NeMo Guardrails from a stateless classifier chain: it fuses safety controls with **dialog management** rather than treating safety as a pure input/output filter.

## The execution rail: NVIDIA ships the hook, not the policy

**"Agent Security"** is a first-class documented category: **tool-call validation**, **execution rails for tools**, **action monitoring/tracing**, and a **LangGraph** integration for multi-agent safety (`NEMOGUARDRAILS_LLM_FRAMEWORK=langchain`). LangChain tools register as **custom actions**, which the execution rail gates.

But note the asymmetry. Every *other* rail ships with a pretrained model behind it (content safety, jailbreak, topic, PII). The execution rail ships with **a place to put your own Python function**. There is no "is this tool call safe" model — that policy is irreducibly domain-specific, and for a robot it is **yours to write**. See [Guardrails for robot agents](../syntheses/agents/guardrails-for-robot-agents.md).

## The guardrails library

| Category | Options |
|---|---|
| **Content safety** | LLM self-check; **Llama 3.1 NemoGuard 8B Content Safety**; LlamaGuard (Meta); Fiddler; ActiveFence; Cisco AI Defense |
| **Jailbreak** | Self-check; **heuristic pattern-based** (no model call → no latency); **NemoGuard Jailbreak Detect NIM**; Prompt Security; Pangea AI Guard |
| **Topic control** | Dialog/topical rails (Colang); **NemoGuard Topic Control NIM** |
| **PII** | **NVIDIA GLiNER-PII**; Microsoft Presidio; Private AI; Polygraf; AutoAlign; GuardrailsAI validators |
| **Agent security** | Tool-call validation; execution rails; action tracing; LangGraph multi-agent |

The NemoGuard models are trained on the open **Nemotron Content Safety Dataset v2** (formerly "Aegis") and served as **NIM microservices**. Code Apache-2.0; models under the NVIDIA AI Foundation Models Community License.

## Deployment and interfaces

- **Library** — PyPI package, application-level scaling.
- **Microservice** — container image, Kubernetes/Helm.
- **Same YAML + Colang config transfers between the two without modification.**

Three entry points: **Python SDK**; **LangChain/LangGraph** plugins; and a **FastAPI guardrails server** exposing **`/v1/chat/completions`** in OpenAI-compatible format (default port 8000).

> [!note] The OpenAI-compatible server is the interesting one for this wiki
> It means guardrails can be inserted in front of an existing LLM planner as a **base-URL swap** — no application rewrite. Most of the wiki's [LLM-agent robots](../concepts/agents/llm-agent-architecture.md) talk to OpenAI-compatible endpoints already (GPT-4o-mini, [Ollama](ollama.md), Qwen-plus), which makes input/output/dialog rails a near-free addition. The execution rail is *not* free — see the synthesis.

## Where it sits in NVIDIA's stack

- Ships as a **NeMo Microservice** inside NVIDIA AI Enterprise; also usable standalone as open source.
- As of **2026-04-22**, Guardrails is one of three services the deprecated [safety-for-agentic-ai blueprint](../sources/nvidia-safety-recipe-agentic-ai.md) redirects users to — alongside **NeMo Auditor** (pre-deployment scanning; productized [garak](garak.md)) and **Safe Synthesizer** (DP synthetic data). Guardrails is the survivor of that consolidation, not a casualty.
- The same "policy-based guardrails" idea appears as **NVIDIA OpenShell** inside [NemoClaw](../sources/nvidia-nemoclaw-page.md), NVIDIA's hardened [OpenClaw](openclaw.md) distribution. The through-line: NVIDIA's answer to "personal AI assistant with tool access" and to "enterprise agent with tool access" is the *same architecture* — a local model plus a policy-enforcement runtime.

## Undocumented
No latency/performance benchmarks anywhere in the docs. No non-text modalities (no vision, audio, or robot state). No discussion of attacks against the guardrail layer itself — the guard models are LLMs too.

## Related
- [NVIDIA](nvidia.md) — owner.
- [garak](garak.md) — the build-phase counterpart (find the holes) to Guardrails' run-phase job (plug them).
- [AI guardrails](../concepts/safety/ai-guardrails.md), [AI red-teaming](../concepts/safety/ai-red-teaming.md) — the concepts.
- [Guardrails for robot agents](../syntheses/agents/guardrails-for-robot-agents.md) — what it takes to put this in front of a robot.
- [NVIDIA NemoClaw](../sources/nvidia-nemoclaw-page.md) — sibling stack, same pattern via OpenShell.

## Mentioned in
- [NeMo Guardrails — Library Overview](../sources/nemo-guardrails-library-overview.md) — **primary source**.
- [Safeguard Agentic AI Systems with the NVIDIA Safety Recipe](../sources/nvidia-safety-recipe-agentic-ai.md)
- [NVIDIA NemoClaw — Product Page](../sources/nvidia-nemoclaw-page.md)

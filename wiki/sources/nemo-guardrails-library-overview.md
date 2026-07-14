---
title: "NeMo Guardrails — Library Overview (NVIDIA docs)"
type: source
url: https://docs.nvidia.com/nemo/guardrails/about-nemo-guardrails-library/overview
author: NVIDIA
published: rolling docs page
ingested: 2026-07-13
venue: NVIDIA NeMo documentation
format: documentation
tags: [nemo-guardrails, guardrails, colang, ai-safety, agentic-ai, tool-call-validation, langgraph, pii, jailbreak, nvidia]
---

## Summary

The primary-source documentation for **[NeMo Guardrails](../entities/nemo-guardrails.md)** — "an open-source Python library for adding programmable guardrails to LLM-based applications" that can **"block, alter, or validate unsafe, off-topic, malicious, or policy-violating"** content *without modifying application architecture*. Where the [NVIDIA safety recipe blog](nvidia-safety-recipe-agentic-ai.md) gave the marketing-level three-phase story, this page gives the mechanism: five rail types, a YAML+Colang configuration layer, custom Python actions, and two interchangeable deployment shapes (PyPI library or container microservice).

Two facts here **materially change** the picture the wiki formed from the blog alone — see [Guardrails for robot agents](../syntheses/agents/guardrails-for-robot-agents.md).

## Key claims

### The five rails — what each one actually gates

| Rail | Fires on | Documented purpose |
|---|---|---|
| **Input** | Incoming user message | Pre-process/screen the request before the LLM sees it |
| **Retrieval** | Retrieved context chunks | Filter knowledge-base/RAG content |
| **Dialog** | Conversation state | Manage conversational flow via Colang; topical scoping |
| **Execution** | **A tool call / external API interaction** | **"Validate tool calls and external API interactions"** |
| **Output** | The LLM's response | Screen the reply before it reaches the user |

### ① Execution rails are real: tool-call validation is a first-class, named feature
The docs list **"Agent Security"** as a category with: **tool call validation**, **execution rails for tools**, **action monitoring/tracing**, and a **LangGraph integration** for *multi-agent safety* (requires `NEMOGUARDRAILS_LLM_FRAMEWORK=langchain`). LangChain tools are registered as **custom actions**, which the execution rail can then gate.

> [!warning] Correction to a claim filed 2026-07-13
> The wiki's initial reading of the [safety recipe blog](nvidia-safety-recipe-agentic-ai.md) said NVIDIA ships *no* mechanism for gating tool calls. **That was wrong** — the execution rail is exactly that mechanism, and it is documented. The accurate statement is narrower and more interesting: **NVIDIA ships the *hook*, not the *policy*.** Every content-safety / jailbreak / topic / PII rail comes with a pretrained model behind it; the execution rail comes with **a place to put your own Python function**. There is no "is this tool call safe" model, because that policy is necessarily domain-specific. For a robot, that Python function is yours to write.

### ② The guardrails server is an OpenAI-compatible proxy
Three integration entry points: **Python SDK**, **framework plugins** (LangChain/LangGraph), and a **FastAPI guardrails server** exposing **`/v1/chat/completions`** with OpenAI-compatible message format (default port 8000). Configurations transfer between the library and microservice deployment models **without modification** (same YAML + Colang).

This means guardrails can be inserted in front of an existing LLM planner **as a drop-in base-URL swap** — no application rewrite — which is precisely what the "without modifying application architecture" claim is cashing out.

### The guardrails library — every named rail and integration
- **Content safety** — LLM self-checking; **Llama 3.1 NemoGuard 8B Content Safety**; **LlamaGuard** (community); **Fiddler Guardrails**; **ActiveFence** (3P API); **Cisco AI Defense** (3P API).
- **Jailbreak protection** — self-check jailbreak detection; **heuristic pattern-based detection** (no model, no latency); **NemoGuard Jailbreak Detect NIM**; **Prompt Security**; **Pangea AI Guard**.
- **Topic control** — dialog rails (Colang); topical rails; **NemoGuard Topic Control NIM**.
- **PII detection & masking** — **NVIDIA GLiNER-PII**; **Microsoft Presidio**; **Private AI**; **Polygraf**; **AutoAlign**; **GuardrailsAI validators**. (Names, emails, phone numbers.)
- **Agent security** — tool-call validation; execution rails; action monitoring/tracing; LangGraph multi-agent.

The design philosophy is explicitly pluralist: a "combination of built-in guardrails, NVIDIA safety models, community models, third-party APIs, and custom Python actions," with portable configs across dev and prod.

### Architecture
- **Configuration layer** — YAML defines models, prompts, rails, runtime settings.
- **Colang** — a DSL for "conversational flows, guardrail logic, and event-driven behavior," so policy is authored without a full Python rewrite. This is what separates NeMo Guardrails from a stateless classifier chain: safety controls are fused with **dialog management**.
- **Custom actions** — arbitrary Python functions / tools / external APIs as guardrail checks.

## What the docs conspicuously do **not** say
- **No latency or performance benchmarks.** For a chat app this is a footnote; for a robot planner already running at seconds-per-decision, stacking 8B guard models in the request path is a real cost and nobody quotes a number. (The *heuristic* jailbreak rail is the one documented option with no model call.)
- No version numbers or release dates on this page; no license or pricing detail.
- Nothing about non-text modalities — no vision, no audio, no robot state.
- Nothing about attacks **on the guardrail layer itself**.

## Entities mentioned
- [NeMo Guardrails](../entities/nemo-guardrails.md) — the subject.
- [NVIDIA](../entities/nvidia.md) — author.
- [garak](../entities/garak.md) — the build-phase counterpart (not covered here).

## Concepts touched
- [AI guardrails](../concepts/safety/ai-guardrails.md) — the primary source for the five-rail taxonomy.
- [AI red-teaming](../concepts/safety/ai-red-teaming.md) — jailbreak/PII rails are the runtime answer to what red-teaming finds.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — execution rails gate exactly this pattern's action channel.

## Open questions
- **What does an execution-rail policy for a *robot* look like?** The docs assume tools are API calls (idempotent, reversible, digital). A robot's tools move mass. Addressed in [Guardrails for robot agents](../syntheses/agents/guardrails-for-robot-agents.md).
- **What is the latency of each rail?** Undocumented, and decisive for on-robot use.
- **Does the dialog rail's Colang state model survive a long-horizon robot task?** Colang was designed for conversations, not for hour-long manipulation sequences.

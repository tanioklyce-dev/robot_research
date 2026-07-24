---
title: garak
type: entity
subtype: tool
created: 2026-07-13
updated: 2026-07-13
sources: 2
tags: [nvidia, red-teaming, security, llm, open-source, vulnerability-scanner, jailbreak]
---

Open-source **LLM vulnerability scanner** — "nmap for LLMs." Points a battery of adversarial probes at a model endpoint and reports which attacks succeed: jailbreaks, prompt injection, harmful-content elicitation, data leakage, encoding tricks. Maintained by [NVIDIA](nvidia.md) ([github.com/NVIDIA/garak](https://github.com/NVIDIA/garak)).

## Role in the safety lifecycle

garak is the **measurement** half of the [guardrail](../concepts/safety/ai-guardrails.md) story. In the [NVIDIA safety recipe](../sources/nvidia-safety-recipe-agentic-ai.md), it is the security-evaluation step of the **build** phase: scan the candidate open-weights model, read the report, safety post-train against the failures, re-scan. The recipe's headline security number — **56% → 63%** after post-training — is a garak-style pass rate, and the fact that a *hardened* model still fails about a third of the probes is the empirical case for keeping [NeMo Guardrails](nemo-guardrails.md) live at runtime.

The division of labor is clean: **garak finds the holes; Guardrails plugs them.** You need both, because post-training never closes the gap completely.

## Status

Since **2026-04-22**, the productized successor for this job in NVIDIA's stack is **NeMo Auditor** (pre-deployment vulnerability scanning, delivered as a NeMo Microservice), which is where the deprecated [safety-for-agentic-ai blueprint](../sources/nvidia-safety-recipe-agentic-ai.md) redirects users. The open-source garak project remains the reference implementation of the idea and the one you can run without NVIDIA AI Enterprise.

> [!note] Not (yet) an embodied-agent tool
> garak probes a **text** endpoint. It has no notion of a robot's tool-call channel or of [prompt injection arriving through a camera](../concepts/safety/ai-red-teaming.md). Nothing in the wiki's sources red-teams an embodied agent, and garak as it stands would not do it for you.

## Related
- [NeMo Guardrails](nemo-guardrails.md) — the runtime counterpart.
- [NVIDIA](nvidia.md) — maintainer.
- [AI red-teaming and LLM vulnerability scanning](../concepts/safety/ai-red-teaming.md) — the concept.

## Mentioned in
- [Safeguard Agentic AI Systems with the NVIDIA Safety Recipe](../sources/nvidia-safety-recipe-agentic-ai.md)

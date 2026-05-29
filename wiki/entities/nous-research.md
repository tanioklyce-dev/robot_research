---
title: Nous Research
type: entity
subtype: organization
created: 2026-05-28
updated: 2026-05-28
sources: 2
tags: [nous-research, agentic-ai, hermes, llm-fine-tuning, decentralized-ai, open-source, mit, ai-org]
---

**Nous Research** — open-source AI research organization, prominent for two distinct product lines:

1. **Hermes LLM family** — fine-tuned model weights on top of base models (Llama, Qwen, Mistral). Known for strong **function-calling / tool-use** behavior. Per [nousresearch.com](https://nousresearch.com/), latest line is **Hermes 4** (as of May 2026).
2. **[Hermes Agent](hermes-agent.md)** — open-source self-improving agent framework that uses LLM tool-calling as its primitive; **171K GitHub stars, MIT licensed**. Featured by NVIDIA as a flagship [DGX Spark](dgx-spark.md) workload ([RTX AI Garage blog](../sources/nvidia-rtx-ai-garage-hermes-agent.md)). *"Most used agent in the world according to OpenRouter."*

Other products surfaced from their homepage but not yet wiki-tracked: **Nous Portal** (subscription routing 300+ models), **Psyche**, **Nous Chat**, **Simulators**.

## Position in the agent-framework landscape

Nous's [Hermes Agent](hermes-agent.md) is the principal **Nous Research entry in the "Claw" ecosystem** of open-source personal-AI-agent frameworks that emerged in 2025–2026:

| Project | Author | Stars |
|---|---|---|
| [OpenClaw](openclaw.md) | Peter Steinberger + community | 375K |
| [NemoClaw](nemoclaw.md) | NVIDIA (wraps OpenClaw) | early preview |
| **[Hermes Agent](hermes-agent.md)** | **Nous Research** | 171K |

The relationship is somewhere between competitive and cooperative — Hermes Agent ships a `hermes claw migrate` command to import from OpenClaw, suggesting Nous expects users to flow toward Hermes from the upstream framework.

## Related

- [Hermes Agent](hermes-agent.md) — primary agent framework.
- [OpenClaw](openclaw.md) — sibling / competitor.
- [NemoClaw](nemoclaw.md) — NVIDIA-wrapped sibling.

## Mentioned in

- [NVIDIA RTX AI Garage — Hermes Agent on DGX Spark](../sources/nvidia-rtx-ai-garage-hermes-agent.md)
- [Hermes Agent GitHub README](../sources/hermes-agent-github.md)

## Open questions

- **Hermes 4 LLM family** — not yet a wiki entity; relationship to [Hermes Agent](hermes-agent.md) (do they use Hermes 4 as the default brain?).
- **Nous Portal** — 300+ model routing service; not yet a wiki entity.
- **Psyche** — referenced on the homepage; unclear what it is.
- **Org structure, funding, key researchers** — not yet captured.
- **Decentralized-AI thesis** — Nous has historically advocated for open / decentralized AI development; positioning vs Anthropic / OpenAI / Meta-AI worth surfacing if relevant.

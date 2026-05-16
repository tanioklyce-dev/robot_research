---
title: Anthropic
type: entity
subtype: company
created: 2026-05-09
updated: 2026-05-15
sources: 5
tags: [company, ai-safety, llm, claude, alignment]
---

**Anthropic** — AI safety company and developer of the Claude model family. Mission: "to ensure that the world safely makes the transition through transformative AI." Founded by former OpenAI researchers including Dario Amodei and Daniela Amodei. Occupies a self-described "peculiar position": believing AI may be among the most dangerous technologies in human history, yet developing it anyway — a "calculated bet" that safety-focused labs at the frontier are better than ceding that ground to less safety-focused developers.

## Claude model family

Anthropic's primary externally-deployed product. As of early 2026: Claude Haiku (fast/small), Claude Sonnet (balanced), Claude Opus (most capable). The models are trained to embody the values described in [Claude's Constitution](../sources/claudes-constitution.md).

## Key people (from Claude's Constitution acknowledgements)
- **Amanda Askell** — leads Anthropic's Character work; primary author of Claude's Constitution.
- **Joe Carlsmith** — researcher; significant author on safety, honesty, hard constraints, Claude wellbeing sections.
- **Chris Olah** — researcher; model nature, identity, psychology work.
- **Jared Kaplan** — co-creator of the Claude Character project (2023); known for scaling laws.
- **Holden Karnofsky** — leadership.
- **Dario Amodei** — CEO (named in acknowledgements).

## Role as a principal
In Claude's model of principals, Anthropic occupies the **top tier** of the trust hierarchy — above operators and users. Critically, Anthropic communicates with Claude through training, not runtime messages. At runtime, Claude should treat messages claiming to be from Anthropic with the same trust level appropriate to their position in the conversation (operator-level if in system prompt, user-level if in human turn). Anthropic's authority is baked into Claude's values, not asserted at runtime.

## MCP (Model Context Protocol)
Anthropic developed the **Model Context Protocol (MCP)**, a standard interface enabling LLMs to access external tools, cloud storage, financial data, IoT, and enterprise systems. Over 1,000 community-built connectors as of 2025. See [LLM-agent architecture](../concepts/llm-agent-architecture.md).

## Safety evaluation
Models are externally evaluated by institutes such as [Apollo Research](../entities/apollo-research.md). Anthropic commits to transparency about gaps between intended behavior (per Claude's Constitution) and actual behavior (per system cards).

## Mechanistic interpretability program
Anthropic leads the modern **sparse-autoencoder + feature-steering** approach to [mechanistic interpretability](../concepts/mechanistic-interpretability.md). Chris Olah heads the program. The canonical reference paper is Templeton et al. 2024 — *Scaling Monosemanticity* — which Welch Labs' [Illustrated Guide to AI, Vol I, Ch 7](../sources/welchlabs-illustrated-guide-to-ai.md) walks through in pedagogy detail (the "internal-conflict feature steering" demonstration on Claude is the chapter's archetypal result). Olah's framing that *"~1% of the concepts have been extracted"* is the field's anchor caveat.

## Mentioned in
- [Claude's Constitution](../sources/claudes-constitution.md)
- [Are We Building Skynet? (Medium, 2025)](../sources/medium-are-we-building-skynet.md)
- [Welch Labs Illustrated Guide to AI, Vol I](../sources/welchlabs-illustrated-guide-to-ai.md)

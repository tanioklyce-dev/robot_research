---
title: CodeAct
type: entity
subtype: method
created: 2026-08-03
updated: 2026-08-03
sources: 1
tags: [codeact, llm-agent, tool-use, action-space, uiuc, benchmark]
---

**CodeAct** — UIUC + Apple, ICML 2024. The proposal to consolidate LLM-agent actions into **executable Python** rather than JSON or text in a pre-defined format, with a Python interpreter in the loop for multi-turn revision ([paper](../sources/codeact-paper.md)).

## Why it matters in this wiki
CodeAct supplies the **non-robotics grounding** for the [code-as-policy](../concepts/agents/code-as-policy.md) definition: the advantage of code is that it "inherently supports control and data flow," letting one action carry a loop, a conditional, and a variable piping one tool's output into another.

> [!note] The advantage is composition, not tool use
> Across 17 LLMs, CodeAct is only marginally best on **atomic** single-tool calls (API-Bank: 8 wins vs JSON 5, Text 4 — and JSON actually wins among closed-source models). It wins decisively on **multi-tool composition** (M3ToolEval: 12 of 17 for both success rate and fewer turns). "Code beats tool menus" is specifically a claim about tasks needing control flow — which is the regime robot policies live in.

Best result: `gpt-4-1106-preview` at **74.4%** vs 53.7% (text) — **+20.7 pp** with 2.1 fewer turns.

Also ships **CodeActInstruct** (7k multi-turn interactions) and **CodeActAgent**, finetuned from Llama-2 and Mistral.

## Related
- [Code as Policies](../sources/code-as-policies-paper.md) — the same argument from robotics, eighteen months earlier.
- [Voyager](voyager.md) — the other cheap-trial validation of code-as-action-space.
- [CaP-X](cap-x.md) — carries the claim into embodied control.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — CodeAct is a claim about that page's core pattern.

## Mentioned in
- [CodeAct paper](../sources/codeact-paper.md) — primary source.
- [Introducing Waddle](../sources/waddle-labs-introducing-waddle.md) — cited in Waddle's lineage survey as a cheap-trial-domain precedent.

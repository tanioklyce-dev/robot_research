---
title: "Executable Code Actions Elicit Better LLM Agents (CodeAct)"
type: source
url: https://arxiv.org/abs/2402.01030
author: "Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li, Hao Peng, Heng Ji"
affiliation: University of Illinois Urbana-Champaign, Apple
published: 2024-02-01
ingested: 2026-08-03
venue: "ICML 2024 (PMLR 235)"
format: conference paper (25 pp with appendices)
local_path: raw/2402.01030.pdf
sha256: 749a45e36cf89fc7e1b701a2a72f6609ce8d3697577ceb0fff5ce9339ce8539e
license: arXiv preprint (v4, 2024-06-07)
tags: [codeact, llm-agent, tool-use, action-space, benchmark, instruction-tuning, code-as-policy, primary-source]
---

## Summary

**CodeAct** is the paper that establishes *code beats a fixed tool schema* as a general LLM-agent result, outside robotics. It is the direct grounding for this wiki's [code-as-policy](../concepts/agents/code-as-policy.md) definition — that the pattern's advantage is an **action space that supports control and data flow**, not merely a different serialization format.

The argument in one line: JSON or text actions are "limited by constrained action space (e.g., the scope of pre-defined tools) and restricted flexibility (e.g., inability to compose multiple tools)," whereas code lets one action carry a `for` loop, an `if`, and a variable that pipes one tool's output into another.

## Key claims

### The measured advantage is in *composition*, not tool use

This distinction is the paper's most useful contribution and is easy to lose:

**API-Bank — atomic tool calls (one tool per action).** Best-format counts across 17 LLMs:

| | CodeAct | JSON | Text |
|---|---:|---:|---:|
| Open-source | 4 | 0 | 4 |
| Closed-source | 4 | **5** | 0 |
| **Overall** | **8** | 5 | 4 |

**M3ToolEval — multi-tool composition.** Best-format counts:

| | CodeAct | JSON | Text |
|---|---:|---:|---:|
| Success rate (best in) | **12 / 17** | 5 | 4 |
| Fewer turns (best in) | **12 / 17** | 3 | 2 |

> [!note] Read the two tables together
> On **atomic** tool use CodeAct barely wins (8/5/4, and JSON actually wins among closed-source models). On **compositional** tasks it wins decisively (12/5/4) *and* uses fewer turns. The claim "code is a better action space" is therefore specifically a claim about **tasks requiring control flow or multi-tool composition** — which is exactly the regime robot policies live in, and exactly what [Code as Policies](code-as-policies-paper.md) argued from the robotics side eighteen months earlier.

Best model, `gpt-4-1106-preview` on M3ToolEval: **74.4%** with CodeAct vs 53.7% (text) and 52.4% (JSON) — **+20.7 pp** over next-best, with **2.1 fewer interaction turns** on average.

### The open/closed gap
Best open-source model reaches **13.4%** (lemur-70b) against **74.4%** closed-source — attributed to "open-source models' weak task-solving capability and inability to follow complex instructions without demonstration."

### CodeActInstruct and CodeActAgent
A **7k multi-turn interaction** instruction-tuning dataset; models finetuned from Llama-2 and Mistral, integrated with a Python interpreter, able to "perform sophisticated tasks (e.g., model training) using existing libraries and autonomously self-debug." The paper's stated motivation for code as an action space includes that **code data is already heavily represented in LLM pretraining**, making adoption cheap.

## Entities mentioned
- UIUC / Apple · [Anthropic](../entities/anthropic.md) (claude-2, claude-instant-1 among the 17 models)
- [CodeAct](../entities/codeact.md)

## Concepts touched
- [Code as policy](../concepts/agents/code-as-policy.md) — the non-robotics half of the argument; the wiki's definitional grounding.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — CodeAct is a claim about *this page's* core pattern: the action vocabulary should be code, not a tool schema.
- [Agent skills](../concepts/agents/agent-skills.md)

## Open questions
- **M3ToolEval is the authors' own benchmark**, introduced in the same paper as the method it favors. API-Bank is external — and it is on API-Bank, the external benchmark, that CodeAct's advantage is weakest. Worth weighting accordingly.
- **The 2024 open-source gap may not hold.** 13.4% vs 74.4% was measured on Llama-2/Mistral/CodeLlama-era models; [CaP-X](cap-x-paper.md)'s 2026 12-model comparison still finds closed-source ahead on robot code, but the magnitudes are not comparable across benchmarks.
- No robotics evaluation — the embodied claim is inherited from the robotics branch, not tested here.

## Related sources
- [Code as Policies](code-as-policies-paper.md) — the same argument from robotics, made earlier.
- [Voyager](voyager-paper.md) — the other "cheap-trial domain" where code-as-action-space was validated before robotics.
- [CaP-X](cap-x-paper.md) — cites executable code as "empirically a superior agent action representation"; carries the claim into embodied control.

---
title: Aleph
type: entity
subtype: product
created: 2026-05-17
updated: 2026-05-17
sources: 2
tags: [aleph, logical-intelligence, agent, lean, formal-verification, putnambench, gpt-5.2, theorem-proving, ebm]
---

**Aleph** — agentic orchestration product from [Logical Intelligence](logical-intelligence.md). Sits on top of a frontier LLM (GPT-5.2 in the headline-result run) plus the [Lean theorem prover](../concepts/learning/lean-theorem-prover.md), and optionally [Kona](kona.md). Targets **formal verification and automated code generation with machine-checkable proofs** ([Aleph EBM video](../sources/2026-05-aleph-ebm-refuses-bullshit-video.md)).

The "verified" half is the load-bearing claim: outputs are written in **[Lean](../concepts/learning/lean-theorem-prover.md)** and certified by the **deterministic Lean compiler**, so correctness is mechanical rather than judged by a language model.

## Architecture

Three-stage agentic pipeline ([Aleph EBM video](../sources/2026-05-aleph-ebm-refuses-bullshit-video.md), citing Logical Intelligence's 2026-05-14 PutnamBench blog post):

1. **Plan** — decompose the theorem statement into manageable subproblems.
2. **Prove** — generate candidate Lean proofs; verify each via the Lean kernel.
3. **Refine** — adjust strategy based on which subproblems succeeded.

Implementation notes from the blog post: "recursive and interactive state management system with highly parallel Lean verification calls." Users provide theorems in **natural language or Lean directly**, plus **time and cost budgets**.

The architecture is **engine-agnostic** — supports multiple reasoning models underneath. **GPT-5.2 was the engine for the PutnamBench result.**

## PutnamBench result (2026-05-14)

The wiki's anchor data point for Aleph:

| Metric | Value |
| --- | --- |
| Benchmark | [PutnamBench](../concepts/learning/putnambench.md) — 672 William Lowell Putnam Exam problems, 50+ years |
| Aleph (GPT-5.2) | **668 / 672 (99.4%)** with formally verified Lean proofs |
| Previous leaders | ByteDance and Apple (specific scores not in materials I've ingested) |
| Notable | Aleph identified and corrected **~15 (~2%) formal problem statements** before solving them |

Cited via [Aleph EBM video](../sources/2026-05-aleph-ebm-refuses-bullshit-video.md), itself drawing on Logical Intelligence's 2026-05-14 blog post.

## Why it matters in this wiki

- **First commercial-grade formal-verification agent in the wiki.** Distinct in kind from the LLM-emits-tool-calls agents in [karpathy/autoresearch](../sources/karpathy-autoresearch.md) and [Gemini Robotics-ER](gemini-robotics.md) — Aleph's outputs are **kernel-certified**, not language-model-judged.
- **Demonstrates the "LLM as one piece of a verified pipeline" pattern.** GPT-5.2 provides the proof-search heuristic; the Lean compiler provides the ground truth; Aleph orchestrates between them. The thing the user sees is the *intersection* of "LLM can find" and "Lean can verify," which is much smaller than what LLMs alone confidently produce.
- **Bridges to Kona**: Aleph is the productized form of the orchestration + verification layer; Kona is the proprietary reasoning model intended to eventually replace GPT-5.2 in the pipeline.

## Related

- [Logical Intelligence](logical-intelligence.md) — vendor.
- [Kona](kona.md) — Logical Intelligence's EBM reasoning model; intended substitute for the GPT-5.2 layer over time.
- [Lean theorem prover](../concepts/learning/lean-theorem-prover.md) — the verification substrate.
- [Formal verification](../concepts/learning/formal-verification.md) — the broader concept.
- [PutnamBench](../concepts/learning/putnambench.md) — the benchmark.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the broader pattern Aleph belongs to.

## Mentioned in

- [Aleph and Energy-Based Models: The AI That Refuses to Bullshit (video)](../sources/2026-05-aleph-ebm-refuses-bullshit-video.md)
- [Kona: Energy-Based Models (EBMs) for AI Reasoning — Logical Intelligence page](../sources/2026-05-14-logical-intelligence-kona-ebms-page.md) — Aleph name-checked as "delivering verified reasoning today."

---
title: Lean theorem prover
type: concept
created: 2026-05-17
updated: 2026-05-17
sources: 2
tags: [lean, theorem-prover, formal-verification, kernel, proof-assistant, mathlib]
---

**Lean** — a functional programming language + interactive theorem prover. Output proofs are **deterministically checked by the Lean kernel**: type-correctness in the dependent type theory underlying Lean *is* the correctness criterion for a proof. This makes Lean the dominant substrate for the recent generation of **LLM-driven automated theorem proving** work (DeepSeek-Prover line, ByteDance and Apple's PutnamBench entries, [Aleph](../../entities/aleph.md)).

This wiki's interest in Lean is functional: it's the **verification substrate underneath [Aleph](../../entities/aleph.md)** ([Aleph EBM video source](../../sources/2026-05-aleph-ebm-refuses-bullshit-video.md)).

## Why Lean specifically

- **Mathlib** — large, actively-maintained formal-mathematics library. Provides the lemmas and definitions an LLM-driven prover can reach for. Roughly comparable in scope to a mature mathematician's working toolkit.
- **Tactic language** — programmable proof scripts (`tactic` mode) that LLMs can plausibly generate, plus a verbose-form (`term` mode) that's harder for LLMs but cleaner to inspect.
- **Kernel determinism** — proof acceptance is not subject to LLM judgment. This is the property [Aleph](../../entities/aleph.md) leverages to make its outputs **machine-checkable** rather than just plausible.
- **PutnamBench** — the [community-maintained benchmark](putnambench.md) on Lean (with Coq + Isabelle ports) of 672 Putnam problems is the proving-ground for LLM-Lean systems. Aleph's 99.4% result is on this benchmark.

## Related

- [Formal verification](formal-verification.md) — the broader concept Lean instantiates.
- [PutnamBench](putnambench.md) — the benchmark.
- [Aleph](../../entities/aleph.md) — the agentic theorem-prover this wiki tracks.

## Mentioned in

- [Aleph and Energy-Based Models: The AI That Refuses to Bullshit (video)](../../sources/2026-05-aleph-ebm-refuses-bullshit-video.md)

## Open questions / TBD

- This page is a **stub** focused on Lean's role in Aleph. A real Lean concept page would cover its type theory, history (Lean 3 / 4 transition), and the broader Mathlib community. Worth expanding if more Lean-based AI work surfaces.

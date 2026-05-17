---
title: PutnamBench
type: concept
created: 2026-05-17
updated: 2026-05-17
sources: 1
tags: [putnambench, benchmark, formal-verification, lean, theorem-proving, reasoning]
---

**PutnamBench** — formal-reasoning benchmark of **672 problems** from the **William Lowell Putnam Mathematical Competition**, spanning 50+ years of the oldest collegiate mathematics contest in North America. Problems are formalized in [Lean](lean-theorem-prover.md) (and Coq, Isabelle ports), so submissions must produce **machine-checkable proofs**, not natural-language solutions.

## Why this benchmark

- **Hard mathematics, short statements** — Putnam problems are written to be solvable by an exceptional undergraduate in ~30 minutes with paper and pencil, which makes them a sweet spot: substantively difficult, but with self-contained formalizations.
- **Long history** — 50+ years of problems means a benchmark that's resistant to memorization-via-training: a solver has to handle unfamiliar phrasings and combinations.
- **Lean-native** — by formalizing the problem statement and requiring a Lean proof of solution, PutnamBench dodges the standard "the LLM guessed the right number" failure mode of natural-language math benchmarks. **A correct proof is mechanically verified.**

## Leaderboard context (as of May 2026)

| System | Score | Source |
| --- | --- | --- |
| **[Aleph](../../entities/aleph.md) (GPT-5.2)** | **668 / 672 (99.4%)** | [Aleph EBM video](../../sources/2026-05-aleph-ebm-refuses-bullshit-video.md), citing Logical Intelligence's 2026-05-14 blog post |
| ByteDance (previous leader) | — | named in same source, score not surfaced |
| Apple (previous leader) | — | named in same source, score not surfaced |

Aleph reportedly **identified and corrected ~15 (~2%) of the formal problem statements** before solving them — a notable note on the benchmark's own formalization quality.

## Related

- [Formal verification](formal-verification.md) — the broader practice.
- [Lean theorem prover](lean-theorem-prover.md) — the substrate.
- [Aleph](../../entities/aleph.md) — current leaderboard occupant.

## Mentioned in

- [Aleph and Energy-Based Models: The AI That Refuses to Bullshit (video)](../../sources/2026-05-aleph-ebm-refuses-bullshit-video.md)

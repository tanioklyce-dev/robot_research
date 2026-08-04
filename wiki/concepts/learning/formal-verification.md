---
title: Formal verification
type: concept
created: 2026-05-17
updated: 2026-08-03
sources: 3
tags: [formal-verification, lean, theorem-proving, proof-checking, machine-checkable, aleph]
---

**Formal verification** — the practice of producing a **machine-checkable proof** that a statement is true (a theorem) or that a piece of code satisfies a specification. The proof is verified by a **deterministic checker** (a theorem prover's kernel), so correctness becomes a **mechanical fact** rather than a judgment.

For LLM-era AI, formal verification is the cleanest answer to **hallucination**: an LLM's confidence in an output is statistical; a proof's correctness is checked by an algorithm. If the proof passes the checker, the statement is true — regardless of what produced it.

## Pipeline (as used by Aleph)

The [Aleph](../../entities/aleph.md) "translate and verify" pipeline ([Aleph EBM video source](../../sources/2026-05-aleph-ebm-refuses-bullshit-video.md)):

1. **Translate** — convert a real-world requirement (natural-language theorem, code spec) into a statement in a formal language. [Lean](lean-theorem-prover.md) is Aleph's substrate; alternatives include Coq, Isabelle, Rocq, Agda.
2. **Propose** — generate candidate proofs of that statement. This is the hard, search-heavy step; in Aleph's PutnamBench run, the proof-search heuristic is **GPT-5.2** under an agentic Plan/Prove/Refine loop.
3. **Verify** — run the candidate proof through the prover's **deterministic kernel**. Either it type-checks (proof accepted, statement now formally true) or it doesn't (reject and retry).

The split between (2) and (3) is the load-bearing trick: **the LLM doesn't have to be right, it has to be right *often enough that the verifier catches the wrong ones***. The user sees only the intersection of "LLM can propose" and "Lean can verify," which is a much smaller, much more trustworthy set than "things an LLM said with high confidence."

## Why it matters in this wiki

- **First wiki source on commercial-scale formal verification.** [Aleph's 99.4% PutnamBench result](../../entities/aleph.md) (2026-05) is the data point.
- **Cleanest contrast to hallucination-tolerant LLM use.** Every other wiki AI pipeline — [VLA action heads](../learning/vla-models.md), [chain-of-thought](chain-of-thought.md), [LLM agents](../agents/llm-agent-architecture.md) — relies on the LLM's output being *plausibly* right. Formal verification relies on it being *checkably* right.
- **Bridge to safety-critical robotics.** If formal-verification stacks become commoditized, they could underpin safety-critical robot deployments — surgical robotics is explicitly named as a target for [Kona](../../entities/kona.md). This is adjacent to the [assistive robotics](../robotics/assistive-robotics.md) thread.

## Limits

- **Specifications are still informal at their boundary.** The formal proof certifies that code matches a spec, but the spec itself is written by humans; "the code is correct" reduces to "the code matches what the spec-author wrote down," which can be wrong.
- **Proving is expensive.** PutnamBench problems are short and self-contained. Real-world software specs are large; verified code generation at scale is the open problem [Logical Intelligence](../../entities/logical-intelligence.md) is positioning into.
- **Domains without a tractable formalization** (e.g. "this robot should behave politely with humans") aren't reachable by this approach.

## Related

- [Lean theorem prover](lean-theorem-prover.md) — Aleph's verification substrate.
- [PutnamBench](putnambench.md) — the benchmark.
- [Aleph](../../entities/aleph.md) — the agent.
- [Energy-based models](energy-based-models.md) — sibling technique aimed at constraint-satisfaction reasoning; [Kona](../../entities/kona.md) intended to plug into the same Aleph pipeline.

## Mentioned in

- [Aleph and Energy-Based Models: The AI That Refuses to Bullshit (video)](../../sources/2026-05-aleph-ebm-refuses-bullshit-video.md)
- [Safely Learning Dynamical Systems](../../sources/safely-learning-dynamical-systems-paper.md) — safe *exploration* with certificates: the set of safe initial conditions is LP-, SOCP-, or SDP-representable, and at T=1 the algorithm either recovers the dynamics in ≤n trajectories **or certifies that safe learning is impossible**. The wiki's only ingested safety method that can return an impossibility proof rather than a rate.

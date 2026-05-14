---
title: "micrograd — Karpathy's tiny scalar autograd engine (GitHub repo, 2020)"
type: source
url: https://github.com/karpathy/micrograd
author: Andrej Karpathy
affiliation: independent / Stanford alumnus / formerly Tesla & OpenAI
published: 2020-04-13 (initial commit)
ingested: 2026-05-14
created: 2026-05-14
updated: 2026-05-14
tags: [karpathy, autograd, backprop, pedagogy, github, reference-implementation, micrograd]
github_stats: 15.8K stars, 2.4K forks (May 2026)
---

> [!note] Ingest depth
> Read the README only (~70 lines) plus repo metadata. The repo's code (`engine.py` ~100 lines, `nn.py` ~50 lines, plus a demo notebook) is the actual artifact — the README is just an entry point.

## Summary

**micrograd** — Karpathy's "tiny Autograd engine (with a bite!)." A scalar-valued reverse-mode autodiff engine in **~100 lines of Python**, plus a ~50-line neural-net library on top that mimics PyTorch's API. The DAG operates only on scalars (each neuron is chopped into individual adds/multiplies), but this is enough to build and train an MLP binary classifier on 2D data. **Potentially useful for educational purposes** — and it has been: 15.8K GitHub stars (as of May 2026) make it one of the most-referenced pedagogical ML repos.

**Why it matters to this wiki.** The cleanest "I understand backprop" milestone available anywhere. The full backward pass is a few dozen lines you can step through in a debugger. Once you can read `engine.py` end to end, every later autograd library (PyTorch, JAX, etc.) is a more-engineered version of the same idea. The repo is **the recommended exit-ramp at the bottom of [Curriculum Module 1](../syntheses/curriculum-01-neural-networks.md)**.

## What's in the repo

- **`micrograd/engine.py`** — the `Value` class: holds a scalar, its gradient, the children that produced it, and a `_backward` closure. Implements `+, -, *, /, **, relu, exp` etc. with both forward semantics and a local gradient rule.
- **`micrograd/nn.py`** — `Neuron`, `Layer`, `MLP` classes; PyTorch-shaped API; ~50 lines.
- **`demo.ipynb`** — train a 2-hidden-layer MLP binary classifier on the moon dataset with SVM-style max-margin loss + SGD; produces a decision-boundary plot.
- **`trace_graph.ipynb`** — Graphviz visualization of a `Value` DAG showing data + grad on each node.

## Example (from the README)

```python
from micrograd.engine import Value

a = Value(-4.0)
b = Value(2.0)
c = a + b
d = a * b + b**3
c += c + 1
c += 1 + c + (-a)
d += d * 2 + (b + a).relu()
d += 3 * d + (b - a).relu()
e = c - d
f = e**2
g = f / 2.0
g += 10.0 / f
print(f'{g.data:.4f}')   # 24.7041
g.backward()
print(f'{a.grad:.4f}')   # 138.8338 — dg/da
print(f'{b.grad:.4f}')   # 645.5773 — dg/db
```

The expression tree gets built dynamically; `g.backward()` walks the DAG in reverse topological order, calling each node's local `_backward` closure to accumulate gradients. **That's the whole algorithm.**

## Curriculum hookup

This repo is the **recommended hands-on exercise for [Curriculum Module 1 — Neural networks and training](../syntheses/curriculum-01-neural-networks.md)**. After reading the module's coverage of MLPs + forward pass + backprop + SGD, working through `engine.py` is the cleanest way to validate the math is no longer mysterious. Specifically:

- Module 1 §3 (forward pass) → matches the `__add__ / __mul__ / __pow__` forward semantics in `engine.py`.
- Module 1 §4 (backprop) → matches the local `_backward` closures + the topological-sort walk in `Value.backward()`.
- Module 1 §6 (SGD) → matches `nn.py`'s `zero_grad` + parameter-by-parameter update loop.

The repo also pairs naturally with Karpathy's **[Zero to Hero](https://karpathy.ai/zero-to-hero.html)** lecture series — the first lecture builds micrograd from scratch on video.

## Why it has staying power

Most "implement autograd from scratch" tutorials hand-wave the topological sort, or use a forward-mode autodiff that doesn't generalize, or get lost in tensor broadcasting. micrograd does **scalar reverse-mode** which is the algorithm PyTorch actually uses, just without vectorization. The 100-line scalar version makes the algorithm legible; once it clicks, the leap to "the same algorithm but on tensors with broadcasting and CUDA" is purely engineering, not conceptual.

## Entities mentioned

- **[Andrej Karpathy](../entities/andrej-karpathy.md)** — sole author.

## Concepts touched

- Reverse-mode autodiff / backpropagation.
- DAG-based computation graphs.
- MLP / feed-forward networks (Module 1).
- SGD (Module 1).

## Related sources

- [karpathy/nanoGPT](karpathy-nanogpt.md) — same author, same minimalism, applied to GPT training.
- [karpathy/nanochat](karpathy-nanochat.md) — same author, evolved to a full ChatGPT pipeline.
- [karpathy/autoresearch](karpathy-autoresearch.md) — same author, agent-driven research on nanochat training.

## Open questions / TBD

- The repo hasn't seen substantive code changes since ~2024-08; the demo notebooks and README are still authoritative. No risk of staleness for the curriculum's purposes.

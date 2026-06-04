---
title: "Computing Neural Network Gradients (Kevin Clark, CS224n)"
type: source
url: https://web.stanford.edu/class/cs224n/readings/gradient-notes.pdf
author: Kevin Clark
published: 2019-01 (Stanford CS224n 2019 reading)
ingested: 2026-06-03
local_path: raw/gradient-notes.pdf
venue: Stanford CS224n course notes
format: PDF (7 pp.)
tags: [backpropagation, gradients, jacobian, vectorization, chain-rule, cross-entropy, softmax, mlp, pedagogy, curriculum, module-1]
---

# Computing Neural Network Gradients (Kevin Clark, CS224n)

## Summary

A 7-page Stanford CS224n handout by [Kevin Clark](../entities/kevin-clark.md) that teaches how to compute neural-network gradients **in fully vectorized form** using **Jacobian matrices** and the chain rule, rather than element-by-element. The whole method reduces to: write the forward pass as a sequence of simple sub-operations, look up each operation's Jacobian from a short table of identities, multiply the Jacobians, and transpose at the end to satisfy the "gradient shape = parameter shape" convention. It closes with a complete worked backward pass for a one-hidden-layer classifier. It's the cleanest **vectorized-backprop cheat sheet** — the practical complement to a scalar autograd engine like [micrograd](karpathy-micrograd.md) and a lightweight on-ramp to the full treatment in [The Elements of Differentiable Programming](blondel-roulet-differentiable-programming.md).

## Key claims / content

**The method.** The Jacobian of `f: Rⁿ → Rᵐ` is the `m×n` matrix `(∂f/∂x)ᵢⱼ = ∂fᵢ/∂xⱼ`. Chain rule on vector-valued functions = **matrix-multiplying Jacobians**.

**The seven identities** (the reusable table — memorize or recover by shape-matching):
1. `z = Wx` → `∂z/∂x = W`
2. `z = xW` (row vector) → `∂z/∂x = Wᵀ`
3. `z = x` → `∂z/∂x = I` (vanishes in the chain rule)
4. `z = f(x)` elementwise → `∂z/∂x = diag(f′(x))` (≡ elementwise `∘ f′(x)`)
5. `z = Wx`, `δ = ∂J/∂z` → `∂J/∂W = δᵀxᵀ` (outer product)
6. `z = xW` → `∂J/∂W = xᵀδ`
7. **softmax + cross-entropy**: `ŷ = softmax(θ)`, `J = CE(y, ŷ)` → `∂J/∂θ = ŷ − y` (the single most-used identity in practice).

**Gradient-layout convention.** Jacobian form is ideal for *applying* the chain rule, but SGD wants **"the shape of the gradient equals the shape of the parameter"** (so you can do `θ ← θ − η·∇θ`). Practical rule: compute in Jacobian form, then **transpose** column-vector results in the final answer. A shape check (columns of each term = rows of the next) catches most errors.

**Worked example — 1-layer NN.** Forward: `z = Wx + b₁; h = ReLU(z); θ = Uh + b₂; ŷ = softmax(θ); J = CE(y, ŷ)`. Define **error signals** `δ₁ = ∂J/∂θ = (ŷ − y)ᵀ` and `δ₂ = ∂J/∂z = δ₁U ∘ sgn(h)` (using `ReLU′(x) = sgn(ReLU(x))`, i.e. the derivative written in terms of the activation itself — the trick that makes backprop reuse the forward pass). Then the parameter gradients:
- `∂J/∂U = δ₁ᵀhᵀ`, `∂J/∂b₂ = δ₁ᵀ`
- `∂J/∂W = δ₂ᵀxᵀ`, `∂J/∂b₁ = δ₂ᵀ`
- `∂J/∂x = (δ₂W)ᵀ`

The point of reusing `δ₁`, `δ₂`: computing `∂J/∂θ` once and passing it down avoids the redundant recomputation a naive per-parameter derivation would incur — exactly what autodiff does mechanically.

## Entities mentioned
- [Kevin Clark](../entities/kevin-clark.md) — author.

## Concepts touched
- Backpropagation / the chain rule — the operational core of [Curriculum Module 1 §3](../syntheses/curriculum/curriculum-01-neural-networks.md).
- [Cross-entropy](../glossary.md#ce) + softmax — the `ŷ − y` gradient (identity 7) underpins every classifier.
- Vectorization / Jacobians — pairs with the rigorous [Elements of Differentiable Programming](blondel-roulet-differentiable-programming.md) (forward/reverse-mode autodiff, ch. 8).

## Open questions / notes
- Scope is deliberately narrow: dense layers + ReLU + softmax-CE. No convolutions, attention, normalization-layer, or recurrent gradients — those are left as "figure them out by shape-matching" exercises.
- Assumes the loss is a scalar and uses the denominator-layout/numerator-layout mix common in ML notes; the "transpose at the end" convention papers over the layout subtleties that [Blondel & Roulet](blondel-roulet-differentiable-programming.md) treat formally.

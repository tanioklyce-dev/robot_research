---
title: Curriculum Module 1 — Neural networks and training
type: synthesis
created: 2026-05-10
updated: 2026-05-10
tags: [curriculum, module-1, neural-networks, mlp, backpropagation, sgd, adam, batch-norm, layer-norm, residual-connections]
prereqs: []
status: draft
---

> [!note] Curriculum context
> This is **Module 1** of the [Robot-learning curriculum](robot-learning-curriculum.md). Tier 1 — first module. No prerequisites beyond linear algebra (matrix multiplication, gradients) and calculus (chain rule, partial derivatives).
>
> Tier 1 modules are **brisk-but-rigorous refreshers**, not ground-zero textbooks. Audience: "strong programmer with some ML exposure" (per the curriculum's audience assumption). If the prereq diagnostic below feels comfortable, skim this module. If it doesn't, read carefully — every subsequent module assumes this material.
>
> Acronyms used here are also in the [Glossary](../../glossary.md). First-mention links go there.

> [!note] Video overview — recommended before reading
> [Welch Labs — "ChatGPT is made from 100 million of these [The Perceptron]" (Feb 2025)](../../sources/welchlabs-perceptron.md) walks the same arc this module covers — Rosenblatt 1957 → Mark I (1958) → XOR roadblock (Minsky & Papert 1969) → backprop (Rumelhart/Hinton/Williams 1986) → MLP-at-scale (GPT-3) — at the popular-explainer level. Good 20-min orientation before doing the math here. Pairs with the deeper-into-the-transformer [3Blue1Brown — How might LLMs store facts (Chapter 7)](../../sources/3blue1brown-mlp-in-llms.md) once Module 3 is in scope.

> [!note] Don't have a year of PyTorch under your belt?
> [fast.ai — Practical Deep Learning for Coders 2022](../../sources/fastai-practical-deep-learning.md) (Jeremy Howard) is the strongest library-first onboarding ramp before this curriculum. Lessons 1–3 cover image classification, deployment, and SGD-from-scratch in a hands-on PyTorch + fastai + Hugging Face workflow. Come back to this module afterwards.

## Prereq diagnostic

Can you answer these without notes?

1. Write the forward pass of a 2-layer MLP with ReLU activations, given input `x ∈ ℝ^d`.
2. Why does ReLU work better than sigmoid for deep networks?
3. State the chain rule for `∂L/∂w` where `L = f(g(w))` and explain how it generalizes to a deep network.
4. What's the difference between Batch Norm and Layer Norm? When would you use each?
5. Why are residual connections (`y = x + F(x)`) load-bearing for training networks deeper than ~10 layers?

If yes to all five, skim §1–8 and do the anchor exercise. If no to any, read the relevant section.

## What this module is

The mathematical machinery every subsequent module assumes. By the end you should be able to:

1. Implement a 2-layer MLP forward + backward pass in NumPy without consulting references.
2. Read `loss = ‖predictor(z_t, a_t) − z_{t+1}‖²` and know exactly what gradient flows through which parameters when you call `.backward()`.
3. Decide between Batch Norm and Layer Norm in a new architecture based on what the input distribution looks like.
4. Recognize when a model is overfitting and pick from the standard remedy menu (regularization, more data, smaller model, early stopping).

## §1 — The neuron and the MLP

A **neuron** is a linear map composed with a nonlinearity:

```
neuron:  h = σ(w^T x + b)
```

where `w ∈ ℝ^d` is the weight vector, `b ∈ ℝ` is the bias, `x ∈ ℝ^d` is the input, and `σ: ℝ → ℝ` is the **activation function**.

A **layer** is a stack of neurons sharing the same input. In matrix form, a layer is:

```
h = σ(W x + b)        W ∈ ℝ^{m × d},  b ∈ ℝ^m,  h ∈ ℝ^m
```

A **Multi-Layer Perceptron ([MLP](../../glossary.md#mlp))** stacks `L` layers:

```
h_1 = σ(W_1 x + b_1)
h_2 = σ(W_2 h_1 + b_2)
   ⋮
h_L = W_L h_{L-1} + b_L              // final layer often linear (no σ)
```

The output `h_L` is the model's prediction.

### Activation functions

The nonlinearity matters more than the architecture for "does this train?" questions.

- **Sigmoid** `σ(x) = 1/(1+e^{-x})` — bounded in (0,1); historically common; saturates and produces vanishing gradients for `|x| ≫ 0`. Don't use for hidden layers in deep networks.
- **Tanh** `σ(x) = (e^x − e^{-x})/(e^x + e^{-x})` — bounded in (-1, 1); same saturation problem.
- **ReLU** `σ(x) = max(0, x)` — the default since ~2012. Non-saturating in the positive direction; cheap to compute; gradient is 0 for `x < 0` (sometimes a problem; see "dead ReLU"). Module 5's DDPM, Module 11's ViT, and most modern networks use ReLU or close variants (GELU, SiLU).
- **GELU** `σ(x) = x · Φ(x)` (Φ = standard normal CDF) — a smooth ReLU approximation; standard in transformers and ViTs.

**Why ReLU works in deep networks:** the gradient is exactly 1 for active neurons, so there's no decay through depth. Sigmoid's gradient is bounded by 0.25, so a 10-layer sigmoid network multiplies gradients by ≤ 0.25^10 ≈ 10^{-6} per backward pass — they vanish.

## §2 — Loss functions

How do we measure prediction quality?

### Mean Squared Error ([MSE](../../glossary.md#mse))

For regression targets `y ∈ ℝ^k`:

```
L_MSE = ‖h_L − y‖² / k
```

Equivalent to maximum-likelihood under a Gaussian observation model. Used everywhere in this curriculum: JEPA's next-embedding prediction loss; DDPM's noise prediction loss; BC's MSE-MLP baseline.

### Cross-Entropy ([CE](../../glossary.md#ce))

For classification targets `y ∈ {1, …, K}`:

```
softmax(h_L)_k  =  exp(h_L_k) / Σ_j exp(h_L_j)
L_CE = −log( softmax(h_L)_y )                              // negative log-likelihood
```

Equivalent to maximum-likelihood under a categorical observation model. The standard classification loss. Module 7's BeT uses CE on action clusters.

### Why these and not others

Both MSE and CE have **interpretable gradients** that fall out cleanly from the chain rule (see §3). They also correspond to maximum-likelihood under specific observation noise models, which makes them the right choice unless you have specific reason to deviate.

## §3 — Gradient descent and backpropagation

To train, we need `∂L/∂θ` where `θ = (W_1, b_1, …, W_L, b_L)`. Then we update:

```
θ ← θ − η · ∂L/∂θ                                          // η is the learning rate
```

### The chain rule

For a composition `L = f(g(θ))`:

```
∂L/∂θ  =  (∂L/∂g) · (∂g/∂θ)
```

A neural network is a deep composition. The chain rule extends:

```
∂L/∂θ_l  =  (∂L/∂h_L) · (∂h_L/∂h_{L-1}) · ⋯ · (∂h_{l+1}/∂h_l) · (∂h_l/∂θ_l)
```

This is **backpropagation**: compute the loss `L`, then propagate `∂L/∂h_l` backward layer by layer using the chain rule. Each layer needs to know `∂h_l/∂h_{l-1}` (for the upstream gradient) and `∂h_l/∂θ_l` (for the layer's own parameter update).

Most of the time you don't compute backprop by hand — PyTorch's autograd does it from a graph trace. You should be able to do it by hand for a 2-layer MLP, though, to ground the intuition.

### Stochastic Gradient Descent ([SGD](../../glossary.md#sgd))

Computing `∂L/∂θ` over the full training set every step is expensive. Instead, sample a **minibatch** of `B` examples per step, compute the average gradient over the batch, and update:

```
θ ← θ − η · (1/B) · Σ_i ∂L_i/∂θ                            // L_i = loss on example i
```

Typical batch sizes: 32–256 for small models, up to 4K+ for large transformers.

### Adam ([Adam](../../glossary.md#adam))

A first-order SGD variant that adaptively scales the learning rate per parameter using running averages of gradients (first moment) and squared gradients (second moment):

```
m_t = β_1 · m_{t-1} + (1 − β_1) · g_t                      // running gradient mean
v_t = β_2 · v_{t-1} + (1 − β_2) · g_t²                     // running gradient variance
m̂_t = m_t / (1 − β_1^t),    v̂_t = v_t / (1 − β_2^t)        // bias correction
θ ← θ − η · m̂_t / (√v̂_t + ε)
```

Defaults: `β_1 = 0.9`, `β_2 = 0.999`, `ε = 10^{-8}`, `η = 10^{-3}`. **Adam (and its variant AdamW with decoupled weight decay) is the de-facto optimizer in 2024–2026.** Use it unless you have a specific reason not to.

## §4 — Overfitting and regularization

A model overfits when training loss is much lower than validation loss — it's memorized the training set rather than learning generalizable features.

### Standard remedies

- **Smaller model** — fewer parameters can't memorize as much.
- **More data** — the cleanest fix when available.
- **Weight decay (L2 regularization)** — add `λ · ‖θ‖²` to the loss; pulls weights toward zero. Implemented as part of AdamW.
- **Dropout** — during training, set a random subset of activations to zero with probability `p` (typical `p = 0.1` to `0.5`). Forces the network to not rely on any single neuron.
- **Data augmentation** — random crops, flips, color jitter for images; analogous for other modalities. Effectively expands the training set.
- **Early stopping** — monitor validation loss; stop when it starts increasing. Simple and effective.

### Why this matters for the curriculum

[Diffusion Policy](../../entities/diffusion-policy.md) (Module 7) uses dropout in the predictor. [JEPA-line](../../sources/lejepa-paper.md) work uses weight decay extensively. [LeWM](../../sources/leworldmodel-paper.md)'s 15M-param model is small enough to underfit, so regularization isn't the issue — for it, the issue is collapse (Module 4's main topic, not classical overfitting).

## §5 — Normalization

The most important architectural detail you can add to a deep network.

### Batch Normalization ([BN](../../glossary.md#bn))

Per Ioffe & Szegedy 2015. For each feature channel `j`:

```
μ_j = (1/B) · Σ_i x_{i,j}                                  // mean across batch
σ_j² = (1/B) · Σ_i (x_{i,j} − μ_j)²                        // variance across batch
x̂_{i,j} = (x_{i,j} − μ_j) / √(σ_j² + ε)                    // normalize
y_{i,j} = γ_j · x̂_{i,j} + β_j                              // learnable scale + shift
```

At inference, replace `(μ_j, σ_j²)` with running averages computed during training.

**When to use:** CNNs (where the batch dimension is meaningful and consistent).

**When NOT to use:** small batch sizes (BN statistics are noisy); recurrent networks (BN doesn't compose with time-step variation); transformers (use Layer Norm instead).

### Layer Normalization ([LN](../../glossary.md#ln))

Per Ba et al. 2016. Normalizes across features *per sample*:

```
μ_i = (1/d) · Σ_j x_{i,j}                                  // mean across features for example i
σ_i² = (1/d) · Σ_j (x_{i,j} − μ_i)²
x̂_{i,j} = (x_{i,j} − μ_i) / √(σ_i² + ε)
y_{i,j} = γ_j · x̂_{i,j} + β_j
```

**When to use:** transformers, RNNs, anywhere the batch dimension isn't statistically meaningful. **The transformer-default normalizer.**

> [!warning] LayerNorm interacts subtly with SSL losses
> [Module 12 §3.1](curriculum-12-lewm-deep-dive.md) covers an instance where LayerNorm at the encoder output *breaks* a SSL loss ([SIGReg](../../glossary.md#sigreg)) — because LayerNorm normalizes per-sample, the batch-level distribution SIGReg operates on gets pre-normalized away. The LeWM fix: swap to BN in the projection MLP. Worth remembering.

## §6 — Residual connections

Per He et al. 2015 ([ResNet](../../glossary.md#resnet)). Define each layer as a *residual*:

```
h_{l+1} = h_l + F(h_l)
```

where `F` is a learnable transformation (typically a small MLP or convolution block).

**Why this enables deep networks.** Without residuals, the gradient through `L` layers is a product of `L` Jacobians; if any Jacobian is small, gradients vanish. With residuals, the identity term in `h_{l+1} = h_l + F(h_l)` provides a path with unit gradient — the network can always propagate the gradient back through depth even if `F(h_l)` is producing tiny outputs.

He et al.'s headline result: 152-layer ResNet beats 22-layer GoogLeNet on ImageNet. Before residual connections, networks deeper than ~30 layers consistently *underperformed* shallower ones (the "degradation problem"). Residuals fix this.

### Where they appear

**Every modern architecture has residual connections.** Transformers wrap each attention and MLP block with `h_{l+1} = LN(h_l + F(h_l))`. ResNet-18/50/101/152 use them in CNN form. ViT uses them in transformer form. The U-Net used in [DDPM (Module 5)](curriculum-05-generative-models.md) has them. They're a structural primitive, not an optimization.

## §7 — Why depth helps

A theoretical question with a practical answer.

**Theory.** A 1-layer MLP with enough hidden units can approximate any continuous function (universal approximation theorem). So in principle you don't need depth — you need width.

**Practice.** Depth lets the network learn *compositional features* — early layers learn low-level primitives (edges in CNN; token embeddings in transformer); later layers compose them into higher-level concepts (objects; sentences; meanings). A 1-layer network would need *exponentially many* hidden units to express the same compositional features that a deep network learns with polynomial cost.

The practical answer is empirical: deep networks outperform shallow-and-wide ones across nearly every benchmark for sufficiently complex tasks. The standard depth in 2024–2026: ResNet-50 (50 layers), ViT-L (24 layers), GPT-line (32+ layers). For very small models like [LeWM](../../entities/leworldmodel.md)'s ViT-tiny: 12 layers.

## §8 — Practical training recipe

A minimal recipe that works in 2024–2026:

```
1. Model:      MLP with ~2–4 layers, ReLU/GELU activations, LayerNorm between layers.
               Add residual connections if > 10 layers.
2. Loss:       MSE for regression, CE for classification.
3. Optimizer:  AdamW(lr=1e-3 to 3e-4, weight_decay=1e-2, betas=(0.9, 0.999))
4. Schedule:   cosine annealing from initial lr to 1e-5 over training.
5. Batch size: 64–256 (smaller for small models, larger for transformers).
6. Augmentation: domain-specific (image flips, etc.).
7. Validation:  hold out 10–20% of data; track validation loss; early-stop on plateau.
```

This is enough for ~80% of supervised-learning settings. The remaining 20% (very deep transformers, very small datasets, very imbalanced classification, etc.) require more care — but you'll know when you've hit one.

## Anchor exercise

> **Train an MLP digit classifier on a tiny dataset. Reason about what "the embedding before the last layer" is.**

Concrete:

1. **Data.** MNIST (handwritten digits) or Fashion-MNIST. ~60k 28×28 grayscale images, 10 classes. The PyTorch `torchvision.datasets` API loads it in 2 lines.
2. **Model.** 3-layer MLP: 784 → 256 → 128 → 10. ReLU activations. ~250k parameters.
3. **Training.** Cross-entropy loss, AdamW, 5–10 epochs. Should reach ~97% test accuracy on MNIST.
4. **Probe the second-to-last layer.** Extract activations after the 128-unit hidden layer for ~1000 test images. Run t-SNE or UMAP to visualize in 2D. **You should see digit classes separating into clusters** — even though the classifier head is the only part of the model "trained to classify," the hidden layer's activations are already organized by digit identity. This is **the embedding** — a learned representation that captures task-relevant structure.
5. **Compare to random.** Run t-SNE on randomly-initialized hidden-layer activations (same architecture, no training). You should see no class separation. The training process is what shapes the embedding.

The point of the exercise: feel that **the embedding emerges as a side effect of training the classifier**. This is the foundation of everything in [Module 4](curriculum-04-self-supervised-learning.md) (SSL — train without labels, get useful embeddings anyway) and [Module 11](curriculum-11-jepa-deep.md) (JEPA — train to predict next embeddings; the latent space is the object of interest).

If you want a deeper variant: replace MNIST with [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) and the MLP with a small CNN. The accuracy will drop (MLP on CIFAR is hard); replacing with a small ResNet brings it back. This previews [Module 2](curriculum-02-cnns.md).

## Recommended reading

In order of effort:

1. **3Blue1Brown's [Neural Networks series](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)** (YouTube, free) — for visual / intuitive coverage of forward pass + backprop. Most concise way to get the intuitions.
2. **Goodfellow, Bengio, Courville — *[Deep Learning](https://www.deeplearningbook.org/)*** (textbook, free online) — chapters 1–6. Authoritative but verbose. Skim.
3. **PyTorch's [60-minute blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)** — hands-on starter; gets you to a working MLP fast.
4. **Karpathy's [micrograd](../../sources/karpathy-micrograd.md)** — backprop in ~100 lines of Python; the cleanest "I understand backprop" milestone. ([repo](https://github.com/karpathy/micrograd); wiki source page covers structure, the `Value`-class scalar autograd design, and the demo notebook.)

## What you should now be able to do

- Read any subsequent module's "loss = ‖f(x) − y‖²" formulation without confusion.
- Diagnose a stuck training run: vanishing gradients, exploding gradients, dead ReLU, batch too small for BN, learning rate too high or low.
- Pick BN vs LN appropriately when designing a new architecture.
- Recognize when a deep network needs residual connections (basically: always if > 10 layers).
- Write the AdamW optimizer's update rule from memory.

## Hand-off

Module 1 is the foundation for:

- **[Module 2](curriculum-02-cnns.md) — CNNs** — specialized neural networks for spatial input.
- **[Module 3](curriculum-03-attention-and-transformers.md) — Sequence models** — specialized neural networks for sequential input.
- **[Module 4](curriculum-04-self-supervised-learning.md) — SSL** — using neural networks for representation learning without labels.
- **[Module 5](curriculum-05-generative-models.md) — Generative models** — using neural networks to model `p(x)`.

Every subsequent module assumes you can read the math in §1–8.

## Related curriculum modules

- All later modules build on this one.
- [Module 4](curriculum-04-self-supervised-learning.md) — the "embedding before the last layer" idea generalizes.
- [Module 5](curriculum-05-generative-models.md) — uses U-Nets (CNN-based; Module 2) trained with the standard recipe in §8.

## Mentioned in

- [Robot-learning curriculum](robot-learning-curriculum.md)
- [Index](../../index.md)

## Open questions / TBD

- **Karpathy's neural-network-from-scratch lecture series** as a wiki source page — would be the cleanest external reference for this module if filed.
- **A "common training pathologies" reference page** — vanishing gradients, exploding gradients, dead ReLU, loss-not-decreasing failure modes — would help readers debug their own experiments.

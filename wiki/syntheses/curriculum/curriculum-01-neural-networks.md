---
title: Curriculum Module 1 — Neural networks and training
type: synthesis
created: 2026-05-10
updated: 2026-07-09
tags: [curriculum, module-1, neural-networks, mlp, backpropagation, sgd, adam, batch-norm, layer-norm, residual-connections]
prereqs: []
status: draft
---

> [!note] Curriculum context
> This is **Module 1** of the [Robot-learning curriculum](robot-learning-curriculum.md). Tier 1 — first module. No prerequisites beyond linear algebra (matrix multiplication) and calculus (derivatives, the chain rule) — and §0 below reviews the notation for both.
>
> This module was originally written as a brisk refresher for readers who already knew the material. It has since been expanded to *teach* the material: every symbol is defined when it first appears, and each equation is followed by a plain-English reading. If you already know this stuff, the equations and bold takeaways skim well; if you don't, read it top to bottom — every subsequent module assumes it.
>
> Acronyms used here are also in the [Glossary](../../glossary.md). First-mention links go there.

> [!note] Video overview — recommended before reading
> [Welch Labs — "ChatGPT is made from 100 million of these [The Perceptron]" (Feb 2025)](../../sources/welchlabs-perceptron.md) walks the same arc this module covers — Rosenblatt 1957 → Mark I (1958) → XOR roadblock (Minsky & Papert 1969) → backprop (Rumelhart/Hinton/Williams 1986) → MLP-at-scale (GPT-3) — at the popular-explainer level. Good 20-min orientation before doing the math here. Pairs with the deeper-into-the-transformer [3Blue1Brown — How might LLMs store facts (Chapter 7)](../../sources/3blue1brown-mlp-in-llms.md) once Module 3 is in scope.

> [!note] Don't have a year of PyTorch under your belt?
> [fast.ai — Practical Deep Learning for Coders 2022](../../sources/fastai-practical-deep-learning.md) (Jeremy Howard) is the strongest library-first onboarding ramp before this curriculum. Lessons 1–3 cover image classification, deployment, and SGD-from-scratch in a hands-on PyTorch + fastai + Hugging Face workflow. Come back to this module afterwards.

## Prereq diagnostic

Can you answer these without notes?

1. Write the forward pass of a 2-layer MLP with ReLU activations, given input $x \in \mathbb{R}^d$.
2. Why does ReLU work better than sigmoid for deep networks?
3. State the chain rule for $\partial L / \partial w$ where $L = f(g(w))$, and explain how it generalizes to a deep network.
4. What's the difference between Batch Norm and Layer Norm? When would you use each?
5. Why are residual connections ($y = x + F(x)$) load-bearing for training networks deeper than ~10 layers?

If yes to all five, skim §1–8 and do the anchor exercise. **If no to some or all — that's fine and expected.** This module teaches every one of them; by the end, come back and try again.

## What this module is

The mathematical machinery every subsequent module assumes. By the end you should be able to:

1. Implement a 2-layer MLP forward + backward pass in NumPy without consulting references.
2. Read $\text{loss} = \|\text{predictor}(z_t, a_t) - z_{t+1}\|^2$ and know exactly what gradient flows through which parameters when you call `.backward()`.
3. Decide between Batch Norm and Layer Norm in a new architecture based on what the input distribution looks like.
4. Recognize when a model is overfitting and pick from the standard remedy menu (regularization, more data, smaller model, early stopping).

## §0 — How to read the math

Deep-learning papers compress a lot into notation. Here is the full decoder ring for this module (and most of the curriculum):

**Vectors and matrices.**

- $x \in \mathbb{R}^d$ — "$x$ is a vector of $d$ real numbers." Think of it as a plain array of length $d$, like a Python list of floats. $\mathbb{R}$ is the set of real numbers; the superscript is the length.
- $W \in \mathbb{R}^{m \times d}$ — "$W$ is a matrix with $m$ rows and $d$ columns" — a 2-D array. Capital letters are usually matrices; lowercase are vectors or scalars.
- $Wx$ — matrix–vector multiplication. Takes a length-$d$ vector in, produces a length-$m$ vector out. Each output entry is a weighted sum of all the input entries, using one row of $W$ as the weights.
- $w^\top x$ — the **dot product**: multiply the vectors entry-by-entry and add it all up, $w_1 x_1 + w_2 x_2 + \dots + w_d x_d$. One number out. The $\top$ means "transpose" (flip a column vector into a row vector so the multiplication is shape-legal) — in practice, just read $w^\top x$ as "weighted sum of $x$ with weights $w$."
- $\sum_i a_i$ — summation: add up the $a_i$ over all values of the index $i$.
- $\|v\|^2$ — the **squared length** of a vector: $\|v\|^2 = \sum_i v_i^2$, the sum of squared entries. Measures "how big" a vector is; used constantly in losses, where $\|{\text{prediction}} - {\text{target}}\|^2$ means "sum of squared errors, entry by entry."

**Derivatives.**

- $\partial L / \partial w$ — a **partial derivative**: "if I nudge $w$ up by a tiny amount, how much does $L$ change, and in which direction?" Positive means increasing $w$ increases $L$; negative means increasing $w$ decreases $L$. When $w$ is a whole vector or matrix of parameters, $\partial L / \partial w$ is a same-shaped array of these per-entry sensitivities, called the **gradient**.
- The gradient points in the direction of *steepest increase* of $L$. To make $L$ smaller, move in the opposite direction. That single fact is what all of training is built on (§3).

**Conventions.**

- Greek letters are almost always knobs or small quantities: $\sigma$ (an activation function), $\eta$ (learning rate), $\lambda$ (regularization strength), $\beta$ (momentum coefficients), $\epsilon$ (a tiny constant to avoid dividing by zero), $\mu$ (a mean), $\sigma^2$ (a variance).
- Subscripts index things: $h_l$ is the activation at layer $l$; $x_{i,j}$ is feature $j$ of example $i$ in a batch; $m_t$ is a quantity at training step $t$.
- A hat ($\hat{m}$) usually means "a corrected or estimated version of $m$."

If you can read $h = \sigma(Wx + b)$ as "multiply the input vector by a weight matrix, add a bias vector, then apply a squashing function to each entry," you're ready for §1.

## §1 — The neuron and the MLP

A **neuron** is the atom of a neural network: it computes a weighted sum of its inputs, adds a constant, and passes the result through a simple nonlinear function:

$$h = \sigma(w^\top x + b)$$

where $x \in \mathbb{R}^d$ is the input, $w \in \mathbb{R}^d$ is the neuron's **weight vector** (how much it cares about each input entry), $b \in \mathbb{R}$ is the **bias** (a learnable offset that shifts the neuron's activation threshold), and $\sigma : \mathbb{R} \to \mathbb{R}$ is the **activation function** — a fixed nonlinear function applied to the single number that comes out of the weighted sum. In words: *score the input with a weighted sum, then squash or clip the score.*

A **layer** is a stack of $m$ neurons all looking at the same input. Rather than write $m$ separate dot products, we collect all the weight vectors as rows of a matrix and write the whole layer as one matrix multiplication:

$$h = \sigma(Wx + b) \qquad W \in \mathbb{R}^{m \times d},\; b \in \mathbb{R}^m,\; h \in \mathbb{R}^m$$

Here $\sigma$ is applied entry-wise: each of the $m$ output numbers gets squashed independently.

A **Multi-Layer Perceptron ([MLP](../../glossary.md#mlp))** feeds the output of one layer into the next, $L$ times:

$$
\begin{aligned}
h_1 &= \sigma(W_1 x + b_1) \\
h_2 &= \sigma(W_2 h_1 + b_2) \\
&\;\;\vdots \\
h_L &= W_L h_{L-1} + b_L \qquad \text{(final layer usually linear — no } \sigma\text{)}
\end{aligned}
$$

The output $h_L$ is the model's prediction. The final layer usually skips the activation because the output needs to be able to take any value (for regression) or get converted to probabilities by a separate step (for classification, §2).

**Why the nonlinearity is not optional.** If you removed every $\sigma$, the stack of layers would collapse into a single matrix multiplication ($W_2(W_1 x) = (W_2 W_1)x$ — a matrix times a matrix is just another matrix). A "deep" network without activation functions is mathematically identical to a 1-layer linear model, no matter how many layers you stack. The nonlinearity is what lets depth buy you anything at all.

### Activation functions

The choice of nonlinearity matters more than the architecture for "does this train?" questions. The recurring villain here is **saturation**: a region of the activation function that is nearly flat. Flat means derivative ≈ 0, and (as §3 will make precise) derivative ≈ 0 means *no learning signal flows backward through that neuron*.

- **Sigmoid** — $\sigma(x) = \dfrac{1}{1+e^{-x}}$. An S-shaped curve squashing any input into the range $(0, 1)$. Historically the default (it looks like a smooth on/off switch). But it flattens out for inputs far from zero — for $|x| \gg 0$ the curve is essentially horizontal, gradients vanish, and learning stalls. Don't use it for hidden layers in deep networks.
- **Tanh** — $\sigma(x) = \dfrac{e^{x} - e^{-x}}{e^{x} + e^{-x}}$. Same S-shape, but squashes into $(-1, 1)$ and is centered on zero (a modest improvement). Same saturation problem.
- **ReLU** ("rectified linear unit") — $\sigma(x) = \max(0, x)$. Outputs the input unchanged if positive, zero otherwise. The default since ~2012. It never saturates on the positive side, and it's nearly free to compute. Its one flaw: the gradient is exactly 0 for $x < 0$, so a neuron whose input is always negative learns nothing — a "**dead ReLU**." Module 5's DDPM, Module 11's ViT, and most modern networks use ReLU or close variants (GELU, SiLU).
- **GELU** — $\sigma(x) = x \cdot \Phi(x)$, where $\Phi$ is the standard normal CDF (the smooth 0-to-1 ramp giving the probability a standard Gaussian lands below $x$). Behaves like a smoothed ReLU with no hard corner at zero. Standard in transformers and ViTs.

**Why ReLU works in deep networks:** for any active (positive-input) neuron, ReLU's derivative is exactly 1 — the learning signal passes through *undiminished*, layer after layer. Sigmoid's derivative peaks at 0.25, so a 10-layer sigmoid network multiplies the backward signal by at most $0.25^{10} \approx 10^{-6}$ — the gradient **vanishes** to nothing before it reaches the early layers, and they never learn.

## §2 — Loss functions

Training needs a single number that says how wrong the current prediction is — the **loss**. Lower is better; training is the process of driving it down. Two losses cover nearly everything in this curriculum.

### Mean Squared Error ([MSE](../../glossary.md#mse))

For **regression** — predicting continuous values, with target $y \in \mathbb{R}^k$:

$$L_{\text{MSE}} = \frac{1}{k}\,\|h_L - y\|^2$$

In words: subtract the target from the prediction entry-by-entry, square each difference (so over- and under-shooting both count, and big errors count disproportionately), and average. Squaring is also what makes the loss smooth and differentiable everywhere, which §3 needs.

MSE is equivalent to maximum-likelihood under a Gaussian observation model — that is, if you assume your targets are "the true value plus Gaussian noise," then the statistically principled thing to do is exactly to minimize squared error. Used everywhere in this curriculum: JEPA's next-embedding prediction loss; DDPM's noise prediction loss; BC's MSE-MLP baseline.

### Cross-Entropy ([CE](../../glossary.md#ce))

For **classification** — picking one of $K$ classes, with target $y \in \{1, \dots, K\}$. Two steps. First, the network's raw outputs $h_L$ (called **logits** — $K$ unbounded scores, one per class) are converted into probabilities by the **softmax** function:

$$\text{softmax}(h_L)_k = \frac{e^{h_{L,k}}}{\sum_j e^{h_{L,j}}}$$

In words: exponentiate every score (making them all positive and exaggerating differences), then divide by the total so they sum to 1. The result is a proper probability distribution over the $K$ classes.

Second, the loss is the negative log of the probability the model assigned to the *correct* class:

$$L_{\text{CE}} = -\log\big(\text{softmax}(h_L)_y\big)$$

In words: if the model put probability 0.9 on the right answer, the loss is $-\log(0.9) \approx 0.1$ — small. If it put probability 0.01 on the right answer, the loss is $-\log(0.01) \approx 4.6$ — large. The logarithm makes the penalty explode as the model gets *confidently* wrong, which is exactly the behavior you want to punish. (This is also called the **negative log-likelihood**.)

CE is equivalent to maximum-likelihood under a categorical observation model. It's the standard classification loss. Module 7's BeT uses CE on action clusters.

### Why these and not others

Both MSE and CE have **clean, interpretable gradients** that fall out of the chain rule (see §3) — e.g. softmax-plus-CE famously reduces to the simple gradient "predicted probabilities minus true one-hot vector." And both correspond to maximum-likelihood under a specific noise model, which makes them the principled default unless you have a specific reason to deviate.

## §3 — Gradient descent and backpropagation

Training is an optimization problem: find the parameter values that make the loss small. Write $\theta$ for the full bag of parameters, $\theta = (W_1, b_1, \dots, W_L, b_L)$. If we can compute the gradient $\partial L / \partial \theta$ — how sensitive the loss is to each individual parameter — then we can improve every parameter a little bit at once by stepping *against* the gradient (recall from §0: the gradient points uphill, so minus the gradient points downhill):

$$\theta \leftarrow \theta - \eta \cdot \frac{\partial L}{\partial \theta}$$

where $\eta$ (the **learning rate**) controls the step size. Too small and training crawls; too large and you leap over the valley and the loss oscillates or explodes. This loop — compute loss, compute gradient, take a small downhill step, repeat — is **gradient descent**, and it is the entire training algorithm. Everything else in this section is about computing that gradient efficiently.

### The chain rule

The one calculus fact that powers all of deep learning. For a composition of functions $L = f(g(\theta))$:

$$\frac{\partial L}{\partial \theta} = \frac{\partial L}{\partial g} \cdot \frac{\partial g}{\partial \theta}$$

In words: the sensitivity of the final output to $\theta$ is the sensitivity of the output to the intermediate value, times the sensitivity of the intermediate value to $\theta$. Sensitivities *multiply* through a chain of functions. (Concretely: if a 10% nudge in $\theta$ moves $g$ by 5%, and a 5% move in $g$ moves $L$ by 1%, then the nudge moved $L$ by 1% — you multiply the two ratios.)

A neural network is exactly such a chain — a deep composition of layers — so the chain rule extends link by link. The gradient of the loss with respect to layer $l$'s parameters $\theta_l$ is the product of every layer-to-layer sensitivity between the loss and layer $l$:

$$\frac{\partial L}{\partial \theta_l} = \frac{\partial L}{\partial h_L} \cdot \frac{\partial h_L}{\partial h_{L-1}} \cdots \frac{\partial h_{l+1}}{\partial h_l} \cdot \frac{\partial h_l}{\partial \theta_l}$$

This is **backpropagation**: run the network forward to compute the loss $L$, then sweep *backward* through the layers, at each step multiplying in one more link of the chain. Each layer only needs to know two local quantities: $\partial h_l / \partial h_{l-1}$ (how its output depends on its input — passed further upstream) and $\partial h_l / \partial \theta_l$ (how its output depends on its own parameters — used for that layer's update). No layer needs global knowledge; the chain rule stitches the local pieces together.

Notice this equation is also the *why* behind two things from earlier: a long product of per-layer sensitivities each < 1 shrinks exponentially (**vanishing gradients**, §1's sigmoid problem), and each > 1 grows exponentially (**exploding gradients**). Deep-network architecture design (§5, §6) is largely about keeping this product well-behaved.

Most of the time you don't compute backprop by hand — PyTorch's autograd does it from a graph trace. You should be able to do it by hand for a 2-layer MLP, though, to ground the intuition. The cleanest reference for doing exactly that *in vectorized form* is [Kevin Clark's CS224n gradient notes](../../sources/clark-computing-nn-gradients.md): seven reusable Jacobian identities (incl. the workhorse $\partial J / \partial \theta = \hat{y} - y$ for softmax-CE) plus a full worked backward pass for a 1-hidden-layer classifier, ending exactly at the [anchor exercise](#anchor-exercise) below.

### Stochastic Gradient Descent ([SGD](../../glossary.md#sgd))

The loss above is really the average loss over the *entire training set* — and computing the exact gradient would mean running every training example through the network for every single update step. Far too slow. Instead, sample a small random **minibatch** of $B$ examples per step, average the gradient over just those, and update:

$$\theta \leftarrow \theta - \eta \cdot \frac{1}{B} \sum_{i=1}^{B} \frac{\partial L_i}{\partial \theta} \qquad (L_i = \text{loss on example } i)$$

The minibatch gradient is a *noisy estimate* of the true gradient — each step points roughly downhill rather than exactly — but it's unbiased (right on average), and taking thousands of cheap approximate steps beats taking a few exact ones. That's the "stochastic" in SGD. Typical batch sizes: 32–256 for small models, up to 4K+ for large transformers.

### Adam ([Adam](../../glossary.md#adam))

Plain SGD has two annoyances: the minibatch noise makes steps jittery, and one global learning rate $\eta$ must fit all parameters — but some parameters routinely get large gradients and some tiny ones. **Adam** fixes both by maintaining, *for every individual parameter*, two running averages of its gradient $g_t$: the recent mean (the "first moment" — which way has this gradient been pointing on average?) and the recent mean of its square (the "second moment" — how big has it typically been?):

$$
\begin{aligned}
m_t &= \beta_1\, m_{t-1} + (1 - \beta_1)\, g_t
  && \text{running mean of the gradient (smooths out minibatch noise)} \\
v_t &= \beta_2\, v_{t-1} + (1 - \beta_2)\, g_t^2
  && \text{running mean of the squared gradient (tracks typical size)} \\
\hat{m}_t &= \frac{m_t}{1 - \beta_1^t}, \qquad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}
  && \text{bias correction (see below)} \\
\theta &\leftarrow \theta - \eta \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}
\end{aligned}
$$

Reading the update line: step in the direction of the *smoothed* gradient $\hat{m}_t$, but divide by $\sqrt{\hat{v}_t}$ — the gradient's typical magnitude — so a parameter with habitually huge gradients takes proportionally smaller steps and one with tiny gradients takes larger ones. Every parameter effectively gets its own auto-tuned learning rate. The $\epsilon$ just prevents division by zero. The **bias correction** exists because $m_0 = v_0 = 0$, so early in training the running averages are dragged toward zero; dividing by $(1 - \beta^t)$ exactly undoes that (the correction fades to nothing as $t$ grows).

Defaults: $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\epsilon = 10^{-8}$, $\eta = 10^{-3}$. **Adam (and its variant AdamW with decoupled weight decay) is the de-facto optimizer in 2024–2026.** Use it unless you have a specific reason not to.

## §4 — Overfitting and regularization

A model **overfits** when training loss is much lower than validation loss — it has *memorized* the training set rather than learning features that **generalize** (work on data it hasn't seen). The classic tell: training loss keeps falling while loss on held-out data flattens and then rises. It's the student who memorized last year's exam answers instead of learning the method — perfect on the practice test, lost on the real one.

### Standard remedies

- **Smaller model** — fewer parameters can't memorize as much; the model is forced to learn compressed, general patterns instead.
- **More data** — the cleanest fix when available: with enough varied examples, memorizing becomes harder than generalizing.
- **Weight decay (L2 regularization)** — add $\lambda \cdot \|\theta\|^2$ to the loss, where $\lambda$ sets the strength. This charges the model "rent" on large weights, pulling all of them gently toward zero; the model keeps a weight large only when it genuinely pays for itself in loss reduction. Implemented as part of AdamW.
- **Dropout** — during training, set a random subset of activations to zero with probability $p$ (typical $p = 0.1$ to $0.5$), a fresh random subset every step. No neuron can be relied on to always be present, so the network can't route everything through a few memorizing neurons — it must spread the work redundantly. (At inference, dropout turns off.)
- **Data augmentation** — random crops, flips, color jitter for images; analogous transforms for other modalities. Each training image is seen slightly differently every epoch, effectively expanding the training set.
- **Early stopping** — monitor validation loss during training; stop when it starts increasing even though training loss is still falling. Simple and effective.

### Why this matters for the curriculum

[Diffusion Policy](../../entities/diffusion-policy.md) (Module 7) uses dropout in the predictor. [JEPA-line](../../sources/lejepa-paper.md) work uses weight decay extensively. [LeWM](../../sources/leworldmodel-paper.md)'s 15M-param model is small enough to underfit, so regularization isn't the issue — for it, the issue is collapse (Module 4's main topic, not classical overfitting).

## §5 — Normalization

The most important architectural detail you can add to a deep network. The problem it solves: as activations flow through many layers, their scale can drift — grow without bound or shrink toward zero — and each layer's input distribution keeps shifting under it as earlier layers update. Both effects destabilize training. The fix is blunt and effective: at chosen points in the network, **re-standardize the activations** — shift them to mean 0 and rescale to variance 1 — so every layer always sees inputs in a healthy, predictable range. The two standard variants differ only in *which direction they compute the statistics over*.

### Batch Normalization ([BN](../../glossary.md#bn))

Per Ioffe & Szegedy 2015. Recall that training processes a minibatch of $B$ examples at once, so at any layer the activations form a $B \times d$ array: $x_{i,j}$ is feature $j$ of example $i$. BN standardizes each **feature** (each column $j$) using statistics computed **across the batch** — "for feature $j$, what's the mean and variance over the $B$ examples currently in front of me?":

$$
\begin{aligned}
\mu_j &= \frac{1}{B} \sum_{i} x_{i,j}
  && \text{mean of feature } j \text{ across the batch} \\
\sigma_j^2 &= \frac{1}{B} \sum_{i} (x_{i,j} - \mu_j)^2
  && \text{variance of feature } j \text{ across the batch} \\
\hat{x}_{i,j} &= \frac{x_{i,j} - \mu_j}{\sqrt{\sigma_j^2 + \epsilon}}
  && \text{standardize: shift to mean 0, scale to variance 1} \\
y_{i,j} &= \gamma_j\, \hat{x}_{i,j} + \beta_j
  && \text{learnable re-scale and re-shift}
\end{aligned}
$$

The last line matters: $\gamma_j$ and $\beta_j$ are *learned* parameters that let the network undo the normalization wherever mean-0/variance-1 isn't actually what it wants — normalization constrains the *default*, not the expressiveness.

At inference there may be no meaningful batch (you might be classifying one image), so the batch statistics $(\mu_j, \sigma_j^2)$ are replaced with running averages accumulated during training.

**When to use:** CNNs (where the batch dimension is meaningful and consistent).

**When NOT to use:** small batch sizes (statistics estimated from a handful of examples are too noisy); recurrent networks (BN doesn't compose with time-step variation); transformers (use Layer Norm instead).

### Layer Normalization ([LN](../../glossary.md#ln))

Per Ba et al. 2016. Same standardize-then-rescale recipe, but the statistics are computed in the *other direction*: **across the features of a single example**, one example at a time. "For example $i$, what's the mean and variance over its own $d$ features?"

$$
\begin{aligned}
\mu_i &= \frac{1}{d} \sum_{j} x_{i,j}
  && \text{mean across features, for example } i \text{ alone} \\
\sigma_i^2 &= \frac{1}{d} \sum_{j} (x_{i,j} - \mu_i)^2 \\
\hat{x}_{i,j} &= \frac{x_{i,j} - \mu_i}{\sqrt{\sigma_i^2 + \epsilon}} \\
y_{i,j} &= \gamma_j\, \hat{x}_{i,j} + \beta_j
\end{aligned}
$$

Because each example is normalized using only itself, LN doesn't care what else is in the batch — batch size 1 works fine, and inference needs no running averages.

**When to use:** transformers, RNNs, anywhere the batch dimension isn't statistically meaningful. **The transformer-default normalizer.**

> [!warning] LayerNorm interacts subtly with SSL losses
> [Module 12 §3.1](curriculum-12-lewm-deep-dive.md) covers an instance where LayerNorm at the encoder output *breaks* a SSL loss ([SIGReg](../../glossary.md#sigreg)) — because LayerNorm normalizes per-sample, the batch-level distribution SIGReg operates on gets pre-normalized away. The LeWM fix: swap to BN in the projection MLP. Worth remembering.

## §6 — Residual connections

Per He et al. 2015 ([ResNet](../../glossary.md#resnet)). Instead of each layer *replacing* its input with a transformed version, define each layer as the input *plus* a learned correction (a "residual"):

$$h_{l+1} = h_l + F(h_l)$$

where $F$ is a learnable transformation (typically a small MLP or convolution block). The layer's job shifts from "compute the new representation from scratch" to "compute what to *add* to the current one" — and if $F$ outputs zero, the layer is simply an identity, passing its input through untouched.

**Why this enables deep networks.** Recall §3: the gradient reaching early layers is a *product* of per-layer sensitivities ($\partial h_{l+1} / \partial h_l$ terms — each one a matrix of these sensitivities, called a **Jacobian**), and a long product of small terms vanishes exponentially. Differentiating $h_{l+1} = h_l + F(h_l)$ gives the sensitivity as **identity + (derivative of $F$)** — the "+ $h_l$" term contributes a clean, always-present 1. So even if $F$'s contribution is tiny, the gradient can flow backward through the identity path completely undiminished, through any number of layers. Residuals build a gradient highway through depth.

He et al.'s headline result: 152-layer ResNet beats 22-layer GoogLeNet on ImageNet. Before residual connections, networks deeper than ~30 layers consistently *underperformed* shallower ones (the "degradation problem" — remarkable because a deeper network could in principle just imitate a shallow one by making its extra layers identities, yet plain deep networks couldn't even learn that). Residuals fix this by making "extra layer = identity" the starting point rather than something to be learned.

### Where they appear

**Every modern architecture has residual connections.** Transformers wrap each attention and MLP block with $h_{l+1} = \text{LN}(h_l + F(h_l))$. ResNet-18/50/101/152 use them in CNN form. ViT uses them in transformer form. The U-Net used in [DDPM (Module 5)](curriculum-05-generative-models.md) has them. They're a structural primitive, not an optimization.

## §7 — Why depth helps

A theoretical question with a practical answer.

**Theory.** The **universal approximation theorem** says a 1-layer MLP with enough hidden units can approximate any continuous function to any precision. So in principle you never need depth — a wide-enough shallow network can represent anything. (The catch is in "enough hidden units.")

**Practice.** Depth lets the network learn *compositional features* — early layers learn low-level primitives (edges in a CNN; token embeddings in a transformer); later layers combine those primitives into higher-level concepts (objects; sentences; meanings), reusing the same low-level parts across many high-level ones. A 1-layer network gets no reuse — it would need *exponentially many* hidden units to separately represent every combination that a deep network expresses compositionally at polynomial cost.

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

(Line 4, **cosine annealing**: rather than a fixed learning rate, decay it smoothly from its initial value down to near-zero over the course of training, following the shape of a cosine curve — big exploratory steps early, fine-tuning steps late. It's the standard schedule and most frameworks provide it as a one-liner.)

This is enough for ~80% of supervised-learning settings. The remaining 20% (very deep transformers, very small datasets, very imbalanced classification, etc.) require more care — but you'll know when you've hit one.

## Anchor exercise

> **Train an MLP digit classifier on a tiny dataset. Reason about what "the embedding before the last layer" is.**

Concrete:

1. **Data.** MNIST (handwritten digits) or Fashion-MNIST. ~60k 28×28 grayscale images, 10 classes. The PyTorch `torchvision.datasets` API loads it in 2 lines.
2. **Model.** 3-layer MLP: 784 → 256 → 128 → 10. ReLU activations. ~250k parameters. (784 because each 28×28 image is flattened into a vector of 784 pixel values; 10 because there are 10 digit classes.)
3. **Training.** Cross-entropy loss, AdamW, 5–10 epochs (an **epoch** = one full pass through the training set). Should reach ~97% test accuracy on MNIST.
4. **Probe the second-to-last layer.** Extract activations after the 128-unit hidden layer for ~1000 test images — each image gives you a 128-number vector. Run t-SNE or UMAP (standard tools that squash high-dimensional vectors down to 2D while keeping similar vectors near each other, so you can plot them) to visualize. **You should see digit classes separating into clusters** — even though the classifier head is the only part of the model "trained to classify," the hidden layer's activations are already organized by digit identity. This is **the embedding** — a learned representation that captures task-relevant structure.
5. **Compare to random.** Run t-SNE on randomly-initialized hidden-layer activations (same architecture, no training). You should see no class separation. The training process is what shapes the embedding.

The point of the exercise: feel that **the embedding emerges as a side effect of training the classifier**. This is the foundation of everything in [Module 4](curriculum-04-self-supervised-learning.md) (SSL — train without labels, get useful embeddings anyway) and [Module 11](curriculum-11-jepa-deep.md) (JEPA — train to predict next embeddings; the latent space is the object of interest).

If you want a deeper variant: replace MNIST with [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) and the MLP with a small CNN. The accuracy will drop (MLP on CIFAR is hard); replacing with a small ResNet brings it back. This previews [Module 2](curriculum-02-cnns.md).

## Recommended reading

In order of effort:

1. **3Blue1Brown's [Neural Networks series](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)** (YouTube, free) — for visual / intuitive coverage of forward pass + backprop. Most concise way to get the intuitions.
1. **Google's [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)** (free, browser-based) — short video/text lessons with **interactive in-browser exercises**; the [Neural Networks module](https://developers.google.com/machine-learning/crash-course/neural-networks) (~75 min) covers nodes, hidden layers, activation functions, and backprop hands-on. Good for *playing with* the ideas in §1–§3 rather than just reading them. Start at the [prereqs & prework page](https://developers.google.com/machine-learning/crash-course/prereqs-and-prework) to see what it assumes (algebra, basic Python; Colab-hosted exercises, no local setup).
1. **Karpathy's [Neural Networks: Zero to Hero](../../sources/karpathy-nn-zero-to-hero.md)** (YouTube, free) — lectures 1–5 live-code this module's §1–§5 from scratch (backprop → MLP → train/dev/test hygiene → activation statistics + BatchNorm → manual backprop). The *do-the-work* video companion to this module: lecture 1 builds micrograd (below) on video; lecture 5 is the video form of the Clark notes (below).
2. **Goodfellow, Bengio, Courville — *[Deep Learning](https://www.deeplearningbook.org/)*** (textbook, free online) — chapters 1–6. Authoritative but verbose. Skim.
3. **PyTorch's [60-minute blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)** — hands-on starter; gets you to a working MLP fast.
4. **Karpathy's [micrograd](../../sources/karpathy-micrograd.md)** — backprop in ~100 lines of Python; the cleanest "I understand backprop" milestone. ([repo](https://github.com/karpathy/micrograd); wiki source page covers structure, the `Value`-class scalar autograd design, and the demo notebook.)
5. **[Kevin Clark — Computing Neural Network Gradients (CS224n)](../../sources/clark-computing-nn-gradients.md)** — the vectorized-backprop cheat sheet: Jacobian identities + the "gradient shape = parameter shape" convention + a worked 1-layer-NN backward pass. Do this *after* micrograd (scalar) to graduate to matrix/vector form; it's the on-ramp to the rigorous [Elements of Differentiable Programming](../../sources/blondel-roulet-differentiable-programming.md).

## What you should now be able to do

- Read any subsequent module's $\text{loss} = \|f(x) - y\|^2$ formulation without confusion.
- Diagnose a stuck training run: vanishing gradients, exploding gradients, dead ReLU, batch too small for BN, learning rate too high or low.
- Pick BN vs LN appropriately when designing a new architecture.
- Recognize when a deep network needs residual connections (basically: always if > 10 layers).
- Write the AdamW optimizer's update rule from memory.

## Hand-off

Module 1 is the foundation for:

- **[Module 2](curriculum-02-cnns.md) — CNNs** — specialized neural networks for spatial input.
- **[Module 3](curriculum-03-attention-and-transformers.md) — Sequence models** — specialized neural networks for sequential input.
- **[Module 4](curriculum-04-self-supervised-learning.md) — SSL** — using neural networks for representation learning without labels.
- **[Module 5](curriculum-05-generative-models.md) — Generative models** — using neural networks to model $p(x)$.

Every subsequent module assumes you can read the math in §1–8.

## Related curriculum modules

- All later modules build on this one.
- [Module 4](curriculum-04-self-supervised-learning.md) — the "embedding before the last layer" idea generalizes.
- [Module 5](curriculum-05-generative-models.md) — uses U-Nets (CNN-based; Module 2) trained with the standard recipe in §8.

## Mentioned in

- [Robot-learning curriculum](robot-learning-curriculum.md)
- [Computing Neural Network Gradients (Kevin Clark, CS224n)](../../sources/clark-computing-nn-gradients.md) — vectorized-backprop reference for §3.
- [Index](../../index.md)

## Open questions / TBD

- ~~**Karpathy's neural-network-from-scratch lecture series** as a wiki source page~~ — **resolved 2026-07-09**: filed as [Neural Networks: Zero to Hero](../../sources/karpathy-nn-zero-to-hero.md); added to the recommended-reading list above.
- **A "common training pathologies" reference page** — vanishing gradients, exploding gradients, dead ReLU, loss-not-decreasing failure modes — would help readers debug their own experiments.

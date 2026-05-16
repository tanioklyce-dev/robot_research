---
title: Curriculum Module 2 — CNNs and visual representation learning
type: synthesis
created: 2026-05-10
updated: 2026-05-10
tags: [curriculum, module-2, cnn, convolution, pooling, resnet, imagenet, fine-tuning, visual-encoder]
prereqs: [curriculum-01]
status: draft
---

> [!note] Curriculum context
> This is **Module 2** of the [Robot-learning curriculum](robot-learning-curriculum.md). Tier 1. Prerequisite: [Module 1](curriculum-01-neural-networks.md) (NN basics; you need to be comfortable with forward pass, backprop, ReLU, BN, residuals, AdamW).
>
> CNNs are *de-facto* prerequisite for two things downstream: (1) the [ResNet](../../glossary.md#resnet) visual encoder that every BC-line policy uses ([Diffusion Policy](../../entities/diffusion-policy.md), [Robot Utility Models](../../entities/robot-utility-models.md)); (2) the U-Net architecture used by every [DDPM](curriculum-05-generative-models.md)-line model. ViT (Module 3) is the alternative, but CNNs are still the right default for many control-grade tasks.
>
> Acronyms used here are also in the [Glossary](../../glossary.md). First-mention links go there.

## Prereq diagnostic

Can you answer these without notes?

1. Write the formula for a 2D convolution: given input `X ∈ ℝ^{H×W×C}` and kernel `K ∈ ℝ^{k×k×C×C'}`, what's the output shape and how is each output computed?
2. Why does a 7×7 receptive field after 3 stacked 3×3 convolutions but with fewer parameters than a single 7×7 conv?
3. Why do CNNs use weight sharing (the same kernel applied at every spatial location)?
4. What's the difference between max pooling and average pooling? When does each win?
5. What's a "visual encoder" and why is ResNet-18 the canonical one for BC-line policies?

If yes to all five, skim and do the anchor exercise. If no to any, read the relevant section.

## What this module is

The CNN family — from the convolution operation to ResNet-18 as the BC-line default. By the end you should be able to:

1. Implement a 2D convolution in NumPy from scratch (you won't, but you could).
2. Read any CNN architecture's "Conv → BN → ReLU → MaxPool" block and predict the output shape and parameter count.
3. Explain why ResNet's skip connections matter for deep CNNs specifically.
4. Recognize the ImageNet-pretrain → fine-tune workflow and explain its data-economy logic.
5. Pick CNN vs ViT (Module 3) for a new task based on dataset size and input structure.

## §1 — The convolution operation

The key inductive bias of CNNs: **spatial locality + weight sharing.**

### 2D convolution (the mathematical definition)

Given input `X ∈ ℝ^{H × W × C_in}` (an image with `H × W` spatial extent and `C_in` channels) and a kernel `K ∈ ℝ^{k × k × C_in × C_out}`, the convolution produces output `Y ∈ ℝ^{H' × W' × C_out}` where each entry is:

```
Y[i, j, c'] = Σ_{u=0..k-1} Σ_{v=0..k-1} Σ_{c=0..C_in-1}  K[u, v, c, c'] · X[i+u, j+v, c]   +   b[c']
```

The kernel is a small (typically 3×3 or 5×5) tensor that **slides** across the input, computing dot products with the local patch at each position. The output channel dimension `C_out` represents *different feature detectors* — each output channel has its own kernel, and they all see the same input patch.

### Why this is a good inductive bias

Three properties:

1. **Locality** — each output entry depends only on a local patch of input. Reflects that visual features (edges, textures, parts) are local.
2. **Translation equivariance** — moving the input shifts the output the same way. Reflects that visual structure doesn't depend on absolute position.
3. **Weight sharing** — the same kernel is applied at every position. Massively reduces parameter count (a 3×3 conv with 64 output channels has 3·3·64·C_in parameters, regardless of image size).

These priors are why CNNs train well on small image datasets and why they generalize across image sizes.

### Stride and padding

Two knobs that affect output shape:

- **Stride `s`** — step size of the kernel. `s = 1` produces output `H' = H` (with padding); `s = 2` halves spatial extent.
- **Padding `p`** — zero-pad the input edges by `p` pixels. Used to control output size; "same padding" makes `H' = H` with `s = 1`.

Output shape formula: `H' = ⌊(H + 2p − k) / s⌋ + 1`.

## §2 — Pooling

A downsampling operation that reduces spatial extent without (much) loss of information.

### Max pooling

For each `k × k` non-overlapping region, take the maximum:

```
Y[i, j, c] = max_{u, v ∈ [0, k)}  X[s·i + u, s·j + v, c]
```

Typical: `k = s = 2` (halves spatial extent).

### Average pooling

Same, but with average instead of max:

```
Y[i, j, c] = (1/k²) · Σ_{u, v ∈ [0, k)}  X[s·i + u, s·j + v, c]
```

**When to use which.** Max pooling is more aggressive — it picks the strongest activation in each region and discards others. Good for object-detection-flavored tasks where you care about "is the feature present anywhere?" Average pooling preserves softer information; good when summing many weak signals matters.

**Global average pooling (GAP)** is a common trick at the end of CNNs: average across the entire `H' × W'` spatial dimension to produce a single vector per channel. Replaces fully-connected layers as the final feature extractor. ResNet uses GAP.

### Strided convolution as an alternative to pooling

Many modern CNNs use stride-2 convolutions instead of pooling. The math is the same (downsample by 2×), but the kernel is *learned* rather than fixed (max/avg). Empirically marginal; both are fine.

## §3 — Feature maps and receptive fields

### Feature maps

Each output channel of a conv layer is a **feature map** — a 2D array where each entry indicates how strongly that feature was detected at the corresponding spatial location. Early layers' feature maps respond to low-level patterns (edges, corners, textures); deeper layers respond to compositional patterns (parts, objects, scenes).

You can literally visualize feature maps as images — they're heat maps showing where the network "sees" each feature.

### Receptive field

The set of input pixels that influence a single output entry. For a single 3×3 conv, the receptive field is 3×3. For two stacked 3×3 convs, it's 5×5 (each output depends on a 3×3 patch of the intermediate layer, each of which depends on a 3×3 patch of the input). For three stacked 3×3 convs, it's 7×7.

**Why this matters:** to "see" a feature spanning `n` pixels, the network needs a receptive field ≥ `n`. Deeper networks see larger features. Pooling and strided convs expand the receptive field faster (each stride-2 layer multiplies it).

**The 3×3 trick:** three stacked 3×3 convs have the same receptive field as one 7×7 conv (7×7) but use **fewer parameters** (3 · 3·3·C·C vs 7·7·C·C) and have **more nonlinearities** (3 ReLUs vs 1). This is why modern CNNs almost exclusively use 3×3 kernels.

## §4 — ResNet and skip connections

[ResNet](../../glossary.md#resnet) (He et al. 2015) — the architectural insight that enabled CNNs deeper than ~30 layers.

### The residual block

```
input: x
F(x) = Conv → BN → ReLU → Conv → BN
output: y = ReLU(x + F(x))
```

The key element is the **skip connection** that adds the input `x` directly to `F(x)`. We covered this in [Module 1 §6](curriculum-01-neural-networks.md): residual connections enable gradient flow through deep networks by providing an identity path.

Before ResNet, the deepest practical CNN was VGG-19. After ResNet, networks of 100+ layers became standard. The 2015 ImageNet winner used 152 layers.

### Bottleneck residual blocks (deeper ResNets)

For ResNet-50, -101, -152, each residual block uses a 1×1 → 3×3 → 1×1 sandwich:

```
F(x) = Conv1×1 (C → C/4) → BN → ReLU
       → Conv3×3 (C/4 → C/4) → BN → ReLU
       → Conv1×1 (C/4 → C) → BN
```

The 1×1 convs reduce-then-expand the channel dimension, making the 3×3 conv (the expensive part) work on a thinner tensor. Same expressiveness, ~10× fewer FLOPs.

### ResNet variants

| Variant | Layers | Params | ImageNet top-1 |
| --- | --- | --- | --- |
| ResNet-18 | 18 | 11M | ~70% |
| ResNet-34 | 34 | 22M | ~73% |
| ResNet-50 | 50 | 25M | ~76% |
| ResNet-101 | 101 | 45M | ~77% |
| ResNet-152 | 152 | 60M | ~78% |

**ResNet-18 is the BC-line default visual encoder.** Small enough to train alongside a policy; expressive enough to capture useful spatial features. [Diffusion Policy](../../sources/diffusion-policy-paper.md), [Robot Utility Models](../../sources/robot-utility-models-paper.md), and most BC-line robotics work uses ResNet-18 as the per-frame encoder.

## §5 — ImageNet pretraining and fine-tuning

The single most important workflow in computer vision.

### The workflow

1. **Pretrain on ImageNet** (1.3M labeled images, 1000 classes). The model learns general-purpose visual features (edges, textures, objects).
2. **Replace the final classification head** with a new head for the downstream task (e.g., 1000-way → 10-way for CIFAR; or a regression head for a robotic task).
3. **Fine-tune** on the downstream dataset — usually with a smaller learning rate than pretraining.

The result: a model that performs much better on the downstream task than one trained from scratch on the (typically much smaller) downstream dataset.

### Why this works

ImageNet contains enough visual diversity that the pretrained features are *generally useful* — they detect edges, textures, parts, and object-flavored compositions that show up in any natural-image task. Fine-tuning lets the model adapt these general features to the specific task.

### Practical pretraining options in 2024–2026

- **ImageNet-1k (supervised)** — the classical default. Available in `torchvision.models.resnet18(weights="DEFAULT")`.
- **ImageNet-21k (supervised, ~14M images, 21k classes)** — better features but rarely needed.
- **[DINOv2](../../entities/dinov2.md) (self-supervised)** — pretrained on ~124M images. Strong general-purpose features without classification labels. The standard for "frozen-feature" robotics work; the encoder behind [DINO-WM](../../entities/dino-wm.md).
- **CLIP** — pretrained on image-caption pairs; aligns visual features with text embeddings. Useful for vision-language tasks.

### What "frozen" vs "fine-tune" buys you

- **Frozen encoder + trained head:** fastest. Only the head trains. Uses pretrained features as-is. Works when the downstream task is similar to ImageNet.
- **Fine-tune the whole network:** slowest, most expressive. Adapts all parameters. Works when you have enough data to avoid overfitting.
- **Fine-tune the last few layers + train head:** a middle ground. Common in practice.

[DINO-WM](../../entities/dino-wm.md) (Module 11) takes the frozen route — DINOv2 features are good enough that the predictor on top can be trained alone. [LeWM](../../entities/leworldmodel.md) takes the end-to-end route — a small ViT trained from scratch on the specific task.

## §6 — The "visual encoder" abstraction

By 2024–2026 the term **visual encoder** is shorthand for: "a CNN or ViT pretrained on large image data, used as a feature extractor for downstream tasks."

For BC-line robotics:
- ResNet-18 (end-to-end trained or fine-tuned) — Diffusion Policy default.
- ResNet-18 with [R3M](../../glossary.md#r3m) pretraining — a manipulation-specific pretrained version; appears as a Diffusion Policy ablation.
- DINOv2 (frozen) — DINO-WM, JEPA-WMs, occasionally as a Diffusion Policy ablation.

For JEPA-line robotics:
- Custom ViT-tiny (LeWM) — small, end-to-end.
- V-JEPA-pretrained ViT (V-JEPA 2-AC) — large, frozen.
- DINOv2 (frozen) — DINO-WM, JEPA-WMs.

For VLAs:
- ViT or VLM-pretrained ViT — depends on the VLA family ([Module 9](curriculum-09-vla.md)).

The unifying frame: a visual encoder maps `image → feature_vector`. Whether the encoder is CNN or ViT, frozen or trained, the downstream models all consume features rather than raw pixels.

## §7 — When CNN vs ViT?

[Module 3](curriculum-03-attention-and-transformers.md) covers ViT in detail. For now, the practical heuristic:

- **CNN wins when:** small datasets (CNN's inductive bias regularizes); modest compute budget; "classical" image classification or detection tasks; legacy pipelines.
- **ViT wins when:** large datasets (so the lack of CNN inductive bias doesn't hurt); features need to interact globally (attention sees everything); pretraining is available at scale (DINOv2, CLIP).

For 2024–2026 robotics: **both work**. ResNet-18 is the BC default; ViT (DINOv2 or custom) is the JEPA-line default. The two are interchangeable for many tasks.

## §8 — Other CNN architectures worth knowing

Briefly, for vocabulary:

- **VGG** — pre-ResNet baseline (16–19 layers, all 3×3 convs). Mostly historical.
- **GoogLeNet / Inception** — pre-ResNet with "inception modules" (parallel branches with different kernel sizes). Mostly historical.
- **DenseNet** — connects each layer to all subsequent layers (instead of just the next one). Memory-heavy; rarely used.
- **EfficientNet** — Tan & Le 2019; scales depth + width + resolution jointly. Stronger than ResNet at matched compute.
- **U-Net** — Ronneberger et al. 2015; encoder-decoder CNN with skip connections at each resolution level. **The architecture of [DDPM](curriculum-05-generative-models.md)** (the denoising network is a U-Net). Originally for biomedical image segmentation.
- **ConvNeXt** — Liu et al. 2022; modernized ResNet that matches ViT performance on ImageNet. The "CNNs are not dead" rebuttal to ViT enthusiasm.

You'll see U-Net referenced repeatedly in this curriculum because it's DDPM's denoising network. Don't conflate U-Net with ResNet; they're different shapes (U-Net has a contracting + expanding path with skip connections at each level; ResNet is a single flow).

## Anchor exercise

> **Load a ResNet-18, extract features for a batch of PushT frames, visualize the feature similarity structure.**

Concrete:

1. **Get the data.** Clone the [diffusion_policy](https://github.com/columbia-ai-robotics/diffusion_policy) repo or use the `stable-worldmodel` PushT dataset from [LeWM howto](../world-models/leworldmodel-howto.md). Extract ~500 frames at 96×96 resolution.
2. **Load ResNet-18 pretrained on ImageNet.** `torchvision.models.resnet18(weights="DEFAULT")`. Remove the final classifier (`model.fc = nn.Identity()`).
3. **Extract features.** Pass each frame through the network; get the 512-dim global-average-pooled feature vector.
4. **Visualize.** Run t-SNE on the 500 features. Color points by some PushT property (e.g., T-block angle, or end-effector position). **Do the colors form spatial structure in the t-SNE plot?**
5. **Compare to random.** Run t-SNE on randomly-initialized ResNet-18 features. The structure should be much weaker.

The point: feel that **pretrained ImageNet features are already useful for PushT** — even though the pretraining didn't see PushT, the visual primitives transfer. This is why ResNet-18 + Diffusion Policy works without any robotics-specific pretraining.

Deeper variant: try the same with a frozen DINOv2 ViT-S/14. The features are different (more semantic, less texture). Compare the t-SNE plots side by side. This previews [Module 11](curriculum-11-jepa-deep.md)'s "frozen-feature" vs "end-to-end" axis.

## Recommended reading

In order:

1. **3Blue1Brown's Convolutional Networks** (YouTube, free) — visual intuitions for convolution.
2. **Karpathy's [CS231n notes on CNNs](https://cs231n.github.io/convolutional-networks/)** — the canonical online reference. Read sections 1–4.
3. **He et al. 2015 — ResNet paper** (arxiv 1512.03385) — the original residual-connections paper. Sections 1–3.
4. **PyTorch's [torchvision models](https://pytorch.org/vision/stable/models.html)** — the API for loading pretrained models.
5. **Ronneberger et al. 2015 — U-Net paper** (arxiv 1505.04597) — for the DDPM denoising network architecture. Brief, ~5 pages.

## What you should now be able to do

- Read any CNN's "Conv → BN → ReLU → MaxPool" stack and predict output shapes, parameter counts, FLOPs.
- Pick ResNet-18 vs ResNet-50 based on dataset size and compute budget.
- Recognize the ImageNet-pretrain → fine-tune workflow in any paper and reason about which layers should be frozen vs trained.
- Distinguish CNN, ResNet, U-Net, ViT (preview) by architectural shape.
- Sketch why three stacked 3×3 convs are better than one 7×7 conv at matched receptive field.

## Hand-off

Module 2 is foundational for:

- **[Module 3](curriculum-03-attention-and-transformers.md) — Sequence models and attention** — ViT generalizes CNN's "local features" into "tokenized patches"; the comparison is sharper after you've internalized CNN.
- **[Module 5](curriculum-05-generative-models.md) — Generative models** — DDPM's denoising network is a U-Net (CNN family).
- **[Module 7](curriculum-07-bc-lineage-pusht.md) — BC lineage** — the ResNet-18 visual encoder is the BC default.
- **[Module 11](curriculum-11-jepa-deep.md) — JEPA depth** — DINO-WM and JEPA-WMs use frozen DINOv2 (ViT) as encoder; ResNet variants appear in ablations.

## Related curriculum modules

- **[Module 1](curriculum-01-neural-networks.md)** — prerequisite (forward pass, BN, residuals).
- **[Module 3](curriculum-03-attention-and-transformers.md)** — sibling (ViT is CNN's challenger).
- **[Module 5](curriculum-05-generative-models.md)** — DDPM uses U-Net.
- **[Module 7](curriculum-07-bc-lineage-pusht.md)** — ResNet-18 as the BC encoder.
- **[Module 11](curriculum-11-jepa-deep.md)** — frozen-encoder vs end-to-end-encoder axis.

## Mentioned in

- [Robot-learning curriculum](robot-learning-curriculum.md)
- [Index](../../index.md)

## Open questions / TBD

- **R3M source page** (Nair et al. 2022) — referenced as a manipulation-pretrained ResNet-18; appears in Diffusion Policy ablations. Not yet a wiki source page.
- **U-Net source page** (Ronneberger et al. 2015) — referenced as the DDPM denoising network architecture. Not yet a wiki source page; lower priority since DDPM specifics are covered in Module 5.
- **ConvNeXt source page** (Liu et al. 2022) — the modernized ResNet. Only worth filing if it shows up in more curriculum-relevant sources.

---
title: Inductive bias
type: concept
created: 2026-08-30
updated: 2026-08-30
sources: 7
tags: [inductive-bias, generalization, scaling, architecture, priors, ssl, vit, cnn, robot-data-scale]
---

**Inductive bias is the set of assumptions a learner uses to generalize beyond its training data.** Tom Mitchell's 1980 formulation is the crisp one: the assumptions that, *combined with the training data*, deductively entail the learner's predictions on inputs it has never seen.

The consequence that matters: infinitely many functions fit any finite dataset, and something has to choose among them. That something is the bias. **A learner with no inductive bias cannot generalize at all — it can only memorize.** The question is never *whether*, only *which* and *how much*.

> [!note] What the no-free-lunch theorem does and does not say
> Averaged over **all possible** target functions, no learner outperforms any other. The correct reading is not "all methods are equal in practice" — it is that **any real advantage a learner has comes entirely from its assumptions matching the problems actually faced.** Performance is a claim about fit between bias and world, not a property of the architecture alone. This is why "which bias" is the only interesting version of the question.

## Where it actually lives

"Inductive bias" is usually said to mean architecture. It enters in at least five places, and the ones people don't choose deliberately are often decisive:

| Locus | Example | The claim being made about the world |
| --- | --- | --- |
| **Architecture** | CNN: locality, translation equivariance, weight sharing | "features are local; identity is position-invariant" |
| **Objective** | MSE vs cross-entropy; contrastive losses | "noise is Gaussian"; "these pairs mean the same thing" |
| **Regularization** | weight decay, early stopping, dropout | "prefer smooth, small-norm functions" |
| **Optimization** | SGD's implicit bias toward flat / min-norm solutions | rarely chosen, frequently decisive |
| **Representation** | tokenization, action discretization, augmentation | "these two inputs are the same thing" |

The bottom row is the cheapest to change and the most often overlooked. **An augmentation set is an invariance claim**, not a data-multiplier — choosing random crops asserts that scale and position do not carry task information, which is true for ImageNet classification and false for a manipulation policy that has to know where the handle is.

**A bias pays off exactly to the extent its claim is true.** Translation equivariance works for natural images because objects genuinely look the same when shifted. It is actively harmful when absolute position carries the signal.

## The scale trade-off

Bias substitutes for data. With little data a *correct* bias is worth enormous amounts of it; with enough data the model can **learn** the structure you would have hardcoded, and the hardcoded version turns from a floor into a ceiling.

Three measurements in this wiki, at different levels of directness:

**[ViT (Dosovitskiy et al. 2020)](../../sources/vit-paper.md) — the architectural version.** On ImageNet alone (~1.3M images) ViT *underperforms* comparable ResNets, precisely because it lacks the CNN's locality and translation-equivariance priors. At ImageNet-21k (14M) the gap closes. At JFT-300M (303M) ViT overtakes — **and the ResNets plateau while ViT keeps improving**. Their hybrid experiment is the same finding in miniature: CNN-stem hybrids beat pure ViT at small compute budgets and the advantage vanishes at large ones. Also note §B: training ViT from scratch on ImageNet needs unusually strong explicit regularization (weight decay 0.3, dropout, label smoothing, gradient clipping) — *because the architecture has no built-in regularization from inductive bias*. **The bias does not disappear; it moves from the architecture to the regularizer.**

**[TDV (You Don't Need Strong Assumptions)](../../sources/tdv-paper.md) — the closest thing to a direct measurement.** Sweeping masking ratio as a proxy for assumption strength across ImageNet-1k subsets: at **0.1% of ImageNet the best masking ratio is 50%**, with 30% and 10% behind "by a significant margin"; as data grows, **30% overtakes 50% and 10% approaches it**. The offered mechanism is the useful part — strong assumptions "encode beliefs that are only approximately correct," and **at scale the approximation error dominates the guidance benefit.** That is a testable statement of *why* the curve bends, not just that it does.

**[Karpathy](../../sources/karpathy-software-3-and-transformer-history-lecture.md) — the practitioner's summary.** *"If you have infinite data you actually want to encode less and less… if you have very little data then you do want to encode some biases, and maybe convolutions are a good idea because you have this bias coming from the filters."*

> [!warning] "Less inductive bias" almost never means "no inductive bias"
> A ViT is not unbiased. It carries a **strong** bias toward permutation-invariant processing of a set with all-pairs interaction — which is exactly why positional encoding has to be bolted back on, and why [Karpathy describes attention](../../sources/karpathy-software-3-and-transformer-history-lecture.md) as freeing computation "from this version of Euclidean space… in attention, everything is just sets."
>
> [TDV](../../sources/tdv-paper.md) makes the same caveat unavoidable: its own Table 1 shows that **naively removing DINO's inductive biases collapses the representation**, so the method keeps an EMA teacher, a stop-gradient, and a DINO self-distillation loss. What it removes is augmentation, masking and cropping. "Learning without strong inductive biases" means *without the image-level ones*, not without machinery.
>
> Read every "we remove the inductive bias" claim as **"we relocate it"** until shown otherwise.

## When a bias fails, and how you find out

Two failure modes worth separating, because they look different in the loss curve.

**The bias is wrong for the task, and you can see it.** Standard overfitting-in-reverse: the model is fighting its own prior. Usually diagnosable by ablation.

**The bias is satisfiable by something useless, and the loss looks fine.** This is the dangerous one. [Sobal et al. 2022](../../sources/sobal2022-jepa-slow-features-paper.md) is the cleanest demonstration in this wiki: the **slow-features** bias — prefer representations that change slowly over time — is satisfied perfectly by an encoder that outputs a per-episode constant. All three VICReg terms reach zero at that trivial solution, and InfoNCE's alignment-and-uniformity optimum is also satisfied. **The slowest feature wins, even when it isn't the useful feature.** Nothing in the objective pushes back, so the training curve reports success.

This generalizes: **[representation collapse](../world-models/jepa.md) is what an under-constrained inductive bias looks like from the inside.** The whole anti-collapse design space the wiki tracks — [VICReg](../../sources/vicreg-paper.md), [Barlow Twins](../../sources/barlow-twins-paper.md), [SIGReg](../../sources/lejepa-paper.md), EMA teachers, DINO self-distillation — exists to add *just enough* additional bias to exclude the degenerate solutions without excluding the good ones.

There is also an impossibility result worth knowing: **Locatello et al. 2019** (ICML best paper, un-ingested) shows unsupervised **disentanglement is impossible without inductive biases** — flagged on the [β-VAE page](../../sources/beta-vae-paper.md) so the wiki does not over-credit β-VAE's claims. Not "hard": impossible, on the theory. The bias is not an aid to the objective; in that case it *is* the objective.

## The instructive example: manufacturing a space where bias is available

[Bengio et al. 2003](../../sources/bengio2003-neural-probabilistic-language-model.md) is an inductive-bias argument end to end, and it is the most useful one in this wiki because the bias is not architectural.

One-hot symbols supply **no usable bias**: under Hamming distance `cat` and `dog` are exactly as far apart as `cat` and `the`, so nothing learned about one transfers to the other. Smoothness — the workhorse assumption for continuous inputs — is simply unavailable over a discrete alphabet. Their move was to **manufacture a continuous space** ([the embedding table](distributed-representations.md)) in which smoothness becomes both available and *correct*, so that "each training sentence informs the model about an exponential number of semantically neighboring sentences."

They did not add data. They added a bias that made the existing data go further. **That is the shape of a good inductive bias: not "constrain the model" but "give the model a space in which the right generalization is cheap."**

## Why this cuts the other way in robotics

The strongest claim on this page, and the one most worth arguing with.

**The "discard your priors" conclusion was earned at a data scale robotics does not have.** Language went from 14M words ([Bengio et al. 2003](../../sources/bengio2003-neural-probabilistic-language-model.md)) to 100B ([word2vec](../../sources/mikolov2013-efficient-estimation-word-representations.md)) to internet-scale. Vision's bias-discarding result required [JFT-300M](../../sources/vit-paper.md) — and *lost* at 1.3M images. Robot manipulation corpora are at **350 hours ([DROID](../../entities/droid.md))** to **20,854 ([EgoScale](../../sources/egoscale-paper.md))**.

Reasoning from ViT or GPT to "don't build in structure" on a few thousand demonstrations applies the conclusion without its premise. On the [TDV](../../sources/tdv-paper.md) curve, robot learning sits near the **left** end — where the stronger assumption wins by a significant margin.

Practical consequences at that scale:

- **Keep the structure you actually know.** Known kinematics, explicit 3D geometry, action chunking, force/contact priors. These are not shortcuts pending more data; they are correct claims about the world that data would otherwise have to rediscover.
- **A pretrained backbone is renting someone else's data scale.** A frozen [DINOv2/v3](../../entities/dinov3.md) encoder moves the bias question off the encoder and onto the head — you are inheriting a low-bias representation trained at a scale you cannot reach, and the design decisions that remain are downstream of it.
- **Spend the bias budget on representation, not architecture.** Action space, observation framing and augmentation choice are cheaper to change and usually more load-bearing than swapping ResNet for ViT — which the wiki's own [Module 2 verdict](../../syntheses/curriculum/curriculum-02-cnns.md) already implies when it says the two backbones are "interchangeable for many tasks" in 2024–2026 robotics.
- **Withhold the bias the surrounding system already supplies.** [Cho et al. 2014](../../sources/cho2014-rnn-encoder-decoder-phrase-representations.md) deliberately discarded phrase-pair frequencies when training, because the phrase table already encoded them, so the learned component's capacity went to what the system lacked. The same logic applies to any hybrid learned/classical robot stack.

## Related concepts

- [Distributed representations](distributed-representations.md) — the 2003 example above; manufacturing a space where smoothness applies.
- [JEPA](../world-models/jepa.md) and [latent space](../world-models/latent-space.md) — representation collapse as the signature of an under-constrained bias.
- [Spectral theory of SSL](spectral-theory-of-ssl.md) — the theory side of what SSL objectives actually prefer.
- [Sim-to-real transfer](sim-to-real-transfer.md) — domain randomization is an inductive-bias choice: it asserts which variations are task-irrelevant.
- [Scaling laws for VLAs](scaling-laws-vla.md) — the robot-side data-scale question this page's last section depends on.

## Key references

- **[ViT (Dosovitskiy et al. 2020)](../../sources/vit-paper.md)** — "large-scale training trumps inductive bias," measured across three dataset scales plus the hybrid ablation.
- **[TDV — You Don't Need Strong Assumptions](../../sources/tdv-paper.md)** — the optimal *strength* of a bias decreasing as data grows, swept directly.
- **[Sobal et al. 2022 — JEPA and slow features](../../sources/sobal2022-jepa-slow-features-paper.md)** — a bias with a specific, silent failure mode.
- **[Bengio et al. 2003](../../sources/bengio2003-neural-probabilistic-language-model.md)** — the discrete/continuous asymmetry, and manufacturing a space where smoothness is usable.
- **[Karpathy lecture](../../sources/karpathy-software-3-and-transformer-history-lecture.md)** — the data-scale heuristic, and attention as freeing computation from Euclidean structure.
- **[β-VAE](../../sources/beta-vae-paper.md)** — via the Locatello et al. 2019 impossibility result flagged there.
- **[Curriculum Module 2](../../syntheses/curriculum/curriculum-02-cnns.md)** — the CNN's three biases (locality, translation equivariance, weight sharing) and the CNN-vs-ViT decision heuristic.

## Current state

Settled as vocabulary, unsettled as practice. Nobody disputes the shape of the curve — more data, less benefit from strong priors — and there is no accepted way to *measure* how much bias a given design carries, which is why [TDV](../../sources/tdv-paper.md) has to use masking ratio as a proxy. "Strength of inductive bias" is treated as a scalar in the scaling arguments and is obviously not one.

For this wiki's subject matter the operative question is not the language-and-vision one. It is **whether robot learning is on the flat part of the curve or the steep part**, and the honest answer is that nobody has run the [TDV](../../sources/tdv-paper.md) sweep on robot data. Every architecture choice in the [VLA](vla-models.md) literature implicitly answers it, and none of them measure it.

## Mentioned in

- [ViT Paper (Dosovitskiy et al. 2020)](../../sources/vit-paper.md)
- [TDV Paper](../../sources/tdv-paper.md)
- [Sobal et al. 2022 — JEPA and slow features](../../sources/sobal2022-jepa-slow-features-paper.md)
- [Bengio et al. 2003 — A Neural Probabilistic Language Model](../../sources/bengio2003-neural-probabilistic-language-model.md)
- [β-VAE Paper](../../sources/beta-vae-paper.md)
- [Karpathy — Software 3.0 and the history of the Transformer](../../sources/karpathy-software-3-and-transformer-history-lecture.md)
- [Sensorimotor world models paper](../../sources/sensorimotor-world-models-paper.md) — the single-step inverse objective used as an inductive bias without its theoretical guarantees.
- [Curriculum Module 2 — CNNs](../../syntheses/curriculum/curriculum-02-cnns.md) and [Module 3](../../syntheses/curriculum/curriculum-03-attention-and-transformers.md) (syntheses, not sources)
- [From n-grams to attention](../../syntheses/sequence-models/language-model-to-transformer-lineage.md) (synthesis)

## Open questions / TBD

- **Nobody has swept assumption strength on robot data.** The [TDV](../../sources/tdv-paper.md) experiment — vary one bias, sweep dataset size, plot the crossover — is directly runnable on [DROID](../../entities/droid.md) or [LIBERO](../../entities/libero.md) and would settle the argument in this page's last section instead of leaving it as a reasoned assertion. **The most valuable un-run experiment this page implies.**
- **Locatello et al. 2019** is un-ingested and is the field's main impossibility result on this topic.
- **"Strength of inductive bias" has no measure.** Masking ratio is a proxy for one bias in one method. There is no way to compare "how much bias" a CNN carries against a ViT-plus-augmentations, which makes cross-architecture versions of the scaling claim informal.
- **The implicit bias of the optimizer** — SGD's preference for flat / min-norm solutions — is a real and well-studied locus that this wiki has no source for, and it is the one practitioners choose least deliberately.

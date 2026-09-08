---
title: "Critique of World Model (Xing, Deng & Hou, 2025–26)"
type: source
url: https://arxiv.org/abs/2507.05169
local_path: raw/critique-of-world-model_2507.05169.pdf
sha256: 8d08a38b914b4ecad93380b349edf247a899a6ecb7ca939e35f72b578ce923e3
author: Eric Xing, Mingkai Deng, Jinyu Hou
published: 2025-07-07
ingested: 2026-09-07
venue: "arXiv essay; read at v5 (2026-06-17, dated June 1 2026). v1 July 2025. Later versions carry the subtitle 'A Generative Latent Prediction Architecture for World Modeling'"
format: paper (34 pp, position/essay; three propositions/theorems with proofs, no experiments)
tags: [world-model, jepa, glp, generative-latent-prediction, pan, critique, position-paper, collapse, latent-loss, generative-loss, discrete-tokens, stateful, mpc-vs-rl, llm-backbone, mbzuai, cmu, xing]
---

# Critique of World Model

**[Eric Xing](../entities/eric-xing.md)**, Mingkai Deng, Jinyu Hou — [MBZUAI](../entities/mbzuai.md) Institute of Foundation Models + CMU. The paper the [Nicolas Substack post](../syntheses/world-models/generative-video-vs-jepa-world-models.md) cites for the claim that *"the AI community remains divided"* between JEPA's no-decoder stance and a **Generative Latent Prediction** camp. It is the origin of the term GLP, and **the clearest published counter-position to the LeCun programme this wiki has**. It is also a position paper: three short proofs, a design blueprint, a motivating story, and **zero experiments** — the results are deferred to the separate [PAN](../entities/pan-world-model.md) paper (arXiv 2511.09057, un-ingested).

## Summary

The essay's definition: a world model is *"a generative model that simulates the possibilities in diverse scenarios"* — physical, mental, social, counterfactual — whose primary goal is **simulating all actionable possibilities of the real world for purposeful reasoning and acting**. From that definition it argues that a WM is *not* a video generator (the Genie / Cosmos / Sora line optimises visual quality for its own sake) and *not* an open-loop latent predictor either. It reads [LeCun's 2022 blueprint](lecun2022-path-towards-ami.md) as five "common wisdoms" and argues against each, then proposes **GLP**: an encoder–decoder generative bottleneck grounding predictions in observations, wrapped around a hierarchical *latent reasoning backbone* made of an enhanced LLM (discrete concepts) plus a diffusion-based next-embedding predictor (continuous perception). **PAN** is the named instantiation; a mountaineering expedition is the motivating use case.

## The five "common wisdoms" and the five replies

The paper attributes these to the JEPA line ([LeCun 2022](lecun2022-path-towards-ami.md), [V-JEPA 2](v-jepa-2-paper.md), [DINO-WM](dino-wm-paper.md), PLDM) and answers each in turn (§4.1–4.5).

| # | Common wisdom (as stated by the paper) | The paper's reply |
|---|---|---|
| 1 | **Sensory data over text** — a 4-year-old has seen ~1.1×10¹⁴ bytes of vision vs ~0.9×10¹⁴ bytes of all LLM text | **Information density, not volume.** Video is redundant; language is *"an evolved compression of human experiences"* and the only channel for justice, regret, motivation, collective memory. Use **all modalities**, stratified by level. |
| 2 | **Continuous state vectors**, for gradient-based optimisation | **Statefulness is mandatory.** A fixed-size embedding of a raw sensory stream is *stateless* — it moves with noise and viewpoint, not with the world. Discrete vocabulary tokens are *"identifiable, persistent, memory-anchored."* **Theorem 1**: discrete codes can preserve arbitrarily fine distinctions between real inputs; scaling *out* (longer sequences, O(TD log TD)) is far cheaper than scaling *up* the vocabulary (O((TD)ᴰ)). Advocates **mixed** discrete + continuous. |
| 3 | **Encoder–encoder, no decoder**, to avoid compounding autoregressive error | **JEPA is functionally autoregressive anyway**: recursive `ŝ′ = f(ŝ,a)` is a degenerate Dirac-delta transition, so it inherits the same error-accumulation issues while giving up the decoder's diagnostic. A lossy, non-invertible encoder *cannot* yield a stateful representation; if it discards something the dynamics need, *"no amount of predictor sophistication can recover what was thrown away."* The decoder is *"a diagnostic tool that continuously pressures the representation to retain all dynamically relevant information."* |
| 4 | **Latent-space loss** rather than reconstruction, to avoid modelling irrelevant detail | **Proposition 1**: the bare latent loss has a trivial global minimum (constant encoder, identity transition). **Proposition 2**: the generative loss has no such degenerate optimum, given a fixed expressive decoder and two distinct next-observations in the data. **Theorem 2**: under isotropic-Gaussian assumptions and a round-trip error ε, **`L_latent ≤ L_gen + ε`** — the latent loss is an *upper-bounded surrogate*, so minimising it does not guarantee observation-consistency and *"can miss semantically important mistakes that the latter will penalize."* |
| 5 | **MPC** over RL, for sample efficiency and safety | MPC re-simulates at every step (expensive at decision time), plans only **10–20 steps** with **hundreds to thousands** of samples and simple proposal distributions, and *"has shown promise primarily in simplified settings."* Prefer **RL from world-model-simulated experience** (Ha & Schmidhuber's paradigm), which moves cost to training and learns long-horizon value. The PAN-agent sketch adds a **cache of precomputed simulations** consulted at decision time. |

## Key claims

- **Definition and taxonomy (§2–3).** Belief state `ŝ_t = h(o_t)`, WM `p_f(ŝ_{t+1} | ŝ_t, a′_t)`, simulation-based decision rule (Eq. 6). Survey of five families: gaming WMs (Genie 2/3, Muse, Oasis, LingBot-World), 3-D scene WMs ([World Labs](../entities/world-labs.md) Marble, WorldGen — *"closer to a digital twin than a learned world model"* because dynamics live in an exported physics engine), physical WMs ([Cosmos](../entities/nvidia-cosmos.md) / [Cosmos 3](cosmos-3-technical-report.md), GAIA-2, 1XWM, Runway GWM-1), video generators (Sora, Veo, Seedance — *"fall outside the definition of world models"*), and JEPA (*"conceptually elegant … evidence for practical usability remains scarce"*). Cites [Fei-Fei Li](../entities/fei-fei-li.md)'s [functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md) X post and a **LeCun–Xing debate** (Spring School AI for Impact, Ben Guerir, Morocco, 2026-03-25) as recent convergence on *simulator, not renderer*.
- **Semantic vs generative representations (§4.3.2).** CLIP/DINO-class encoders capture invariances and discard the rest; VAE/MAE/diffusion-class encoders keep enough to reconstruct. *"Generative representations subsume semantic ones"*; *"information discarded by a semantic encoder cannot be recovered, but information preserved by a generative encoder can always be further abstracted."* The sharp version: what a semantic encoder deems important is set by its training distribution, so **rare, high-stakes events (car crashes) are exactly what gets abstracted away.**
- **The efficiency argument is closing (§4.3.2).** FastVideo (trainable sparse attention) generates 30 s of 1080p in ~3 s; Causal Swin-DPM damps long-horizon error with chunk-wise causal attention. *"The marginal efficiency gain of dropping the decoder does not justify the fundamental information loss."*
- **GLP architecture (§4.3.3, Fig. 5).** Encoder h + decoder g form a generative bottleneck; a hierarchical backbone f: latent-diffusion next-embedding predictors at the bottom (pixels, audio, proprioception), a next-token predictor over VQ-VAE-style modality tokens in the middle, an LLM in *"thought space"* at the top — the upper two implemented as one enhanced LLM. *"Our argument is not that world models must operate in pixel space, but that they should learn from it."*
- **PAN (§5).** Sensory encoder = tokenizer (hierarchical vocabulary, extensible at train and inference time) + embedder; backbone = enhanced LLM + diffusion embedding predictor with a **Learned Switch** choosing per step; multimodal decoder reconstructs *"sound, temperature, motion, pain, and/or even text."* Factorised as `p(o′|o,a) = Σ p_h(ŝ|o) p_f(ŝ′|ŝ,a) p_g(o′|ŝ′)`. Training: pretrain modules separately (LLM on text, diffusion on video), then align with multimodal data; discrete components may need RL-style gradient-free updates. Data-efficiency claim: navigation needs no pixel-level snow; foot placement needs no geography — *"travel book for trail guide, indoor video for rock climbing."* **Details and results deferred to arXiv 2511.09057.**
- **Companion in preparation:** *Critiques of Agents* (Xing, Deng, Hou, 2026), on how acting on simulations belongs to a separate agent model.

## The wiki's read

> [!warning] Contradiction — two theorems point in opposite directions, and neither settles it
> Theorem 2 here says the latent loss is bounded *above* by the generative loss, so it can under-penalise. [Joint-Embedding vs Reconstruction (Van Assel et al.)](joint-embedding-vs-reconstruction-paper.md) proves the opposite ordering *on what matters*: when the nuisance noise is high-dimensional, reconstruction is *forced* to spend capacity on it and latent prediction is provably better for the downstream target. Both proofs are correct in their own model. The disagreement is about **which residual is "a semantically important mistake" and which is noise** — and Theorem 2 is agnostic on that, because under its isotropic-Gaussian assumption every pixel is weighted equally. The [abstraction-tax](../syntheses/world-models/abstraction-tax.md) page holds the wiki's working answer: it depends on whether the axis of shift was declared at training time.

- **Proposition 1 is aimed at a target nobody defends.** That the bare latent loss collapses is the founding fact of the entire [anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md); the live question is whether the fix is principled or heuristic. The essay's actual claim is the parenthetical — regularisers are *"hard to tune and difficult to understand"* — which is exactly what [LeJEPA / SIGReg](lejepa-paper.md) contests with a one-hyperparameter, isotropic-Gaussian-optimality argument. The essay does not engage it.
- **Proposition 2 proves less than it is used for.** It shows the *constant-encoder* solution is not a global optimum of the generative loss with a fixed expressive decoder. It does not rule out the decoder ignoring the latent and modelling `o′` on its own — **posterior collapse**, the [VAE](../concepts/learning/variational-autoencoder.md) literature's standard failure, is precisely a generative loss with a collapsed latent. The wiki's [JEPA page](../concepts/world-models/jepa.md) already records Balestriero's version of the same point (*reconstruction cannot collapse*) — with the caveat that it cannot collapse *the reconstruction*, which is a different thing from a useful state.
- **Two arguments the wiki should absorb, because they match its own findings.** (i) *Rare events get abstracted away* — this is the [OOD-collapse result](../syntheses/world-models/generative-video-vs-jepa-world-models.md#a-third-jepa-failure-mode-measured-may-2026-out-of-distribution-collapse) (50.8% → 6–26% under colour/size/shape shift) stated as a mechanism. (ii) *JEPA is functionally autoregressive and deterministic* — the same observation the [WorldDP close read](worlddp-paper.md#reading-notes) made about a "diffusion" transformer trained by MSE. The essay's framing is stronger than either wiki page: it is not a quirk of one model, it is the architecture.
- **"Stateful" is the [belief-state](../concepts/world-models/belief-states-and-mixed-states.md) argument in different clothes.** The wiki reached the same requirement from Blackwell 1957 and the POMDP derivation. What is new here is the claim that *discrete tokens* are the natural carrier — and Theorem 1 is an existence proof for a quantisation code, which says nothing about whether such a code is *learnable* or stable. The wiki has no evidence either way.
- **The MPC characterisation is accurate and the alternative is Dreamer.** 10–20 steps, hundreds of samples, first-action execution, replan — that is the [LeWM](leworldmodel-paper.md) recipe verbatim, and the [WorldDP](worlddp-paper.md) horizon is 2–3. "RL in imagination" is the Dreamer line the wiki's [world-model page](../concepts/world-models/world-model.md) already carries; the PAN-agent's simulation cache is a sketch with no result behind it.
- **Evidentiary weight.** Zero experiments, results deferred, one YouTube debate cited as a primary. File as a *position*, on the same footing as [LeCun 2022](lecun2022-path-towards-ami.md) — which is a fair pairing, since it is written as that paper's rebuttal.

## Entities mentioned

- [Eric Xing](../entities/eric-xing.md) — first author; MBZUAI president, CMU.
- [MBZUAI](../entities/mbzuai.md) — Institute of Foundation Models; the paper's home.
- [PAN world model](../entities/pan-world-model.md) — the GLP instantiation previewed here.
- [Yann LeCun](../entities/yann-lecun.md) — the position being rebutted; debated Xing on JEPA vs GLP, March 2026.
- [Fei-Fei Li](../entities/fei-fei-li.md) — cited for the functional taxonomy; [World Labs](../entities/world-labs.md) Marble is filed as *"closer to a digital twin."*
- [NVIDIA Cosmos](../entities/nvidia-cosmos.md), [Genie 3](../entities/genie-3.md), [V-JEPA 2](../entities/v-jepa-2.md), [DINO-WM](../entities/dino-wm.md) — the surveyed systems.

## Concepts touched

- [Generative Latent Prediction](../concepts/world-models/generative-latent-prediction.md) — the concept page this source creates.
- [World model](../concepts/world-models/world-model.md) — the definition fight; a fifth position for the "three eras" table.
- [JEPA](../concepts/world-models/jepa.md) — the architecture under critique.
- [Belief states](../concepts/world-models/belief-states-and-mixed-states.md) — "stateful" = sufficient statistic carried forward.
- [Identifiability](../concepts/world-models/identifiability.md) — the essay's *"any latent representation of real-world signal intrinsically suffers from issues of identifiability and stability."*
- [World-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md) — cited; the essay's *simulator not renderer* is the same cut.
- [Variational autoencoder](../concepts/learning/variational-autoencoder.md) — the posterior-collapse counter to Proposition 2.

## Open questions

- Does PAN (arXiv 2511.09057) report anything that tests Theorem 2's practical claim — a case where a latent-trained WM misses a decision-relevant error that a generative one catches?
- Is a *learned* discrete state (VQ-VAE tokens) actually more stable under nuisance variation than a regularised continuous one? Theorem 1 is existence-only.
- The essay says JEPA has been shown *"mainly in toy environments."* [V-JEPA 2-AC](v-jepa-2-paper.md)'s real-Franka results and [HWM](../entities/hwm.md)'s 0→70% are the counter-evidence; the essay cites V-JEPA 2 and waves at it. What is the generative-side equivalent at matched compute? The [head-to-head section](../syntheses/world-models/generative-video-vs-jepa-world-models.md#the-first-head-to-head-measurements-mid-2026) is the wiki's best current answer.
- The LeCun–Xing debate (2026-03-25) is a primary for both positions stated live. Not ingested.

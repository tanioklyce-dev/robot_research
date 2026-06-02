---
title: Generative-video vs JEPA world models — what they predict, what it costs, what works
type: synthesis
created: 2026-05-07
updated: 2026-06-02
tags: [world-models, jepa, generative-video, cosmos, cosmos-3, world-action-model, genie-envisioner, dreamdojo, v-jepa-2, leworldmodel]
---

# Generative-video vs JEPA world models

The simulator survey ([Simulators for agentic robotics — 2026 landscape](../simulators/simulators-for-agentic-robotics-2026.md) §3) split [world-model simulators](../../concepts/world-models/world-model-simulators.md) into two paradigms but did not work through the comparison in detail. This page does. The two paradigms are not just "different ways to learn dynamics" — they make different bets about *what* a robot needs from a world model, with consequences that show up in compute, training data scale, planning latency, and demonstrated real-robot transfer.

## What each paradigm predicts

| | Generative-video | JEPA / latent-prediction |
|---|---|---|
| Output | Next-frame **pixels** | Next-state **embedding** (no pixels) |
| Loss computed in | Pixel space | Representation space |
| Decoder required? | Yes | No |
| Canonical instances | [NVIDIA Cosmos](../../entities/nvidia-cosmos.md) / **[Cosmos 3](../../sources/cosmos-3-technical-report.md)** (the omnimodal [WAM](../../concepts/world-models/world-action-model.md)), [Genie Envisioner](../../entities/genie-envisioner.md) / GE-Sim2, **[DreamDojo](../../sources/dreamdojo-paper.md)** | [V-JEPA 2](../../entities/v-jepa-2.md) / V-JEPA 2-AC, [LeWorldModel](../../entities/leworldmodel.md) |
| Lead labs | NVIDIA, [AGIBOT](../../entities/agibot.md) | [Meta FAIR](../../entities/meta-fair.md), [Mila](../../entities/mila.md), NYU (the LeCun program) |

The asymmetry runs deep: a video generator has to commit to a specific RGB rendering of every imagined future; a JEPA only has to commit to an embedding. Most of the cost difference between the two paradigms traces to that single design choice.

## Cost and speed

| Axis | Generative-video | JEPA |
|---|---|---|
| Training cost | Massive (per-frame generation + decoder) | Lower (no decoder, no pixel loss) |
| Inference cost | Heavy video diffusion / autoregressive generation | Light forward pass through an encoder + small predictor |
| Planning cost | High — every imagined rollout is a video | Low — rollouts happen in latent space |
| Concrete number | DreamDojo teacher: 35 denoising steps @ **2.72 FPS**; distilled student: 4 steps @ **10.81 FPS** ([DreamDojo Paper](../../sources/dreamdojo-paper.md)) | [LeWorldModel](../../entities/leworldmodel.md) reports **up to 48× faster planning** than foundation-model-based world models ([LeWorldModel Paper](../../sources/leworldmodel-paper.md)) |
| Smallest known instance | Cosmos-Predict2-2B-Video2World (2B params) underpins [GE-Sim2](../../entities/genie-envisioner.md) ([AGIBOT Genie Envisioner 2.0 Announcement](../../sources/agibot-genie-envisioner-2-announcement.md)) | LeWorldModel: **15M params, single GPU, hours of training** ([LeWorldModel Paper](../../sources/leworldmodel-paper.md)) |
| Largest known instance | **DreamDojo-14B** — 14B params trained 140k steps on **256 NVIDIA H100 GPUs**, pretrained on **44,711 hr** of human video ([DreamDojo Paper](../../sources/dreamdojo-paper.md)) | V-JEPA 2: **1B-param ViT-g encoder + 300M-param action-conditioned predictor** ([V-JEPA 2 Paper](../../sources/v-jepa-2-paper.md)) |

The 48× planning-speed gap matters for closed-loop control. A model-predictive controller running at 10–30 Hz needs to imagine many candidate rollouts per cycle; a paradigm that's an order of magnitude faster doesn't just save compute, it expands the space of planners that are runnable on a real robot.

## What each does with data

| | Generative-video | JEPA |
|---|---|---|
| Pretraining data | Web video + simulated rollouts; **DreamDojo: 44,711 hr egocentric human video** (DreamDojo-HV — the largest WM-pretraining corpus to date) | Web video (V-JEPA 2: **1M+ hours, 22M videos**) |
| Action data needed | Action-conditioned variants need labeled action data — *unless* you use **continuous latent actions** (DreamDojo) as self-supervised proxy labels; small target-robot post-training stage to adapt to the real action space. | Same — V-JEPA 2-AC post-trained on **62 hr of Droid robot data** |
| Why this is the JEPA-shaped opportunity | — | **Pretraining is action-free**; action conditioning is added in a small post-training stage, dramatically reducing the need for expensive teleop data |

V-JEPA 2's two-stage recipe — 1M+ hours of action-free internet video, then 62 hours of Droid robot data — is the clearest existence proof on the JEPA side that **massive observation pretraining can substitute for massive interaction data**.

> [!note] DreamDojo closes part of this gap on the generative-video side
> Until Feb 2026 the generative-video paradigm lacked an action-free → action-conditioned recipe at JEPA-comparable scale. **[DreamDojo](../../sources/dreamdojo-paper.md)** delivers exactly that: 44,711 hr of human-video pretraining using *continuous latent actions* as self-supervised proxy labels (VAE with information bottleneck on consecutive frame pairs), then post-training on small target-robot data to adapt to the real action space. Crucially, Table 2 of the paper shows latent-action conditioning **matches** ideal ground-truth-action conditioning despite needing no mocap or retargeting — the latent-action recipe is the generative-video counterpart to V-JEPA-2-AC's action-free-then-action-conditioned staging.

## Demonstrated real-robot results

> [!note] V-JEPA 2-AC's zero-shot Franka result is the most concrete cross-paradigm validation available
> [V-JEPA 2 Paper](../../sources/v-jepa-2-paper.md) reports **zero-shot deployment on Franka arms in two new labs** for image-goal pick-and-place via MPC, with **no robot-specific data, no task-specific training, no rewards** — the model came in pretrained on internet video plus 62 hr of Droid, and worked on hardware it had never seen. This is the strongest published evidence that latent-prediction world models can produce real-robot capability with minimal robot data.

> [!note] Cosmos 3 partially closes the generative-video real-robot gap — as a *policy*, not zero-shot transfer
> Until June 2026 the generative-video side had no strong *real-robot policy* result. **[Cosmos 3](../../sources/cosmos-3-technical-report.md)**'s Cosmos3-Nano-Policy-DROID (a generative, joint video+action diffusion policy — a [world-action model](../../concepts/world-models/world-action-model.md)) **tops the RoboArena real-world leaderboard** and beats π0.5 on RoboLab-120. This is a genuine generative-video-family real-robot win — but note it's a *policy that imagines its own consequence*, post-trained on DROID, **not** the V-JEPA-2-AC-style "trained-inside-the-model, deployed-zero-shot-on-novel-hardware via MPC" result. The cleanest cross-paradigm test (MPC planning inside a pixel world model → novel hardware) is still open on the generative-video side.

| | Generative-video | JEPA |
|---|---|---|
| Real-robot zero-shot evidence | Genie Envisioner / GE-Sim2 supports minute-scale stable rollouts inside the simulator. **DreamDojo** demonstrates policy *evaluation* (closed-loop rollouts of a real GR00T N1.5 policy on AgiBot fruit-packing) but **not** policy-trained-inside → real-robot zero-shot transfer ([DreamDojo Paper](../../sources/dreamdojo-paper.md) §4.7). The JEPA-style "trained-inside-model, deployed-on-novel-hardware" result is still open on the generative-video side. | V-JEPA 2-AC: pick-and-place on Franka in two new labs ([V-JEPA 2 Paper](../../sources/v-jepa-2-paper.md)) |
| Task-fidelity claim | Long-horizon, minute-scale stable rollouts ([AGIBOT Genie Envisioner 2.0 Announcement](../../sources/agibot-genie-envisioner-2-announcement.md)); DreamDojo human-preference: **72.5% physics correctness** wins for DreamDojo-14B vs Cosmos-Predict2.5 baseline ([DreamDojo Paper](../../sources/dreamdojo-paper.md)) | Latent-space planning over short horizons; LeWM probes show encoded physical structure ([LeWorldModel Paper](../../sources/leworldmodel-paper.md)) |
| Interpretability | Visual rollouts are human-inspectable; failure modes (hallucination, drift) are visible | Latent space is opaque; LeWM's "surprise evaluation" is the closest the sources come to interpretability tooling |

The interpretability axis is genuinely a generative-video advantage: a roboticist can watch a Cosmos rollout and see what the model thinks will happen. A JEPA predicts a vector — debugging requires probing tooling that doesn't exist as a default workflow yet.

## Failure modes

| Generative-video | JEPA |
|---|---|
| **Hallucination** — generated frames depict events that violate physics | **Representation collapse** — encoder + predictor settle on trivial constants without the right inductive biases |
| **Drift over long rollouts** — error accumulates frame-by-frame | **Predictor overfitting** on small interaction sets |
| **Compute wall** — long rollouts get expensive fast | **Latent-only debugging** — failures are harder to inspect than a bad video frame |

JEPAs have spent the last few years adding fixes for collapse: EMA target encoders, stop-gradient, frozen pre-trained encoders, multi-term losses ([Joint-Embedding Predictive Architecture](../../concepts/world-models/jepa.md)). LeWorldModel's contribution is collapsing this whole battery into a single SIGReg regularizer — projecting embeddings onto random directions and enforcing Gaussianity — bringing tunable loss hyperparameters from 6 (PLDM) down to 1 ([LeWorldModel Paper](../../sources/leworldmodel-paper.md)).

## When to use which (current best read)

- **You need to *evaluate* high-level agent behavior with human-inspectable rollouts** → generative-video. GE-Sim2's minute-scale stable rollouts are designed for exactly this.
- **You need cheap, fast latent-space planning for closed-loop MPC** → JEPA. The 48× planning-speed advantage is real and consequential.
- **You have massive action-free observation data and small interaction data** → JEPA's two-stage recipe (V-JEPA 2 → V-JEPA 2-AC) is the canonical pattern.
- **You want generated video as a *training-data source* to feed a downstream policy or [VLA](../../concepts/learning/vla-models.md)** → generative-video. This is what [Cosmos](../../entities/nvidia-cosmos.md) and [GE-Sim2](../../entities/genie-envisioner.md) are designed for.
- **You want to replace the physics engine for contact-rich training** → neither, yet. Both paradigms complement physics simulators today rather than replacing them. The simulator survey's section 3 statement still holds.

## Cross-paradigm interactions

The two paradigms are not independent. [GR00T](../../entities/nvidia-groot.md) N1.7 reportedly uses **Cosmos-Reason2-2B** as a backbone ([NVIDIA Cosmos](../../entities/nvidia-cosmos.md) entity page) — i.e., a generative-video world model is being repurposed as a perception backbone for a VLA. Meanwhile, V-JEPA 2's encoder produces representations aligned well enough with LLMs to score 84.0 on PerceptionTest ([V-JEPA 2 Paper](../../sources/v-jepa-2-paper.md)) — i.e., a JEPA encoder is becoming a candidate vision backbone for multimodal LLMs.

**Implication:** the long-run picture may not be "one paradigm wins"; it may be that generative-video models become training-data engines and authoring tools, while JEPA encoders become perception backbones for VLAs and on-robot world models for fast planning. Different jobs, complementary substrates.

## Open questions

- **No published head-to-head**: no source ingested compares Cosmos / GE-Sim2 / **DreamDojo** against V-JEPA 2 on the same robot task. The cleanest comparison the wiki has is *between V-JEPA 2 and LeWorldModel* — both JEPAs at very different scales — not across paradigms. DreamDojo would be the natural generative-video side of such a comparison given its scale and OOD-robustness publication.
- **Generative-video zero-shot transfer to real**: DreamDojo demonstrates policy *evaluation* but not "policy trained inside DreamDojo, deployed zero-shot on real hardware." That's the V-JEPA-2-AC-style result that would close the cross-paradigm-validation gap. GE-Sim2 doesn't have it either.
- **Scaling laws on each side**:
  - JEPA side: V-JEPA 2 (1B params, 1M+ hours) and LeWM (15M params, single GPU) span 60–70× model size and ~5 orders of magnitude data — what does the curve between them look like? No published JEPA scaling law.
  - Generative-video side: DreamDojo's Table 3 shows monotone OOD improvement with data scale (In-lab → +EgoDex → +DreamDojo-HV → 14B) but does **not** fit a closed-form scaling law like EgoScale's `L = a − b·ln(D)`. A clean WM-side scaling law is still missing.
- **Action-conditioned generative video at 62-hr scale**: V-JEPA 2-AC's 62-hr post-train number is the JEPA-side existence proof. DreamDojo's post-training data scale is also small but not explicitly framed as "minimal." A controlled 62-hr-equivalent comparison would be the cleanest paradigm test.
- **Compute parity**: DreamDojo-14B on 256 H100s vs V-JEPA 2's published compute budget — these are comparable in FLOPs. Per-task performance comparison at fixed compute is the open question for fair paradigm comparison.

## Sources used in this synthesis

- [V-JEPA 2 Paper](../../sources/v-jepa-2-paper.md)
- [LeWorldModel Paper](../../sources/leworldmodel-paper.md)
- [Genie Envisioner Paper](../../sources/genie-envisioner-paper.md)
- [AGIBOT Genie Envisioner 2.0 Announcement](../../sources/agibot-genie-envisioner-2-announcement.md)
- [Top 10 Physical AI Models 2026](../../sources/top-10-physical-ai-models-2026.md) (background on Cosmos / GR00T)
- [DreamDojo Paper](../../sources/dreamdojo-paper.md) (the 2026 generative-video high-water mark)
- [Cosmos 3 Technical Report](../../sources/cosmos-3-technical-report.md) (the omnimodal world-action-model — generative-video side's strongest real-robot policy)

## Related

- [World-model simulators](../../concepts/world-models/world-model-simulators.md) — the umbrella concept page.
- [Joint-Embedding Predictive Architecture](../../concepts/world-models/jepa.md) — paradigm B's architectural definition.
- [Simulators for agentic robotics — 2026 landscape](../simulators/simulators-for-agentic-robotics-2026.md) — §3 sketches this comparison at survey level; this page is the deep dive.
- [VLA models](../../concepts/learning/vla-models.md) — the policies that consume world-model environments or use world-model encoders as backbones.

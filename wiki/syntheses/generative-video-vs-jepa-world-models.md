---
title: Generative-video vs JEPA world models — what they predict, what it costs, what works
type: synthesis
created: 2026-05-07
updated: 2026-05-07
tags: [world-models, jepa, generative-video, cosmos, genie-envisioner, v-jepa-2, leworldmodel]
---

# Generative-video vs JEPA world models

The simulator survey ([[simulators-for-agentic-robotics-2026|Simulators for agentic robotics — 2026 landscape]] §3) split [[world-model-simulators|world-model simulators]] into two paradigms but did not work through the comparison in detail. This page does. The two paradigms are not just "different ways to learn dynamics" — they make different bets about *what* a robot needs from a world model, with consequences that show up in compute, training data scale, planning latency, and demonstrated real-robot transfer.

## What each paradigm predicts

| | Generative-video | JEPA / latent-prediction |
|---|---|---|
| Output | Next-frame **pixels** | Next-state **embedding** (no pixels) |
| Loss computed in | Pixel space | Representation space |
| Decoder required? | Yes | No |
| Canonical instances | [[nvidia-cosmos|NVIDIA Cosmos]], [[genie-envisioner|Genie Envisioner]] / GE-Sim2 | [[v-jepa-2|V-JEPA 2]] / V-JEPA 2-AC, [[leworldmodel|LeWorldModel]] |
| Lead labs | NVIDIA, [[agibot|AGIBOT]] | [[meta-fair|Meta FAIR]], [[mila|Mila]], NYU (the LeCun program) |

The asymmetry runs deep: a video generator has to commit to a specific RGB rendering of every imagined future; a JEPA only has to commit to an embedding. Most of the cost difference between the two paradigms traces to that single design choice.

## Cost and speed

| Axis | Generative-video | JEPA |
|---|---|---|
| Training cost | Massive (per-frame generation + decoder) | Lower (no decoder, no pixel loss) |
| Inference cost | Heavy video diffusion / autoregressive generation | Light forward pass through an encoder + small predictor |
| Planning cost | High — every imagined rollout is a video | Low — rollouts happen in latent space |
| Concrete number | (no comparable benchmark surfaced in sources) | [[leworldmodel|LeWorldModel]] reports **up to 48× faster planning** than foundation-model-based world models ([[leworldmodel-paper|LeWorldModel Paper]]) |
| Smallest known instance | Cosmos-Predict2-2B-Video2World (2B params) underpins [[genie-envisioner|GE-Sim2]] ([[agibot-genie-envisioner-2-announcement|AGIBOT Genie Envisioner 2.0 Announcement]]) | LeWorldModel: **15M params, single GPU, hours of training** ([[leworldmodel-paper|LeWorldModel Paper]]) |
| Largest known instance | Cosmos series (parameter counts not surfaced in sources) | V-JEPA 2: **1B-param ViT-g encoder + 300M-param action-conditioned predictor** ([[v-jepa-2-paper|V-JEPA 2 Paper]]) |

The 48× planning-speed gap matters for closed-loop control. A model-predictive controller running at 10–30 Hz needs to imagine many candidate rollouts per cycle; a paradigm that's an order of magnitude faster doesn't just save compute, it expands the space of planners that are runnable on a real robot.

## What each does with data

| | Generative-video | JEPA |
|---|---|---|
| Pretraining data | Web video + simulated rollouts | Web video (V-JEPA 2: **1M+ hours, 22M videos**) |
| Action data needed | Action-conditioned variants need labeled action data | Same — V-JEPA 2-AC post-trained on **62 hr of Droid robot data** |
| Why this is the JEPA-shaped opportunity | — | **Pretraining is action-free**; action conditioning is added in a small post-training stage, dramatically reducing the need for expensive teleop data |

V-JEPA 2's two-stage recipe — 1M+ hours of action-free internet video, then 62 hours of Droid robot data — is the clearest existence proof in either paradigm that **massive observation pretraining can substitute for massive interaction data**. Generative-video models can in principle do the same staging, but no source ingested here demonstrates an action-free → action-conditioned pipeline at comparable scale.

## Demonstrated real-robot results

> [!note] V-JEPA 2-AC's zero-shot Franka result is the most concrete cross-paradigm validation available
> [[v-jepa-2-paper|V-JEPA 2 Paper]] reports **zero-shot deployment on Franka arms in two new labs** for image-goal pick-and-place via MPC, with **no robot-specific data, no task-specific training, no rewards** — the model came in pretrained on internet video plus 62 hr of Droid, and worked on hardware it had never seen. This is the strongest published evidence that latent-prediction world models can produce real-robot capability with minimal robot data.

| | Generative-video | JEPA |
|---|---|---|
| Real-robot zero-shot evidence | Genie Envisioner / GE-Sim2 supports minute-scale stable rollouts inside the simulator; whether policies trained inside it transfer zero-shot to new hardware is not established in the sources here | V-JEPA 2-AC: pick-and-place on Franka in two new labs ([[v-jepa-2-paper|V-JEPA 2 Paper]]) |
| Task-fidelity claim | Long-horizon, minute-scale stable rollouts ([[agibot-genie-envisioner-2-announcement|AGIBOT Genie Envisioner 2.0 Announcement]]) | Latent-space planning over short horizons; LeWM probes show encoded physical structure ([[leworldmodel-paper|LeWorldModel Paper]]) |
| Interpretability | Visual rollouts are human-inspectable; failure modes (hallucination, drift) are visible | Latent space is opaque; LeWM's "surprise evaluation" is the closest the sources come to interpretability tooling |

The interpretability axis is genuinely a generative-video advantage: a roboticist can watch a Cosmos rollout and see what the model thinks will happen. A JEPA predicts a vector — debugging requires probing tooling that doesn't exist as a default workflow yet.

## Failure modes

| Generative-video | JEPA |
|---|---|
| **Hallucination** — generated frames depict events that violate physics | **Representation collapse** — encoder + predictor settle on trivial constants without the right inductive biases |
| **Drift over long rollouts** — error accumulates frame-by-frame | **Predictor overfitting** on small interaction sets |
| **Compute wall** — long rollouts get expensive fast | **Latent-only debugging** — failures are harder to inspect than a bad video frame |

JEPAs have spent the last few years adding fixes for collapse: EMA target encoders, stop-gradient, frozen pre-trained encoders, multi-term losses ([[jepa|Joint-Embedding Predictive Architecture]]). LeWorldModel's contribution is collapsing this whole battery into a single SIGReg regularizer — projecting embeddings onto random directions and enforcing Gaussianity — bringing tunable loss hyperparameters from 6 (PLDM) down to 1 ([[leworldmodel-paper|LeWorldModel Paper]]).

## When to use which (current best read)

- **You need to *evaluate* high-level agent behavior with human-inspectable rollouts** → generative-video. GE-Sim2's minute-scale stable rollouts are designed for exactly this.
- **You need cheap, fast latent-space planning for closed-loop MPC** → JEPA. The 48× planning-speed advantage is real and consequential.
- **You have massive action-free observation data and small interaction data** → JEPA's two-stage recipe (V-JEPA 2 → V-JEPA 2-AC) is the canonical pattern.
- **You want generated video as a *training-data source* to feed a downstream policy or [[vla-models|VLA]]** → generative-video. This is what [[nvidia-cosmos|Cosmos]] and [[genie-envisioner|GE-Sim2]] are designed for.
- **You want to replace the physics engine for contact-rich training** → neither, yet. Both paradigms complement physics simulators today rather than replacing them. The simulator survey's section 3 statement still holds.

## Cross-paradigm interactions

The two paradigms are not independent. [[nvidia-groot|GR00T]] N1.7 reportedly uses **Cosmos-Reason2-2B** as a backbone ([[nvidia-cosmos|NVIDIA Cosmos]] entity page) — i.e., a generative-video world model is being repurposed as a perception backbone for a VLA. Meanwhile, V-JEPA 2's encoder produces representations aligned well enough with LLMs to score 84.0 on PerceptionTest ([[v-jepa-2-paper|V-JEPA 2 Paper]]) — i.e., a JEPA encoder is becoming a candidate vision backbone for multimodal LLMs.

**Implication:** the long-run picture may not be "one paradigm wins"; it may be that generative-video models become training-data engines and authoring tools, while JEPA encoders become perception backbones for VLAs and on-robot world models for fast planning. Different jobs, complementary substrates.

## Open questions

- **No published head-to-head**: no source ingested compares Cosmos/GE-Sim2 against V-JEPA 2 on the same robot task. The cleanest comparison the wiki has is *between V-JEPA 2 and LeWorldModel* — both JEPAs at very different scales — not across paradigms.
- **GE-Sim2 zero-shot transfer**: is there published evidence that policies trained inside Genie Envisioner transfer to real hardware they haven't seen? The announcement claims "physical evolution engine" but the wiki has no zero-shot transfer result on the generative-video side comparable to V-JEPA 2-AC's Franka demonstration.
- **Scaling laws for JEPA**: V-JEPA 2 (1B params, 1M+ hours) and LeWM (15M params, single GPU) span 60–70× model size and ~5 orders of magnitude data, both succeed. What does the curve between them look like?
- **Action-conditioned generative video at 62 hr scale**: can a Cosmos-class model be post-trained with as little robot data as V-JEPA 2-AC and still get zero-shot transfer? Untested in the sources here.

## Sources used in this synthesis

- [[v-jepa-2-paper|V-JEPA 2 Paper]]
- [[leworldmodel-paper|LeWorldModel Paper]]
- [[genie-envisioner-paper|Genie Envisioner Paper]]
- [[agibot-genie-envisioner-2-announcement|AGIBOT Genie Envisioner 2.0 Announcement]]
- [[top-10-physical-ai-models-2026|Top 10 Physical AI Models 2026]] (background on Cosmos / GR00T)

## Related

- [[world-model-simulators|World-model simulators]] — the umbrella concept page.
- [[jepa|Joint-Embedding Predictive Architecture]] — paradigm B's architectural definition.
- [[simulators-for-agentic-robotics-2026|Simulators for agentic robotics — 2026 landscape]] — §3 sketches this comparison at survey level; this page is the deep dive.
- [[vla-models|VLA models]] — the policies that consume world-model environments or use world-model encoders as backbones.

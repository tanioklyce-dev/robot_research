---
title: JEPA task capabilities
type: synthesis
created: 2026-05-08
updated: 2026-05-08
tags: [jepa, world-model, capabilities, manipulation, navigation, planning, video-understanding, taxonomy]
---

# JEPA task capabilities

What can a [[jepa|JEPA]]-style world model actually *do*? Pulling together evidence from the seven JEPA / JEPA-adjacent papers ingested in this wiki, the demonstrated capabilities sort into seven task categories. This page is a reference index — it answers "is there a JEPA paper that does X?" by pointing at the source.

> [!note] Wiki coverage caveat
> Seven papers in this wiki: [[v-jepa-2-paper|V-JEPA 2]], [[v-jepa-2-1-paper|V-JEPA 2.1]], [[leworldmodel-paper|LeWorldModel]], [[dino-wm-paper|DINO-WM]], [[dino-world-paper|DINO-world]], [[vla-jepa-paper|VLA-JEPA]], [[jepa-wms-paper|JEPA-WMs]]. The categories below are precise to ingested evidence, not a universal claim about the JEPA literature.

## 1. Real-robot manipulation (zero-shot or with minimal real data)

- **Pick-and-place via image-goal MPC** — V-JEPA 2-AC zero-shot on Franka arms in **two new labs** with no robot-specific data, training, or rewards ([[v-jepa-2-paper|V-JEPA 2 Paper]]). The strongest published evidence in either world-model paradigm that **massive observation pretraining can substitute for massive interaction data**.
- **Real-Franka grasping** — V-JEPA 2.1 reports +20pt improvement over V-JEPA 2-AC ([[v-jepa-2-1-paper|V-JEPA 2.1 Paper]], per agent secondary research; the abstract itself is generic).
- **Heavy-sim manipulation + real-Franka eval in the same paper** — JEPA-WMs trains/evaluates on RoboCasa kitchen manipulation + 42 Metaworld tasks + DROID + real Franka unroll decode ([[jepa-wms-paper|JEPA-WMs Paper]]).
- **JEPA-augmented VLA manipulation** — VLA-JEPA evaluates on LIBERO + LIBERO-Plus + SimplerEnv + real-world manipulation, using a JEPA objective as auxiliary representation learning *inside* a VLA policy ([[vla-jepa-paper|VLA-JEPA Paper]]).

## 2. Robot navigation

- **2D maze / point-mass / wall navigation** —
  - JEPA-WMs: PointMaze + Wall ([[jepa-wms-paper|JEPA-WMs Paper]])
  - LeWM: PushT + two-rooms + reacher ([[leworldmodel-paper|LeWorldModel Paper]])
  - DINO-WM: PushT, Wall, PointMaze, Rope, Granular, Reacher ([[dino-wm-paper|DINO-WM Paper]])
- **Real-robot navigation** — V-JEPA 2.1 reports robotic navigation results; platform not named in abstract ([[v-jepa-2-1-paper|V-JEPA 2.1 Paper]]).

## 3. Planning (world model as cost function)

JEPA models are most often used **not as policies** but as **cost functions for planners** — the planner optimizes action sequences against the learned latent dynamics:

- **Image-goal MPC** — V-JEPA 2-AC and V-JEPA 2.1 plan toward an observation-goal in latent space ([[v-jepa-2-paper|V-JEPA 2 Paper]]).
- **Action-sequence planning, end-to-end-trained** — LeWM uses planner against learned latent dynamics; reports up to **48× faster planning** than foundation-model-based world models ([[leworldmodel-paper|LeWorldModel Paper]]).
- **Zero-shot observational-goal planning** — DINO-WM optimizes action sequences against goal images without expert demos, reward modeling, or pre-learned inverse models ([[dino-wm-paper|DINO-WM Paper]]).
- **Physical-planning benchmark study** — JEPA-WMs's whole framing is *"what drives success in physical planning with JEPA-WMs"* ([[jepa-wms-paper|JEPA-WMs Paper]]); explicitly outperforms DINO-WM and V-JEPA 2-AC on the proposed setup.

## 4. Video understanding (encoder downstream)

The V-JEPA 2 encoder (1B-param ViT-g pretrained on 1M+ hr internet video) transfers to standard video benchmarks **without fine-tuning**:

- **Motion classification**: 77.3 top-1 on Something-Something v2.
- **Action anticipation**: 39.7 R@5 on Epic-Kitchens-100 — SOTA, beating prior task-specific models.
- **LLM-aligned VQA at 8B-parameter scale**: 84.0 PerceptionTest, 76.9 TempCompass.

All three from [[v-jepa-2-paper|V-JEPA 2 Paper]].

## 5. Dense vision tasks (V-JEPA 2.1)

V-JEPA 2.1's "dense features" framing extends the encoder to spatially structured outputs:

- **Depth estimation**, **segmentation forecasting**, evaluated on Ego4D, EPIC-KITCHENS, Something-Something v2, NYUv2, TartanDrive ([[v-jepa-2-1-paper|V-JEPA 2.1 Paper]]).

## 6. Video prediction

- **Segmentation forecasting + depth forecasting** as video-prediction benchmarks (DINO-world, [[dino-world-paper|DINO-world Paper]]).
- All JEPA models predict **next-frame representation** as their core training objective; this is the substrate that the other six categories sit on top of.

## 7. Probing / interpretability

- **Latent space encodes physical structure** — probing the LeWM latent space surfaces interpretable physical structure ([[leworldmodel-paper|LeWorldModel Paper]]).
- **Surprise / anomaly detection** — LeWM surprise scores reliably detect physically implausible events ([[leworldmodel-paper|LeWorldModel Paper]]). Useful for safety / out-of-distribution monitoring.

## Cross-cutting structural notes

- **JEPA models are typically used as cost functions, not as policies.** Except for VLA-JEPA's auxiliary use, JEPA work in this wiki does not provide a `policy.act(obs)` interface — actions come from a planner that *queries* the world model. This is a meaningful design contrast with VLA models that emit actions directly.
- **JEPA models do not generate pixels.** That's the [[generative-video-vs-jepa-world-models|generative-video paradigm]] ([[nvidia-cosmos|Cosmos]], [[genie-envisioner|Genie Envisioner]]). JEPA's whole bet is to predict in *representation* space — cheaper, but not human-inspectable in the way generative video is.
- **Sim weight class varies by paper** — see [[why-jepa-research-skips-the-simulator-stack|the JEPA-and-sim synthesis]]. Capabilities listed above are demonstrated across multiple sim weight classes (none / lightweight / mid / heavy), so the *task* and the *sim setup* are independent design axes.
- **Real-robot evaluation is the genre's gold standard.** V-JEPA 2 (zero-shot real Franka), V-JEPA 2.1 (real-Franka grasping), JEPA-WMs (real Franka), VLA-JEPA (real-world manip) all back their claims with real-robot results. This is rarer than it sounds — most simulator-bound robot-learning papers don't.

## Mapping: which model does which task

| Task | V-JEPA 2 | V-JEPA 2.1 | LeWM | DINO-WM | DINO-world | VLA-JEPA | JEPA-WMs |
|---|---|---|---|---|---|---|---|
| Real-robot manipulation | ✓ (Franka) | ✓ (Franka grasp) | — | — | — | ✓ (real manip) | ✓ (Franka) |
| Robot navigation | — | ✓ (real) | ✓ (2D) | ✓ (2D) | — | — | ✓ (PointMaze/Wall) |
| Planning (cost fn) | ✓ (image-goal MPC) | ✓ | ✓ (48× faster) | ✓ (zero-shot) | — | — | ✓ |
| Video understanding | ✓ (SSv2, EK-100, VQA) | ✓ | — | — | — | — | — |
| Dense vision | — | ✓ (depth, seg) | — | — | — | — | — |
| Video prediction | — | — | — | — | ✓ (seg + depth forecasting) | — | — |
| Probing / interpretability | — | — | ✓ (latent + surprise) | — | — | — | — |

## What JEPA models *don't yet* do (in this wiki)

- **Long-horizon manipulation tasks with subgoals** — most JEPA results are short-horizon (pick-and-place, single-step navigation). Long-horizon hierarchical planning with JEPA is not yet demonstrated in ingested sources.
- **Multi-robot / multi-agent control.**
- **Language-conditioned action emission directly** — VLA-JEPA bolts JEPA onto a VLA, but the VLA does the language-conditioning. No JEPA-native language-conditioned action policy in this wiki.
- **Open-world humanoid whole-body control** — that domain is occupied by [[nvidia-groot|GR00T]] and similar VLAs.

## Open questions / TBD

> [!note] Specific task-success rates often hedged
> V-JEPA 2's "enable picking and placing" framing is qualitative; precise success rates need the paper body ([[v-jepa-2-paper|open question]]). The +20pt V-JEPA 2.1 grasping number is secondary research, not abstract text.

- The DROID and Metaworld papers are not yet source pages; once ingested, they would let us cite training-data and benchmark-design rationale directly.
- LeWM's "scales to high-resolution real-robot deployment" question is still open per the LeWM paper itself.
- Long-horizon hierarchical JEPA planning — likely a future paper, not yet demonstrated.

## Sources used in this synthesis

- [[v-jepa-2-paper|V-JEPA 2 Paper]]
- [[v-jepa-2-1-paper|V-JEPA 2.1 Paper]]
- [[leworldmodel-paper|LeWorldModel Paper]]
- [[dino-wm-paper|DINO-WM Paper]]
- [[dino-world-paper|DINO-world Paper]]
- [[vla-jepa-paper|VLA-JEPA Paper]]
- [[jepa-wms-paper|JEPA-WMs Paper]]
- [[jepa|JEPA concept page]]

## Related

- [[jepa|Joint-Embedding Predictive Architecture]] — the architecture family.
- [[world-model|World model]] — broader concept.
- [[world-model-simulators|World-model simulators]] — narrower companion.
- [[why-jepa-research-skips-the-simulator-stack|Why JEPA research skips the simulator stack]] — companion synthesis on simulator choice across the same papers.
- [[generative-video-vs-jepa-world-models|Generative-video vs JEPA world models]] — paradigm contrast.

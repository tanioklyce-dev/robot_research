---
title: "Yann LeCun's $1B Bet Against LLMs [Part 2] (Welch Labs)"
type: source
url: https://www.youtube.com/watch?v=v_jDvpEGTIg
author: Stephen Welch (Welch Labs); co-creators Matthew Cohen, Sam Baskin, Pranav Gundu, Varun Reddy
affiliations: Welch Labs (YouTube)
published: 2026-05-30
ingested: 2026-05-31
duration: "40:57 (2,457 s)"
local_path: raw/2026-05-30-welchlabs-lecun-1b-bet-against-llms-part2.txt
format: video
tags: [video, jepa, world-model, v-jepa-2, vl-jepa, leworldmodel, hierarchical-jepa, vla-models, cem, lecun, ami-labs, welch-labs, popular-explainer]
---

## Summary

Part 2 of the Welch Labs JEPA series (sequel to ["Yann LeCun's $1B Bet Against LLMs"](welchlabs-lecun-1b-bet-against-llms.md)). Where Part 1 traced the path *to* [JEPA](../concepts/world-models/jepa.md) (blurry pixels → Siamese → collapse → Barlow Twins → DINO), Part 2 climbs the **"alternative stack"**: for each layer of a modern [VLA](../concepts/learning/vla-models.md) (vision encoder → VLM → full robot policy) there is a JEPA-based counterpart with different trade-offs. It walks **[V-JEPA 2](../entities/v-jepa-2.md)** (vision encoder), **[VL-JEPA](../entities/vl-jepa.md)** (a JEPA reframing of the whole VLM), and **[LeWorldModel](../entities/leworldmodel.md) + cross-entropy-method planning** and **hierarchical JEPA** (robot control), bracketed by new on-camera [LeCun](../entities/yann-lecun.md) interview clips. The recurring thesis, from the [AMI Labs](../entities/ami-labs.md) landing page: *"Real intelligence does not start in language. It starts in the world."* LeCun's verdict on VLAs is blunt: *"VLA are doomed."*

## Key claims

Chapter-by-chapter (timestamps from the official description):

- **0:00 — Intro.** Opens on [Physical Intelligence](../entities/physical-intelligence.md)'s **π0.7** ([π0.7](../entities/pi07.md)) peeling a zucchini / folding a pinwheel / taking out trash — the VLA "pinnacle" — vs JEPA taking **60 seconds to move a cup off a platform**. Sets up the question: are these impressive VLAs actually "doomed"?
- **2:30 — V-JEPA.** [V-JEPA 2](../entities/v-jepa-2.md): Meta, 2025, **1M hours of video, up to 1B params**. Trained by masking video patches and predicting the *embeddings* of missing patches (vs [CLIP](../concepts/world-models/jepa.md), which aligns image embeddings to caption embeddings). VJEPA is "blissfully unaware of language." Key result: **a video encoder pretrained without language supervision can be aligned to an LLM and hit SOTA on video understanding "contrary to conventional wisdom."** Example: a TempCompass question about a video played in reverse — **ChatGPT 5.5 gets it wrong both directions; only some Claude/Gemini versions get it right.**
- **8:18 — VL-JEPA.** Reframe the *entire* VLM as JEPA: instead of generating output text token-by-token, encode the target text and train a predictor to hit its **embedding**, conditioned on the image + prompt. Maps cleanly onto the standard VLM architecture (the predictor plays the LLM's role). Abstracting away phrasing of correct answers ("do not eat this mushroom" ≈ "this mushroom is not safe to eat") gives efficiency: **35% video-classification accuracy after 5M examples vs 20% for a matched standard VLM**; **1.6B-param VL-JEPA outperforms 7B-param models on the GQA compositional-reasoning benchmark.** Caveat: VL-JEPA is **not generative** — answers come via multiple-choice embedding-similarity or an optionally-trained text decoder.
- **14:05 — But what about VLA?** VLAs turn VLMs into robot brains; recent ones (π0.7) use a separate **action expert** rather than emitting control tokens directly from the LLM.
- **15:13 — KiwiCo** (sponsor). Includes LeCun's "a four-year-old has taken in more visual data than the largest LLM has seen in text" back-of-envelope.
- **17:14 — LeCun's critique of VLA.** Two prongs: **(1) behavioral cloning doesn't scale** — needs "tons and tons" of demos, only practical for low-variability tasks, "completely helpless" / brittle in slightly-new situations; **(2) no explicit planning** — VLAs are end-to-end (images+joints → next joints), "do not have world models," "cannot predict the consequences of their actions." LeCun: *"I do not understand how you can even think of building an agentic system without … the ability of predicting the consequences of its actions."* The video fairly counters with **RT-2's 2023 Taylor-Swift generalization** and π0.7's out-of-distribution tasks (air fryer, microwave Tupperware, paper-towel rolls) — generalization is "a sliding scale," and whether VLAs generalize *enough* is the open empirical question.
- **22:42 — LeWorldModel.** [LeWorldModel](../entities/leworldmodel.md) on **push-t**: learn an action-conditioned latent world model from human trajectories (like BC data, but learning *dynamics*, not *imitation*). A separate **decoder** maps predicted embeddings back to images — revealing a "learned cartoon sketch" of push-t physics (rigid, movable T; effector interaction). Planning uses the **cross-entropy method (CEM)**: sample ~500 random action trajectories, roll them out in the world model (in **groups of 5 actions**), score by **Euclidean distance in embedding space** between final predicted embedding and the goal-image embedding, keep an **elite set of 30**, resample, repeat. Planning happens **entirely in latent space**. This "cleanly addresses LeCun's critiques" — no human imitation, explicit planning — **but** performance is "dramatically behind VLA"; the model only reliably plans **~5 prediction loops** ahead before drifting "off the rails."
- **30:41 — Hierarchical JEPA.** LeCun's fix for long horizons: low levels make **detailed short-term** predictions; high levels make **abstract long-term** predictions (fewer details → less divergence). Inter-layer interface is an **embedding space, "not semantic, certainly not language"** ("your cat can do hierarchical planning"). LeCun's NYU→Paris analogy: you can't plan a trip in millisecond muscle control; you decompose into sub-goals (airport → taxi → street). **LeCun and collaborators recently applied a 2-layer hierarchical world model to push-t, extending the planning horizon from 5 to 15 steps**, with the higher level's predictions serving as **sub-goals** for the lower. Hope: the right architecture makes the hierarchy **emergent** (like CNN feature hierarchies) — but it "probably requires training on semi-expert trajectories," not random ones.
- **34:55 — My Take.** JEPA is early; VJEPA 2 + VL-JEPA show it's *not incompatible* with the mainstream language-driven stack, but on agentic/robotics it remains "quite limited." Analogy: LeCun's 1990s handwritten-digit nets also felt limited before scaling.
- **35:57 — The Future of JEPA.** LeCun's [AMI Labs](../entities/ami-labs.md) plan: within **1–2 years**, apply world-model planning to **industrial applications** — "complex systems whose behavior cannot be reduced to a small number of equations" (jet engine, airplane, chemical/power plant; a diabetes patient's blood sugar; coaxing a stem cell into a beta cell; materials/catalyst/battery design). Within **3–5 years**, the ambition is to become "the main supplier of intelligent systems." Explicitly *not* simple robot arms/humanoids/rockets — those "you can just write down the dynamical equations."
- **38:57 — JEPA Poster & Patreon.** Companion "Web of AI" poster summarizing VJEPA, VL-JEPA, LeWorldModel.

## Cited papers (from the description)

- **[V-JEPA 2](../entities/v-jepa-2.md)** — arXiv 2506.09985.
- **[VL-JEPA](../entities/vl-jepa.md)** — arXiv 2512.10942 (Chen, Shukor, Moutakanni, … LeCun, Fung).
- **[LeWorldModel](../entities/leworldmodel.md)** — arXiv 2603.19312; plus an "identifiability theory of LeWorldModel" (arXiv 2605.26379) — *neither hierarchical-JEPA push-t paper is explicitly named.*
- Balestriero's recommended reading: **LeJEPA** (arXiv 2511.08544, [ingested](lejepa-paper.md)), SSL↔spectral-embedding (2205.11508), and the why-JEPA-not-reconstruction pair (2402.11337, 2505.12477).
- Collaborator credited for JEPA discussion: **Randall Balestriero**.

## Entities mentioned
- [Yann LeCun](../entities/yann-lecun.md)
- [V-JEPA 2](../entities/v-jepa-2.md)
- [VL-JEPA](../entities/vl-jepa.md) (entity created with this ingest)
- [LeWorldModel](../entities/leworldmodel.md)
- [Physical Intelligence](../entities/physical-intelligence.md) / [π0.7](../entities/pi07.md)
- [AMI Labs](../entities/ami-labs.md)
- [Welch Labs](../entities/welch-labs.md) / [Stephen Welch](../entities/stephen-welch.md)

## Concepts touched
- [Joint-Embedding Predictive Architecture (JEPA)](../concepts/world-models/jepa.md) — incl. **hierarchical JEPA** and **CEM latent-space planning**
- [VLA models](../concepts/learning/vla-models.md) — the foil; LeCun's two-pronged critique
- [Imitation learning](../concepts/learning/imitation-learning.md) — behavioral-cloning scaling critique
- [World model](../concepts/world-models/world-model.md) / [World-model simulators](../concepts/world-models/world-model-simulators.md)
- [Latent space](../concepts/world-models/latent-space.md) — planning happens here

## Why this matters for the wiki

- **Net-new entity: [VL-JEPA](../entities/vl-jepa.md) (Meta, Chen et al., Dec 2025).** Distinct from the wiki's existing [VLA-JEPA](../entities/vla-jepa.md) (USTC, Sun et al.) despite the near-identical name — see the disambiguation note on both pages.
- **Partially answers a logged open question.** The [LeCun page](../entities/yann-lecun.md) asked whether anyone has built a working **Hierarchical JEPA (H-JEPA)**. This video reports a concrete 2-layer hierarchical world model extending push-t planning 5→15 steps — the first such result the wiki tracks, though the underlying paper isn't named.
- **First wiki source to lay out LeCun's VLA critique on camera**, with the wiki's own VLA evidence ([π0.7](../entities/pi07.md), RT-2) as the counterargument — a clean tie-in to [the critiques-of-the-intelligence-north-star synthesis](../syntheses/society/critiques-of-the-intelligence-north-star.md).
- **Concretizes LeWM planning** (CEM, ~5-loop horizon, embedding-distance cost) beyond the architecture-only treatment on the [LeWorldModel entity](../entities/leworldmodel.md).

## Open questions

- ~~**Which paper reports the hierarchical push-t 5→15 result?**~~ **Resolved:** it's **[HWM — "Hierarchical Planning with Latent World Models"](hwm-paper.md)** (Zhang, Terver, …, LeCun, Ballas — arXiv 2604.03208, April 2026), with Balestriero (the credited collaborator) among the authors. The video's "5→15 steps" was a simplification — the paper reports **Push-T 17%→61%** across task horizons d=25→75 (on a DINO-WM base, not LeWM), and **real-Franka 0%→70%** from a single goal image.
- **VL-JEPA vs VLA-JEPA naming** will keep causing confusion; the wiki should keep the disambiguation note current if either group renames.
- The "1.6B beats 7B on GQA" and "35% vs 20%" figures are the video's framing of the [VL-JEPA paper](https://arxiv.org/abs/2512.10942); the paper's own abstract emphasizes "50% fewer trainable params, 2.85× fewer decoding ops, comparable to InstructBLIP/QwenVL." Reconcile against the paper body if/when ingested.

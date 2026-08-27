---
title: Yann LeCun
type: entity
subtype: person
created: 2026-05-07
updated: 2026-08-26
sources: 40
tags: [person, meta-fair, nyu, jepa, world-model, turing-award, ami-labs, logical-intelligence, ebm, diffusion-policy, object-centric, spectral-graph-theory]
---

> [!note] Reported organizational changes
> Two post-Meta affiliations are recorded in this wiki, with different evidentiary weight:
> - **[AMI Labs](ami-labs.md)** (founder) — now corroborated beyond the original [Towards AI](../sources/towardsai-lecun-ami-labs.md) piece by [TechCrunch](https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/) (2026-03-09) and Wikipedia. The lab's *existence and funding* are no longer provisional; its *publications* remain unestablished.
> - **[Logical Intelligence](logical-intelligence.md)** (Founding Chair of Technical Research Board, announced 2026-01-21) — surfaced via [the Aleph EBM video source](../sources/2026-05-aleph-ebm-refuses-bullshit-video.md) drawing on the BusinessWire press release. The Logical Intelligence/yann-lecun bio page additionally lists him as "Executive Chairman of AMI Labs."
>
> These appear to be two separate companies, both downstream of LeCun's EBM-and-world-models agenda. Whether they collaborate, are parallel, or one is a subsidiary of the other is not addressed by any source in this wiki.
>
> **He publishes under NYU — but the first AMI Labs byline has now appeared.** Checked 2026-07-26: the two May 2026 world-model papers ([stable-worldmodel](../sources/stable-worldmodel-paper.md), [When Does LeJEPA Learn a World Model?](../sources/when-does-lejepa-learn-a-world-model-paper.md)) carry a **New York University** byline only. **However, [WorldDP](worlddp.md) (arXiv 2606.08775, 7 Jun 2026) lists LeCun's affiliation as "Courant Institute, NYU" *and* "AMI Labs"** — the first AMI-Labs-affiliated paper found in this wiki, updating the earlier "no AMI Labs paper exists" finding. See the [attribution correction](ami-labs.md#attribution-correction).

**Yann LeCun** — Silver Professor at NYU; Turing Award (2018, with Bengio + Hinton). Formerly VP & Chief AI Scientist at [Meta FAIR](meta-fair.md). Per secondary reporting (April 2026), now founder of [AMI Labs](ami-labs.md). As of **2026-01-21**, also Founding Chair of the Technical Research Board at **[Logical Intelligence](logical-intelligence.md)**. In this wiki, **the architect of the [JEPA](../concepts/world-models/jepa.md) research program** and the senior author or co-author across nearly every Meta-affiliated world-model paper ingested.

## Role in the JEPA program
LeCun introduced the JEPA framing publicly around 2022 and has driven its application to vision and robotics through the FAIR / Mila pipeline. He is **senior author** on every FAIR-affiliated JEPA / JEPA-adjacent paper this wiki has ingested:

- [V-JEPA 2](../sources/v-jepa-2-paper.md) (2025-06) — co-senior with Rabbat / Ballas / Bardes.
- [V-JEPA 2.1](../sources/v-jepa-2-1-paper.md) (2026-03) — same.
- [LeWorldModel](../sources/leworldmodel-paper.md) (2026-03) — senior author (with Mila / NYU / Samsung / Brown collaborators).
- [DINO-WM](../sources/dino-wm-paper.md) (2024-11) — co-senior with Lerrel Pinto (NYU).
- [DINO-world](../sources/dino-world-paper.md) (2025-07) — listed in author group.
- [JEPA-WMs](../sources/jepa-wms-paper.md) (2025-12) — co-senior with Bardes.
- **[stable-worldmodel](../sources/stable-worldmodel-paper.md) (2026-05-20)** — co-author (12 authors, led by [Lucas Maes](lucas-maes.md)); the reproducibility/evaluation platform.
- **[When Does LeJEPA Learn a World Model?](../sources/when-does-lejepa-learn-a-world-model-paper.md) (2026-05-25)** — co-author with [Klindt](david-klindt.md) + [Balestriero](randall-balestriero.md); the [identifiability](../concepts/world-models/identifiability.md) theorems.
- **[WorldDP](../sources/worlddp-paper.md) (2026-06-07)** — co-author (with NYU Tandon's Goswami / Krishnamurthy / Khorrami); an **object-centric world model + [Diffusion Policy](diffusion-policy.md)** hierarchy for multi-stage manipulation. His **first AMI-Labs-affiliated byline** in this wiki, and a rare robotics/manipulation paper (vs. his usual JEPA-world-model line).

- **[Spectral Graph Theory: The Mathematics of Self-Supervised Learning](../sources/spectral-graph-theory-ssl-paper.md)** (2026, with [Balestriero](randall-balestriero.md), IEEE Signal Processing Magazine 43(3):8–20) — a review formalizing **[SSL as spectral graph learning](../concepts/learning/spectral-theory-of-ssl.md)** (VICReg ↔ Laplacian Eigenmaps, SimCLR ↔ MDS, …); the math spine under the JEPA/LeJEPA line. Paywalled; ingested via its open 2022 precursor.

> [!note] One more LeCun paper not ingested here
> **S-JEPA** (arXiv 2606.19398, JEPA extended to *speech*, with Ravid Shwartz-Ziv, NYU) surfaced in the 2026-07-26 web search but is **not ingested**. NYU-bylined.

Ten papers in this wiki now carry his name. The world-model paradigm that distinguishes [FAIR](meta-fair.md) from [NVIDIA](nvidia.md) (generative video) and [AGIBOT](agibot.md) (sim-native) is, for practical purposes, LeCun's research direction.

## Public stance relevant to this wiki
- **Latent-prediction over generative-video.** LeCun has argued publicly (talks, blog posts, social media) that pixel-level generative models are the wrong target for video world modeling — that prediction in representation space is more efficient and more aligned with what biological systems do. JEPA is the technical instantiation of that argument. The on-camera framing of this position is the **[Welch Labs explainer "Yann LeCun's $1B Bet Against LLMs" (2026-05-01)](../sources/welchlabs-lecun-1b-bet-against-llms.md)**, which interviews LeCun and traces the blurry-pixels → Siamese → Barlow Twins → DINO → JEPA arc.
- **Canonical position paper.** **["A Path Towards Autonomous Machine Intelligence" (2022-06-27, v0.9.2)](../sources/lecun2022-path-towards-ami.md)** is LeCun's full architectural vision document: a six-module differentiable agent (perception, world model, actor, cost, short-term memory, configurator), JEPA / H-JEPA as the world-model substrate, intrinsic-cost + learned-critic as the reward replacement, and the long-form argument against contrastive SSL and generative video. **Every JEPA paper in this wiki instantiates a piece of this blueprint.** It is also the source of LeCun's repeated public claim that "LLMs are insufficient for common sense."
- **Self-supervised learning at internet-scale.** The V-JEPA 2 framing — internet-scale video pretraining + small action-conditioning — is consistent with LeCun's broader "energy-based models / observation-only learning" agenda predating JEPA. The same Welch Labs video opens with his "intelligence is a cake" metaphor (SSL = cake, supervised = icing, RL = cherry).
- **"VLA are doomed."** In the on-camera [Welch Labs Part 2 explainer (2026-05-30)](../sources/welchlabs-lecun-1b-bet-against-llms-part2.md), LeCun makes his sharpest recorded attack on the dominant [VLA](../concepts/learning/vla-models.md) paradigm, on two grounds: **(1)** behavioral cloning doesn't scale and is brittle ("completely helpless" in slightly-new situations), and **(2)** VLAs lack explicit planning / a world model — *"I do not understand how you can even think of building an agentic system without … the ability of predicting the consequences of its actions."* The JEPA + planning alternative is his answer. (The wiki's own VLA evidence — [π0.7](../entities/pi07.md) emergent capabilities, RT-2 generalization — is the standing counterargument; see [critiques of the intelligence north star](../syntheses/society/critiques-of-the-intelligence-north-star.md).)
- **Near-term AMI Labs plan (per Part 2).** Within 1–2 years, apply world-model planning to **complex industrial systems "that cannot be reduced to a small number of equations"** (jet engines, chemical/power plants, a diabetes patient's blood-sugar control, stem-cell→beta-cell differentiation, materials/catalyst/battery design) — explicitly *not* robot arms / humanoids / rockets, whose dynamics can be written down. Within 3–5 years, the stated ambition is to be "the main supplier of intelligent systems." See [AMI Labs](../entities/ami-labs.md).

## Position in the broader field
LeCun is one of the small number of researchers whose **simultaneous senior position at a major lab + university appointment + Turing-award credibility** lets him drive a multi-year research program at scale. The JEPA program is the visible artifact of that.

## Related
- [Meta FAIR](meta-fair.md) — prior primary affiliation.
- [AMI Labs](ami-labs.md) — his new lab; existence corroborated, no publications attributable to it.
- [Randall Balestriero](randall-balestriero.md) — the theory-side counterpart on the LeJEPA line.
- [Lucas Maes](lucas-maes.md) — LeWorldModel + stable-worldmodel lead.
- [David Klindt](david-klindt.md) — identifiability paper lead.
- [Identifiability](../concepts/world-models/identifiability.md) — the strongest formal result the JEPA program has produced.
- [Logical Intelligence](logical-intelligence.md) — Founding Chair of Technical Research Board (2026-01-21); commercializes EBMs for reasoning. Distinct from AMI Labs.
- [Energy-based models](../concepts/learning/energy-based-models.md) — the long-running thread that underlies both JEPA and the new Kona work.
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — research program LeCun architected.
- [Adrien Bardes](adrien-bardes.md) — frequent JEPA co-senior.
- [Basile Terver](basile-terver.md) — JEPA-WMs lead author working under LeCun.

## Earlier work (AT&T Bell Labs era)
- **[Bromley, Guyon, LeCun, Säckinger, Shah 1993 — "Signature Verification using a 'Siamese' Time Delay Neural Network"](../sources/bromley1993-siamese-signature-verification.md)** — co-author (third position). The **original [Siamese network](../concepts/world-models/siamese-network.md) paper**, written during LeCun's AT&T Bell Labs Holmdel period. Architecturally continuous with the 2020s JEPA program: two weight-tied encoders + a similarity head is the J/A in JEPA, 30 years before LeCun named the framework. The Welch Labs explainer's framing of JEPA as "the natural continuation of the Siamese-network research LeCun started in the 1990s" is literally correct — same author, same architectural family, different loss.

## Mentioned in
- [VAE Paper (Kingma & Welling, 2013)](../sources/vae-paper.md) — his predictive sparse decomposition (Kavukcuoglu, Ranzato, LeCun 2008) is cited as an encoder–decoder architecture the VAE authors "drew some inspiration" from.
- [Bromley et al. 1993 — Signature Verification using a Siamese TDNN](../sources/bromley1993-siamese-signature-verification.md) — co-author; original Siamese network paper.
- [Barlow Twins Paper (Zbontar et al., ICML 2021)](../sources/barlow-twins-paper.md) — senior author; first non-asymmetric anti-collapse SSL method.
- [VICReg Paper (Bardes, Ponce, LeCun, ICLR 2022)](../sources/vicreg-paper.md) — senior author; the regularizer LeCun later endorses in his AMI paper as JEPA's anti-collapse method.
- [A Path Towards Autonomous Machine Intelligence (LeCun, 2022)](../sources/lecun2022-path-towards-ami.md)
- [V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)
- [V-JEPA 2.1 Paper](../sources/v-jepa-2-1-paper.md)
- [LeWorldModel Paper](../sources/leworldmodel-paper.md)
- [DINO-WM Paper](../sources/dino-wm-paper.md)
- [DINO-world Paper](../sources/dino-world-paper.md)
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md)
- [LeJEPA Paper](../sources/lejepa-paper.md)
- [Towards AI — LeCun / AMI Labs article](../sources/towardsai-lecun-ami-labs.md)
- [Welch Labs — Yann LeCun's $1B Bet Against LLMs (video)](../sources/welchlabs-lecun-1b-bet-against-llms.md)
- [Welch Labs — Yann LeCun's $1B Bet Against LLMs Part 2 (video)](../sources/welchlabs-lecun-1b-bet-against-llms-part2.md) — VLA critique, hierarchical-JEPA push-t result, AMI near-term plan.
- [Hierarchical Planning with Latent World Models (HWM, paper)](../sources/hwm-paper.md) — senior author; the realized H-JEPA.
- [WorldDP paper (Goswami et al. 2026)](../sources/worlddp-paper.md) — co-author; object-centric world model + diffusion policy; his first AMI-Labs-affiliated byline here.
- [Spectral Graph Theory review (Balestriero & LeCun, IEEE SPM 2026)](../sources/spectral-graph-theory-ssl-paper.md) — co-author; SSL as spectral graph learning, the theory spine under JEPA.
- [Aleph and Energy-Based Models: The AI That Refuses to Bullshit (video)](../sources/2026-05-aleph-ebm-refuses-bullshit-video.md) — names LeCun as Founding Chair of Logical Intelligence's Technical Research Board; verbatim quote on EBMs as "reasoning and inference by minimizing an energy function."

## Resolved / TBD
- ~~Has anyone built a working **Hierarchical JEPA (H-JEPA)** at the multi-time-scale envisioned in the [2022 position paper](../sources/lecun2022-path-towards-ami.md)?~~ **Resolved (2026-05-31):** **[HWM — "Hierarchical Planning with Latent World Models"](../sources/hwm-paper.md)** (Zhang, Terver, …, LeCun, Ballas — arXiv 2604.03208, April 2026) is the concrete realization: a two-temporal-scale latent MPC wrapper (high-level macro-actions → subgoals → low-level primitive actions), model-agnostic across [DINO-WM](dino-wm.md), [PLDM](pldm.md), and [V-JEPA 2](v-jepa-2.md)-AC. Real-Franka pick-&-place **0%→70%** from a single goal image; Push-T **17%→61%** at the hardest horizon. (This is the paper the [Welch Labs Part 2 video](../sources/welchlabs-lecun-1b-bet-against-llms-part2.md) referenced but couldn't name — and its "5→15 steps" was a simplification of the paper's d=25→75 task-horizon framing.) Note it's **two** levels and goal-image-conditioned; the N-level *emergent* hierarchy and language conditioning remain open.
- Has the **configurator** module (Section 6 of the 2022 paper) ever been concretely instantiated? LeCun left it as a sketch; worth checking AMI Labs / later FAIR output.

## Summer 2026 batch (ingested 2026-08-26)

Six papers, June–August 2026, spanning the program's breadth. Ordered by relevance to this wiki:

- **[LpWM](../sources/lpwm-paper.md)** (Aug 24) — sparse latent geometry lowers the predictor capacity needed to plan; mode-factored codes. **Sits in tension with his own group's [identifiability result](../concepts/world-models/identifiability.md)** that the Gaussian is uniquely optimal.
- **[Patch Policy](../sources/patch-policy-paper.md)** (Jul 20, with [Lerrel Pinto](lerrel-pinto.md)) — a 51M-parameter policy on frozen patch features beats a fine-tuned 7.6B [OpenVLA-OFT](openvla.md) in-domain at 10.99 ms latency.
- **[AdaJEPA](../sources/adajepa-paper.md)** (Jun 30) — [test-time adaptation](../concepts/learning/test-time-adaptation.md) of a latent world model inside the MPC loop; one gradient step per replan.
- **[TDV](../sources/tdv-paper.md)** (Jun 14) — SSL from temporal differences; the argument that **optimal inductive-bias strength decreases as data grows.**
- **[Music-JEPA](../sources/music-jepa-paper.md)** (Jul 24) — the action-conditioned world-model recipe outside vision (audio = state, pianoroll = action).
- **[HP-JEPA](../sources/hp-jepa-paper.md)** (Aug 1) — multi-resolution graph JEPA. Peripheral to this wiki.

> [!note] The batch is mostly other people's first-author work
> He is a middle or late author on all six, across five different institutional clusters (NYU, Mila/Brown, UIUC, Stony Brook, Columbia-adjacent). Read as a research *program* propagating rather than a lab shipping — which is consistent with the wiki's earlier observation that his AMI Labs affiliation appears on almost none of the papers carrying his name.

**Two further world-model papers surfaced in Music-JEPA's references and are not ingested**: *"Closing the train-test gap in world models for gradient-based planning"* (arXiv 2512.09929) and *"Temporal straightening for latent planning"* (arXiv 2603.12231). Both look directly relevant to the latent-planning thread.

- [LpWM paper](../sources/lpwm-paper.md)
- [Patch Policy paper](../sources/patch-policy-paper.md)
- [AdaJEPA paper](../sources/adajepa-paper.md)
- [TDV paper](../sources/tdv-paper.md)
- [Music-JEPA paper](../sources/music-jepa-paper.md)
- [HP-JEPA paper](../sources/hp-jepa-paper.md)

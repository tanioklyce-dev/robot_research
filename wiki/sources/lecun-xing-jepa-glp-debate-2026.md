---
title: "How Should AI Learn to Understand the World? — Yann LeCun & Eric Xing on JEPA and GLP (Spring School AI for Impact, 2026)"
type: source
url: https://www.youtube.com/watch?v=8LKgvrNYZz0
local_path: raw/2026-03-spring-school-lecun-xing-jepa-glp-debate.txt
sha256: fae9379e7f81135954667ad3c9f13df0fc2b6c1d7755d28cd2698a1a6b8f3167
author: "Eric Xing (MBZUAI / CMU), Yann LeCun (NYU / AMI Labs); moderated by the Spring School organisers"
published: 2026-03-25
ingested: 2026-09-07
venue: "Spring School AI For Impact 2026, UM6P Benguerir, Morocco (co-organised by EMINES-UM6P, École Polytechnique, EMSI; supported by OCP). Recorded March 2026 (the Critique cites 2026-03-25); uploaded to YouTube 2026-05-01 by channel 'melrhabi'. Both speakers remote."
duration: "2:31:31"
format: video (auto-captioned transcript, deduplicated, ~1-minute paragraphs; proper names garbled)
tags: [debate, jepa, glp, world-model, lecun, xing, pan, generative, reconstruction, entropy, collapse, mpc-vs-rl, benchmarks, spring-school, primary]
---

# LeCun & Xing on JEPA and GLP — the debate

The primary the [Critique of World Model](critique-of-world-model-paper.md) cites as its reference [32]. Structure: **[03:07–58:39]** Xing's talk (*"beyond book intelligence"*, the Critique's five axes, [PAN](../entities/pan-world-model.md), the agent-model roadmap); **[71:46–84:56]** LeCun's ten-minute statement; **[85:56–104:07]** Xing's point-by-point rebuttal; **[105:09–112:11]** LeCun's rebuttal; **[112:11–117:14]** Xing again; **[118:23–150:52]** audience questions. Transcript is auto-captioned; timestamps below are minutes into the video.

## Summary

Billed as a debate, run as one, and yet the two men agree on more than they disagree: a world model is a simulator for planning, not a video generator; prediction should happen in an abstract latent space; hierarchy is essential; "AGI" is *"a hollow empty word"* (Xing) / *"nonsense"* (LeCun); benchmarks should be planning tasks, ideally out of distribution. The disagreement is narrow and Xing names it at [132:39]: **where does the prediction get *checked*** — in latent space (LeCun) or against the observation (Xing)? LeCun: *"That may be where we disagree."* Everything else — data, discrete vs continuous, MPC vs RL — is either conceded or reduced to engineering.

## Key claims — LeCun

- **"World models must not be generative"** [71:46], opening line. Text is ~10¹⁴ bytes; video is unlimited [72:46]. *"You cannot imagine building a reliable agentic system without that system being able to predict the consequences of its own actions"* [73:47]. **Inference is by optimisation** against task + guardrail objectives [74:49–75:52].
- **Fifteen years of failing at pixel prediction** [76:52–77:52]: *"essentially failing for the first 10 of those 15 years, including using all kinds of latent variable models."* The rotating-camera example: no system can predict what everyone in the room looks like — *"the information is just not there."*
- **The entropy argument** [105:09–108:09], his central rebuttal: `PV = nRT` is a useful model of an intractable molecular process precisely because it ignores what cannot be predicted. *"This is the only way to understand reality: to ignore details you cannot predict."* JEPA trades off information content against prediction error and keeps only the predictable part. **"Whatever information you cannot predict is not going to be useful. I guarantee that."** [109:09]. The car and the leaves on the roadside trees [110:10]: *"If you attempt to train your system to make those predictions, you kill it."*
- **A field of science is a level of abstraction** [79:53–81:53]: quantum fields → particles → atoms → molecules → proteins → cells → organisms → societies; *"every level in this hierarchy is a different field of science … that essentially destroys the whole idea of generative models."*
- **The empirical claim** [137:44–139:45]: at Meta, MAE *"basically failed"* — *"none of those techniques ever produced competitive representations for images. Like, none. Absolutely none. … All attempts to train image representation by reconstruction have failed. … It's not Yann's intuition. It's hard data."* DINO, I-JEPA, MoCo, SimSiam, SimCLR are the counter-list.
- **Why not predict a distribution over videos** [135:42–137:44]: normalising an energy over the space of video clips is intractable; diffusion models look good but carry *"absolutely zero guarantee that the model is not mode collapsed."*
- **Jupiter in six numbers** [130:37]: all we know about Jupiter is enormous, but predicting its position in a century needs three positions and three velocities — *"the genius of Newton was to figure out what is the right representation."*
- **Concessions.** *"You don't need text, but if you have text, you might as well use it. And there is no objection to using text in the context of a JEPA architecture"* [112:11]. [SIGReg](../concepts/world-models/sigreg.md) named as the regulariser (*"distribution of points … basically isotropic Gaussian"*) and [LeWorldModel](../entities/leworldmodel.md) as *"still at relatively small scale, but it works"* [82:54–83:54].
- **On intelligence and benchmarks** [144:45–148:50]: LLMs hold declarative knowledge and reason only where language is the substrate (code, maths, law); intelligence is the speed of learning a new task — the teenager who learns to drive in 20 hours against millions of hours of behaviour-cloning data that still does not match human reliability, *"because the dataset does not have complete coverage of all the corner cases."* Benchmarks must be planning tasks, out of distribution, and eventually measure adaptation speed rather than a fixed suite.

## Key claims — Xing

- **Intelligence by utility, in tiers** [09:10–13:12]: book (lingual) → physical → social → philosophical. Reasoning-model failures on a helping-or-harming photo and on simple motion/size questions [04:08–06:09].
- **The five axes, and GLP** [20:16–33:21]: information density over volume; a **stateful, identifiable** latent (words as *"human embeddings of what they see"*, plus learned tokens); a closed-loop encoder–backbone–decoder; a generative loss that is *"strictly an upper bound of the latent loss"* [30:19]; MPC **plus** offline RL on the simulator, *"like a Go player doing self-play when not in a match"* [32:20].
- **The rebuttal** [85:56–104:07]. Common ground first: *"I fundamentally agree with Yann that the prediction needs to happen in abstract space."* Then: (i) **video is not enough** — the 1968 Saigon execution photograph, where the context that flips the reading is not in the pixels [87:58–88:59]; (ii) **an apple rotting over months** needs symbols, not a visual simulator [90:01]; (iii) **the encoder becomes a predictor**, so whatever does not help prediction is discarded, and *"that information loss is very hard to recover"* [91:01–92:01]; (iv) **saliency is defined by the training data** — *"when you go to testing data, the generalisability is lost because you may already have lost the information"* [94:02–95:04]; (v) efficiency is *"an engineering issue"* — partial reconstruction, sparse attention, video generated at 10× playout speed [35:23–36:24, 95:04]; (vi) **interoperability** — GLP plugs into existing VLMs, diffusion decoders and LLMs (their own K2), JEPA latents *"are very difficult to interpret and be compatible with existing systems built elsewhere"* [97:04–98:04].
- **"GLP can strictly subsume JEPA if you turn off the generative function"** [115:14–116:14] — and the reconstruction weight can be dialled, and validation can happen *"from time to time, not every frame."*
- **On the pixel-loss objection** [119:25–120:26]: *"There is no such score that we use to measure pixel-level reconstruction. This is a training score, not an evaluation score."* Reconstruction is *"a form of examination"*, not the goal.
- **Verification by generation** [128:36–129:36]: theories are validated by predicting the position of a star and going to measure — *"that is how an abstract theory is established."* And the red-shift [131:39]: nobody was collecting red-shift data; the discovery came from a mismatch in data kept for other reasons — *"we will not always know what we actually need to predict."*
- **The biologist's position** [140:45]: *"all data are good data"*; LLM training throws everything in. And a bet on hardware [141:45–142:45]: *"I want to make sure the model architecture itself is not a function of current technology."*
- **The agent model** [45:29–56:37]: "system three" — a configurator deciding when to plan (system two, world model) and when to react (system one, policy); a self-regulatory agent prototype at ~20–30 B parameters claimed comparable to models *"hundreds of times bigger"* on a planning benchmark (model names garbled in captions; unverified).

## The wiki's read

> [!note] The crux, stated once
> [132:39–133:39] Xing: *"the point of prediction lies, in my opinion, in the observation space, not in the latent space."* LeCun: *"That may be where we disagree. … There's a trade-off between maximising information and minimising prediction error, and this is exactly what the JEPA training criteria are doing."* That exchange is the whole debate. Everything else is agreed or engineering.

- **They argue past each other on *rare* versus *unpredictable*, and nobody says so.** Xing's example is the car crash: rare in training, decision-critical, and *predictable* once it starts. LeCun's examples are the leaves and the room: *unpredictable* from the available information, at any data scale. LeCun's *"whatever you cannot predict is useless"* is true of the leaves and irrelevant to the crash; Xing's *"saliency is set by training data"* is true of the crash and irrelevant to the leaves. The wiki's [abstraction-tax](../syntheses/world-models/abstraction-tax.md) page already holds this distinction under another name: the declared axis. A JEPA cannot generalise along an axis nothing declared; a reconstruction loss declares every axis, including the ones that are noise. That is the actual trade, and it is task-dependent.
- **LeCun's evidentiary claim is stronger than the evidence.** *"All attempts to train image representation by reconstruction have failed"* is true of **linear-probe** quality and false of **fine-tuned** quality — MAE fine-tunes competitively, which is why the [anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) files reconstruction as *"the control condition, and stronger than the wiki's framing of it."* The [Van Assel theorem](joint-embedding-vs-reconstruction-paper.md) is the honest form of his claim: latent prediction wins *when nuisance noise is high-dimensional*.
- **Xing's subsumption remark converts the debate into a hyperparameter.** If GLP with reconstruction weight zero *is* JEPA, then the question is the value of that weight, and the answer is an experiment on a task with a known shift axis — the [declared-axis experiment](../syntheses/world-models/declared-axis-experiment.md). Neither speaker proposes it.
- **Two concessions worth recording.** LeCun on text: *no objection*. Xing on latent space: *fundamentally agree*. The data axis and the "encoder–encoder vs generative" framing of the Critique are both softer live than on paper.
- **The Critique's "stateful discrete tokens" thesis does not appear in the [PAN results](pan-world-model-paper.md).** PAN's latent state is 256 *continuous* tokens from a VLM. Xing did not raise this; nobody asked.
- **Evidentiary weight.** No numbers were exchanged. LeCun cites LeWorldModel as small-scale-but-working; Xing cites PAN's benchmark by name and shows demos. The [PAN paper](pan-world-model-paper.md) is where the numbers are.

## Entities mentioned

- [Yann LeCun](../entities/yann-lecun.md), [Eric Xing](../entities/eric-xing.md), [MBZUAI](../entities/mbzuai.md), [AMI Labs](../entities/ami-labs.md), [PAN](../entities/pan-world-model.md), [LeWorldModel](../entities/leworldmodel.md), [DINO](../entities/dino.md), [SimSiam](../entities/simsiam.md).

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md), [Generative Latent Prediction](../concepts/world-models/generative-latent-prediction.md), [World model](../concepts/world-models/world-model.md), [SIGReg](../concepts/world-models/sigreg.md), [Energy-based models](../concepts/learning/energy-based-models.md) (LeCun's normalisation argument), [World-model evaluation](../concepts/world-models/world-model-evaluation.md) (both agree benchmarks must be planning tasks).

## Open questions

- Which of the two is right about MAE at the relevant scale? The wiki has the lineage page but no fine-tune-vs-linear-probe table for video encoders.
- The self-regulatory agent Xing describes [51:36–54:36] has no primary in the wiki; captions garble its name and its comparison models. Un-ingested.
- Names of audience questioners are auto-captioned and unverified; none are used on this page.

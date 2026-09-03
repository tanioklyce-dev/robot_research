---
title: "Third World Modeling Workshop — Day 3 (Chicago Booth, 2026-09-02)"
type: source
url: https://www.youtube.com/live/PkaYC3fwEsc
local_path: raw/2026-09-02-chicago-booth-world-modeling-workshop-day3-transcript.txt
sha256: 15466aa66d326222bd16257bb3ac249ed17991d729eafe20a2ec75e66d12ac5b
author: "Center for Applied Artificial Intelligence (CAAI), Chicago Booth; organized by Randall Balestriero, Bradford Levy, Kawin Ethayarajh, XY Han"
published: 2026-09-02
venue: "Chicago Booth / Gleacher Center — livestream recording, 7h48m"
format: video (livestream) — machine transcript (YouTube auto-captions)
tags: [world-models, workshop, jepa, lejepa, sigreg, lewm, levjepa, tutorial, finance, marketone, simulation-economics, synthetic-data, lambda, massive, history, transcript, secondary-source]
ingested: 2026-09-03
---

## Summary

Day 3 of the **third World Modeling Workshop** — the hands-on day, and structurally unlike [Day 1](chicago-booth-world-modeling-workshop-2026.md) (JEPA/robotics keynotes) or [Day 2](chicago-booth-world-modeling-workshop-2026-day2.md) (finance/economics keynotes). Two tutorials, one vendor talk, one infrastructure talk, a two-hour hackathon, seven participant presentations, and closing remarks. **The value here is procedure, not claims**: this is the day where the wiki's most-covered method line ([LeJEPA](lejepa-paper.md) → [SIGReg](../concepts/world-models/sigreg.md) → [LeWM](../entities/leworldmodel.md)) is taught by its author, live, from the code the wiki [already ingested](wm-booth-lejepa-lewm-tutorial-repo.md).

Four things on this page are not anywhere else in the wiki:

1. **[Balestriero](../entities/randall-balestriero.md)'s own account of why reconstruction fails** — not the usual "it wastes capacity on pixels" hand-wave, but a spectral argument with a falsifiable prediction, plus a demonstration that **reconstruction loss carries no information about representation quality at all**.
2. **A cost model for synthetic data** ([Amir Zadeh](../entities/lambda.md), Lambda) — simulation-seconds per GPU-second across four scene complexities, with the sensor stack as the cliff. The wiki has argued for years that synthetic data scales; this is the first source that prices it.
3. **The augmentation-design problem for financial world models** ([Bradford Levy](../entities/bradford-levy.md)) — what "a different view of the same thing" even means when the thing is a limit order book, and why the obvious answer provably cannot learn what you want.
4. **A three-era history of the term "world model"** ([Kawin Ethayarajh](../entities/kawin-ethayarajh.md)'s closing remarks), reaching back to Epictetus and forward to three named open problems.

> [!warning] Machine transcript — names reconciled against the programme
> `raw/` holds YouTube auto-captions, so proper nouns are badly garbled: *"Rando Bolstrio"* (Randall Balestriero), *"Leeppa"* / *"Japa"* / *"Jeepa"* (LeJEPA / JEPA), *"cig"* / *"creg"* / *"C greg"* (SIGReg), *"lower model"* / *"lo wall model"* (LeWM), *"Levie Jeppa"* / *"Louis Vij Japa"* (LeVJEPA), *"m0ero"* (MuZero), *"Exand"* (XLand), *"Ilia Sutsker"* (Ilya Sutskever), *"Daario Amade"* (Dario Amodei), *"W Terry Winterrad"* (Terry Winograd), *"Ra Sutton"* (Rich Sutton), *"epspooly"* (Epps–Pulley), *"craral the theorem"* (Cramér–Wold). **Every speaker name, talk title and room assignment on this page comes from the workshop programme**, archived at `raw/2026-09-02-wm-booth-org-programme.html`; paper titles and author lists were checked against arXiv and the vendors' own sites. Timestamps are reliable; quotes are lightly cleaned.

## Programme

Times are video-relative (the stream opens ~5 minutes before the first talk).

| Time | Speaker | Session |
|---|---|---|
| 00:05:02 | **Randall Balestriero** (Brown) | Tutorial 1 — *How to Train JEPA World Models Without Headache* |
| 02:03:12 | **Steve Bravo** ([Massive](../entities/massive.md)) | *Institutional-Grade Market Data* |
| 02:21:49 | **Bradford Levy** (Chicago Booth) | Tutorial 2 — *Financial Data: Challenges, Evaluation, and Training* |
| 04:32:59 | **Amir Zadeh** ([Lambda](../entities/lambda.md), via Zoom) | *Scaling GPU Infrastructure* |
| 05:16:35 | — | Open working session — modeling challenge (2 h) |
| 07:03:09 | ×7 participants | Challenge presentations |
| 07:33:02 | **Kawin Ethayarajh** (Chicago Booth) | Closing remarks |

---

## Tutorial 1 — Balestriero, *How to Train JEPA World Models Without Headache* (00:05:02)

He opens by lowering expectations, and the disclaimer is the most useful sentence in the tutorial:

> *"We are not yet at the stage like supervised cross-entropy-based training where you can just plug anything and Adam will do all the heavy lifting… It's a lot of careful parameter tuning, careful debugging, looking at the embeddings you learn and trying to understand what happens."*

He put "counterfactual" in the submitted title and drops it immediately — *"this will actually be one of the open research questions I will mention at the end."*

### The argument against reconstruction, stated properly

The wiki's [JEPA](../concepts/world-models/jepa.md) page carries the standard case (pixel prediction wastes capacity on unpredictable detail). Balestriero's case is different and stronger, and it comes in three parts.

**1. Reconstruction loss is uninformative about representation quality.** Two autoencoders, same architecture, same initialization, same data order. Their reconstructions are visually indistinguishable and their **train and test MSE curves lie on top of each other** — and their embeddings differ by **~20 points of ImageNet classification accuracy**, under both linear *and* nonlinear probes.

> [!note] The construction is deliberately artificial, and that is the point
> Asked what separates them, he says the second run adds *"a very very very very small gradient signal so that you keep the same reconstruction loss but you learn features that are more aligned with your downstream task."* So this is an existence proof, not a measurement of ordinary training: **the reconstruction objective does not determine the representation**. Left alone, MAE-style training lands in the bad case (*"if you just do the default MAE autoencoding style, you will end up in the blue scenario"*).

**2. Why it lands in the bad case — a spectral argument.** Image pixel covariance has the familiar **1/f eigenvalue decay**. Gradients of an MSE reconstruction loss are guided by the top eigenvectors of that covariance, so **the model learns the largest-eigenvalue subspaces first** and works down. He shows the reconstructed spectrum filling in from the high-eigenvalue end across training, and states the prediction as a prediction: *"if you give me a dataset I can tell you what you will learn first."* It is provable in the linear regime and at initialization; it matches empirically across MLP, ResNet and transformer, *"if your architecture is powerful enough."*

**3. Why that ordering is the wrong ordering.** Low-frequency-filtered images are colour and coarse contour — *"there is no way you know what it is."* High-frequency-filtered images keep the structure that classification, segmentation and counting need. **Reconstruction learns the useless half first and the useful half last**, which is exactly the observed slow convergence of MAE relative to a JEPA at equal FLOPs.

The escape hatch — *just find a better reconstruction loss* — he closes off by scope: SSIM is image-specific; LPIPS needs a pretrained network, *"which defeats the whole sense of it"*; and outside images (**EEG, stock prices**) MSE is worse still. His summary:

> *"If your goal is to come up with a better objective than MSE, you're basically competing with 60 years of extremely smart researchers who tried to do this and quote-unquote did not succeed yet… I would argue that if you are able to find a meaningful reconstruction loss, it means you already learned everything, because you are able to construct a loss with all the invariances that you need."*

He applies the critique to [Dreamer v4](../entities/dreamer.md) by name: its causal tokenizer learns `Z` **by reconstruction**, which is why it is stable to train (*"it will produce good reconstructed pixels, training probably will not diverge"*) and why he thinks `Z` is not a good representation. See [Dreamer](../entities/dreamer.md) for the other side.

### SIGReg, taught rather than proved

The derivation matches the [SIGReg concept page](../concepts/world-models/sigreg.md); what the tutorial adds is emphasis and engineering advice.

- The DINO critique is sharper here than in the papers: EMA doubles model memory, adds a hyperparameter, and **makes the loss uninterpretable** — *"you can see the loss actually increase but the quality of your model become better and better."* He shows hyperparameter sensitivity taking ImageNet-1k accuracy *"from almost state-of-the-art to completely random."* That instability, he says, is the reason people won't train JEPAs at all.
- **Cramér–Wold** is presented as the load-bearing lemma, with an aside worth keeping: XY Han's reaction from the statistics side was *"I mean, it's kind of obvious though"* — Balestriero's reply, *"you say that's obvious for statisticians, but typically people don't always learn about it."*
- **Epps–Pulley** is chosen for gradient properties, not statistical power: characteristic-function-based, always exists, no moment conditions, *"literally one line of code"* on GPU, no all-gather. The one implementation gotcha he calls out live: **the random projection directions must be identical across GPUs** — seed carefully.
- The generalized advice: *"if you work on JEPA and you want to come up with a new objective, always keep in mind to look at the gradients."*
- **Architecture-agnosticism as the selling point for this audience**: 50 architectures thrown at ImageNet-10 out of the box, all training to within a small delta. *"When you want to do JEPA on new domains with new architecture, you need this stability"* — aimed squarely at the finance half of the room.

### The two exercises, and the debugging habit

The code is the [tutorial repo](wm-booth-lejepa-lewm-tutorial-repo.md) the wiki ingested the day before, now with narration.

| Exercise | What it is | His live figures |
|---|---|---|
| `inet10.py` | ResNet-9 LeJEPA on ImageNette | *"8 minutes on one GPU, 80% accuracy"* |
| `mmnist.py` + `app.py` | Action-conditioned [LeWM](../entities/leworldmodel.md) on Moving MNIST, then an interactive viewer | *"10 minutes"*; ~80% digit accuracy under a nonlinear probe, **position near-perfect** |

> [!note] His numbers are live-talk numbers; the repo page has measured ones
> The [tutorial repo page](wm-booth-lejepa-lewm-tutorial-repo.md) records **76.7 / 78.1% linear probe in 8m29s** and **digit accuracy 66.4 / 76.9% against position R² 0.9195 / 0.9830**. Same story, and the position-vs-identity split is the same lesson: *"you always track the position extremely extremely well… but you do have a small weird shaping of the actual digit number."* Sevens turn into eights while the location stays exact.

Suggested variations for the afternoon, in his order: **change the target distribution** (rederive the characteristic function and swap it into Epps–Pulley), vary the number of views, vary the SIGReg/prediction loss weighting, change the encoder. Google Colab is enough.

**The debugging habit is the transferable part**, and it is stated as a rule:

> *"This is something that you should always do when you train a world model. Always plug a detached online decoder and see what it reconstructs, because this is quite informative to see if you have a collapsed Z, or if you have a Z that actually did not collapse enough and the reconstruction is very crisp."*

The decoder is trained **post-hoc, detached**, purely for visualization — it never touches the training dynamics. On his cube-manipulation example the arm motion and joints decode correctly from actions alone while **cube rotation and gripper rotation do not**, which he offers as the open question: *"what do you capture or not, and how can you assess if you learned a good Z without having to reconstruct?"*

And a research-methodology warning that generalizes past JEPA:

> [!warning] Don't use planning success as your research signal
> *"The planning performance is very very sensitive to the planner you use, when do you replan, open loop or closed loop… it's not a nice signal to do research."* His recommended ladder: **decoded frames → probe `Z` for known object properties (XYZ position) → only then planning**. A single 3D cube plan can occupy a GPU for ten minutes, so the signal is slow as well as noisy. This is the same measurement complaint the wiki records under [world-model evaluation](../concepts/world-models/world-model-evaluation.md) and [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md), arriving from a third direction.

### Inverse dynamics as the rival regularizer — and the combination

He presents [SMWM](../entities/smwm.md)'s inverse-dynamics regularizer (predict `a_t` from `z_t, z_{t+1}`) fairly, as a *different theory of what a latent should contain*: not everything, only what the agent's actions determined. Two things the [SIGReg page](../concepts/world-models/sigreg.md) did not have:

- **Why IDM latents plan better.** If the inverse model is weak — linear, say — then a linear combination of `z_t` and `z_{t+1}` must recover `a_t`. *"This is a very very strong geometric constraint on how you put your Z embedding, which you don't have with SIGReg"*, and the result is a space *"much easier to optimize for at planning time."*
- **Why IDM alone is not enough, shown by ablation.** IDM's anti-collapse power is bounded by the richness of the action space. With no actions the latent loses object position and shape; with only XY control it preserves position but becomes **shape-invariant**; only with XY *and* rotation does it retain enough to reconstruct the object. *"In practice we never observe all the actions"* — so **combining SIGReg and IDM is the promising path**, and he says the latest work does exactly that.

An audience member asks the obvious question — *"to what degree is this just imitation learning?"* — and gets a clean answer: **imitation learning in terms of dynamics, but not in outcome, because planning at test time solves tasks not present in training.** Training data still has to explore; a random policy *"will never have an interaction with the cube, so you will not learn a meaningful world model."*

### Prediction loss as graph specification

The most theoretically interesting stretch, and the one the wiki's [spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md) page has been missing a plain-language version of.

Start with supervised least squares plus a linear probe and a Frobenius penalty. Solve **in closed form** for the probe weights and substitute back. The `Y` disappears and what remains is a trace involving `YᵀY` — an `N×N` matrix of **pairwise label relationships** — projected onto the whitened embeddings. So:

**Designing a prediction loss = designing a graph over samples.** Supervised learning connects all samples of a class. Standard SSL connects only augmented views of the same sample (as many disjoint complete subgraphs as there are samples). Both are special cases of one objective over an arbitrary affinity graph.

Two consequences he draws:

- **Coordinate-free labels are cheaper to obtain.** *"If I show you two pictures of a very specific dog and ask what's the dog breed, you will not know. But if I ask, is it the same dog breed, everyone will know."* Hence cheap active learning by filling in graph entries rather than labels.
- **Metadata becomes usable as supervision.** Using **captions** to build a denser graph (so a dog and a cat sharing a background are not fully disconnected) beats CLIP by *"a high margin"* — this is **X-CLR** / [X-Sample Contrastive Loss](https://arxiv.org/abs/2407.18134), and the graph-noise sensitivity work is a companion paper: false positives and false negatives **do not cost the same**, which is why characterizing the asymmetry matters.

He names four papers around this: the closed-form derivation (**"The Birth of Self-Supervised Learning: A Supervised Theory"**), relational representation learning under graph misspecification, the caption-graph paper (X-CLR), and a recent summary. The wiki has the [IEEE SPM review](spectral-graph-theory-ssl-paper.md) of the same line but none of these four.

### LeVJEPA, and where the program is going

Announced here as *"on arXiv like last week"* — it is **[LeVJEPA](../entities/levjepa.md)** (arXiv 2608.27395, 2026-08-27; Kuhn, **[Lucas Maes](../entities/lucas-maes.md)**, Serra, Le Lidec, **[LeCun](../entities/yann-lecun.md)**, **Balestriero**, Buettner). Structurally it is LeJEPA with multiple frames: encode two views of a clip, predict one from the other, SIGReg to prevent collapse, no EMA and no stop-gradient. Against V-JEPA 2 it claims comparable or better results at **5.6–20.8× less pretraining compute**.

His framing is the one to keep: *"this is really the very beginning of us starting to have reliable pre-training solutions where we can finally become more sample efficient, more FLOP efficient."* And he is careful about what it is when asked directly — *"it is a video encoder that gives you a very strong embedding Z on which you can learn an action-conditioned predictor to do world modeling."* **LeVJEPA is not a world model; it is the encoder half.**

Three limitations he volunteers at the end:

1. **Single modality.** *"All current models overfit to vision"* — including audio models, which are audio-only. A lab paper (hardware rig on a car, driven around Philadelphia) finds **video-only self-driving world models degrade sharply at night**, and that an MAE-style *reconstruction* model with extra sensor streams beats the vision-only V-JEPA state of the art. **There is currently no JEPA-family pretraining objective that handles multiple streams gracefully.** A companion toy study on prediction direction across modalities finds it is *"not as simple as saying we just predict everything from everything"* — noisier or poorer modalities bottleneck the embedding.
2. **Noise.** DINOv2 out of the box degrades in accuracy *and* convergence speed under input noise, with unfavourable scaling — *"if you have two times worse SNR you need like four times more compute."* Their fix is a **curriculum over noise levels**, using synthetic clean data to restore the noiseless convergence rate. Aimed at the finance audience; relevant to any sensor-limited robot.
3. **Stochastic and partially observed environments.** Everything shown assumes near-full observability and near-determinism, *"or the thing that is not deterministic is what you actually don't care to capture."* Doing better is named as open.

---

## Steve Bravo — Institutional-Grade Market Data (02:03:12)

A 20-minute vendor talk from **[Massive](../entities/massive.md)** (formerly Polygon.io), the data partner behind [MarketOne](../entities/marketone.md). Substance for the wiki is mostly the shape of the agent-facing tooling rather than the market data:

- Delivery is **REST, WebSockets, flat files, and now MCP**. They have shipped **x402** support so **agents can buy market data per request without a subscription or API key**.
- Direct SIP connections (UTP, CTA for equities; **OPRA** for options — *"probably the largest financial dataset in the world"*), plus indices and a new CME futures partnership.
- A research team building derived datasets, e.g. **event tags extracted from SEC 8-K filings**.

> [!note] The failure mode he describes is the one this wiki keeps meeting
> Asked about agents on raw market data: they *"pull all the data, get confused, and hallucinate."* His colleague's agent loaded a series into context and reported no signal until a human overlaid the analytic frame. Their response was to make **the MCP server token-efficient so the agent has to choose what to pull** rather than defaulting to everything. Same lesson as the [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) material: retrieval discipline is the product.

An academic in the room makes the more interesting point unprompted: finance research typically needs **~10,000 observations in narrow windows around information events**, and has historically paid a cluster-computing tax (WRDS, TAQ) to get them. A REST API that returns exactly the event windows removes that tax — *"it was like ten lines of code."*

---

## Tutorial 2 — Bradford Levy, *Financial Data: Challenges, Evaluation, and Training* (02:21:49)

[Levy](../entities/bradford-levy.md) is an engineer turned accounting professor, and he sets out to translate: *"I saw a lot of common math but different English words around that math."*

### The measurement that motivates everything

Time-series foundation models ([TimesFM](../concepts/learning/time-series-foundation-models.md), now on v4; Chronos, now v2; Sundial) assume the past predicts the future — formally, **nonzero mutual information between representations of different time periods**. He tests it: push consecutive periods through a time-series foundation model, extract representations, and estimate mutual information between them with the **SMILE** estimator, across domains.

**Electricity demand, weather, traffic, dynamical systems: high. Finance: markedly lower than all of them — but not zero.** This was prompted by a hallway conversation with XY Han (*"surely we can empirically measure this, right?"*) and it is the cleanest empirical statement in the wiki of *how much harder* finance is, rather than an assertion that it is harder.

### Why, in two economics results a CS audience can use

- **Rational expectations equilibrium.** Traders get private signals about an asset's terminal value and trade. *Ex ante*, mutual information between your signal and terminal value can be positive. *Ex post*, price aggregates every signal, and given price your signal is worthless. *"You interacting with the market… it's changing and it's adapting."*
- **Grossman–Stiglitz (1980).** Information is costly, so agents *endogenously* choose whether to become informed; only a fraction do; **price therefore cannot fully reveal private information**. The market is *"efficiently inefficient."* Predictability exists in pockets (**post-earnings-announcement drift** is his most robust example), news is priced in *"hours or days"* rather than weeks, and *"this is what people mean when they say financial data are noisy"* — strong-signal periods are **rare**, not absent.

His analogy for the room is the sharpest sentence of the day and belongs next to the wiki's [reflexivity](../syntheses/society/world-models-for-financial-markets.md) material:

> *"Imagine if the friction coefficient in [Push-T] was adversarially changing to try to mess with the robot. That's more of the type of environment that we're dealing with in financial markets."*

Asked whether a working model destroys its own edge, he answers with Grossman–Stiglitz rather than denial: *"if this thing works, people will start to use it, markets will become more efficient, the actual trading profits will decline… but you've got to run this on a GPU, you've got to purchase the data"* — so the equilibrium is more efficient, never perfectly efficient.

### The augmentation problem — the transferable methodology

To train a JEPA on markets you need to say what "two views of the same thing" means. He walks through what they tried and *why each one is wrong or right*, which is recorded as its own concept page: **[financial time-series augmentations](../concepts/economics/financial-time-series-augmentations.md)**.

The reasoning worth repeating here, because it is a template rather than a result: under a factor model `r = βᵀf + ε` where `f` is time-specific, **random resized crop takes its two views from different time periods**, so the invariance the encoder learns *must be time-independent* — bid-ask spread level, typical order sizes — and **cannot, by construction, be the latent factor structure**. They saw this empirically and then saw it was obvious. **Cross-stock** (same window, different tickers) fixes it: whatever is common to Apple and NVIDIA at 10:00 on Tuesday *is* a common factor.

**Time warping won on return prediction and he says he expected it to lose** — squeezing and stretching the clock seemed likely to destroy economic structure. Interpretability afterwards suggests it *"forces the model to focus more on volume"* and smooth price noise. The encoder he ships was trained with time warping alone; he notes vision practice would stack all of these probabilistically.

### What is released

- **[Market-JEPA](../entities/market-jepa.md)** — a **22.3M-parameter** encoder mapping a 20×450 market-state tensor to a **384-dimensional** embedding, trained on a **single month of 2016 data**, **MIT licensed**, on Hugging Face. Performance decays slowly enough to be useful years out of sample; scaling studies are in the paper.
- **[MarketOne](../entities/marketone.md)** — the dataset, streamed rather than downloaded, hosted with Massive.

The aggregation argument is his own contribution to the SSL case and is worth keeping: a regular trading day is **23,400 seconds**, and finance has always compressed it with **open/high/low/close** — a rule nobody chose on evidence. *"It seems a little goofy to me… maybe we can learn a different aggregation rule"*, one that is not identical across intervals *"when clearly not all time intervals are created equal in terms of predictivity."*

Four challenge tasks, ordered easiest to hardest: **(1)** probe the embedding for asset risk exposure; **(2)** an event study (COVID disclosure — Starbucks was among the first firms to warn); **(3)** **spoofing detection**, where their paper reports an identifiable signature of manipulation; **(4)** find persistent predictability and make money — deliberately last.

---

## Amir Zadeh (Lambda) — Scaling GPU Infrastructure (04:32:59)

The most robotics-relevant talk of the day, and the reason this source matters outside finance. Full treatment on **[simulation economics](../concepts/world-models/simulation-economics.md)**; the outline:

**Opening result — [Sim2Reason](../entities/sim2reason.md)** (ICML 2026, Lambda × CMU). An LLM writes scene descriptions into **MuJoCo**; the simulator produces forces, velocities and accelerations; a second pipeline turns those traces into verified question–answer pairs; a model fine-tunes on them. Gains on **International Physics Olympiad mechanics** hold across **3B–72B** models, closing much of the gap to frontier models trained on curated human expert data. And it **transfers to mathematics** — *"a physics simulator generating data that makes you do better in math."* His term for this is **correlated frontiers**, and his framing is that **synthetic data has been neglected and is about to stop being**.

**The core content — what a simulation costs.** Take 100,000 environments × 1,024 runs each × 90-second rollouts on a B200 at ~$6–7/hour, and ask *how many simulation-seconds per GPU-second*:

| Scene | Sim-seconds per GPU-second |
|---|---|
| Static warehouse (shelving, pallets), one Unitree G1 | **~100** |
| Same, with articulation | **~50** (cost doubles) |
| Rubble or forest | lower again |
| **+ lidar and camera with RTX rendering** (RTX PRO 6000 Blackwell — *"B200 doesn't render"*) | **~1** |

That last row is the finding. **Turning the sensors on costs about two orders of magnitude**, and *"G1 in a forest plus lidar plus camera — I'm not asking for too much."* The dollar figure he quotes for that cell runs to **millions per experiment** (the ASR gives both $5M and $45M; the order of magnitude is the claim), and his target is breaking it by 10×.

**Three unsolved problems he names for the community, not for Lambda:**

1. **How do you know a simulation is good?** Learning signal is high early and decays; *"the goal becomes how do I hunt down those fresh gradients."* And the metrics are **task-dependent** — a legged robot and a quadrotor do not share one.
2. **Data, not compute, may be the binding constraint.** Simulation output must be **streamed** during training and **indexed** afterwards — *"give me all the instances where there's a cat crossing the street"* — because regenerating is what you are trying to avoid. *"These have cost you a lot of money to generate."*
3. **Heterogeneous cluster orchestration.** Render GPUs feeding training GPUs, with no general answer to which side throttles: *"there's no orchestration that is globally applicable, there's no playbook on how to build these clusters."*

> [!note] The incentive question was asked directly, and the answer is worth recording
> An organizer: *"as a provider you'd benefit if we never solve this — like, we pay you more. What's the symbiosis?"* Zadeh's answer is a market-growth argument, not a values argument: *"it's far more lucrative for us if this becomes mainstream and everybody is successful, as opposed to this bringing in revenue for one year and then the next year everybody's like 'I'm never doing this again.'"* He then puts a concrete offer behind it — Lambda research grants, *"if it is connected to world modeling it very likely will get funded"* — and Lambda part-funded the workshop. Read it as a vendor talk with a disclosed interest, which is the honest version.

---

## The modeling challenge (05:16:35) and its presentations (07:03:09)

Two hours, no obligation, volunteer presentations — *"there is no pressure to present what worked only. If you tried things and it did not work, it's actually pretty useful."* Seven presented. Filed because **this is the only place in the wiki where naive users hit these models cold**, and the failure modes are informative out of proportion to the effort behind them:

| Who | What they tried | Outcome |
|---|---|---|
| Ahmed | Extra SIGReg "arm" over type-only and time-only market features | **Didn't work**; assumptions about what was already in training were wrong |
| (turbulence background) | Two-point autocorrelations + spectra on the raw MarketOne data before touching a model | No model yet; planned as summary statistics feeding a foundation model |
| Sean (incoming MBA) | Nearest-neighbour trading: embed a firm, look at its 10 neighbours' realized `t+1`, trade the discrepancy | Three strategies backtested on a tiny sample in ~45 min; explicitly *"non-peer-reviewed"* |
| (unnamed) | LeWM on **Atari Breakout**, playable | Paddle responds; **the ball never reconstructs** and blocks confuse it. His own diagnosis: **64-dimensional latent, more than 64 blocks** |
| Janing (incoming MCSS) | Does latent proximity predict similar futures? Market-JEPA vs a 32-d PCA baseline, "neighbour advantage" over random controls, block-bootstrapped CIs | **Positive and decaying** for both; Market-JEPA above PCA-32. Proposes a **"representation half-life"** |
| (team) | Swap SIGReg's isotropic Gaussian target for **multivariate Laplace** and **Student-t**, on MNIST and on UrbanSound audio | **Gaussian beat both, by a clear margin** |
| (LeVJEPA author) | DINO-WM-style predictor on **frozen LeVJEPA features**, MineRL navigate, interactive rollout | Learns navigable structure in minutes on frozen features; blurry at 64×64 |

Three of these are worth more than a hackathon note:

> [!note] The Laplace/Student-t result is a free ablation of the isotropic-Gaussian claim
> [SIGReg's](../concepts/world-models/sigreg.md) Gaussian target is defended by two theorems (minimax risk; unique linear identifiability) and challenged by [LpWM](../entities/lpwm.md)'s sparse Rectified-Generalized-Gaussian target, which reports **+24–57%** on Push-T. A team with a couple of hours and MNIST found **Gaussian clearly best** against two heavier-tailed alternatives. That does not settle anything — different task, different scale, no tuning — but it is the first attempt in the wiki at the ablation Balestriero explicitly invited, and it went the theory's way. Balestriero's own live position: *"in terms of performance it does not seem to matter so much as long as you feed the distribution in a nice way"* — the hard part is the **matching mechanism**, not the target.

> [!note] The Breakout failure is a capacity bound, not a JEPA failure
> A 64-dimensional latent cannot index more than 64 destructible blocks, so block state is unrepresentable regardless of objective. Compare the tutorial's own Moving-MNIST result — **position near-perfect, identity mushy** — and [LeWM](../entities/leworldmodel.md)'s design intent. An action-conditioned latent keeps what actions move; here that is the paddle, and the paddle is exactly what worked.

**Janing's "representation half-life"** is the most reusable idea produced by the challenge: measure how far into the future latent-space neighbours remain predictive, relative to random controls with the same intraday anchor. It is a *representation-quality* metric that needs no decoder, no planner and no labels — precisely the gap Balestriero named that morning. Presented as exploratory, with the right caveats (three horizons, one seed, PCA-32 not claimed optimal), and built *"only with the help of Codex"* in 45 minutes.

---

## Kawin Ethayarajh — closing remarks (07:33:02)

[Ethayarajh](../entities/kawin-ethayarajh.md) takes on the question the workshop never resolved — *what is a world model?* — historically rather than by definition. Recorded in full on the [world model](../concepts/world-models/world-model.md) concept page; the shape:

**Three eras of the term.**

| Period | "World model" meant |
|---|---|
| 1940s–1980s | A **symbolic description** of the world, typically **specified by hand** |
| 1980s–2010s | A **probabilistic model** of how the world changes |
| 2012– | A **deep network** predicting observations, consequences, and/or affinities between states |

with [LeCun](../entities/yann-lecun.md) holding a narrower fourth position: a neural world model that is **separate from any actor in that world**.

**The prehistory**, which the wiki had nothing on:

- **Epictetus, c. 125 CE** — *premeditatio malorum*: rehearse the rowdy bathhouse in advance and you can *"enjoy bathing unperturbed."* Offered as the earliest thing resembling planning against an internal model.
- **Tolman's rats** — trained on a direct path, then given a maze where that path is sealed; **38%, a large plurality, take the direct route to the reward**, having built a **cognitive map** rather than a policy. (The wiki carries the Tolman–Honzik latent-learning argument via [David Klindt](../entities/david-klindt.md).)
- **Winograd's SHRDLU (1970)** — a near-perfect model of a tiny world, natural-language block manipulation, and even a mechanism for admitting ignorance (*"I don't know what a steeple is"* → be told → *"okay, I get what a steeple is"*). His verdict is pointed: *"much in the way of LLM psychosis nowadays, people were really amazed by this program"* and concluded scale would finish the job. *"Turns out this was kind of a dead end, but it was still a very important milestone."*
- **Cyc** — *"scale ontologies the hard way, one relation at a time"*; reasoning worked, encoding did not scale.
- **Pearl** on probabilistic reasoning; **Sutton's Dyna**, which he correctly identifies as *"in many ways resembling the kind of world model setups we see today"*; and **HMM part-of-speech tagging** as the era's language-side artifact.

**Then 2012, and the fork.** He gives the deep-learning premise as Sutskever's — *"make the whole world in distribution"* — and splits the response into two columns:

- **Scaling language** — humans have a world model, it is crystallized in language, predict the next token. word2vec → LLMs.
- **Scaling experience** — you have to go into the world or a simulation of it. MuZero, Tesla Autopilot, **XLand**. And a claim the wiki should chase: **DeepMind's bet on scaling experience is part of why Google was behind on language models.**

Today's synthesis is all four cells — real and synthetic × language and experience — with **humanoid robots in homes** named as the real-experience collection strategy, *"as slightly terrifying as that might be."* His summary of the prevailing view is **Amodei's "big blob of compute"**: whether data is real or synthetic, language or experience, *"is secondary to ultimately growing this blob."*

**Three open questions he leaves the field:**

1. **Explicit vs implicit.** Is an implicit world model learned through language enough, or is an explicit one necessary — *"and could we resolve this using theory?"*
2. **Latent vs observation space.** LeCun's position (latent) is *"an unresolved debate."*
3. **Adaptation.** *"The world is constantly changing, and moreover, as we release more and more AI into the wild, the world is going to adapt in response to the rise of AI."* Can a world model be adapted fast enough?

> [!note] Question 3 is Day 2's reflexivity problem, restated as an ML problem
> [Day 2](chicago-booth-world-modeling-workshop-2026-day2.md) surfaced reflexivity in markets — the modelled system changes because it is modelled. Ethayarajh generalizes it past finance: **as AI drives more activity, every domain acquires the property that made finance hard.** The wiki's [world models for financial markets](../syntheses/society/world-models-for-financial-markets.md) synthesis is, on this reading, an early case study rather than a special case.

---

## Entities mentioned

- [Randall Balestriero](../entities/randall-balestriero.md) · [Bradford Levy](../entities/bradford-levy.md) · [Kawin Ethayarajh](../entities/kawin-ethayarajh.md) · [Yann LeCun](../entities/yann-lecun.md) · [Lucas Maes](../entities/lucas-maes.md) · [David Klindt](../entities/david-klindt.md)
- [Lambda](../entities/lambda.md) · [Massive](../entities/massive.md) · Brown University
- [LeVJEPA](../entities/levjepa.md) · [LeWorldModel](../entities/leworldmodel.md) · [Market-JEPA](../entities/market-jepa.md) · [MarketOne](../entities/marketone.md) · [Sim2Reason](../entities/sim2reason.md) · [Dreamer](../entities/dreamer.md) · [SMWM](../entities/smwm.md) · [LpWM](../entities/lpwm.md) · [DINOv2](../entities/dinov2.md) · [V-JEPA 2](../entities/v-jepa-2.md) · [Unitree G1](../entities/unitree-g1.md) · [Isaac Sim](../entities/nvidia-isaac-sim.md) · [MuJoCo](../entities/mujoco.md)

## Concepts touched

- [SIGReg](../concepts/world-models/sigreg.md) · [JEPA](../concepts/world-models/jepa.md) · [world model](../concepts/world-models/world-model.md) · [latent space](../concepts/world-models/latent-space.md) · [world-model evaluation](../concepts/world-models/world-model-evaluation.md) · [identifiability](../concepts/world-models/identifiability.md) · [gradient-based planning](../concepts/world-models/gradient-based-planning.md)
- [simulation economics](../concepts/world-models/simulation-economics.md) · [the synthetic flywheel](../concepts/learning/synthetic-data-flywheel.md) · [sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md)
- [financial time-series augmentations](../concepts/economics/financial-time-series-augmentations.md) · [time-series foundation models](../concepts/learning/time-series-foundation-models.md) · [asset embeddings](../concepts/economics/asset-embeddings.md)
- [spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md) · [inductive bias](../concepts/learning/inductive-bias.md) · [generative data augmentation](../concepts/learning/generative-data-augmentation.md)

## Open questions

- **What is the Philadelphia multimodal driving paper?** Balestriero describes a lab rig on a car, a video-vs-multimodal comparison, night-time degradation, and an MAE-based multimodal model beating vision-only V-JEPA. Not identified against arXiv — searches surface adjacent JEPA/lidar driving work but nothing matching this description. Worth finding: it is a **reconstruction method beating a JEPA**, from the JEPA line's own author, which is a genuinely awkward result for the morning's argument.
- **Does the "DeepMind was behind on language because it bet on experience" claim survive checking?** Stated confidently in the closing remarks; the wiki has no source for it.
- **The four SSL-theory papers named** (Birth of Self-Supervised Learning; relational representation learning under graph noise; X-CLR; a recent summary) are none of them ingested. The graph-specification framing is the most portable idea in the tutorial and the wiki holds only the [IEEE SPM review](spectral-graph-theory-ssl-paper.md) of the same line.
- **Is "representation half-life" already a named metric?** Janing's neighbour-advantage-decay measure needs no decoder or planner, which is exactly what the field's evaluation problem calls for. Worth checking whether it exists under another name before treating it as novel.
- **Where does the noise-curriculum result generalize to?** A curriculum over synthetic noise levels restoring noiseless convergence rates is directly applicable to cheap robot sensors, and this is the only mention in the wiki.
- **Nothing on this page settles the counterfactual question** the tutorial's submitted title promised. Counterfactual JEPAs remain, in his words, an open research question.

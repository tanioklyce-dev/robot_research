---
title: "Third World Modeling Workshop — Day 2 (Chicago Booth, 2026-09-01)"
type: source
url: https://www.youtube.com/live/j_AujLxYUJc
local_path: raw/2026-09-01-chicago-booth-world-modeling-workshop-day2-transcript.txt
sha256: fe406391c5e75ccdbf2496d490b9ca812ec2f6c7d6b012c24896b1b8f4aaf1f0
author: "Center for Applied Artificial Intelligence (CAAI), Chicago Booth; organized by Randall Balestriero, Bradford Levy, Kawin Ethayarajh, XY Han"
published: 2026-09-01
venue: "Chicago Booth / Gleacher Center — livestream recording, 8h05m"
format: video (livestream) — machine transcript (YouTube auto-captions)
tags: [world-models, workshop, finance, economics, jepa, faust, diyi-yang, koijen, klabjan, kalshi, prediction-markets, user-models, time-series, synthetic-data, transcript, secondary-source]
ingested: 2026-09-02
---

## Summary

Day 2 of the **third World Modeling Workshop**, the sequel to [Day 1](chicago-booth-world-modeling-workshop-2026.md). Where Day 1 was the JEPA/robotics day, Day 2 delivers on the host's framing — *"non-stationary signals, time series, economy, finance, business"* — with three keynotes, a deep-dive, eight lightning talks and a 105-minute **Finance & Markets panel**. Eight hours, and **the most substantive material in the wiki on what happens when you point world-model machinery at a domain that pushes back**.

The day has two spines that never quite meet, which is itself the finding:

1. **A world model of a person** ([Diyi Yang](../entities/diyi-yang.md)) and **a world model of a market** ([Koijen](../entities/ralph-koijen.md), [Airoldi](../entities/edoardo-airoldi.md), [Bruss](../entities/bayan-bruss.md), [Kagan](../entities/kalshi.md)) — domains where the thing being modelled *knows it is being modelled and changes in response*.
2. **[Aleksandra Faust](../entities/aleksandra-faust.md)'s keynote**, which is the clearest statement in this wiki of the position that **realism is the wrong target for synthetic data** — a superset of reality beats a faithful copy — supported across four unrelated domains.

> [!warning] Machine transcript — but names were fixed against a primary
> The transcript in `raw/` is **YouTube auto-captions**, so proper nouns are garbled ("Ego Clavian" for Diego Klabjan, "Cali"/"Kelsey"/"Kouchi" for Kalshi, "japa" for JEPA, "Whimo" for Waymo, "Jan" for Yann). **Every speaker name, title and affiliation on this page was corrected against the workshop's own programme**, archived at `raw/2026-09-02-wm-booth-org-programme.html` (from `wm-booth.org`, captured 2026-09-02 while the site was still live). Timestamps are reliable; quotes are lightly cleaned.
>
> This is the fix for the failure recorded on the [Day 1 page](chicago-booth-world-modeling-workshop-2026.md), where Whisper's "sim tool real" propagated into the wiki as a wrong title. The rule that follows: **a talk-derived source page must reconcile its speaker list against the event's own programme before anything is filed.**

## Programme

Times are video-relative. Titles and affiliations from the workshop programme; content from the transcript.

| Time | Speaker | Talk |
|---|---|---|
| 04:17 | **Diyi Yang** (Stanford CS) | *Optimizing Human-AI Collaboration* — General User Models, Next Action Prediction |
| 54:29 | **Diego Klabjan** (Northwestern IEMS; dir. Center for Deep Learning) | *Time-Series Modeling* — hallucination in time-series foundation models |
| 02:04:23 | **Ralph Koijen** (Chicago Booth, AQR Distinguished Service Prof. of Finance & Applied AI) | *Learning Representations of Assets and Investors* |
| 02:59:58 | Lightning ×4 | [WorldTrace](../entities/worldtrace.md) · [AdaJEPA](../entities/adajepa.md) · [When Does LeJEPA Learn a World Model?](when-does-lejepa-learn-a-world-model-paper.md) · VISReg |
| 04:34:15 | **Aleksandra Faust** (Director of Research, Google DeepMind — Frontier AI Health) | *The Synthetic Flywheel: Self-Improvement and Simulation in Foundation Models* |
| 05:29:33 | Lightning ×4 | DSeq-JEPA · [VTAM](../entities/vtam.md) · [MetaOthello](../entities/metaothello.md) · [MarketOne](../entities/marketone.md) |
| 06:25:55 | **Panel — Finance & Markets** | [Edoardo Airoldi](../entities/edoardo-airoldi.md) (Temple) · [Bayan Bruss](../entities/bayan-bruss.md) (Capital One) · [Nicole Kagan](../entities/kalshi.md) (Kalshi) |

## Diyi Yang — a user model *is* a world model (04:17)

The framing claim, stated flatly at 11:11: **"a user model is actually a world model of a person."** Same decomposition — perceive (observe interactions), model (infer latent goals, preferences, knowledge, habits), predict (anticipate the next action).

She grounds it in a 50-year lineage most ML work skips: the **good regulator theorem** (1970 — "a good regulator must contain a model of" the system it regulates), early general user models, GOMS/KLM from HCI in the 1980s, and **Eric Horvitz's Bayesian mixed-initiative work (1998)** that shipped as Clippy. Her verdict: *"Clippy was a vision that's very ahead of time. It didn't work out as expected because the technology foundation at that time is very thin."*

**Three results:**

- **The grounding gap (12:17).** Take human-human conversations, delete one turn, have a model generate it, and compare *discourse acts* — clarification, follow-up, acknowledgement. Humans produce far more of all three. Isolating instruction-tuning stages shows **SFT is neutral and preference tuning is where grounding degrades**: correlation with human discourse-act usage falls monotonically as preference training proceeds, across models and datasets. And *"the newer models actually do similar or worse."*
- **GUM — General User Models (19:01).** A local model observes any computer interaction and emits **confidence-weighted propositions** about the user, retrieved/merged/revised into a growing bank. Audited through a **contextual-integrity** filter so sensitive material is never screenshotted. Proposition accuracy **~88%** against 18 users' own judgement (27:29), with a deliberately *under*-confident calibration curve — *"if models are very confident, very annoying."* Deployed to five users who installed it on their laptops (28:04).
- **NAP — Next Action Prediction (30:52).** The base-model play: *"next action prediction is what we view as the general base model for this kind of user model."* Trained on Stanford's **Screenomics** corpus (10,000 people recorded for over a month); **1,800 hours of screen use, 1.9M screenshots**. Rather than weight updates, the policy **retrieves relevant past reasoning** for that specific user and does in-context learning — because *"new data should immediately inform the next action prediction"* and weight-based learning is too slow. Reported ~**37%** accuracy, which she defends directly: *"the next action on your laptop, the space is actually infinity."*

The strongest demo (22:54): the model saw her stalled in PowerPoint for five minutes, saw a Slack message asking where her slides were, knew she was a professor who gets slides from students, and **drafted a message to the student** — rather than offering to write slides. *"If you ask AI today... they will be like 'I'm happy to help you finish your slides.'"*

> [!warning] The surveillance objection was put to her directly, and the answer was partial
> An audience member (41:11): *"My students get checked, their phones get checked when they enter the United States... if I pull this and say 'do you support Donald Trump' — that seems like it's opening a whole new bag of words for surveillance. Is locality enough to protect privacy?"*
>
> Her answer concedes the hypothetical (*"if [the system] gets attacked then this kind of thing may get very dangerous"*), notes sensitive content is filtered at capture, and argues the capability already exists via social-simulation models trained on public posts. What it does not do is claim locality is sufficient. She also volunteers the **privacy paradox** unprompted (29:43): *"whenever there are benefits or convenience, despite that people mention that they care about privacy, they actually give up on it"* — and quotes a participant: *"if I didn't know and trust you I would have never installed this."*

## Diego Klabjan — do time-series foundation models hallucinate? (54:29)

Yes, and the paper (NeurIPS, by his PhD student Yifang Zhu) defines it without reference to LLMs at all. The setup is **zero-shot forecasting** with [Chronos](../concepts/learning/time-series-foundation-models.md) and two other time-series foundation models; the motivating example is a clean alternating 0-1-0-1 series that the model forecasts as constant 1.

**Four rule-based hallucination detectors (01:13:11)**, all built the same way — compute a statistic over sliding windows of the context, compute it on the forecast, flag a large gap:

| Rule | Statistic | Notes |
|---|---|---|
| R1 trend | slope of univariate regression per window | |
| R2 frequency | frequency of y-values | |
| R3 relative absolute error | window vs forecast | |
| R4 ARMA(1,1) coefficients | AR + MA coefficient pair | **fires far more often than the others** (01:43:09) |

Then the mechanistic half. Projecting last-layer hidden states with UMAP, **hallucinated samples cluster tightly and non-hallucinated ones are dispersed** (01:23:05) — and the effect *strengthens in higher layers* (01:24:48). So homogeneity of hidden state correlates with hallucination.

The mitigation follows from that: decompose hidden states into **signal** (per-neuron standard deviation across real data) and **noise** (the same statistic computed when the model is fed **pure Gaussian noise** as input — *"keep it simple, stupid"*), then at every layer center, project onto the signal subspace, **amplify the signal component by λ−1 (λ > 1)**, and restore the mean.

> [!note] Honest about the effect size
> Asked to characterise the improvement, he says it twice: *"it doesn't shake the boat... they are better."* Against vanilla Chronos the gain is clear; against the other two models it is small. The wiki should carry this as a **mechanism with a modest effect**, not a fix.

Two limitations he names: the method is **white-box** (needs hidden states — *"completely black box, that's still an open problem"*), and the relationship to causality is unexplored. An audience member reports unpublished work finding **classical statistical models often outperform LLM/deep time-series models** on standard datasets, which he does not dispute (01:49:27).

He also states his position on the workshop's central question outright (01:01:16): *"I know Yann is a speaker here and he believes that LLMs are not going to lead to AGI. I'm on his side — I don't see how hallucinations can be got rid of."*

## Ralph Koijen — portfolios as sentences (02:04:23)

The most transferable idea of the finance half, and the one that treats a market like a corpus.

**The theoretical claim first.** Investors choose portfolios given prices and asset characteristics; supply must be held; markets clear; therefore prices are a function of those characteristics. Substitute prices back into demand and you get the **reduced-form demand system** — holdings alone, reflecting every characteristic that matters for pricing. Conclusion (02:25:28): *"if you want to start learning representations of financial assets, then holdings data contain all the information that's relevant for prices."*

**The method.** Treat a portfolio the way NLP treats a sentence:

| Model | Analogue | Masked-holdings prediction (share of variation explained) |
|---|---|---|
| Observed characteristics (150 accounting/asset-pricing features) | baseline | ~20% |
| Linear recommender system | the micro-founded optimum under standard finance assumptions | ~same as baseline |
| word2vec-style shallow model | mask a position, predict from the rest of the portfolio | significantly better |
| **BERT-style transformer** (masked asset modelling + contrastive sentence-transformer fine-tune) | **contextualized** asset embeddings | **~60%** |

Rotating the data matrix gives the dual: mask *investors* in a firm's ownership list and you learn **investor embeddings**. The contextualization argument is exactly the polysemy argument (02:58:03): *"If I hold Apple in a portfolio with all large-cap stocks I'm going to get a different representation compared to when I hold Apple in a portfolio of all technology firms."*

Details worth keeping:
- **Ranking beats weights (02:33:51).** Information in holdings sits at three levels — do I hold it, where does it rank, and what exact percentage. *"It's really the first two parts that are the most valuable."*
- **Regularization is forced (02:30:59):** the median investor holds only **50–60 stocks**.
- **Scale:** ~1,600 firms per period, ~1M holdings per quarter as training data; household-level datasets (Autopar; Finland's full population) are orders of magnitude larger.
- **Text embeddings cannot explain holdings (02:43:26)**, and observed characteristics cannot either. He reports asking AI labs about training on holdings and being told *"we shouldn't be doing this at all"* because their firm embeddings already carry everything (02:41:45) — the empirical answer is that they do not.
- **Credit application:** embeddings explain yield dispersion *within* rating buckets and predict investment-grade→junk downgrades; re-rating insurers on that basis would move required equity by **~16 percentage points** on average (02:51:14).
- Live at **market-gen.ai**.

His closing question to the room (02:53:28) is the one the ML side never answers: for counterfactuals you need **elasticities** — if a constrained investor is forced to sell, how far must prices move for others to absorb it? *"I would love to know if there's a JEPA-style equivalent to that."*

## Aleksandra Faust — the synthetic flywheel (04:34:15)

The keynote with the widest reach, and the strongest single thesis on this page: **synthetic training environments should be a superset of reality, not a replica of it.** She supports it four times, in four unrelated domains.

She opens on the 1996 nuclear test ban — a decision that forced simulation and high-performance computing into being — as the analogue for AI entering *"high-consequence applications."*

**1. AutoRL navigation (04:38:14).** Two nested optimization loops: an inner loop training the agent, an outer loop optimizing the reward and architecture — *"a person is making sequential decision making, [so] we can have a model that's doing it."* Trained in an office environment of **flat walls and no furniture**, with randomized start/goal and noise injected into sensors, actuators and the kinematic model. Transfers **zero-shot** to a real robot dodging a custodian's cart, and to a **robot 100 lb lighter**, because decisions run at **10 Hz** and the noise training makes it re-adapt continuously. Asked whether the lesson is the bitter lesson, she rejects it explicitly: *"it's not the bitter lesson. The lesson is exactly clean out — use the noisy data. Embrace the noise. Change the initial conditions. Use the right abstraction for the simulator."*

**2. Web-navigation curricula (04:42:50).** A teacher network generates web pages; a population of student agents tries to complete them; the teacher gets the *average* and *best* student's performance and adjusts — lower difficulty if the best student fails, raise diversity if everyone succeeds. Learned curriculum beats a manual one. Two lessons stated generally:

> *"These web pages... don't need to be realistic. It can have three first names if you want, as long as it has that submit button and you can complete the task. But these three first names is a superset of the real distribution."*

> *"Curriculum is nothing else than sampling the same data from the same distribution in different order. Curriculum is a permutation on the data."*

**3. Autonomous driving (04:46:54).** Driving logs have *"giant holes"* — the risky scenarios are rare or absent, and *"you can't set up the sets where you're throwing the kids in front of the car."* Worse, replaying logs is not closed-loop: stop the ego vehicle and the logged cars drive through it. So: train a behavior model from real logs, ship a hardware-accelerated closed-loop simulator (Waymax, open source, decisions at 100 Hz–1 kHz), then train with a **weighted combination of an RL safety loss and behavior cloning for everything else** — *"when the data starts going out of distribution RL becomes more strong, and then otherwise it's behavior cloning."* The result is the argument for the hybrid: **RL alone "slams the brakes or accelerates as fast as it can, because that's what it does"**; the combined agent's deceleration distribution matches the human one while failing less on critical scenarios.

> [!note] This is the concrete answer to Day 1's imitation-learning argument
> On [Day 1](chicago-booth-world-modeling-workshop-2026.md), LeCun said *"imitation learning has been a failure for driving"* and *"reinforcement learning is a complete no-no in the real world."* Faust's talk answers both with the same system: RL for the tail where no data exists, imitation for the *hows* that are hopeless to specify as reward — *"how you brake, how you turn, how you have the conversation, all these hows do matter and they're very very difficult to encode into the reward."* Neither pure position survives her result. See [imitation learning](../concepts/learning/imitation-learning.md).

**4. Molecular structure prediction (04:55:13).** The whole field has ~**200,000 crystal structures**. They generated **>500,000 synthetic structures from physics models** — *"does not need to be realistic... as long as it's plausible"* — until synthetic data was **two-thirds of the training mix**, with performance rising as the synthetic share grew. Stated as *"the first model that outperformed AlphaFold 3"* as of October the previous year, and the advantage *widens* under the stricter metric real drug programmes need (**RMSD < 1 Å**, not < 2 Å, because mirror-image atom placements sneak through the looser threshold).

**Then the self-improvement half:**

- **LLMs as world models of human personality (04:59:50).** With Oxford psychometricians: larger, instruction-tuned models exhibit **consistent Big Five personality traits**, steerable across nine levels, and the steering **survives into downstream tasks** (prompt a personality, generate social-media posts, reverse-infer the personality from the posts). Against human baselines the models are *"more exaggerated... a more cartoonish version."* Her careful phrasing: *"We're not saying that they have personalities. They exhibit behaviors that mimic human personality traits."*
- **Many-shot in-context learning (05:06:03).** Going from 32-shot to 500-shot keeps improving, and *"we can correct the pre-training biases"* — train that blue is red with enough in-context examples and the labels flip. **Context becomes an environment** subject to the same learning laws as training. And **unsupervised ICL and model-generated ("reinforced") ICL beat supervised ICL** (05:07:11), transferring from math to GPQA. Her hypothesis: *"the human-provided solutions are way out of distribution for the model... when it proposes its own solution, it's closer to its own distribution that it can learn from."*
- **Self-correction (05:14:37).** Naive self-correction fails twice — distribution shift from SFT labels, and models becoming conservative and refusing to change answers. Fix is a **two-stage RL**: first keep answer 1 close to the original while rewarding improvement in answer 2; then improve answer 1 too. Trained on two turns, it **extends to 32** and keeps improving, and **beats parallel best-of-N at equal inference budget** (05:18:04).
- **Clinical triage (05:18:36).** An LLM simulates patients — demographics, a *prompted personality*, a case summary, and **things they won't volunteer** (forgotten, embarrassing, not thought relevant). A multi-turn RL agent runs up to **60-step dialogues** with tool use against a reward of **70 rubrics written by physicians**. In clinical trials with Included Health, **5,000 patients** across the US. Asked why not just train on recorded doctor-patient logs: *"if you have logs this is the static data. This is the offline, and we know that that collapses."*
- **Levels of AGI (05:23:08).** Two axes — performance (none → superhuman) against scope (narrow → general) — crossed with a second grid of *how the technology is used* (tool → consultant → collaborator → expert) and the societal risk at each rung (deskilling → overreliance and targeted manipulation → rapid societal change and labor displacement). Her aside is the honest part: **the slide is 2½–3 years old and she has not had to update it.** *"I'm waiting for when I need to update it."*

## The Finance & Markets panel (06:25:55) — three incompatible answers

### Edoardo Airoldi (Temple) — the data has eight layers, and you should hardcode the rules

Opens with a definitional cleanup worth importing (06:27:03): people say "world model" to mean at least four different things, and *"when you read papers about world models, try to figure out which bin you fall in."* His own: *"a mechanistic model — what you would think of as a mental model — good enough to explore what-if scenarios conditional on actions, and capable of producing counterfactuals."*

Then **eight layers of financial data** (06:28:11), each a different observable: line charts → OHLCV bars → individual trades → the order book → order packets → **co-location** (the same packet timestamped from different physical locations) → the network path from your machine to the exchange → the exchange's matching engine and queue. His note on the last: the time an order is *received* is meaningful; the time it is *processed* is not, being an artifact of queue depth.

His architectural recommendation, repeated three times: **hybrid.** *"Hardcode stable aspects of the system — the exchange mechanics, accounting identities, lots of the rules — and then learn the flow dynamics on top. You don't have to learn everything."*

And the reflexivity warning stated as a property of the object, not a nuisance (06:34:24): *"once you learn a world model for the financial system and you start implementing policies based on that world model, the world model will change under your feet."* This is **alpha decay**: *"three weeks, three months later, that representation starts to change."*

Two epistemics he offers that generalize far past finance:

> *"Prediction implies structure? Somewhat... the symmetry is always broken, there's so many idiosyncrasies in the data that you cannot really assume that you learn the structure because you're good at predicting certain observables."*

> *"Realism does not imply validity... there's so many mechanistic models that are compatible with us being able to match the observables. It's kind of hard to assume that you understand anything if you can just have a realistic simulator."*

His proposed way out is **benchmarks built from agent-based simulators (ABIDES)** where intentions are known by construction and deliberately withheld from the model — so ground truth exists for the latent variable you actually care about. His model for the field is **CASP**: twenty years of community datasets, benchmarks and competitions before AlphaFold could exist.

### Bayan Bruss (Capital One) — the evaluation problem is the whole problem

Starts philosophically, and the room liked it enough that Booth faculty texted the moderator about it: money is *"a system of mutual trust... a complete figment of our collective imaginations,"* and it is created from nothing when a bank decides to make a loan. The economy itself *"is completely unobservable. I can't walk outside and say okay, that's the economy."*

His spec for a consumer-finance world model is a **two-level correctness requirement**: accurate per-person prediction *and*, when individual models are aggregated, recovery of known macroeconomic dynamics. Plus horizons machine learning does not think in — *"a mortgage... 30 years to pay me back. That is a time scale that machine learning doesn't typically think about."*

Five challenges, of which he declares four tractable:

1. **Representation** — tabular + temporal + semi-structured clickstream + unstructured documents, jointly.
2. **Partial observability, twice over** — you cannot see inside a person, and *"no one financial institution can see all of the participants in the economy."*
3. **Non-stationarity with reflexivity** — *"the environment itself, if you consider the environment to be the person you are interacting with, they know that they are being modeled... and they change depending on what they think of your own beliefs about them."*
4. **Steerability** — not just steering the policy but **changing the environment's rules**: *"how would my policy operate under a financial crisis? How would my policy operate under GDP rips and goes to 16% per year because AI is making everybody so much money?"*
5. **Evaluation** — *"the hardest problem here."*

> [!warning] The evaluation circularity, stated cleanly
> World-model evaluation reduces to two families: **reconstruction** and **task-based**. Consumer finance can't use reconstruction usefully, and task-based needs a simulator it doesn't have — so it uses **back-testing**: replay a historical trajectory, swap in the new policy, aggregate realized outcomes. But back-testing *"scores the policy using historical outcomes which assume that the state didn't change under the new policy. But that's exactly what we're trying to ask."*
>
> Hence: *"If I had a good world model, I could simulate the economy and I could test any policy — but how do I know if my world model is good if I don't have a simulator? And there's no way out of it."*
>
> His partial escape is **deliberate off-policy data collection**, which has to have been started years earlier: *"You can't just do it today because a lot of this data takes a long time to mature."* Compare [world-model evaluation](../concepts/world-models/world-model-evaluation.md), where the same circularity appears as *teaching to a flawed test*.

Two more: the **time-travel problem** — *"very very subtle choices you make in how you do the evaluation end up vastly inflating what you think the quality of your decisions are"* — and the observation that in this domain the rare events are simultaneously the only ones that matter and the sparsest thing in the data.

Asked (05:37:44, by Balestriero) what the **ImageNet of finance** would be, he concedes there isn't one, describes a released synthetic benchmark (**PersonalLedger** — NVIDIA's 100,000 census-matched personas, expanded by an LLM into grounded transaction histories), reports that **longitudinal fidelity of the synthetic generation was the hard part**, and makes an offer: *"I think we can't release our data, but I will tell you what the benchmark needs to have if it's going to unlock more research."*

### Nicole Kagan (Kalshi) — a calibrated world model that contains no neural network

The sharpest reframe of the day (07:12:18): a world model is a system that turns a partially observed environment into a compact updatable representation sufficient to predict what happens next — *"and what I want to argue today is that actually such a system already exists, at scale, and it exists outside of any machine learning representation or neural network."*

The argument: an equity price is a **compound object** (uncertain cash flows, discount rate, risk preferences, frictions), so recovering a clean probability from it requires unwinding all of that. An **event contract** is an Arrow–Debreu security whose price *is* a probability by construction, and mispricings are arbitrageable, so the incentive to correct them is endogenous. Against polling: *"they might tell you what they think you want to hear... What they're unlikely to tell you is what they think will actually happen."*

The evidence is a **calibration study over 2.2 million resolved markets** across the exchange's full 2021–2026 history — described as the first on the complete resolved history of any US regulated exchange:

| Finding | Number |
|---|---|
| Brier score, 3-month horizon → market close | **0.08 → 0.02** |
| Uninformative-forecaster benchmark | 0.25 |
| Reliability diagram | tracks the 45° line closely, **across categories** |
| Calibration vs. market depth | improves near-monotonically with volume and unique traders |
| **Volume needed for good calibration** | **~$10,000 at the event level** → Brier ≈ 0.1, *"up with the best forecasting models across fields like meteorology"* |
| Users who never trade | ~75% |

Her actual proposal to the room: the resolved-market history is *"a real-time, adjudicated and incentive-disciplined dataset against which forecasting competence of any learned world model is able to be directly benchmarked"* — and the marginal cost of listing a new contract is ~zero, so she will **list markets researchers ask for**, including conditional ones. All data is free through a public API.

> [!note] This is an answer to Airoldi's and Bruss's problem, and nobody in the room connected it
> Airoldi wants benchmarks with known ground truth; Bruss says evaluation is unsolvable without a simulator. Kagan is offering **2.2M resolved, incentive-disciplined, externally-adjudicated forecasting instances with realized outcomes** — an evaluation surface that requires no simulator because the world already ran the experiment. The panel discussion moves on to other things. See [prediction markets](../concepts/economics/prediction-markets.md).

Pressed on sports dominating volume, she pushes back rather than conceding (07:50:36): a fan who has followed a team for 28 World Cups is not obviously less informed than a hedge-fund researcher on short rates — *"maybe if people wore suits it would be a little bit different in the way that they're perceived."*

### Panel Q&A — the Lucas critique (07:59:26)

An audience member raises the **Lucas critique** (past data cannot predict future behavior once policy changes, because agents re-optimize) and adds a second objection: economics has a *cultural and metaphysical* component — citing Joel Mokyr on culture and economic growth — that is not a closed sandbox.

Nobody claims otherwise. The three answers, which is the useful part:

- **Airoldi:** the same is true of robotics sim-to-real — you build the sandbox anyway and find out how much the extra noise matters. *"I'm not going to be stopped by the fact that there's some extra noise."*
- **Bruss:** *"I think black swans are real... whether or not [the Lucas critique] is true isn't a binary. It's: for how long is it true?"* — plus *"the only thing you can fully count on is that an assumption you made will turn out to be wrong,"* which is why steerability and monitoring are load-bearing, and *"the real trick is to not be so wrong that it's your last trade or your last loan."*
- **Airoldi again, on scope:** *"What is the goal? If the goal is to learn something from this exercise, we're definitely going to learn something. If the goal is to have fully automated traders, that's probably not going to happen."*

## The lightning talks

**Session 2 (02:59:58).** Two of the four are already in the wiki as papers — [AdaJEPA](adajepa-paper.md) (Ying Wang, NYU) and [When Does LeJEPA Learn a World Model?](when-does-lejepa-learn-a-world-model-paper.md) (David Klindt, CSHL) — so the talks are corroboration plus a few new details:

- **[WorldTrace](../entities/worldtrace.md) — "Addressable Memory for Video World Models"** (Xindi Wu et al., NVIDIA; presented by Aljoša Ošep). New to the wiki. Diagnoses long-rollout drift in interactive video world models as **two coupled failure modes**: *addressability* (RoPE offsets grow past the training context, so frames remain in the KV cache but can no longer be addressed) and *content fidelity* (averaging rotated embeddings makes phases cancel). Fix is training-free: a fixed-size summary cache plus a recent window, where **summary slots are assigned fixed *virtual* positions relative to the current query** so they never leave the training context regardless of rollout length.
- **AdaJEPA** adds one number the [wiki's page](../concepts/learning/test-time-adaptation.md) listed as an open question: adaptation costs **~0.3 s per replanning step**, *"very small compared to the planning time."*
- **Klindt** adds the empirical scaling comparison and, more interestingly, a **behavioral prediction from the theory**: citing Tolman & Honzik's 1930s latent-learning maze experiments (rats that explored freely find relocated food faster than rats always run to the goal), he argues **goal-biased training data produces a worse map**. Demonstrated on a robot reaching task: a model trained on exploratory random-walk data follows *"the shadow of the correct solution"*, while the goal-focused one overshoots and corrects.
- **VISReg** (Haiyu Wu, Balestriero, Morgan Levine — Altos Labs). Decomposes [SIGReg](../concepts/world-models/sigreg.md)-style regularization into **scale, shape and centre**, separately re-weightable. Claims a stronger anti-collapse gradient, DINOv2-comparable results on ImageNet-22k with **10% of the data**, and better out-of-domain world-model transfer — but only at **large batch size**, because the shape term uses a sliced-Wasserstein distance that is batch-size sensitive. Honest negative: long-horizon open-loop planning still degrades badly from 25→75 steps, and *"I don't think it's a problem of the regularization."*

**Session 3 (05:29:33).**

- **DSeq-JEPA** (Xiangteng He, UBC). Changes *what* and *in what order* [I-JEPA](../concepts/world-models/jepa.md) predicts: use the target encoder's attention to find salient regions, order them primary→secondary, and predict them **sequentially, each conditioned on its predecessors**. The finding that matters: **neither component works alone** — enabling only region selection or only sequential prediction *decreases* performance — and **random or inverse order actively hurts**, with the gain growing as the ordering becomes more semantically meaningful. Holds across ViT-B/L/H and transfers to detection and segmentation.
- **[VTAM](../entities/vtam.md)** (Ismini Lourentzou's group, UIUC). Adapts a pretrained video-action model into a predictive backbone that ingests **tactile images** and predicts visual *and* tactile dynamics before acting — a tactile [world-action model](../concepts/world-models/world-action-model.md) rather than a tactile-conditioned reactive policy. **~10 minutes of teleoperated demonstrations per task**, no separately trained tactile encoder and no wrist force sensor. Tasks chosen for contact dependence (crushable chip, slippery whiteboard wiping); reports predicting future tactile signals *"as faithfully as future video,"* and a higher stable-contact ratio.
- **[MetaOthello](../entities/metaothello.md)** (Aviral Chawla, University of Vermont; presented by a Michigan collaborator). Train 8-layer GPT-style transformers on ~40M sequences **mixed from two Othello rule variants** whose legal-move sequences partly overlap. Three results: all models predict legal moves equally well; **both** candidate board states are linearly decodable, and interventions on them are **causally equivalent** — evidence of one shared base representation with per-world perturbations on top; and the **optimal posterior over which world generated the sequence appears suddenly at layer 5**, where a single latent direction can be used to *steer* which rule set the model applies.
- **[MarketOne](../entities/marketone.md)** (Humzah Merchant, Chicago Booth/Brown, with Balestriero and Bradford Levy). A permissively licensed dataset — top-of-book aggregates and trades for all US equities, **2008–2025, ~1 trillion observations** — built with Massive (formerly Polygon) to fix a field where *"data sets are extremely scattered."* Then an SSL bake-off over 18 method/augmentation combinations. The headline is a **trade-off, not a winner**: the three prediction tasks (return, volatility, spread change) correlate with each other and are **negatively correlated with the "economically meaningful latent organization" tasks**. Multi-head supervised training wins pure forecasting; **the LeJEPA setup wins economic interpretability**; LeJEPA and BYOL with time-warping sit on the efficient frontier between. Regime shifts across the sample are visible enough that evaluating on a single recent year *"gives a very biased estimate."*

## Contradictions and tensions with the rest of the wiki

> [!warning] Contradiction — "realism doesn't matter" vs. "realism does not imply validity"
> **Faust** argues four times that synthetic environments *"don't need to be realistic"* — they need to be a **superset** of the real distribution, and this is what makes zero-shot transfer work. **Airoldi**, three hours later, argues that **"realism does not imply validity"** — a simulator that matches every observable still licenses no claim of understanding, because too many mechanistic models are compatible with the same observables.
>
> These are not actually opposed; they are the same observation used for opposite purposes. Realism is neither necessary (Faust) nor sufficient (Airoldi) for the thing you want. What differs is **what you want**: a policy that transfers, or a model you can run counterfactuals through. The wiki's [sim-heavy vs real-data paths](../syntheses/simulators/sim-heavy-vs-real-data-paths.md) and [world-model evaluation](../concepts/world-models/world-model-evaluation.md) pages both treat fidelity as a single axis; this pair says it is two.

> [!warning] Faust's AV result cuts against Day 1's LeCun position
> Recorded above under her keynote. LeCun's Day 1 claim that imitation learning *"has been a failure"* for driving and that RL is *"a complete no-no in the real world"* is answered by a system that uses both, each where the other fails, with a measured distributional result. Both pages should be read together.

> [!note] Reflexivity is a category the wiki's world-model pages do not have
> Airoldi (*"the world model will change under your feet"*) and Bruss (*"they know that they are being modeled... and they change depending on what they think of your beliefs about them"*) both describe an environment that **responds to the existence of the model**. Every world model in this wiki — [JEPA](../concepts/world-models/jepa.md), [Dreamer](../entities/dreamer.md), video world models, [simulators](../concepts/world-models/world-model-simulators.md) — assumes a world whose dynamics are indifferent to being modelled. Non-stationarity is in the wiki; *strategic* non-stationarity is not.

## Entities mentioned

- **New**: [Diyi Yang](../entities/diyi-yang.md), [Diego Klabjan](../entities/diego-klabjan.md), [Ralph Koijen](../entities/ralph-koijen.md), [Aleksandra Faust](../entities/aleksandra-faust.md), [Edoardo Airoldi](../entities/edoardo-airoldi.md), [Bayan Bruss](../entities/bayan-bruss.md), [Kalshi](../entities/kalshi.md), [WorldTrace](../entities/worldtrace.md), [VTAM](../entities/vtam.md), [MetaOthello](../entities/metaothello.md), [MarketOne](../entities/marketone.md).
- **Existing**: [Randall Balestriero](../entities/randall-balestriero.md) (organizer), [Yann LeCun](../entities/yann-lecun.md), [David Klindt](../entities/david-klindt.md), [AdaJEPA](../entities/adajepa.md), [Google DeepMind](../entities/google-deepmind.md), [NVIDIA](../entities/nvidia.md).
- **No page**: Bradford Levy, Kawin Ethayarajh, XY Han (Booth co-organizers); Aljoša Ošep, Xindi Wu; Xiangteng He; Ismini Lourentzou; Aviral Chawla; Humzah Merchant; Haiyu Wu, Morgan Levine (Altos Labs); Yifang Zhu (Klabjan's student); Capital One; Included Health; Massive/Polygon.

## Concepts touched

- New: [user models](../concepts/agents/user-models.md), [prediction markets](../concepts/economics/prediction-markets.md), [asset embeddings](../concepts/economics/asset-embeddings.md), [time-series foundation models](../concepts/learning/time-series-foundation-models.md), [synthetic data flywheel](../concepts/learning/synthetic-data-flywheel.md).
- Updated: [world-model evaluation](../concepts/world-models/world-model-evaluation.md), [world-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md), [belief states and mixed states](../concepts/world-models/belief-states-and-mixed-states.md), [mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md), [imitation learning](../concepts/learning/imitation-learning.md), [sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md), [test-time adaptation](../concepts/learning/test-time-adaptation.md), [JEPA](../concepts/world-models/jepa.md), [SIGReg](../concepts/world-models/sigreg.md).
- Synthesis: [World models for financial markets](../syntheses/society/world-models-for-financial-markets.md).

## Open questions

- **Klabjan's hallucination paper is not ingested.** NeurIPS, first-authored by Yifang Zhu (Northwestern CS). Everything on this page about the four rules and the signal/noise amplification comes from a talk with slides not visible in the stream — it is a secondary reading of a primary that exists. Worth chasing before any of it is quoted as a method.
- **Faust's four systems each have a paper, and none is ingested.** AutoRL navigation (2018), the web-navigation curriculum work, Waymax, the sub-angstrom structure model (stated as beating AlphaFold 3 in October 2025 — a *checkable* claim the wiki should verify rather than relay), the Big Five psychometrics study with Oxford, many-shot ICL, SCoRe-style self-correction, and ResidencyRL (named in the abstract, not the talk). This is the largest single cluster of un-ingested primaries this source points at.
- **Is anyone doing what Kagan offered?** Benchmarking a learned world model against resolved prediction-market history is, as far as this wiki knows, unattempted. It is also cheap — free API, 2.2M resolved instances.
- **Koijen's elasticity question has no answer here.** Predicting *who buys* is not enough for counterfactuals, because every buyer has a seller; you need to know how far prices must move to clear. No world-model architecture in this wiki represents an equilibrium response.
- **Does the grounding gap reproduce?** Diyi Yang's claim that *preference tuning specifically* degrades clarification behavior is a sharp, falsifiable result with implications for every LLM-agent page here. Paper not identified from the talk.
- **Day 3 is not ingested.** `PkaYC3fwEsc` — hands-on coding workshop with tutorials and a modeling challenge, 2026-09-02 (today). See [backlog](../backlog.md).
- **The Day 1 page's Blackwell date may need a footnote.** Day 1 cites *Blackwell 1957* (Prague proceedings); the workshop's own abstract for that keynote says **"Blackwell's little-known 1956 result."** Almost certainly conference year vs. proceedings year for the same paper, but the wiki asserts 1957 in several places.

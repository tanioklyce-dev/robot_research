---
title: World models for financial markets — why the hard part is evaluation
type: synthesis
created: 2026-09-02
updated: 2026-09-02
tags: [finance, economics, world-model, evaluation, reflexivity, lucas-critique, counterfactuals, benchmarks, prediction-markets, non-stationarity]
---

Synthesized from the finance half of [Day 2 of the third World Modeling Workshop](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md) (Chicago Booth, 2026-09-01) — five speakers who mostly did not talk to each other, and whose disagreements are more useful than their agreements.

The short version: **every technical problem the finance people name has a robotics analogue already covered in this wiki, except one.** That one is reflexivity — an environment that changes *because* it is being modelled — and it is the reason their evaluation problem is not the same as ours, even though it looks identical.

## Who said what

| | Object modelled | Position |
|---|---|---|
| [Ralph Koijen](../../entities/ralph-koijen.md) | assets & investors | Holdings data are *sufficient*; transformers extract them. But prediction ≠ counterfactual without elasticities. |
| [Diego Klabjan](../../entities/diego-klabjan.md) | time series | Foundation forecasters hallucinate; the signature is in hidden-state geometry. |
| [Edoardo Airoldi](../../entities/edoardo-airoldi.md) | market microstructure | Hybrid: hardcode the rules, learn the flows. Realism ≠ validity. Build benchmarks from simulators with known intentions. |
| [Bayan Bruss](../../entities/bayan-bruss.md) | consumer behavior | Four of five problems are tractable; **evaluation is not**, and it is circular. |
| [Kalshi](../../entities/kalshi.md) (Nicole Kagan) | events | A calibrated world model already exists, contains no neural network, and has 2.2M resolved instances you can benchmark against. |

## 1. The evaluation circularity, and the answer sitting three seats away

Bruss states the trap cleanly. World-model evaluation reduces to **reconstruction** (generate more data, check it looks like real data) or **task-based** (train a policy in the model, test the policy). Consumer finance can't use reconstruction usefully, and task-based needs a simulator it doesn't have. So the field uses **back-testing** — replay history, swap in the new policy, score realized outcomes — which

> *"scores the policy using historical outcomes which assume that the state didn't change under the new policy. But that's exactly what we're trying to ask."*

Hence:

> *"If I had a good world model, I could simulate the economy and I could test any policy — but how do I know if my world model is good if I don't have a simulator? And there's no way out of it."*

This is the wiki's [teaching-to-a-flawed-test](../../concepts/world-models/world-model-evaluation.md) problem in its purest form. Robotics has a partial escape that finance does not: **you can put the policy on a real robot.** Expensive, slow, and it doesn't scale — but it terminates the regress. Finance has no equivalent; deploying the policy *is* the experiment, and it changes the thing being measured.

> [!note] Kagan's offer is the closest thing to an exit, and the panel walked past it
> A resolved prediction market is a forecast with a **realized outcome, externally adjudicated, made by people who paid to be right.** No simulator required — the world already ran the experiment. **2.2 million** of them, free through a public API, with **conditional** contracts available on request as priced counterfactuals.
>
> Airoldi, on the same panel, proposed manufacturing ground truth inside agent-based simulators precisely because real ground truth about intentions is unobservable. Bruss, on the same panel, said no benchmark exists and offered to spec one. Kagan was offering an externally-adjudicated one with five years of history. Nobody connected the three. See [prediction markets](../../concepts/economics/prediction-markets.md).

Bruss's own partial escape is worth recording because it is unglamorous and probably right: **deliberate off-policy data collection**, with the sting that *"you have to have done it years ago. You can't just do it today because a lot of this data takes a long time to mature."* The counterfactual capacity of your evaluation is determined by exploration decisions made before you knew you needed them.

## 2. Reflexivity — the category this wiki does not have

Two independent statements of the same thing:

> **Airoldi:** *"Once you learn a world model for the financial system and you start implementing policies based on that world model, the world model will change under your feet."*

> **Bruss:** *"The environment itself, if you consider the environment to be the person you are interacting with, they know that they are being modeled... and they change depending on what they think of your own beliefs about them."*

In finance this has a name and a measured half-life: **alpha decay**. *"Three weeks, three months later, that representation starts to change."*

Every world model in this wiki — [JEPA](../../concepts/world-models/jepa.md), [Dreamer](../../entities/dreamer.md), video world models, [learned simulators](../../concepts/world-models/world-model-simulators.md) — assumes dynamics indifferent to being modelled. **Non-stationarity** is well covered here; *strategic* non-stationarity is not represented anywhere. The distinction matters because the responses differ: non-stationarity is answered by adaptation ([test-time adaptation](../../concepts/learning/test-time-adaptation.md), continual retraining), and strategic non-stationarity is not — adapting faster is a move in the game, and the counterparty adapts to that.

> [!note] It shows up in robotics too, and the wiki has not named it
> [User models](../../concepts/agents/user-models.md) is exactly this case: a household robot's environment is a person who learns the robot's habits and changes their own behavior in response. The finance people have twenty years of vocabulary for it. Robotics does not, and will need it.

## 3. Where the two fields have the same problem under different names

| Finance framing | This wiki's framing |
|---|---|
| "You can't collect the crisis data ethically or at all" | [Long-tail scenarios in AV data](../../concepts/learning/synthetic-data-flywheel.md) — *"you can't throw the kids in front of the car"* |
| "There is no ImageNet for this" | [Robot policy evaluation](../../concepts/robotics/robot-policy-evaluation.md) — no agreed benchmark, every lab reports its own |
| **Time-travel problem** — leaking future knowledge into evaluation | Train/test contamination; the [Physion-Eval](../../entities/physion-eval.md) finding that the judges are unvalidated |
| "Rare events are what we care about and the sparsest thing in our data" | [Runtime failure detection](../../concepts/robotics/runtime-failure-detection.md)'s base-rate problem |
| Back-testing as the only harness | Learned world models as [policy evaluators](../../concepts/world-models/world-model-evaluation.md), with the same flattery bias |
| **Hardcode the rules, learn the flows** (Airoldi) | Hybrid architectures — [safety filters](../../concepts/robotics/safety-filters.md), [behavior trees](../../concepts/robotics/behavior-trees.md) over learned policies |

The last row is the most transferable. Airoldi's recommendation — *"hardcode stable aspects of the system, the exchange mechanics, accounting identities, lots of the rules, and then learn the flow dynamics on top; you don't have to learn everything"* — is architecturally identical to what this wiki's robotics pages have concluded about safety-critical control from a completely different direction. Two fields with unrelated failure modes arriving at the same layering is weak but real evidence for it.

## 4. Two epistemics worth stealing outright

Airoldi's, aimed at his own field and landing squarely on ours:

> *"Prediction implies structure? Somewhat... the symmetry is always broken, there's so many idiosyncrasies in the data that you cannot really assume that you learn the structure because you're good at predicting certain observables."*

> *"Realism does not imply validity... there's so many mechanistic models that are compatible with us being able to match the observables."*

The first is the [Vafa et al.](../../sources/vafa-world-model-implicit.md) result restated as a prior rather than a measurement: a model that scores 1.00 on next-token legality and 0.10 on world-model compression is what "prediction does not imply structure" looks like when you actually measure it. The wiki now has both the theorem and the folk version.

The second is the direct counterweight to [Aleksandra Faust](../../entities/aleksandra-faust.md)'s "it doesn't need to be realistic," and the pair resolves cleanly once you separate the goals: **realism is neither necessary nor sufficient**. Necessary-for-what is the question. Faust wants a policy that transfers, and a superset of reality beats a replica. Airoldi wants a model he can run counterfactuals through, and matching observables is not evidence of the mechanism. Both are right; the wiki's [sim-heavy vs. real-data](../../syntheses/simulators/sim-heavy-vs-real-data-paths.md) framing collapses them onto one fidelity axis and should not.

## 5. The Lucas critique, and the three honest answers

Raised from the audience: past data cannot predict future behavior once policy changes, because agents re-optimize — plus a second objection that economics has a **cultural** component (Joel Mokyr on culture and growth) that is not a closed sandbox.

Nobody claimed otherwise. What they said instead:

- **It's not binary; it's a duration.** Bruss: *"whether or not it's true isn't a binary. It's: for how long is it true?"* Along a trajectory the past does predict; the question is detecting the regime break.
- **The response is monitoring and steerability, not a better model.** *"The only thing you can fully count on is that an assumption you made will turn out to be wrong."* And *"the real trick is to not be so wrong that it's your last trade or your last loan."*
- **Scope the goal.** Airoldi: *"If the goal is to learn something from this exercise, we're definitely going to learn something. If the goal is to have fully automated traders, that's probably not going to happen."*

> [!note] The third answer is the one to keep
> It is the only place in either day of the workshop where someone separates *the world model is useful* from *the world model is a controller*. Almost every claim in this wiki's world-model coverage — [what world models are measurably good for](../world-models/what-world-models-are-measurably-good-for.md) included — would be sharper stated that way.

## What would actually move this forward

Concrete, in rough order of cost:

1. **Benchmark a learned world model against resolved prediction-market history.** Free data, 2.2M instances, realized outcomes, and a calibration baseline (Brier 0.08 → 0.02) that is genuinely hard to beat. Nobody has done it.
2. **Take Kagan and Bruss up on their offers.** She will list contracts, including conditional ones, on request; he will specify what a consumer-finance benchmark needs. Both offers were made to a room and unclaimed.
3. **Build the ABIDES-style benchmark Airoldi described** — agent intentions known by construction, withheld from the model — so "did it recover the latent" is answerable rather than argued.
4. **Name reflexivity as a category on the wiki's world-model pages**, and check which existing claims quietly assume it away.
5. **Find out whether anyone has an equilibrium-aware world model at all.** Koijen's elasticity question — how far must prices move for someone to absorb a forced sale — has no answer in this wiki, and it is the difference between predicting the market and reasoning about it.

## Related
- [World-model evaluation](../../concepts/world-models/world-model-evaluation.md) · [world-model functional taxonomy](../../concepts/world-models/world-model-functional-taxonomy.md)
- [Prediction markets](../../concepts/economics/prediction-markets.md) · [asset embeddings](../../concepts/economics/asset-embeddings.md) · [time-series foundation models](../../concepts/learning/time-series-foundation-models.md)
- [Synthetic data flywheel](../../concepts/learning/synthetic-data-flywheel.md) · [user models](../../concepts/agents/user-models.md)
- [Collectivist AI](../../concepts/economics/collectivist-ai.md) · [mechanism design](../../concepts/economics/mechanism-design.md)
- [Critiques of the intelligence north star](critiques-of-the-intelligence-north-star.md) · [world-model policy vs wiki evidence](world-model-policy-vs-wiki-evidence.md)

## Sources
- [Third World Modeling Workshop — Day 2](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — all five speakers.
- [Third World Modeling Workshop — Day 1](../../sources/chicago-booth-world-modeling-workshop-2026.md) — the JEPA/robotics half the finance speakers were reacting to.

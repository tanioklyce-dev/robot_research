---
title: The synthetic flywheel (supersets, curricula, self-improvement)
type: concept
created: 2026-09-02
updated: 2026-09-03
sources: 2
tags: [synthetic-data, curriculum-learning, autorl, self-improvement, domain-randomization, in-context-learning, self-correction, sim-to-real, waymax, faust, cost, simulation-economics]
---

**The synthetic flywheel** — a world model generates training data for an agent; the agent's exploration produces new data that improves the world model; repeat. [Aleksandra Faust](../../entities/aleksandra-faust.md)'s framing of it at [Day 2 of the Chicago Booth workshop](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md), stated as a design requirement rather than a metaphor:

> *"You need to have a world model, you need to have your training agent that is creating this noisy synthetic data — and that's the flywheel. Your world model is probably trained with some self-supervised methodology, and your training agent needs to have some RL on it, because it needs to be able to go outside of the distribution."*

## The load-bearing claim: supersets, not replicas

**A synthetic environment should be a superset of the real distribution, not a faithful copy of it.** This is the page's reason to exist, and it is supported in four unrelated domains in a single hour:

| Domain | The synthetic data | Outcome |
|---|---|---|
| Indoor navigation | Office of **flat walls, no furniture**; randomized start/goal; noise injected into sensors, actuators, kinematics | Zero-shot to a real robot dodging a moving cart, **and to a robot 100 lb lighter** |
| Web navigation | Teacher-generated pages that need not be realistic — *"it can have three first names if you want, as long as it has that submit button"* | Zero-shot; learned curriculum beats a manual one |
| Autonomous driving | Behavior model learned from real logs, run in a hardware-accelerated **closed-loop** simulator (Waymax, 100 Hz–1 kHz) | Fewer failures on critical scenarios than behavior cloning |
| Molecular structure | **>500k physics-generated structures** against ~200k real crystal structures in the entire field | Synthetic reaches **two-thirds of the mix**; performance rises with the synthetic share |

The explicit anti-bitter-lesson reading, when the audience proposed it:

> *"It's not the bitter lesson. The lesson is exactly clean out — use the noisy data. Embrace the noise. Change the initial conditions when you're training. Use the right abstraction for the simulator."*

Note the last clause. In the navigation case they *chose* the coarsest abstraction — static geometry, no dynamic obstacles — because it made the simulator fast enough to train thousands of policies. Fidelity was traded for throughput deliberately, not conceded.

> [!warning] The counterweight, from the same day
> [Edoardo Airoldi](../../entities/edoardo-airoldi.md), three hours later: **"realism does not imply validity"** — a simulator matching every observable licenses no claim of understanding, because too many mechanistic models are compatible with the same observables.
>
> These are the same observation used for opposite ends. Realism is **neither necessary** (Faust: a superset transfers) **nor sufficient** (Airoldi: a match is not a mechanism). What differs is the goal — a policy that transfers, or a model you can run counterfactuals through. The wiki's [sim-heavy vs. real-data paths](../../syntheses/simulators/sim-heavy-vs-real-data-paths.md) treats fidelity as one axis; this pair says it is two.

## Curriculum is a permutation

> *"Curriculum is nothing else than you're sampling the same data from the same distribution in different order. Curriculum is a permutation on the training data. So order matters."*

The mechanism used for web navigation is **teacher-student co-training**: a teacher network generates environments; a population of student agents attempts them; the teacher receives the *average* and the *best* student's performance and adjusts — lower difficulty when even the best student fails, raise diversity when everyone succeeds. The teacher is disciplined by its own reward: pages with no submit button are unsolvable, so it earns nothing.

The target is a **Goldilocks** band: *"we really need to go to that goldilocks principle where the data is just at the edge of the distribution."* Not in-distribution, not far out. And the same rule is reported to hold for **in-context** learning as for training, which is the bridge to the next section.

Convergent evidence from robotics: RT-1's ablations showed that reducing **diversity** hurts more than reducing sample count. See [crowdsourced robot training data](crowdsourced-robot-training-data.md).

## Where synthetic data is not optional

Driving logs illustrate the structural case. *"Not all data is created equal"* — hours of empty streets at night, and near-zero samples of the risky scenarios that matter, which **cannot be collected ethically**: *"you can't set up the sets where you're throwing the kids in front of the car."*

Worse, replaying logs is not a simulator. Stop the ego vehicle and the logged traffic drives straight through it. A closed-loop simulator needs a **behavior model** that reacts — if a car stops, the others stop.

The training recipe that follows is a weighted sum, and it is the wiki's cleanest empirical resolution of an argument it has been carrying:

- **RL** carries a safety reward — stay on the road, don't hit anything — for the tail where no data exists.
- **Behavior cloning** carries everything that is hopeless to specify as reward: *"how you brake, how you turn, how you have the conversation — all these hows do matter and they're very very difficult to encode into the reward."*
- The weighting shifts toward RL as the state goes out of distribution.

Measured result: RL alone *"slams the brakes or accelerates as fast as it can, because that's what it does"*; the combined agent's deceleration distribution matches the human one **and** fails less on critical scenarios than behavior cloning. See [imitation learning](imitation-learning.md).

## The self-improvement half

Once the data is model-generated, the flywheel's second half is the model improving on its own output.

- **Many-shot in-context learning.** Going from 32 → 500+ examples keeps improving, and enough in-context examples will **override pre-training bias** (train that blue is red and the labels flip). *"Your context now becomes an environment, and it's more or less subject to the similar learning laws"* as training.
- **Model-generated beats human-provided.** Unsupervised ICL (problems without solutions) and **reinforced** ICL (the model proposes and corrects its own solutions) both **outperform supervised ICL**, and transfer across domains (math → GPQA). The hypothesis is a distribution-match effect: *"the human-provided solutions are way out of distribution for the model... when it proposes its own solution, it's closer to its own distribution that it can learn from."*
- **Self-correction needs staged RL.** Naive self-correction fails twice — distribution shift from SFT labels, and models turning conservative and refusing to revise. The fix is two-stage: first hold answer 1 near the original while rewarding improvement in answer 2 (*"counterintuitive, but it's teaching it to think a bit longer term"*), then improve answer 1. Trained on two turns, it **extends to 32** and keeps improving — and **beats parallel best-of-N at equal inference budget**.
- **Simulated humans as the environment.** A clinical triage agent trains against LLM-simulated patients carrying demographics, a *prompted personality*, a case summary, and **facts they won't volunteer** (forgotten, embarrassing, not thought relevant) — up to 60-turn dialogues with tool use, against a reward of **70 physician-written rubrics**. In clinical trials with 5,000 patients. Asked why not train on recorded doctor-patient logs: *"if you have logs this is the static data. This is the offline, and we know that that collapses."*

## The limit nobody can flywheel past

> *"If the model never learned about malaria, it won't know what to do with malaria."*

Coverage is not generated by the loop. The flywheel amplifies and reorders what the world model can already express; it does not add facts the world model never had. Every "does not need to be realistic" claim above is a claim about **fidelity**, not about **coverage** — and the two failure modes look nothing alike.

## The bill — and where the affordable results are

The day after Faust's keynote, [Amir Zadeh](../../entities/lambda.md) priced the thing she was arguing for. The full cost model is on **[simulation economics](../world-models/simulation-economics.md)**; the two numbers that change how this page should be read:

- **A humanoid in a static warehouse runs ~100 simulated seconds per GPU-second. The same humanoid in a forest, with lidar and cameras rendered, runs ~1** — and needs a different GPU, since a B200 does not render. **Turning the sensors on costs about two orders of magnitude**, and the experiment cost reaches the millions.
- **[Sim2Reason](../../entities/sim2reason.md)** — a flywheel result from the same speaker that works precisely because it **never renders anything**. MuJoCo emits forces, velocities and accelerations; an LLM turns the traces into verified question–answer pairs; the fine-tuned model gains **5–10 points on IPhO mechanics from 3B to 72B**, and the gains **transfer to mathematics**, a domain the pipeline never targeted.

> [!note] The two together sharpen the flywheel thesis rather than contradicting it
> Faust's argument is about **what** to synthesize (a superset of reality, not a replica). Zadeh's is about **what you can afford to**. Put together they suggest the near-term wins are in the corner where you keep the *state* and throw away the *pixels* — physics traces, proprioception, structured events — and that the rendered, sensor-rich case robotics actually needs is the one nobody has priced down. Zadeh poses the obvious construction and does not claim it exists: **a curriculum over simulation cost**, cheap scenes for coverage and expensive ones for the gradients only they provide. Compare the *noise* curriculum from the same day's [JEPA tutorial](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md) — cheap synthetic clean data restoring convergence rates on noisy data — the same idea on a different axis.

## Related concepts
- [Simulation economics](../world-models/simulation-economics.md) — what a turn of the flywheel costs in GPU-hours.
- [Generative data augmentation](generative-data-augmentation.md) — the narrower version of the same move.
- [Sim-to-real transfer](sim-to-real-transfer.md) / [domain randomization](sim-to-real-transfer.md) — the classical mechanism the superset argument generalizes.
- [Imitation learning](imitation-learning.md) — the RL+IL hybrid.
- [Real-world robot RL](real-world-robot-rl.md) — the alternative to simulating the tail.
- [Crowdsourced robot training data](crowdsourced-robot-training-data.md) — diversity beating volume.
- [In-context robot learning](in-context-robot-learning.md) — many-shot ICL, robot side.
- [Chain of thought](chain-of-thought.md) / [adaptive depth reasoning](adaptive-depth-reasoning.md) — sequential self-correction vs. parallel sampling.

## Mentioned in
- [Third World Modeling Workshop — Day 2](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — Aleksandra Faust keynote.
- [Third World Modeling Workshop — Day 3](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md) — Amir Zadeh (Lambda): the cost of a flywheel turn, and [Sim2Reason](../../entities/sim2reason.md).

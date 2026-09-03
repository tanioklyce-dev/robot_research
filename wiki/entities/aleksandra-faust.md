---
title: Aleksandra Faust
type: entity
subtype: person
created: 2026-09-02
updated: 2026-09-02
sources: 1
tags: [person, faust, google-deepmind, autorl, curriculum-learning, synthetic-data, self-improvement, waymax, in-context-learning, agi-levels, clinical-agents]
---

**Aleksandra Faust** — **Director of Research at [Google DeepMind](google-deepmind.md)**, leading Frontier AI Health efforts. Keynote speaker at [Day 2 of the Chicago Booth world-modeling workshop](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) (2026-09-01), *"The Synthetic Flywheel: Self-Improvement and Simulation in Foundation Models."*

Her research line, as she tells it, runs continuously from **AutoRL** (learning the reward and architecture in an outer loop around RL training, ~2018) through learned curricula and closed-loop AV simulation to today's **model-generated data and self-correction** — the same meta-learning principles at successively larger scale.

## The one idea to take from her

**A synthetic training environment should be a *superset* of reality, not a replica of it.** She supports this in four unrelated domains in a single hour ([Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md)):

- Zero-shot sim-to-real navigation trained in an office of **flat walls and no furniture**, with noise injected into sensors, actuators and kinematics — transferring to a real robot and to a robot **100 lb lighter**.
- Learned web-page curricula where the generated pages *"don't need to be realistic — it can have three first names if you want, as long as it has that submit button... these three first names is a superset of the real distribution."*
- **>500,000 physics-generated molecular structures** against a field-wide total of ~200,000 real crystal structures, until synthetic data was **two-thirds of the mix** — stated as the first model to outperform AlphaFold 3.
- LLM-simulated patients for a clinical triage agent, prompted with personalities and with facts *"they won't share voluntarily."*

Explicitly **not** the bitter lesson, when asked: *"The lesson is exactly clean out — use the noisy data. Embrace the noise. Change the initial conditions. Use the right abstraction for the simulator."*

See [synthetic data flywheel](../concepts/learning/synthetic-data-flywheel.md).

## Positions worth recording

- **Curriculum is a permutation.** *"Curriculum is nothing else than you're sampling the same data from the same distribution in different order... So order matters."* And the target is a **Goldilocks** zone — data at the *edge* of the distribution, not inside it and not far outside.
- **RL and imitation are complements, measured.** Her AV result — RL for the safety tail, behavior cloning for the un-specifiable *hows* — is the wiki's most direct empirical answer to [LeCun](yann-lecun.md)'s Day 1 claims that imitation learning failed for driving *and* that RL is unusable in the real world. See [imitation learning](../concepts/learning/imitation-learning.md).
- **Offline logs collapse.** Asked why a clinical agent needs a simulator rather than recorded doctor-patient sessions: *"if you have logs this is the static data. This is the offline, and we know that that collapses."*
- **Model-generated beats human-provided, in context.** Unsupervised and self-generated ("reinforced") in-context examples outperform ground-truth ones, hypothesised as a distribution-match effect: human solutions are out of distribution for the model.
- **Context is an environment.** With enough in-context examples, *"we can correct the pre-training biases"* — train that blue is red and the labels flip.
- **On AGI levels.** Two axes (performance × scope), crossed with a use grid (tool → consultant → collaborator → expert) and its societal risks. Her aside is the substance: the slide is **2½–3 years old and has not needed updating.**

## Related
- [Google DeepMind](google-deepmind.md) — employer.
- [Synthetic data flywheel](../concepts/learning/synthetic-data-flywheel.md) — the concept page her keynote anchors.
- [Imitation learning](../concepts/learning/imitation-learning.md) / [sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md).
- [Yann LeCun](yann-lecun.md) — the position her AV work answers.

## Mentioned in
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — keynote.

> [!note] Thin entity, deep backlog
> Everything here is from one talk. **Eight distinct papers** are referenced in that hour and none is ingested — AutoRL navigation, the web-navigation curriculum, Waymax, the sub-angstrom structure model, the Oxford Big Five psychometrics study, many-shot ICL, self-correction RL, and ResidencyRL. The AlphaFold-3 claim in particular is checkable and should be verified rather than relayed.

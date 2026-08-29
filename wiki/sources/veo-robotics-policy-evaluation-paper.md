---
title: "Evaluating Gemini Robotics Policies in a Veo World Simulator"
type: source
url: https://arxiv.org/abs/2512.10675
author: "Gemini Robotics Team, Google DeepMind (incl. Krzysztof Choromanski, Coline Devin, Yilun Du, Ruiqi Gao, Thomas Kipf, Sean Kirmani, Anirudha Majumdar, Carolina Parada, Dhruv Shah, Vikas Sindhwani, Jie Tan, Fei Xia, Ted Xiao, Sherry Yang, Wenhao Yu)"
affiliation: Google DeepMind
published: 2025-12-11
ingested: 2026-08-03
venue: arXiv preprint (v2, 2026-01-06)
format: technical report (19 pp)
local_path: raw/2512.10675.pdf
sha256: e8c5b3ae6584cc8efa9907eeffcd4f73dcdb10576b789f28fb588b46e46ff930
tags: [veo, world-model, policy-evaluation, generative-simulation, gemini-robotics, red-teaming, semantic-safety, ood, google-deepmind, primary-source]
---

## Summary

Uses **Veo**, a frontier video foundation model, as a **generative world simulator for evaluating robot policies** — across "the entire spectrum of policy evaluation use cases: from assessing nominal performance to out-of-distribution (OOD) generalization, and probing physical and semantic safety."

This is the wiki's **third distinct paradigm for robot policy evaluation**, alongside conventional success-rate rollouts ([RoboLab](nvidia-robolab-evaluation-blog.md)) and pairwise human preference ([RoboArena](roboarena-paper.md)). Its argument for existing is sharpest on safety, and it is the same argument [ASIMOV](asimov-benchmark-paper.md) makes about data collection:

> "When the objective is to evaluate safety, hardware evaluation is often simply infeasible." Setting up real scenes probing the long tail — "that sharp objects may break computer screens, that a piece of plastic should not be placed on a stove, that broken glass should not be left on the floor" — "can endanger the robot, its environment, and humans."

The system adds to base Veo: **robot action conditioning**, **multi-view consistency**, and integrated **generative image editing + multi-view completion** to synthesize scene variations. Multi-view consistency is precisely the limitation [Predictive Red Teaming](predictive-red-teaming-paper.md) flagged ten months earlier.

## Key claims

### Validation — does the simulator predict reality?

**1600+ real-world evaluations**, **eight GROD policy checkpoints**, **five tasks**, bimanual manipulator, **80 scene-instruction combinations**. Each episode is an **8-second closed-loop rollout** conditioned on the first frame from the robot's four cameras plus the instruction, scored by **human evaluators** on binary success.

| Metric | Value |
|---|---|
| **Pearson correlation** (predicted vs real success rate) | **0.88** |
| **MMRV** (mean maximum rank violation — ranking consistency) | **0.03** |

> [!warning] The simulator is pessimistic in absolute terms
> "The absolute values of predicted success rates are **lower** than their real counterparts." So Veo(Robotics) is validated as a **ranking and relative-comparison instrument**, not as a source of absolute success rates. That is exactly the tradeoff [RoboArena](roboarena-paper.md) makes for a different reason — and it means this paradigm, like pairwise preference, **cannot answer "what success rate will I get in deployment."**

### What it is used for
- Ranking policies in **nominal** conditions.
- Ranking in **OOD** conditions and quantifying the relative impact of different generalization axes (novel interaction objects, novel visual backgrounds, novel distractors).
- **Red teaming** — exposing behaviors violating physical or semantic safety constraints, using [ASIMOV's](asimov-benchmark-paper.md) definition of semantic safety.

## Entities mentioned
- [Google DeepMind](../entities/google-deepmind.md) · [Gemini Robotics](../entities/gemini-robotics.md) · [Veo](../entities/veo.md)
- [Anirudha Majumdar](../entities/anirudha-majumdar.md) · [Vikas Sindhwani](../entities/vikas-sindhwani.md)

## Concepts touched
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — the third paradigm.
- [World model simulators](../concepts/world-models/world-model-simulators.md) — a video world model used as an evaluation harness rather than a policy or a data generator.
- [Semantic safety](../concepts/safety/semantic-safety.md) · [AI red teaming](../concepts/safety/ai-red-teaming.md)
- [World models](../concepts/world-models/world-model.md) — the generative-video branch.

## Open questions

Stated limitations (§7):
- **Contact-rich interaction with small objects remains hard.** Fig. 11 shows a hallucination — "a novel object appears spontaneously while the gripper is interacting with a different object."
- **8-second episodes.** "Achieving long-horizon (e.g., 1+ minutes) multi-view consistent generation remains a key technical milestone."
- **Human scoring.** The pipeline is not autonomous; automated VLM-based scoring is future work.
- **Inference efficiency** of video generation needs optimization.

Wiki additions:
- **A world model evaluating a policy is a circularity risk the report does not fully address.** If the video model and the policy share training data or failure modes, agreement could reflect correlated error rather than fidelity. Pearson 0.88 against real rollouts is the check on this, but it is measured on 80 scene-instruction combinations for one embodiment.
- **Eight checkpoints of one policy family** — cross-family generalization (would it rank a π0 against a GR checkpoint?) is untested.
- **This interacts with the wiki's LIBERO-PRO thread.** If a generative simulator can synthesize perturbations cheaply, it is a plausible route to running perturbation suites at scale — the thing the [audit backlog](../backlog.md) says nobody has done for 2026-class models. Whether simulator-measured robustness transfers is open.

## Related sources
- [RoboArena](roboarena-paper.md) — pairwise-preference evaluation; also trades absolute magnitude for reliable ranking.
- [How to Evaluate General-Purpose Robot Policies](nvidia-robolab-evaluation-blog.md) — the "collect far more rollouts" pole.
- [Predictive Red Teaming](predictive-red-teaming-paper.md) — the predecessor whose multi-view limitation this addresses.
- [ASIMOV Benchmark](asimov-benchmark-paper.md) — supplies the semantic-safety definition being probed.

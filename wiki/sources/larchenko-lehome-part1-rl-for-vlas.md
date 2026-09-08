---
title: "How I Beat 61 Teams at Robot Laundry Folding in Simulation (with RL) — LeHome Challenge deep dive, Part 1 (Larchenko, 2026)"
type: source
url: https://www.youtube.com/watch?v=mTohakalKz8
local_path: raw/2026-07-19-larchenko-lehome-part1-rl-for-vlas.txt
sha256: 51de3ad3d302fde621a9fd94f6eb2638b5384cc38cec0c2c3c265c7f27d9b5be
author: "Ilia Larchenko"
published: 2026-07-19
ingested: 2026-09-07
venue: "YouTube (channel 'Ilia'); Part 1 of a 3-part series. Companions: tech report arXiv 2606.27163 (v1 2026-06-25, v2 2026-07-18), code github.com/IliaLarchenko/lehome_solution, blog ilialarchenko.com/projects/lehome2026, checkpoints on HF"
duration: "1:17:29"
format: video (author-provided English subtitles; chaptered)
tags: [lehome, icra-2026, so-arm101, bimanual, garment-folding, deformable, rl, vla, pi0.5, flow-matching, awr, recap, advantage-conditioning, cfg, asynchronous-rl, hugging-face-hub, isaac-lab, domain-randomization, curriculum, dagger, sim-to-real, competition, practitioner]
---

# Learning to Fold, Part 1 — RL for a flow-matching VLA

**[Ilia Larchenko](../entities/ilia-larchenko.md)** explains, from the inside, the solution that took **1st of 62 teams** in the simulation round of the **[LeHome Challenge 2026](../entities/lehome-challenge-2026.md)** (ICRA 2026, Vienna) and **2nd in the real-world final**: a **π0.5**-based VLA improved by a reinforcement-learning loop on a **bimanual [SO-ARM101](../entities/so-arm101.md)** folding four garment types in **Isaac Lab**. The video is Part 1 of 3 and covers the RL method, the policy architecture, and rollout collection. Parts 2 (reward, advantage, inference-time optimisation) and 3 (sim-to-real, DAgger, the ICRA final) were not yet released at ingest. **Everything here is first-person practitioner testimony**; the [tech report](larchenko-learning-to-fold-tech-report.md) is the primary for numbers — now ingested.

## Summary

Two design decisions carry the whole solution. First, **the RL method is chosen by the action head**: a flow-matching policy can sample actions but cannot evaluate their likelihood, so anything that needs `log π(a|s)` — REINFORCE, TRPO, PPO — does not apply directly [28:02–31:07]. Larchenko uses two methods that only *reweight the target distribution* and let flow matching learn it: **Advantage-Weighted Regression** (sample training data proportional to `exp(clip(A)/β)`, β = 1, implemented in the *data loader* rather than the loss) and **RECAP** from [π*0.6](pistar06-paper.md) (train one network in an unconditional mode and an advantage-conditioned mode; at rollout, ask for good actions). Combined, they lift the base policy *and* unlock classifier-free guidance. Second, **the policy is its own value function**: auxiliary heads on the π0.5 backbone predict success probability, completion, garment type, and **keypoint distances now and after the action chunk** — the last being *"a cheap replacement for a world model."* The training and rollout processes never talk to each other; they exchange checkpoints and rollout datasets through the **Hugging Face Hub**, so each side scales independently. Rollout collection is curriculum-targeted (sample garments whose current success rate is near 40–50 %), with **success replay** under aggressive domain randomisation and **semi-success replay** from the state where a near-miss went wrong.

## Key claims

### The competition [02:34–12:25]

- Four garment types (long-sleeve top, short-sleeve top, long pants, shorts); **full-fold success only**, defined by keypoint-distance thresholds — some pairs must be close, others far apart so the garment is not balled up [03:09–05:11]. Organiser demonstrations on HF (top camera flipped 180°); simulator = Isaac Lab (README: Isaac Lab 2.3.1 / Isaac Sim 5.1 / LeRobot 0.4.2); sponsor Lightwheel.
- Why it is hard [07:14–09:18]: cheap arms with **backlash and a gripper that sometimes cannot hold fabric**; hardware and placement fixed by the organisers; the final ran on **an orange robot he had never touched** against his red ones — *"every time you assemble it, every time you calibrate it … they work slightly differently."*
- Motivation: a playground for RL-for-VLA ideas with **10–20 s episodes**, so no cluster needed [11:25].

### The asynchronous loop [12:42–18:29]

- Policy and value are one model, so there are two processes: **train** (one H200; downloads new rollout datasets, computes advantages from returns *without any model prediction*, trains, uploads a checkpoint every 30–60 min) and **rollout** (one or more RTX PRO 6000 machines; download latest checkpoint, roll out, predict value/completion, tag hard states, upload). *"Nothing waits for each other."* A third, optional process is human teleop / DAgger from stored hard states — **mattered little in simulation, a lot in the real round** [16:34–17:34].

### Why PPO does not fit, and what does [18:29–48:52]

- Policy-gradient methods need the action's log-probability; on-policy ones also need data from the *current* policy — *"as soon as you made your first step, it's not on-policy anymore"* [28:02]. Flow matching learns a velocity field that transports Gaussian noise to actions; it *"cannot tell you what the probability is to sample this action"* [24:49]. PPO-for-flow variants exist but *"make the problem more complex … then apply PPO to this approximated problem"* [31:07].
- **AWR** [32:08–38:30]: constrain KL(π‖μ) ≤ ε and the closed-form optimum is μ reweighted by `exp(A/β)` — *"our flow matching approach is good at sampling from any distribution, and it doesn't care from what distribution."* One extra weight in the BC pipeline. His variant: clip A, β = 1, and **weight by sampling probability rather than in the loss** — bad actions are rarely loaded at all, so batches carry more variance of good ones (*"I didn't ablate it properly"*).
- **RECAP** [39:05–44:36], his simplification of the π*0.6 derivation: split μ by total probability into high- and low-advantage parts; train the same weights unconditionally (= BC) and conditioned on an advantage-indicator embedding (= only the high-advantage part); roll out conditioned. *"Surprisingly, the policy starts to predict better actions when you simply ask it to."* Equivalent to reweighting by `P(A > threshold)` — a step function smoothed by advantage noise. Using **both** lifts the base *and* enables CFG at inference (Part 2).
- **The manifold argument** [44:36–46:47]: 12 DoF × 30 steps = a 360-dimensional action chunk, and valid chunks are a thin manifold inside it. Methods that *push down* bad actions spread that probability anywhere, possibly off-manifold; AWR/RECAP only *redistribute toward* good actions, even still training on bad ones, so they stay on it.
- **The cost**: *"literally zero exploration … the model never learned new behavior"* — it got better at what the demonstrations already contained [46:47].

### Policy architecture [48:55–60:10]

- π0.5 (PaliGemma = Gemma + SigLIP, plus the flow-matching action expert and a FAST branch), starting from his team's winning **BEHAVIOR-1K Challenge 2025** architecture.
- **Inputs added**: an advantage-indicator token (sent only when good actions are wanted) and a garment-type token; both also injected **directly into the action expert via AdaRMS** alongside the flow timestep, because one token among hundreds *"is not conditioned enough"* [57:30–58:33]. Not ablated.
- **Auxiliary heads** from three query tokens: a *current* query after the images only (garment type, success probability, completion, time-to-completion [legacy], current keypoint distances); a *FAST* query and a *flow* query after each action branch, predicting **success delta** (*"something between a Q and an advantage"*), future completion, and **future keypoint distances after the chunk** — *"this is exactly what a world model does, just … this subset"* [52:09–55:24].
- Garment type is predicted over the first few frames and fed back for the rest of the episode — a *"System 2"* at episode start, ~99 % accurate, probably unnecessary, now load-bearing [56:29–57:30].
- Attention blocks: images + current query | state + garment type | advantage (visible to nothing) | FAST and flow branches see everything before them but not each other [58:33–59:34].

### Rollout collection [60:10–75:20]

- ~30 s per episode; optimisations: resolutions, video codecs, parallel workers, **episode cut-out when the policy stalls**.
- **Domain randomisation** per rollout: garment pattern and colour (even per frame — *"our policy is memoryless"*), lighting, camera pose, arm placement, cloth physics; far more aggressive for the real round. *"Never break the actual physics."* He calls image augmentation *"very underutilized in robotics."*
- **Curriculum**: sample garments by closeness of current success rate to a target (40–50 %) — near-zero and near-100 % garments teach little [68:03–70:06].
- **Success replay**: re-run a successful episode's *actions* from the same initial state under heavy visual randomisation, no policy needed — used heavily for sim-to-real camera alignment [70:06–71:10].
- **Semi-success replay**: on a near-miss (checkpoint reached, then success probability fell), replay to just before the drop and let the policy finish — yielding a failed and a successful rollout from the same state, *"very important data for RL"* [71:10–73:16].
- **Hard mining** of difficult states: tried, mostly dropped — too few successes per unit time [73:16–74:16].
- Thousands of rollouts; **old rollouts down-weighted** because they carry stale value predictions (Part 2).

### Numbers (from the companion blog post; all confirmed by the [tech report](larchenko-learning-to-fold-tech-report.md))

| | |
|---|---|
| Simulation round | **79.63 %** full-fold success; long-sleeve 74.5 / short-sleeve 70.0 / pants 80.5 / shorts 93.5; **+6.1 pts** over 2nd; 80 evaluation rollouts × 10 episodes |
| Real-world final | **865 / 1080** points, 2nd (winner 895) |
| Inference (Part 2) | CFG scale 7–9; best-of-N with N = 2–3; replan every ~5 of 30 steps; noise temperature < 1 |
| Real fine-tune mix | 60 % organiser data / 30 % own teleop + DAgger / 10 % augmented sim replays; 2–3 DAgger loops |

## The wiki's read

- **This is the counterexample the [flow-matching page](../concepts/learning/flow-matching.md) said it did not have.** That page recorded that *no wiki source has RL-post-trained a flow-matching action head against a task reward*. Here is one, at single-GPU scale, and the method is not a new gradient estimator — it is the observation that a sampler does not need likelihoods if you reweight what it samples from. AWR and RECAP are the two ways to do that, and they compose.
- **"The policy is its own value function" is a real departure from π*0.6**, which trains a *separate* distributional value model. Folding it into the policy saves a network and, more interestingly, makes the value estimate see exactly what the policy sees. The wiki has no comparison of the two; it is the obvious ablation.
- **Keypoint distances as a world model** is the [Jupiter-in-six-numbers](lecun-xing-jepa-glp-debate-2026.md) argument applied to laundry: the task's success criterion *defines* the sufficient statistic, so predict that after the action chunk and skip pixels and latents. It only works because the criterion is known and low-dimensional — which is the case in a competition and rarely in a home.
- **The zero-exploration confession matters more than the leaderboard.** AWR and RECAP sharpen a distribution; they cannot widen it. Everything the winning policy does was in the organiser demonstrations. That is the same ceiling the [RECAP page](../entities/pistar06.md) notes, stated by someone who hit it.
- **The Hub as an RL message bus** is the practical idea most likely to travel: two processes, two repositories, no coordination, and the human teleop process is a third client of the same bus. It is the low-budget form of the [HIL-SERL](hil-serl-paper.md) loop and drops straight onto the SO-ARM101 stack this wiki already tracks.
- **Evidentiary weight.** First-person, un-ablated by the author's own repeated admission, single competitor, one task family. The blog numbers are confirmed by the [tech report](larchenko-learning-to-fold-tech-report.md), which also supplies the Part 2/3 material and two candid corrections (a CUPED coefficient error, a units bug). The BEHAVIOR-1K link — the wiki's [12.4 %](../entities/behavior-benchmark.md) figure is the 2025 challenge winner's score, and Larchenko says his team won — is confirmed by the tech report's citation [8] (Larchenko, Zarin & Karnatak, *1st Place Solution for the 2025 BEHAVIOR Challenge*, arXiv 2512.06951); that paper itself is un-ingested.

## Entities mentioned

- [Ilia Larchenko](../entities/ilia-larchenko.md) — author and competitor.
- [LeHome Challenge 2026](../entities/lehome-challenge-2026.md) — the competition.
- [SO-ARM101](../entities/so-arm101.md) — the designated arm, bimanual.
- [Physical Intelligence](../entities/physical-intelligence.md), [π*0.6](../entities/pistar06.md) — π0.5 backbone and the RECAP recipe.
- [LeRobot](../entities/lerobot.md), [Hugging Face](../entities/hugging-face.md) — the framework and the Hub used as the RL bus.
- [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) — the simulator.
- [BEHAVIOR-1K](../entities/behavior-benchmark.md) — his prior win, architecture carried over.

## Concepts touched

- [RL for flow-matching VLAs](../concepts/learning/rl-for-flow-matching-vlas.md) — the concept page this source creates.
- [Flow matching](../concepts/learning/flow-matching.md) — why likelihoods are unavailable.
- [Real-world robot RL](../concepts/learning/real-world-robot-rl.md) — the asynchronous, human-optional loop.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — domain randomisation and success replay.
- [Imitation learning](../concepts/learning/imitation-learning.md) — BC as the base, DAgger as the third process.
- [VLA models](../concepts/learning/vla-models.md) — π0.5 with auxiliary heads.
- [World model](../concepts/world-models/world-model.md) — the keypoint-distance substitute.

## Open questions

- Ablations he names as missing: sampler-weighting vs loss-weighting; AdaRMS conditioning; hard mining; the garment-type feedback loop.
- Combined policy-value vs a separate value model (π*0.6's choice): which estimates advantage better on the same rollouts?
- How much of the 79.6 % is RL over BC? No BC-only number in Part 1.
- Parts 2 and 3 (reward and advantage computation; sim-to-real and the ICRA final) — the transfer story is the one this wiki most needs.

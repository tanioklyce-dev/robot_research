---
title: Curriculum Module 6 — Imitation learning and behavior cloning
type: synthesis
created: 2026-05-10
updated: 2026-05-10
tags: [curriculum, module-6, imitation-learning, behavior-cloning, multi-modal-actions, distribution-shift, dagger, pusht]
prereqs: [curriculum-01, curriculum-02, curriculum-03, curriculum-04]
status: draft
---

> [!note] Curriculum context
> This is **Module 6** of the [Robot-learning curriculum](robot-learning-curriculum.md). It assumes Tier 1 ([Modules 1–4](robot-learning-curriculum.md): NN, CNN, attention, SSL). It directly precedes **[Module 7](curriculum-07-bc-lineage-pusht.md)**, which dives into the IBC → BeT → Diffusion Policy lineage; this module sets up the conceptual frame those papers respond to. It is also a sibling of **Module 8** (RL vocabulary) — the two cover the two main robot-policy training paradigms.
>
> Acronyms used here are also in the [Glossary](../../glossary.md). First-mention links go there.

## What this module is

The conceptual setup for everything in [Module 7](curriculum-07-bc-lineage-pusht.md): what **imitation learning** is, why **behavior cloning** is its simplest instance, where the demonstration data comes from, and the two failure modes — **multi-modal action distributions** and **distribution shift** — that every later technique in the curriculum is responding to. Then a quick hand-off to Module 7 with a clear statement of what's left to solve.

By the end of the module you should be able to:

1. Explain in one paragraph what makes imitation learning different from reinforcement learning, and why robotics has gravitated toward it.
2. Write the BC training loop from memory, including the structure of the dataset and the loss.
3. Describe the **multi-modal action distribution** failure mode without consulting notes, and predict in advance which tasks will trigger it.
4. Describe **distribution shift** (covariate shift) and explain why a BC policy with low training loss can still fail in deployment.
5. Recognize when a paper or system is using **action chunking** + **receding-horizon control**, and roughly what those choices buy.

## IL vs RL vs world-model + planning

Three ways to obtain a policy:

| Paradigm | What you train on | What's learned | Action selection at deploy |
| --- | --- | --- | --- |
| **Imitation learning (IL)** | demonstrations `(s, a)` from an expert | a policy `π: s → a` | sample / forward-pass the policy |
| **Reinforcement learning ([RL](../../glossary.md#rl))** | environment interactions + reward | a policy and/or value function | sample policy, possibly value-shaped |
| **World model + planning** | observation sequences (often `(s, a, s')`) | a dynamics model `f: (s, a) → s'` | optimize action sequences against `f` and a cost ([MPC](../../glossary.md#mpc)) |

These can be combined — many modern systems are hybrids — but the curriculum keeps them separate for now because the failure modes and design pressures differ.

**Why IL dominates 2023–2026 robotics.** Reward design for real-world robotic tasks is hard, sparse, and easy to game. Demonstrations, by contrast, are something a human operator can produce in minutes per task using teleoperation rigs (e.g. [UMI](../../entities/umi.md)). Once you have demos, BC is the simplest thing that could possibly work, and "simplest thing that could possibly work" was the right move for an empirical era — until the failure modes below started to bite.

> [!note] Curriculum cross-link
> RL fundamentals (MDPs, return, policy gradient, PPO, SAC, Dreamer-class MBRL) are [Module 8](robot-learning-curriculum.md) — kept brief because RL is *not* the focus of this curriculum. World models are [Module 10](robot-learning-curriculum.md). For the rest of this module we stay inside IL.

## BC: the simplest possible IL

[Behavior cloning](../../glossary.md#bc) reduces policy learning to **supervised learning**:

- **Dataset.** A set of demonstrations, each a sequence of `(observation, action)` pairs collected from an expert (human teleoperator, scripted controller, prior policy, …). Concretely: `D = {(s_i, a_i)}_{i=1..N}`.
- **Model.** Any function approximator from observation to action. Historically a multi-layer perceptron ([MLP](../../glossary.md#mlp)); modern variants are a [CNN](../../glossary.md#cnn) / [ViT](../../glossary.md#vit) over images stacked with an MLP head, possibly with a temporal model ([transformer](../../glossary.md#transformer) / [LSTM](../../glossary.md#lstm)).
- **Loss.** Supervised regression — typically [MSE](../../glossary.md#mse) on continuous actions. For discrete actions, [cross-entropy](../../glossary.md#ce).
  ```
  L_BC(θ) = E_(s,a)~D [ ‖a − π_θ(s)‖² ]      // continuous
  L_BC(θ) = E_(s,a)~D [ −log π_θ(a | s) ]    // discrete
  ```
- **Training.** Standard [SGD](../../glossary.md#sgd) / [Adam](../../glossary.md#adam). Same playbook as image classification.
- **Inference.** At each control tick, observe `s_t`, compute `a_t = π_θ(s_t)`, send `a_t` to the robot.

That is the entire algorithm. There are no rewards, no environment interactions during training, no exploration. Whatever capability the policy ends up with comes from what was in the demonstrations.

This simplicity is BC's selling point and its central weakness. The two weaknesses below are the reason every later technique in the curriculum exists.

## Where the demonstrations come from

A BC policy is only as good as its demos. Practically, demos for robotics come from a few sources:

- **Direct teleoperation.** A human pilots the robot — joystick, VR rig, leader–follower arm pair, hand-held gripper ([UMI](../../entities/umi.md)). High fidelity; expensive to scale; the dominant source for [Diffusion Policy](../../entities/diffusion-policy.md) / [Robot Utility Models](../../entities/robot-utility-models.md) / [π0](../../entities/physical-intelligence.md).
- **Scripted demos in simulation.** Hand-written controllers solve the task in sim; the rollout becomes a demo. Cheap; brittle to task structure; effective for simple primitives. [MimicGen](../../entities/mimicgen.md) generalizes this idea by re-targeting a single demo across many configurations.
- **Human video.** The robot doesn't appear in the demo at all — pretraining datasets like the ~20,854 hr egocentric corpus used by [GR00T N1.6/N1.7](../../entities/nvidia-groot.md) are this style. Useful for representation pretraining; doesn't directly give actions, so an additional bridge is needed (action labels via inverse dynamics, or downstream fine-tuning on real teleop).
- **Cross-platform demos.** Datasets like [DROID](../../entities/droid.md) (350 hr, 76k trajectories on Franka) aggregate across labs and tasks. The 2024–2026 trend is to pretrain on aggregated datasets and fine-tune on a small task-specific demo set.

Two scaling laws show up empirically:

- **More demos help, sublinearly.** Doubling the demo count usually improves but rarely doubles success rate.
- **Diversity > raw count.** [Robot Utility Models](../../entities/robot-utility-models.md) makes this concrete: training on a small but diverse set of environments outperforms more data from a single environment. The [Robot Utility Models paper](../../sources/robot-utility-models-paper.md) is the cleanest reference for this.

The data question is **the** bottleneck for IL-based robotics. [Module 13](robot-learning-curriculum.md) returns to it from the home-robotics deployment side; for now, take "demos are the limited resource" as given.

## Failure mode 1: multi-modal action distributions

This is the failure that the entire [Module 7](curriculum-07-bc-lineage-pusht.md) lineage is designed to fix. Stating it precisely here so Module 7 can immediately start solving it.

**Setup.** A demo dataset is a set of `(s, a)` pairs. Suppose for a given state `s`, the demos contain action `a_1` half the time and action `a_2` the other half. Both are valid expert behaviors — there's just symmetry in the task. Examples:

- A pushing task where you can approach the object **from the left** or **from the right**.
- A manipulation task with **two valid grasps** (one top, one side).
- A driving task with **two safe lane choices** at a fork.

**The failure.** Vanilla MSE-BC fits a deterministic function `π_θ(s) = a`. The MSE objective has a closed-form optimum at the **conditional mean** of the action distribution: `π*(s) = E[a | s] = (a_1 + a_2) / 2`. That midpoint is *neither demo action*, and in robotics it can be physically nonsensical (mid-trajectory between two grasps = empty space; mid-direction between left-push and right-push = stand still or push into the object). Mode averaging is silent — training loss looks fine, but the policy executes none of the demonstrated behaviors.

**When does this bite?** Whenever the optimal-actions-given-state distribution `p(a | s)` has more than one mode. That's almost always, in real robotics — any task with symmetry, multiple valid plans, or stylistic freedom triggers it. PushT was *engineered* to make this pathology visible (see below).

**Why MLP + MSE specifically.** Cross-entropy on discretized actions partially escapes this — it can put mass on multiple bins. But the *continuous* version of "softmax over actions" is exactly what [IBC](../../entities/ibc.md), [BeT](../../entities/bet.md), and [Diffusion Policy](../../entities/diffusion-policy.md) build, each in a different way. **Module 7 is the answer to this section.**

## Failure mode 2: distribution shift (covariate shift)

A more subtle failure that BC has independently of multi-modality. Even a perfectly-trained MSE-BC policy can fail at deployment.

**Setup.** Training data is `(s, a)` pairs visited by the *expert*. At deploy, the policy visits states *it* induces. If the policy's actions are slightly off from the expert's, it visits states the expert never visited, where the policy was never trained, where its actions are even further off, …

**The mathematical statement.** BC training assumes `s ~ d_expert`, but at deploy the relevant distribution is `s ~ d_π_θ`. These are different distributions ("covariate shift"). Errors compound: small per-step errors in action prediction accumulate into states never seen in training.

**Worst-case bound (Ross & Bagnell 2010).** For an episode of length `T`, the expected return gap between BC and the expert grows as **O(T²)** with per-step error rate, vs O(T) for an oracle. Real numbers vary, but the key intuition is: **BC errors compound across time** in a way classification errors don't.

**The classical fix: [DAgger](../../glossary.md#dagger)** (Ross, Gordon, Bagnell, AISTATS 2011) — Dataset Aggregation. The recipe:

1. Train a BC policy `π_0` on the initial expert demos.
2. Roll out `π_0` in the environment to collect states `π_0` actually visits.
3. **Ask the expert for actions at those states.**
4. Add these `(s, a_expert)` pairs to the dataset.
5. Retrain → `π_1`. Repeat.

DAgger reduces the worst-case bound to O(T), at the cost of **needing the expert in the loop during training** — usually a human teleoperator who can label states the policy actually reaches. That cost makes DAgger expensive and rarely run in modern practice. Modern systems mostly tolerate distribution shift through other means (much more data, broader coverage, action chunking + replanning, on-policy fine-tuning with simulators or human corrections).

> [!note] Why DAgger appears anyway
> Even if DAgger isn't run literally, "distribution shift" as a concept is *the* reason modern BC pipelines emphasize **demo coverage** — the practical move is to make the demo distribution wide enough that the policy's induced distribution stays in-support. RUM's [data diversity > data quantity](../assistive/long-term-in-home-robot-deployments.md) finding is essentially this insight under another name.

## Action chunking and receding-horizon control

Two related design choices that show up across modern BC and bear naming here.

**Action chunking** — predict a *sequence* of `T_p` future actions at once, not just the next one. The policy is `π_θ: s → (a_1, a_2, …, a_{T_p})`. This regularizes the policy: it has to commit to a coherent short-horizon trajectory rather than oscillate between modes per timestep. Chunking smooths multi-modal flicker even before specialized methods like Diffusion Policy.

**Receding-horizon control** — execute only the first `T_a < T_p` actions of the predicted chunk, then re-observe and re-plan. This closes the loop: even if the world drifts from what the model expected by step 5 of an 8-step plan, the agent corrects.

Convention popularized by [Diffusion Policy](../../entities/diffusion-policy.md): predict `T_p = 16` actions, execute `T_a = 8` before re-planning. By 2026 this is near-default across BC and [VLA](../../glossary.md#vla) implementations.

Module 7 covers chunking + receding horizon in more depth in the Diffusion Policy section — for now, just remember that they're orthogonal to the action-head choice and almost free to add.

## The canonical [PushT](../../entities/pusht.md) setup

The benchmark Module 7 builds on. Briefly:

- **Task.** 2D top-down: a circular pusher (point-mass end-effector, no gripper) shoves a T-shaped block to a target pose, then retreats to an end-zone.
- **Why it's the canonical BC failure-demo benchmark.** Multi-modality is built in by symmetry: a human demonstrator can approach the T from the left or right; both work. So a demo dataset has bimodal action distributions for many states — and vanilla MSE-BC fails by mode-averaging. PushT was designed by [IBC](../../entities/ibc.md) (Florence et al., CoRL 2021) to make this failure visible.
- **Why it's used everywhere.** Cheap (trains in ~1 hour on a single GPU), discriminative (purely reactive policies fail), and shared across both BC-line work ([IBC](../../sources/ibc-paper.md), [BeT](../../sources/bet-paper.md), [Diffusion Policy](../../sources/diffusion-policy-paper.md)) and world-model-line work ([LeWM](../../entities/leworldmodel.md), [DINO-WM](../../entities/dino-wm.md), [JEPA-WMs](../../entities/jepa-wms.md)). That overlap is the reason this curriculum threads PushT through Modules 6–12.

Full mechanics — observation modality, action space, success criterion, dataset format, variant differences — are in the [PushT entity page](../../entities/pusht.md). Read that page once now; it'll be referenced repeatedly through the curriculum.

## Anchor exercise

> **Train a vanilla MSE-MLP BC policy on PushT demos. Watch it fail by averaging modes.**

This is the experimental ground-truth for everything in this module. Concrete steps:

1. **Get the data.** Either:
   - Clone the [diffusion_policy](https://github.com/columbia-ai-robotics/diffusion_policy) repo and download the canonical PushT dataset (state-based variant is fastest); or
   - Use the `stable-worldmodel` PushT shipped with [LeWM howto](../world-models/leworldmodel-howto.md) and dump `(s, a)` pairs from a few hundred trajectories.
2. **Build a tiny MLP.** Input: end-effector xy + T-block xy + T-block angle (state variant; ~5 dims). Output: 2D action. 2–3 hidden layers of 128–256 units. ReLU, no dropout, Adam, MSE loss. ~10 minutes to train.
3. **Roll out.** Run the policy in the PushT environment for ~50 episodes. Track success rate.
4. **Visualize the failure.** At a fixed start state, render the rollout. Plot the trajectory the policy executes alongside trajectories from a few demos. You should observe:
   - Policy hovers near the T-block but doesn't commit to a side.
   - Or pushes from a "compromise" angle that fails the IoU threshold.
   - Success rate well below the demo-rollout baseline (~95% with a competent policy on this task).
5. **Sanity check the diagnosis.** Plot the demo action distribution at one or two ambiguous states (e.g., end-effector near the T's symmetry axis). You should see two clusters; the MLP's prediction sits between them.

The point is to feel the failure in your hands. After this exercise, every architecture in [Module 7](curriculum-07-bc-lineage-pusht.md) reads as a specific answer to a specific problem you've now seen with your own eyes.

If you want to push further: replace the MSE-MLP with an MLP that outputs **mixture-of-Gaussians** parameters (mean + variance per component, weighted) and trains via negative log-likelihood. This is the simplest possible mode-aware BC and is roughly the LSTM-GMM baseline used in the Diffusion Policy paper. Note where it works (clean bimodal cases) and where it fails (sharp mode boundaries, more than ~3 modes). That motivates Module 7's escalation to EBMs / discrete heads / diffusion.

## Recommended reading

In order:

1. **[Imitation learning concept page](../../concepts/learning/imitation-learning.md)** — short overview and recent canonical references.
2. **[PushT entity page](../../entities/pusht.md)** — full task mechanics; image / state variants; dataset format.
3. **Pomerleau 1989 (ALVINN)** — classical reference for the *first* BC system; not a wiki source page but worth a search if you want historical context. (Five-minute skim; primary value is "BC has been around for a while and the failure modes were known early.")
4. **Ross, Gordon, Bagnell 2011 (DAgger)** — the canonical distribution-shift paper. Sections 1–3 are enough; the proofs are skippable.
5. **[Robot Utility Models paper](../../sources/robot-utility-models-paper.md)** — the data-diversity finding in practice. §2 (data collection) and §4 (cross-environment generalization).

Do not yet read IBC / BeT / Diffusion Policy — those are [Module 7](curriculum-07-bc-lineage-pusht.md). Reading them now would skip the "feel the failure mode in your hands" step.

## What you should now be able to do

- Read a robotics paper's "method" section and immediately identify whether it is BC, RL, or world-model + planning, and (if BC) what action head it uses.
- Predict in advance which tasks will trigger multi-modal failure (any task with action symmetry or multiple valid plans) and which won't (e.g., reaching to a unique target).
- Diagnose a deployed BC policy that drifts off-distribution as a covariate-shift problem rather than an "underfitting" problem, and reason about whether more data, more diversity, or DAgger-style on-policy correction is the appropriate fix.
- Hand off cleanly to [Module 7](curriculum-07-bc-lineage-pusht.md): you understand the problem; the next module is the architecture catalog of solutions.

## Hand-off to Module 7

Module 6 ends with a concrete failure (mode averaging on PushT) and a known-but-rarely-used fix (DAgger). [Module 7](curriculum-07-bc-lineage-pusht.md) walks the three-paper lineage that solves the multi-modal problem **without** asking the expert again at deploy time:

- **[IBC](../../sources/ibc-paper.md)** — make the policy implicit, training an energy-based model with [InfoNCE](../../glossary.md#infonce).
- **[BeT](../../sources/bet-paper.md)** — discretize the action space via k-means; predict a cluster ID + offset.
- **[Diffusion Policy](../../sources/diffusion-policy-paper.md)** — model `p(a | s)` with a conditional [DDPM](../../glossary.md#ddpm) over action chunks. The dominant 2024–2026 default.

Distribution shift remains an open problem across all three; modern systems address it through coverage (more / more-diverse demos), action chunking + replanning, and occasional on-policy correction loops.

## Related curriculum modules

- **[Modules 1–4](robot-learning-curriculum.md)** — prerequisites for the model architectures (MLP, CNN, transformer, embeddings).
- **[Module 7](curriculum-07-bc-lineage-pusht.md)** — direct successor; the IBC → BeT → DP architecture lineage.
- **[Module 8](robot-learning-curriculum.md)** — RL vocabulary; the alternative paradigm to IL.
- **[Module 9](robot-learning-curriculum.md)** — VLAs; BC scaled up with a VLM backbone and language conditioning.
- **[Module 10](robot-learning-curriculum.md)** — World models; the third paradigm (the one [LeWM](../../entities/leworldmodel.md) inhabits).

## Mentioned in

- [Robot-learning curriculum](robot-learning-curriculum.md)
- [Index](../../index.md)

## Open questions / TBD

- **Pomerleau 1989 (ALVINN)** as a source page — would anchor the BC line historically; low priority.
- **Ross / Bagnell DAgger paper** as a source page — would let us cite the O(T²) bound directly rather than paraphrasing.
- **Mixture-of-Gaussians BC (LSTM-GMM)** as an entity — appears as a Diffusion Policy ablation; useful intermediate between MSE-MLP and the Module 7 lineage.

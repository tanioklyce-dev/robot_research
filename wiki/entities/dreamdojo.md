---
title: DreamDojo
type: entity
subtype: model
created: 2026-11-13
updated: 2026-11-13
sources: 16
tags: [dreamdojo, world-model, action-conditioned, generative-video, nvidia-gear, cosmos, latent-action, self-forcing, distillation, human-video-pretraining, open-weights, neural-simulation]
---

**DreamDojo** is [NVIDIA GEAR](nvidia-gear.md)'s action-conditioned video [world model](../concepts/world-models/world-model-simulators.md) for robots (February 2026, ICML 2026 spotlight). Given robot actions, it predicts the camera frames that would follow. It is pretrained on 44,711 hours of egocentric human video ([DreamDojo paper](../sources/dreamdojo-paper.md)).

It *consumes* actions and outputs video. That makes it a simulator, not a policy: the opposite role to its sibling [DreamZero](dreamzero.md), a [world-action model](../concepts/world-models/world-action-model.md) that *emits* actions.

## Design
- **Backbone:** [Cosmos-Predict2.5](nvidia-cosmos.md), a latent video diffusion transformer, in 2B and 14B sizes. Pretrained for 140k steps on 256 H100s ([paper](../sources/dreamdojo-paper.md)).
- **Latent actions from unlabeled video.** An encoder with an information bottleneck turns consecutive frames into a continuous action code. This lets human video, which has no action labels, condition pretraining. On held-out evaluations it matches conditioning on ground-truth retargeted actions (PSNR 20.913 vs 20.960). Post-training then swaps in each robot's real action space.
- **Data:** 43,827 h of crowdsourced egocentric video (DreamDojo-HV), plus [EgoDex](egodex.md) at 829 h and 55 h of in-lab hand capture. The paper calls it the largest corpus used to pretrain a world model.
- **Real-time distillation.** A 35-step bidirectional teacher is distilled into a 4-step causal student using Self-Forcing. Speed rises from 2.72 FPS to 10.81 FPS at 640×480, and rollouts run stably for more than a minute.

## Results
- **Benefit of human-video pretraining.** PSNR rises steadily as more human data is added, and 14B beats 2B. In a 12-person preference study, raters chose DreamDojo-14B over plain Cosmos-Predict2.5 about 73% of the time for physics and for action following ([paper](../sources/dreamdojo-paper.md)).
- **Uses shown in the paper:** policy evaluation (scoring GR00T N1.5 checkpoints on AgiBot fruit packing without a robot), live teleoperation inside the model, and model-based planning.
- **As an RL environment, in a later NVIDIA report.** [GR00T 2](../sources/gr00t-2-whitepaper.md) (App. F.5) adapts DreamDojo to a policy's own rollouts and runs GRPO inside it. Policies trained this way improve outside the model too: ten RoboLab tasks rise from 51.3% to 70.9%, and four real tasks from 42.5% to 71.7% (60 trials each). Each task family needs about 300 physical rollouts plus a learned success detector, and each configuration is one run. See [real-world robot RL](../concepts/learning/real-world-robot-rl.md).

> [!note] What hasn't been shown
> No source in the wiki reports a policy learned *from scratch* inside DreamDojo and then deployed. The GR00T 2 result fine-tunes a pretrained policy. It also hasn't been compared head to head with the JEPA line ([V-JEPA 2](v-jepa-2.md), [LeWorldModel](leworldmodel.md)) on a shared benchmark. See [generative-video vs JEPA world models](../syntheses/world-models/generative-video-vs-jepa-world-models.md).

## Availability (checked 2026-11-13)
| Artifact | Licence |
|---|---|
| Code ([NVIDIA/DreamDojo](https://github.com/NVIDIA/DreamDojo)): pretraining, post-training, distillation, evaluation | Apache-2.0 |
| Weights ([nvidia/DreamDojo](https://huggingface.co/nvidia/DreamDojo)): 2B and 14B pretrained; post-trained versions for [Fourier GR-1](fourier-gr-1.md), [Unitree G1](unitree-g1.md), [AGIBOT](agibot.md) and [YAM](yam.md); latent-action model | NVIDIA Open Model License |
| GR-1 post-training data and evaluation sets | CC BY-NC 4.0 |
| DreamDojo-HV (the 44k h corpus) | Not released |

Everything above was released on 2026-02-18. The released checkpoints can be fine-tuned, but the pretraining can't be reproduced. Details are in the [paper page's release section](../sources/dreamdojo-paper.md#project-page-and-release-checked-2026-11-13).

## Lineage
One of three Dream* papers from NVIDIA GEAR, alongside [DreamGen](dreamgen.md) (a video model as a robot-data generator, 2025) and [DreamZero](dreamzero.md) (a world-action policy). DreamDojo (2026-02-06) predates DreamZero (2026-02-17) by 11 days. The two are parallel branches, not a sequence. The "destination paper" framing in some older wiki pages is outdated.

## Related
- Concepts: [World-model simulators](../concepts/world-models/world-model-simulators.md), [World-action model](../concepts/world-models/world-action-model.md), [Real-world robot RL](../concepts/learning/real-world-robot-rl.md), [Cross-embodiment transfer](../concepts/learning/cross-embodiment.md)
- People: [Joel Jang](joel-jang.md), [Jim Fan](jim-fan.md), [Yuke Zhu](yuke-zhu.md) (project leads)
- Data: [EgoDex](egodex.md), [Human-1M](human-1m.md) (GR00T 2's later, larger human-video corpus)

## Mentioned in

- [DreamDojo paper](../sources/dreamdojo-paper.md): primary source; includes the release check.
- [GR00T 2 whitepaper](../sources/gr00t-2-whitepaper.md): used as the RL environment (App. F.5).
- [DreamZero paper](../sources/dreamzero-paper.md) and [DreamGen paper](../sources/dreamgen-paper.md): sibling Dream* papers.
- [NVIDIA GEAR publications](../sources/nvidia-gear-publications.md): listed as an ICML 2026 spotlight.
- [AW-0 paper](../sources/agentic-world-action-models-aw0-paper.md): cited as a sibling Dream* paper.
- [GR00T N1 paper](../sources/groot-n1-paper.md): neural trajectories, the pattern DreamGen and DreamDojo later scale up.
- [VP² paper](../sources/vp2-paper.md): asks whether the "capacity doesn't help" result survives at 14B.
- [MBRA paper](../sources/mbra-paper.md): action labels inferred from images, as DreamDojo assumes for human video.
- [PAN world model paper](../sources/pan-world-model-paper.md): compounding error in long rollouts.
- [History-guided video diffusion](../sources/history-guided-video-diffusion-paper.md): whether History Guidance transfers to DreamDojo or Predict2.5.
- [Waymo World Model](../sources/waymo-world-model.md): contrasted as a robotics model that publishes hard numbers.
- Also mentioned in: [Egocentric-vision locomotion](../sources/egocentric-vision-locomotion-paper.md), [RMA](../sources/rma-paper.md), [SmolVLA](../sources/smolvla-paper.md), [Welch Labs guide](../sources/welchlabs-illustrated-guide-to-ai.md).

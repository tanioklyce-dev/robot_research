---
title: Generative data augmentation for robot learning
type: concept
created: 2026-08-27
updated: 2026-08-27
sources: 6
tags: [data-augmentation, synthetic-data, cosmos, cosmos-transfer, dreamgen, mimicgen, imitation-learning, domain-randomization, sim-to-real, vla]
---

**Generative data augmentation** is the practice of multiplying a small corpus of real robot demonstrations into a much larger training set by *generating* the extra data — with a video model, a world model, or a simulator — rather than collecting it on hardware. It exists because the binding constraint on [imitation learning](imitation-learning.md) is robot-hours, and robot-hours are the one input that does not get cheaper with scale.

## The three families, and what each one costs

They are usually lumped together. They should not be — they buy different things and their action labels come from different places.

| Family | What is generated | Where actions come from | Example |
|---|---|---|---|
| **1. Trajectory synthesis in simulation** | New *trajectories* in new object configurations | Replayed/adapted from the source demo; exact by construction | [MimicGen](../../entities/mimicgen.md), [RoboTwin 2.0](../../entities/robotwin.md) |
| **2. Neural trajectory generation** | New *video and new behavior* from a prompt | **Inferred** by an inverse-dynamics model or latent-action model — pseudo-labels | [DreamGen](../../entities/dreamgen.md) |
| **3. Appearance transfer with preserved motion** | New *pixels only*; the trajectory is unchanged | **Reused verbatim** from the original episode — no relabeling at all | [Cosmos 3](../../entities/nvidia-cosmos.md) Transfer video-to-video |

Family 3 is the cheapest and the most limited, and the [Seeed × NVIDIA DLI course](../../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) is the wiki's clearest worked example of it.

## Family 3 in detail: why "actions carry over" is the whole trick

A video-to-video model is given the original episode video, a **structural control signal** extracted from it (Canny edges and/or SAM2 segmentation, optionally depth or blur), and a text prompt describing a *different* scene. The control signal is weighted so heavily — the course's recipe is **edge 0.9 / seg 0.1**, `control_guidance 1.5` — that the robot's geometry and motion are locked in place while the background, lighting, and surfaces are replaced.

Because the arm never moves differently, **the original joint angles and gripper states remain correct labels for the generated video**. There is no inverse-dynamics model, no pseudo-label noise, no relabeling step. One teleop episode becomes N training episodes across N scenes for the cost of N video generations.

That is also exactly the limit: **it can only fix appearance overfitting.** The failure mode it targets is a policy that has latched onto wall color, lighting, or table texture — the course names this directly ("background overfitting"). It cannot add a new grasp, a new object pose, a new recovery behavior, or any new *behavior* at all, because it is definitionally forbidden from changing the trajectory. For behavioral diversity you need family 1 or 2.

The practical footprint, per the course: **Cosmos3-Nano ≈ 24 GB VRAM** (one RTX 4090 / A5000, or a [Jetson AGX Thor](../../entities/jetson-thor.md)); Cosmos3-Super ≈ 4× 80 GB. So family 3 is the only one of the three a single-workstation lab can run without a cluster.

## Does it work?

This is where the wiki has to hedge, because the evidence is uneven across the three families.

- **Family 1 is measured.** [RoboTwin 2.0](../../sources/robotwin2-paper.md) is the wiki's cleanest controlled study: 10 real demonstrations + 1,000 randomized synthetic trajectories beat 10 real demonstrations alone by **+24.4 points averaged**, with the gain *growing* with difficulty (+13.5 easiest, **+33.0** unseen-background-cluttered). Crucially, *clean* synthetic data gave **no** benefit — the entire gain came from diversity, not fidelity. [DexMimicGen](../../entities/mimicgen.md) turns dozens of demos into 780,000 trajectories in 11 hours and those feed [GR00T N1](../../sources/groot-n1-paper.md) pretraining.
- **Family 2 is measured, indirectly.** DreamGen neural trajectories are part of the [GR00T N1.5](../../sources/groot-n1_5.md) pretraining mixture, which lifted real GR-1 language-following from 46.6% to 93.3% — though that release changed several things at once.
- **Family 3 is, so far, unmeasured in this wiki.** The DLI course demonstrates the mechanism, publishes the working weights and the Jetson workarounds, then says of its own output: *"due to the resolution we have set being only 480p and possible issues with the prompt writing, the current outcome is not the best."* It lists the right validation — FID/IS, a **policy transfer test** (train on augmented data, measure real success rate), manual inspection — **and runs none of it.**

> [!warning] Do not read family 1's evidence onto family 3
> RoboTwin 2.0's result is about **behavioral and appearance diversity together, generated in a physics simulator with exact action labels.** Cosmos Transfer supplies appearance diversity only. The mechanism is plausible and the label story is strictly cleaner than DreamGen's — but "randomized synthetic data helps a lot" is not yet an established claim for the video-restyling variant, and the one source that tried it reported an unsatisfying result.

## The tension with controlled environments

The same DLI course that generatively diversifies its backgrounds also requires building a **"Lightbox"** — a light-controlled enclosure with fixed camera mounts — so the real workspace matches the [Isaac Sim](../../entities/nvidia-isaac-sim.md) scene. These are opposite strategies applied to the same problem: one narrows the real distribution to meet the simulator, the other widens the training distribution to cover reality. Using both is not obviously incoherent (constrain what you *record*, diversify what you *train on*), but no source in the wiki has examined whether the augmentation actually recovers the generalization the enclosure gave up. It is an open question and a good experiment.

The deeper version of this is already in [sim-to-real transfer](sim-to-real-transfer.md): RoboTwin 2.0 found that **fidelity was not what closed the gap — diversity was.** Every family here is a diversity engine. The interesting question for each is *which axis of diversity it can actually move.*

## Related concepts

- [Sim-to-real transfer](sim-to-real-transfer.md) — domain randomization is the non-generative ancestor of all of this
- [Real-to-sim-to-real](../robotics/real-to-sim-to-real.md) — reconstructing the specific task as a simulator, then generating in it
- [Imitation learning](imitation-learning.md) — the consumer of all this data
- [VLA models](vla-models.md) — the policies being trained
- [Scaling laws — VLAs and human data](scaling-laws-vla.md) — what more data is worth

## Mentioned in

- [A Sim-to-Real VLA Pipeline with Seeed reBot Arm and NVIDIA Isaac](../../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) — the worked family-3 recipe, weights, Jetson workarounds, and its own negative self-assessment
- [RoboTwin 2.0 Paper](../../sources/robotwin2-paper.md) — the measured family-1 result
- [GR00T N1.5](../../sources/groot-n1_5.md) — DreamGen neural trajectories in the pretraining mix
- [Cosmos 3 Technical Report](../../sources/cosmos-3-technical-report.md) — the model behind family 3
- [NVIDIA GEAR Publications](../../sources/nvidia-gear-publications.md) — MimicGen / DreamGen / RoboCasa lineage

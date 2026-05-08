---
title: Sim-heavy vs real-data paths to generalist policies
type: synthesis
created: 2026-05-07
updated: 2026-05-07
tags: [generalist-policies, vla, imitation-learning, sim-to-real, synthetic-data, world-models]
---

# Sim-heavy vs real-data paths to generalist policies

The simulator survey ([Simulators for agentic robotics — 2026 landscape](simulators-for-agentic-robotics-2026.md) §6) noted a "sim-vs-real divide" between NVIDIA / AGIBOT-style sim-trained generalist agendas and the Hello Robot / RUM-style real-demo agenda. This page works through the comparison and adds a third path the survey didn't fully separate: the **observation-pretraining** path that V-JEPA 2 represents. Three distinct bets on what data robots should learn from.

## The three paths

### Path A — Sim-heavy synthetic-data scaling

Train a generalist policy ([VLA](../concepts/vla-models.md) or BC) almost entirely inside a simulator. Use synthetic-demo expansion ([MimicGen](../entities/mimicgen.md)-style) to multiply human teleop. Bet that **scene diversity + task diversity** generated cheaply in sim transfers to real robots.

- **[RoboCasa](../entities/robocasa.md) / RoboCasa365** ([RoboCasa365 Paper](../sources/robocasa365-paper.md), ICLR 2026) — 612 hr human teleop **expanded ~2.6×** to 1,615 hr synthetic via MimicGen, across 365 tasks / 2,500 kitchens / 3,200+ objects, totaling 500K+ trajectories.
- **[AGIBOT Genie Sim 3.0](../entities/agibot-genie-sim.md)** ([AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)) — open simulation platform with **10,000+ hours synthetic data** and **100,000+ evaluation scenarios**, benchmarking GR00T, Pi, GO-2.
- **NVIDIA Isaac Lab + GR00T** — implicit in the [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md) release; sim-trained VLAs as the production stack.

### Path B — Real-data, viewpoint-locked

Skip the simulator. Collect real demonstrations with a hardware rig that **locks the camera viewpoint** so the same model transfers across embodiments. Bet that **modest data with high environment diversity** is enough for zero-shot generalization on a narrow task set.

- **[Robot Utility Models](../entities/robot-utility-models.md)** (NYU + Meta, [RUM project page](../sources/robot-utility-models-website.md)) — **5,509 real trajectories** across 5 tasks × 180 environments × ~36 envs per task. Custom "Stick V2" gripper with iPhone POV mount keeps camera viewpoint identical across collectors and across [Stretch](../entities/stretch.md) / xArm 7 deployment. **~90% success in unseen environments**, **zero-shot cross-embodiment** Stretch → xArm 7.
- **[stretch_ai](../entities/stretch-ai.md)'s LLM agent** ([Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)) — orthogonal to RUMs as a method, but lives in the same real-only ecosystem; no sim in the agent loop.

### Path C — Observation-pretraining + small interaction

Pretrain a representation or world model on **massive action-free internet video**, then add a small action-conditioned post-training stage on real robot data. Bet that **observation alone** carries most of the signal a robot needs.

- **[V-JEPA 2](../entities/v-jepa-2.md) / V-JEPA 2-AC** ([V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)) — **1M+ hours of internet video** pretraining (action-free) → **62 hr of Droid robot data** post-training → **zero-shot Franka pick-and-place in two new labs**, no robot-specific data, no rewards. The strongest published existence proof of this path so far.
- **[LeWorldModel](../entities/leworldmodel.md)** ([LeWorldModel Paper](../sources/leworldmodel-paper.md)) — companion JEPA at the small end of the same paradigm; argues the recipe works across 60–70× model size and ~5 orders of magnitude data scale.

## Data scale at a glance

| Path | Pretraining data | Robot interaction data | Action-conditioned? | Demonstrated transfer |
|---|---|---|---|---|
| A — Sim-heavy (RoboCasa365) | — | 612 hr human + 1,615 hr synthetic teleop, 500K+ trajectories | Yes (BC + RL) | Sim-internal benchmark; cross-task generalization claimed |
| A — Sim-heavy (Genie Sim 3.0) | — | 10,000+ hr synthetic | Yes | Benchmarks for GR00T / Pi / GO-2 (real-robot transfer not detailed in source) |
| B — Real-data (RUM) | — | 5,509 trajectories (5 tasks × 180 envs) | Yes | **~90% zero-shot**, novel environments + Stretch → xArm 7 cross-embodiment |
| C — Observation pretraining (V-JEPA 2-AC) | 1M+ hr internet video, 22M videos | 62 hr Droid post-training | Yes (post-training only) | **Zero-shot Franka in 2 new labs**, image-goal MPC |

**Order-of-magnitude takeaway**: Path A spends massively on simulated interaction. Path B spends modestly on real interaction. Path C spends massively on action-free observation and **shockingly little** on interaction (62 hr is ~30 days of one robot teleoperating).

## What each path actually demonstrates today

| | Path A (sim-heavy) | Path B (real-data) | Path C (observation pretraining) |
|---|---|---|---|
| Strongest evidence | RoboCasa365's 365-task benchmark; Genie Sim 3.0's 100k+ eval scenarios | RUM's 90% zero-shot novel-env success on 5 tasks | V-JEPA 2-AC's zero-shot Franka deployment |
| Task breadth | High (hundreds) | Narrow (5) | Narrow (image-goal pick/place) |
| Environment generalization | Claimed via scene diversity in sim | Demonstrated on real novel environments | Demonstrated on two new labs |
| Cross-embodiment? | Implicit (one policy, many sim robots) | **Explicit and demonstrated** (Stretch → xArm 7) | Implicit (Franka was new to V-JEPA 2-AC) |
| Real-robot evaluation | Variable — many sim-trained VLAs lack real-deploy results in the sources | Yes — Stretch + xArm 7 | Yes — Franka |
| Sim-to-real burden | High (the entire physics + scene + rendering pipeline exists for this) | None — there is no sim | Low — only the small interaction post-training touches a robot |

The empirical asymmetry is striking. Path B and Path C have **published zero-shot real-robot results in unseen environments**. Path A has the biggest *benchmarks* but the source pages don't surface comparable in-the-wild deployment numbers — the real-world transfer claims for sim-trained VLAs are mostly held by individual VLA papers (GR00T, Pi) that this wiki has not ingested in depth.

## When each path wins (current best read)

- **You need to scale to hundreds of tasks** → Path A. Hand-collecting 5,509 demos per task at RUM's level for 365 tasks is intractable; sim with synthetic expansion is the only path that scales.
- **You need a deployable policy on a small task set in two months** → Path B. RUM's recipe is faster end-to-end than authoring scenes, training in sim, and validating sim-to-real.
- **You can absorb internet video at scale and have access to limited robot interaction** → Path C. This is the most data-efficient path *if* the JEPA / observation-pretraining recipe holds at scale.
- **You want maximum generalization headroom across novel environments and embodiments** → Path B's results are the cleanest demonstration today; Path C's two-lab Franka result is the closest contender. Path A's evidence is mostly intra-sim.

## Where the paths actually meet

> [!note] These paths are not actually independent
> The simulator survey called this out at the bottom of section 6: "the two paths are complementary." This page makes the dependencies explicit.

- **Real-data corpora feed sim pipelines.** RoboCasa365's 612 hr of human teleop is real; the 1,615 hr of synthetic is *expansion* of the real, not a replacement. Path A's synthetic ratio depends on Path B's collection rigs.
- **Sim-trained policies need real targets.** [Stretch](../entities/stretch.md) is the de-facto research robot for both ecosystems. Aaron Edsinger ([Hello Robot](../entities/hello-robot.md) co-founder) is a co-author on the RUM paper — the hardware vendor is explicitly bridging sim and real research agendas.
- **Path C uses neither.** V-JEPA 2's pretraining data is *internet video*, not teleop and not sim. This is the most genuinely orthogonal path; if it scales, it competes with both Path A and Path B's data assumptions, not just one.
- **Sim simulators consume real data too.** [Genie Sim 3.0](../entities/agibot-genie-sim.md) explicitly bills its 10,000+ hours synthetic dataset as "including real-world robot operation scenarios" ([AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)) — i.e. real demos seeded a synthetic-expansion pipeline, then both feed the same training run.

## Implications

1. **The "sim vs real" framing is wrong by 2026.** The interesting axis is *what kind of data substitutes for what*: synthetic teleop for real teleop (Path A), environment diversity for data quantity (Path B), action-free observation for action-conditioned interaction (Path C). The choice is not sim-or-not; it is which substitution you bet on.
2. **Path A scales tasks; Path B scales environments; Path C scales pretraining.** Each path has a different scaling axis, and the costs to scale along each axis are very different. Synthetic teleop in sim is cheap per task but expensive in scene-authoring upfront; real demos are expensive per task but easy to collect on a robot you already have; internet video is essentially free as input but requires large-model engineering.
3. **VLAs and utility-model BC are still distinct.** [RUMs](../entities/robot-utility-models.md) are explicitly **not** language-conditioned ([RUM entity page](../entities/robot-utility-models.md)); [VLAs](../concepts/vla-models.md) are. The "generalist policy" label spans both, but the data and training profiles differ — RUMs lean Path B; VLAs largely lean Path A with Path C contributions.
4. **The biggest unknown is whether Path A's sim-trained VLAs match Path B's real-data BC on the same metric.** No source ingested here runs RUM-style 90% novel-environment success against an Isaac Lab–trained VLA on the same task set. Until that comparison exists, claims about "sim is enough" or "real demos are enough" are hard to settle.

## Open questions

- **Where does Pi (Physical Intelligence) sit?** Genie Sim benchmarks Pi alongside GR00T but Pi's own sim/real data ratio is not in the wiki yet — Pi is on the standing TBD list.
- **Skild AI is similarly absent.** Their "any-robot" generalization claims would help locate them on this map.
- **Tesla Optimus** uses imitation from human video (Path C-adjacent) plus in-house sim (Path A) — this hybrid isn't in the public stacks ingested here.
- **Synthetic data quality plateau**: RoboCasa365's 2.6× synthetic-to-human ratio is the only concrete data point on Path A's optimal mix. Whether higher ratios degrade or improve real-robot transfer is open in the sources.
- **Direct head-to-head**: an experiment training the same VLA architecture with (a) Path A synthetic teleop, (b) Path B real teleop, and (c) Path C observation pretraining + small post-training, then evaluating zero-shot on the same benchmark — would settle most of the debate. Not in the wiki.

## Sources used in this synthesis

- [RoboCasa365 Paper](../sources/robocasa365-paper.md)
- [AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)
- [Robot Utility Models Project Page](../sources/robot-utility-models-website.md)
- [Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)
- [V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)
- [LeWorldModel Paper](../sources/leworldmodel-paper.md)
- [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)

## Related

- [Simulators for agentic robotics — 2026 landscape](simulators-for-agentic-robotics-2026.md) — §6 sketches Path A vs Path B at survey level; this page is the deeper comparison and adds Path C.
- [Generative-video vs JEPA world models](generative-video-vs-jepa-world-models.md) — Path C's underlying architecture choice.
- [LLM-agent architecture across stacks](llm-agent-architecture-across-stacks.md) — orthogonal control paradigm to the policy paradigms above.
- [VLA models](../concepts/vla-models.md) / [Imitation learning](../concepts/imitation-learning.md) — the policy classes consuming all three paths.

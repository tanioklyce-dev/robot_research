---
title: VLA deployability landscape — the four axes (openness, hardware, latency, success)
type: synthesis
created: 2026-07-25
updated: 2026-08-04
tags: [vla, deployability, open-source, open-data, affordable-hardware, inference-latency, landscape-survey, molmoact2, physical-intelligence, smolvla, groot, turbovla, llm-free-vla]
---

A cross-player comparison of the wiki's [VLA models](../../concepts/learning/vla-models.md) along the axes that decide whether a policy can actually be **deployed** — not just whether it tops a benchmark. The framing is borrowed from the [MolmoAct2 paper](../../sources/molmoact2-paper.md) (Fang, Duan et al. 2026), which argues that today's VLAs each fail *at least one* of four deployment criteria, and positions [MolmoAct2](../../entities/molmoact2.md) as the first open model to plausibly satisfy all four at once. This page tests that claim against the other VLAs the wiki tracks.

## The four axes

MolmoAct2's deployment thesis ([§1](../../sources/molmoact2-paper.md)): a policy you can depend on in the real world must clear **all** of these — and most VLAs clear only some.

1. **Openness** — are weights, **training data**, *and* code released? "Open-weights" alone doesn't let a practitioner reproduce, audit, or re-target the model to their own robot.
2. **Hardware accessibility** — does out-of-the-box deployment require an expensive/specialized platform (bimanual [ALOHA](../../entities/aloha.md), mobile manipulators, humanoids), or does it run on low-to-medium-cost arms an academic lab or hobbyist can buy?
3. **Latency** — can it close the control loop in real time, or does a heavyweight reasoning step (hundreds of tokens, predicted goal frames, world-model rollouts) dominate inference before a single action is emitted?
4. **Fine-tuned success rate** — after task-specific adaptation, does it clear the reliability threshold for dependable use, or does it plateau below it?

> [!note] Why "openness" is load-bearing here
> This is [Ai2](../../entities/ai2.md)'s signature argument, running from [OLMo](../../entities/olmo.md) → [Molmo](../../entities/molmo.md) → [MolmoAct2](../../entities/molmoact2.md): the frontier VLAs ([π-series](../../entities/physical-intelligence.md), Gemini Robotics, closed GR00T variants) withhold data and recipes, so practitioners can't adapt them to their own robots or in-house demonstrations. Openness isn't ideology — it's the precondition for the *other three* axes being fixable by anyone other than the original lab.

## The landscape, scored

Scores are directional (✅ strong / ◐ partial / ❌ weak) from the sources ingested here; they compare *deployment posture*, not raw benchmark rank.

> [!warning] The LIBERO numbers in the "fine-tune success" column do not rank these models
> Per the [success-rate audit](vla-success-rate-audit.md), **98.1 / 98.1 / 97.7 / 97.4 / 97.3 / 97.2 / 97.2 / 97.1 / 97.0 / 96.9 are one statistical tie** (ten models as of 2026-08-13, [X-VLA](../../entities/x-vla.md) included) — separating two policies at ~97% needs >1.8 pp at the standard protocol and the whole cluster spans 1.6 pp. Read that column as **"clears the bar" vs "doesn't,"** never as an ordering. The real-world numbers in the same column are better discriminators precisely because the gaps are larger: MolmoAct2's real YAM **+15 pp** over OpenVLA-OFT survives (p=0.00002 aggregated over 400 rollouts), though its companion claim of *winning 7 of 8 tasks* does not (sign test p=0.070).

| VLA | Openness (weights / data / code) | Hardware tier | Latency posture | Fine-tune success | Deployment corner |
| --- | --- | --- | --- | --- | --- |
| **[MolmoAct2](../../entities/molmoact2.md)** (Ai2) | ✅ ✅ ✅ — fully open incl. 3 datasets | ✅ [YAM](../../entities/yam.md) / SO-100 / [DROID](../../entities/droid.md), **<$6k** rig | ✅ 55.8 Hz; [adaptive depth](../../concepts/learning/adaptive-depth-reasoning.md) keeps reasoning cheap | ✅ LIBERO 97.2 / **Think 98.1**; real YAM 50.1% | **All four (the pitch)** |
| **[SmolVLA](../../entities/smolvla.md)** (HF) | ✅ ✅ ✅ — 481 community datasets | ✅ [SO-100](../../entities/so-arm101.md), **~$100-class** | ✅ 450M; async stack; edge-friendly | ◐ strong real SO-100, smaller scale | Open + affordable |
| **[π0.5 / π0.6](../../entities/pi-zero-6.md)** ([PI](../../entities/physical-intelligence.md)) | ◐ some weights; **data + recipe closed** | ❌ bimanual / mobile manipulators | ✅ flow-matching, no reasoning tax | ✅ strong — the baseline MolmoAct2 targets | Performant, closed, expensive |
| **[π0.7](../../entities/pi07.md) / [π*0.6](../../entities/pistar06.md)** (PI) | ❌ data + recipe closed | ❌ expensive platforms | ◐ [KI](../../concepts/learning/knowledge-insulation.md) fast expert, but MEM/world-model add-ons | ✅ frontier real-world (RL-from-deployment) | Frontier, closed |
| **[GR00T N1.x](../../entities/nvidia-groot.md)** (NVIDIA) | ✅ weights + code; data pyramid ◐ | ❌ humanoid ([GR-1](../../entities/fourier-gr-1.md)); ◐ N1.7 adds SO-101 | ✅ dual-system; edge numbers on [Thor](../../entities/jetson-thor.md)/Orin | ✅ LIBERO 96.5–97.0 | Open-weights, humanoid-first |
| **[OpenVLA-OFT](../../entities/openvla-oft.md)** | ✅ weights + recipe | ◐ ALOHA / general | ✅ parallel decoding, **26×** throughput | ✅ LIBERO 97.1 | Open, fast, benchmark-strong |
| **[VLA-0](../../entities/vla-0.md)** (NVIDIA) | ✅ recipe (action-as-text) | ◐ SO-100 real eval | ◐ autoregressive text decode | ✅ LIBERO 94.7 *no pretraining* | Open recipe, minimalist |
| **[Cosmos 3](../../entities/nvidia-cosmos.md)** (NVIDIA) | ✅ weights (OpenMDW) | ◐ DROID-class | ❌ omnimodal world model, heavy | ✅ #1 RoboArena | Open-weights, world-model-heavy |
| **[MolmoAct](../../entities/molmoact.md)** (Ai2) | ✅ ✅ ✅ | ◐ | ❌ **full** depth grid every step | ◐ LIBERO 86.8 | The predecessor — the latency gap MolmoAct2 closes |
| **[TurboVLA](../../entities/turbovla.md)** (HUST/Huawei) | ◐ code announced; **no data release**, but LIBERO/RoboTwin data are public | ✅ [AgileX Piper](../../entities/agilex-piper.md); **0.9 GB fits an [Orin Nano](../../entities/jetson-orin-nano.md)** | ✅✅ **31.2 ms / 32 Hz on a consumer RTX 4090** — no LLM in the loop | ✅ LIBERO 97.7 (tied); [RoboTwin](../../entities/robotwin.md) 60.2 **>** π0.5 57.0 | **The compute corner nothing else occupies** |

## Where the corners cluster

- **Performant-but-closed-and-expensive** — the [π-series](../../entities/physical-intelligence.md). These are the strongest deployed generalist policies (RL-from-deployment, 13-hr espresso runs), but the training data and recipes are proprietary and the out-of-the-box hardware is bimanual/mobile rigs beyond most labs. You can't reproduce them, and you can't cheaply run them. This is exactly the gap the openness argument targets.
- **Open-and-affordable** — [SmolVLA](../../entities/smolvla.md) got here first: fully open, 450M params, runs on a [$100-class SO-100](../../entities/so-arm101.md), async inference stack designed for deployment. Its limitation is scale/performance — it's a smaller model trained on ~10× less data than π0. MolmoAct2 is the argument that you can hold the open+affordable corner **and** match/beat the frontier on performance.
- **Open-weights-but-not-open-data** — [GR00T](../../entities/nvidia-groot.md), [OpenVLA-OFT](../../entities/openvla-oft.md), [Cosmos 3](../../entities/nvidia-cosmos.md). Weights and code are out, but the full training corpus/recipe isn't, so re-targeting to a new robot still depends partly on the originating lab. GR00T is additionally humanoid-first (its out-of-the-box embodiment is a [Fourier GR-1](../../entities/fourier-gr-1.md), not a cheap arm), though N1.7's SO-101 walkthrough softens this.

## A fifth axis the four-axis frame was hiding (added 2026-08-04)

[TurboVLA](../../entities/turbovla.md) ([paper](../../sources/turbovla-paper.md)) breaks this page's scoring in a way worth recording, because the break is informative rather than a bookkeeping problem.

MolmoAct2's axis 3 is **latency**, and this page treats it as satisfied at 55.8 Hz — measured on an **H100**, a caveat flagged above as the page's biggest weakness. TurboVLA hits 32 Hz on a **$1,600 consumer RTX 4090** in **0.9 GB**, and was *trained* on four of them. Those are not the same achievement, and the four-axis frame cannot tell them apart:

**Axis 3 conflates "how fast does it run" with "what must you own to run it."** A policy that needs a data-center GPU to reach 55.8 Hz and a policy that reaches 32 Hz in under a gigabyte are in different deployment universes, and only the second one has any path onto a battery-powered robot. Splitting latency into **rate** and **the compute class required to achieve that rate** re-sorts the table: on *rate* MolmoAct2 leads, on *compute class* nothing here is close to TurboVLA.

This also reframes axis 2. "Hardware accessibility" has meant **the arm** throughout this page — the <$6k rig, the $100-class SO-100. But the [Jetson module ladder](jetson-module-ladder-power-performance.md) note already observed the tension: the *compute* to run the policy is a $2k–$3.5k module, often more than the robot. TurboVLA is the first entry where **the policy's memory footprint is not the binding constraint on the platform** — 0.9 GB clears an 8 GB [Orin Nano](../../entities/jetson-orin-nano.md) with room for perception, ROS, and the OS, where GR00T-3B's 16 GB floor eliminates the board outright.

> [!warning] Two things TurboVLA has not earned here
> **Openness** — code is announced, but there is no data release and, at ingest, no verified checkpoints. It scores ◐, well below the Ai2 line. It is at least *reproducible in principle* on public benchmark data at a compute scale a small lab has, which is a different and cheaper kind of openness than releasing a 720-hour corpus.
>
> **Edge validation** — 31.2 ms is a 4090 number, not a Jetson number, so TurboVLA inherits *exactly* the caveat this page raises against MolmoAct2's H100 figure. It is the more plausible edge candidate by an order of magnitude on memory, and it is equally unmeasured. Do not let the smaller number smuggle in an unproven claim.
>
> **And the success axis remains contingent on [LIBERO-PRO](../../sources/libero-pro-paper.md)** — with no embodied pretraining and no LLM priors, TurboVLA is the most exposed model on this table to the memorization critique. If deleting the LLM costs *robustness* rather than in-distribution accuracy, this row's axis-4 ✅ is the one that flips. See [LLM-free VLA](../../concepts/learning/llm-free-vla.md).

## What MolmoAct2 actually changes

The claim isn't a new capability — it's **occupying all four corners at once**, which no prior *open* VLA had:

- **Openness** — releases weights, code, **and all three robot datasets** (the [720-hr BimanualYAM set](../../entities/yam.md) is the largest open bimanual corpus to date), plus an [open-data FAST tokenizer](../../entities/fast-action-tokenization.md). This is strictly more open than GR00T/OpenVLA-OFT and categorically more open than the π-series.
- **Hardware** — the three deployment embodiments ([YAM](../../entities/yam.md), SO-100/101, [DROID](../../entities/droid.md) Franka) span the low-to-medium cost range; the flagship bimanual rig is **under $6,000 of off-the-shelf parts**. It beats [π0.5](../../entities/pi-zero-6.md) *out-of-the-box* on these cheap platforms, which is the specific inversion of the "open models are tied to expensive hardware" problem.
- **Latency** — instead of paying the reasoning tax on every step, [adaptive depth reasoning](../../concepts/learning/adaptive-depth-reasoning.md) recomputes only the depth cells that changed, and [per-layer KV conditioning](../../concepts/learning/per-layer-kv-conditioning.md) + CUDA-graph caching gets the continuous path to 55.8 Hz. This is the axis MolmoAct2 most directly engineers, and the one its own predecessor [MolmoAct](../../entities/molmoact.md) failed.
- **Success** — top of the wiki's [LIBERO](../../entities/libero.md) table (97.2 / 98.1) *and* a large released real-world suite (real DROID 87.1% zero-shot, real YAM 50.1%, +15 over OpenVLA-OFT) — not just a sim number.

## Caveats and open questions

> [!warning] "Deployable" is validated at H100 latency, not edge latency
> MolmoAct2's 55.8 Hz is measured on a **single H100**. The wiki's on-edge latency thread — [GR00T/π0.5 at 22–24 Hz on Thor](../../sources/nvidia-forum-thor-realtime-vla-inference.md), [SmolVLA/ACT/Diffusion on Jetson Orin Nano](../../sources/cutting-the-cord-untethered-xlerobot.md) — has **not** been run on MolmoAct2. Its backbone is a 4B VLM + a 36-layer action expert; whether that fits a [Jetson Thor](../../entities/jetson-thor.md)/Orin power-and-memory budget at usable rates is unverified here. The "real-world deployment" claim is about openness + platform cost + H100 throughput, not yet about on-robot edge inference. See the [XLeRobot power budget](../projects/xlerobot-thor-power-budget.md) and [GR00T-on-Jetson](gr00t-inference-on-jetson.md) threads for the edge-latency framing this synthesis can't yet apply.
>
> For *which* edge target the question would have to be settled on, see the [Jetson module ladder](jetson-module-ladder-power-performance.md). The short version: memory gates before throughput does. GR00T-3B's stated **16 GB inference floor** already equals an **Orin NX 16 GB**'s entire shared RAM, so a 4B VLM + 36-layer expert realistically implies **AGX Orin 64 GB (5.8 Hz on GR00T-3B) or Thor (10.9 Hz official / 22–24 Hz community)** — and rules out the 8 GB **Orin Nano** that the cheap-hardware axis otherwise points at. Note the tension this creates with axis 2: the **<$6k rig** argument is about the *arm*, while the compute to run the policy on it is a **$2k–$3.5k** module. Whichever tier it lands on, Thor's sub-120 W nvpmodel modes power-gate the GPU 10 → 6 TPC (~−40 %), so a *battery-powered* deployment number would be lower again than any benchmark figure.

- **MolmoAct2-Think's latency tax is still real** — 12.7 Hz vs 55.8 Hz for a +0.9 LIBERO gain. Adaptive depth *reduces* the reasoning cost but doesn't eliminate it; whether the interpretability/robustness gain justifies ~4× the latency is deployment-dependent.
- **Fine-tuned success is still below "dependable"** on the hardest real tasks — MolmoAct2's own real-world YAM average is **50.1%**. It's the best open number by +15, but "best available" and "dependable" are not the same threshold. The deployability bar, on this axis, is raised but not cleared.
- **Adaptive depth's latency win is viewpoint-dependent** — biggest in static third-person setups; egocentric/mobile deployments (where the whole scene moves) offer fewer replayable cells.

## Related
- [Success-rate audit](vla-success-rate-audit.md) — which comparisons in this table survive their sample sizes. **The openness / hardware / latency axes are unaffected; the success axis is where the ties are.**
- [Control-rate ladder](control-rate-ladder.md) — the latency axis widened past VLAs to include servo-loop *requirements* and LLM-in-the-loop inference. Puts this page's H100-vs-edge caveat in its full context: the gap from MolmoAct2's 55.8 Hz to a Franka's 1 kHz servo loop is larger than the gap this page scores.

- [VLA models](../../concepts/learning/vla-models.md) — the action-head taxonomy underneath this comparison.
- [Open-source robot AI projects — landscape](open-source-robot-ai-projects.md) — the broader open-ecosystem catalog this deployability cut sits within.
- [Robot platforms comparison](robot-platforms-comparison.md) — the hardware-side survey.
- [Jetson module ladder — performance and power](jetson-module-ladder-power-performance.md) — the edge-compute ladder any of these policies would have to run on: full SKU specs, memory floors, nvpmodel power modes, and the (sparse) measured on-Jetson VLA rates.
- [Per-layer KV conditioning](../../concepts/learning/per-layer-kv-conditioning.md) / [Adaptive depth reasoning](../../concepts/learning/adaptive-depth-reasoning.md) — the two mechanisms behind MolmoAct2's latency posture.
- [Knowledge insulation](../../concepts/learning/knowledge-insulation.md) — the training recipe shared across the frontier open + closed VLAs.

## Sources

- [MolmoAct2 paper (Fang, Duan et al. 2026)](../../sources/molmoact2-paper.md) — the four-axis framing and MolmoAct2's scores.
- [SmolVLA paper](../../sources/smolvla-paper.md) / [VLA-0 paper](../../sources/vla-0-paper.md) / [OpenVLA-OFT paper](../../sources/openvla-oft-paper.md) / [Cosmos 3 report](../../sources/cosmos-3-technical-report.md) — the open comparators.
- [π0.7](../../sources/pi07-paper.md) / [π*0.6](../../sources/pistar06-paper.md) / [Knowledge Insulation](../../sources/knowledge-insulation-paper.md) papers — the closed-frontier corner.
- [NVIDIA Thor real-time VLA inference](../../sources/nvidia-forum-thor-realtime-vla-inference.md) / [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) — the edge-latency caveat.

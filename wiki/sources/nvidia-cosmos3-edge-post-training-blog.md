---
title: "Post-Train NVIDIA Cosmos 3 Edge for On-Device Robot Control (NVIDIA Technical Blog)"
type: source
url: https://developer.nvidia.com/blog/post-train-nvidia-cosmos-3-edge-for-on-device-robot-control/
local_path: raw/2026-08-19-nvidia-cosmos3-edge-post-training-blog.md
sha256: 9092c9448af1114101a2961806e4e6c351b73c74ae27dc74229983ae573b55ec
author: "Saeed Babamohamadi (NVIDIA, technical marketing engineer, physical AI)"
affiliation: NVIDIA
published: 2026-08-19
venue: "NVIDIA Technical Blog — tutorial; companion to the cosmos-framework repo, the Cosmos3-Edge-Policy-DROID checkpoint and the Cosmos3-DROID dataset"
format: web (vendor tutorial post; text snapshot, video lost)
license: "models and framework under OpenMDW 1.1 (stated in post)"
tags: [nvidia, cosmos, cosmos3-edge, post-training, jetson-thor, droid, robolab, on-device, action-chunking, openpi, world-action-model, lerobot-dataset, so-101, vendor-source]
ingested: 2026-09-12
---

# Post-Train NVIDIA Cosmos 3 Edge for On-Device Robot Control

## Summary

NVIDIA's tutorial for turning the **4B [Cosmos 3 Edge](../entities/nvidia-cosmos.md)** omni-model into a manipulation policy that runs entirely on **[Jetson AGX Thor](../entities/jetson-thor.md)**: post-train on the **Cosmos3-DROID** dataset, serve the checkpoint from a WebSocket server on the robot, run a receding-horizon loop, and score it in closed-loop simulation on **[RoboLab](../entities/nvidia-robolab.md)**. The released **Cosmos3-Edge-Policy-DROID** reaches **22.9%** on RoboLab's 120 tasks (Nano: 36.8%), the first published score for the Edge policy.

Three things in it matter more than the recipe. **First, the latency number the wiki had been carrying was misread**: the post gives **~1.53 s per 32-action chunk** on Thor T5000, and the "15 Hz" of the [launch blog](nvidia-cosmos3-edge-hf-blog.md) is the *playback* rate of those 32 actions (2.13 s of motion), not an inference rate — the model plans at roughly **0.65 Hz** and *"doesn't replan after every observation."* **Second, the post-training cost**: the validated run is **64 nodes × 4 GB200 for ~68 hours (~17.4K GB200-hours)** — *"foundation model post-training, not a single-GPU fine-tune"* — which is what the Thor launch's *"post-train for a specific embodiment in ~a day"* actually means. **Third, the supported-embodiment list includes LeRobot SO101**, the first NVIDIA world-action-model recipe naming a sub-$500 arm.

> [!warning] Vendor tutorial — one policy, one benchmark, no baseline, no trial counts
> Everything is NVIDIA self-reported. The 22.9% is a single aggregate over 120 tasks with **no rollouts-per-task stated** (RoboLab's own [methodology blog](nvidia-robolab-evaluation-blog.md) says ±2 pp needs ≈1,030 rollouts). No non-Cosmos baseline is run. The Aigen "1% real data" anecdote is a customer claim with no numbers. The post is nonetheless the **primary** for the Edge policy's recipe, cost, latency and score, and supersedes secondary readings of the launch blog on those points.

## Key claims

### Latency, precisely

| Quantity | Value | Source line |
|---|---|---|
| Per-chunk inference on Jetson AGX Thor T5000 | **~1.53 s** | *"generates each action chunk in about 1.53 seconds (running at 640×540 resolution and 15 Hz)"* |
| Actions per chunk | **32** at **15 Hz** | Table 1 |
| Motion covered per chunk | **~2.13 s** | *"a single chunk covers roughly 2.13 seconds of robot motion"* |
| Implied replanning rate | **~0.65 Hz** | derived: 1 / 1.53 s |
| Executed prefix in the example loop | **16 of 32** (~1.07 s) | code: `execute_actions(result["action"][:16], hz=15)` |
| Weights on device | **~9 GB BF16** | *"the weights fit in Thor's on-board memory"* |

*"Because the next chunk is ready before the current one finishes, the arm moves continuously… The policy supports continuous streaming on-device by generating action chunks and replanning after each inference cycle. It doesn't replan after every observation."*

> [!note] The example loop and the latency claim do not quite fit together
> The prose argument for continuity is that 1.53 s of inference is shorter than the 2.13 s a full chunk plays. But the reference loop executes only **16** actions (~1.07 s) before calling `infer` again, and it is written sequentially — infer, execute, infer. Unless inference is overlapped with execution (the post does not show that), each cycle stalls ~0.46 s. Either the shipped client pipelines and the snippet is simplified, or the "continuous" claim is for the 32-action case and the 16-action example is a different trade. The [FLUX-mimic](flux-3-launch.md) post is explicit about real-time chunking overlapping execution; this one is not.

**What this corrects.** The [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) and the [Thor page](../entities/jetson-thor.md) had placed Cosmos 3 Edge at "15 Hz" beside GR00T's 10.9 Hz TensorRT and the community's 22–24 Hz — all of which are *inference* rates. On the same axis Cosmos 3 Edge sits at **~0.65 Hz**, below [Diffusion Policy on an Orin Nano](../syntheses/platforms/control-rate-ladder.md) (1.8 Hz). It is in the open-loop-chunk band, like [π0](../entities/pi-zero.md)-style 50-step chunks, not the reactive band. That is not a criticism of the design — chunking is how every flow-matching policy runs — but it changes which row the model belongs on.

### RoboLab closed-loop score

- **Cosmos3-Edge-Policy-DROID: 22.9%** across the **120** language-conditioned tasks; **Cosmos3-Nano: 36.8%**. *"That result is earned at a fraction of the inference compute of larger Cosmos3 variants… precisely the trade Edge is designed to make."*
- Evaluation runs the same OpenPI-protocol policy server against the RoboLab client (Isaac Lab-Arena), executing each chunk in physics and streaming rendered observations back; `--num-envs 10 --headless` for statistics. Isaac Sim 5.x requires RTX Server Driver ≥ 580.

> [!warning] Nano is 36.8% here and 39.7% in the technical report
> The [Cosmos 3 technical report](cosmos-3-technical-report.md) (Table 19) gives Cosmos3-Nano-Policy-DROID **39.7%** on RoboLab-120 *under specific instructions*, versus π0.5's 28.1%. This post says **36.8%** with no instruction-complexity level stated. RoboLab scores on a vague/default/specific language axis, so the two may be different rows of the same table rather than a revision — but the post does not say, and 2.9 points is within the noise RoboLab's own methodology attributes to ~70-rollout evaluations. Treat the Nano figure as **36.8–39.7% depending on instruction specificity, provenance unstated**.

### The post-training run

| Setting | Value |
|---|---|
| Initialization | Cosmos3-Edge checkpoint (4B; **2B Nemotron-based reasoner**) |
| Data | `nvidia/Cosmos3-DROID` — **76k successful teleop trajectories, ~350 h, 86 tasks, 564 scenes**, [Franka Panda](../entities/franka-panda.md) + Robotiq; LeRobotDataset v3.0 at 640×360 |
| Curation | filter idle/non-task frames; success split only; random crop / rescale / colour jitter |
| Action space | **8-D absolute joint position** (7 + gripper), **raw values, no normalization** |
| Observation | 3-camera canvas: wrist 360×640 over two exterior 180×320 → **540×640** |
| Action heads | freshly initialised encoder + decoding MLP + embedding tokens, **5× LR** |
| Loss | vision flow-matching weighted to match the action loss |
| Optimisation | lr 2e-4, **global batch 8192** (32/rank × 256 ranks, HSDP 32×8), long-cosine (cycle 100K) |
| Compute | **64 nodes × 4 GB200, 60K iterations, ~68 h ≈ 17.4K GB200-hours** |
| Validated hardware | DGX Station GB200 / GB300; **CUDA 13.0 (cu130), NGC 26.06-py3** |

- *"This is foundation model post-training, not a single-GPU fine-tune… Plan compute accordingly."* At list cloud rates this is on the order of a mid-five-figure dollar run; it is the number that decides whether *post-train Cosmos 3 Edge yourself* is available to a small lab (it is not) versus *use the shipped DROID policy* (it is).
- **Internal inconsistency**: the prose says 60K iterations; Table 1 says *"a 10K-iteration run"* with checkpoints every 1K. One of them is wrong, or the table describes a shorter reference schedule.
- The Edge recipe is the Nano recipe with three edits (swap `NANO_MODEL_CONFIG` for `EDGE_MODEL_CONFIG`, point at the Edge DCP checkpoint, rename the launcher) — *"Everything else, including dataset, action space, curation filter, and training schedule, stays the same."*

### Bring your own robot

- Data in **LeRobot Dataset v3** (per-frame video, joint states, gripper, actions, task instruction). For DROID-like Franka the only change is the dataset path; a new embodiment needs its own experiment config (action space, dimensionality, camera layout, normalization).
- **Embodiments the model card lists**: dual-arm Franka, **UR**, **WidowX 250**, **LeRobot [SO101](../entities/so-arm101.md)**. This is the first Cosmos policy source to name the SO-101 — the hobbyist arm the wiki tracks as its default low-cost platform — though nothing here says the SO-101 has been post-trained or scored.

### Deployment on Thor

- Served by a **WebSocket policy server speaking the OpenPI protocol**, *"the same protocol used across the DROID policy ecosystem"*; client sends an observation dict, server returns `[32, 8]` actions. `host="localhost"` — *"the request never leaves the robot."*
- **`TORCHDYNAMO_DISABLE=1` is required on Thor**: *"stock Triton wheels lack sm_110a kernels."* Another entry in the Thor software-maturity ledger beside the cuBLASLt patch on the [Thor page](../entities/jetson-thor.md).
- **State-conditioned**: joint and gripper positions are real inputs; the smoke test feeds zeros and only proves the server returns a well-formed chunk. Each replan *"starts from where the arm actually is rather than where the previous chunk assumed it would be."*
- Starting the server with video decoding enabled **returns the model's imagined rollout alongside the actions** — the [world-action-model](../concepts/world-models/world-action-model.md) property exposed at the API.

### Beyond control

- **Aigen** post-trained Cosmos for synthetic crop/weed variation, *"enabling an autonomous weeding system to achieve strong performance using just 1% real-world data."* Customer anecdote; no numbers, no baseline.
- Models and framework under **OpenMDW 1.1**.

## Contradictions and tensions

- **Reasoner provenance.** This post says Edge carries a *"2B NVIDIA [Nemotron](../entities/nemotron.md)-based reasoner"*; the [technical report](cosmos-3-technical-report.md) describes the family's reasoner tower as initialised from Qwen3-VL. Either Edge differs from Nano/Super, or the family moved to Nemotron after the report. Unresolved.
- **"~A day" vs 68 hours on 256 GB200s.** The [Thor T3000/T2000 launch](nvidia-jetson-thor-t3000-t2000-blog.md) said Edge *"can post-train for a specific embodiment in ~a day."* This is the primary for what that day costs.
- **Rate placement** — see [Latency, precisely](#latency-precisely). Not a contradiction in the sources; a correction to how the wiki read them.

## Entities mentioned

- [NVIDIA Cosmos](../entities/nvidia-cosmos.md) — Cosmos 3 Edge, Nano; the cosmos-framework repo.
- [Jetson Thor](../entities/jetson-thor.md) — AGX Thor T5000 as the on-device target; the Triton/sm_110a workaround.
- [RoboLab](../entities/nvidia-robolab.md) — the closed-loop benchmark; 22.9% / 36.8%.
- [DROID](../entities/droid.md) — the Cosmos3-DROID success-split repackaging (76k trajectories, ~350 h).
- [Franka Panda](../entities/franka-panda.md) — the dataset's arm, with Robotiq gripper.
- [SO-ARM101](../entities/so-arm101.md) — named as a supported embodiment.
- [Nemotron](../entities/nemotron.md) — the 2B reasoner.
- [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) — Isaac Lab-Arena, behind RoboLab.
- [LeRobot](../entities/lerobot.md) — Dataset v3 as the ingest format.

## Concepts touched

- [World-action model](../concepts/world-models/world-action-model.md) — the imagined rollout returned beside the actions.
- [Control-rate ladder](../syntheses/platforms/control-rate-ladder.md) — 32 actions per 1.53 s inference, a prefix executed per cycle; where the model actually sits on the ladder.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — sim-before-real closed loop, no trial counts.
- [VLA models](../concepts/learning/vla-models.md) — the DROID-policy ecosystem and OpenPI protocol.

## Open questions

- **Rollouts per task** behind 22.9%. Unstated.
- **Which RoboLab instruction level** the 36.8% and 22.9% use, and whether 36.8% vs the report's 39.7% is a row difference or a revision.
- **Does the shipped client overlap inference with execution?** The snippet does not; the prose claims continuity.
- **60K or 10K iterations?**
- **Any real-robot result** for the Edge policy. None here — RoboLab only.
- **SO-101 post-training**: listed as supported; no data, config, or score shown.

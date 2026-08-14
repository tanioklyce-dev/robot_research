---
title: NVIDIA GR00T
type: entity
subtype: product
created: 2026-05-06
updated: 2026-07-08
sources: 46
tags: [groot, vla, nvidia, foundation-model, humanoid]
---

NVIDIA's open, commercially-licensed [VLA](../concepts/learning/vla-models.md) foundation model line for humanoid robots. The flagship policy that ships with NVIDIA's Physical AI stack ([NVIDIA Isaac Lab](nvidia-isaac-lab.md), [NVIDIA Isaac Sim](nvidia-isaac-sim.md)). **Both site champions of the [October 2025 Seeed × NVIDIA × HF Embodied AI Hackathon](../sources/seeed-embodied-ai-hackathon-2025-recap.md) ran GR00T N1.5** (fine-tuned via NVIDIA Brev) on non-humanoid dual-arm platforms (XLeRobot, SO-ARM101) — the strongest external signal yet that GR00T fine-tunes work at weekend-hackathon data scales (150–300 episodes) outside the humanoid form factor it was designed for.

## Version history

A clear ~quarterly cadence, with a **backbone progression Eagle → Cosmos-2B → Cosmos-Reason2-2B** and a steady move toward reasoning-integrated, cross-embodiment, whole-body control. All releases keep the **3B / dual-system (VLM + flow-matching DiT)** shape.

| Version | Date | VLM backbone | Key change | Checkpoint |
|---|---|---|---|---|
| **N1** | 2025-03 | [Eagle](eagle-vlm.md)-2 (SmolLM2 + SigLIP-2) | dual-system VLA + data pyramid; VLM **unfrozen** | `nvidia/GR00T-N1-2B` |
| **N1.5** | 2025-06-11 | [Eagle](eagle-vlm.md) 2.5 | VLM **frozen** + [FLARE](../concepts/world-models/flare.md) loss; huge language-following gains | `nvidia/GR00T-N1.5-3B` |
| **N1.6** | 2025-12-15 | Cosmos-2B variant | reasoning-integrated backbone; DiT 16→32 layers; state-relative actions | `nvidia/GR00T-N1.6-3B` |
| **N1.7** | **GA 2026-04-18** (repo README); LeRobot 2026-07-07 | Cosmos-Reason2-2B (Qwen3-VL) | 20K-hr EgoScale human video; relative-EEF action space; **state/action dims 29→132, action horizon 16→40**; native [LeRobot](lerobot.md) integration; **N1.5 dropped** | `nvidia/GR00T-N1.7-3B` |

- **N1** — **GR00T N1: An Open Foundation Model for Generalist Humanoid Robots** ([arXiv 2503.14734](https://arxiv.org/abs/2503.14734)); full paper ingested — see [GR00T N1 Paper](../sources/groot-n1-paper.md). ~50 contributors; research leads [Jim Fan](jim-fan.md) + [Yuke Zhu](yuke-zhu.md).
- **N1.5** ([research page](../sources/groot-n1_5.md)) — **frozen** [Eagle 2.5](eagle-vlm.md) VLM + simplified adapter + **[FLARE](../concepts/world-models/flare.md)** (Future LAtent REpresentation Alignment) loss (coef 0.2) + [DreamGen](dreamgen.md) neural trajectories. **Real GR-1 language-following 46.6% → 93.3%, success 43.3% → 83.0%**; RoboCasa 30-demo 17.4 → 47.5; [Unitree G1](unitree-g1.md) seen-objects 44.0% → **98.8%** (first strong non-GR-1 humanoid result). Won both sites of the October 2025 Seeed × NVIDIA × HF Embodied AI Hackathon (fine-tuned via [NVIDIA Brev](nvidia-brev.md); deployed on [Jetson Thor](jetson-thor.md)).
- **N1.6** ([research page](../sources/groot-n1_6.md)) — **internal Cosmos-2B VLM variant** trained on embodied-reasoning + general VL; DiT doubled to 32 layers; adapter removed, top-4 VLM layers unfrozen; **state-relative action chunks**; adds bimanual YAM / AGIBot Genie1 / Galaxea R1 Pro (BEHAVIOR) / Unitree G1 whole-body loco-manip data. "Outperforms N1.5" (no published numbers). Also the version newly available in [Isaac Lab](nvidia-isaac-lab.md) alongside Newton 1.0 GA at GTC 2026 ([Newton blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)).

> [!note] The N1.5/N1.6 whole-body controller has a name: **"Decoupled WBC"**. The [GR00T-WholeBodyControl repo](../sources/gr00t-wholebodycontrol-github.md) ships a `decoupled_wbc/` directory described as *"controllers used in GR00T N1.5 and N1.6"* — distinct from the [GEAR-SONIC](gear-sonic.md) controller used with N1.7's `UNITREE_G1_SONIC` tag. No standalone Decoupled-WBC paper is cited.
- **N1.7** (GA per [repo README](../sources/isaac-gr00t-github.md): 2026-04-18) — 3B, **Cosmos-Reason2-2B (Qwen3-VL) backbone, flexible resolution** (confirmed via [Isaac-GR00T repo](../sources/isaac-gr00t-github.md)); **state/action dimensions expanded 29 → 132 and action horizon 16 → 40** (README-only claim, no ablations published); **[EgoScale](../sources/egoscale-paper.md) pretraining on 20,854 h of egocentric human video**; shared relative-EEF action space across robot + human embodiments; whole-body [Unitree G1](unitree-g1.md) via the `UNITREE_G1_SONIC` tag + the **[GEAR-SONIC](gear-sonic.md)** controller ([paper](../sources/sonic-paper.md)) — a GR00T N1.5 VLA predicts SONIC universal-motion tokens for autonomous whole-body loco-manipulation (5-task avg 75%). EgoScale (Zheng et al., NVIDIA GEAR, Feb 2026) publishes the log-linear scaling law `L = 0.024 − 0.003·ln(D)` (R² = 0.9983) — see [Scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md).

> [!note] Version overlap resolved — and EA→GA timeline caveat
> The earlier "N1.6 vs N1.7 EA in parallel" ambiguity was a normal GA-plus-EA pattern: N1.6 (Dec 2025, Cosmos-2B) was the last stable release while N1.7 was in early access. The [repo README (re-ingested 2026-07-07)](../sources/isaac-gr00t-github.md) now dates **N1.7 GA to 2026-04-18** — which predates the wiki's 07-04 ingest that still recorded "EA"; the GA labeling may have been added retroactively (see the contradiction callout on the source page). N1.5/N1.6 remain on release branches; N1.5 is unsupported.

### N1.7 GA in LeRobot (2026-07-07)

The [NVIDIA HF blog](../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md) graduates N1.7 to general availability **inside [LeRobot](lerobot.md)** (`--policy.type=groot`, base `nvidia/GR00T-N1.7-3B`), branding it "the latest open, commercially viable VLA foundation model" and stating **N1.5 is no longer supported**. LeRobot and the [Isaac-GR00T](../sources/isaac-gr00t-github.md) open-source path use **identical weights**; post-training requires **LeRobot Dataset v3.0** (a step past the "flavor of LeRobot v2" the repo consumed). **First published N1.7 benchmark numbers** — [LIBERO](libero.md) avg **96.5% vs 87%** for GR00T 1.5 (Spatial 95 vs 82, Object 100 vs 99, Goal 98 vs n/a, Long 93 vs 82; NVIDIA-reported self-comparison), with per-suite fine-tuned checkpoints released (`nvidia/gr00t17-lerobot-libero_*-640`). The reference fine-tune recipe targets the **$100-class [SO-101](so-arm101.md)** (relative actions excluding gripper, chunk 16, bf16, 20k steps, batch 64), with demonstrations collected via the new [Isaac Teleop](nvidia-isaac-teleop.md) framework (leader arm or XR headset) — the first-party version of the GR00T-on-affordable-LeRobot-hardware pattern the [Seeed hackathon champions](../sources/seeed-embodied-ai-hackathon-2025-recap.md) improvised with N1.5.

## Codebase — [Isaac-GR00T](../sources/isaac-gr00t-github.md)
Apache-2.0 code (weights under NVIDIA Open Model License), ~7.5k★. LeRobot-v2 data format + `modality.json`; **embodiment tags** (`LIBERO_PANDA`, `OXE_DROID_…`, `UNITREE_G1_SONIC`, `NEW_EMBODIMENT`) drive cross-embodiment fine-tuning. Inference 16 GB+ VRAM, fine-tune 40 GB+; runs on [Jetson Thor](jetson-thor.md) / [Orin](jetson-orin-nano.md) / [DGX Spark](dgx-spark.md). PyTorch 2.7 + flash-attn 2.7.4 + `uv`.

### Inference performance (edge)

First measured latency numbers, from the [official TensorRT deployment docs](../sources/isaac-gr00t-tensorrt-deployment-docs.md) (benchmarks **N1.6-3B** — no N1.7 numbers published yet) and a [community forum report](../sources/nvidia-forum-thor-realtime-vla-inference.md): **[Jetson Thor](jetson-thor.md) 92 ms / 10.9 Hz** official TensorRT (22–24 Hz with community hand-written CUDA kernels), **Jetson AGX Orin 173 ms / 5.8 Hz** TensorRT (300 ms eager), RTX 5090 31 ms / 32.1 Hz. The official recipe compiles only the DiT action head (VLM stays PyTorch eager); BF16 recommended. Orin NX 16 GB is unbenchmarked and sits at the 16 GB memory floor — use the ZMQ policy server off-board instead. Full analysis: [GR00T inference on Jetson](../syntheses/platforms/gr00t-inference-on-jetson.md).

## N1 architecture & data (from the primary paper)

- **Dual-system VLA** ([GR00T N1 Paper](../sources/groot-n1-paper.md)): Eagle-2 VLM (SmolLM2 + SigLIP-2; System 2, 10 Hz) + flow-matching Diffusion Transformer (System 1, 120 Hz), trained jointly end-to-end. GR00T-N1-2B = 2.2B params (1.34B VLM); 16-action chunk in 63.9 ms on an L40; K=4 Euler steps at inference; VLM features taken from middle layer 12.
- **Data pyramid**: 8,375.7 h total pretraining corpus — real robot 3,288.8 h + human video 2,517 h + DexMimicGen sim 1,742.6 h + **827 h of video-model-generated "neural trajectories"** (~10× multiplier over the 88 h of in-house GR-1 teleop). ~50k H100 GPU-hours to pretrain.
- **Headline results**: real [Fourier GR-1](fourier-gr-1.md) tabletop 76.8% vs Diffusion Policy 46.4%; 10%-data GR00T within 3.8 points of full-data DP; sim average 45.0% vs DP 33.4% at 100 demos.
- Extends the [LeRobot](lerobot.md) dataset format (`modality.json`, rotation-representation semantics) — the concrete lineage behind GR00T's presence in LeRobot-ecosystem tooling like [Rosetta](rosetta.md).

## Related
- [NVIDIA GEAR](nvidia-gear.md) — research lab; co-leads ([Jim Fan](jim-fan.md) + [Yuke Zhu](yuke-zhu.md)) own the GR00T program.
- [Eagle VLM](eagle-vlm.md) — VLM backbone through N1.5 (Eagle-2 → Eagle 2.5).
- [DreamGen](dreamgen.md) — source of the neural-trajectory synthetic data; [FLARE](../concepts/world-models/flare.md) — N1.5's auxiliary loss; [GEAR-SONIC](gear-sonic.md) — the whole-body controller under the `UNITREE_G1_SONIC` tag.
- [NVIDIA Cosmos](nvidia-cosmos.md) — backbone from N1.6 (Cosmos-2B → Cosmos-Reason2-2B).
- [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — bundled training/eval framework.
- [VLA models](../concepts/learning/vla-models.md) — concept page.
- [AGIBOT Genie Sim 3.0](agibot-genie-sim.md) — third-party benchmark that tests GR00T.

## Mentioned in
- [GR00T N1 Paper](../sources/groot-n1-paper.md) — **primary source (N1)**
- [GR00T N1.5 research page](../sources/groot-n1_5.md) — frozen VLM + FLARE
- [GR00T N1.6 research page](../sources/groot-n1_6.md) — Cosmos-2B backbone + state-relative actions
- [Isaac-GR00T GitHub](../sources/isaac-gr00t-github.md) — the official codebase (N1.7 EA default)
- [NVIDIA Isaac Teleop and GR00T 1.7 in LeRobot (HF blog)](../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md) — N1.7 GA in LeRobot; LIBERO numbers; N1.5 deprecation
- [NVIDIA + HF LeRobot partnership blog](../sources/nvidia-hf-lerobot-open-robotics-blog.md) — corporate umbrella; brands 1.7 "the **first** open and commercially viable robot foundation model" (HF blog says "latest")
- [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)
- [Top 10 Physical AI Models 2026](../sources/top-10-physical-ai-models-2026.md)
- [AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)
- [Seeed × NVIDIA × HF Embodied AI Hackathon 2025 Recap](../sources/seeed-embodied-ai-hackathon-2025-recap.md)
- [Isaac GR00T docs — TensorRT optimization](../sources/isaac-gr00t-tensorrt-deployment-docs.md) — official edge-inference latency (Thor 10.9 Hz, AGX Orin 5.8 Hz; N1.6)
- [NVIDIA forums — real-time VLA inference on Thor & RTX](../sources/nvidia-forum-thor-realtime-vla-inference.md) — community 22–24 Hz on Thor
- [NVIDIA GEAR Lab — Publications](../sources/nvidia-gear-publications.md)
- [EgoScale Paper](../sources/egoscale-paper.md)
- [DreamDojo Paper](../sources/dreamdojo-paper.md)

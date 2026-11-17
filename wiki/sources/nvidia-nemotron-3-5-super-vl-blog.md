---
title: "NVIDIA Nemotron 3.5 Super VL Powers Specialized Agents with Multimodal Reasoning (NVIDIA blog)"
type: source
url: https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/
fetch_url: https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/
local_path: raw/2026-11-17-nvidia-blog-nemotron-3-5-super-vl.md
sha256: d7de61df02e1a6682be528d44543e5658a21ed301104890bf1f80573a62786c5
author: Chris Alexiuk and Chintan Patel (NVIDIA)
published: 2026-10-15
ingested: 2026-11-17
venue: NVIDIA Technical Blog
format: "vendor launch post with one table and six figures. Page metadata shows it was modified 2026-11-09; this capture is of that version. Text captured via curl with article extraction; Figures 1-4 saved in raw/assets/nemotron-3-5-super-vl/ and read for the values below. Figures 5 and 6 were read from their captions and alt text only."
tags: [nemotron, nemotron-3-5-super-vl, nvidia, open-weights, moe, vlm, multimodal, agents, post-training, nvfp4, speculative-decoding, mamba, dgx-spark, nim, dynamo, hermes-agent, openclaw, vendor-source]
---

# NVIDIA Nemotron 3.5 Super VL Powers Specialized Agents with Multimodal Reasoning

## Summary

NVIDIA's launch post for **Nemotron 3.5 Super VL**, an open-weights multimodal model in the [Nemotron](../entities/nemotron.md) family: a **120B-parameter mixture-of-experts that "activates 12B parameters per token"**, taking text, images, documents and video. The pitch is not that it is the most capable open model. It is that it is fast, that one model replaces a text model plus a vision-language model, and that customers who post-train it on their own workflow beat frontier models on that workflow. The post names its engineering: distillation from Nemotron 3 Ultra, a speculative-decoding method called LiLiCorr, 4-bit NVFP4 quantization with quantization-aware distillation, multi-token prediction, and cache reuse across agent turns. Robotics, Jetson and physical AI are not mentioned anywhere in it.

## Key claims

### The model
- "An open, customizable multimodal model"; "120B-parameter mixture-of-experts (MoE) architecture activates 12B parameters per token." Checkpoint name: `NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4`.
- A "hybrid architecture": the serving notes refer to preserving "both attention caches and Mamba recurrent states," so the backbone mixes attention with Mamba layers.
- "Distilled from Nemotron 3 Ultra," with a "SkewReverse loss," then "multi-teacher on-policy distillation (MOPD)" from specialised text and vision teachers.
- Visual training covers "charts, tables, optical character recognition (OCR), multipage documents, and video understanding" through "a two-stage SFT pipeline."
- **Where it sits in the family**: "Smaller models, such as NVIDIA Nemotron 3.5 Lightning, handle high-volume text tasks, while frontier models such as NVIDIA Nemotron 3 Ultra tackle complex planning and orchestration."
- The release "includes base, post-trained, and NVFP4-quantized checkpoints with training recipes, data, and reinforcement-learning environments," plus open datasets including "40 vision-language datasets" and an Indic corpus of "about 2.8T tokens across 22 Indian languages."

### Speed and accuracy, as charted

**Figure 1** (Artificial Analysis Intelligence Index against output speed, open-weights models, 100K input tokens; values read from the chart):

| Model | Index | Output tokens/s |
|---|---:|---:|
| GLM-5.3-Flash | ~42 | ~65 |
| Qwen3.8-Flash-Next | ~40 | ~60 |
| DeepSeek V4.1 Flash (max) | ~39 | ~225 |
| Qwen3.8 27B (xhigh) | ~34 | ~75 |
| **Nemotron 3.5 Super VL** | **~27** | **~625** |
| Inkling Small | ~26 | ~125 |
| Nemotron 3 Ultra | ~23 | ~195 |
| Nemotron 3 Super | ~13 | ~140 |

The "5x" is drawn against Inkling Small, the one model at a similar index. The caption says the speed was measured "on the Baseten endpoint."

**Figure 3** (SWE-bench Pro accuracy against hours to finish 10,000 tasks on 4× B200, all at NVFP4):

| Model | Accuracy | Hours |
|---|---:|---:|
| Qwen3.8 Flash Next | ~60 | ~50 |
| DeepSeek V4 Flash | ~57 | ~56 |
| Inkling Small | ~56 | ~118 |
| **Nemotron 3.5 Super VL** | **~51** | **~10** |

**Table 1** (as printed):

| Model | Hermes Bench | LangChain Evals |
|---|---:|---:|
| Nemotron 3 Ultra | 56.33% | 84.3% |
| Nemotron 3.5 Super VL | 63.44% | 87.05% |

- CharXiv chart reasoning: 80.8%, against 63% for Nemotron 3 Nano Omni; 84% with a Python interpreter.
- "One of the top open models on the OCRBench v2 leaderboard." No figure given.
- "Outperforms Nemotron 3 Super on SWE-bench and Terminal-Bench." No figures given.

### On DGX Spark (Figure 4)

"An independent evaluation by EXO Labs placed Nemotron 3.5 Super VL on the Pareto frontier for accuracy and task completion time." The chart itself is branded local.ai. Values read from it (index 0–100; end-to-end agentic task time, log scale):

| Model | Index | Task time |
|---|---:|---:|
| Qwen 3.8 Flash Next | ~90 | ~12 min |
| Qwen 3.8 27B (off frontier) | ~83 | ~30 min |
| **Nemotron 3.5 Super VL** | **~80** | **~6.5 min** |
| Qwen 3.6 35B A3B | ~67 | ~4.7 min |
| Ornith 1.0 35B | ~67 | ~3 min |
| Nemotron 3.5 Lightning | ~55 | ~2 min |
| Gemma 4 E4B | ~28 | ~1 min |
| Gemma 4 E2B | ~24 | ~40 s |
| LFM2.5 8B A1B | ~11 | ~20 s |

- LiLiCorr "is the recommended drafter for low-latency inference" on DGX Spark, "up to 2.3x faster token generation than decoding without speculation."

### Post-training results (Figure 2)

| Workflow (partner) | Frontier model | Base Super VL | Post-trained | Labeled gain |
|---|---:|---:|---:|---:|
| Document intelligence (Scale AI, Skydance) | Claude Opus 5 ~83% | ~71% | ~86% | +15% |
| Security attack resilience (AI21, Alice) | GPT-6.1 Sol ~66% | ~35% | ~76% | +41% |
| Financial receipt extraction (Ramp) | GPT-6 Luna ~92% | ~85% | ~94% | +9% |
| Scientific experimentation (Lila) | GPT-6 Astra ~54% | ~31% | ~61% | +30% |
| Medical insurance claims | Claude Opus 5 ~37% | ~28% | ~72% | +44% |

Bar heights are read from the chart; the gain labels are printed. Text claims alongside: Scale AI's workload "will decrease" inference cost "by 40x and latency by 5x"; Ramp "expects up to 50% higher throughput and 10x lower latency."

### Inference engineering
- **LiLiCorr**: speculative decoding that scores token candidates "across an entire draft" with "a lightweight network... in a single pass."
- **NVFP4**: "4-bit weights and activations on the NVIDIA Blackwell architecture"; the same checkpoint runs elsewhere "with 4-bit weights and 16-bit activations." Quantization-aware distillation trains the quantized model "to match the outputs of the original BF16 model," and lets the KV cache be stored in NVFP4.
- **Multi-token prediction**: "an internal drafter that proposes several tokens for the main model to verify in one forward pass."
- **Context reuse**: prefix caching of "system instructions, tool definitions, and conversation history," with extra Mamba state checkpoints.
- **Dynamo**: on 16 B200 GPUs at 50 tokens/s per user, KV-aware routing "serves up to 8x as many users while reducing first-token latency by 85%."

### Ecosystem
- Evaluated across "Hermes, LangChain, OpenClaw, OpenCode, Pi, Codex, and Claude" harnesses.
- Built "with support and expertise from Nemotron Coalition organizations," naming Perplexity (datasets) and Prime Intellect (environments).
- Runtimes listed include Ollama, LM Studio, vLLM, SGLang, Unsloth and Exo.

## Reading it critically

- **It is the fastest model on its own charts and never the most accurate.** On Figure 1 at least five open models score higher on the index, by up to about 15 points. On Figure 3 it has the lowest SWE-bench Pro accuracy of the four shown. The "5x" and "4x" are real on the page and are speed comparisons at lower accuracy.
- **"Compared to other open models in its size category" is one model.** The 5x arrow goes to Inkling Small. DeepSeek V4.1 Flash is plotted at about 225 tokens/s with a higher index, which is under 3x.
- **The mid-size model beats the family's "frontier" model.** Super VL outscores Nemotron 3 Ultra on both rows of Table 1 and on the Figure 1 index, while the text assigns Ultra the harder planning work. The post does not explain this.
- **The post-training comparison is tuned against untuned.** Every base Super VL bar is below the frontier model it is compared with. The specialised version wins after training on the partner's task; the frontier models were not adapted. That is a fair description of the product and not evidence about the models' general capability.
- **"+41%" is percentage points** on the chart (about 35 to 76), which is more than a doubling in relative terms. The text's "improving accuracy by 41%" does not say which.
- **Cost and latency figures are forecasts**: "will decrease," "expects."
- **"Independent evaluation by EXO Labs"** is shown as a local.ai-branded chart, the model is NVIDIA's, the hardware is NVIDIA's, and Exo is listed as a partner. The index is not defined in the post.
- **No trial counts, harness settings or thinking budgets** for any number. Several figure files carry "updated" in their names, and the page was modified on 2026-11-09, 25 days after publication, with no changelog.

## Why it is in this wiki

- It fills in the [Nemotron](../entities/nemotron.md) family, which the wiki knew only through Lightning, Bolt and ASR as components of NVIDIA's agent stacks.
- **Figure 4 is a rare per-task latency ladder for local agents on one box.** On a [DGX Spark](../entities/dgx-spark.md), the capable end of the open-model range takes 5 to 12 minutes per agentic task and the fast end takes under a minute at a quarter of the score. That is the planning-tier budget an on-robot or beside-robot agent would inherit; see [on-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md).
- It ships with [Hermes Agent](../entities/hermes-agent.md) and [OpenClaw](../entities/openclaw.md) named as supported harnesses, both of which the wiki tracks as robot-agent candidates.
- **What it does not offer**: any embodied-reasoning benchmark, any robot result, or a Jetson target. Its video understanding is pitched at "search, content review, and incident analysis."

## Entities mentioned
- [Nemotron](../entities/nemotron.md) · [NVIDIA](../entities/nvidia.md) · [DGX Spark](../entities/dgx-spark.md)
- [Hermes Agent](../entities/hermes-agent.md) · [OpenClaw](../entities/openclaw.md) · [Qwen](../entities/qwen.md) · [Gemma 4](../entities/gemma4.md) · [GPT-6 Astra](../entities/gpt-6-astra.md) (comparator)
- No entity pages: Artificial Analysis, EXO Labs / local.ai, Scale AI, Ramp, AI21, Baseten, Inkling Small (Thinking Machines), NVIDIA Dynamo, NIM

## Concepts touched
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md): a tiered system of models (Lightning, Super VL, Ultra)
- [Local-model harness design](../concepts/agents/local-model-harness-design.md): harness-specific evaluations, context reuse across turns

## Open questions
- **The technical report** linked from the post is the primary for architecture and benchmarks and is not ingested.
- What changed in the 2026-11-09 revision.
- How Super VL relates to Nemotron 3.5 Bolt (74B, 9B active), which the wiki knows only from a checkpoint name.
- Whether it runs on Jetson Thor, and at what speed. The post lists DGX Spark as the local target and nothing smaller.
- The definition and task set of the local.ai index, and who ran it.
- Any embodied or spatial-reasoning evaluation of its vision side.

## Related sources
- [NVIDIA Local AI blog series, Aug 2026](nvidia-local-ai-blog-series-2026-08.md): the Nemotron 3.5 Lightning launch.
- [Using AI agents to teach Microduck to walk in simulation](nvidia-microduck-ai-agents-sim-blog.md): Nemotron 3.5 Bolt as a local planner.
- [A Local-First Agent for Private and Cost-Effective Knowledge Work](perplexity-local-first-agent-research.md): Perplexity on small local models, and a Nemotron Coalition member here.

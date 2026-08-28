---
title: "Gemma 4 Powers Open Duck Mini: Meet Autumn, the On-Device AI Robot Duck (explainx.ai)"
type: source
url: https://explainx.ai/blog/gemma-4-open-duck-mini-robot-on-device-ai-2026
author: Yash Thakker (AISOLO Technologies Pvt Ltd)
published: 2026-06-15
ingested: 2026-08-27
venue: explainx.ai blog
format: secondary blog post, ~7 min read; updated 2026-08-27 with a Microduck note
tags: [open-duck-mini, gemma4, google-io-2026, on-device, raspberry-pi-5, jetson-orin-nano, litert, secondary-source, source-quality]
---

# Gemma 4 Powers Open Duck Mini (explainx.ai)

> [!warning] Secondary source with material errors — do not cite for specs
> This is a third-party blog paraphrasing a Google demo. **The underlying event is real** and is confirmed by Google primaries. **Several of the article's technical claims are wrong**, and at least one contradicts a page this wiki already had right. Corrections are tabulated below against [the Gemma 4 primaries](gemma-4-e2b-model-card.md). Filed as a record of the event and as this wiki's clearest worked example of the failure modes the [primary-source rule](../../CLAUDE.md) describes.

## What is real

Confirmed by **Google's own posts** — [@googlegemma on X](https://x.com/googlegemma/status/2057142732494352689) and the *"Gemma Playground: Robot Duck"* video on the [Google for Developers](https://www.youtube.com/watch?v=pLwB_63yUBY) channel:

> "At Google I/O today? **Stop by the Gemma Playground** and chat with our Gemma 4-powered Open Duck robot! 🤖🦆 Not on site? No problem! You can 3D print your own at home."

So: at **Google I/O 2026**, two [Open Duck Mini](../entities/open-duck-mini.md) v2 robots ran **Gemma 4 E2B on-device** — one on a **Raspberry Pi 5**, one on an **[NVIDIA Jetson Orin Nano](../entities/jetson-orin-nano.md)** — handling speech, vision and spoken response with no cloud connection. Demo led by **Xavier Plantaz**, Partner Solutions Engineer at Google. One duck, asked to introduce itself, answered *"I am Autumn, a small duck robot's brain"* — "Autumn" being ODM (Open Duck Mini) rendered phonetically.

The claimed pipeline — **Parakeet** (NVIDIA ASR) → **Gemma 4 E2B on LiteRT** → **Kokoro** (TTS) — is plausible and appears only in this article; **no Google primary names the ASR or TTS components.** Treat the stack as unverified.

This is a genuinely interesting datapoint for the wiki: [Open Duck Mini](../entities/open-duck-mini.md) is the ancestor of [Microduck](../entities/microduck.md), and Google chose it as the vehicle for its edge-AI story four months before Pollen shipped the commercial version.

## Corrections

Every row checked against [google/gemma-4-E2B-it and the LiteRT-LM card](gemma-4-e2b-model-card.md).

| Article says | Primary says | Severity |
|---|---|---|
| *"Antoine **Piron**"* (3×, in body text) | **Antoine Pirrone** — GitHub `apirrone`, name field "Antoine Pirrone", R&D engineer at Pollen Robotics, member of team Rhoban. The article's *own* August update paragraph spells it "Pirrone." | **Wrong, and internally inconsistent** |
| *"E2B — 2B parameters"* / *"Parameters: ~2 billion"* | **2.3B effective, 5.1B with embeddings** (safetensors: 5,123,178,051). The card is explicit: *"the 'E' in E2B and E4B stands for **effective** parameters."* | **Wrong** — misses the whole PLE mechanism |
| *"Context window: 256K tokens"* | **128K** for E2B/E4B; 256K belongs to 12B / 26B A4B / 31B. And under LiteRT-LM on-device it is **32K**. | **Wrong twice** — scope loss |
| *"Runtime memory: ~607 MB on XNNPACK (Apple CPUs)"* | **1546 MB** measured on a Raspberry Pi 5. And **XNNPACK is Google's CPU backend for ARM/x86**, not "Apple CPUs." | **Wrong on both halves** |
| Family: *"E2B, E4B, 26B MoE, 31B dense"* | **Five sizes** — the **12B Unified** is omitted, and it is the third-most-downloaded variant. | Incomplete |
| *"26B MoE"* | 26B **A4B** = 25.2B total / **3.8B active** — the "A" is load-bearing. | Imprecise |
| *"Modalities: text + image + audio (E2B and E4B)"* | Text, image, **video**, audio; audio on **E2B, E4B and 12B**. | Incomplete |
| *"Released April 2, 2026"* | HF repo created **2026-03-02**. | Doubtful |
| *"brought two ducks **to the stage**"* | Google's own post: *"stop by the **Gemma Playground**"* — a demo booth, not a keynote stage slot. | Overstated |
| Microduck update: *"15 actuators, **LiDAR**"* | Pollen's own press kit: *"compact LiDAR, an **8×8 time-of-flight matrix**"* — 64 depth zones. See [the launch page](pollen-robotics-microduck.md). | Propagates a vendor marketing term |
| *"Model size: ~2.58 GB"* | **2583 MB.** | ✅ Correct |
| *"~$400 in components"*, Pi 5 recommended, Apache-2.0, BDX-droid inspiration | Matches the [repo](../entities/open-duck-mini.md). | ✅ Correct |

## The claim that matters most, and it is unsupported

> "The response latency was described as **'very snappy'** by Plantaz, running entirely on local hardware."

Google's published benchmarks for the **two exact boards in this demo**:

| Device | Backend | Prefill (tok/s) | Decode (tok/s) | TTFT (s) |
|---|---|---|---|---|
| Raspberry Pi 5 | CPU | 133 | **7.6** | 7.8 |
| Jetson Orin Nano | CPU | 109 | 12.2 | 9.4 |
| Jetson Orin Nano | **GPU** | 1,142 | **24.2** | **0.9** |

Being fair to the article: the 7.8 s time-to-first-token is measured at **1024 prefill tokens**, and a short spoken question is perhaps 30–60 tokens, so real TTFT on the Pi would be well under a second. TTFT is not the problem.

**Decode rate is.** It is independent of prompt length, and the duck's own quoted answer — *"A large language model is a complex AI designed to understand and generate human-like text. I am here to assist you with tasks and interactions"* — is roughly **45 tokens**. On the Pi 5's 7.6 tok/s that is about **six seconds** to generate, before TTS. On the Orin Nano's GPU at 24.2 tok/s it is under two.

So the two ducks were **not** equivalent, and the article's flat "very snappy" describes at most one of them. The article states Duck A is a Pi 5 and Duck B an Orin Nano, then draws no distinction — and there is no Pi 5 GPU row in Google's table, meaning a Pi deployment *is* the slow configuration. **This is the omission that costs the reader something**: someone building from this article would pick the $80 Pi 5 and get a robot that takes six seconds to answer.

## How this went wrong, mapped to the rule

The [CLAUDE.md](../../CLAUDE.md) primary-source rule names two failure modes. Both are present:

- **Scope loss** — *"paraphrase preserves the noun phrase and drops what it was bound to."* "256K tokens" is a real Gemma 4 number attached to the *wrong variants*, exactly as "CUDA 13.0" was on the JetPack 7.2 correction. Same for "2B parameters," which is real as an *effective* count and false as a parameter count.
- **Omission** — the CPU-vs-GPU gap, the video modality, the 12B variant, and the decode-rate consequence. The decision-relevant content is precisely the un-headline-able part.

A third, specific to AI-assisted secondaries: **internal inconsistency**. The article spells the creator's name two different ways in one document, which is a signature of text assembled from multiple sources without a consistency pass.

> [!note] Not corroboration
> This article, `cryptobriefing.com`, `circuitdigest.com` and `franksworld.com` all cover the same demo. Per the rule, **that is one source, not four** — they paraphrase the same Google posts. Only the Google X post, the Google for Developers video, and the HF model cards are origins.

## Entities mentioned

- [Open Duck Mini](../entities/open-duck-mini.md) · [Gemma 4](../entities/gemma4.md) · [Jetson Orin Nano](../entities/jetson-orin-nano.md) · [Microduck](../entities/microduck.md) · [Pollen Robotics](../entities/pollen-robotics.md)

## Concepts touched

- [On-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md)

## Open questions

- **Did the demo use vision at all?** The article says the camera feeds Gemma's multimodal input, but the only quoted exchanges are pure text Q&A. Google's post says "chat with." Unconfirmed.
- **ASR and TTS components unverified** — Parakeet and Kokoro appear in no primary.
- **Which duck was demonstrated?** The quoted responses are not attributed to Duck A or Duck B, which is exactly the distinction the benchmark table says matters.
- **The ducks did not walk.** The article lists walking as a *next step* — so the Google demo was a conversational head, not a locomotion demo, on a robot whose entire point upstream is legged RL.

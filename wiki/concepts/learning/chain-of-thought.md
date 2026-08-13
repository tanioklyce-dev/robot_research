---
title: Chain of thought
type: concept
created: 2026-05-15
updated: 2026-08-03
sources: 9
tags: [llm, reasoning, prompting, chain-of-thought, reasoning-models, embodied-cot, depth-tokens]
---

**Chain of thought (CoT)** is a prompting and generation technique in which a language model emits intermediate reasoning steps in natural language before producing its final answer. The intermediate tokens serve as a scratchpad that conditions the answer, exploiting the fact that more autoregressive compute per problem yields better answers.

## Definition
Given a question `q`, a vanilla LM samples `answer ~ p(a | q)`. A CoT model samples `rationale, answer ~ p(r, a | q)` and returns `a`. The rationale is produced in the same token stream as the answer, so the model conditions the answer on its own reasoning. CoT is not an architectural change; it is a behavior elicited by prompting (few-shot, zero-shot) or trained-in via supervised fine-tuning and RL on reasoning traces.

## Origin and lineage
- **Wei et al., 2022** — "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (Google Brain, NeurIPS 2022). Few-shot prompts that include worked-out reasoning examples sharply improved performance on arithmetic (GSM8K), commonsense, and symbolic reasoning. **Emergent with scale**: the lift was small below ~60B params and large above ~100B at the time.
- **Kojima et al., 2022** — "Large Language Models are Zero-Shot Reasoners". Showed that simply appending *"Let's think step by step"* to the prompt elicits CoT without exemplars. Established CoT as a zero-shot capability of sufficiently large models.
- **Wang et al., 2022 — Self-Consistency** — sample many CoT trajectories at temperature > 0 and majority-vote the final answer. Substantial gains over greedy CoT because reasoning errors are not perfectly correlated across samples.
- **Yao et al., 2023 — Tree of Thoughts (ToT)** — generalizes the linear chain to a search tree over reasoning states, with explicit lookahead and backtracking.
- **Reasoning models (2024–2025)** — OpenAI o1 / o3, DeepSeek-R1, Claude extended thinking, Gemini 2.5 thinking. RL-trained to produce long internal CoTs ("thinking" tokens, often hidden from the user) before the visible answer. The shift is from "CoT as a prompt trick" to "CoT as the model's native control flow," with inference-time compute budgeted explicitly (number of thinking tokens) as a knob alongside model size.

## Why it works (and where it breaks)
- More tokens between question and answer = more transformer forward passes = more effective compute per problem. CoT externalizes intermediate state into tokens, sidestepping the depth limits of a single forward pass.
- CoT is **faithful to the answer's correctness but not necessarily to the model's true reasoning** — published rationales can be post-hoc rationalizations rather than the actual computation. This matters for interpretability and AI-safety arguments that lean on chain-of-thought monitoring; see [AI safety and alignment](../safety/ai-safety-alignment.md).
- Below the emergent-capability threshold, CoT can *hurt* small models, which produce plausible-sounding but wrong reasoning.

## Robotics relevance
CoT appears in robotics primarily through the [LLM-agent architecture](../agents/llm-agent-architecture.md) pattern, where the LLM planner emits a sequence of tool calls. Recent VLA work pushes CoT *inside* the policy:

- **Embodied chain of thought** in [VLA models](vla-models.md) — the model generates a short natural-language plan ("the cup is on the left edge of the table; I should approach from above and close the gripper") before emitting action tokens. The reasoning trace conditions the action head and is often supervised during training.
- **Hierarchical S1/S2 VLAs** (e.g. [Helix](../../sources/helix-blog.md)) split slow CoT-style reasoning (System 2, 7–9 Hz) from fast continuous control (System 1, ~200 Hz). The S2 stream is functionally an embodied CoT producing a latent plan that conditions S1.
- **Reasoning VLMs as planners** — Google's Gemini Robotics-**ER** ("embodied reasoning") variant is explicitly trained for CoT-style planning over a tool-call vocabulary on the [Spot](../../entities/spot.md) demo ([Boston Dynamics Spot + Gemini Robotics](../../sources/bostondynamics-spot-gemini-robotics.md)).
- **NVIDIA GR00T N1** uses an explicit System 2 (VLM reasoning) + System 1 (diffusion action head) decomposition that maps onto the same CoT-before-action pattern (see [NVIDIA GR00T](../../entities/nvidia-groot.md)).
- **Non-textual (spatial) embodied CoT** — [MolmoAct](../../entities/molmoact.md) / [MolmoAct2](../../entities/molmoact2.md) reason in *depth tokens* rather than language: before acting, the model predicts a compact discrete depth map (a 10×10 VQ grid) that grounds the policy in 3D structure. MolmoAct2's argument is that tacit physical knowledge (distance, free space, occlusion) is rarely articulated in text, so a **visual/spatial** reasoning trace beats a textual one for manipulation. [Adaptive depth reasoning](adaptive-depth-reasoning.md) then makes this CoT cheap by only recomputing changed scene regions — a direct answer to embodied CoT's core problem: **the reasoning trace's token cost dominates control latency**.

## Related
- [LLM-agent architecture](../agents/llm-agent-architecture.md) — CoT is the typical reasoning style of the LLM planner emitting tool calls.
- [VLA models](vla-models.md) — embodied CoT bakes reasoning into the action policy.
- [Adaptive depth reasoning](adaptive-depth-reasoning.md) — depth tokens as a latency-aware non-textual embodied CoT.
- [AI safety and alignment](../safety/ai-safety-alignment.md) — chain-of-thought monitoring as a (debated) interpretability tool.

## Key references
- Wei et al., 2022 — *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. arXiv:2201.11903.
- Kojima et al., 2022 — *Large Language Models are Zero-Shot Reasoners*. arXiv:2205.11916.
- Wang et al., 2022 — *Self-Consistency Improves Chain of Thought Reasoning in Language Models*. arXiv:2203.11171.
- Yao et al., 2023 — *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*. arXiv:2305.10601.
- **[Welch Labs Illustrated Guide to AI, Vol I, Ch 8](../../sources/welchlabs-illustrated-guide-to-ai.md)** (Welch, 2026) — pedagogy-grade reference. The attention chapter motivates DeepSeek's Multi-Head Latent Attention partly by *the volume of CoT tokens reasoning models like R1 must generate*; useful angle on why CoT-heavy reasoning models drove a new wave of attention-architecture innovation.

> [!note] Text-CoT primaries still not ingested
> The textual-CoT foundations (Wei et al., Kojima et al.) are seeded from general knowledge, not ingested sources. The **embodied-CoT** thread now has a primary — the [MolmoAct2 paper](../../sources/molmoact2-paper.md) (depth-token reasoning). Expand the textual side with citations when a Wei-style or reasoning-model paper lands in `raw/`.

## Mentioned in
- [MolmoAct2 paper (Fang, Duan et al. 2026)](../../sources/molmoact2-paper.md) — depth-token reasoning as a non-textual embodied CoT; the "tacit physical knowledge isn't in text" argument.
- [MolmoAct paper](../../sources/molmoact-paper.md) — embodied CoT with **decodable** intermediate steps: depth tokens → visual trace → actions, each independently renderable; the trace doubles as a steering interface.

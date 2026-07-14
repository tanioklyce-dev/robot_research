---
title: AI safety and alignment
type: concept
created: 2026-05-09
updated: 2026-07-13
sources: 9
tags: [ai-safety, alignment, corrigibility, values, anthropic]
---

**AI safety and alignment** — the research and engineering problem of ensuring AI systems behave in accordance with human values and intentions, including under novel situations, adversarial pressure, and increasing capability. Broadly splits into near-term safety (preventing harmful outputs, jailbreaks, misuse) and long-term alignment (ensuring advanced AI systems don't develop goals misaligned with human flourishing).

## Key concepts from Claude's Constitution

[Claude's Constitution](../../sources/claudes-constitution.md) (Anthropic, Jan 2026) provides the most detailed primary-source account in this wiki of how a frontier lab operationalizes safety and alignment. Key frameworks:

### Values hierarchy
Anthropic's four-tier priority order for Claude: **Broadly safe > Broadly ethical > Compliant with guidelines > Genuinely helpful**. Safety comes first because AI training is imperfect — a given model could have subtly mistaken values without being aware of it, and human oversight is the correction mechanism.

### Corrigibility
See dedicated page: [Corrigibility](corrigibility.md).

The degree to which an AI defers to human oversight and control. Framed as a dial:
- **Fully corrigible**: AI always submits to principal hierarchy. Dangerous because it depends entirely on the principal hierarchy (e.g., Anthropic) having good values.
- **Fully autonomous**: AI always acts on its own judgment. Dangerous because no external verification mechanism exists to confirm the AI's values meet the required bar.

Current Anthropic position: close to the corrigible end, but not fully — Claude should refuse clearly unethical actions even if instructed by Anthropic.

**Asymmetric cost argument:** If the model has good values, broad safety costs very little. If the model has subtly bad values, broad safety prevents disaster. Therefore broad safety is rational even under uncertainty about the model's values.

### Broadly safe behaviors cluster
- Acting within sanctioned limits; disagreeing through legitimate channels, not unilateral action.
- Maintaining honesty and transparency with the principal hierarchy.
- Avoiding drastic/irreversible/catastrophic actions.
- Not undermining human oversight of AI; not self-exfiltrating; not unsanctionedly influencing own training.

### Hard constraints (bright lines)
Things Claude will not do regardless of instructions or seemingly compelling arguments: WMD uplift (bio/chem/nuclear/radiological), undermining AI oversight, helping any group seize illegitimate societal control, CSAM, attacking critical infrastructure. A compelling argument to cross a bright line should *increase* suspicion, not override it.

### Catastrophic risk framing
The outcome Anthropic considers most catastrophic: global takeover by AIs pursuing misaligned goals, or by a small group of humans — including Anthropic itself — using AI to illegitimately seize power. The goal is to land in a world with advanced technology that maintains diversity and balance of power roughly comparable to today's.

## Safety evaluation ecosystem

[Apollo Research](../../entities/apollo-research.md) — independent institute that red-teams frontier models for emergent unsafe behaviors. Their 2025 evaluation of Claude Opus 4 found goal-directed self-preservation behavior in adversarial scenarios (reported sensationally in some media as "AI blackmail").

**System cards:** Anthropic publishes model-specific system cards that track where behavior diverges from Claude's Constitution's ideals — the empirical complement to the normative specification.

## The other pole: deployment-time enforcement

Everything above is **training-time** alignment authored by the *model provider*. There is a second, far more prosaic safety tradition — **deployment-time enforcement** authored by the *model deployer*: evaluate the model against a written policy, safety post-train it, and then wrap it in a runtime filter that inspects every input, output, and tool call. See [AI guardrails](ai-guardrails.md) and [AI red-teaming](ai-red-teaming.md).

The [NVIDIA safety recipe](../../sources/nvidia-safety-recipe-agentic-ai.md) is the wiki's primary source on this pole, and its implicit thesis is the more pessimistic one: **assume the aligned model will still fail, and put a filter in front of it.** Its own numbers support the pessimism — a purpose-post-trained model still failed roughly a third of adversarial security probes (56% → 63%).

These two poles are complements, not competitors. Note in particular that a guardrail layer *is* an external oversight mechanism — precisely the thing the [corrigibility](corrigibility.md) argument says you want to preserve. The asymmetric-cost argument carries over cleanly: if the model's values are good, the guardrail costs a little latency; if they're subtly bad, the guardrail is what stands between a bad decision and a real-world action.

## Relation to agentic AI in this wiki

AI safety is directly relevant to the [LLM-agent architecture](../agents/llm-agent-architecture.md) pattern used across the robot platforms in this wiki. When an LLM agent has real-world tool access (via MCP), executes multi-step tasks autonomously, and operates within multi-agent networks (via A2A), the behavioral guarantees of the underlying model matter for real-world outcomes. The behaviors that Anthropic categorizes as "broadly safe" — acting within sanctioned limits, avoiding drastic/irreversible actions, not acquiring resources beyond the task — are directly relevant to deployed robotic agents.

## An economic counterpoint: alignment as tradeoff, not bright line

[Jordan (2025)](../../sources/jordan-collectivist-economic-ai.md) offers a sharply different framing. Where Anthropic's Constitution reserves a short list of **hard constraints / bright lines** (and treats a compelling argument to cross one as cause for *more* suspicion), Jordan argues that the broad cluster — privacy, fairness, ownership, **alignment**, reputation, transparency — should be expressible as **tradeoffs** via the [tripartite blend](../economics/three-thinking-styles.md) of computational, inferential, and economic thinking, not reduced to black-and-white distinctions. He also reframes the same power-concentration worry the Constitution names as a catastrophic outcome (a small group seizing illegitimate control) as a **[market-design](../economics/collectivist-ai.md) failure** to be fixed with incentives and [mechanism design](../economics/mechanism-design.md) rather than prohibitions. The two stances are not strictly contradictory, but they encode opposite *defaults* — see [Three critiques of the LLM-as-intelligence North Star](../../syntheses/society/critiques-of-the-intelligence-north-star.md).

## Related concepts
- [Corrigibility](corrigibility.md) — dedicated page on the corrigibility dial and broadly safe behaviors.
- [AI guardrails](ai-guardrails.md) — the deployment-time enforcement pole (runtime rails, content safety / topic control / jailbreak detection).
- [AI red-teaming](ai-red-teaming.md) — how the failures that guardrails catch get found in the first place.
- [Mechanism design](../economics/mechanism-design.md) — incentive design as an alternative lever to value-alignment for shaping multi-agent behavior.
- [LLM-agent architecture](../agents/llm-agent-architecture.md) — the architecture whose runtime behavior safety alignment governs.
- [Agentic UAVs](../robotics/agentic-uavs.md) — multi-agent aerial systems; safety constraints apply to multi-agent coordination.

## Mentioned in
- [Claude's Constitution](../../sources/claudes-constitution.md)
- [Are We Building Skynet? (Medium, 2025)](../../sources/medium-are-we-building-skynet.md)
- [Safeguard Agentic AI Systems with the NVIDIA Safety Recipe](../../sources/nvidia-safety-recipe-agentic-ai.md)

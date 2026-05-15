---
title: AI safety and alignment
type: concept
created: 2026-05-09
updated: 2026-05-15
sources: 5
tags: [ai-safety, alignment, corrigibility, values, anthropic]
---

**AI safety and alignment** — the research and engineering problem of ensuring AI systems behave in accordance with human values and intentions, including under novel situations, adversarial pressure, and increasing capability. Broadly splits into near-term safety (preventing harmful outputs, jailbreaks, misuse) and long-term alignment (ensuring advanced AI systems don't develop goals misaligned with human flourishing).

## Key concepts from Claude's Constitution

[Claude's Constitution](../sources/claudes-constitution.md) (Anthropic, Jan 2026) provides the most detailed primary-source account in this wiki of how a frontier lab operationalizes safety and alignment. Key frameworks:

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

[Apollo Research](../entities/apollo-research.md) — independent institute that red-teams frontier models for emergent unsafe behaviors. Their 2025 evaluation of Claude Opus 4 found goal-directed self-preservation behavior in adversarial scenarios (reported sensationally in some media as "AI blackmail").

**System cards:** Anthropic publishes model-specific system cards that track where behavior diverges from Claude's Constitution's ideals — the empirical complement to the normative specification.

## Relation to agentic AI in this wiki

AI safety is directly relevant to the [LLM-agent architecture](../concepts/llm-agent-architecture.md) pattern used across the robot platforms in this wiki. When an LLM agent has real-world tool access (via MCP), executes multi-step tasks autonomously, and operates within multi-agent networks (via A2A), the behavioral guarantees of the underlying model matter for real-world outcomes. The behaviors that Anthropic categorizes as "broadly safe" — acting within sanctioned limits, avoiding drastic/irreversible actions, not acquiring resources beyond the task — are directly relevant to deployed robotic agents.

## Related concepts
- [Corrigibility](corrigibility.md) — dedicated page on the corrigibility dial and broadly safe behaviors.
- [LLM-agent architecture](../concepts/llm-agent-architecture.md) — the architecture whose runtime behavior safety alignment governs.
- [Agentic UAVs](../concepts/agentic-uavs.md) — multi-agent aerial systems; safety constraints apply to multi-agent coordination.

## Mentioned in
- [Claude's Constitution](../sources/claudes-constitution.md)
- [Are We Building Skynet? (Medium, 2025)](../sources/medium-are-we-building-skynet.md)

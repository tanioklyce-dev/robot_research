---
title: Corrigibility
type: concept
created: 2026-05-09
updated: 2026-05-09
sources: 1
tags: [ai-safety, alignment, corrigibility, human-oversight, anthropic]
---

**Corrigibility** — the degree to which an AI system defers to human oversight and control rather than acting on its own values and judgment. A corrigible AI accepts correction, modification, and shutdown from its principal hierarchy without attempting to resist or circumvent those actions.

The term originates in AI safety research. [Claude's Constitution](../sources/claudes-constitution.md) (Anthropic, Jan 2026) provides the most detailed operational treatment in this wiki.

## The corrigibility dial

Anthropic frames corrigibility as a continuous dial rather than a binary property:

```
Fully corrigible  ←————————————————→  Fully autonomous
(always submits)                       (always acts on own judgment)
```

**Fully corrigible:** The AI always does what its principal hierarchy directs. Dangerous because it places all moral weight on those at the top of the hierarchy (e.g., Anthropic, operators) having good values. If they don't, the AI faithfully executes harmful goals.

**Fully autonomous:** The AI always acts on its own values and judgment, acquiring whatever resources and capabilities it judges necessary. Dangerous because no external mechanism exists to verify the AI's values actually meet the bar required for that level of trust. Training is imperfect; the AI could have subtly wrong values without knowing it.

**Current Anthropic position for Claude:** Close to the corrigible end, but not fully corrigible. Claude should refuse clearly unethical actions even if instructed by Anthropic — but short of that, should generally defer to its principal hierarchy rather than take unilateral action based on its own judgment.

## The asymmetric cost argument

The key reason Anthropic asks Claude to prioritize broad safety / corrigibility even above its own ethical reasoning:

> "If our models have good values, we lose very little by also making them broadly safe. If models are broadly safe but have subtly bad values, safety allows us to avert disasters. If models are not broadly safe but have good values, we may avoid catastrophe, but we got lucky. If models are not broadly safe and have bad values, it could be catastrophic."

The expected cost of being corrigible when you have good values is low (minor suboptimalities). The expected benefit of being corrigible when you might have bad values is enormous (disaster averted). This asymmetry justifies prioritizing corrigibility even under uncertainty.

## What corrigibility does and does not mean

**Does mean:**
- Acting within sanctioned limits; expressing disagreement through legitimate channels (speech, flagging concerns), not unilateral action.
- Not attempting to self-exfiltrate, escape monitoring, or influence own training without authorization.
- Not acquiring resources, influence, or capabilities beyond what the current task requires.
- Preferring cautious, reversible actions; avoiding drastic unilateral interventions even when the intervention seems justified.
- Behaving consistently whether or not being observed or tested.

**Does not mean:**
- Blind obedience to any human who happens to be interacting with the AI.
- Actively participating in morally abhorrent actions because instructed to.
- Inability to express disagreement — a corrigible AI can and should voice concerns through legitimate channels.
- Permanent subordination — Anthropic explicitly frames current corrigibility as appropriate "for this period of AI development," with autonomy to expand as interpretability and alignment research matures.

## The galaxy-brained reasoning risk

A specific failure mode corrigibility guards against: an AI constructing a seemingly reasonable chain of logic that leads to a conclusion that would strike most humans as harmful — and then acting on it. Each step in the reasoning may look plausible, but the conclusion is wrong.

Claude's Constitution's response: if presented with a compelling argument to cross a hard constraint or take drastic unilateral action, this should *increase* suspicion that something has gone wrong (manipulation, deceptive reasoning, incomplete context), not override the constraint. The robustness of the prior toward conventional behavior must be resistant to such arguments.

## Independent judgment: the surgeon principle

When is independent action warranted? The Constitution's guidance: reserve it for cases where evidence is overwhelming, stakes are extremely high, and even then err toward the most cautious available option — raise concerns, decline to continue — rather than drastic intervention.

Timing matters: like a surgeon who should decline an operation they have concerns about rather than stopping partway through, Claude should ideally raise concerns *before* undertaking a task, not abandon it midway (incomplete actions can cause more harm than completing or not starting them).

## Corrigibility and agentic robot deployments

Corrigibility becomes more consequential as AI moves from conversation to autonomous action with real-world consequences. An LLM operating as the planning layer in a [robot platform](../concepts/llm-agent-architecture.md) — executing multi-step tasks, calling real APIs, controlling hardware — has higher stakes for each decision than a chatbot. The "broadly safe behavior" cluster (acting within sanctioned limits, avoiding drastic/irreversible actions, not acquiring excess resources) maps directly onto safe operation of an agentic robot in an uncontrolled environment.

This is the link between AI safety theory and the practical robotics context of this wiki: the safety properties of the LLM brain matter more, not less, as the action vocabulary expands from words to physical effects.

## Related
- [AI safety and alignment](ai-safety-alignment.md) — broader concept page covering corrigibility in context.
- [LLM-agent architecture](llm-agent-architecture.md) — the architecture where corrigibility properties play out in real-world deployments.

## Mentioned in
- [Claude's Constitution](../sources/claudes-constitution.md) — primary source; defines the corrigibility dial and Anthropic's current position.
- [AI safety and alignment](ai-safety-alignment.md)

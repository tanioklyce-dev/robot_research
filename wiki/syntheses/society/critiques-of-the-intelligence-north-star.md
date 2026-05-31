---
title: Three critiques of the LLM-as-intelligence North Star
type: synthesis
created: 2026-05-29
updated: 2026-05-29
tags: [ai-society, economics-of-ml, world-models, alignment, michael-jordan, lecun, anthropic, synthesis]
---

Three sources in this wiki, written by very different camps, all argue that the dominant framing of frontier AI — **"scale up LLMs toward general intelligence"** — is aiming at the wrong target. They diverge sharply on *what the right target is*. Reading them together is more useful than any one alone, because the disagreement is really about **which discipline should supply AI's missing foundations**.

| | [LeCun — AMI / world models](../../sources/lecun2022-path-towards-ami.md) | [Jordan — collectivist-economic AI](../../sources/jordan-collectivist-economic-ai.md) | [Anthropic — Claude's Constitution](../../sources/claudes-constitution.md) |
|---|---|---|---|
| **What's wrong with the LLM North Star** | LLMs predict tokens; they lack a **world model** and so can't reason, plan, or learn like animals. | "Intelligence" is the wrong frame — AI is **social/collectivist**, not individual cognition; an LLM is *a culture*, not a person. | An LLM at scale is a powerful **agent whose values may be subtly wrong**; capability without aligned values is the danger. |
| **Right unit of analysis** | The single autonomous agent + its predictive **world model** (JEPA / H-JEPA). | The **market** — many strategic human + non-human participants linked by data. | The model's **values and its relationship to human oversight**. |
| **Missing foundation** | Self-supervised learning of latent-space world models. | The **tripartite blend** of [computational + inferential + economic thinking](../../concepts/economics/three-thinking-styles.md). | A **values hierarchy + corrigibility**; bright-line hard constraints. |
| **Borrowed-from discipline** | Neuroscience / developmental psychology. | Statistics + microeconomics. | Moral philosophy + safety engineering. |
| **Status in wiki** | Architectural spine of the [JEPA program](../../concepts/world-models/jepa.md) (17 sources). | New economics-of-ML wing (1 source). | Anchor of [AI safety & alignment](../../concepts/safety/ai-safety-alignment.md) (5 sources). |

## Where they actually conflict

**On power and control.** Jordan and the Constitution both worry about **illegitimate concentration of power**, but reach for opposite levers. The Constitution treats catastrophic power-grabs as something to forbid via **bright lines** — a small group (including Anthropic itself) using AI to seize control is named as the worst outcome, and the model is built to refuse steps toward it ([Claude's Constitution](../../sources/claudes-constitution.md)). Jordan treats the same disempowerment (producers stripped of value, users stripped of privacy) as a **market-design failure** to be fixed with incentives, contracts, and equilibria — *not* with prohibitions ([Jordan 2025](../../sources/jordan-collectivist-economic-ai.md)).

> [!note] Alignment: bright line vs. tradeoff
> This is the sharpest tension in the wiki's AI-society material. The Constitution's [hard constraints](../../concepts/safety/ai-safety-alignment.md) are *deliberately* black-and-white — "a compelling argument to cross a bright line should *increase* suspicion." Jordan argues the opposite stance for the broad cluster of issues (privacy, fairness, ownership, **alignment**, reputation, transparency): the tripartite blend exists precisely to express them as **tradeoffs rather than black-and-white distinctions**. The two are not strictly contradictory — Anthropic also reasons about most behavior as tradeoffs and reserves bright lines for a short catastrophic list — but they encode opposite *defaults*, and that difference is load-bearing for anyone designing governance.

**On individual vs. collective.** LeCun's program is methodologically *individualist* — build one agent with a good world model. Jordan's whole thesis is that this misses the point: intelligence and value are **social**, and the interesting design problems live *between* agents (information asymmetry, incentives), not inside one. The Constitution sits in between — a single model, but defined entirely by its *relationship* to a principal hierarchy.

## Where they reinforce each other
- All three are **position papers / vision documents**, not empirical results — each is a senior figure's argument about direction, and each is explicit that the field lacks solid foundations (LeCun: no learned world models yet; Jordan: "no Maxwell's equations… we are winging it"; Anthropic: training is imperfect, values may be subtly wrong).
- All three reject **"just more data and compute"** as sufficient.
- LeCun's "agent + world model" and Jordan's "market of agents" are at *different altitudes* and compose cleanly: a world-model-equipped agent is exactly the kind of strategic participant Jordan's markets are made of. The wiki's own [LLM-agent architecture](../../concepts/agents/llm-agent-architecture.md) page is the *engineering* view; Jordan supplies the missing *economic* view of the same multi-agent systems.

## Takeaway
If you want to know **how to build a more capable agent**, read LeCun. If you want to know **how a system of agents and humans will behave and how to make it fair**, read Jordan. If you want to know **how to keep a capable agent from doing catastrophic harm**, read the Constitution. The three are complementary lenses, and the wiki is stronger for holding all three than for collapsing AI's open problems into a single "scale the LLM" axis.

## Sources
- [A Path Towards Autonomous Machine Intelligence (LeCun, 2022)](../../sources/lecun2022-path-towards-ami.md)
- [A Collectivist, Economic Perspective on AI (Jordan, 2025)](../../sources/jordan-collectivist-economic-ai.md)
- [Claude's Constitution (Anthropic, 2026)](../../sources/claudes-constitution.md)
- Adjacent register: [Are We Building Skynet? (2025)](../../sources/medium-are-we-building-skynet.md) — the hype/hysteria discourse Jordan opens by criticizing.
- Adjacent axis: [Computational Life (Agüera y Arcas et al., 2024)](../../sources/computational-life-self-replicating-programs-paper.md) — a *fourth* alternative to LLM-scaling, on a different axis than governance. [Agüera y Arcas](../../entities/blaise-aguera-y-arcas.md)'s "[Paradigms of Intelligence](../../concepts/alife/artificial-life-and-self-replication.md)" view treats intelligence/life as **emergent from simple interacting computation** (self-replicators arise with no fitness function). Where LeCun/Jordan/Constitution argue about *building* and *governing* agents, this asks what intelligence-like complexity *is* and how it spontaneously appears.

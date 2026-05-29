---
title: Mechanism design & statistical contract theory
type: concept
created: 2026-05-29
updated: 2026-05-29
sources: 1
tags: [economics-of-ml, mechanism-design, game-theory, contract-theory, e-values, stackelberg, incentives, michael-jordan]
---

**Mechanism design** — the branch of economics that, given a *desired outcome*, asks **what game would deliver that outcome as an equilibrium**. It is the **inverse of game theory**: game theory predicts the equilibrium that results when strategic agents interact; mechanism design works backward from the equilibrium to the rules (Hurwicz & Reiter 2006; Myerson 1991; Nisan et al. 2007, *Algorithmic Game Theory*). In [Jordan 2025](../../sources/jordan-collectivist-economic-ai.md) it is the **economic leg** of the [tripartite blend](three-thinking-styles.md).

## Key economic objects
- **Information asymmetry** — agents know different things and have strategic reasons to withhold knowledge in a transaction. Critically, this uncertainty **does not go away as sample size grows** (unlike statistical/sampling uncertainty) — it requires an *economic mechanism*, not more data.
- **Equilibria, not optima** — solutions to multi-agent design are equilibrium concepts. **Nash equilibrium** for simultaneous play; **Stackelberg equilibrium** for sequential play (a *Leader* moves first anticipating a *Follower*). Sequential/Stackelberg play is the relevant case for large-scale collectivist systems because agents act **asynchronously**.
- **Contract** (Laffont & Martimort 2002) — a mechanism for sequential play: instead of a single action (e.g., one price), the Leader offers a **menu** of (service, price) options; the Follower self-selects using private knowledge. A well-designed menu beats a fixed price on **both revenue and social welfare** (high-willingness-to-pay Followers opt into richer options).
- **Incentive compatibility** — the contract is designed so that gaming it is unprofitable (e.g., a low-quality item yields nonpositive expected profit to its supplier).

## Statistical contract theory — the headline ML link
Classical contract theory has no role for **inference from data**; **statistical contract theory** adds one (Bates, Jordan, Sklar & Soloff 2024, *Principal-agent hypothesis testing*).

Setup: a **buyer** (Leader, e.g. a marketplace) runs **hypothesis testing** — buy / no-buy decisions on a sequence of products of unknown quality, supplied by self-interested **suppliers** (Followers). The buyer collects costly data (e.g. a focus group) and will make false positives / false negatives. Suppliers may privately know which products are low-quality and *hope* low-quality items slip through as false positives (profit for them). The buyer designs an **incentive-compatible contract** — a menu trading off data-collection burden and licensing terms / risk — so the overall product mix has controlled statistical error and the system can't be gamed.

> [!note] The e-value result
> Bates et al. (2024) prove these statistical contracts are incentive-compatible **if and only if the menu options can be expressed as e-values** (Ramdas & Wang 2025). An **e-value** is a function of data that is ≤ 1 in expectation under the null hypothesis (an alternative to the p-value's tail probability), with a **betting interpretation**: the multiplicative factor by which wealth grows in expectation under the null. For sequential data the right object is a **nonnegative supermartingale** (an e-value at any stopping time — accumulated evidence over time). The result identifies an *inferential* concept (e-values for hypothesis testing) with an *economic* one (information-asymmetry-robust contracts) — a concrete instance of the inference⊕economics blend.

## Related concepts
- [Three thinking styles](three-thinking-styles.md) — mechanism design is the economic leg.
- [Collectivist AI / AI-as-market](collectivist-ai.md) — markets are built out of these mechanisms (three-layer data markets are generalized Stackelberg games).
- [Prediction-powered inference](prediction-powered-inference.md) — PPI as an *implicit* incentive mechanism (a data provider aware the receiver holds ground truth is disincentivized from bias).
- [AI safety and alignment](../safety/ai-safety-alignment.md) — incentive design as an alternative lever to value-alignment for shaping multi-agent behavior.

## Mentioned in
- [A Collectivist, Economic Perspective on AI (Jordan, 2025)](../../sources/jordan-collectivist-economic-ai.md)

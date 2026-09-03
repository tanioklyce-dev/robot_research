---
title: Massive (formerly Polygon.io)
type: entity
subtype: company
created: 2026-09-03
updated: 2026-09-03
sources: 1
tags: [massive, polygon-io, market-data, api, mcp, x402, opra, sip, cme, agents, marketone, dataset-provenance]
---

**Massive** (massive.com) — a developer-first financial market-data platform, **rebranded from Polygon.io** (announced 2025-10-30, in effect through early 2026). The data partner behind [MarketOne](marketone.md) and the source of the ticks under [Market-JEPA](market-jepa.md). **Steve Bravo** presented it at [Day 3 of the World Modeling Workshop](../sources/chicago-booth-world-modeling-workshop-2026-day3.md); he came to Massive from **OPRA**, the options SIP.

## What it carries

Direct SIP connections rather than resold feeds: **UTP and CTA** for equity level-one, **OPRA** for options (*"probably the largest financial dataset in the world"*), plus dark-pool and OTC prints, indices (S&P, Dow Jones, FTSE), currencies, and a **CME futures** partnership that is their newest offering. Also a research team building derived data — e.g. **event tags extracted from SEC 8-K filings**, explicitly to keep models from drowning in unlabelled filings.

## Why it is in a robotics wiki: the agent-facing delivery layer

Delivery is REST, WebSockets, flat files, **MCP**, and **x402** — the last of which is the interesting one. x402 lets an **agent buy market data per request, in USDC, with no account and no API key**. Whatever one thinks of the payment rail, the pattern is the general one: a machine-readable resource priced per call so an autonomous process can acquire it without a human provisioning a subscription first.

> [!note] Their MCP design was driven by a failure this wiki keeps meeting
> Bravo's account of agents on raw market data: they *"pull all the data, get confused, and hallucinate."* A colleague's agent loaded a series into context and reported it could find no signal, until a human overlaid the analytic frame. The response was to make **the MCP server token-efficient so the agent must choose what to pull**, rather than defaulting to everything — reportedly a rewrite down to four composable tools. Same lesson as the [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) pages: the product is retrieval discipline, not access.

## The academic-workflow point

Made by an audience member rather than the vendor, and it is the substantive one. Finance research typically needs **~10,000 observations in narrow windows around information events**, and has historically paid a cluster-computing tax (WRDS, TAQ) to extract them from bulk data. An API that returns the event windows directly removes that tax — *"it was like ten lines of code."* Bravo confirms this is how academics actually use them.

> [!note] Dataset provenance for MarketOne now has a named source
> The [MarketOne](marketone.md) page previously flagged that if the dataset's provenance and licensing ever became load-bearing, the Day 3 Massive talk was the place to look. It is now ingested — and the answer is that the underlying data is Massive's SIP-sourced feed, with Massive hosting the full dataset. Licensing terms for MarketOne itself were **not** stated in the talk; the [Market-JEPA](market-jepa.md) *checkpoint* is MIT.

## Related

- [MarketOne](marketone.md) — the dataset derived from this feed.
- [Market-JEPA](market-jepa.md) — the encoder trained on it.
- [Bradford Levy](bradford-levy.md) — the academic partner, *"since back when they were called Polygon."*
- [World models for financial markets](../syntheses/society/world-models-for-financial-markets.md).

## Mentioned in

- [Third World Modeling Workshop — Day 3](../sources/chicago-booth-world-modeling-workshop-2026-day3.md) — *Institutional-Grade Market Data*, Steve Bravo.
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — named as MarketOne's data partner.

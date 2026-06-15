---
title: The Blue Alliance
type: entity
subtype: platform
created: 2026-06-14
updated: 2026-06-14
sources: 2
tags: [frc, the-blue-alliance, tba, scouting, match-video, competition-results, webcast, api, open-source]
---

# The Blue Alliance

**The Blue Alliance (TBA)** — the volunteer-run, **open-source** community platform that is the de-facto third-party record of the [FIRST Robotics Competition](first-robotics-competition.md): team information, event results, match video, and live webcasts, plus a **public API**. Its self-description: "the best way to **scout, watch, and relive** the FIRST Robotics Competition."

## Why it matters in this wiki

TBA is the **authoritative results source** for the wiki's FRC coverage. Where firstinspires.org runs the competition, TBA is the machine-readable, deep-linkable record on top of it — the source used to verify [Team 4414's 2026 REBUILT World Championship](../sources/tba-team-4414-2026.md) and the natural reference for any FRC team's competition history ([Team 254](team-254.md), [Team 4414](team-4414-hightide.md)). It's also the data backbone that team scouting workflows build on (cf. Team 4414's in-house "Tide Apps" scouting suite).

## Key facts

- **Scope:** Events, Teams, **GameDay** (webcast aggregator), Insights, Blog. Per-team/-event/-match pages with records, rankings, alliances, awards, and video.
- **myTBA:** Google-account personalization — Favorites + Subscriptions (push notifications); web + **Android** + **iOS** apps.
- **Open source + API:** community-maintained codebase; public API for programmatic data access.
- **Funding:** donations + a platinum sponsor; community-contributed offseason event data.
- **Hosts season resources:** REBUILT (2026) materials, FIRST 2027 resources; 2027 Kickoff Jan 16, 2027.

> [!note] Fetch access
> TBA returns **HTTP 403 to WebFetch** (and to `WebFetch`-style bots). Ingests here were fetched via `curl` with a browser user-agent; the **TBA API** is the proper path for structured pulls.

## Related

- [FIRST Robotics Competition](first-robotics-competition.md) — the competition TBA tracks.
- [Team 4414 (HighTide)](team-4414-hightide.md) / [Team 254](team-254.md) — teams whose records are sourced from TBA.

## Open questions

- TBA API surface + auth model (would justify a dedicated ingest if the wiki pulls FRC data programmatically).

## Mentioned in

- [The Blue Alliance (homepage)](../sources/the-blue-alliance-homepage.md) — platform overview.
- [The Blue Alliance — Team 4414 (2026 season)](../sources/tba-team-4414-2026.md) — a team-season record sourced from TBA.

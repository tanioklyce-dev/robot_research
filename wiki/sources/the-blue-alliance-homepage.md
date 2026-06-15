---
title: "The Blue Alliance (homepage)"
type: source
url: https://www.thebluealliance.com/
author: The Blue Alliance (volunteer community)
published: 2026
ingested: 2026-06-14
local_path: null
venue: thebluealliance.com
license: open source (TBA codebase is open-source; data from FIRST)
format: web page (platform landing page)
tags: [frc, the-blue-alliance, tba, scouting, match-video, competition-results, webcast, api, open-source]
---

## Summary

The landing page for **[The Blue Alliance](../entities/the-blue-alliance.md)** (TBA) — "the best way to **scout, watch, and relive** the [FIRST Robotics Competition](../entities/first-robotics-competition.md)." It is the de-facto third-party hub for FRC team information, match videos, event results, and live webcasts, with a public API that makes it the authoritative machine-readable record of FRC competition data (the source the wiki used to verify [Team 4414's 2026 championship](tba-team-4414-2026.md)). Volunteer-run and **open source**, funded by donations and sponsorship.

## Key claims

- **Mission:** scout / watch / relive FRC; "team information and match videos and results from the FIRST Robotics Competition." Points to firstinspires.org for FIRST itself.
- **Core sections:** **Events**, **Teams**, **GameDay** (live-webcast aggregator), **Insights**, **Blog**, **Swag**.
- **myTBA:** personalized accounts (Google sign-in) with **Favorites** (personalized content / quick access) and **Subscriptions** (push notifications); settings sync across web + **Android** and **iOS** apps.
- **Open source + public API:** the codebase is open source ("Help improve it!") and exposes an **API** (linked in the footer) — the basis for programmatic access to team/event/match data.
- **Community-data model:** invites teams to add offseason events + data ("Add an Offseason Event", "Adding Data Overview"); funded via **Donate** + a **platinum sponsor**.
- **Hosts season resources:** links the **REBUILT Game Manual and Materials** and **FIRST 2027 Game and Season Resources**; counts down to **2027 Kickoff (Jan 16, 2027)**, streamed live on GameDay.
- **Currency:** the homepage is generated fresh per request (footer "This page was generated on Jun. 15, 2026…"); "This Week's Events" listed live offseason events (e.g., NC/RC, Illinois State Championship, Duel on the Delaware).

> [!note] Access note
> TBA returns **HTTP 403 to WebFetch**; this ingest was fetched via `curl` with a browser user-agent. For structured data, the TBA **API** (or that approach) is the reliable path — see the [Team 4414 2026 record](tba-team-4414-2026.md), fetched the same way.

## Entities mentioned

- [The Blue Alliance](../entities/the-blue-alliance.md) (the platform)
- [FIRST Robotics Competition](../entities/first-robotics-competition.md) — the competition TBA tracks

## Concepts touched

- **Third-party open competition data** — TBA is the community-maintained record layer over FIRST's events; the wiki treats it as the authoritative results source for FRC teams ([Team 254](../entities/team-254.md), [Team 4414](../entities/team-4414-hightide.md)).
- **Scouting** — TBA + myTBA as the data backbone teams build scouting workflows on (cf. Team 4414's in-house "Tide Apps" scouting suite).

## Open questions

- Exact TBA API surface / auth model (the homepage links an API but specifics aren't captured here) — would justify a dedicated API ingest if the wiki starts pulling FRC data programmatically.
- Governance/funding specifics beyond "volunteer-run, donation + platinum sponsor."

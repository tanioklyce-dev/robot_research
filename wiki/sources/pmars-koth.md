---
title: "pMARS — Portable Redcode Simulator (KOTH.org homepage)"
type: source
url: http://www.koth.org/pmars/
author: Albert Ma, Nándor Sieben, Stefan Strack, Mintardjo Wangsaw (+ later contributors)
published: 1993-08-25
ingested: 2026-05-31
format: web
license: GPL-2.0 (per Debian/FreshPorts packaging)
tags: [core-war, pmars, mars, redcode, simulator, icws-94, koth, programming-game, tooling]
---

> [!note] Fetch note
> `koth.org/pmars/` timed out repeatedly at ingest time; this page is grounded in the **rec.games.corewar FAQ-level facts** corroborated via corewar.co.uk + Debian/FreshPorts/Ubuntu packaging metadata, not a live read of the homepage.

## Summary

**pMARS ("Portable MARS")** is the **de-facto standard Core War simulator** — a portable, C-language implementation of the [MARS](../entities/core-war.md) virtual machine that runs [Redcode](../entities/core-war.md) warriors. It became the **official Redcode simulator of the rec.games.corewar community**. **KOTH.org** ("King of the Hill") is the long-running home of pMARS and of the email-based **KOTH tournament hills** where warriors compete continuously online.

## Key claims / facts

- **Authors.** Written in C by **Albert Ma, Nándor Sieben, Stefan Strack, and Mintardjo Wangsaw** (with later contributors); first version released **1993-08-25**.
- **Why it exists.** The project was started after the **ICWS'94 draft standard** was proposed on **rec.games.corewar** — the community needed a portable simulator to **try out, modify, or reject** the proposed standard.
- **Standards.** Implements the **ICWS'94 draft** standard and can also run in **ICWS'88 mode**; the modern build supports extended '94 Redcode, **p-space** (persistent storage across rounds), and read/write field limits.
- **Portability.** Cross-platform: **DOS, UNIX/Linux, Windows** (the corewars.org site points players to "the pMARS homepage" for these builds); packaged in Debian (`pmars`), FreeBSD ports, Ubuntu.
- **KOTH = King of the Hill.** An online tournament format: a warrior is submitted (historically by email) and challenges a "hill" of N resident warriors; the lowest-scoring warrior is bumped off. KOTH.org hosted the canonical hills.

## Entities mentioned
- [Core War](../entities/core-war.md) — pMARS is the standard simulator that runs the game's Redcode warriors.

## Concepts touched
- [Artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md) — pMARS is the *tooling* layer of the Core War programming-game lineage.

## Open questions
- Current maintenance status: pMARS is decades old; active forks exist on GitHub (e.g. `mbarbon/pMARS`, `akosela/pmars`) — which (if any) is the canonical maintained line is not captured here.
- Exact licensing per-file (the umbrella is GPL per Linux distro packaging, but the original distribution had mixed terms) — not verified at the file level.

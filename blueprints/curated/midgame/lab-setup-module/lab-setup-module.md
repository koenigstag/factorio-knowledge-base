# Lab Setup Module

Third-party blueprint, sourced by the project owner. Filed under
`curated/midgame/` — its own description names `fast-inserter` and
`fast-transport-belt` ("red belts") as requirements, i.e. authored for
midgame tier from the start; see `earlygame/lab-setup-module` in this
project for a tier-1 downgrade of this same design, covering
`guides/early_game_progression_checklist.md`'s step 2 lab gap at the
earlygame stage instead.

Blueprint's own label: `"Science setup"`. 118 entities: `lab` (14),
`fast-transport-belt` (56), `fast-underground-belt` (10),
`fast-inserter` (22), `long-handed-inserter` (8),
`medium-electric-pole` (8). No `constant-combinator`s — unlike the
science-pack production modules elsewhere in this project's
`curated/`, this design carries no informal lane labels; the site's
own listing says "Each input belt should have it's own science pack
type (see screenshot)" but the screenshot itself wasn't fetched, so
which belt carries which pack isn't recorded here as fact.

## Layout

14 labs in two banks (roughly 5+5+4 across three rows, with one lab
tucked into a central gap) straddling a belt corridor. One tunnel pair
(entities 115→56, a 6-tile entrance-to-exit span) carries a lane
*underground specifically to free up its surface tiles* for two
`long-handed-inserter`s sitting directly on the tunnel's path — the
belt passes beneath them rather than being routed around.

## Provenance

- Author: Roel (factorio.school user; display name resolved via the
  site's public Firebase Realtime Database at
  `/users/<userId>/displayName` — factorio.school and factorioprints.com
  share the same backend, see `tools.md`'s "same project, official
  rename" entry).
- Source: https://www.factorio.school/view/-MJ8OPOMPa66QqJPH2Oo, titled
  "Science Lab Setup". Created/last updated 2020-10-08 (a genuine
  Factorio 1.0 export — `version` decodes to `1.0.0.0`), 20 favorites
  as of 2026-08-23. Site's own description: "Easy and extendable
  Science Lab Setup. Requirements: red belts / fast inserters /
  longhanded inserters. Each input belt should have it's own science
  pack type (see screenshot). Easily upgradable to blue belt with an
  upgrade planner."
- Added to the repository: 2026-08-23, at the project owner's request
  — fills the "no lab/research blueprint" gap identified while
  discussing `guides/early_game_progression_checklist.md`'s first two
  steps (nothing in this project's curated blueprints previously
  consumed science packs, only produced them).

## Validation

`blueprints/validate.py` (factorio-draftsman): **OK, 0 errors, 0
warnings** — unlike this project's pre-2.0 (0.17.x) curated entries,
draftsman's converters do cover Factorio 1.0, so this one validates
cleanly rather than failing on version support.

`build_vectors.py`: 30 inserters (0 flagged/ambiguous), 21 belt_runs,
5 underground-tunnel pairs (0 dead-ends).

Verified: 2026-08-23

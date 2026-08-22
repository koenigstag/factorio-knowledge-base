# City Block 100×100 — Midgame Edge/Poles Variant

Personal blueprint, not a third-party design — the project owner's own
build. Same base filename as
[earlygame/city-block-100x100.md](../earlygame/city-block-100x100.md),
but genuinely different content (different byte size/hash, not a
duplicate) — the two live in separate stage folders precisely because
the same design recurs at different tiers as the game progresses (here:
fewer, longer-reach `big-electric-pole` instead of the earlygame
variant's many `small-electric-pole`), and folder-per-stage is how this
project's own blueprint collection tells those variants apart rather
than needing distinct names for what's conceptually the same block.

Blueprint's own label: `"poles"`. 56 entities: `small-lamp` (32),
`big-electric-pole` (20), `roboport` (4) — a lighter edge/power/
lighting skeleton than the earlygame variant, no rail or production
entities in this specific save.

## Ports: not applicable (author-confirmed)

Same reasoning as
[earlygame/city-block-100x100.md](../earlygame/city-block-100x100.md):
no belt entities at all, and not a production module — a tileable
layout template, not something that imports or exports items.

## Provenance

- Author: project owner (self-authored).
- Filed under `blueprints/curated/midgame/` — game-stage folders
  organize the project owner's personal collection; third-party
  entries stay flat at `curated/`'s root.
- Added to the repository: 2026-08-09.

## Validation

`blueprints/validate.py` (factorio-draftsman): **OK — 0 errors, 56
warnings**, all `UnknownKeywordWarning` on `ElectricPole`/`Lamp`/
`Roboport` entities for an unrecognized `direction` key (same
suspected schema-version gap as
[earlygame/24x2-stone-furnaces-module.md](../earlygame/24x2-stone-furnaces-module.md)),
not an entity/placement problem. `codec.py`'s own decode succeeds
cleanly.

Verified: 2026-08-09

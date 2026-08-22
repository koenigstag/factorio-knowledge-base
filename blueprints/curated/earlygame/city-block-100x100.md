# City Block 100×100 — Early-Game Edge/Poles Variant

Personal blueprint, not a third-party design — the project owner's own
build. Same base filename as
[midgame/city-block-100x100.md](../midgame/city-block-100x100.md), but
genuinely different content (different byte size/hash, not a
duplicate) — the two live in separate stage folders precisely so a
name like this one doesn't collide, since the actual difference is a
tier upgrade, not a redesign: this earlygame version wires the block's
edge with many short-reach `small-electric-pole`s, while the midgame
version switches to fewer, longer-reach `big-electric-pole`s (the
"big ЛЭП" — big power-line poles) covering the same 100×100 footprint
with less infrastructure once that tier is unlocked.

Blueprint's own label: `"poles"`. 116 entities: `small-electric-pole`
(80), `small-lamp` (32), `roboport` (4) — just the edge/power/lighting
skeleton of a 100×100 city-block cell, no rail or production entities
included in this specific save — presumably meant to be combined with
separate rail/production blueprints for the block's interior, the way
[nilaus_100x100_city_block.md](../nilaus_100x100_city_block.md)'s book
splits the same concerns into separate named sub-blueprints.

## Ports: not applicable (author-confirmed)

No `transport-belt`/`underground-belt`/`splitter` entities at all, so
`blueprints/codec.py`'s `classify_edge_ports` has nothing to find. Not
a production module — a tileable *layout* template (edge poles/lamps/
roboport coverage only), not something that imports or exports items,
unlike every other entry in this project's `curated/` collection so
far. The import/export port question this project has been answering
for the mining and smelting modules doesn't apply here.

## Provenance

- Author: project owner (self-authored).
- Filed under `blueprints/curated/earlygame/` — game-stage folders
  organize the project owner's personal collection; third-party
  entries stay flat at `curated/`'s root.
- Added to the repository: 2026-08-09.

## Validation

`blueprints/validate.py` (factorio-draftsman): **failed to parse**
(`list index out of range`, an internal draftsman error). `codec.py`'s
own decode succeeds cleanly — same suspected schema-version-gap cause
as the other entries here that fail the same way.

Verified: 2026-08-09

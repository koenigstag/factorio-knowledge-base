# Iron Gear Tileable — Midgame Tier-2 Variant

Personal blueprint, not a third-party design — the project owner's own
build.

Blueprint's own label: `"Iron Gear Maker"`. 37 entities:
`fast-transport-belt` (18), `fast-inserter` (12), `assembling-machine-2`
(4, each with `recipe: "iron-gear-wheel"`), `medium-electric-pole` (2),
`small-electric-pole` (1) — the midgame successor to
[earlygame/iron-gear-tileable.md](../earlygame/iron-gear-tileable.md):
identical layout and bounding box (`x:[-6.5,5.5] y:[-2.5,2.5]`), same
entity positions and directions throughout, upgraded to
`assembling-machine-2`, tier-2 (fast) belts/inserters, and mostly
`medium-electric-pole` (one `small-electric-pole` remains, at
`(0.5,0.5)`, replacing the earlygame version's third pole position).

**Tileable for scaling** (author-confirmed, same pattern as the
earlygame version): each copy's export row feeds the next copy's
import row directly.

## Ports

Structured, author-confirmed data:
[iron-gear-tileable.ports.json](iron-gear-tileable.ports.json). Same
port layout as
[earlygame/iron-gear-tileable.md](../earlygame/iron-gear-tileable.md)
— confirmed identical by re-running `classify_edge_ports`
(`blueprints/codec.py`) against this blueprint's own entities, not
assumed from the earlygame result:

- **2 outer lanes** (`x=-6.5` west, `x=5.5` east), facing South: carry
  **iron-plate** in to the assemblers. Import at `y=-2.5`, export at
  `y=2.5`.
- **1 shared center lane** (`x=-0.5`), facing North: carries
  **iron-gear-wheel** out, opposite flow direction from the outer
  lanes. Import at `y=2.5`, export at `y=-2.5`.

Same "raw material outside, product inside" shape as
[layouts/smelter_module_ports.md](../../../layouts/smelter_module_ports.md)'s
"Plate on the inside" furnace pattern — see
[earlygame/iron-gear-tileable.md](../earlygame/iron-gear-tileable.md)
for the full reasoning; nothing about the port topology changes with
the tier upgrade, only entity names.

## Provenance

- Author: project owner (self-authored).
- Filed under `blueprints/curated/midgame/` — game-stage folders
  organize the project owner's personal collection; third-party
  entries stay flat at `curated/`'s root.
- Added to the repository: 2026-08-09.

## Validation

`blueprints/validate.py` (factorio-draftsman): **failed to parse**
(`list index out of range`, an internal draftsman error). `codec.py`'s
own decode succeeds cleanly — same suspected schema-version-gap cause
as the other entries here that fail the same way, not evidence of a
corrupt blueprint.

Verified: 2026-08-09

# Iron Gear Tileable

Personal blueprint, not a third-party design — the project owner's own
build.

Blueprint's own label: `"Iron Gear Maker"`. 37 entities: `transport-belt`
(18), `inserter` (12), `assembling-machine-1` (4, each with
`recipe: "iron-gear-wheel"` explicitly set), `small-electric-pole` (3) —
a tileable iron-gear-wheel production block: 4 assemblers (2 pairs,
stacked vertically on the west and east sides) fed by iron-plate on two
outer belt lanes, with their combined iron-gear-wheel output collected
onto one shared central lane.

**Tileable for scaling** (author-confirmed, same pattern as
[4x2-stone-furnaces-w-upgrade-spacing.md](4x2-stone-furnaces-w-upgrade-spacing.md)):
each copy's export row feeds the next copy's import row directly.

## Ports

Structured, author-confirmed data:
[iron-gear-tileable.ports.json](iron-gear-tileable.ports.json).
3 parallel pass-through lanes, each an unbroken 6-tile `transport-belt`
run from `y=-2.5` to `y=2.5`:

- **2 outer lanes** (`x=-6.5` west, `x=5.5` east), facing South: carry
  **iron-plate** — the sole ingredient of `iron-gear-wheel` (confirmed
  against `datapacks/dump/vanilla/recipe/iron-gear-wheel.json`). Import
  at `y=-2.5` (north), export at `y=2.5` (south). Inserters at `x=-5.5`
  and `x=4.5` pick iron-plate off these lanes and feed it into the
  adjacent assembler pair.
- **1 shared center lane** (`x=-0.5`), facing North — the opposite flow
  direction from the outer lanes: carries **iron-gear-wheel**, the
  product. Import at `y=2.5` (south), export at `y=-2.5` (north).
  Inserters at `x=-1.5` (west assembler pair) and `x=0.5` (east
  assembler pair) pull the finished gear wheels off their assemblers and
  drop them onto this lane.

`classify_edge_ports` (`blueprints/codec.py`) found all 6 candidate
tiles correctly (3 import, 3 export) from belt direction alone, but —
per `blueprints/README.md`'s "Import/export port heuristic" rule —
neither the resource identity of each lane nor the inserter pickup/drop
side came from the geometry alone; both are author-confirmed. The first
pass at this analysis had the outer/center resource assignment and the
inserter pickup/drop side backwards; the table above reflects the
corrected, author-confirmed reading.

This is the same "raw material outside, product inside" shape as
[layouts/smelter_module_ports.md](../../../layouts/smelter_module_ports.md)'s
"Plate on the inside" furnace pattern, generalized past furnaces to an
assembling-machine module: iron-plate (the input) arrives via the 2
outer lanes, iron-gear-wheel (the product) leaves via the shared center
lane — furnaces and assemblers land on the same design principle.

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
as the other entries here that fail the same way, not evidence of a
corrupt blueprint.

Verified: 2026-08-09

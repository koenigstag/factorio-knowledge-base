# Main bus consumer layout: city-block modules fed by a bus through gaps

The belt-specific composition of [city-block](../glossary/canonical/city-block.md)
and [main-bus](../glossary/canonical/main-bus.md): a grid of blocks
with the bus itself running through the gaps between them, each block
tapping in/out via a dedicated module. Split out from
[layouts/city_block_grid.md](city_block_grid.md) (2026-08-09) once it
became clear that file's own dominant community usage is
**train**-connected, not bus-connected — this file is specifically the
belt variant, not "the" city-block-grid pattern.

## Structure

- The base is a grid of [city-block](../glossary/canonical/city-block.md)
  modules — repeatable, similarly-sized processing units.
- Adjacent blocks along the bus axis are separated by an empty strip
  of space, not placed edge-to-edge. The
  [main-bus](../glossary/canonical/main-bus.md) itself runs through
  that space, not through the blocks — a block never touches the bus
  directly, it only reaches it via a
  [tap-module](../glossary/invented/tap-module.md) sitting in the gap
  beside it. See "Gap width" below for the space convention.
- Most blocks are regular: `tap-module` pulls bus items in on one
  side, pushes the block's output back onto the bus on the other.
- Some grid positions spend one of those two bus-facing ports on
  something else instead — a secondary bus or a rail export siding —
  so their output leaves the grid rather than rejoining the main bus
  (e.g. `layouts/scalable_main_base.md`'s red/green science modules,
  which feed a dedicated science bus this way).
- Bus orientation (which axis it runs along) and grid size (rows ×
  columns) are choices for a specific base, not fixed by this pattern.

**Concrete instance**: `layouts/scalable_main_base.md` — city-block
modules, tap-modules in the gaps, main bus through the gaps, exactly
as described above.

## Gap width

Adjacent modules placed one after another along the bus (not directly
across from it) aren't placed edge-to-edge either — practical
convention reserves a strip of space between them, sized in chunks:
**1-3 chunks**, 1 most common, 2 less common, 3 when that space needs
to hold export storage + a single-track railway + the next module's
import belts, one chunk each. This is conveyor-belt space by design —
room for the tap-in/tap-out infrastructure connecting each module to
the bus, not a buffer for its own sake.

Practical convention, not independently sourced to a specific
publication or derived from `formulas/` primitives — stated by the
project owner as working knowledge. A formal derivation would still
need real component sizes, e.g.
[mechanics/rails.json](../mechanics/rails.json)'s `curve_radius_tiles`
(turnout clearance) for the railway-chunk case specifically. Whether a
rail export siding needs a dedicated additional chunk or reuses the
standard tap chunk is also unresolved.

## What's still open (not resolved by writing this file)

- **Diverted-output block port geometry** — which side becomes the
  export-facing port, and whether it needs a dedicated additional gap
  or reuses the standard tap gap, is unresolved.
- ~~Whether this pattern is worth adopting at all past a certain
  scale~~ — resolved by
  [decisions/0003](../decisions/0003-main-bus-as-bootstrap-city-block-train-bus-as-target.md):
  this project treats it as an explicit early-game bootstrap, not a
  permanent architecture — city-blocks + train-bus is the stated
  long-game target. The underlying community sourcing itself
  (`glossary/invented/train-bus.md`, `layouts/main_bus.md`'s "Red vs
  blue circuit"/"bus is early/mid-game infrastructure" sections) is
  still genuinely split, not unanimous; this project's position is a
  decision made with that split in view, not a claim that the
  community has settled it.
- ~~What the bootstrap-to-target transition actually looks like~~ —
  resolved: see
  [layouts/main_bus_to_city_block_transition.md](main_bus_to_city_block_transition.md).

Coined by connecting existing glossary entries; not yet backed by a
`decisions/` ADR recording why this particular composition (bus
through gaps, tap-module as the only bus contact point) was chosen
over alternatives.

# City-block grid: how city-block / main-bus / gap-chunk / export-block compose

Ties together 4 terms that so far only existed as separate
`glossary/invented/`+`glossary/canonical/` entries cross-referencing
each other in prose. This file is the composition itself.

## Structure

- The base is a grid of [city-block](../glossary/canonical/city-block.md)
  modules — repeatable, similarly-sized processing units.
- Adjacent blocks along the bus axis are separated by a
  [gap-chunk](../glossary/invented/gap-chunk.md), not placed
  edge-to-edge. The [main-bus](../glossary/canonical/main-bus.md)
  itself runs through the gap-chunks, not through the blocks — a
  block never touches the bus directly, it only reaches it via a
  [tap-module](../glossary/invented/tap-module.md) sitting in the
  adjacent gap-chunk.
- Most blocks are regular: `tap-module` pulls bus items in on one
  side, pushes the block's output back onto the bus on the other.
- An [export-block](../glossary/invented/export-block.md) is a grid
  position that spends one of those two bus-facing ports on something
  else instead — a secondary bus or a rail export siding — so its
  output leaves the grid rather than re-joining the main bus.
- Bus orientation (which axis it runs along) and grid size (rows ×
  columns) are choices for a specific base, not fixed by this pattern.

## What's still open (not resolved by writing this file)

- **gap-chunk width** — [gap-chunk.md](../glossary/invented/gap-chunk.md)
  already flags this unresolved ("2-3 chunk estimate... not yet
  re-derived as a formula"). This file doesn't change that. Whatever
  eventually derives it will need to size 3 independent things that
  share the gap: the `tap-module` belt/pipe run, a
  [lane balancer](../glossary/canonical/lane-balancer.md) if one is
  used, and an optional rail siding. The rail siding component
  specifically is the one piece with real sourced numbers already
  sitting in this repo ready to use —
  [constraints/rails.json](../constraints/rails.json)'s
  `curve_radius_tiles` (turnout clearance) and
  [constraints/trains.json](../constraints/trains.json)'s
  wagon/locomotive `tile_box` (siding length needs to fit a full
  train) — but combining them into one gap-chunk width figure hasn't
  been done here.
- **export-block port geometry** — which side becomes the export port,
  and whether it needs a dedicated additional gap-chunk or reuses the
  standard tap gap, is unresolved (also flagged in
  [export-block.md](../glossary/invented/export-block.md)).
- **city-block size itself** — intentionally left undefined, not an
  oversight: production modules (drills, furnaces, assembling
  machines, labs, ...) have different footprints, so there's no single
  "correct" block size the way there's one correct `tile_box` for a
  single building. Convention: express it in chunk fractions rather
  than an absolute tile count — a single production module ≈ 1/2 chunk
  (16×16 tiles, since `constraints/world.json`'s `chunk_size_tiles=32`)
  is the commonly cited baseline. Stated here as the project owner's
  own planning heuristic, not an independently sourced or derived
  figure — not yet checked against real building footprints in
  `datapacks/`.

Coined by connecting existing glossary entries; not yet backed by a
`decisions/` ADR recording why this particular composition (bus
through gap-chunks, tap-module as the only bus contact point) was
chosen over alternatives.

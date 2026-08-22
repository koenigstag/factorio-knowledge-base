# Bootstrap-to-target transition: build for the city-block grid while still on the bus

Fills the gap [decisions/0003](../decisions/0003-main-bus-as-bootstrap-city-block-train-bus-as-target.md)
flagged as unwritten: what actually happens when a base built on
[main_bus_consumer_layout.md](main_bus_consumer_layout.md) (the
bootstrap) moves into a [city_block_grid.md](city_block_grid.md)-shaped,
train-connected grid (the target).

## The core idea: build to the target footprint from day one

Project owner's stated design position (2026-08-09): even while a base
is still in its main-bus bootstrap phase, its consumer blocks should
already be positioned and sized as if they were `city_block_grid.md`
cells — not laid out ad-hoc and reflowed later. The reasoning:

A city-block's *interior* (the drills/furnaces/assembling-machines
actually doing the production) doesn't know or care how its inputs
arrive or its outputs leave — that's the block's edge, not its core.
During the bootstrap phase the edge is a
[tap-module](../glossary/invented/tap-module.md) reaching into the
main bus running through the gap beside it
(`main_bus_consumer_layout.md`'s pattern). At the target, the edge is
a rail station instead. Nothing about the interior module changes
between those two states — only the interface at its border does.

So if a block is already positioned on the grid the target pattern
will eventually use, reaching the target doesn't mean rebuilding
production — it means swapping one edge module for another, block by
block, while the interior keeps running the whole time. Building
ad-hoc during bootstrap and only imposing grid discipline later would
instead mean physically relocating or rebuilding every module once the
transition starts — the exact large, disruptive rebuild this approach
is meant to avoid.

## What "build to the target footprint" means concretely

- **Position blocks on the target grid's coordinate system from the
  start.** Pick one of `city_block_grid.md`'s block sizes now (this
  project's own bias, inherited from `layouts/scalable_main_base.md`'s
  "City-block size" section, is 100×100 — the one candidate with an
  independent derivation, via roboport logistic-network spacing, not
  just cited convention) and place every block's origin at a multiple
  of that size, even during the bus-fed phase.
- **Reserve edge space for a future rail connection, not just the
  belt-tap gap.** `main_bus_consumer_layout.md`'s gap (1-3 chunks) is
  sized for belt infrastructure — tap-module, export storage, the next
  block's import belts. A future rail spur and station need more than
  that: at minimum, room for `mechanics/rails.json`'s
  `curve_radius_tiles=13` turning geometry plus turnout clearance.
  **No hard figure for this reserved amount is given here** — turnout
  clearance itself is still an open item in `city_block_grid.md`'s
  "What's still open" section, so this file inherits that gap rather
  than inventing a number to fill it. `city_block_grid.md`'s "Rail
  spacing between blocks" section (three published designs
  cross-checked directly from their blueprint data) found this varies
  by an order of magnitude even among real designs — from 0 extra
  tiles (Nilaus's 100×100, rail built entirely within the block's own
  footprint) to 64+ tiles (a high-throughput multi-lane elevated-rail
  skeleton) — so "generously more than the belt-only gap" is the most
  that can be said without first deciding how ambitious a rail
  connection this base's target actually needs.
- **The main bus itself is a temporary tenant of that reserved space**,
  not a permanent fixture — it runs through the same gap during
  bootstrap, but gets removed once every block along that segment has
  migrated (see below), freeing the space back up for rail.

## The transition sequence, block by block

1. Build the block's rail spur and station in the edge space already
   reserved for it. This doesn't touch the block's interior at all.
2. Rewire the block's input/output from the tap-module to the new
   station's inserters/pumps. The production chain inside keeps
   running throughout — only its supply/demand interface moves.
3. Once a block is rail-fed, its tap-module and the stretch of bus
   feeding it are redundant for that block specifically — but the bus
   segment itself may still be live if other blocks further along it
   haven't migrated yet.
4. Once **every** block along a given bus segment has migrated, that
   segment is fully redundant — remove it. The freed corridor becomes
   available for something else (widening a junction, an additional
   station track, etc.), not left as dead space.

A base with some blocks still bus-fed and others already rail-fed at
the same time is an expected, valid intermediate state under this
approach, not a failure mode — it's the direct consequence of the
interior/edge split above: each block migrates independently, on its
own schedule, because its neighbors' state doesn't affect whether its
own interior still works.

## Tradeoff: reserved space now vs. rebuild cost later

This isn't free. Reserving city-block-grid-aligned footprint and extra
edge space from the start makes the bootstrap-phase base less
space-efficient than laying it out ad-hoc would be — some of that
reserved space sits unused (or only lightly used, by the temporary bus)
until the block actually migrates.

The trade this project's stated position makes: removing a main-bus
corridor later is a small, local, reversible action (pick up belts,
maybe some poles). Rebuilding a production module — or worse, an
entire ad-hoc-sized grid of them — to fit a different block size and
alignment is not reversible in the same way; it's a full teardown and
rebuild. Paying a modest, ongoing space cost during bootstrap to avoid
a large, one-time rebuild cost at the transition is the same logic
already behind `layouts/scalable_main_base.md`'s cited **68Cadillac**
quote (*"Main bus is just a stepping stone"*) — this file extends that
framing one step further: the stepping stone is cheaper to cross if the
base was already built standing where it needs to land.

## What's still open

- **Reserved edge-space figure** — no number given here, inherits
  `city_block_grid.md`'s open turnout-clearance gap. Until that's
  derived, "reserve generously more than the belt gap" is a qualitative
  rule, not a sized one.
- **Whether a live bus corridor blocks or coexists with an
  already-migrated neighbor's station footprint** — not modeled here;
  this file assumes reserved space is large enough for both to coexist
  during the mixed-mode window, but that assumption isn't checked
  against real junction/signal geometry.
- **Standardized train length/signaling** — inherited from
  `city_block_grid.md`/`glossary/invented/train-bus.md`; needed before
  stations get built out at scale, not specific to the transition
  itself.
- Whether it's ever worth reserving for a size *larger* than the
  base's chosen target (e.g. building 100×100-positioned blocks that
  could later merge into 128×128 cells) — not considered here; this
  file assumes the target size is decided once, up front, not itself
  revised mid-transition.

Not independently sourced to a third-party publication — this is the
project owner's own design reasoning extending decision 0003, the same
confidence tier as `main_bus_consumer_layout.md`'s gap-width
convention ("stated by the project owner as working knowledge").

Verified: 2026-08-09

# city block

A base-layout pattern: organize production into a grid of
self-contained, similarly-sized modules ("blocks"), each connected to
a shared rail and/or belt grid rather than one continuous sprawling
bus. Named by direct analogy to urban-planning city blocks. Trades
some train-routing complexity (a commonly cited limiting factor on
megabases built this way) for uniform, easily-repeatable expansion.

Unlike `main bus`, this term has no official Wube wiki tutorial page
and no entry in the official glossary — it's community-coined. The
forum thread below doesn't state a formal definition either (it's a
build-feedback thread, not a tutorial), but its discussion directly
supports the modularity/pathfinding tradeoff described above:
> "City blocks are great because of many reasons like modularity and
> ease of expansion, fun, symmetry" ... "best avoided [by some] because
> they complicate a lot the pathfinding for trains"

See [layouts/city_block_grid.md](../../layouts/city_block_grid.md) for
the dominant, rail-connected shape of this pattern, or
[layouts/main_bus_consumer_layout.md](../../layouts/main_bus_consumer_layout.md)
for the belt-through-gaps alternative. Opposite approach: [monolith](monolith.md)
(one site, no repeatable unit). Easy to confuse with, but distinct
from: [micro-factory](micro-factory.md) (self-contained, not
necessarily adjacent, usually train-fed rather than bus-fed).

Source: https://forums.factorio.com/viewtopic.php?t=126785 (community usage, not a formal definition)
Verified: 2026-08-06

## Block size: community convention, one figure independently cross-checked

Three sizes recur across community discussion, in tiles per block
side:

| size | chunks | rationale |
|---|---|---|
| 96×96 | exactly 3×3 | clean chunk alignment (`mechanics/world.json`'s `chunk_size_tiles=32`); fine if the base won't lean heavily on roboports |
| 100×100 | not chunk-aligned | matches roboport logistic-network connection distance — see below |
| 128×128+ | exactly 4×4 | more interior room for longer trains (2-4/4-8), wider junctions, station bays |

Only the 100×100 figure has a mechanism this project can independently
verify, rather than just cite: the forum reasoning given is roboport
"50+50 tiles" connection distance, which matches
[relations/roboport_network_range.md](../../relations/roboport_network_range.md)'s
own wiki-sourced, formula-derived `max_connection_distance=50` tiles
for the logistic network (`2 × logistics_radius`, `logistics_radius=25`
from `datapacks/dump/vanilla/roboport/roboport.json`) — a 100×100 grid
lets roboports at adjacent block centers land exactly at that 50-tile
maximum spacing. The 96×96 and 128×128 figures are cited as-is from
the forum thread without an equivalent independently-derivable
mechanism found this session — train-length and junction-footprint
reasoning is qualitative in the source, not tied to a sourced number
the way the roboport case is.

Derived one step further in
[relations/roboport_area_coverage.md](../../relations/roboport_area_coverage.md):
gap-free *logistic* coverage of a 96×96 or 100×100 block needs a 2×2
grid (4 roboports), while a single roboport's *construction* area
already covers either block on its own; a 128×128 block needs 9 for
logistic, 4 for construction.

Sources: https://forums.factorio.com/viewtopic.php?t=105310 (community
forum, primary — 96×100×128 figures and the roboport/train-length
reasoning); https://factoriocalculator.blog/factorio-city-block-size/
(secondary, lower confidence — a fan blog, not forum/wiki consensus;
corroborates the same three sizes with qualitative train/junction
reasoning but no derivation)
Verified: 2026-08-08

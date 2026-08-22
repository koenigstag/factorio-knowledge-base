# City-block grid: a grid of blocks, each connected by rail

The dominant community shape of [city-block](../glossary/canonical/city-block.md):
a grid of repeatable, similarly-sized modules, dense and packed
block-to-block, each connected to the rest of the base by its own
[train-base](../glossary/canonical/train-base.md) point-to-point rail
station — not a shared belt bus running through the grid. Community
sourcing leans toward this being the more common and better-scaling
pattern at megabase size specifically: see
`glossary/invented/train-bus.md` (burenning's mechanical explanation of
why a belt bus resists combining with a block grid — every block would
have to sit adjacent to it) and `layouts/main_bus.md`'s "Red vs blue
circuit"/"bus is early/mid-game infrastructure" sections. For the
belt-through-gaps alternative (main bus running through the grid
instead of rail), see
[layouts/main_bus_consumer_layout.md](main_bus_consumer_layout.md) —
split out separately (2026-08-09) once it became clear that variant
isn't this file's own dominant case.

## Structure

- The base is a grid of [city-block](../glossary/canonical/city-block.md)
  modules — repeatable, similarly-sized processing units, packed
  block-to-block rather than spread out.
- Each block gets its own rail station(s), a
  [train-base](../glossary/canonical/train-base.md) connection to
  whatever supplies its inputs and takes its outputs — not a shared
  line every block taps into (that would be a
  [train-bus](../glossary/invented/train-bus.md), which
  `train-bus.md` itself notes this project hasn't actually built
  anywhere yet, despite several rail-connected layouts).
- Spacing between blocks is rail infrastructure — track, signals,
  junction footprint, turning radius — not belt-tap room the way
  `main_bus_consumer_layout.md`'s gap is. Not formalized here (see
  "What's still open").
- Bus orientation doesn't apply in the same way it does for the belt
  variant; grid size (rows × columns) is still a per-base choice.

## Block size: community convention, one figure independently cross-checked

Three sizes recur across community discussion, in tiles per block
side — this part of the pattern is transport-agnostic (the same sizes
get cited regardless of whether a given base ends up rail- or
belt-connected):

| size | chunks | rationale |
|---|---|---|
| 96×96 | exactly 3×3 | clean chunk alignment (`mechanics/world.json`'s `chunk_size_tiles=32`); fine if the base won't lean heavily on roboports |
| 100×100 | not chunk-aligned | matches roboport logistic-network connection distance — see below |
| 128×128+ | exactly 4×4 | more interior room for longer trains (2-4/4-8), wider junctions, station bays |

Only the 100×100 figure has a mechanism this project can independently
verify, rather than just cite: the forum reasoning given is roboport
"50+50 tiles" connection distance, which matches
[relations/roboport_network_range.md](../relations/roboport_network_range.md)'s
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
[relations/roboport_area_coverage.md](../relations/roboport_area_coverage.md):
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

## Rail spacing between blocks: three published designs, no single convention

Neither general web search nor the forum thread above states a figure
for the empty space a rail-connected grid reserves between blocks
(distinct from the block's own interior size) — searched specifically
for this, found nothing citable. Stronger than a forum quote: decoded
three real, independently-published city-block blueprints directly
(retrieved via factorioprints.com's public Firebase REST API,
`blueprintString` field, standard Factorio encoding — version byte +
base64 + zlib-deflated JSON — then measured each design's own entity
positions against its `snap-to-grid` cell size) rather than trusting a
secondhand description of one.

| design | author | cell size | rail infra vs. cell | source |
|---|---|---|---|---|
| "Updated 100×100 City Blocks - Snapped to Grid" | Nilaus | 100×100 | **Fits entirely inside the cell** — rail-only entities (train station variant) bbox `x:[1,99] y:[13.5,86.5]`, no overflow past the block's own 0–100 edge. Generic edge decoration (lamps/poles) overflows ±6.5 tiles, but that's cosmetic trim mirrored across the shared border with the next block, not functional track space. | [factorioprints.com/view/-MOy8SsNcu5BNqCZ2ZnL](https://factorioprints.com/view/-MOy8SsNcu5BNqCZ2ZnL), curated locally: [blueprints/curated/nilaus_100x100_city_block.*](../blueprints/curated/nilaus_100x100_city_block/nilaus_100x100_city_block.md) |
| "City Block Rail Grid (8×8), elevated rails" | Aquael Q. | 256×256 (8×8 chunks) | **Overflows 64 tiles past each edge** (bbox `-64` to `320` around a 256 cell) — but this is a 4-lane, 2-level elevated-rail skeleton with O-turn loops and 8 station slots per the author's own spec, a qualitatively bigger design than a single-lane connector. | [factorioprints.com/view/-OqJqpOGjWRur_dCWYrE](https://factorioprints.com/view/-OqJqpOGjWRur_dCWYrE) |
| "DaviAMSilva's Rail City Block" | DaviAMSilva | 32×32 (1 chunk) | Different composition strategy entirely — junction/station pieces are standalone 1-chunk-snapped modules meant to be arranged flexibly ("not every section needs to be a perfect square"), not one fixed block-plus-gap template. | [factorioprints.com/view/-Mrt33eX6zhJnWe3QMSY](https://factorioprints.com/view/-Mrt33eX6zhJnWe3QMSY) |

**Conclusion: there is no single community-standard inter-block rail
spacing figure** — it depends on design ambition (a simple single-lane
connector needs none beyond the block itself; a high-throughput
multi-lane elevated skeleton needs a large shared margin) and
composition strategy (fixed block+gap vs. flexible modular chunk
pieces), not a fixed convention the way `100×100`'s block size itself
is. Recorded as three concrete, sourced data points rather than left
as a total unknown, but this doesn't resolve the "What's still open"
item below into a single number or formula.

Verified: 2026-08-09

## What's still open (not resolved by writing this file)

- **Rail spacing between blocks, formally** — see "Rail spacing
  between blocks" above: cross-checked against three published
  designs, found it genuinely varies (0 to 64+ tiles) by design
  ambition rather than following one convention, so there's still no
  single number or formula to state here — only that it depends on
  [mechanics/rails.json](../mechanics/rails.json)'s `curve_radius_tiles`
  (turnout clearance, itself still undetermined) and
  [mechanics/trains.json](../mechanics/trains.json)'s
  wagon/locomotive `tile_box` for whatever train length/configuration
  a base standardizes on.
- **city-block size itself** — still no single "correct" size the way
  there's one correct `tile_box` for a single building, since
  production modules (drills, furnaces, assembling machines, labs,
  ...) have different footprints. Partially resolved for one
  candidate (100×100, see above); still open whether 96×96 or 128×128
  have an equivalent independently-derivable mechanism, and whether
  any of the three has actually been checked against real
  production-module footprints (drill 3×3, furnace 2×2/3×3, etc.)
  rather than just roboport/train-length reasoning.
- **Standardized train length/signaling** — `glossary/invented/train-bus.md`
  flags this as the recurring practical complaint for a true shared
  train-bus; a dense point-to-point grid like this file describes
  needs it too, for every block's station to interoperate, but it
  isn't derived here.

Verified: 2026-08-09

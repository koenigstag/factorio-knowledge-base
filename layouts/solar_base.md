# Solar base: large panel/accumulator fields as their own outpost

A [solar base](../glossary/invented/solar-base.md) — an
[outpost](../glossary/canonical/outpost.md) dedicated to power
generation, separate from `layouts/scalable_main_base.md`,
`layouts/scalable_chem_base.md`, or any other production site. Solar
scales with the *whole megabase's* total power draw, not any single
block's, and the field footprint needed per MW is large enough that
folding it into another site's grid would distort that site's own
layout — the same reasoning `layouts/scalable_chem_base.md` already
used for why oil processing gets its own site.

## Core ratio

`relations/solar_accumulator_ratio.md`, fully derived from `data.raw`
(not cited): **23.81 solar-panel/MW**, **20.0 accumulator/MW**,
**0.84 accumulator/panel** — independently matching the community's own
published "21:25 (0.84)" figure exactly (`wiki.factorio.com`, cited in
that file).

## Footprint

`solar-panel`: `collision_box` ±1.4 → **3×3 tiles** (9 tiles).
`accumulator`: `collision_box` ±0.9 → **2×2 tiles** (4 tiles) (both
values pulled directly from `data.raw`, not assumed). Raw building
footprint per MW (no spacing/poles/roads yet): `23.81×9 + 20.0×4` ≈
**294 tiles²** — real built footprint will be larger once spacing for
poles and maintenance access is added, not derived here.

## Tileable cell: 25 solar-panel : 21 accumulator ≈ 1.05 MW

Clearing the 23.81/20.0 ratio to round numbers: 25 panels ÷ 23.81 =
1.050 MW, 21 accumulators ÷ 20.0 = 1.050 MW — both sides agree, so this
is a clean repeatable tile at the mathematically optimal ratio, not
just a round-number approximation.

**A different, commonly-blueprinted community cell** (`factorio.school`,
various) — 16 solar-panel : 12 accumulator arranged in a cross around a
central substation — is worth noting *not* the same ratio: `12/16 =
0.75`, short of the 0.84 optimum (yields 0.672 MW from panels vs 0.6 MW
from accumulators — accumulator-limited, i.e. it under-builds
accumulator buffer relative to panel output). A practical, popular
layout, not the precise optimum — cited here for the pattern (compact
cross around a substation, not a long row) rather than its exact counts.

## Internal distribution: substations

`substation` (`supply_area_distance=9`, `maximum_wire_distance=18`)
covers a much larger area than `small`/`medium-electric-pole`
(`supply_area_distance=2.5`/`3.5`) — the natural choice for tiling a
solar field, one substation per cell keeping the whole field on one
connected electric network. Community layouts (above) confirm this
convention (a substation at the center of each repeatable cell) rather
than this project deriving a specific tiling pattern from primitives.

## Connecting to other sites: pole chain, not rail

Every other outpost in this project (`layouts/scalable_chem_base.md`,
the remote labs site in `layouts/scalable_main_base.md`) connects by
rail. A solar base is different: **power has to reach every other site
through the electric network itself** — copper wire between poles, not
cargo. `big-electric-pole` (`maximum_wire_distance=32`,
`data.raw`) is the long-reach tier for this: a chain of them spaced at
their max distance covers roughly `(N-1)×32` tiles for `N` poles — e.g.
~10 poles bridge ~288 tiles, ~20 poles ~608 tiles. **Not resolved
here**: whether a solar base actually needs to be electrically chained
all the way to the main base and every outpost (one shared network), or
whether each remote site is expected to run its own local
solar/accumulator or nuclear supply instead and the "solar base" is
really only the main base's own power source — this project hasn't
settled which topology the wider megabase uses, and the answer changes
how far this pole chain actually has to run.

## What's still open

- Real per-cell footprint including pole/road spacing, not just raw
  building tiles.
- Whether one shared electric network spans the whole megabase (long
  pole chains to every outpost) or each site is self-powered — see
  above.
- Night-cycle timing differences if a future Space Age surface's solar
  base is considered (`relations/solar_accumulator_ratio.md`'s
  per-planet section already flags this as an assumption, not derived,
  for Vulcanus/Fulgora/Gleba/Aquilo).
- Target MW for a specific base isn't fixed here, by design — same
  "derive the ratio, don't cite a magic total" stance as
  `layouts/main_bus.md`.

Verified: 2026-08-09

# World grid

## chunk_size_tiles = 32

Size of a single map chunk (square) — the engine's world-generation
and alignment unit.

Source: https://wiki.factorio.com/Map_structure
Verified: 2026-08-06

## map_coordinate_max_tiles = 1,000,000

Maximum distance from the origin (0,0) in any direction. The full map
is therefore a 2,000,000 × 2,000,000 tile square — 4 trillion tiles
total. Not backed by any `data.raw` prototype (no "world"/"map"
entity) — a pure engine boundary, unrelated to any formula input.
Purely theoretical in practice: performance limits are reached long
before this coordinate range does.

Source: https://wiki.factorio.com/Map_structure
Verified: 2026-08-06

# Roboport count for gap-free area coverage

How many roboports a square area needs for full, gap-free coverage —
i.e. every tile inside is covered by at least one roboport's own area,
not just "the network is connected" (that's
`relations/roboport_network_range.md`, a different question).

Formula: `formulas/roboport_coverage_count.py:min_roboports_for_area`
— `ceil(width / (2×radius)) × ceil(height / (2×radius))`, placing
roboports on a grid spaced exactly `2×radius` apart so their square
coverage areas tile edge-to-edge with no gaps and no overlap.

Input: `datapacks/dump/vanilla/roboport/roboport.json` —
`logistics_radius=25` (50-tile side), `construction_radius=55`
(110-tile side).

## min_roboports_for_gapless_coverage

Applied to the three city-block sizes cited in
`glossary/canonical/city-block.md`:

| block size | logistic (side 50) | construction (side 110) |
|---|---|---|
| 96×96 | 4 | 1 |
| 100×100 | 4 | 1 |
| 128×128 | 9 | 4 |

Reading the 100×100 row: **one** roboport's construction area (110×110)
already covers the entire block on its own, but full *logistic*
(bot-network item/request) coverage of the same block needs a 2×2
grid of roboports — a single centered roboport's 50×50 logistic area
leaves the block's corners uncovered.

## Why the network-connection spacing and the gap-free tiling spacing are the same number

`relations/roboport_network_range.md`'s `max_connection_distance` (50
for logistic, 110 for construction) and this relation's tiling spacing
(`2×radius`) are the identical formula for a non-coincidental reason:
"two coverage-area borders touch" (the connection rule, see
`mechanics/roboport-network-connection.md`) and "two coverage areas
sit edge-to-edge with no gap between them" are the same geometric
condition. A roboport grid spaced for network connectivity is
automatically also a gap-free coverage grid, and vice versa — there's
no separate, larger spacing needed just to avoid dead zones.

Verified: 2026-08-08

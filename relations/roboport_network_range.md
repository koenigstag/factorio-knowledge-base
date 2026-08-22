# Roboport network connection range

Formula: `formulas/roboport_network_range.py:max_connection_distance`
— `2 × radius`, since each roboport's coverage area is a square
centered on it with `radius` as half the side length.

Input: `datapacks/dump/vanilla/roboport/roboport.json` —
`logistics_radius=25`, `construction_radius=55`.

## max_connection_distance_tiles

| area | radius | max center-to-center distance |
|---|---|---|
| logistic | 25 | 50 |
| construction | 55 | 110 |

Confirmed against wiki.factorio.com/Roboport: the logistic area is a
50×50 square ("orange"), the construction area is 110×110 ("green").
For *why* 50/110 tiles center-to-center is the actual maximum (not
merely close to it) and why logistic/construction connectivity are
judged independently, see
[mechanics/roboport-network-connection.md](../mechanics/roboport-network-connection.md)
— that's the qualitative engine-behavior rule this relation's numbers
plug into.

This distance also happens to be the exact grid spacing for gap-free
*area* coverage (not just network connectivity) — see
[relations/roboport_area_coverage.md](roboport_area_coverage.md) for
why, and for roboport-count-per-city-block figures built on top of it.

Verified: 2026-08-07

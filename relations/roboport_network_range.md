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
50×50 square ("orange"), and *"two or more roboports can connect to
form a logistic network, if the borders of the orange logistic areas
touch"* — border-touching is a `≤` condition, not strict overlap, so
50 tiles center-to-center is the actual maximum, not merely close to
it. Same rule for the 110×110 construction area ("green"), independent
of the logistic one.

## Two separate connection rules, not one

The wiki explicitly distinguishes them: construction robots cooperate
across the green (110-tile) area even when the orange (50-tile)
logistic areas don't touch — roboports were specifically designed so
they *"can build each other without interconnecting their logistic
areas."* Practical consequence: a roboport placed up to 110 tiles from
the nearest existing one will still get built/repaired by that
network's construction bots (useful for bootstrapping an outpost
expansion one hop at a time), but its *logistic* network (shared
item/robot inventory) only merges with the existing one if placed
within 50 tiles. Placing them believing 110 tiles keeps one shared
logistic network is a common beginner mistake this distinction
explains.

Verified: 2026-08-07

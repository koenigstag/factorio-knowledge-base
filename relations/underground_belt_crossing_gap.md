# Underground belt crossing gap

Tiles of surface space left completely free of belt graphics between
an underground-belt entrance and exit — usable for perpendicular
crossing traffic (another belt group, a road, a rail).

Formula: `formulas/underground_belt_crossing_gap.py:crossing_gap`
(`max_distance − 1`) — `max_distance` is the maximum entrance-to-exit
tile distance (a `data.raw` field), but the entrance/exit tiles
themselves show belt graphics on the surface and aren't part of the
clear span, hence the `−1`.

Input: `datapacks/dump/vanilla/underground-belt/*.json`'s
`max_distance` (5/7/9/11 across tiers).

## crossing_gap_tiles

| tier | max_distance | crossing gap |
|---|---|---|
| underground-belt | 5 | 4 |
| fast-underground-belt | 7 | 6 |
| express-underground-belt | 9 | 8 |
| turbo-underground-belt | 11 | 10 |

Cross-checked against `factoriocheatsheet.com`'s `undergroundSpacing`
field (community-compiled, not a `data.raw` dump), which independently
lists the same four values (4/6/8/10) — this project's own
`max_distance − 1` derivation, not simply copied from that citation.

**Why this matters**: `layouts/main_bus.md`'s belt-grouping-by-4
convention depends on this exactly, not approximately — a 4-wide belt
group needs a crossing gap of at least 4 tiles, and the basic tier
provides precisely 4, no slack.

Verified: 2026-08-08

# Belt item density: 8 items per tile

Not a `data.raw` field (checked `transport-belt`/`item` directly,
nothing there) — a fixed engine constant, the missing link between a
belt's `speed` (tiles/tick, a `data.raw` field — see
`datapacks/dump/vanilla/UNITS.md`) and its commonly-cited items/sec
throughput.

`items/sec = speed × 60 × items_per_tile`. Confirmed by multiplying it
out for `transport-belt`: `0.03125 × 60 × 8 = 15`, exactly the
commonly-cited "yellow belt = 15/s" figure this project already used
in `relations/smelting_ratios.md` and elsewhere as a cited constant,
not previously derived from `speed` directly — this closes that gap.

Source: `github.com/deniszholob/factorio-cheat-sheet`'s data
(`beltDensity: 8`) — community-compiled, not a `data.raw` dump or an
official wiki citation, but independently confirmed here via the
multiplication above rather than trusted at face value.
Verified: 2026-08-08

# Fluid wagon fill/drain time

Formula: `formulas/fluid_transfer_time.py:fluid_transfer_time` —
`capacity / (pumping_speed_per_sec × pump_count)`.

Inputs:
- capacity=50000: `datapacks/dump/vanilla/fluid-wagon/fluid-wagon.json`
  (normal quality; wiki-confirmed, see `UNITS.md`'s `fluid_box.volume`
  section).
- pumping_speed_per_sec=1200: `datapacks/dump/vanilla/pump/pump.json`'s
  `pumping_speed=20` × 60 (per-tick → per-second conversion sourced in
  `UNITS.md`'s `pump.pumping_speed` section).

## fill_or_drain_seconds_by_pump_count

| pumps | seconds |
|---|---|
| 1 | 41.67 |
| 2 | 20.83 |
| 4 | 10.42 |

Symmetric for both directions — a pump's `pumping_speed` doesn't
distinguish loading from unloading, so filling and draining a wagon
take the same time for the same pump count. A single wagon connects to
up to 2 pipe-adjacent tiles per side in a station (loading from both
ends), which is why 2- and 4-pump station layouts are common in
practice — included here rather than just the 1-pump baseline.

Not covered: higher `quality` wagons hold more (wiki cites up to
125,000 at legendary), which would change `capacity` and thus every
figure here — left out because `quality` isn't extracted as a datapack
in this repo yet.

Verified: 2026-08-07

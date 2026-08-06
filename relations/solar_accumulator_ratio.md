# Solar panel : accumulator ratio

How many solar panels and accumulators are needed per MW of constant
base load, and the ratio between them, for uninterrupted power through
the full day/night cycle.

Formula: `formulas/solar_accumulator_ratio.py:solar_accumulator_ratio`.

Inputs:
- `dawn_ticks=5000, day_ticks=12500, dusk_ticks=5000, night_ticks=2500` — `constraints/day-night-cycle.json` (default map setting, not `data.raw`)
- `solar_panel_output_kw=60` — `datapacks/dump/vanilla/solar-panel/solar-panel.json`'s `production`
- `accumulator_capacity_mj=5` — `datapacks/dump/vanilla/accumulator/accumulator.json`'s `energy_source.buffer_capacity`

## panels_per_mw = 23.81

Sized so solar output *averages* 1 MW over the full cycle: average
daylight factor over 25000 ticks (linear ramp during dawn/dusk) =
0.7, so `(1000/60) / 0.7 = 23.81` panels.

## accumulators_per_mw = 20.0

Numerically integrates net power (solar output − 1 MW load) over a
steady-state cycle; the accumulator has to cover the full swing
between the cycle's cumulative-energy maximum and minimum, not just
the deficit measured from an arbitrary starting instant — see
`examples/solar_accumulator_derivation.md` for why that distinction
mattered here. Swing = 100 MJ per MW baseload ÷ 5 MJ/accumulator = 20.

## accumulators_per_solar_panel = 0.84

`20.0 / 23.81 = 0.84`.

## Verification

Fully self-derived from `datapacks/`/`constraints/` values, not cited
from the community — and it happens to match the community's
independently-published figure exactly: "the optimal ratio is 0.84
(21:25) accumulators per solar panel... 23.8 solar panels per
megawatt" (Factorio Wiki / community consensus, see
`examples/solar_accumulator_derivation.md` for the source and how a
bug in the first attempt at this derivation was caught by that
cross-check, not avoided by it).

Verified: 2026-08-06

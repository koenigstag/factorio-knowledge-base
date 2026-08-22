# Solar panel : accumulator ratio

How many solar panels and accumulators are needed per MW of constant
base load, and the ratio between them, for uninterrupted power through
the full day/night cycle.

Formula: `formulas/solar_accumulator_ratio.py:solar_accumulator_ratio`.

Inputs:
- `dawn_ticks=5000, day_ticks=12500, dusk_ticks=5000, night_ticks=2500` — `mechanics/day-night-cycle.json` (default map setting, not `data.raw`)
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

Fully self-derived from `datapacks/`/`mechanics/` values, not cited
from the community — and it happens to match the community's
independently-published figure exactly: "the optimal ratio is 0.84
(21:25) accumulators per solar panel... 23.8 solar panels per
megawatt" (Factorio Wiki / community consensus, see
`examples/solar_accumulator_derivation.md` for the source and how a
bug in the first attempt at this derivation was caught by that
cross-check, not avoided by it).

Verified: 2026-08-06

## Per-planet extension (2026-08-08) — assumption flagged, not fully confirmed

The ratio above is Nauvis-specific. Other Space Age surfaces have
their own `solar-power` and `day-night-cycle` values
(`glossary/canonical/surface.md`), both of which feed this formula:
`solar-power` scales `solar_panel_output_kw` (`60 × surface_solar_power
/ 100`, confirmed via forum discussion of the
`solar_power_in_space`/`default_value` mechanism — a real engine
multiplier, not this project's assumption), and a shorter
`day-night-cycle` should proportionally shrink the accumulator swing
(less time for a deficit to accumulate before solar recovers).

**Assumption, not verified**: this project doesn't have each planet's
own dawn/day/dusk/night sub-phase breakdown, only the total
`day-night-cycle` tick count. The table below assumes every surface
uses Nauvis's *same relative* dawn:day:dusk:night proportions
(20:50:20:10%), just uniformly time-scaled to that surface's own total
— stated as an assumption because it wasn't found confirmed anywhere,
not because it's known to be true.

| surface | day-night-cycle | solar-power | panels/MW | accumulators/MW | accum:panel |
|---|---|---|---|---|---|
| vulcanus | 5400 | 400 | 5.95 | 4.32 | 0.73 |
| fulgora | 10800 | 20 | 119.05 | 8.64 | 0.07 |
| gleba | 36000 | 50 | 47.62 | 28.80 | 0.61 |
| aquilo | 72000 | 1 | 2380.95 | 57.60 | 0.02 |

**Qualitative cross-check** (Steam community discussion, community-tier
source): *"Vulcanus has solar panels produce 4 times as much as on
Nauvis, Gleba only half, fulgora a fifth and aquillo a tiny 1%,"*
shorter cycles on vulcanus/fulgora and longer on gleba/aquilo, and
*"aquilo becomes very unfeasible for solar"* — all directionally
confirmed by the table above (aquilo's 2381 panels/MW dwarfs every
other surface), but the exact per-planet numbers aren't independently
confirmed elsewhere, and `factoriocheatsheet.com`'s own Vulcanus
citation states a rounder "1 panel : 1 accumulator" practical
building ratio for 240MW, not far off this table's 0.73 but not an
exact match either — plausibly a simplified blueprint ratio rather
than the precise mathematical optimum this formula computes.

# Example: deriving the solar:accumulator ratio from scratch (and catching a bug)

**Question**: how many solar panels and accumulators does 1 MW of
continuous base load need? This one is different from the other
examples — it's not a lookup, it's the actual derivation story,
including a bug that a cross-check caught.

## Step 1 — find the primitives

| what | file | field | value |
|---|---|---|---|
| solar panel output | `datapacks/dump/vanilla/solar-panel/solar-panel.json` | `production` | 60kW |
| accumulator capacity | `datapacks/dump/vanilla/accumulator/accumulator.json` | `energy_source.buffer_capacity` | 5MJ |
| day/night timing | `mechanics/day-night-cycle.json` | `dawn_ticks`/`day_ticks`/`dusk_ticks`/`night_ticks` | 5000/12500/5000/2500 |

Day/night timing isn't in `data.raw` (checked `planet`/`surface`
directly, nothing there) — it's a default map-generation setting,
sourced from the wiki instead.

## Step 2 — first attempt: sizing panels

Solar output ramps linearly during dawn/dusk, so its *average* factor
over the full 25000-tick cycle is `(day + dusk/2 + dawn/2) / total` =
`(12500 + 2500 + 2500) / 25000` = `0.7`. To average 1 MW over the
cycle, panel capacity needs to be `1 / 0.7` MW, i.e.
`(1000/60) / 0.7 ≈ 23.81` panels per MW.

Community-published figure: 23.8 panels/MW. **Matched immediately.**

## Step 3 — first attempt at accumulators: wrong

Naive approach: integrate net power (solar − load) starting from
energy=0 at the start of dawn, track the most negative value reached,
call that the required accumulator capacity. This gave **5.84
accumulators/MW** — the community figure is **20.2**. Off by 3.4×.

The instinct at this point could have been "the dawn/dusk ramp must
not really be linear" and gone looking for a different curve shape.
That would have been the wrong fix.

## Step 4 — finding the actual bug

The bug wasn't the curve, it was measuring from an arbitrary starting
point. "Most negative value starting from 0 at dawn" only equals the
true required capacity if dawn's start happens to be the exact moment
the accumulator is at its fullest in steady state — nothing guaranteed
that. The correct measure is the **swing** — `max(cumulative energy) −
min(cumulative energy)` — over one steady-state cycle (run a few
cycles first so the starting transient doesn't distort it), regardless
of where in the cycle you start counting from.

Fixing just that gave **100 MJ swing per MW**, i.e. **20.0
accumulators/MW** — matching the community figure almost exactly (20.0
vs 20.2), and `20.0 / 23.81 = 0.84`, matching the commonly-cited ratio
exactly.

## Why this example exists

The other examples in this folder show *using* an existing formula or
composing existing `relations/`. This one is here because the
derivation itself went wrong on the first attempt in a way that
looked physically plausible (wrong curve shape) but was actually a
bookkeeping bug (wrong reference point). The cross-check against an
independently-published number is what caught it — matching the
community's number isn't just a nice-to-have confirmation step, it's
how an actual mistake got found here. See `formulas/solar_accumulator_ratio.py`
for the corrected version and `relations/solar_accumulator_ratio.md`
for the final cited numbers.

Verified: 2026-08-06

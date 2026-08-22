# Robot flight range

How far a construction/logistic robot can fly before its battery is
spent, in tiles.

Formula: `formulas/robot_flight_range.py:flight_range_tiles`
(`energy_budget / (energy_per_move + energy_per_tick / speed)`) — the
denominator is `energy_per_tile`, since `1/speed` is the ticks needed
to cross one tile at the robot's flying speed, and `energy_per_tick`
is spent for every tick in flight regardless of distance covered.

Inputs: `datapacks/dump/vanilla/construction-robot/construction-robot.json`,
`datapacks/dump/vanilla/logistic-robot/logistic-robot.json` —
`speed`, `energy_per_move`, `energy_per_tick`, `max_energy`,
`min_to_charge`, `max_to_charge` (see `datapacks/dump/vanilla/UNITS.md`
for what each field means; these two files are a documented `source.json`
exception, not this project's own dump run).

## Two range figures, not one — they answer different questions

| robot | energy/tile (kJ) | full-charge range (tiles) | usable-band range (tiles) |
|---|---|---|---|
| construction-robot | 5.83 | 514.3 | 385.7 |
| logistic-robot | 6.0 | 250.0 | 187.5 |

- **full-charge range** = `max_energy / energy_per_tile` — the
  theoretical maximum, battery at 100% down to empty. Useful as an
  upper bound, but a robot that actually reaches 0% mid-flight has
  gone past `min_to_charge`'s trigger point without finding a
  roboport in range — a real design failure, not a normal case.
- **usable-band range** = `(max_to_charge − min_to_charge) × max_energy
  / energy_per_tile` — the range available in the engine's normal
  operating band (see `mechanics/robot-types.md`/`UNITS.md`'s
  `min_to_charge`/`max_to_charge` hysteresis note): a robot recharges
  up to 95%, then is expected to fly until it drops below 20% and
  heads back. Use this one for layout planning — it's the distance a
  robot can be relied on to cover before needing to find a roboport
  again, not the absolute physical maximum.

Neither figure is round-trip distance — a task that requires flying
out and back (the common case: fetch an item, deliver it) needs
roughly half of either figure as the one-way leg, ignoring pickup/drop
dwell time.

**Unresearched baseline only.** `worker-robots-speed-*` technologies
increase `speed` (and therefore both range figures, since a faster
robot covers more tiles per unit of `energy_per_tick` upkeep) — see
`mechanics/worker-robot-research.md` for the modifier values and the
combination-formula caveat. Not re-derived here yet.

Verified: 2026-08-08

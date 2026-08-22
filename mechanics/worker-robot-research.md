# Research modifiers on robot speed & cargo capacity

Two technology-effect types apply globally to every construction and
logistic robot on a force, on top of the base per-robot stats in
`datapacks/dump/vanilla/construction-robot/`/`logistic-robot/`:

## `worker-robot-speed` — cumulative additive modifier, applied as a multiplier

Raw per-tech values, already in
`datapacks/dump/vanilla/technology/worker-robots-speed-{1..7}.json`
(`effects[0].modifier`):

| tech | modifier | max_level |
|---|---|---|
| worker-robots-speed-1 | 0.35 | 1 |
| worker-robots-speed-2 | 0.4 | 1 |
| worker-robots-speed-3 | 0.45 | 1 |
| worker-robots-speed-4 | 0.55 | 1 |
| worker-robots-speed-5 | 0.65 | 1 |
| worker-robots-speed-6 | 0.65 | 1 |
| worker-robots-speed-7 | 0.65 | infinite (repeatable) |

Per `lua-api.factorio.com/latest/types/WorkerRobotSpeedModifier.html`
(a `SimpleModifier`): *"Modification value, which will be added to the
variable it modifies."* Each researched level adds its `modifier` to
the force's `worker_robots_speed_modifier` accumulator. The wiki
displays a single tech's effect as e.g. *"+65% Worker robot speed"* —
percentage phrasing, which is this project's basis (not an explicitly
quoted formula) for reading the accumulator as applied multiplicatively:

```
effective_speed = base_speed × (1 + worker_robots_speed_modifier)
```

**Confidence caveat**: no single sourced sentence states this exact
combination formula outright — it's inferred from the "additive to an
accumulator" `SimpleModifier` description plus the wiki's percentage
display convention, the same category of gap flagged in
`decisions/0001-inserter-throughput-not-derived.md` for inserter
research bonuses. Treat `relations/robot_flight_range.md`'s figures as
unresearched-baseline only; don't multiply them out by a researched
total without re-verifying this formula.

Researched total after all finite tiers (1–6, before the infinite
tier-7 grind): `0.35+0.4+0.45+0.55+0.65+0.65 = 3.05` → if the formula
above holds, **+305%** speed, i.e. `4.05×` base.

## `worker-robot-storage` — flat additive slots, same for both robot types

| tech | modifier | max_level |
|---|---|---|
| worker-robots-storage-1 | 1 | 1 |
| worker-robots-storage-2 | 1 | 1 |
| worker-robots-storage-3 | 1 | 1 |

Same `SimpleModifier` mechanism, but here the "variable it modifies"
is a slot *count*, not a ratio — no percentage display convention
exists for this one on the wiki, and a flat integer bonus is the only
reading consistent with "inventory slots." All 3 techs researched:
`base_max_payload_size (1) + 1 + 1 + 1 = 4` slots, for **both**
`construction-robot` and `logistic-robot` — one shared technology
line, not per-robot-type (matches both dump files sharing the same
base `max_payload_size=1`). No infinite tier exists for storage, so 4
is the hard vanilla cap.

Source: `datapacks/dump/vanilla/technology/worker-robots-speed-*.json`,
`worker-robots-storage-*.json` (already-dumped, this project's own
2.0.77 run); https://lua-api.factorio.com/latest/types/WorkerRobotSpeedModifier.html,
https://lua-api.factorio.com/latest/types/WorkerRobotStorageModifier.html,
https://wiki.factorio.com/Technology
Verified: 2026-08-08

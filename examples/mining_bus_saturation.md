# Example: how many mining drills fill an N-lane ore bus?

**Question**: I'm running a raw iron-ore bus with N parallel yellow
(basic) transport belt lanes. How many mining drills do I need to
keep all N lanes saturated?

## Step 1 — get the single-belt answer from the cache

`relations/mining_belt_ratios.json` → `mining_time_1.drills_per_belt.electric-mining-drill.transport-belt`
= 30. That's already the N=1 answer — see `relations/mining_belt_ratios.md`
for how 30 was produced (`machines_to_saturate(15, 0.5, 1)`: belt
throughput ÷ one drill's ore/sec).

## Step 2 — scale by bus width

A bus with N parallel lanes of the *same* item needs N times the
single-lane throughput — the lanes don't interact, so there's no
correction term (see `glossary/canonical/main-bus.md`).

```python
drills_per_belt = 30  # relations/mining_belt_ratios.json, mining_time_1
N = 4                  # bus width, your choice
drills_for_bus = drills_per_belt * N
# -> 120
```

## Worked examples for common bus widths (iron/copper/coal/stone/calcite ore, mining_time=1)

| bus width (N) | electric-mining-drill | burner-mining-drill | big-mining-drill |
|---|---|---|---|
| 1 | 30 | 60 | 6 |
| 2 | 60 | 120 | 12 |
| 4 | 120 | 240 | 24 |
| 8 | 240 | 480 | 48 |

Verified by running the ×N scaling in code against
`relations/mining_belt_ratios.json`'s actual values, not by hand.

## This is not a new relation

`drills_per_belt × N` is a pattern applied at read time, not a fact
worth storing for every possible N — nothing here is cached as a new
`relations/` entry. If one specific N came up often enough to be worth
looking up directly (e.g. "the standard N-lane bus" for this project's
own builds), that would earn a `relations/` entry; until then this
walkthrough is the reusable method, not a table to memorize.

# Example: 1 full belt of iron plate, from scratch — how many furnaces + drills?

**Question**: I want one fully saturated yellow (basic) transport belt
of iron plate. How many steel furnaces do I need, and how many
electric mining drills to feed them ore?

This chains two already-cached `relations/` entries instead of
deriving anything new — the point is showing how to compose existing
answers into a bigger one.

## Step 1 — furnaces needed (from `relations/smelting_ratios.json`)

`energy_required_3.2.furnaces_per_belt.steel-furnace.transport-belt`
= **24**. (See `examples/iron_plate_belt_saturation.md` for how this
number itself was produced.)

## Step 2 — drills needed to feed those 24 furnaces (from `relations/mining_furnace_ratios.json`)

`energy_required_3.2.drills_per_furnace.steel-furnace.electric-mining-drill`
= 1.25 drills per furnace.

```python
furnaces = 24
drills_per_furnace = 1.25
drills = furnaces * drills_per_furnace
# -> 30.0
```

## Answer

**24 steel furnaces + 30 electric mining drills** for one fully
saturated iron-plate transport-belt.

## Cross-check: does this match going straight from ore to belt?

`relations/mining_belt_ratios.json` → `mining_time_1.drills_per_belt.electric-mining-drill.transport-belt`
= **30** — the same number, reached by a completely different path (no
furnace step at all, just "drills needed to fill a raw-ore belt at the
same 15 items/sec rate"). This isn't a coincidence: iron-plate's
recipe is 1 ore → 1 plate, so the ore flow rate needed to keep 24
furnaces fed is identical to the plate flow rate they output — both
equal the belt's own rate, 15 items/sec. The two paths through
`relations/` agree because the underlying ratio is 1:1, not because of
anything special about the chaining method itself; a recipe with a
different ore:plate ratio would make the two numbers diverge.

## Cross-check against independent community sources

Searched for existing community-published ratios for the same setup,
after computing the above (not before — the numbers here weren't
picked to match a target). Found matches on both figures
independently: "the ratio is 5 drills to 4 steel furnaces for iron...
24 steel furnaces to smelt all the iron ore of a saturated yellow
belt" (Factorio Forums / community discussion) — 5:4 = 1.25 drills per
furnace, exactly this file's number, and 24 furnaces matches too. The
same source also flags real-world caveats this project's numbers
don't capture yet: an individual ore patch depletes unevenly, so
miner:furnace ratios drift over a patch's lifetime in practice, and
researched mining-productivity technology or speed/productivity
modules change the effective rate — this example (like all of
`relations/`) is the unmodified, un-researched baseline, not a claim
that a real base stays at exactly 24:30 forever.

Verified: 2026-08-06 — both paths computed by reading the actual
`relations/*.json` files and multiplying/comparing in code, not by
hand.

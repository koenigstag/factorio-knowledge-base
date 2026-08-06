# Example: how many furnaces saturate a belt?

**Question**: I'm smelting iron plate in steel furnaces, feeding a
yellow (basic) transport belt. How many furnaces do I need before the
belt is fully saturated?

## Why not just remember "24"?

This project's own CLAUDE.md rule 1 exists because of this exact
number: an early pass in this project's history misremembered it as
"12". The right approach isn't to recall a number, it's to read the
three primitives that determine it and combine them with a formula —
so the answer stays correct even if the recipe, the furnace tier, or
the belt tier changes.

## Step 1 — find the three primitives

| what | file | field | value |
|---|---|---|---|
| recipe time | `datapacks/dump/vanilla/recipe/iron-plate.json` | `energy_required` | 3.2 |
| furnace speed | `datapacks/dump/vanilla/furnace/steel-furnace.json` | `crafting_speed` | 2 |
| belt speed | `datapacks/dump/vanilla/transport-belt/transport-belt.json` | `speed` | 0.03125 (tiles/tick — see `datapacks/dump/vanilla/UNITS.md` for the ×60×4×2 conversion to 15 items/sec) |

## Step 2 — call the formula

```python
from formulas.production_rate import machines_to_saturate

machines_to_saturate(consumer_rate=15, crafting_speed=2, energy_required=3.2)
# -> 24.0
```

`machines_to_saturate` does `consumer_rate / ((crafting_speed / energy_required) * output_amount)`
— belt items/sec, divided by one furnace's plates/sec.

## Step 3 — sanity check against the cache

`relations/smelting_ratios.json` → `energy_required_3.2.furnaces_per_belt.steel-furnace.transport-belt`
= 24. Matches — this question was already answered there; this file
just shows how that number was actually produced, rather than typed
in from memory.

## Applying the same method to a new question

Nothing above is specific to iron plate or steel furnaces. Swap in
`stone-furnace.json`'s `crafting_speed=1` and the answer becomes 48
(already in `relations/smelting_ratios.json` too). Swap in
`fast-transport-belt.json`'s rate (30/sec) instead and it becomes 48
for steel, 96 for stone — also already cached. The method is what
generalizes; asking "is this combination already in `relations/`?"
first is worthwhile, but when it isn't, this is the walkthrough for
producing it correctly instead of guessing.

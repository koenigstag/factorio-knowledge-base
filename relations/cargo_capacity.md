# Cargo capacity: how many of an item fit, by slots vs weight

Formula: `formulas/cargo_capacity.py:cargo_capacity` — `min(slots ×
stack_size, floor(weight_limit / item_weight))`, or just `slots ×
stack_size` when there's no weight limit at all.

Inputs:
- `cargo-wagon.inventory_size=40` — **no weight limit**: checked
  `cargo-wagon`'s full field list directly, its `weight` field is the
  wagon's *own* mass for train physics (braking/acceleration), not a
  cargo weight cap. Wagons are purely slot-limited.
- `rocket-silo-rocket.inventory_size=20`, weight-limited by
  `utility-constants/default.json`'s `rocket_lift_weight=1000000`.
- `iron-plate`: `stack_size=100`, `weight=1000` (computed —
  `relations/item_weight.md`). `iron-ore`: `stack_size=50`,
  `weight=2000` (explicit in `data.raw`).

## wagon (slot-limited only)

| item | capacity |
|---|---|
| iron-plate | 4000 (40 × 100) |
| iron-ore | 2000 (40 × 50) |
| automation-science-pack | 8000 (40 × 200) |
| logistic-science-pack | 8000 (40 × 200) |

Science packs (`datapacks/dump/vanilla/tool/{automation,logistic}-science-pack.json`)
are `tool`-type prototypes, not plain `item` — `stack_size=200,
weight=1000` is an explicit `data.raw` field for both, not computed via
`formulas/item_weight.py`. Same no-weight-limit rule as the rest of
this section: 40 slots × 200 stack = 8000, unconstrained by weight.
Used in `layouts/scalable_main_base.md`'s remote-labs
train-delivery option.

## rocket (min of slot and weight limits)

| item | slot-limited | weight-limited | capacity (binding) |
|---|---|---|---|
| iron-plate | 20×100=2000 | 1,000,000/1000=1000 | **1000** (weight binds) |
| iron-ore | 20×50=1000 | 1,000,000/2000=500 | **500** (weight binds) |

## Verification

**Both rocket figures independently confirmed** against the official
wiki's own "Rocket capacity" infobox field (a Space Age-specific
stat, not something this project derived independently of Wube — but
computing it via `cargo_capacity()` + the `item_weight()` chain and
getting an exact match confirms both formulas at once, not just one):
- `wiki.factorio.com/Iron_plate`: *"Rocket capacity: 1000 (10 stacks)"* — matches.
- `wiki.factorio.com/Iron_ore`: *"Rocket capacity: 500 (10 stacks)"* — matches.

For both items the weight limit binds before the slot limit does (20
slots would allow more by count alone) — illustrates why rockets need
both numbers tracked, not just slot count the way wagons do.

Verified: 2026-08-06

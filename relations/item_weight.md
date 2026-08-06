# Computed item weight (for items without an explicit `weight` field)

Formula: `formulas/item_weight.py:item_weight`, implementing
lua-api.factorio.com/latest/auxiliary/item-weight.html's documented
algorithm exactly (recipe weight → intermediate result via
`ingredient_to_weight_coefficient=0.5` → compared against
`rocket_lift_weight/stack_size` when the recipe doesn't support
productivity, otherwise resolved via the `stack_amount` branch).

## computed_weight_grams.iron-plate = 1000

Inputs:
- `iron-ore.weight=2000` — `datapacks/dump/vanilla/item/iron-ore.json`
- `iron-plate` recipe: 1 iron-ore in, 1 iron-plate out, `allow_productivity=true` — `datapacks/dump/vanilla/recipe/iron-plate.json`
- `iron-plate.stack_size=100` — `datapacks/dump/vanilla/item/iron-plate.json`
- `rocket_lift_weight=1000000`, `default_item_weight=100` — `datapacks/dump/vanilla/utility-constants/default.json`

Computation: `recipe_weight = 2000×1 = 2000`; `product_count=1`;
`intermediate_result = (2000/1)×0.5 = 1000`; recipe supports
productivity so the `simple_result` branch is skipped;
`stack_amount = 1000000/1000/100 = 10` (> 1, so) final weight =
`1000000/floor(10)/100 = 1000`.

## Verification

**Independently confirmed twice**, not just internally consistent:
1. `wiki.factorio.com/Iron_plate`'s own infobox states rocket capacity
   for iron-plate as *"1000 (10 stacks)"* — exactly
   `rocket_lift_weight / computed_weight` = `1,000,000 / 1000 = 1000`.
2. A Factorio Forums thread on weight calculation independently states
   iron-plate's weight as 1000.

This is a case where the *documented formula* (from Wube's own aux
docs) was implemented directly rather than reverse-engineered, and the
result still got cross-checked against independent sources anyway —
same discipline as every other relation in this project, not skipped
just because the source was authoritative.

Verified: 2026-08-06

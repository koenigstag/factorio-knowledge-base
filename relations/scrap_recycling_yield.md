# Scrap recycling yield (Fulgora)

`scrap` is Fulgora's only ground resource (`resources: ["scrap"]`,
`datapacks/dump/vanilla/planet/fulgora.json`) — there are no ore
patches, so `scrap-recycling` (the `recycler` building's recipe) is the
primary source of iron/steel/circuits/etc. on that planet. Each result
is probabilistic (`recipe.results[].probability`), not a guaranteed
output per craft.

Formula: `formulas/probabilistic_yield.py`
(`expected_yield_per_craft`, `crafts_needed_for_expected_output`).

Inputs: `datapacks/dump/vanilla/recipe/scrap-recycling.json` — 12
results, each `amount=1` with its own `probability` (0.2 down to 0.01).

## expected_yield_per_100_scrap

`expected_yield_per_craft(probability, 1) × 100` per item — see
`scrap_recycling_yield.json`. E.g. iron-gear-wheel `0.2 × 100 = 20`,
holmium-ore `0.01 × 100 = 1`.

## avg_scrap_needed_per_item

`crafts_needed_for_expected_output(probability, 1, 1)` — reciprocal of
probability. E.g. iron-gear-wheel `1/0.2 = 5.0` scrap/item on average,
processing-unit `1/0.02 = 50.0`, holmium-ore and low-density-structure
tied for rarest at `1/0.01 = 100.0`.

## Verification

Directly from `data.raw`'s own `probability` field on the
`scrap-recycling` recipe — no community figure needed for the primary
fact. `factoriocheatsheet.com`'s Fulgora `recyclerScrapRatio` lists the
same 12 items with counts that match `probability × 100` exactly on
every single item (iron-gear-wheel 20, solid-fuel 7, concrete 6, ice 5,
steel-plate/battery/stone 4, advanced-circuit/copper-cable 3,
processing-unit 2, low-density-structure/holmium-ore 1) — a clean
independent confirmation that the cheat sheet's figure is just
`probability × 100` re-expressed, not a separately-measured or
different statistic.

`fulgora.data.ts`'s `basicResourceConversionIcons` also lists
`Fluid_HeavyOil → Icons_OffshorePump`, matching
`planet/fulgora.json`'s `offshore_resources: ["heavy-oil"]` exactly —
already covered by existing datapack data, no new fact needed there.
The rest of `basicResourceConversionIcons` (item-to-item icon chains
with no quantities attached) is UI-only routing guidance, not a
sourceable numeric fact, and is skipped here — same treatment as
Vulcanus's `bootstrapItems`.

Verified: 2026-08-08

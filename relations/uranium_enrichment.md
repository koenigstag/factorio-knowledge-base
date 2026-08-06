# Uranium enrichment: Kovarex vs raw processing

Formula: `formulas/recipe_net_effect.py` (`net_effect`,
`expected_crafts_per_unit`).

## kovarex_net_per_cycle = {uranium-235: 1, uranium-238: -3}

`kovarex-enrichment-process` (centrifuge, `energy_required=60`) —
`datapacks/dump/vanilla/recipe/kovarex-enrichment-process.json`
ingredients: 40 uranium-235 + 5 uranium-238 in; results: 41
uranium-235 + 2 uranium-238 out. The 40/2 uranium-235/238 act as a
catalyst (mostly returned); net = `net_effect(40,41)=+1` uranium-235,
`net_effect(5,2)=-3` uranium-238 per cycle.

## uranium_processing_expected_crafts_per_uranium_235 = 142.86

`uranium-processing` (10 uranium-ore in) has probabilistic results:
`uranium-235` at `probability=0.007`, `uranium-238` at `0.993` —
checked directly against `data.raw`, not cited from prose.
`expected_crafts_per_unit(0.007) = 1/0.007 ≈ 142.86` — matches the
commonly-cited community figure "~143 crafts per uranium-235" almost
exactly, and is why Kovarex (deterministic 3 uranium-238 → 1
uranium-235) is preferred over relying on raw processing RNG.

Verified: 2026-08-06

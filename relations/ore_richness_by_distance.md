# Ore patch richness vs. distance from spawn

Formula: `formulas/ore_richness.py` (`ore_richness_multiplier`).

## flat_multiplier=1.0, flat_until_distance_tiles=1600, offset_tiles=1000, scale_tiles=2600

`resource.<name>.autoplace.richness_expression` — identical pattern
checked directly against `data.raw` on `iron-ore`, `copper-ore`,
`uranium-ore`, `stone`, `coal`
(`datapacks/dump/vanilla/resource/*.json`):

```
max((1000 + distance) / 2600, 1) * control:<name>:richness * default-<name>-patches
```

`ore_richness_multiplier(distance) = max((1000 + distance) / 2600, 1)`
is the distance-only term. It's flat at exactly 1.0× for any distance
<= 1600 tiles from the origin, then grows linearly — e.g. 1.385× at
2600 tiles, 2.385× at 5200 tiles. The other two factors
(`control:<name>:richness` — the in-game map-generator richness
slider, default 1 — and `default-<name>-patches`) are separate
multipliers this formula doesn't cover, since they're player/preset
settings, not a fixed constant.

Corrects a vague claim from a YouTube tips video ("every ore patch
further away will be bigger... in form of richness") with the actual
mechanism: richness is completely flat near spawn (not gradually
increasing from tile 0), only starting to climb past 1600 tiles out.

Source: `datapacks/dump/vanilla/resource/iron-ore.json` (and
copper-ore/uranium-ore/stone/coal, same expression shape)
Verified: 2026-08-19

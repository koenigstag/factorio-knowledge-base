# Surface conditions: how recipes/entities get restricted to specific surfaces

A `SurfaceCondition` is a `{property, min, max}` struct (per
`lua-api.factorio.com/latest/types/SurfaceCondition.html`) — `property`
names one of the 5 surface properties
(`glossary/canonical/surface.md`), `min`/`max` bound the allowed range
(defaulting to the widest possible range if omitted). A recipe or
entity can list one or more of these via `RecipePrototype::
surface_conditions` / `EntityPrototype::surface_conditions`; it's only
craftable/buildable on a surface whose property values fall inside
every listed condition.

This is exactly how `space-science-pack` is restricted to space
platforms rather than any planet
(`datapacks/dump/vanilla/recipe/space-science-pack.json`, if pulled —
already recorded in `relations/science_pack_ratios.md`):
`surface_conditions: [{property: "gravity", min: 0, max: 0}]` — only
`space-platform` has `gravity=0` among all 6 surfaces
(`glossary/canonical/surface.md`'s table); every planet has a nonzero
gravity, so none of them qualify.

No `data.raw` field states "this recipe can only run on a
space-platform" directly — the engine evaluates the numeric
`{property, min, max}` condition against whichever surface is asking,
at runtime. Knowing *why* a recipe is surface-restricted means reading
its `surface_conditions` and cross-referencing against
`glossary/canonical/surface.md`'s per-surface property table, not a
single stored "allowed surfaces" list.

## Practical consequence for base-building reasoning

A recipe/entity with no `surface_conditions` at all works anywhere
(the common case — most of the base game). One that does have
conditions is a hard gate, not a preference: there's no way to craft
`space-science-pack` on Vulcanus by adjusting equipment or research,
the same way there's no way to run a smelting recipe without a
furnace — the surface itself has to match.

Source: https://lua-api.factorio.com/latest/types/SurfaceCondition.html
Verified: 2026-08-08

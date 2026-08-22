# Rail geometry

## curve_radius_tiles = 13

Minimum rail turning radius, in tiles. Introduced in Factorio 2.0 —
was 11 tiles pre-2.0 (1.1 and 2.0 rails are not compatible/mixable).
`main` holds only the current version's data per CLAUDE.md's
versioning rule, so this file states the 2.0 value; the 1.1 value is
noted here only as history, not as live data.

Source: https://factorio.com/blog/post/fff-377
Verified: 2026-08-06

## track_width_tiles = 2

Width of a single rail track, in tiles.

Source: https://wiki.factorio.com/Rail
Verified: 2026-08-06

## Elevated rail: same curve radius, not a separate geometry

Elevated rail (2.0/Space Age) uses **the same `curve_radius_tiles=13`
and the same rail shapes as ground rail** — not a distinct, more
restrictive geometry. FFF #378 ("Trains on another level") states this
directly: elevated track *"have exactly the same rail shapes as ground
rails."* Built between ramps, held up by rail-support entities placed
along the way; can be constructed above most ground obstacles but not
above "tall" entities (rocket silo, roboport, big electric pole, per
the same post) — that constraint isn't independently verified against
`data.raw`'s collision-mask fields here (no elevated-rail entity file
pulled into `datapacks/` yet, only the unlock technologies
`technology/elevated-rail.json`/`technology/rail-support-foundations.json`),
so it's recorded as a stated fact from the primary source, not
cross-checked the way `curve_radius_tiles` itself would be if a ground
rail's own data.raw entry existed. `rail-support-foundations` is
specifically for placing supports over deep ocean; regular supports
already work on shallower water once elevated rail itself is
researched.

Source: https://factorio.com/blog/post/fff-378
Verified: 2026-08-09

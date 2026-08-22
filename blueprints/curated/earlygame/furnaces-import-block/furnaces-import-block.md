# Furnaces Import Block

Personal blueprint, not a third-party design — the project owner's own
build.

Blueprint's own label: *"Early-Game Universal Stone Furnace Smelter
(Opposite-side Input and Output)"* — the same label text as
[24x2-stone-furnaces-module.md](../24x2-stone-furnaces-module/24x2-stone-furnaces-module.md), but
this is a distinct, much smaller piece: 47 entities (`transport-belt`
43, `underground-belt` 2, `splitter` 2), **no furnaces or inserters at
all**. This is purely the distribution/junction block that feeds
furnace modules, not a smelter itself — a standalone version of the
same left-side ore/coal intake logic `24x2-stone-furnaces-module`
builds inline, paired with a right side that fans the supply back out
instead of feeding furnaces directly.

**Role (author-confirmed)**: takes a single combined ore+coal supply
in on the left, and distributes it back out to two separate lines on
the right — the outputs of this block are the inputs of a
[4x2-stone-furnaces-w-upgrade-spacing](../4x2-stone-furnaces-w-upgrade-spacing/4x2-stone-furnaces-w-upgrade-spacing.md)
module (or one furnace row's worth of import lanes), one feed going up
and one going down.

## Ports

Structured, author-confirmed data:
[furnaces-import-block.ports.json](furnaces-import-block.ports.json).
Left side (import) is an identical pattern to
[24x2-stone-furnaces-module.md](../24x2-stone-furnaces-module/24x2-stone-furnaces-module.md)'s left
side (coal via `underground-belt`, ore via a shared `splitter`). Right
side (export) is two ore+coal pairs — outer/inner split, same
convention as `4x2-stone-furnaces-w-upgrade-spacing` (outer = ore,
inner = coal, read by distance from the block's own y=0 center) — fed
by a second `splitter` at `(1.5, 0)` that re-splits the combined ore
stream back into the two outbound (up/down) lanes.

One candidate, `(2.5, -0.5)` direction 12/West, matches the same
false-positive pattern already documented for
`24x2-stone-furnaces-module.md`'s `(33.5,-3.5)`: `classify_edge_ports`
flags it (faces into the schema on an export edge), and it even sits
along the coal path's own turn (`(2.5,-1.5)` direction 8/South →
`(2.5,-0.5)` direction 12/West) which makes it look plausible — but
it's author-confirmed as coincidental, not a functional port. Exactly
why this project's rule (`blueprints/README.md`'s "Import/export port
heuristic") is to confirm rather than assume.

## Provenance

- Author: project owner (self-authored).
- Filed under `blueprints/curated/earlygame/` — game-stage folders
  organize the project owner's personal collection; third-party
  entries stay flat at `curated/`'s root.
- Added to the repository: 2026-08-09.

## Validation

Not yet run through `blueprints/validate.py` (factorio-draftsman) as
of this writing — `blueprints/codec.py`'s own decode succeeds cleanly
and reproduces the entity counts/positions used above.

Verified: 2026-08-09

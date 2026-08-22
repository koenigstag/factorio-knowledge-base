# 24×2 Stone Furnace Smelter (opposite-side input/output)

Personal blueprint, not a third-party design — the project owner's own
build, kept here with the same provenance rigor as
[nilaus_100x100_city_block.md](../nilaus_100x100_city_block.md) rather
than as a bare unlabeled `.txt`.

Blueprint's own label: *"Early-Game Universal Stone Furnace Smelter
(Opposite-side Input and Output)"*. 680 entities — dominated by
`transport-belt` (401), `inserter` (96), `long-handed-inserter` (48),
`stone-furnace` (48), `small-lamp` (30), `small-electric-pole` (26): a
tileable stone-furnace smelting block sized for early-game
(pre-electric-furnace) play.

## Ports

Structured, author-confirmed data:
[24x2-stone-furnaces-module.ports.json](24x2-stone-furnaces-module.ports.json)
(bbox + per-tile edge/direction/role/resource). 4 ports total — coal
import (continues into an `underground-belt` one tile in), 2× ore
import (feeding a shared `splitter`), plate export.

`blueprints/codec.py`'s `classify_edge_ports` flags belt/underground-
belt/splitter entities on the bounding-box edge as import/export
*candidates* from direction alone — not sufficient by itself here:
`x_max` has mixed directions at the edge coordinate (one row facing
out — the real export — one facing in, two running parallel to the
edge and not crossing it at all), and the "facing in" row
(`(33.5,-3.5)`, direction 12/West) turned out to be a false positive
once asked about, not a second port — a bare "belt on the edge, facing
inward/outward" check can flag candidates worth confirming, but can't
replace confirming what's actually a port and what's coincidental
geometry.

Not an instance of the ore/coal-outside, result-inside pattern
documented in
[layouts/smelter_module_ports.md](../../../layouts/smelter_module_ports.md)
— that comparison is specifically about two furnace rows flanking a
shared center lane; this module is a single-direction-flow design
(one input side, one output side), a different shape of module the
inside/outside question doesn't apply to.

## Provenance

- Author: project owner (self-authored, not sourced from a third-party
  site).
- Filed under `blueprints/curated/earlygame/` — game-stage folders
  (`earlygame/`/`init-game/`/`midgame/`) are how the project owner's
  personal collection is organized; third-party entries like
  `nilaus_100x100_city_block.*` stay flat at `curated/`'s root instead,
  since they aren't tied to a specific stage.
- Added to the repository: 2026-08-09.

## Validation

`blueprints/validate.py` (factorio-draftsman): **0 errors, 56
warnings** — all warnings are `UnknownKeywordWarning` on `Lamp`/
`ElectricPole` entities for an unrecognized `direction` key, not an
entity/placement problem. `blueprints/codec.py`'s own decode (used to
produce this file's `.json`) succeeds cleanly with no issues at all —
the warnings look like a schema-version gap between this blueprint
(exported from whatever exact 2.0.x patch the project owner is
currently playing) and draftsman's bundled prototype data (pinned to
`2.0.0`), not a defect in the blueprint itself. Running `draftsman
update` did not resolve it.

Verified: 2026-08-09

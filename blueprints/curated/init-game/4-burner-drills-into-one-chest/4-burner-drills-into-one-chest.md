# 4 Burner Drills into One Chest

Personal blueprint, not a third-party design — the project owner's own
build.

No blueprint-internal label set (generic `"Blueprint"`), matching the
style of its siblings in this folder. 5 entities: `burner-mining-drill`
(4), `wooden-chest` (1) — same bootstrap idea as
[4-burner-miners-w-chests.md](../4-burner-miners-w-chests/4-burner-miners-w-chests.md)
(drills dumping straight into a chest, no belts/inserters, fuelled by
hand), but consolidated into a **single shared chest** instead of one
chest per drill.

## Layout

4 drills arranged around one central chest at `(0.5, 0.5)`, each
facing inward so its output lands on that same tile:

| drill | position | direction |
|---|---|---|
| 1 | `(1, 2)` | South-facing side, points North (`0`) |
| 2 | `(-1, 1)` | West side, points East (`4`) |
| 3 | `(0, -1)` | North side, points South (`8`) |
| 4 | `(2, 0)` | East side, points West (`12`) |

Drop position derived from `vector_to_place_result` in
`datapacks/dump/vanilla/mining-drill/burner-mining-drill.json`
(`[-0.35, -1.3]` for an unrotated/North-facing drill), rotated 90°
per direction step and snapped to the nearest half-tile — the same
snap `4-burner-miners-w-chests`'s own drill→chest offset already
exhibits (`(1.5,-0.5)` for its East-facing drills, not the raw
`(1.3,-0.35)`), used here as a cross-check: the rotation formula
reproduces that entry's exact known-good offset before being applied
to the other 3 directions. All 4 rounded offsets converge on the same
tile by construction (drill position = chest position − direction's
drop offset).

Drills are well-separated (~2.24 tiles center-to-center between
adjacent drills, ~1.58 tiles from each drill to the chest) — no
collision-box overlap.

## Ports: none (by design, same as the sibling entries)

No import (hand-fuelled), no export (the chest is a manual-collection
buffer, same rationale as
[4-burner-miners-w-chests.md](../4-burner-miners-w-chests/4-burner-miners-w-chests.md)'s
own "Ports: none" section).

## Provenance

- Author: project owner (self-authored).
- Filed under `blueprints/curated/init-game/` — game-stage folders
  organize the project owner's personal collection.
- Added to the repository: 2026-08-23, after the project owner
  confirmed it in-game.

## Validation

`blueprints/validate.py` (factorio-draftsman): **OK — 0 errors, 0
warnings**. `codec.py`'s own round-trip (encode → decode) reproduces
the source dict exactly.

Verified: 2026-08-23

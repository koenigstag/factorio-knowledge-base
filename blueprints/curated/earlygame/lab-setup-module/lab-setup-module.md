# Lab Setup Module (tier-1 downgrade)

Derived from `midgame/lab-setup-module` in this project — not an
independent third-party fetch. That entry's own source (factorio.school,
"Science Lab Setup" by Roel) explicitly requires `fast-inserter`/
`fast-transport-belt` ("red belts"), making it a midgame design; this
entry re-tiers it down to `transport-belt`/`inserter`/
`small-electric-pole` so it fits
`guides/early_game_progression_checklist.md`'s earlygame stage, per
the project owner's own instruction. Not a blind find-and-replace —
two real constraints surfaced during the downgrade and both are
resolved and verified below rather than left broken.

## What changed, and why it isn't a uniform rename

**Belts and inserters**: `fast-transport-belt` → `transport-belt`,
`fast-inserter` → `inserter` throughout.
`inserter`/`fast-inserter`'s `pickup_position`/`insert_position` are
identical in `datapacks/dump/vanilla/inserter/*.json` (`[0,-1]`/
`[0,1.2]` for both), so this is a pure speed change with zero
positional risk.

**One underground-belt pair needed a real patch, not just a rename
(entities 115/56)**: its entrance-to-exit span was 6 tiles (`y=166.5`
to `y=160.5`), and `underground-belt.max_distance` is **5**
(`fast-underground-belt.max_distance` is **7** —
`datapacks/dump/vanilla/underground-belt/*.json`) — a tier-1 tunnel
can't bridge a 6-tile gap; a straight rename would leave the entrance
and exit disconnected in-game. First pass at this entry kept the pair
at tier-2 as a pragmatic compromise; the project owner caught that
this could be avoided instead: the exit end (not the boundary-facing
entrance at the southern edge, `y=166.5`) had slack to shorten by
exactly the 1 tile needed:

- Removed `long-handed-inserter` entity 57 at `(-68.5, 161.5)` — the
  tile the new exit needs to occupy. (The *other* LHI on this same
  tunnel, entity 74 at `y=162.5`, stays — it still sits on the
  now-4-tile hidden middle span, `162.5` through `165.5`, which is
  exactly `underground-belt`'s `crossing_gap` of 4
  (`max_distance − 1`, see
  `formulas/underground_belt_crossing_gap.py`); only the entrance/exit
  tiles themselves are real placed entities that can't share a tile
  with an inserter, the hidden middle can.)
- Moved entity 56's exit from `y=160.5` to `y=161.5` and downgraded
  both 56 and entrance entity 115 to `underground-belt`. New span:
  exactly 5 tiles — tier-1's maximum, verified via `build_vectors.py`
  (`span: 5.0`, 0 dead-ends).
- Added a new `transport-belt` tile at the vacated old-exit position
  (`-68.5, 160.5`) to keep the lane connected through to the existing
  belt at `y=159.5`.

**Real cost, stated plainly**: entity 57 fed science packs from the
belt/tunnel network into the `lab` at `(-70.5, 161.5)` (a
`long-handed-inserter`, reach confirmed against
`datapacks/dump/vanilla/inserter/long-handed-inserter.json`'s
`pickup_position`/`insert_position`). That lab loses this one feed
inserter — one science-pack type it could otherwise receive from this
direction. Removing it was the project owner's explicit call, not
independently re-derived here; not undone or second-guessed, just
recorded honestly rather than glossed over.

**Power poles retiered and two added, not just renamed**:
`medium-electric-pole` → `small-electric-pole` for all 8 original
poles, **plus 2 new poles** at `(-72.5, 159.5)` and `(-61.5, 159.5)`.
`small-electric-pole`'s `supply_area_distance` is **2.5** tiles vs
medium's **3.5** (`datapacks/dump/vanilla/electric-pole/*.json`) — a
straight rename left 4 `inserter`s (entity_numbers 53, 54, 65, 66,
symmetric pairs at `x=-72.5` and `x=-61.5`) outside every pole's
supply square. The 2 new poles sit on tiles confirmed empty (no
overlap with any other entity) and close the gap for both pairs at
once (`abs(dx)≤0, abs(dy)≤2` from each). `maximum_wire_distance`
also shrinks (small: 7.5, medium: 9), but the existing 8 pole
*positions* still form one connected network at the shorter reach —
checked directly by building the pairwise-distance graph and running
union-find over it (all 10 poles resolve to a single connected
component), not assumed from the rename alone.

## Verification

- **Round-trip**: re-decoding the generated `.txt` reproduces the
  stored `.json` exactly (`encode_blueprint_dict`/
  `decode_blueprint_string`).
- **Power coverage**: every `lab`/`inserter`/`long-handed-inserter`
  falls within some pole's `supply_area_distance` square (checked by
  center-point containment — the same approximation this project's
  `.ports.json` entries and community coverage tools typically use;
  not a full multi-tile-footprint overlap check).
- **Power connectivity**: all 10 poles resolve to one connected
  component under `maximum_wire_distance=7.5` (union-find over the
  pairwise distance graph).
- **Belt/inserter geometry**: `build_vectors.py` reports 29 inserters
  (0 flagged), 21 belt_runs, 5 underground pairs (0 dead-ends) — one
  fewer inserter than `midgame/lab-setup-module`'s 30, the direct
  result of removing entity 57 above; every other vector is unchanged
  in shape/position.
- `blueprints/validate.py` (factorio-draftsman): **OK, 0 errors, 0
  warnings**.
- Zero `fast-*`-tier entities remain anywhere in this blueprint —
  fully tier-1 (`transport-belt`/`underground-belt`/`inserter`/
  `small-electric-pole` plus the tier-agnostic `lab`/
  `long-handed-inserter`), unlike the first pass at this entry.

## Provenance

- Derived 2026-08-23 from `midgame/lab-setup-module` (itself sourced
  from https://www.factorio.school/view/-MJ8OPOMPa66QqJPH2Oo, "Science
  Lab Setup" by Roel) — see that entry for the original's own
  provenance. This entry's tier-1 rework is the project owner's own
  modification of third-party content, not an independent design.

Verified: 2026-08-23

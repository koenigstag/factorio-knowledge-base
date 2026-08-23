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

**One underground-belt pair kept at `fast-underground-belt`
(entities 115/56)**: its entrance-to-exit span is 6 tiles (`y=166.5`
to `y=160.5`), and `underground-belt.max_distance` is **5**
(`fast-underground-belt.max_distance` is **7** —
`datapacks/dump/vanilla/underground-belt/*.json`). A tier-1 tunnel
physically cannot bridge this gap — the entrance and exit wouldn't
connect in-game. The belt goes underground here specifically to free
its surface tiles for two `long-handed-inserter`s sitting directly on
the tunnel's path (see `midgame/lab-setup-module.md`'s layout note);
shortening the span would mean moving those inserters and the belts
they interact with, which risks breaking the design's alignment with
the rest of the tileable block. Kept at tier-2 for this one pair
rather than redesigning around it — the pragmatic fix, not a full
re-layout.

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
- **Belt/inserter geometry unchanged**: `build_vectors.py` produces
  the identical shape as `midgame/lab-setup-module` — 30 inserters (0
  flagged), 21 belt_runs, 5 underground pairs (0 dead-ends) — pole and
  belt-tier changes don't move anything, so this is expected, but
  checked rather than assumed.
- `blueprints/validate.py` (factorio-draftsman): **OK, 0 errors, 0
  warnings**.

## Provenance

- Derived 2026-08-23 from `midgame/lab-setup-module` (itself sourced
  from https://www.factorio.school/view/-MJ8OPOMPa66QqJPH2Oo, "Science
  Lab Setup" by Roel) — see that entry for the original's own
  provenance. This entry's tier-1 rework is the project owner's own
  modification of third-party content, not an independent design.

Verified: 2026-08-23

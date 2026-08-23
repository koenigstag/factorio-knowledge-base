# 4 Burner Drills Chained

Personal blueprint, not a third-party design — the project owner's own
build.

No blueprint-internal label set (generic `"Blueprint"`), matching the
style of its `init-game/` siblings. 4 entities: `burner-mining-drill`
only — no belts, no inserters, no chest. The 4 drills face each other
in a closed cycle on a **coal** patch, each depositing its mined coal
directly into the next drill's fuel inventory.

## Mechanic: mining-drill output can feed another entity directly

A mining drill's output "acts like an inserter" — with no belt in its
output area, it can deposit directly into any compatible entity sitting
at the drop position (a chest, a furnace, or another mining drill's
*fuel* inventory), no inserter needed. Two burner-mining-drills placed
2 tiles apart facing each other on a coal patch refuel each other this
way indefinitely — a documented, well-known pattern (wiki.factorio.com/
Burner_mining_drill: "Two burner mining drills can refuel each other
when placed next to each other on a coal deposit as long as they're
facing each other. Each drill fuels the other and coal gradually
accumulates in their stacks.").

This entry extends that from a mutual **pair** to a one-directional
**4-drill cycle** (A→B→C→D→A), verified rather than assumed:

| drill | position | direction | feeds |
|---|---|---|---|
| 1 | `(0, 0)` | East (`4`) | drill 2 |
| 2 | `(2, 0)` | South (`8`) | drill 3 |
| 3 | `(2, 2)` | West (`12`) | drill 4 |
| 4 | `(0, 2)` | North (`0`) | drill 1 |

A square loop, 2 tiles per side, each drill facing clockwise toward
the next.

## Verification

Each hop checked against `datapacks/dump/vanilla/mining-drill/
burner-mining-drill.json`'s `vector_to_place_result` (rotated per
direction — the same rotation already cross-validated against the
wiki's confirmed 2-drill pair in this project's other init-game
entries) and `collision_box` (`±0.7` tiles):

- Drill 1's drop point `(1.5, -0.5)` falls inside drill 2's footprint
  (`x∈[1.3,2.7]`, `y∈[-0.7,0.7]`) — same for every other hop around
  the cycle (2→3, 3→4, 4→1), all confirmed programmatically, not by
  eye.
- Center-to-center distance between every drill pair is ≥2 tiles
  (adjacent) or ≥2.83 tiles (diagonal) — no collision-box overlap
  (`±0.7` each, so overlap only below ~1.4 tiles).
- `blueprints/validate.py` (factorio-draftsman): **OK, 0 errors, 0
  warnings**.
- `codec.py` round-trip (encode → decode) reproduces the source dict
  exactly.

## Bootstrap and steady state

The loop needs one manual kick to start: hand-fuel any single drill
(same as every other `init-game/` entry here — nothing is belt-fed).
Once running, each drill's own mined coal feeds the next indefinitely,
same self-sustaining principle as the wiki's 2-drill pair, extended
to 4. No export — this is a closed system, mining only as much coal
as it burns for its own fuel; there's no belt or chest for any surplus
to leave through.

## Provenance

- Author: project owner (self-authored). Placement math derived from
  `datapacks/dump/vanilla/mining-drill/burner-mining-drill.json`,
  cross-checked against wiki.factorio.com/Burner_mining_drill's
  documented 2-drill mutual-refuel case.
- Filed under `blueprints/curated/init-game/` — game-stage folders
  organize the project owner's personal collection.
- Added to the repository: 2026-08-23, after the project owner
  confirmed it in-game. Supersedes an earlier draft at this same slug
  that used a belt+inserter chain instead — the project owner asked
  for the no-belt, no-inserter direct-feed version specifically.

## Validation

`blueprints/validate.py` (factorio-draftsman): **OK — 0 errors, 0
warnings**.

Verified: 2026-08-23

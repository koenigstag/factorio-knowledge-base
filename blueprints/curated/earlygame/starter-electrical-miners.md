# Starter Electrical Miners

Personal blueprint, not a third-party design — the project owner's own
build.

No blueprint-internal label set (generic `"Blueprint"`). 24 entities:
`transport-belt` (14), `electric-mining-drill` (8),
`small-electric-pole` (2) — electric mining once power is available.
Not the same design purpose as
[coal-burner-miners-w-burner-inserters.md](coal-burner-miners-w-burner-inserters.md):
that module is a coal-specific, self-fueling "burner miner chain";
this one is a plain generic-ore collector (`electric-mining-drill`
needs no fuel, so no self-fueling loop applies here) — 8 drills in two
rows straddling a single shared central belt lane.

## Ports

Structured, author-confirmed data:
[starter-electrical-miners.ports.json](starter-electrical-miners.ports.json).
Single pass-through lane (import right, export left), generic ore —
same "drills straddling a shared central belt" shape as
[high-density-miners.md](high-density-miners.md), just without the
underground-belt segments that module uses for tighter packing.

## Provenance

- Author: project owner (self-authored).
- Filed under `blueprints/curated/earlygame/` — game-stage folders
  organize the project owner's personal collection; third-party
  entries stay flat at `curated/`'s root.
- Added to the repository: 2026-08-09.

## Validation

`blueprints/validate.py` (factorio-draftsman): **failed to parse**
(`list index out of range`, an internal draftsman error). `codec.py`'s
own decode succeeds cleanly — same suspected schema-version-gap cause
as the other entries here that fail the same way.

Verified: 2026-08-09

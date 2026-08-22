# High-Density Miners

Personal blueprint, not a third-party design — the project owner's own
build.

No blueprint-internal label set (generic `"Blueprint"`). 20 entities:
`electric-mining-drill` (8), `transport-belt` (6), `underground-belt`
(4), `small-electric-pole` (2) — a tightly-packed electric mining tile
using underground belts to route around drill footprints, higher
drill density per tile than a naive layout.

## Ports

Structured, author-confirmed data:
[high-density-miners.ports.json](high-density-miners.ports.json).
Single pass-through lane (import right, export left), generic ore —
same "drills straddling a shared central belt" shape as
[starter-electrical-miners.md](../starter-electrical-miners/starter-electrical-miners.md), packed
tighter via `underground-belt`.

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

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

## Underground-belt pairing

`build_vectors.py`'s `underground` output on the current `.txt` pairs
all four `underground-belt` entities into two valid tunnels
(entity_numbers 9→6 and 15→13, both `direction: 12`/West, input two
tiles east of output), per
[underground-belt-pairing.md](../../../../mechanics/underground-belt-pairing.md)'s
same-tier/matching-direction/nearest-match rule — no dead-end sinks.
Worth recording explicitly because repo history briefly held an
intermediate revision of this blueprint string, since superseded on
`main`, whose four undergrounds were all typed `"input"` with no
`"output"` partner (would have resolved as dead-end sinks); the string
actually on `main` as of 2026-08-22 does not have that problem.

## Provenance

- Author: project owner (self-authored).
- Filed under `blueprints/curated/earlygame/` — game-stage folders
  organize the project owner's personal collection; third-party
  entries stay flat at `curated/`'s root.
- Added to the repository: 2026-08-09.
- Blueprint string updated by the project owner: 2026-08-22 — same 20
  entities by prototype-type count (8 `electric-mining-drill`, 6
  `transport-belt`, 4 `underground-belt`, 2 `small-electric-pole`) and
  same overall footprint size (11×4 tiles), translated to a different
  absolute position (`bbox` moved from `x:[-5.5,5.5] y:[-2.5,1.5]` to
  `x:[-38.5,-27.5] y:[-14.5,-10.5]`) with entity numbering reassigned.
  `high-density-miners.json` regenerated from the new string via
  `codec.py`'s `decode_blueprint_string`; `high-density-miners.ports.json`
  updated to the new absolute tile coordinates (same relative port
  position and directions, just shifted with the rest of the design).

## Validation

`blueprints/validate.py` (factorio-draftsman): **OK, 0 errors, 0
warnings** as of the 2026-08-22 update — a change from the prior
`list index out of range` failure recorded here since 2026-08-09,
which was chalked up to a schema-version gap between draftsman's
bundled prototype data and this repo's `codec.py`-only decode. Not
determined here whether the new string's clean parse means that gap no
longer applies, or this specific layout just doesn't trigger it.

Verified: 2026-08-22

# Coal Burner Miners with Burner Inserters

Personal blueprint, not a third-party design — the project owner's own
build.

No blueprint-internal label set (generic `"Blueprint"`). 20 entities:
`transport-belt` (12), `burner-mining-drill` (4), `burner-inserter`
(4) — the smallest bootstrap mining tile, all-burner (no electricity
required), for the very first patch before power exists.

**Self-fueling "burner miner chain" variant** (author-confirmed): this
specifically mines a **coal** patch, not a generic ore patch. The 4
`burner-inserter`s face their own drill, not the belt — each pulls
coal off the passing lane and feeds it straight back into its drill's
fuel slot, so the module fuels its own miners out of the same coal
it's moving, with no separate fuel supply needed. See
[coal-burner-miners-w-burner-inserters.ports.json](coal-burner-miners-w-burner-inserters.ports.json)
for the single coal lane both ports share.

## Provenance

- Author: project owner (self-authored).
- Filed under `blueprints/curated/earlygame/` — game-stage folders
  organize the project owner's personal collection; third-party
  entries stay flat at `curated/`'s root.
- Added to the repository: 2026-08-09.

## Validation

`blueprints/validate.py` (factorio-draftsman): **OK — 0 errors, 0
warnings**. Clean on both draftsman and `codec.py`.

Verified: 2026-08-09

# Electronic Circuit Module

Third-party blueprint — one entry from Robbie Theron's blueprint book
"Nauvis Start - Factorio 2.1",
https://factorioprints.com/view/-P-hYRfTCEjpttIq9oSr (published
2026-08-23, 0 favorites — brand new at the time of curation). This
entry is its `Basic Green Circuits` blueprint specifically. Replaces
an earlier from-scratch draft at this same slug — the project owner
compared both and preferred this one.

Blueprint's own label: `"Basic Green Circuits"`. 176 entities:
`assembling-machine-1` (20: 12× `copper-cable`, 8× `electronic-circuit`),
`fast-inserter` (45), `transport-belt` (61), `underground-belt` (13),
`splitter` (10), `small-electric-pole` (18), `small-lamp` (8),
`wooden-chest` (1, `bar: 4` — inventory capped to 4 slots, role not
traced further).

## Ratio: matches this project's own derived fact

12 copper-cable assemblers : 8 electronic-circuit assemblers reduces
to exactly **3:2** — the same ratio this project already derived
independently in
[relations/circuit_assembly_ratio.md](../../../../relations/circuit_assembly_ratio.md)
(cross-checked there against wiki.factorio.com/Electronic_circuit and
a second source), just built at double the scale of the earlier draft
this entry replaces.

## Ports

Confirmed by direction/geometry only — this design carries no
constant-combinator/display-panel lane labels anywhere, so resource
identity on each port is explicitly **not** confirmed (see
`blueprints/README.md`'s "Import/export port heuristic" on why a
direction-only candidate isn't treated as ground truth here):
[electronic-circuit-module.ports.json](electronic-circuit-module.ports.json).
4 import candidates and 1 export candidate, all on the `x_max` edge.

## Provenance

- Author: Robbie Theron (factorioprints.com user).
- Source: https://factorioprints.com/view/-P-hYRfTCEjpttIq9oSr — the
  book's own `blueprintString` was fetched directly from
  factorioprints' backing Firebase Realtime Database
  (`facorio-blueprints.firebaseio.com`; the CDN cache used for earlier
  entries in this project returned 404 for this specific book, likely
  not yet cached given how recently it was published), decoded with
  this project's `codec.py`, and re-encoded as a standalone single
  blueprint via `encode_blueprint_dict` — round-trip verified
  (re-decoding the standalone `.txt` reproduces the extracted book
  entry exactly).
- Added to the repository: 2026-08-23, replacing this project's own
  earlier from-scratch draft at this slug, per the project owner's
  explicit preference after comparing both.

## Validation

`blueprints/validate.py` (factorio-draftsman): **OK — 0 errors, 0
warnings**. A genuine Factorio 2.1 export (`version` decodes to
`2.1.11.1`) — unlike this project's pre-2.0 curated entries, draftsman
validates it cleanly.

`build_vectors.py`: 45 inserters (0 flagged/ambiguous), 17 belt_runs,
5 underground-tunnel pairs (0 dead-ends), 10 splitters — all 10
unconfigured balancers (no `input_priority`/`output_priority`/`filter`
set; per
[mechanics/splitter-priority.md](../../../../mechanics/splitter-priority.md)
that's a fully-resolved deterministic 50/50 split, not an ambiguous
junction).

Verified: 2026-08-23

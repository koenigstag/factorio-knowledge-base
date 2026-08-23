# Logistic Science Module

Third-party blueprint — source site/author unknown, pasted directly to
the project owner. Filed under `curated/earlygame/` per the project
owner's own placement instruction. Same author style as
`automation-science-module` in this same folder (unwired
constant-combinator lane labels, pre-2.0 export, matching "N.N/s"
label naming) — likely the same source, though the site itself is
unknown.

Blueprint's own label: `"Logistic Science 1.5/s"`. 147 entities:
`assembling-machine-2` (16), `transport-belt` (73), `inserter` (12),
`long-handed-inserter` (12), `fast-inserter` (10), `underground-belt`
(12), `small-electric-pole` (9), `constant-combinator` (3, unwired —
pure lane labels, see `blueprints/README.md`'s "Constant-combinator
signals as informal lane labels").

## Layout

Unlike `automation-science-module`, this one crafts its own
intermediates: a 4-assembler support column (x=3-4) makes 2x
`iron-gear-wheel`, 1x `inserter`, and 1x `transport-belt` from raw
`iron-plate` + `electronic-circuit` — the actual ingredients of
`logistic-science-pack` (1 inserter + 1 transport-belt, vanilla
assembling-machine-2 recipe). 12 assemblers making
`logistic-science-pack` sit in two columns of 6 (x=-7 and x=0, y=-6/
-3/0/3/6/9), fed by a full-height belt spine at x=-3 (17 tiles, y=-7
to y=10) carrying the crafted inserter/transport-belt items:
long-handed-inserters reach across the gap to the far column (x=-7),
regular inserters feed the near column (x=0).

Ports (tunnel identity confirmed via the unwired constant-combinator
sitting directly below each): [logistic-science-module.ports.json](logistic-science-module.ports.json).

## Pre-2.0 export

This blueprint's `version` field decodes to `0.17.79.0` — a pre-2.0
export, same as `automation-science-module`. Its `direction` values
are on the 8-value pre-2.0 scale (cardinals 2 apart), not the 16-value
2.0+ scale (cardinals 4 apart); see
[mechanics/inserters-directionality.md](../../../../mechanics/inserters-directionality.md)'s
"Pre-2.0 blueprints use a different `direction` scale" section.
`build_vectors.py`'s `normalize_pre_2_0_directions()` rescales this
automatically before computing geometry — the `.vectors.json` sibling
here is already in modern-scale cardinals, zero ambiguity across all
34 inserters and 6 underground-tunnel pairs.

## Provenance

- Author: unknown (third-party, no site/URL available).
- Added to the repository: 2026-08-23, at the project owner's request
  to curate this blueprint (and `automation-science-module`, its
  sibling in this same folder) as reference material — no specific
  claim elsewhere in this project cited it as evidence yet.

## Validation

`blueprints/validate.py` (factorio-draftsman): **failed to parse** —
`No converter exists for version (0, 17, 79, 0)`. Same cause as
`automation-science-module`: draftsman's bundled converters don't
cover pre-2.0 blueprint versions at all, independently confirming this
is a genuine pre-2.0 export. `codec.py`'s own decode succeeds cleanly.

Verified: 2026-08-23

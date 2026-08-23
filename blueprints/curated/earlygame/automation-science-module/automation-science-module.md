# Automation Science Module

Third-party blueprint, one entry from a blueprint *book*: "Tileable
Science Production 1.0-2.0 - Early to Mid Game (Vanilla)" by
Christoffer Ramqvist,
https://factorioprints.com/view/-KnQ865j-qQ21WoUPbd3 (created
2017-06-24, 4007 favorites as of 2026-08-23). The book holds 9
blueprints, one per vanilla science pack (some with an alternate
"-input" ingredient variant); this entry is its `Automation Science
1.5/s (Gear-input)` blueprint specifically — confirmed byte-identical
to this project's own stored copy by decoding the book's blueprint
string and comparing entity-by-entity. Filed under `curated/earlygame/`
per the project owner's own placement instruction.

Blueprint's own label: `"Automation Science 1.5/s (Gear-input)"`. 84
entities: `assembling-machine-2` (10, each `recipe:
"automation-science-pack"`), `underground-belt` (18), `transport-belt`
(17), `inserter` (10), `long-handed-inserter` (20),
`small-electric-pole` (6), `constant-combinator` (3, unwired — pure
lane labels, see `blueprints/README.md`'s "Constant-combinator signals
as informal lane labels").

## Layout

Two columns of 5 assemblers (x=-4 and x=4, y=-5/-2/1/4/7), each making
`automation-science-pack` directly from `copper-plate` +
`iron-gear-wheel` — no sub-crafting, both ingredients arrive already
refined. Three continuous vertical belt/underground lanes run the
module's full height at x=-1 (pack output, collected north), x=0
(copper-plate) and x=1 (iron-gear-wheel), each tapped from both sides
by inserters into the adjacent AM column: 30 inserters total, 10 per
lane, matching the 10 assemblers exactly (one copper-in + one gear-in +
one pack-out per AM).

Ports (tunnel identity confirmed via the unwired constant-combinator
sitting directly below each): [automation-science-module.ports.json](automation-science-module.ports.json).

## Pre-2.0 export

This blueprint's `version` field decodes to `0.17.79.0` — a pre-2.0
export. Its `direction` values are on the 8-value pre-2.0 scale
(cardinals 2 apart), not the 16-value 2.0+ scale (cardinals 4 apart);
see [mechanics/inserters-directionality.md](../../../../mechanics/inserters-directionality.md)'s
"Pre-2.0 blueprints use a different `direction` scale" section.
`build_vectors.py`'s `normalize_pre_2_0_directions()` rescales this
automatically before computing geometry — the `.vectors.json` sibling
here is already in modern-scale cardinals, zero ambiguity across all
30 inserters and 9 underground-tunnel pairs.

## Provenance

- Author: Christoffer Ramqvist (factorioprints.com user, display name
  resolved via the site's public Firebase Realtime Database at
  `/users/<userId>/displayName`).
- Source: https://factorioprints.com/view/-KnQ865j-qQ21WoUPbd3 — the
  book's own `blueprintString` was fetched from factorioprints' public
  CDN cache (`factorio-blueprint-firebase-cdn.pages.dev`, the same
  backing store the site's own front end reads from) and decoded with
  this project's `codec.py`; this specific sub-blueprint matched this
  project's already-curated copy exactly.
- Added to the repository: 2026-08-23, at the project owner's request
  to curate this blueprint (and `logistic-science-module`, its sibling
  in this same folder) as reference material — no specific claim
  elsewhere in this project cited it as evidence yet.

## Validation

`blueprints/validate.py` (factorio-draftsman): **failed to parse** —
`No converter exists for version (0, 17, 79, 0)`. This is a different,
more specific failure than the schema-version-gap draftsman errors
recorded on other entries in this folder (e.g.
`iron-gear-tileable.md`'s `list index out of range`): draftsman's
bundled converters simply don't cover pre-2.0 blueprint versions at
all, confirming independently (from a source unrelated to this
project's own rescaling work) that this blueprint really is a pre-2.0
export. `codec.py`'s own decode succeeds cleanly.

Verified: 2026-08-23

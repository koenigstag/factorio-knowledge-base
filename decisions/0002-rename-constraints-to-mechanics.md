# 0002 — Rename `constraints/` to `mechanics/`, broaden it to textual rules

## Status
Accepted

## Context

`constraints/` held only numeric facts with no `data.raw`
representation (rail curve radius, chunk size, max inserters per
wagon), each split into a bare `<topic>.json` + a sourced `<topic>.md`
per Hard rule 1.

Not every fact useful for layout/design reasoning is numeric. Example:
an inserter can only pick up from and drop to the tile directly behind
and in front of it along its facing direction — it cannot reach a
perpendicular tile. This has no `data.raw` field to point to (it's
emergent engine behavior, not a stored value) and no single number to
extract, so it didn't fit the `<topic>.json` + `<topic>.md` numeric
pairing `constraints/` was built around. The rest of the repo's
structure had no home for it either: `glossary/` is for term
definitions, not behavior rules; `layouts/` is for spatial composition
patterns, not per-entity mechanics; `decisions/` is for architectural
decisions about the repo itself, not game facts.

The underlying purpose of this category of knowledge — a harness
against an LLM inventing plausible-sounding but wrong game mechanics —
applies equally to "rail curve radius is 13 tiles" and "an inserter
can't reach sideways." Both are facts the model is prone to
confabulate if left to recall them from training data instead of
citing them.

## Alternatives considered

**Leave `constraints/` numeric-only, add a new sibling folder (e.g.
`rules/`) for textual behavioral facts.**
- Con: splits one coherent category (engine facts absent from
  `data.raw`) across two folders by an accident of format (is there a
  number or not), not by meaning. An LLM checking "is this mechanic
  already documented" would need to check two places.

**Keep the name `constraints/`, just start allowing prose-only
entries in it.**
- Con: "constraint" reads as inherently numeric/limiting (a ceiling or
  bound), which fits rail radius or max-inserters-per-wagon but reads
  oddly for a descriptive behavior rule like inserter directionality.
  `mechanics/` covers both senses without strain.

## Decision

Renamed `constraints/` to `mechanics/` (`git mv`, all in-repo path
references updated). Hard rule 2's test is unchanged — still "if it's
in `data.raw`, it's `datapacks/`, never `mechanics/`" — but its scope
is now explicitly both numeric limits and qualitative/behavioral
rules. Hard rule 1 now allows a `<topic>.md`-only entry (no paired
`.json`) when there's no bare value to extract, still requiring
`Source:`/`Verified:`, with the official wiki (wiki.factorio.com)
confirmed as a valid source alongside Friday Facts and the game's own
data dump.

First entry under the broadened scope: `mechanics/inserters-directionality.md`.

## Consequences

- Existing `mechanics/*.json` + `*.md` pairs (day-night-cycle, fluids,
  rails, trains, world) are unaffected in content, only in directory
  path.
- `mechanics/inserters-throughput.md` was already prose-only before
  this rename (numbers live in prose tables, not a bare `.json`) — it
  turns out to already match the pattern this decision formalizes,
  just not for a behavioral-rule reason (throughput is scenario-
  dependent, not because it's non-numeric).
- Future qualitative rules (e.g. belt side-loading limits, other
  entity orientation rules) have an explicit home and sourcing bar
  instead of drifting into `glossary/` or prose scattered across
  `layouts/`.

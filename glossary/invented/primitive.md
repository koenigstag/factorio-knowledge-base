# primitive

A raw, verified quantitative fact about a game entity — a recipe,
crafting speed, belt/inserter throughput. Stored in `datapacks/`.
Verification lives in one of two places depending on the sub-source
(see rule 5 in CLAUDE.md): a shared `source.json` manifest for a whole
`datapacks/dump/<mod-set>/` tree extracted mechanically from one
`factorio --dump-data` run, or a per-entry `source_url` +
`verified_date` for datapacks sourced some other way (manually
transcribed, community-curated).

Difference from a `constraint`: a primitive is what gets plugged into
a formula as a parameter; a constraint is a hard limit a formula
cannot exceed (e.g. the physical cap on inserters per wagon).

Defined during initial architecture discussion; provenance convention
updated once `datapacks/dump/` was built.

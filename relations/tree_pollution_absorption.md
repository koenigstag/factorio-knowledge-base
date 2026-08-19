# Tree pollution absorption

Not a formula output — a categorical survey across `data.raw.tree.*`,
grouped by distinct value found rather than derived from other
primitives (see `CLAUDE.md` rule 3: belongs here since it combines
many sourced datapack entries into one summary, not a bare guessed
number).

## common_tree_absorption_per_second = 0.001 (25/32 tree types)

`tree.*.emissions_per_second.pollution = -0.001` — negative emission
is absorption. Covers all Nauvis green trees (`tree-01`..`tree-09` and
variants) plus Gleba flora (`boompuff`, `cuttlepop`, `funneltrunk`,
etc.) and `water-cane`. Representative file:
`datapacks/dump/vanilla/tree/tree-01.json`.

## dry_dead_tree_absorption_per_second = 0.0001 (5/32 tree types)

10x weaker — dead/dry desert trees (`dead-dry-hairy-tree`,
`dead-grey-trunk`, `dead-tree-desert`, `dry-hairy-tree`, `dry-tree`).
Representative file: `datapacks/dump/vanilla/tree/dry-tree.json`.

## lichen_tree_absorption_per_second = 0 (2/32 tree types)

No `emissions_per_second` field at all — `ashland-lichen-tree` and
`ashland-lichen-tree-flaming` (Vulcanus flora) don't absorb pollution.
Representative file:
`datapacks/dump/vanilla/tree/ashland-lichen-tree.json`.

All 32 `tree.*` entries in the dump were checked for this survey; only
one representative file per distinct value is saved under
`datapacks/`, not all 32.

Source: `datapacks/dump/vanilla/tree/*.json`
Verified: 2026-08-19

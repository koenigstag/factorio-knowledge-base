# Inserter throughput (cited, not derived)

See `decisions/0001-inserter-throughput-not-derived.md` for why this
is cited from the wiki instead of computed from
`datapacks/dump/vanilla/inserter/*.json`'s `rotation_speed`/
`extension_speed` the way `formulas/production_rate.py` handles
recipes.

## Chest-to-chest cycles/sec (clean baseline case)

The wiki states chest-to-chest transfer moves a full hand's worth of
items in a single tick, so nearly all cycle time is the swing there
and back — the cleanest, least setup-dependent throughput number the
wiki publishes. Approximate cycles/sec by tier (Normal quality):
burner ≈0.79, regular ≈0.86, long-handed ≈1.25, fast/bulk/stack ≈2.5.

**Not independently re-verified to exact precision** — pulled via a
summarized fetch of wiki.factorio.com/Inserters#Inserter_Throughput.
Treat as directionally correct, not exact — before using a precise
figure for anything sensitive, re-pull the raw table directly.

## items/sec = cycles/sec × items per cycle (`formulas/inserter_throughput.py`)

For 4 of the 6 tiers, `items_per_cycle=1` unambiguously (checked
against `datapacks/dump/vanilla/inserter/*.json`: `inserter`,
`burner-inserter`, `long-handed-inserter`, `fast-inserter` have no
`stack_size_bonus`/multi-item hand), so `items/sec` equals the cited
`cycles/sec` directly:

| tier | items/sec (base, unresearched) |
|---|---|
| burner-inserter | 0.79 |
| inserter | 0.86 |
| long-handed-inserter | 1.25 |
| fast-inserter | 2.5 |
| bulk-inserter | 5.0 |
| stack-inserter | 15.0 |

`bulk-inserter`/`stack-inserter` resolved via
`wiki.factorio.com/Inserter_capacity_bonus_(research)`'s stated
**base** (unresearched) grab sizes: regular inserters=1,
`bulk-inserter`=2, `stack-inserter`=6 item(s) per cycle. This also
explains the `data.raw` field directly: `bulk-inserter` has no
`stack_size_bonus` because its base of 2 is an implicit engine
default for any `bulk: true` inserter, not a stored per-tier value;
`stack-inserter`'s `stack_size_bonus=4` is *added to* that same
implicit base of 2, giving `2+4=6` — exactly the wiki's cited base.
`bulk-inserter items/sec = inserter_throughput(2.5, items_per_cycle=2) = 5.0`;
`stack-inserter items/sec = inserter_throughput(2.5, items_per_cycle=6) = 15.0`.

## Researched grab size (resolved)

Previously flagged as open in this file and in
`decisions/0001-inserter-throughput-not-derived.md`: research
(`inserter-capacity-bonus-1..7` in `datapacks/dump/vanilla/technology/`)
adds two *separate* effects, and the wiki's dedicated page states
outright that "the specific formula for combining these effects is
not described." The combination rule was found in
`factoriocheatsheet.com`'s source
(https://github.com/deniszholob/factorio-cheat-sheet — community-
maintained, wiki-derived, not a `data.raw` dump) and independently
**cross-checked against this project's own already-held datapack**:
summing `bulk-inserter-capacity-bonus`/`inserter-stack-size-bonus`
modifiers directly from `datapacks/dump/vanilla/technology/
inserter-capacity-bonus-{1..7}.json` reproduces the cheat sheet's
table exactly at every tech level, confirming the rule rather than
just trusting the citation:

```
formulas/inserter_capacity_bonus.py
nonstack_items_per_cycle = 1 + stack_size_bonus_total   (inserter/burner/long-handed/fast)
bulk_items_per_cycle     = 2 + capacity_bonus_total     (bulk-inserter)
stack_items_per_cycle    = 6 + capacity_bonus_total     (stack-inserter, same accumulator as bulk - it's also bulk:true)
```

`capacity_bonus_total` sums to **10** across all 7 techs (+1 at techs
1-4, +2 at techs 5-7); `stack_size_bonus_total` sums to **2** (+1 at
tech 2, +1 at tech 7 only — the other 5 techs don't touch it). Full
per-tech breakdown:

| tech | nonstack items/cycle | bulk items/cycle | stack items/cycle |
|---|---|---|---|
| 0 (base) | 1 | 2 | 6 |
| 1 | 1 | 3 | 7 |
| 2 | 2 | 4 | 8 |
| 3 | 2 | 5 | 9 |
| 4 | 2 | 6 | 10 |
| 5 | 2 | 8 | 12 |
| 6 | 2 | 10 | 14 |
| 7 (max, all finite — no infinite tier for this research) | 3 | 12 | 16 |

## items/sec at full research

Same `cycles/sec` as the unresearched table (capacity research doesn't
change `rotation_speed`/`extension_speed`, only grab size), × the
tech-7 `items_per_cycle` above, via `formulas/inserter_throughput.py`:

| tier | cycles/sec | items_per_cycle (max research) | items/sec (max research) |
|---|---|---|---|
| burner-inserter | 0.79 | 3 | 2.37 |
| inserter | 0.86 | 3 | 2.58 |
| long-handed-inserter | 1.25 | 3 | 3.75 |
| fast-inserter | 2.5 | 3 | 7.5 |
| bulk-inserter | 2.5 | 12 | 30.0 |
| stack-inserter | 2.5 | 16 | 40.0 |

Chest-to-chest case only — same caveat as the unresearched table
below about chest-to-belt not being a fixed number.

## Chest-to-belt / belt-to-chest — not a single number

The wiki explicitly states throughput here depends on belt
saturation, lane position, and timing between the inserter and items
already moving on the belt — it is not reducible to one fixed
items/sec per tier the way chest-to-chest is. Range observed in
research: roughly 0.78–3.27 items/sec for basic inserters up to
~17/sec for a fully upgraded stack inserter on a turbo belt, but these
are scenario-dependent, not fixed constants.

Sources: https://wiki.factorio.com/Inserters#Inserter_Throughput
(cycles/sec, unresearched grab sizes);
https://github.com/deniszholob/factorio-cheat-sheet (researched grab-size
combination rule, cross-checked against this project's own
`datapacks/dump/vanilla/technology/inserter-capacity-bonus-*.json` —
see "Researched grab size" above)
Verified: 2026-08-06 (base), 2026-08-08 (researched section)

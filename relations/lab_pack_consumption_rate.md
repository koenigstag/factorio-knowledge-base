# Lab pack-consumption rate: how many labs a given pack supply needs

Closes the "Labs consumption rate per specific technology — needs
technology.json data not yet pulled" item from
`layouts/scalable_main_base.md`'s open questions — that file sizes
*pack production* (2.0/s red, 2.0/s green at its reference cell) but
never checked how many labs are actually needed to *consume* that
supply at full rate, since the tech-cost side of the data hadn't been
pulled yet.

## Formula

Reused as-is, no new formula needed —
`formulas/production_rate.py`'s `production_rate(crafting_speed,
energy_required, output_amount)` already has the right shape: one
research "cycle" is structurally a craft with `energy_required =
technology.unit.time` and `output_amount = 1`. `lab.json`'s
`researching_speed=1` (unmodified, no speed modules/tech bonuses) is
the `crafting_speed` input:

```
cycles_per_sec_per_lab = production_rate(lab.researching_speed, tech.unit.time, 1)
                        = lab.researching_speed / tech.unit.time
```

Each cycle consumes exactly 1 of each pack type in
`technology.unit.ingredients` — verified directly against every
`datapacks/dump/vanilla/technology/*.json` file with a `unit` field:
**no technology has a per-cycle ingredient amount other than 1** (a
full sweep found zero exceptions), so `cycles_per_sec_per_lab` *is*
the per-pack-type consumption rate, no extra multiplication needed.
`machines_to_saturate(consumer_rate, crafting_speed, energy_required,
output_amount)` then gives labs needed for a target pack-supply rate,
reusing `ingredient_amount=1` in the `output_amount` slot (the
function is agnostic to whether that slot means "produced" or
"consumed" — same ratio math either way, same reuse pattern already
used throughout `layouts/scalable_chem_base.md` for ingredient-side
rates).

## Computed: the technologies `scalable_main_base.md` actually needs

Three technologies cover this project's own red/green science stage
end to end — the first tech unlocking each pack recipe, plus the first
tech that consumes *both*:

| technology | `unit.time` | ingredients/cycle | packs/sec/lab | labs to saturate 2.0/sec |
|---|---|---|---|---|
| `automation` (unlocks AM1) | 10s | 1× automation-science-pack | 0.1 | 20 |
| `logistic-science-pack` (unlocks green pack recipe) | 5s | 1× automation-science-pack | 0.2 | 10 |
| `automation-2` (unlocks AM2) | 15s | 1× automation + 1× logistic-science-pack | 0.0667 (each type) | 30 |

`automation-2` is the representative case for
`scalable_main_base.md`'s reference cell, since that cell is
explicitly sized for **equal** 2.0/s red and green output — and
`automation-2` consumes both pack types 1:1 per cycle, so one lab
count (**30**) saturates both simultaneously. `automation` and
`logistic-science-pack` (single-pack-type techs, researched earlier)
need fewer labs (20 and 10) for the same 2.0/s supply, simply because
their `unit.time` is shorter.

## Lab count isn't fixed — it grows with tech tier

A full sweep of every `datapacks/dump/vanilla/technology/*.json` with
a `unit` field found `unit.time` values of **5, 10, 15, 30, 35, 45,
60, 120** seconds across the tech tree (e.g. `logistic-science-pack`=5s,
`automation`=10s, `advanced-circuit`=15s, `advanced-combinators`=30s,
`braking-force-5`=35s, `atomic-bomb`=45s,
`advanced-asteroid-processing`=60s, `research-productivity`=120s —
one example per observed value, not an exhaustive list). Since
`cycles_per_sec_per_lab = 1/unit.time`, a fixed lab count that fully
saturates an early cheap tech (`unit.time=5` or `10`) will
increasingly *under*-consume as research reaches costlier techs, even
though the pack *production* rate (2.0/s + 2.0/s) never changes — the
labs field has to grow over the game the same way the main base's
production modules do, not just once at the start. Not modeled here:
exactly how much labs count should grow by end-game tier, or whether
overbuilding labs upfront (accepting idle capacity early) is better
than scaling them incrementally — a design choice, not a derived fact.

Source: `datapacks/dump/vanilla/lab/lab.json` (`researching_speed=1`),
`datapacks/dump/vanilla/technology/{automation,logistic-science-pack,automation-2,advanced-circuit,advanced-combinators,braking-force-5,atomic-bomb,advanced-asteroid-processing,research-productivity}.json`
(`unit.time`, `unit.ingredients` — pulled directly, not cited from a
third party).
Verified: 2026-08-09

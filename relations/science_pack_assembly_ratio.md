# Science pack assembler ratio (equal output rate)

How many assembling machines of each science pack type are needed so
all six packs are produced at the same rate as each other, assuming
every pack is made on the same assembling-machine tier. (Space Age
packs — space, metallurgic, agricultural, electromagnetic, cryogenic,
promethium — are made in different buildings entirely, not covered
here.)

Formula: `formulas/production_rate.py:production_rate` /
`machines_to_saturate`.

## Primitives

None of these six recipes are yet in `datapacks/dump/vanilla/recipe/`
(only 6 unrelated recipes are extracted there so far); recorded in
`datapacks/wiki/recipe/` per CLAUDE.md rule 5, same gap as
`relations/circuit_assembly_ratio.md`.

| Recipe | `energy_required` | `results` amount | Source |
|---|---|---|---|
| `automation-science-pack` | 5 | 1 | `datapacks/wiki/recipe/automation-science-pack.json` |
| `logistic-science-pack` | 6 | 1 | `datapacks/wiki/recipe/logistic-science-pack.json` |
| `military-science-pack` | 10 | 2 | `datapacks/wiki/recipe/military-science-pack.json` |
| `chemical-science-pack` | 24 | 2 | `datapacks/wiki/recipe/chemical-science-pack.json` |
| `production-science-pack` | 21 | 3 | `datapacks/wiki/recipe/production-science-pack.json` |
| `utility-science-pack` | 21 | 3 | `datapacks/wiki/recipe/utility-science-pack.json` |

## Derivation

For a target output rate equal to the assembling machine's own
`crafting_speed` (`cs`) — an arbitrary but tier-independent reference
point — `machines_to_saturate(cs, cs, energy_required, output_amount)`
= `energy_required / output_amount`, since `cs` cancels out of both
sides:

| Pack | `energy_required / output_amount` | Machines |
|---|---|---|
| automation | 5/1 | 5 |
| logistic | 6/1 | 6 |
| military | 10/2 | 5 |
| chemical | 24/2 | 12 |
| production | 21/3 | 7 |
| utility | 21/3 | 7 |

Because `cs` cancels, this **5:6:5:12:7:7** ratio holds at any
assembling-machine tier — the same shape of tier-independence as
`relations/circuit_assembly_ratio.md`, and for the same reason (the
ratio only depends on `energy_required`/`output_amount` per recipe, not
on the shared multiplier).

## Cross-check

Independently confirmed by two sources:
- wiki.factorio.com/Science_pack states this exact ratio directly: *"The ratio needed to keep production in sync is 5:6:5:12:7:7"* — and separately confirms it's tier-independent: *"The above list assumes that all science packs are being produced by the same tier of assembling machine."*
- The Xterminator short cross-checked in `relations/steam_power_ratio.md` states the same six numbers in the same order (red/green/military/blue/purple/yellow = 5/6/5/12/7/7) for "one science per second base rate" — matches exactly.

Verified: 2026-08-22

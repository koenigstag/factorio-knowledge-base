# Basic oil processing ratio

`basic-oil-processing` (crude-oil 100 → petroleum-gas 45, no water, no
byproducts) is the single-input/single-output oil recipe — unlike
`advanced-oil-processing`, it needs no cracking chain (see
`relations/oil_cracking_ratio.md`), so it fits the same
production-rate/saturation shape as `relations/smelting_ratios.*`,
except the "consumer" is a fluid connection, not a belt.

Formula: `formulas/production_rate.py` (`production_rate`,
`machines_to_saturate`).

## petroleum_gas_per_refinery_per_sec = 9

`production_rate(crafting_speed=1, energy_required=5, output_amount=45)`
= (1/5)×45 = 9. Inputs: `oil-refinery.crafting_speed=1` —
`datapacks/dump/vanilla/assembling-machine/oil-refinery.json`;
`basic-oil-processing.energy_required=5`, output amount 45 — recipe
data (not yet an individual datapack file, checked directly against
`data.raw`).

## refineries_to_saturate_one_fluid_connection

- `at_theoretical_cap_6000_per_sec` = 666.67 — `machines_to_saturate(6000, 1, 5, 45)`. 6000 = `datapacks/dump/vanilla/utility-constants/default.json`'s `max_fluid_flow` (100/tick × 60).
- `at_practical_cap_4200_per_sec` = 466.67 — same formula, consumer_rate = `mechanics/fluids.json`'s `max_flow_per_connection_sec_practical`.

Unlike the smelting ratios, these aren't whole numbers (6000/9 and
4200/9 don't divide evenly) — no rounding applied, this is the exact
formula output.

**Why this number matters**: a single refinery outputs far less
petroleum-gas (9/s) than one fluid connection can carry (4200-6000/s)
— it would take 450-650+ refineries feeding the *same* connection
point before the fluid system itself becomes the bottleneck. In
practice this means, for `basic-oil-processing` specifically, pipe/
connection throughput is essentially never the limiting factor —
refinery count and crude-oil supply are the real constraints long
before fluid flow caps out.

Verified: 2026-08-06

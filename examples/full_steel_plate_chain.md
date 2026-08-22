# Example: 1 full belt of steel plate, from scratch — how many furnaces + iron lanes + drills?

**Question**: I want one fully saturated yellow (basic) transport belt
of steel plate. How many steel furnaces do I need for the steel stage,
how many for the iron stage feeding it, how many iron-plate belt lanes
does that take, and how many electric mining drills? Same style as
`examples/full_iron_plate_chain.md`, one stage further upstream.

Chains four already-cached `relations/` entries — nothing new derived
here, just composed.

## Step 1 — steel-plate furnaces needed (from `relations/smelting_ratios.json`)

`energy_required_16.furnaces_per_belt.steel-furnace.transport-belt`
= **120**.

## Step 2 — iron-plate furnaces needed to feed them (from `relations/iron_to_steel_furnace_ratio.json`)

Same tier on both stages (steel-furnace throughout) →
`iron_furnaces_per_steel_furnace = 1.0`.

```python
steel_furnaces = 120
iron_furnaces = steel_furnaces * 1.0
# -> 120
```

## Step 3 — iron-plate belt lanes needed (from `relations/bus_lane_ratios.json`)

`lanes_per_output_lane.steel-plate.iron-plate = 5.0` — for 1 lane
(15 items/sec) of steel-plate, feed **5 lanes** of iron-plate, same
belt tier.

```python
steel_plate_lanes = 1
iron_plate_lanes = steel_plate_lanes * 5.0
# -> 5.0
```

## Step 4 — drills needed to feed the 120 iron-plate furnaces (from `relations/mining_furnace_ratios.json`)

`energy_required_3.2_ingredient_amount_1.drills_per_furnace.steel-furnace.electric-mining-drill`
= 1.25 drills per furnace.

```python
drills = iron_furnaces * 1.25
# -> 150.0
```

## Answer

**120 steel-plate-smelting steel furnaces + 120 iron-plate-smelting
steel furnaces + 5 iron-plate belt lanes between them + 150 electric
mining drills**, for one fully saturated yellow steel-plate belt.

## Cross-check: do steps 2 and 3 agree?

Two independent paths to "how much iron-plate is needed," and they
should land on the same flow rate:

- **Furnace-count path** (step 2): 120 iron-furnaces ×
  `production_rate(crafting_speed=2, energy_required=3.2, amount=1)`
  = 120 × 0.625 = **75 items/sec** produced.
- **Belt-lane path** (step 3): 120 steel-furnaces ×
  `production_rate(2, 16, 5)` (5 = iron-plate ingredient amount) =
  120 × 0.625 = **75 items/sec** consumed.

Both **75 items/sec**, which is exactly 5 × 15 (5 lanes' worth of a
yellow belt) — confirming `iron_to_steel_furnace_ratio.md`'s 1:1
furnace ratio and `bus_lane_ratios.md`'s 5.0 lane ratio are the same
underlying fact read two different ways, not two independent claims
that happen to agree.

Verified: 2026-08-08 — all four numbers computed by reading the actual
`relations/*.json` files and multiplying in code, not by hand.

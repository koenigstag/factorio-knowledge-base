def production_rate(crafting_speed: float, energy_required: float, output_amount: float = 1,
                     productivity_multiplier: float = 1) -> float:
    """Items produced per second by one machine at 100% uptime.

    crafting_speed: machine's effective crafting_speed, including any
        speed-module/beacon bonuses already folded in (e.g.
        machine.crafting_speed for an unmodified machine)
    energy_required: recipe's base time in seconds at crafting_speed=1
        (recipe.energy_required - see datapacks/dump/vanilla/UNITS.md)
    output_amount: items produced per craft (recipe.results[].amount)
    productivity_multiplier: 1 + sum of productivity-module effect.productivity
        bonuses applied to the machine (module.json's effect.productivity;
        only affects output, never ingredient consumption - see
        recipe_ingredient_ratio.py for consumption-side rates)
    """
    return (crafting_speed / energy_required) * output_amount * productivity_multiplier


def machines_to_saturate(consumer_rate: float, crafting_speed: float, energy_required: float, output_amount: float = 1) -> float:
    """Machines needed to fully saturate a consumer running at consumer_rate items/sec
    (e.g. a belt's throughput_items_per_second_total)."""
    return consumer_rate / production_rate(crafting_speed, energy_required, output_amount)

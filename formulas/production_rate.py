def production_rate(crafting_speed: float, energy_required: float, output_amount: float = 1) -> float:
    """Items produced per second by one machine at 100% uptime.

    crafting_speed: machine's crafting_speed (e.g. furnace.crafting_speed)
    energy_required: recipe's base time in seconds at crafting_speed=1
        (recipe.energy_required - see datapacks/dump/vanilla/UNITS.md)
    output_amount: items produced per craft (recipe.results[].amount)
    """
    return (crafting_speed / energy_required) * output_amount


def machines_to_saturate(consumer_rate: float, crafting_speed: float, energy_required: float, output_amount: float = 1) -> float:
    """Machines needed to fully saturate a consumer running at consumer_rate items/sec
    (e.g. a belt's throughput_items_per_second_total)."""
    return consumer_rate / production_rate(crafting_speed, energy_required, output_amount)

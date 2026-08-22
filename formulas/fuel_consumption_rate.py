def fuel_consumption_rate(energy_usage: float, fuel_value: float, effectivity: float = 1) -> float:
    """Fuel items consumed per second by a burner machine at 100% uptime
    (continuously crafting, never idle).

    energy_usage: machine's power draw while working, in watts
        (furnace.energy_usage, parsed per datapacks/dump/vanilla/UNITS.md's
        "90kW" -> 90000 convention).
    fuel_value: energy released by one unit of fuel, in joules
        (item.fuel_value, e.g. coal's "4MJ" -> 4000000).
    effectivity: burner.energy_source.effectivity - fraction of fuel energy
        actually usable (1 = no loss). Actual energy drawn from fuel per
        second is energy_usage / effectivity; dividing that by fuel_value
        gives items/sec.
    """
    return (energy_usage / effectivity) / fuel_value

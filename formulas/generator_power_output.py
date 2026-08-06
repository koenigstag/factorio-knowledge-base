def generator_power_output(fluid_usage_per_tick: float, effectivity: float, heat_capacity_kj: float,
                            temperature: float, ambient_temperature: float = 15, ticks_per_sec: int = 60) -> float:
    """Electrical power output (kW) of a `generator`-type entity (steam-engine,
    steam-turbine) fed fluid at a fixed input temperature.

    fluid_usage_per_tick: generator.fluid_usage_per_tick
    effectivity: generator.effectivity
    heat_capacity_kj: the consumed fluid's fluid.heat_capacity, in kJ per unit per degree
        (see datapacks/dump/vanilla/fluid/*.json — e.g. steam=0.2)
    temperature: input fluid temperature in deg C (generator.maximum_temperature at full supply)
    ambient_temperature: the fluid's fluid.default_temperature — the zero-point
        the engine measures energy from, not merely a reference constant
    """
    return fluid_usage_per_tick * ticks_per_sec * effectivity * heat_capacity_kj * (temperature - ambient_temperature)

def boiler_fluid_consumption(energy_consumption_kw: float, heat_capacity_kj: float,
                              target_temperature: float, ambient_temperature: float = 15) -> float:
    """Fluid consumed per second (fluid units/sec) by a `boiler`-type entity
    heating its input fluid from ambient_temperature to target_temperature.

    Inverse of formulas/generator_power_output.py's core relation, solved
    for flow rate instead of power.

    energy_consumption_kw: boiler.energy_consumption (fuel-side power draw), in kW
    heat_capacity_kj: the input fluid's fluid.heat_capacity, kJ per unit per degree
    target_temperature: boiler.target_temperature, deg C
    ambient_temperature: the fluid's fluid.default_temperature — the zero-point
        the boiler heats from
    """
    return energy_consumption_kw / (heat_capacity_kj * (target_temperature - ambient_temperature))

def heat_exchangers_per_reactor(reactor_consumption_kw: float, exchanger_consumption_kw: float) -> float:
    """Heat exchangers needed to fully consume one reactor's heat output."""
    return reactor_consumption_kw / exchanger_consumption_kw


def heat_exchanger_steam_output_per_sec(energy_consumption_kw: float, heat_capacity_kj: float,
                                         target_temperature: float, ambient_temperature: float = 15) -> float:
    """Steam produced per second by a heat exchanger running at full energy_consumption.

    energy_consumption_kw: boiler(heat-exchanger).energy_consumption
    heat_capacity_kj: output fluid's fluid.heat_capacity (steam=0.2)
    target_temperature: boiler(heat-exchanger).target_temperature
    """
    return energy_consumption_kw / (heat_capacity_kj * (target_temperature - ambient_temperature))


def turbines_per_heat_exchanger(exchanger_steam_output_per_sec: float, turbine_fluid_usage_per_sec: float) -> float:
    """Steam turbines needed to fully consume one heat exchanger's steam output."""
    return exchanger_steam_output_per_sec / turbine_fluid_usage_per_sec


def heat_pipe_paths_needed(total_heat_kw: float, max_transfer_kw: float) -> float:
    """Minimum parallel heat-pipe routes needed to carry total_heat_kw out of a
    reactor block without the pipe itself throttling below max_transfer_kw
    (heat-pipe.heat_buffer.max_transfer) per path."""
    return total_heat_kw / max_transfer_kw

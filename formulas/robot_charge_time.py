def charge_time_seconds(energy_to_add: float, charging_power: float) -> float:
    """Seconds to add energy_to_add (kJ) at charging_power (kW).

    kJ / kW = kJ / (kJ/s) = seconds directly, no conversion factor
    needed as long as both inputs share the same kilo-prefix scale
    (true for Factorio's "kJ"/"kW" prototype string fields).

    charging_power: roboport.charging_energy - see
        datapacks/dump/vanilla/roboport/roboport.json. This is the max
        power delivered to *each* charging station, not a pool split
        across every robot at that roboport (confirmed via
        lua-api.factorio.com/latest/prototypes/RoboportPrototype.html).
    """
    return energy_to_add / charging_power

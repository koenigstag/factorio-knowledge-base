def fluid_transfer_time(capacity: float, pumping_speed_per_sec: float, pump_count: int = 1) -> float:
    """Seconds to fully fill or drain a fluid container.

    capacity: container's fluid_box.volume-scale capacity (e.g.
        fluid-wagon.capacity, storage-tank capacity).
    pumping_speed_per_sec: one pump's rate, already converted to
        per-second (pump.pumping_speed × 60 — see
        datapacks/dump/vanilla/UNITS.md).
    pump_count: number of pumps operating in parallel.
    """
    return capacity / (pumping_speed_per_sec * pump_count)

def crossing_gap(max_distance: float) -> float:
    """Tiles of surface space left free for crossing traffic between an
    underground belt pair.

    max_distance: underground-belt.max_distance (the maximum
        entrance-to-exit tile distance, a data.raw field - see
        datapacks/dump/vanilla/underground-belt/*.json). The entrance
        and exit tiles themselves show belt graphics and aren't part
        of the clear span, hence -1.
    """
    return max_distance - 1

def max_connection_distance(radius: float) -> float:
    """Maximum center-to-center distance (tiles) between two roboports
    for their square coverage areas to still touch at the border.

    radius: half the square's side (roboport.logistics_radius or
        roboport.construction_radius, see
        datapacks/dump/vanilla/roboport/roboport.json).
    """
    return 2 * radius

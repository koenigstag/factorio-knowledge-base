import math


def min_roboports_for_area(width_tiles: float, height_tiles: float, radius: float) -> int:
    """Minimum roboports needed for gap-free coverage of a width x height area.

    Places roboports on a grid spaced exactly 2 x radius apart (see
    formulas/roboport_network_range.py:max_connection_distance) so
    their square coverage areas tile edge-to-edge with no gaps and no
    overlap. radius: roboport.logistics_radius or
    roboport.construction_radius, see
    datapacks/dump/vanilla/roboport/roboport.json.
    """
    side = 2 * radius
    return math.ceil(width_tiles / side) * math.ceil(height_tiles / side)

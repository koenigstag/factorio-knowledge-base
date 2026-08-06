def beacon_effect_multiplier(n_beacons, distribution_effectivity, profile):
    """Combined module-effect multiplier from n_beacons beacons affecting one machine.

    distribution_effectivity: beacon.distribution_effectivity (datapacks/dump/vanilla/beacon/beacon.json).
    profile: beacon.profile - a lookup table, profile[n-1] is the
        per-beacon transmission fraction for n beacons affecting the
        same machine (index n-1, 0-based). Equal to 1/sqrt(n) to
        rounding precision, but read from the table rather than
        computed, since that's what the game actually uses (and the
        table is capped at 100 entries).

    Returns the total multiplier applied to one module's effect,
    summed across all n beacons (per_beacon_fraction * distribution_effectivity * n_beacons).
    """
    if n_beacons < 1:
        return 0.0
    index = min(n_beacons, len(profile)) - 1
    per_beacon_fraction = profile[index]
    return distribution_effectivity * per_beacon_fraction * n_beacons

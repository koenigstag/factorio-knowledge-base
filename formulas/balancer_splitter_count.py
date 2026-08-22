import math


def power_of_two_balancer_splitter_count(n: int) -> int:
    """Splitters needed for an n -> n throughput-unlimited belt balancer.

    n: number of input belts = number of output belts, must be a power
        of two. Formula from Benes network topology, per
        wiki.factorio.com/Balancer_mechanics: n x log2(n) - n/2.
    """
    if n < 1 or (n & (n - 1)) != 0:
        raise ValueError("n must be a power of two")
    return int(n * math.log2(n) - n / 2)

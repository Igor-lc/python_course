import physics
from physics import CONSTANTS, G


def height(t):
    # if t > 10:
        # physics.G = 10
    return (physics.G * (t ** 2)) / 2


"""
def height(t):
    G = physics.G
    if t > 10:
        G = 10
    return (G * (t ** 2)) / 2
    """

"""def height(t):
    CONSTANTS["G"] = 10
    return (CONSTANTS["G"] * (t ** 2)) / 2


def height_2(t):
    G = 10
    return (G * (t ** 2)) / 2"""

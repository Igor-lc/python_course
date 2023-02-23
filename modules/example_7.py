"""
import physics
print(dir(physics))

from physics import __file__
print(__file__)
"""

import physics_2
G = 10
print(G, physics_2.height(10), physics_2.physics.G)

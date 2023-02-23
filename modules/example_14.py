from rel import *
from physics import *

print(ek(100, 10))


import physics
import rel

print(physics.ek(100, 10), rel.ek(100, 10))


from physics import ek
from rel import ek as rel_ek

print(ek(100, 10), rel_ek(100, 10))

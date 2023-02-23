from math import sqrt

C = 299792458


def ek(m, v):
    return (m * (C ** 2)) / sqrt(1 - (v ** 2) / (C ** 2)) - (m * (C ** 2))

print(ek(100, 10))

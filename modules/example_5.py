"""
from physics import ep, G
from physics_2 import height
m = 80

print("Ускорение:", G)
print("Потенциальная энергия:", ep(m, 2))
print("Расстояние:", height(20))
print("Ускорение (еще раз):", G)
print("Потенциальная энергия (еще раз)", ep(m, 2))

print()
print()
    """

# Избегаем прямого изменения объектов в других модулях.
from physics import ep, G
from physics_2 import height
m = 80

print("Ускорение:", G)
print("Потенциальная энергия:", ep(m, 2))
print("Расстояние:", height(20))
print("Ускорение (еще раз):", G)
print("Потенциальная энергия (еще раз)", ep(m, 2))

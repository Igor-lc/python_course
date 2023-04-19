import random

def is_cross(lst1, lst2):
    x1_1, y1_1, x2_1, y2_1 = lst1
    x1_2, y1_2, x2_2, y2_2 = lst2

    for i in range(999999999):
        # формируем прямоугольник
        x = random.uniform(x1_1, x2_1)
        y = random.uniform(y1_1, y2_1)
        # print(x, y)
        # Проверяем, находится ли точка внутри второго прямоугольника
        if x1_2 <= x <= x2_2 and y1_2 >= y >= y2_2:
            return True
    print()
    for i in range(999999999):
        x = random.uniform(x1_2, x2_2)
        y = random.uniform(y1_2, y2_2)
        # print(x, y)
        # Проверяем, находится ли точка внутри первого прямоугольника
        if x1_1 <= x <= x2_1 and y1_1 >= y >= y2_1:
            return True

    return False

result = is_cross([1, 1, 2, 2], [2, 1, 3, 2])
print(result)

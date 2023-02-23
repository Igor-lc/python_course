cities = [
    # Клд  Мск   СПб,  Каз   Врж,  Тверь
    [0,    1337, 1103, 2192, 1855, 1255],  # Калининград
    [1337, 0,    712,  825,  522,  192],   # Москва
    [1103, 712,  0,    1526, 1337, 531],   # Санкт-Петербург
    [2192, 825,  1526, 0,    1080, 1006],  # Казань
    [1855, 522,  1337, 1080, 0,    815],   # Воронеж
    [1255, 192,  531,  1006, 815,  0]      # Тверь
]


def calc_distance(path):
    dist = 0
    for i in range(len(path)):
        if i != len(path) - 1:
            dist += cities[path[i]][path[i + 1]]

    return dist


def calc_distance2(path):
    distance = 0
    prev_city = path[0]
    for city in path[1:]:
        distance += cities[prev_city][city]
        prev_city = city

    return distance

print(calc_distance([3, 0, 5]))
print(calc_distance2([3, 0, 5]))

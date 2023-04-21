import math


def near_shops(start, radius, shops):
    my_shops = []
    for shop in shops:
        x, y = shop[1]
        distance = math.sqrt((start[0] - x) ** 2 + (start[1] - y) ** 2)
        if distance <= radius:
            my_shops.append((shop[0], distance))
        my_shops = sorted(my_shops, key=lambda shop: shop[1])

    return my_shops


# ver 2
def near_shops2(coordinates, radius, shops):
    x, y = coordinates
    x0 = [i[1][0] for i in shops]
    y0 = [i[1][1] for i in shops]
    shops_near = []

    for idx, j in enumerate(zip(x0, y0)):
        dist = ((x - j[0]) ** 2 + (y - j[1]) ** 2)
        if dist <= radius ** 2:
            shops_near.append((shops[idx][0], dist ** 0.5))

    shops_sort = []
    i = shops_near.__len__()
    m, mi = shops_near[0], 0
    while i > 0:
        for j, digit in enumerate(shops_near):
            if m[1] > digit[1]:
                m, mi = digit, j
        shops_sort.append(m)
        shops_near[mi] = ('', float('inf'))
        m = ('', float('inf'))
        i -= 1

    return shops_sort


shops = [
    ("Магазин 1", (1, 1)),
    ("Магазин 2", (-1, 0)),
    ("Магазин 3", (2, -1)),
    ("Магазин 4", (2, 4)),
    ("Магазин 5", (2, 0)),
]
my_shops = near_shops2((2, 3), 3, shops)
print(my_shops)
my_shops = near_shops2((2, 3), 3, shops)
print(my_shops)

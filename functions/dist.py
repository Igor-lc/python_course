import math

def distance(point1, point2):
    if len(point1) == 2:
        x1, y1 = point1
        x2, y2 = point2
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance
    if len(point1) == 3:
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        distance = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2) ** 0.5
        return distance


print(distance((-1, 3), (6, 2)))  # 7.0710678118654755
print(distance((-1, 3, 3), (6, 2, -2)))  # 8.660254037844387

class Point:
    def __init__(self):
        self._x = None
        self._y = None

    def set(self, x, y):
        self._x = float(x)
        self._y = float(y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


    x = property(get_x, set)
    y = property(get_y, set)


point = Point("12.34", 15.67)
print(type(point.x))  # <class 'float'>
print(type(point.y))  # <class 'float'>
print()

point = Point(12.34, "15.46")
print(type(point.x))  # <class 'float'>
print(type(point.y))  # <class 'float'>
print()

point.x = "4"
point.y = 5.4
print(point.x)  # 4.0
print(point.y)  # 5.4
print()

point.set(7, "99.8")
print(point.x)  # 7.0
print(point.y)  # 99.8

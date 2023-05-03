class Point:
    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)
    def set_x(self, x):
        self._x = float(x)
    def get_x(self):
        return self._x
    def set_y(self, y):
        self.y = float(y)
    def get_y(self):
        return self._y
    x = property(get_x, set_x)
    y = property(get_y, set_y)

'''class Point:
    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = float(value)

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = float(value)

    def set(self, x, y):
        self.x = x
        self.y = y

    x = property(get_x, set_x)
    y = property(get_y, set_y)'''

point = Point(12.34, "15.46")
print(type(point.x))
print(type(point.y))
point.x = "4"
point.y = 5.4
print(point.x)
print(point.y)
point.set(7, "99.8")
print(point.x)
print(type(point.y))

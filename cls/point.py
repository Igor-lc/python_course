class Point:
    def __init__(self, x, y):
        self._x = self._y = 0
        self.set(x, y)

    def set_x(self, x):
        self._x = float(x)

    def get_x(self):
        return self._x

    def set_y(self, y):
        self._y = float(y)

    def get_y(self):
        return self._y

    def set(self, x, y):
        self.set_x(x)
        self.set_y(y)

    x = property(get_x, set_x)
    y = property(get_y, set_y)

point = Point(12.34, "15.46")
print(type(point.y))
point.x = "4"
point.y = 5.4
print(point.x)
print(point.y)
point.set(7, "99.8")
print(point.x)
print(point.y)


'''320. DOT
Difficulty: 2 out of 10
Create a Point class that will model the behavior of a point in a rectangular coordinate system on a plane.

The class constructor must take two arguments x and y, which are responsible for the coordinates of the point.

Change of coordinates of a point has to happen by means of properties (property). Each coordinate must be a separate point property.

We also need to add the set(x, y) method, which can be used to change both coordinates.

Coordinate values must be stored as floats, however the class must accept coordinates represented as both numbers (int, float) and strings (str) that can be converted to float.'''

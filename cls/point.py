class Point:
    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, value):
        self._x = float(value)

    def set_y(self, value):
        self._y = float(value)

    def set(self, v1, v2):
        self._x = float(v1)
        self._y = float(v2)

    x = property(get_x, set_x)
    y = property(get_y, set_y)


'''320. DOT
Difficulty: 2 out of 10
Create a Point class that will model the behavior of a point in a rectangular coordinate system on a plane.

The class constructor must take two arguments x and y, which are responsible for the coordinates of the point.

Change of coordinates of a point has to happen by means of properties (property). Each coordinate must be a separate point property.

We also need to add the set(x, y) method, which can be used to change both coordinates.

Coordinate values must be stored as floats, however the class must accept coordinates represented as both numbers (int, float) and strings (str) that can be converted to float.'''

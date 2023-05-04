# ver 2
import math


class Rectangle_2:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def _get_sides(self):
        side_1 = math.sqrt((self.x2 - self.x1) ** 2)
        side_2 = math.sqrt((self.y2 - self.y1) ** 2)
        return side_1, side_2

    def get_length(self):
        side_1, side_2 = self._get_sides()
        if side_1 > side_2:
            return side_1
        return side_2

    def get_width(self):
        side_1, side_2 = self._get_sides()
        if side_1 > side_2:
            return side_2
        return side_1

    def get_area(self):
        return self.get_length() * self.get_width()

    def get_perimeter(self):
        return self.get_length() * 2 + self.get_width() * 2

    def is_square(self):
        return self.get_length() == self.get_width()

# ver 1
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_length(self):
        return self.x2 - self.x1

    def get_width(self):
        return self.y1 - self.y2

    def get_area(self):
        return self.get_length() * self.get_width()

    def get_perimeter(self):
        return self.get_length() * 2 + self.get_width() * 2

    def is_square(self):
        return self.get_length() == self.get_width()

rectangle = Rectangle_2(-3, 2, 4, -2)
print(rectangle.get_length())
print(rectangle.get_width())
print(rectangle.get_area())
print(rectangle.get_perimeter())
print(rectangle.is_square())

rectangle = Rectangle(-3, 2, 4, -2)
print(rectangle.get_length())
print(rectangle.get_width())
print(rectangle.get_area())
print(rectangle.get_perimeter())
print(rectangle.is_square())

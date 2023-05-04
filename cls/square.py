import math


class Rectangle:
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


class Square(Rectangle):
    def __init__(self, x, y, l):
        super().__init__(x, y, x + l, y + l)


square = Square(1, 4, 2)
print(square.get_length())
print(square.get_width())
print(square.get_area())
print(square.get_perimeter())
print(square.is_square())


'''SQUARE
Difficulty: 4 out of 10
Create a Square class that will model a square in a rectangular coordinate system on a plane. Since a square is a special case of a rectangle, Square must inherit from Rectangle from problem 133.

The Square constructor must take 3 arguments: x, y, l:

x, y are the coordinates of the upper left corner of the square;
l is the length of the side of the square.
The parent Rectangle class must also be in the solution file.

Usage example:
square = Square(1, 4, 2)
print(square.get_length())
2
print(square.get_width())
2
print(square.get_area())
4
print(square.get_perimeter())
8
print(square.is_square())
True'''

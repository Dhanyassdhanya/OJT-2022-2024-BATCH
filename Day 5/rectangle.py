# Create a function called display_info() that takes an object of either Rectangle or Square class and 
# displays information about the shape (area, perimeter, diagonal if applicable).

import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def diagonal(self):
        return math.sqrt(2) * self.length

def display_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
    if isinstance(shape, Square):
        print(f"Diagonal: {shape.diagonal()}")

# Example usage:
rect = Rectangle(5, 3)
sq = Square(4)

print("Rectangle Info:")
display_info(rect)

print("\nSquare Info:")
display_info(sq)

import math

# Base class
class Shape:
    def area(self):
        print("Area method not defined for generic shape.")

# Subclass: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Subclass: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Subclass: Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Example usage
shapes = [
    Circle(radius=5),
    Rectangle(length=4, width=6),
    Triangle(base=3, height=7)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")
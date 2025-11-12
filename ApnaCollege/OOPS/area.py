class Circle:

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius **2

    def parameter(self):
        return 2 * 3.14 * self.radius


c1 = Circle(21)
# c1.area()
# c1.parameter()

print("Area of circle is", c1.area())
print("Parameter of circle is", c1.parameter())


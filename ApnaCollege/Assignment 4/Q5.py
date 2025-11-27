# inheritance


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)  # Call Vehicle's constructor
        self.seats = seats


# Subclass: Bike
class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)  # Call Vehicle's constructor
        self.engine_cc = engine_cc


c1 = Car("Ford", 2015, 4)
b1 = Bike("Yamaha", 2020, "200cc")


print(f"Car: {c1.brand} {c1.model}, Seats: {c1.seats}")
print(f"Bike: {b1.brand} {b1.model}, Engine: {b1.engine_cc}")

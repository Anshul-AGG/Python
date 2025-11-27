# Multiple Inheritance

class Herbivore:
    def eat_plants(self, plants):
        self.plants = plants
        print(f"Eats plants: {self.plants}")


class Carnivore:
    def eat_meat(self, animal):
        self.animal = animal
        print(f"Eats meat: {self.animal}")


class Omnivore:
    def eat_both(self, plants, animal):
        self.plants = plants
        self.animal = animal
        print(f"Eats both: {self.plants} and {self.animal}")


class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        self.name = name
        print(f"{self.name} the Bear is created.")
        
b = Bear("Baloo")
b.eat_plants("berries")
b.eat_meat("fish")
b.eat_both("roots", "deer")

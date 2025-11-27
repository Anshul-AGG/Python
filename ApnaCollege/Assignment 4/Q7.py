class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(f"Name: {self.name}")

        if self.age is not None:
            print(f"Age: {self.age}")

        if self.address is not None:
            print(f"Address: {self.address}")

        print("------------------------")


p1 = Person("Aarav")  # name only
p2 = Person("Neha", 25)  # name + age
p3 = Person("Ravi", 30, "Delhi")  # name + age + address

p1.display()
p2.display()
p3.display()

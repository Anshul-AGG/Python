class Store:

    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Store.count += 1

    def info(self):
        print(f"Price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total products in store = {cls.count}")

    @staticmethod
    def cal_disc(price, discount):
        print(f"Discounted price = {price - (price * discount/100)}")


p1 = Store("Phone",10000)
p2 = Store("Laptop", 50000)

p1.get_count()
p1.cal_disc(p1.price, 12)
p2.cal_disc(p2.price, 15)

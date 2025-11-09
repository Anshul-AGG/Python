class Account:
    def __init__(self, balance, accNo):
        self.balance = balance
        self.account_No = accNo
        print("Your current balance is :", self.balance)

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "is debited.")
        print("Your current balance is", self.printBalance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "is credited.")
        print("Your current balance is",  self.printBalance())

    def printBalance(self):
        return self.balance
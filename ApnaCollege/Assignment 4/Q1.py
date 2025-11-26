class BankAccount:

    def __init__(self, account_number, owner_name, balance=0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self):
        if self.account_number and self.owner_name:
            try:
                deposit_amount = float(input("Enter the amount to deposit: "))
                if deposit_amount > 0:
                    self.balance += deposit_amount
                    print(
                        f"{deposit_amount}, is successfully deposited to your Bank Account."
                    )
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def withdraw(self):
        if self.account_number and self.owner_name:
            try:
                withdraw_amount = float(
                    input("Enter the amount you want to withdraw: ")
                )
                #if withdraw_amount > 0 and withdraw_amount <= self.balance:
                if 0 < withdraw_amount <= self.balance:
                    self.balance -= withdraw_amount
                    print(f"{withdraw_amount}, withdrawal successfull.")
                else:
                    print("Not enough funds.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    def checkBalance(self):
        print(f"{self.balance}, is your current balance.")

account = BankAccount("12", "Anshul", 5000)

account.deposit()
account.withdraw()
account.checkBalance()

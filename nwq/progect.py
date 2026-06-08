class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance is {self.balance}.")


# 🔹 Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest of {interest} added. New balance is {self.balance}.")


# 🔹 Checking Account
class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, transaction_fee):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def deduct_transaction_fee(self):
        self.balance -= self.transaction_fee
        print(
            f"Transaction fee of {self.transaction_fee} deducted. New balance is {self.balance}."
        )


# 🔥 الاستخدام (زي الصورة)
savings = SavingsAccount("123456", 5000, 2.5)  #
savings.deposit(1000)
savings.add_interest()

checking = CheckingAccount("987654", 2000, 10)
checking.withdraw(500)
checking.deduct_transaction_fee()

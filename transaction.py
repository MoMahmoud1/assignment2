from bankAccount import BankAccount


class Transaction:
    def __init__(self, from_account: BankAccount, to_account: BankAccount, amount: float):
        self.__from_account = from_account
        self.__to_account = to_account
        self.amount = amount
        if self.__from_account.withdraw(amount):
            self.__to_account.deposit(amount)

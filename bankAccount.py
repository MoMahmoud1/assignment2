class BankAccount:
    def __init__(self, account_id: str, balance: float, transaction_list: []):
        self.__account_id = account_id
        self.__balance = balance
        self.__transaction_list = transaction_list

    # @property
    def account_id(self):
        return self.__account_id

    # @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        successful = True
        if self.__balance + amount < self.__balance:
            successful = False
        elif self.__balance + amount > self.__balance:
            successful = True
            self.__balance = self.__balance + amount

    def withdraw(self, amount):
        successful: bool
        if amount < self.__balance:
            successful = True
            self.__balance = self.__balance - amount
            print(f'balance is : {self.__balance}')
        elif amount > self.__balance:
            successful = False
            raise ValueError

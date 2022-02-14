from bankAccount import BankAccount
from transaction import Transaction

account1 = BankAccount("1", 1000, [])
account2 = BankAccount("2", 2000, [])
account3 = BankAccount("3", 3000, [])
account4 = BankAccount("4", 4000, [])

transaction1 = Transaction(account1, account2, 150)
print(f'withdraw   : {transaction1.amount}')
transaction2 = Transaction(account3, account4, 500)
print(f'withdraw   : {transaction2.amount}')

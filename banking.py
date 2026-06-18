class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self):
        self.deposit_amt = int(input('Enter the deposit amount: '))
        self.balance += self.deposit_amt
        print(f'Final balance after deposit: {self.balance}')

    def withdraw(self):
        self.withdraw_amt = int(input('Enter the amount you would like to withdraw: '))
        if self.withdraw_amt > self.balance:
            print('Cannot withdraw this amount.')
        else:
            self.balance -= self.withdraw_amt
    def print_balance(self):
        print(f'Your final balance is: {self.balance}')

name = input('Enter the name of the account holder: ')
balance = int(input('Enter the current balance of the user: '))
obj1 = BankAccount(name,balance)
obj1.deposit()
obj1.withdraw()
obj1.print_balance()

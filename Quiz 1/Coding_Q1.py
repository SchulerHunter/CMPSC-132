class Account:
    def __init__(self, name):
        self.holder=name
        self.balance=0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(('deposit', amount))
        return self.balance

    def withdraw(self, amount):
        if amount>self.balance:
            return 'Not enough funds'
        self.balance-=amount
        self.transactions.append(('withdraw', amount))
        return self.balance

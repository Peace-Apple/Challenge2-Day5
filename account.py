class BankAccount:
    def __init__(self):
        self.balance = 0
        self.status = False

    def get_balance(self):
        if not self.status:
            raise ValueError(" sorry account closed, transaction can't be done")
        return self.balance

    def open(self):
        self.status = True

    def deposit(self, amount):
        if not self.status:
            raise ValueError(" sorry account closed, transaction can't be done")
        if amount < 0:
            raise ValueError("can not have a negative account")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not self.status:
            raise ValueError(" sorry account closed, transaction can't be done")
        if amount < 0:
            raise ValueError("can not have a negative account")
        if amount > self.get_balance():
            raise ValueError("can not withdraw more than the deposited amount")
        self.balance -= amount
        return self.balance

    def close(self):
        self.status = False
class Client:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContaCorrente:
    def __init__(self, client, number, balance = 0):
        self.balance = 0
        self.number = number
        self.client = client
        self.extract = []
        self.deposit(balance)

    def getExtract(self):
        for operation in self.extract:
            print(operation[0], operation[1])

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            self.extract.append(["Withdraw", value])

    def deposit(self, value):
        self.balance += value
        self.extract.append(["Deposit", value])

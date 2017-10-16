from bank import ContaCorrente
from bank import ContaEspecial
from bank import Client

c1 = Client("Emmanuel", "3216354")
cc = ContaCorrente(c1, 1, 200)
cc.withdraw(100)
cc.deposit(1000)
cc.deposit(20)
cc.getExtract()
print(cc.client.phone)
print("-_" * 10)
c2 = Client("Júlia", "321689")
ce = ContaEspecial(c2, 2, 1000, 200)
ce.withdraw(1100)
ce.getExtract()
print(ce.balance)
print(ce.client.name)

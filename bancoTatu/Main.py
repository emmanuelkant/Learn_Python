from bank import ContaCorrente
from bank import Client

c1 = Client("Emmanuel", "3216354")
cc = ContaCorrente(c1, 1, 200)
cc.withdraw(100)
cc.deposit(1000)
cc.deposit(20)
cc.getExtract()

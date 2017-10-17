import random
def genInteger():
    listInt = []
    for i in range(15):
        listInt.append(random.randint(10, 100))
    return listInt
listInt = genInteger()
for i in listInt:
    print(i)

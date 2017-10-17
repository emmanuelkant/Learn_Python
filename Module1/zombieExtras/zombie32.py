# import random
# def genInteger():
#     listInt = []
#     while True:
#         doOrNot = True
#         num = random.randint(10, 100)
#         for testNum in listInt:
#             if num == testNum:
#                 doOrNot = False
#         if doOrNot:
#             listInt.append(num)
#         if len(listInt) == 15:
#             break
#     return listInt
# listInt = genInteger()
# for i in listInt:
#     print(i)

import random
listInt = []
while len(listInt) < 15:
    x = random.randint(10, 100)
    if x not in listInt:
        listInt.append(x)
listInt.sort()
print(listInt)

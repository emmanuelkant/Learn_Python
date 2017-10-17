def factorial(num):
    fac = 1
    for aux in range(num + 1):
        if aux != 0:
            fac *= aux
    return fac

# userNum = int(input('Enter with a number: '))
# print(factorial(userNum))
for i in range(10):
    print(factorial(i))

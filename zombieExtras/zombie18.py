prevFib1 = 1
prevFib2 = 1
i = 1
userNum = int(input("Enter the number that you need make Fibonacci: "))
while i <= userNum - 2:
    prevFib2, prevFib1 = prevFib1, prevFib2 + prevFib1
    i += 1
print("F(%i) = %i" %(userNum, prevFib1))

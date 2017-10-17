fat = 1
count = int(input("Enter the number which you need make factorial: "))
i = 1
while i < count:
    fat *= i
    i += 1
print("Factorial the %i is %i" %(count, fat))

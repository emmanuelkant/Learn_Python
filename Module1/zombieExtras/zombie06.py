a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Thirth number: "))
if a > b and a > c:
    print("%i é o maior número" %a)
elif b > c:
    print("%i é o maior número" %b)
else:
    print("%i é o maior número" %c)

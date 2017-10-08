total = 0
count = 0
while count < 10:
    num = int(input("Enter the %dº number to average: " %(count + 1)))
    total += num
    count += 1
print("The average is %.2f" %(total / count))

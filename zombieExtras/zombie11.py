userNum = int(input("Enter the number that you want stop: "))
count = 0
while count <= userNum:
    while count % 2 == 0:
        print(count)
        count += 1
    count += 1

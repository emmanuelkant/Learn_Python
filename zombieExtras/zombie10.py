userNum = int(input("Enter the number that you want stop: "))
count = 0
while count <= userNum:
    if count % 2 == 0:
        print(count)
    count += 1

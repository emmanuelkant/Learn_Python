listNum = []
for num in range(1067, 3628):
    if num % 2 == 0 and num % 7 == 0:
        listNum.append(num)
print(len(listNum))

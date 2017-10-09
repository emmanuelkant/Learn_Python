newFile = open('numbers.txt', 'r')
for line in newFile.readlines():
    print(line.rstrip())
newFile.close()

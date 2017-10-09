newFile = open('numbers.txt', 'w')
for line in range(1, 101):
    newFile.write('%d\n' %line)
newFile.close()

import random
def shuffle(name):
    listName = list(name)
    random.shuffle(listName)
    return ''.join(listName)

name = str(input('Enter with name: '))
print(shuffle(name))

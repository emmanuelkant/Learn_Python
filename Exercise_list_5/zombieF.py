def formatBook(line):
    import string
    line = line.lower()
    punctuation = string.punctuation
    for signed in punctuation:
        line = line.replace(signed, '')
    return line.split(" ")

book = open('alice.txt', 'r')
linesBook = book.read()
print(linesBook)
book.close()
dicionarie = {}
count = 0
for line in linesBook:
    listWord  = formatBook(line)
    for word in listWord:
        if word not in dicionarie:
            dicionarie[word] = 1
            count += 1
        else:
            dicionarie[word] += 1
print(count)

# Way of professor
# arq = open('alice.txt')
# texto = arq.read()
# texto = text.lower()
# import string
# for c in string.punctuation:
#     texto = texto.replace(c, " ")
# texto = texto.split()
# dic = {}
# for p in texto:
#     if p not in dic:
#         dic[p] = 1
#     else:
#         dic[p] += 1
# arq.close()

option = ""
while option != "sair":
    option = str(input("Enter with a word: "))
    if option in dicionarie:
        print("This word repeat %i times in the book." %dicionarie[option])
    else:
        print("This word do not exist in Alice's Book. Try another.")

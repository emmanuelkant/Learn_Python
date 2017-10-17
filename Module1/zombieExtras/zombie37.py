def change(s):
    s = list(s)
    newStr = []
    for i in s:
        if i in 'aeiou':
            newStr.append('*')
        else:
            newStr.append(i)
    return ''.join(newStr)

criptoFile = open("cripto.txt", 'w')
messageFile = open('mensage.txt', 'r')
for message in messageFile.readlines():
    lineMessage = message.rstrip()
    criptoFile.write('%s\n' %change(lineMessage))
criptoFile.close()
messageFile.close()


# texto = open('mensage.txt')
# saida = open('cripto.txt', 'w')
# for linha in texto.readlines():
#     for letra in linha:
#         if letra in 'aeiou':
#             saida.write('*')
#         else:
#             saida.write(letra)
# texto.close()
# saida.close()

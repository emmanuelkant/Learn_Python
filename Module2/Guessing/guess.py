# import random
# gameNum = random.randint(1, 101)
# while True:
#     userNum = int(input("Enter with a number between 1 and 100: "))
#     if userNum < gameNum:
#         print("Oh almost there, little bit toward up.")
#     elif userNum > gameNum:
#         print("Oh almost there, little bit toward down.")
#     else:
#         print("Contratulations!!! Right there! You Win!")
#         break
# print("Game Over")


# or

import random
gameNum = random.randint(1, 101)
while True:
    userNum = int(input("Enter with a number between 1 and 100: "))
    if userNum == gameNum:
        print("Congratulations!!! Right there! You Win!")
        break
    else:
        print("Oh almost there, little bit toward down." if userNum > gameNum else "Oh almost there, little bit toward up.")
print("Game Over")

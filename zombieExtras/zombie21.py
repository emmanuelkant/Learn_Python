userStr = str(input("Enter the word and I'll say if it is a polindrome word: "))
userStr2 = userStr[:: -1]
if userStr == userStr2:
	print("The word is polindrome!")
else:
	print("The word is not pilindrome!")
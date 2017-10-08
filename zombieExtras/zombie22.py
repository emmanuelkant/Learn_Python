userStr = str(input('Write a sentence: '))
outPut = ''
if userStr in 'aeiou':
	i = 0
	while i < len(userStr) - 1:
		char = userStr[i]
		if char in 'aeiou':
			outPut += char
else:
	print("Your sentence not have a voice letter")

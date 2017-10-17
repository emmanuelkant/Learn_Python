userStr = str(input('Write a sentence: '))
print(userStr)
output = ''
j = 0
while j < len(userStr) - 1:
	if userStr[j] in 'aeiou':
		output += '*'
	else:
		output += userStr[j]
	j += 1
if output == '':
	print('Your sentence has no vowel.')
else:
	print(output)

countryA = 80000
countryB = 200000
yearsPassed = 0
while True:
	if countryA > countryB:
		break
	else:
		yearsPassed += 1
	countryA += (countryA * 3) / 100
	countryB += (countryB * 1.5) / 100
print("Country A Population -> %.2f" %countryA)
print("Country B Population -> %.2f" %countryB)
print("Was necessary %i years to population of Country A pass population of Country B." %yearsPassed) 
userName = ""
password = ""
choice = True
while choice:
	userName = str(input("Enter the name account: "))
	password = str(input("Enter the password: "))
	if userName.upper() == password.upper():
		print("Error: Username and password do not be equal. Please insert again.")
		choice = True
	else:
		print("Account create with succefull!!!")
		choice = False	
print("Username: %s" %userName)
print("Password: %s" %password)		
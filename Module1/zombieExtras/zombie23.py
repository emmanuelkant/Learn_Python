monthList = ['January', 'February', 'March', 'April', 'May', 'June',
 'July', 'August', 'September', 'October', 'November', 'December']
userDate = str(input('Enter with a date: '))
splitDate = userDate.split('/')
if splitDate[1].startswith ('0'):
    splitDate[1] = splitDate[1].replace('0', '')
print('Your date for extense is %s the %s the %s' %(splitDate[0], monthList[int(splitDate[1]) - 1], splitDate[2]))

# Other kind to make this
day, month, year = input('Date (dd/mm/yyyy)').split('/')
monthList = ['January', 'February', 'March', 'April', 'May', 'June',
 'July', 'August', 'September', 'October', 'November', 'December']
print( 'Your date is %s the %s the %s' %(day, monthList[int(month) - 1], year)

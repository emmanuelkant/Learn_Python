talkedMinutes = int(input('How many minutes you are talked this month: '))
if talkedMinutes < 200:
    print('The value of your account is %.2f' %(talkedMinutes * 0.20))
elif talkedMinutes >= 200 and talkedMinutes <= 400:
    print("The value of your account is %.2f" %(talkedMinutes * 0.18))
else:
    print("The value of your account is %.2f" %(talkedMinutes * 0.15))

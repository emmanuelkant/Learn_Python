talkedMinutes = int(input('How many minutes you are talked this month: '))
pricePerMinute = 0.00
if talkedMinutes < 200:
    print("Your modifier is R$0.20 per minute")
    pricePerMinute = 0.20
elif talkedMinutes <= 400:
    print("Your modifier is R$0.18 per minute")
    pricePerMinute = 0.18
elif talkedMinutes <= 800:
    print("Your modifier is R$0.15 per minute")
    pricePerMinute = 0.15
else:
    print("Your modifier is R$0.08 per minute")
    pricePerMinute = 0.08
print("The value of your account is %.2f" %(talkedMinutes * pricePerMinute))

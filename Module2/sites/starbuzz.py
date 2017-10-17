def getPrice():
    print("Trying...")
    page = urllib.request.urlopen('http://beans.itcarlow.ie/prices-loyalty.html')
    text = page.read().decode('utf-8')
    where = text.find(">$")
    start = where + 2
    end = start + 4
    return float(text[start:end])
import urllib.request
import time
option = str(input("Whish buy now! (S/N)"))
if option.upper() == "S":
    price = getPrice()
    print("Price is {0:.2f} buy now!".format(price))
else:
    price = 99.99
    while price >= 4.50:
        price = getPrice()
        if price >= 4.50:
            print("Price is {0:.2f} do not buy".format(price))
            time.sleep(10)
        else:
            print("Price is {0:.2f} buy now!".format(price))

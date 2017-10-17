import urllib.request
page = urllib.request.urlopen("http://preev.com/btc/brl")
text = page.read()
print(text)

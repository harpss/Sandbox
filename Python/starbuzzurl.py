import urllib.request

page = urllib.request.urlopen("http://www.beans-r-us.biz/prices-loyalty.html")
text = page.read().decode("utf8")

first = text.find(">$")

price = text[first+2:first+6]

print (price)

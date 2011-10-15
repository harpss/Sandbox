
import urllib.request


substringLength = 2
priceLength = 4
price = 99.99

while price > 4.74:
    page = urllib.request.urlopen("http://www.beans-r-us.biz/prices.html")
    text = page.read().decode("utf8")
    substringStartIndex = text.find('>$')
    priceStartIndex = substringStartIndex + substringLength
    priceEndIndex = priceStartIndex + priceLength
    price = text[priceStartIndex:priceEndIndex]
    print(price)
    price = float(text[priceStartIndex:priceEndIndex])

print ("Buy!")
    
    

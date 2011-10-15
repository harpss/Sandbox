
import urllib.request
import time


substringLength = 2
priceLength = 4
price = 99.99

while price > 4.74:
    page = urllib.request.urlopen("http://www.beans-r-us.biz/prices.html")
    text = page.read().decode("utf8")
    substringStartIndex = text.find('>$')
    priceStartIndex = substringStartIndex + substringLength
    priceEndIndex = priceStartIndex + priceLength
    price = float(text[priceStartIndex:priceEndIndex])
    print(price)
    time.sleep(900)
    
print ("Buy!")
    
    

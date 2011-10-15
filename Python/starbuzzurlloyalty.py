import urllib.request

page = urllib.request.urlopen("http://www.beans-r-us.biz/prices.html")
text = page.read().decode("utf8")

lengthOfPrice = 4
lengthOfSubString = 2

substringIndexPosition = text.find(">$")
startingPricePosition = substringIndexPosition + lengthOfSubString
endingPricePosition = startingPricePosition + lengthOfPrice

price = text[startingPricePosition:endingPricePosition]

print (price)

import urllib.request

def get_price():
    page = urllib.request.urlopen("http://www.beans-r-us.biz/prices.html")
    text = page.read().decode("utf8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    
    return(text[start_of_price:end_of_price])

discount = 0.9


price = get_price()

print ("The original price is: " + str(price))
print ('\n')

actual_price = float(price) * discount
print("The discounted price is: " + str(actual_price))


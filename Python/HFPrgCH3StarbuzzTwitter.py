import urllib.request
import time

def send_to_twitter():
    msg = "I am a test message that will be sent to Twitter"
    password_manager = urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API",
                                  "http://twitter.com/statuses", "harpssnagra", "twitHarp1!")
    http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener = urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params = urllib.parse.urlencode({'status':msg})
    resp = urllib.request.urlopen("http://twitter.com/statuses/update.json", params)
    resp.read()







def get_price():
    page = urllib.request.urlopen("http://www.beans-r-us.biz/prices.html")
    text = page.read().decode("utf8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return float(text[start_of_price:end_of_price])

userInput = 0
while not(userInput == 'Y' or userInput == 'N'):
    userInput = input("Is price required immediately?  (Y/N)")
if (userInput == 'Y'):

    price = get_price()
else:
    while(get_price() > 4.74):
        price = get_price()
        print(price)
        time.sleep(900)
print(price)
send_to_twitter()

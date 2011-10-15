import urllib.request
import time
import sys
import tweepy


def send_to_twitter(msg):
    CONSUMER_KEY = 'jgKpEOVK5MTUAAvJbmJQ'
    CONSUMER_SECRET = 'dn6tbNBHCDuJIQVAB9zJb7WWuNpHD6M9MFUmL7VxQ'
    ACCESS_KEY = '375927564-4JWzYO3JFfSecEl5LplfqN0AfiQ362NzwRXjSdlg'
    ACCESS_SECRET = '2XuQr4rgcaLNq9mKCNYdVYZoFs3IKJCkBLXMSAHPk'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(msg)


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
send_to_twitter(price)

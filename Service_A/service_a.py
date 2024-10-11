import requests
import time
from statistics import mean

def get_bitcoin_price():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    return response.json()["bitcoin"]["usd"]

prices = []

while True:
    price = get_bitcoin_price()
    prices.append(price)
    print(f"Current Bitcoin Price: ${price}")
    
    if len(prices) == 10:
        avg_price = mean(prices)
        print(f"Average Price of Last 10 Minutes: ${avg_price}")
        prices = []

    time.sleep(60)  

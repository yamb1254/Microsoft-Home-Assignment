import requests
import time

def fetch_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['bitcoin']['usd']
    else:
        return None

def main():
    prices = []
    while True:
        price = fetch_bitcoin_price()
        if price:
            print(f"Current Bitcoin price: ${price}")
            prices.append(price)
            if len(prices) > 10:
                prices.pop(0)
            if len(prices) == 10:
                avg_price = sum(prices) / len(prices)
                print(f"10-minute average Bitcoin price: ${avg_price}")
        else:
            print("Failed to retrieve Bitcoin price.")
        time.sleep(60)  # Sleep for 1 minute

if __name__ == "__main__":
    main()
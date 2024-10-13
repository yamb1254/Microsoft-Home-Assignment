import requests
import threading
import time
from flask import render_template_string
from constants import Configurations

# Global variable for storing prices
prices = []

def start_price_updater():
    """Starts a background thread to update Bitcoin prices every minute."""
    threading.Thread(target=update_bitcoin_prices, daemon=True).start()

def fetch_bitcoin_price():
    """Fetches the current Bitcoin price from the API."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an exception for HTTP errors
        data = response.json()
        return data['bitcoin']['usd']
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None

def update_bitcoin_prices():
    """Continuously updates the prices list with the latest Bitcoin prices."""
    while True:
        price = fetch_bitcoin_price()
        if price is not None:
            _update_price_list(price)
            _log_price_data()
        else:
            print("Failed to retrieve Bitcoin price.")
        time.sleep(60)

def _update_price_list(price):
    """Updates the list of prices and ensures only the last 10 prices are kept."""
    prices.append(price)
    if len(prices) > 10:
        prices.pop(0)

def _log_price_data():
    """Logs the current price and 10-minute average if available."""
    current_price = prices[-1]
    print(f"Updated Bitcoin price: ${current_price}")
    if len(prices) == 10:
        avg_price = sum(prices) / len(prices)
        print(f"10-minute average Bitcoin price: ${avg_price}")

def get_bitcoin_price_util():
    """Generates and returns the HTML page displaying the Bitcoin price."""
    if not prices:
        return "<h1>No prices available</h1>", 500

    current_price = prices[-1]
    avg_price = _calculate_average_price() if len(prices) == 10 else None

    html = Configurations.html
    return render_template_string(html, current_price=current_price, avg_price=avg_price)

def _calculate_average_price():
    """Calculates the average price of the last 10 updates."""
    return sum(prices) / len(prices)

# Start the price updating thread
start_price_updater()
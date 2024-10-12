from flask import Flask, render_template_string
import requests
import threading
import time

app = Flask(__name__)

prices = []

def fetch_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['bitcoin']['usd']
    else:
        return None

# Background task to fetch and update the Bitcoin price every minute
def update_bitcoin_prices():
    while True:
        price = fetch_bitcoin_price()
        if price:
            prices.append(price)
            if len(prices) > 10:
                prices.pop(0)
            print(f"Updated Bitcoin price: ${price}")
            if len(prices) == 10:
                avg_price = sum(prices) / len(prices)
                print(f"10-minute average Bitcoin price: ${avg_price}")
        else:
            print("Failed to retrieve Bitcoin price.")
        time.sleep(60)

# Start the background thread to update prices
threading.Thread(target=update_bitcoin_prices, daemon=True).start()

# Define an HTTP route to return the current price and 10-minute average as an HTML page
@app.route('/', methods=['GET'])
def get_bitcoin_price():
    if len(prices) == 0:
        return "<h1>No prices available</h1>", 500

    current_price = prices[-1]
    avg_price = sum(prices) / len(prices) if len(prices) == 10 else None

    # HTML template to display the Bitcoin prices
    html = """
    <html>
    <head>
        <title>Bitcoin Price</title>
    </head>
    <body>
        <h1>Bitcoin Price</h1>
        <p><strong>Current Price:</strong> ${{ current_price }}</p>
        {% if avg_price %}
            <p><strong>10-Minute Average Price:</strong> ${{ avg_price }}</p>
        {% else %}
            <p>Not enough data for a 10-minute average yet.</p>
        {% endif %}
    </body>
    </html>
    """

    return render_template_string(html, current_price=current_price, avg_price=avg_price)

if __name__ == "__main__":
    # Run the Flask app on port 80
    app.run(host='0.0.0.0', port=80)

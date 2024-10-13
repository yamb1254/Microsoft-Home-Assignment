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

@app.route('/healthz', methods=['GET'])
def health_check():
    return "OK", 200


@app.route('/readyz', methods=['GET'])
def readiness_check():
    return "Ready", 200

# return the current price and 10-minute average 
@app.route('/', methods=['GET'])
def get_bitcoin_price():
    if len(prices) == 0:
        return "<h1>No prices available</h1>", 500

    current_price = prices[-1]
    avg_price = sum(prices) / len(prices) if len(prices) == 10 else None


    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bitcoin Price</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <div class="row">
                <div class="col-md-8 offset-md-2">
                    <div class="card">
                        <div class="card-header text-center">
                            <h1>Bitcoin Price Tracker</h1>
                        </div>
                        <div class="card-body">
                            <h3 class="text-center">Current Bitcoin Price</h3>
                            <p class="text-center display-4">${{ current_price }}</p>
                            {% if avg_price %}
                                <h4 class="text-center">10-Minute Average Price</h4>
                                <p class="text-center display-4">${{ avg_price }}</p>
                            {% else %}
                                <p class="text-center">Not enough data for a 10-minute average yet.</p>
                            {% endif %}
                        </div>
                        <div class="card-footer text-center">
                            <small>Updated every minute</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>
    """

    return render_template_string(html, current_price=current_price, avg_price=avg_price)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

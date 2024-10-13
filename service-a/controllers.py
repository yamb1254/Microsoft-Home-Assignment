from utilitis import get_bitcoin_price_util
from app import app


@app.route('/healthz', methods=['GET'])
def health_check():
    return "OK", 200

@app.route('/readyz', methods=['GET'])
def readiness_check():
    return "Ready", 200

@app.route('/', methods=['GET'])
def get_bitcoin_price():
   return get_bitcoin_price_util()
from flask import Flask
from constants import Configurations

app = Flask(__name__)


if __name__ == "__main__":
    from controllers import *
    app.run(host=Configurations.server_url, port=80)

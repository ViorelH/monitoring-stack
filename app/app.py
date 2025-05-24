import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home route was accessed.")
    return "Hello from Kubernetes Flask app!"

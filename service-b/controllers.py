from flask import render_template_string
from app import app
from utilities import hello_utili


@app.route('/')
def hello():
   return hello_utili()


# Health check endpoint
@app.route('/healthz', methods=['GET'])
def health_check():
    return "OK", 200


# Readiness check endpoint
@app.route('/readyz', methods=['GET'])
def readiness_check():
    return "Ready", 200
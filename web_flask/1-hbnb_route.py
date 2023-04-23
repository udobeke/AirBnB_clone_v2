#!/usr/bin/python3
"""This script that starts a Flask web application:
        Your web application is  listening on 0.0.0.0, port 5000 """

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Return the Home Page"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return 'HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


#!/usr/bin/python3
"""
A script that starts a Flask web application:
The web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'."""
    return "Hello HBNB!"

# Run the Flask application on 0.0.0.0:5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

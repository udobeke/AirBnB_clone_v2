#!/usr/bin/python3
"""
A script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text
        variable (replace underscore _ symbols with a space )
        /python/(<text>): display “Python ”, followed by the
        value of the text variable (replace underscore _ symbols with a space
"""


from flask import Flask


app = Flask('__name__')


@app.route('/', strict_slashes=False)
def index():
    """Return the Home Page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text=None):
    """display “C ” followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """Display “Python ”, followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=None)

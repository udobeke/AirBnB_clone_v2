#!/usr/bin/python3
"""
A script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
"""

from flask import Flask, render_template


app = Flask('__name__')


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays "Hello HBNB!"."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays "HBNB"."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Route that displays "C " followed by the value of the text variable."""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Route display “Python ”, followed by the value of the text variable."""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Route display “n is a number” only if n is an integer."""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays a HTML page only if n is an integer H1 tag: "Number: n" inside
    the tag BODY."""
    return render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numberoddoreven(n):
    if isinstance(n, int):
        if n % 2 == 0:
            number = 'even'
        else:
            number = 'odd'
        return render_template('6-number_odd_or_even.html', n=n, number=number)


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)

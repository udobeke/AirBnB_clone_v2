#!/usr/bin/python3
"""
This module starts a Flask web application that displays a list of states.
"""

from flask import Flask, render_template, teardown_appcontext
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Removes the current SQLAlchemy Session."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a list of states."""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

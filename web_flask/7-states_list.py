#!/usr/bin/python3
"""
This module starts a Flask web application that displays a list of states.
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    """Displays a list of states."""
    states = storage.all(State)
    states = storage.all()
    return render_template('7-states_list.html', states=sorted_states)
    
@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

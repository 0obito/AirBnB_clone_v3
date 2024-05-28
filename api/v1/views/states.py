#!/usr/bin/python3
"""
this module is a view for State objects that
handles all default RESTFul API actions
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', strict_slashes=False)
def retrieve_all():
    """ retrieves the list of all State objects """
    states_objs = storage.all(State)
    states = [state.to_dict() for state in states_objs.values()]
    return jsonify(states)

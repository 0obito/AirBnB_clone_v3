#!/usr/bin/python3
"""
This module defines routes for API
"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def status():
    """ Provides the status of the API """
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    pass

#!/usr/bin/python3
"""
This module defines routes for API
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """ Provides the status of the API """
    return jsonify({"status": "OK"})

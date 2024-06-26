#!/usr/bin/python3
"""
A module that sets up a Flask application
with a specific configuration
"""
from flask import Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = int(os.getenv('HBNB_API_PORT', '5000'))


@app.teardown_appcontext
def teardown(code):
    """Closes the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def error_404(error):
    """ Handles the famous 404 Error in an unusual way """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)

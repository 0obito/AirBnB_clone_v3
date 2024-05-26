#!/usr/bin/python3

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
HBNB_API_HOST = getenv('HBNB_API_HOST')
HBNB_API_PORT = getenv('HBNB_API_PORT')

@app.route("/")
def func():
    return "YES, I AM WORKING FINE!!!"

@app.teardown_appcontext
def teardown():
    storage.close()

if __name__ == "__main__":
    if HBNB_API_HOST is None:
        HBNB_API_HOST = '0.0.0.0'
    if HBNB_API_PORT is None:
        HBNB_API_PORT = '5000'
    app.run(host=HBNB_API_HOST, port=int(HBNB_API_PORT), threaded=True)

#!/usr/bin/python3
"""
This module initializes the blueprint for API
"""
from flask import Blueprint
from api.v1.views.index import *


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

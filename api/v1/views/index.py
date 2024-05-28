#!/usr/bin/python3
"""
This module defines routes for API
"""
from api.v1.views import app_views
from flask import jsonify
import models
import models.amenity
import models.base_model
import models.city
import models.place
import models.review
import models.state
import models.user

classes = {"amenities": models.amenity.Amenity,
           "cities": models.city.City, "places": models.place.Place,
           "reviews": models.review.Review, "states": models.state.State,
           "users": models.user.User}


@app_views.route('/status', strict_slashes=False)
def status():
    """ Provides the status of the API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def count_by_type():
    """ Retrieves the number of each objects by type """
    stats_dict = {}
    for k, v in classes.items():
        stats_dict[k] = models.storage.count(v)

    return jsonify(stats_dict)

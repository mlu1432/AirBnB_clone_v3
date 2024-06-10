#!/usr/bin/python3
"""cities.py for airbnb"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request, Flask
from models import storage
from models.city import City

app = Flask(__name__)


@app_views.route('/states/<string:state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_cities_by_state(state_id):
    """Retrieves the list of all City objects of a State"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)

    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)


@app_views.route('/cities/<string:city_id>',
                 methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """ Retrieves a specific City """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<string:city_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Deletes a City Object"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    return jsonify({})


@app_views.route('/states/<string:state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def post_city(state_id):
    """Creates a new City"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)

    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)

    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)

    data = request.get_json()
    data['state_id'] = state_id
    city = City(**data)
    city.save()
    return make_response(jsonify(city.to_dict()), 201)


@app_views.route('/cities/<string:city_id>',
                 methods=['PUT'], strict_slashes=False)
def put_city(city_id):
    """Updates a City"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)

    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)

    ignore = ['id', 'state_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(city, key, value)
    storage.save()
    return jsonify(city.to_dict())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

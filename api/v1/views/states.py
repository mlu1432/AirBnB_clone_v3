#!/usr/bin/python3
"""
State module
"""
from flask import jsonify, request, abort
from models import storage
from models.state import State
from api.v1.views import app_views
import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.DEBUG)

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Retrieves the list of all State objects"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieves a State object"""
    logging.debug(f"Fetching State with id {state_id}")
    state = storage.get(State, state_id)
    if state is None:
        logging.debug(f"State with id {state_id} not found")
        abort(404)
    return jsonify(state.to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object"""
    logging.debug(f"Deleting State with id {state_id}")
    state = storage.get(State, state_id)
    if state is None:
        logging.debug(f"State with id {state_id} not found")
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200

@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a State object"""
    if not request.json:
        abort(400, description="Not a JSON")
    if 'name' not in request.json:
        abort(400, description="Missing name")
    data = request.get_json()
    new_state = State(**data)
    storage.new(new_state)
    storage.save()
    logging.debug(f"Created State with id {new_state.id}")
    return jsonify(new_state.to_dict()), 201

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Updates a State object"""
    logging.debug(f"Updating State with id {state_id}")
    state = storage.get(State, state_id)
    if state is None:
        logging.debug(f"State with id {state_id} not found")
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    ignore = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore:
            setattr(state, key, value)
    storage.save()
    logging.debug(f"Updated State with id {state_id}")
    return jsonify(state.to_dict()), 200

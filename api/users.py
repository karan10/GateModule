import json
import uuid

from flask import request, jsonify
from werkzeug.exceptions import BadRequest

from app import app
from calculation.evaluation import Evaluation
from helper.constants import required_attributes
from models.gate.gate_resolver import GateResolver
from models.users.user_resolver import UserResolver
from dto.user import User

# ur = UserResolver('inMem')
user_obj = UserResolver.new()


@app.route('/users', methods=['GET'])
def get_users():
    user_obj.get_all()
    return jsonify({
        'success': True,
        'data': user_obj.get_all()
    }), 200


@app.route('/user', methods=['POST'])
def post_users():
    data = request.get_json()

    is_valid, msg = _is_create_user_valid(data)
    if not is_valid:
        raise BadRequest(msg)

    user_data = User(json.dumps(data))
    user_id = user_obj.add(user_data)
    return jsonify({
        'success': True,
        'data': user_id
    }), 200


@app.route('/user/<user_id>/is-allowed', methods=['POST'])
def is_user_allowed(user_id):
    data = request.get_json()

    if 'gate_id' not in data or not data['gate_id']:
        raise BadRequest("Gate id not available")

    user_id = uuid.UUID(user_id)
    user = user_obj.get(user_id)
    if not user:
        raise BadRequest("User does not exists")


    gate_id = uuid.UUID(data['gate_id'])
    gate_obj = GateResolver.new()
    gate = gate_obj.get(gate_id)
    if not gate:
        raise BadRequest("Gate does not exists")


    try:
        is_allowed = Evaluation().evaluate(gate[0]['condition'], user[0])
        return jsonify({
            'success': True,
            'data': is_allowed
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'data': e.__str__()
        }), 400


def _is_create_user_valid(data):
    if set(required_attributes) != set(dict(data).keys()):
        return False, "Required params missing. Required params {}".format(required_attributes)
    return True, ""

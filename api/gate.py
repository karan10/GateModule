import json

from flask import request, jsonify
from werkzeug.exceptions import BadRequest

from app import app
from dto.gate import Gate
from models.gate.gate_resolver import GateResolver

gate_obj = GateResolver.new()


@app.route('/gates', methods=['GET'])
def get_gates():
    return jsonify({
        'success': True,
        'data': gate_obj.get_all()
    }), 200


@app.route('/gate', methods=['POST'])
def post_gate():
    data = request.get_json()

    is_valid, msg = _is_valid(data)
    if not is_valid:
        raise BadRequest(msg)
    gates = gate_obj.get_all()
    if _is_already_exists(data, gates):
        raise BadRequest("Gate with this feature already exists")

    gate_data = Gate(json.dumps(data))
    gate_id = gate_obj.add(gate_data)
    return jsonify({
        'success': True,
        'data': gate_id
    }), 200

def _is_valid(data):
    if 'condition' not in data or not data['condition']:
        return False, "Missing condition"
    if 'feature' not in data or not data['feature']:
        return False, "Missing feature"
    return True, ""


def _is_already_exists(data, gates):
    for gate in gates:
        if gate['feature'] == data['feature']:
            return True


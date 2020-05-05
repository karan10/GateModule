import uuid

from dto.gate import Gate
from models.gate.gate_interface import GateInterface


class InMemGate(GateInterface):
    def __init__(self):
        self.gate_list = [
            {
                'id': uuid.uuid4(),
                'condition': '( age > 25 AND gender == "f" ) OR ( past_order_amount > 10000 )',
                'feature': 'prime_access'
            }
        ]

    def get_all(self):
        return self.gate_list

    def get(self, gate_id: uuid.UUID):
        return list(filter(lambda x: (x['id'] == gate_id), self.gate_list))

    def add(self, gate: Gate):
        gate.id = uuid.uuid4()
        self.gate_list.append(gate.__dict__)
        return gate.id

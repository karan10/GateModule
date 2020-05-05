import uuid

from dto.gate import Gate
from models.gate.in_mem_gate import InMemGate


class GateResolver:
    gate_resolver = None

    def __init__(self, file_system):
        if file_system == 'inMem':
            self.gate = InMemGate()

    def get_all(self):
        return self.gate.get_all()

    def get(self, gate_id: uuid):
        return self.gate.get(gate_id)

    def add(self, gate: Gate):
        return self.gate.add(gate)

    @staticmethod
    def new():
        if not GateResolver.gate_resolver:
            GateResolver.gate_resolver = GateResolver('inMem')
        return GateResolver.gate_resolver




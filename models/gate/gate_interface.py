import abc
import uuid

from dto.gate import Gate


class GateInterface(abc.ABC):
    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def get(self, gate_id: uuid):
        pass

    @abc.abstractmethod
    def add(self, gate: Gate):
        pass

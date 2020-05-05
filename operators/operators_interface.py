import abc


class OperatorsInterface(abc.ABC):
    @abc.abstractmethod
    def get_operands_count(self):
        pass

    @abc.abstractmethod
    def get_precedence(self):
        pass

    @abc.abstractmethod
    def get_symbol(self):
        pass

    @abc.abstractmethod
    def execute(self, operands: list):
        pass

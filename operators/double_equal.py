from helper.operator_precedence import Precedence
from operators.operators_interface import OperatorsInterface


class DoubleEqualTo(OperatorsInterface):
    def __init__(self):
        self.precedence = Precedence.DOUBLE_EQUAL_TO
        self.symbol = '=='
        self.operands_count = 2

    def get_operands_count(self):
        return self.operands_count

    def get_precedence(self):
        return self.precedence

    def get_symbol(self):
        return self.symbol

    def execute(self, operands: list):
        if len(operands) != self.operands_count:
            raise Exception("invalid operand count")
        a, b = operands
        return a == b


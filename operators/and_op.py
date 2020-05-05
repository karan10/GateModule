from helper.operator_precedence import Precedence
from operators.operators_interface import OperatorsInterface


class And(OperatorsInterface):
    def __init__(self):
        self.precedence = Precedence.AND
        self.symbol = 'AND'
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
        str_left, str_right = operands
        return str_left and str_right


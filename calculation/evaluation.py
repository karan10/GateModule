from calculation import operators
from helper.constants import attributes_supported
from helper.common import convert_in_format
from storage.stack import StackStorage


class Evaluation:
    def __init__(self):
        self.operator_map = self.get_operators_map()

    def get_operators_map(self):
        operators_map = {}
        for operator in operators:
            operators_map[operator.symbol] = operator
        return operators_map

    def is_operand(self, ch):
        return ch in attributes_supported or ch.isdigit() or (ch.startswith("\"") and ch.endswith("\""))

    def not_greater(self, i, j):

        try:
            a = self.operator_map[i].get_precedence()
            b = self.operator_map[j].get_precedence()
            return True if a <= b else False
        except KeyError as e:
            raise KeyError('Seems like a missing operator - {} Please implement the functionality'.format(e.__str__()))

    def inf_to_post(self, tokens: list):
        stack = StackStorage()
        postfix = []
        for i in tokens:
            if self.is_operand(i):
                postfix.append(i)

            elif i == '(':
                stack.push(i)

            elif i == ')':
                while (not stack.empty()) and stack.peek() != '(':
                    a = stack.pop()
                    postfix.append(a)
                if not stack.empty() and stack.peek() == '(':
                    stack.pop()

            else:
                while not stack.empty() and stack.peek() != '(':
                    if self.not_greater(i, stack.peek()):
                        postfix.append(stack.pop())
                    else:
                        break
                if i not in self.operator_map:
                    raise Exception("Invalid operator: ", i)
                stack.push(i)

        while not stack.empty():
            postfix.append(stack.pop())

        return postfix

    def evaluate_postfix(self, exp: list, user_attribute: dict):
        stack = StackStorage()
        for i in exp:
            if self.is_operand(i):
                stack.push(i)

            else:
                val1 = stack.pop()
                val2 = stack.pop()
                arg = []
                for val in [val1, val2]:
                    if val in user_attribute:
                        arg = [user_attribute[val]] + arg
                    else:
                        arg = [convert_in_format(val)] + arg
                stack.push(self.operator_map[i].execute(arg))

        return stack.pop()

    def evaluate(self, expression: str, user_attribute: dict):
        expression_list = expression.strip().split(" ")
        post_fix = self.inf_to_post(expression_list)
        return self.evaluate_postfix(post_fix, user_attribute)

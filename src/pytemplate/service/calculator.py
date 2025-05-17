from pytemplate.domain.models import Operands


class Calculator:
    def add(self, operands: Operands) -> int:
        return operands.first_operand + operands.second_operand

    def subtract(self, operands: Operands) -> int:
        return operands.first_operand - operands.second_operand

    def multiply(self, operands: Operands) -> int:
        return operands.first_operand * operands.second_operand

    def divide(self, operands: Operands) -> int:
        if operands.second_operand == 0:
            raise ValueError("Cannot divide by zero.")
        return operands.first_operand // operands.second_operand  # integer division

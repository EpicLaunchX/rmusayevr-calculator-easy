from pytemplate.domain.models import operands_factory
from pytemplate.service.calculator import Calculator


def main():
    first_operand = int(input("Enter first operand: "))
    second_operand = int(input("Enter second operand: "))
    action = input("Enter action (add, subtract, multiply, divide): ").strip().lower()

    operands = operands_factory(first_operand, second_operand)
    calculator = Calculator()

    if action == "add":
        result = calculator.add(operands)
    elif action == "subtract":
        result = calculator.subtract(operands)
    elif action == "multiply":
        result = calculator.multiply(operands)
    elif action == "divide":
        result = calculator.divide(operands)
    else:
        raise ValueError("Invalid action")

    print(f"Result: {result}")

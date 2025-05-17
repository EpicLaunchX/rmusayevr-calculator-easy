from dataclasses import dataclass


@dataclass
class Operands:
    first_operand: int
    second_operand: int


def operands_factory(first_operand: int, second_operand: int) -> Operands:
    return Operands(first_operand=first_operand, second_operand=second_operand)

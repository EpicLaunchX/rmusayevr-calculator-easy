import pytest

from src.pytemplate.domain.models import Operands


def test_operands_initialization():
    op = Operands(first_operand=5, second_operand=10)
    assert op.first_operand == 5
    assert op.second_operand == 10


def test_operands_types():
    op = Operands(1, 2)
    assert isinstance(op.first_operand, int)
    assert isinstance(op.second_operand, int)


def test_operands_equality():
    op1 = Operands(3, 4)
    op2 = Operands(3, 4)
    assert op1 == op2

import pytest

from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def test_add():
    calculator = Calculator()
    operands = operands_factory(45, 35)
    assert calculator.add(operands) == 80


def test_subtract():
    calculator = Calculator()
    operands = operands_factory(50, 20)
    assert calculator.subtract(operands) == 30


def test_multiply():
    calculator = Calculator()
    operands = operands_factory(6, 7)
    assert calculator.multiply(operands) == 42


def test_divide():
    calculator = Calculator()
    operands = operands_factory(100, 5)
    assert calculator.divide(operands) == 20


def test_divide_by_zero():
    calculator = Calculator()
    operands = operands_factory(10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.divide(operands)

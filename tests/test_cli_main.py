import builtins
from unittest.mock import patch

from src.pytemplate.entrypoints.cli.main import main


def test_add(capsys):
    with patch.object(builtins, "input", side_effect=["45", "35", "add"]):
        main()
    captured = capsys.readouterr()
    assert "Result: 80" in captured.out


def test_subtract(capsys):
    with patch.object(builtins, "input", side_effect=["100", "40", "subtract"]):
        main()
    captured = capsys.readouterr()
    assert "Result: 60" in captured.out


def test_multiply(capsys):
    with patch.object(builtins, "input", side_effect=["7", "6", "multiply"]):
        main()
    captured = capsys.readouterr()
    assert "Result: 42" in captured.out


def test_divide(capsys):
    with patch.object(builtins, "input", side_effect=["90", "10", "divide"]):
        main()
    captured = capsys.readouterr()
    assert "Result: 9" in captured.out


def test_invalid_action():
    with patch("builtins.input", side_effect=["5", "5", "invalid"]):
        try:
            main()
            assert False, "Should raise ValueError"
        except ValueError as e:
            assert "Invalid action" in str(e)

import os
import pytest

from src.decorators import log


def test_log_file() -> None:
    @log(filename="mylog.txt")
    def example_function(x, y):
        return x * y

    result = example_function(5, 100)

    with open(os.path.join(r"logs", "mylog.txt"), "rt") as file:
        for line in file:
            log_string = line

    assert log_string == "example_function ok. Result: 500\n"
    assert result == 500


def test_log_console(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def example_function(x, y):
        return x * y

    result = example_function(5, 100)
    captured = capsys.readouterr()

    assert captured.out == "example_function ok. Result: 500\n"
    assert result == 500

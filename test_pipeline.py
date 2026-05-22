import pytest

from ex_pipeline import add, divide


def test_add_integers() -> None:
    assert add(1, 2) == 3


def test_add_floats() -> None:
    assert add(1.5, 2.5) == 4.0


def test_add_negative() -> None:
    assert add(-1, 1) == 0


def test_add_zero() -> None:
    assert add(0, 0) == 0


def test_divide_integers() -> None:
    assert divide(10, 2) == 5.0


def test_divide_floats() -> None:
    assert divide(7.5, 2.5) == 3.0


def test_divide_negative() -> None:
    assert divide(-6, 2) == -3.0


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)


def test_divide_by_zero_message_contains_args() -> None:
    with pytest.raises(ValueError, match=r"a=10, b=0"):
        divide(10, 0)


def test_divide_invalid_type_a() -> None:
    with pytest.raises(TypeError, match="'a' must be int or float"):
        divide("10", 2)  # type: ignore[arg-type]


def test_divide_invalid_type_b() -> None:
    with pytest.raises(TypeError, match="'b' must be int or float"):
        divide(10, None)  # type: ignore[arg-type]


def test_divide_bool_rejected() -> None:
    with pytest.raises(TypeError):
        divide(True, 2)

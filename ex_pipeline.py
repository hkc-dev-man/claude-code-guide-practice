def add(a: int | float, b: int | float) -> int | float:
    return a + b


def divide(a: int | float, b: int | float) -> float:
    """
    a を b で除算して結果を返す。

    Raises:
        TypeError: a または b が int/float でない場合（bool は不可）
        ValueError: b がゼロの場合
    """
    if isinstance(a, bool) or not isinstance(a, (int, float)):
        raise TypeError(f"'a' must be int or float, got {type(a).__name__}")
    if isinstance(b, bool) or not isinstance(b, (int, float)):
        raise TypeError(f"'b' must be int or float, got {type(b).__name__}")
    if b == 0:
        raise ValueError(f"Cannot divide by zero: a={a!r}, b={b!r}")
    return a / b

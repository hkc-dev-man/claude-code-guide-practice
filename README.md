# claude-code-guide-practice

Python パイプライン関数のサンプルリポジトリです。

## 関数一覧

### `add`

```python
def add(a: int | float, b: int | float) -> int | float
```

`a` と `b` を加算して返します。

**使用例**

```python
from ex_pipeline import add

add(1, 2)      # 3
add(1.5, 2.5)  # 4.0
add(-1, 1)     # 0
```

---

### `divide`

```python
def divide(a: int | float, b: int | float) -> float
```

`a` を `b` で除算して結果を `float` で返します。

**例外**

| 例外 | 発生条件 |
|---|---|
| `TypeError` | `a` または `b` が `int`/`float` でない場合（`bool` も不可） |
| `ValueError` | `b` がゼロの場合 |

**使用例**

```python
from ex_pipeline import divide

divide(10, 2)    # 5.0
divide(7.5, 2.5) # 3.0
divide(-6, 2)    # -3.0
```

**エラー例**

```python
divide(1, 0)       # ValueError: Cannot divide by zero: a=1, b=0
divide("10", 2)    # TypeError: 'a' must be int or float, got str
divide(10, None)   # TypeError: 'b' must be int or float, got NoneType
divide(True, 2)    # TypeError: 'a' must be int or float, got bool
```

## 開発

```bash
# lint
.venv/bin/ruff check .

# 型チェック
.venv/bin/mypy ex_pipeline.py test_pipeline.py

# テスト
.venv/bin/pytest test_pipeline.py -v
```

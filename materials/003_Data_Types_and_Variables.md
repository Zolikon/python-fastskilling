# Data Types and Variables

Python has several built-in data types that are fundamental to programming.

## Numbers

- **int**: Integer values
- **float**: Floating-point numbers
- **complex**: Complex numbers

```python
x = 10        # int
y = 3.14      # float
z = 2 + 3j    # complex
```

## Strings

Strings are sequences of characters:

```python
name = "Alice"
print(name.upper())
```

## Booleans

Boolean values represent `True` or `False`:

```python
is_active = True
```

## None

`None` represents the absence of a value:

```python
result = None
```

## Variable Naming Rules

- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Case-sensitive

## Typing in Python

Python is a dynamically typed language, which means you do not need to declare the type of a variable when you create it. The type is determined at runtime based on the value assigned. This allows for flexibility, but also means that type-related errors may only appear during execution.

```python
x = 5         # x is an int
x = "hello"   # now x is a str
```

You can check the type of a variable using the `type()` function:

```python
value = 42
print(type(value))  # <class 'int'>
```

## Type Hints

Type hints (introduced in Python 3.5) allow you to indicate the expected data types of variables, function arguments, and return values. Type hints do not enforce types at runtime, but they help with code readability and can be checked by static analysis tools like `mypy`.

Example of type hints in function definitions:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b
```

You can also use type hints for variables (Python 3.6+):

```python
age: int = 30
pi: float = 3.1415
```

For more complex types, such as lists or dictionaries, use the `typing` module:

```python
from typing import List, Dict

names: List[str] = ["Alice", "Bob"]
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
```

Continue to the next lecture to learn about Python collections!

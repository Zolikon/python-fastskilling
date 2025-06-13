# Error Handling and Exceptions

Python uses exceptions to handle errors gracefully, allowing you to write robust programs.

## Try and Except

Use `try` and `except` blocks to catch and handle exceptions:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## Else and Finally

- `else` runs if no exception occurs.
- `finally` always runs, even if an exception occurs.

```python
try:
    value = int("42")
except ValueError:
    print("Invalid number!")
else:
    print("Conversion successful!")
finally:
    print("Done.")
```

## Raising Exceptions

You can raise exceptions using `raise`:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
```

## Common Pitfalls

- Catching broad exceptions (`except Exception:`) can hide bugs.
- Not cleaning up resources (use `finally` or context managers).

Next: File I/O in Python!

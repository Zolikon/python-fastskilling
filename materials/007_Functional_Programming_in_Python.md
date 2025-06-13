# Functional Programming in Python: Lambdas, `map`, `filter`, `reduce`, and Passing Functions

Python embraces functional programming concepts, allowing you to use functions as first-class objects. This means you can assign functions to variables, pass them as arguments, and return them from other functions. Functional programming can help you write concise, expressive, and modular code.

---

## Passing Functions as Arguments

You can pass functions as arguments to other functions, enabling higher-order programming. This is useful for applying custom logic or callbacks.

```python
def apply(func, value):
    """Applies a function to a given value."""
    return func(value)

def square(x):
    return x * x

print(apply(square, 5))  # Output: 25
```

Here, `apply` takes a function and a value, and applies the function to the value. This pattern is common in functional programming.

---

## Lambda Functions

Lambda functions are small, anonymous functions defined with the `lambda` keyword. They are useful for short, throwaway functions that are not reused elsewhere.

**Syntax:**

```python
lambda arguments: expression
```

**Example:**

```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

Lambdas are limited to a single expression and cannot contain statements or annotations.

---

## `map`, `filter`, and `reduce`

These built-in functions allow you to process iterables in a functional style.

### `map(func, iterable)`

Applies a function to every item in an iterable, returning a map object (which can be converted to a list).

```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # Output: [1, 4, 9, 16]
```

### `filter(func, iterable)`

Filters items in an iterable, keeping only those for which the function returns `True`.

```python
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4]
```

### `reduce(func, iterable)`

Reduces an iterable to a single value by cumulatively applying a function. `reduce` is available in the `functools` module.

```python
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24
```

---

## Common Pitfalls and Best Practices

- **Lambdas are limited:** They can only contain a single expression. For complex logic, use a regular function.
- **Readability:** Overusing lambdas or functional constructs can make code harder to read. Use them judiciously.
- **Debugging:** Named functions are easier to debug and reuse than anonymous lambdas.

---

## Summary

- Python supports functional programming with first-class functions.
- Use lambdas for simple, short functions.
- `map`, `filter`, and `reduce` enable functional processing of iterables.
- Prefer readability and maintainability over excessive use of functional constructs.

---

**Next:** Explore list, dictionary, and set comprehensions for more concise data processing!

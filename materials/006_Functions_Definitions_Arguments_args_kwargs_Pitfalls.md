# Functions in Python: Definitions, Arguments, `*args`, `**kwargs`, and Common Pitfalls

Functions are fundamental building blocks in Python, enabling you to organize code into reusable, logical units. They help reduce repetition, improve readability, and make code easier to maintain. In Python, functions are **first-class objects**—they can be assigned to variables, passed as arguments, and returned from other functions.

---

## Defining Functions

A function is defined using the `def` keyword, followed by the function name and parentheses containing any parameters. The function body is indented.

```python
def greet(name):
    """Prints a greeting to the given name."""
    print(f"Hello, {name}!")
```

- **Function Name:** `greet`
- **Parameter:** `name`
- **Docstring:** Describes what the function does (optional but recommended).

---

## Return Values

Functions can return values using the `return` statement. If no `return` is specified, the function returns `None` by default.

```python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

result = add(2, 3)  # result is 5
```

- You can return any Python object: numbers, strings, lists, dictionaries, or even other functions.

---

## Default Arguments

You can provide default values for function parameters. If the caller omits an argument, the default is used.

```python
def power(base, exponent=2):
    """Returns base raised to the power of exponent (default is 2)."""
    return base ** exponent

print(power(3))        # 9 (3 squared)
print(power(3, 3))     # 27 (3 cubed)
```

- Default arguments must come after non-default arguments.

---

## Variable-Length Arguments: `*args` and `**kwargs`

Sometimes you don't know in advance how many arguments a function will receive. Python provides two special syntaxes:

- `*args`: Collects extra **positional** arguments as a tuple.
- `**kwargs`: Collects extra **keyword** arguments as a dictionary.

```python
def demo(*args, **kwargs):
    """Prints positional and keyword arguments."""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

demo(1, 2, 3, a=4, b=5)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'a': 4, 'b': 5}
```

- Use `*args` when you want to accept any number of positional arguments.
- Use `**kwargs` when you want to accept any number of keyword arguments.

---

## Common Pitfall: Mutable Default Arguments

Using a mutable object (like a list or dictionary) as a default argument can lead to unexpected behavior. The default value is evaluated only once, so changes persist across function calls.

```python
def append_to_list(value, my_list=[]):
    """Appends value to my_list. Demonstrates a common pitfall."""
    my_list.append(value)
    return my_list

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [1, 2]  <-- Unexpected!
```

**Why is this a problem?**  
The same list is used every time the function is called without a `my_list` argument.

---

### Solution: Use `None` as the Default

A common pattern is to use `None` as the default value and create a new list inside the function if needed.

```python
def append_to_list(value, my_list=None):
    """Appends value to a new list unless a list is provided."""
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [2]
```

---

## Summary

- Functions help organize and reuse code.
- Use default arguments for optional parameters.
- Use `*args` and `**kwargs` for flexible argument lists.
- Avoid mutable default arguments to prevent bugs.

---

**Next:** Explore functional programming concepts in Python!

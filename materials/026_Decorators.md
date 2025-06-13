# Decorators

Decorators are a powerful and flexible feature in Python that allow you to modify or enhance the behavior of functions, methods, or classes without changing their actual code. They are widely used for logging, access control, memoization, and more.

## What is a Decorator?

A decorator is a callable (usually a function or a class) that takes another function or class as an argument and returns a new function or class with extended or altered behavior.

## Function Decorators

The most common use of decorators is with functions. Here’s a simple example:

```python
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**

```
Before function call
Hello!
After function call
```

### Chaining Multiple Decorators

You can apply multiple decorators to a single function:

```python
def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator One")
        return func(*args, **kwargs)
    return wrapper

def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator Two")
        return func(*args, **kwargs)
    return wrapper

@decorator_one
@decorator_two
def greet():
    print("Greetings!")

greet()
```

**Output:**

```
Decorator One
Decorator Two
Greetings!
```

## Built-in Decorators

Python provides several built-in decorators, especially for classes:

- `@staticmethod`: Defines a static method that does not receive an implicit first argument.
- `@classmethod`: Defines a method that receives the class as the first argument instead of the instance.
- `@property`: Allows you to define methods that can be accessed like attributes.

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @staticmethod
    def info():
        print("This is a static method.")

    @classmethod
    def create(cls, value):
        return cls(value)
```

## Decorating Functions with Arguments

Decorators can also accept arguments by defining a decorator factory:

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi!")

greet()
```

**Output:**

```
Hi!
Hi!
Hi!
```

## Preserving Function Metadata

When you write decorators, the metadata (like the function name and docstring) of the original function can be lost. Use `functools.wraps` to preserve it:

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Original docstring"""
    pass

print(example.__name__)      # example
print(example.__doc__)       # Original docstring
```

## Class Decorators

Decorators can also be used to modify classes. A class decorator is a function that takes a class and returns a modified or new class.

```python
def add_repr(cls):
    def __repr__(self):
        return f"<{cls.__name__}({self.__dict__})>"
    cls.__repr__ = __repr__
    return cls

@add_repr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(p)  # Output: <Point({'x': 1, 'y': 2})>
```

## Common Pitfalls

- **Forgetting to return the wrapper function:** If you forget to return the wrapper, the decorated function will be `None`.
- **Losing function metadata:** Always use `functools.wraps` to preserve the original function’s metadata.
- **Incorrect signature in wrapper:** Make sure the wrapper accepts `*args` and `**kwargs` to support all possible arguments.

---

**Next:** Multithreading and multiprocessing!

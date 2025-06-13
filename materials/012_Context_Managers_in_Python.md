# Context Managers in Python

Context managers are a powerful feature in Python that help manage resources such as files, network connections, and locks. They ensure that resources are properly acquired and released, even if errors occur.

## Why Use Context Managers?

- Automatically handle setup and cleanup (e.g., opening and closing files)
- Make code cleaner and less error-prone
- Prevent resource leaks

## Using Built-in Context Managers

The most common example is working with files:

```python
with open('example.txt', 'w') as file:
    file.write('Hello, world!')
# File is automatically closed here
```

## Creating Your Own Context Manager

### 1. Using a Class with **enter** and **exit**

```python
class ManagedResource:
    def __enter__(self):
        print('Resource acquired')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Resource released')

with ManagedResource() as resource:
    print('Using resource')
```

### 2. Using contextlib.contextmanager Decorator

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print('Resource acquired')
    try:
        yield
    finally:
        print('Resource released')

with managed_resource():
    print('Using resource')
```

## Common Pitfalls

- Forgetting to implement both `__enter__` and `__exit__` in custom classes
- Not handling exceptions in `__exit__` or the generator function

Context managers are essential for robust, maintainable Python code, especially when dealing with resources that need explicit cleanup.

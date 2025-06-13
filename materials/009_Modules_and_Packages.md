# Modules and Packages

Modules and packages are essential for organizing and structuring Python code, making it easier to maintain, reuse, and scale.

## Modules

A **module** is any Python file ending with `.py`. Modules allow you to group related code—such as functions, classes, and variables—into a single file.

### Creating and Using Modules

Suppose you have a file called `math_utils.py`:

```python
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159
```

You can import and use these in another file:

```python
# main.py
import math_utils

result = math_utils.add(2, 3)
print(result)
print(math_utils.PI)
```

Or import specific items:

```python
from math_utils import add, PI
print(add(5, 7))
```

### Sharing Common Code

Modules are ideal for sharing common code (like utility functions or constants) across multiple scripts or projects. For example, you might create a `helpers.py` module with functions used throughout your codebase.

## Packages

A **package** is a directory containing an `__init__.py` file (which can be empty or contain initialization code). Packages let you organize modules into hierarchical structures.

Example structure:

```
my_package/
    __init__.py
    math_utils.py
    string_utils.py
```

You can import modules from a package:

```python
from my_package import math_utils
from my_package.string_utils import capitalize_words
```

Packages can also contain subpackages for deeper organization.

## Importing Modules and Packages

- `import module_name` imports the whole module.
- `from module_name import item` imports specific items.
- `from package.module import item` imports from a module inside a package.
- You can use `as` to alias modules or functions:

```python
import math_utils as mu
from my_package.string_utils import capitalize_words as cap
```

## Lifecycle of Imported Items

When you import a module in Python, the code inside that module is executed immediately, but only the first time it is imported during a program’s run. If you import the same module elsewhere, Python uses the already-loaded version from memory (it does not re-execute the code).

### What Happens When You Change a Variable in an Imported Module?

If you change a variable in the imported module from your main script, the change only affects your local reference, not the original module’s variable (unless you directly modify the module’s attribute).

Example:

```python
# math_utils.py
PI = 3.14159
```

```python
# main.py
import math_utils

print(math_utils.PI)  # 3.14159
math_utils.PI = 42
print(math_utils.PI)  # 42
```

Here, changing `math_utils.PI` updates the value for all code that uses `math_utils.PI` after the change. However, if you imported the value directly:

```python
from math_utils import PI
PI = 42
print(PI)  # 42
```

This only changes your local `PI` variable, not the one in `math_utils`.

**Key Points:**

- Module code runs once, at first import.
- Direct changes to module attributes affect all users of that module.
- Changes to imported names (via `from module import item`) only affect your local copy.

## Best Practices and Pitfalls

- Avoid circular imports (modules importing each other).
- Don’t name your modules the same as standard library modules (e.g., `random.py`).
- Use `__init__.py` to control package exports with `__all__`.
- Keep modules focused on a single responsibility.

---

Next: Object-Oriented Programming!

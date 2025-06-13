# Common Pitfalls and Best Practices

Even experienced Python developers can fall into common traps. Here are some to watch out for, and best practices to follow.

## Common Pitfalls

- **Using mutable default arguments (e.g., `def func(x, y=[])`)**  
   Mutable default arguments retain changes between function calls, leading to unexpected behavior and bugs.

- **Modifying a list while iterating over it**  
   Changing a list during iteration can skip elements or cause runtime errors; instead, iterate over a copy or use list comprehensions.

- **Catching broad exceptions (`except Exception:`)**  
   Catching all exceptions can hide bugs and make debugging difficult; catch specific exceptions to handle known error cases.

- **Forgetting to close files (use `with` statement)**  
   Not closing files can lead to resource leaks and data corruption; using the `with` statement ensures files are properly closed.

- **Name conflicts with standard library modules**  
   Naming your files or variables after standard modules (e.g., `random.py`) can shadow the original modules and cause import errors.

- **Not activating virtual environments before installing packages**  
   Installing packages globally can lead to version conflicts and pollute the system Python; always use a virtual environment for project isolation.

- **Shadowing built-in names (e.g., naming a variable `list` or `dict`)**  
   Overwriting built-in names can cause confusing bugs and make code harder to read and maintain.

- **Relying on the order of dictionary keys in versions before Python 3.7**  
   Dictionary key order was not guaranteed before Python 3.7, so relying on it can lead to inconsistent behavior across versions.

- **Using `is` for value equality instead of `==`**  
   The `is` operator checks object identity, not value equality, which can cause subtle bugs when comparing values.

- **Not handling encoding/decoding when working with text files**  
   Ignoring encoding can result in errors or data corruption, especially with non-ASCII text; always specify the correct encoding.

- **Ignoring warnings and error messages**  
   Warnings and errors often indicate real problems; ignoring them can allow bugs and security issues to persist.

- **Overusing global variables**  
   Excessive use of globals makes code harder to understand, test, and maintain, and can lead to unexpected side effects.

## Best Practices

- Follow PEP 8 (Python style guide)
- Use virtual environments for every project
- Write unit tests for your code
- Prefer comprehensions and built-in functions for clarity and speed
- Use docstrings to document your functions and classes
- Profile and optimize only when necessary
- Use type hints to improve code readability and tooling support
- Keep functions small and focused on a single task
- Leverage logging instead of print statements for debugging
- Regularly update dependencies and review security advisories
- Use context managers for resource management
- Refactor duplicated code into reusable functions or classes

Congratulations! You have completed the Python 3.13 training curriculum. Continue practicing and exploring advanced topics as you grow as a Python developer.

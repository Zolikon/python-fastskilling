# Standard Library Overview

Python's standard library is a comprehensive suite of modules that provide solutions for a wide range of programming tasks, from file I/O to data serialization, networking, and more. These modules are included with every Python installation, so you can use them without any additional installation steps.

## Commonly Used Modules and Their APIs

- **os**: Interact with the operating system

  - `os.getcwd()`: Get current working directory
  - `os.listdir(path)`: List files and directories in a given path
  - `os.makedirs(path)`: Create directories recursively
  - `os.remove(path)`: Remove a file
  - `os.environ`: Access environment variables

  ```python
  import os
  print("Current directory:", os.getcwd())
  print("Files:", os.listdir('.'))
  os.environ['MY_VAR'] = 'value'
  print("MY_VAR:", os.environ.get('MY_VAR'))
  ```

- **sys**: Access system-specific parameters and functions

  - `sys.version`: Python version info
  - `sys.argv`: Command-line arguments
  - `sys.exit([arg])`: Exit from Python
  - `sys.path`: List of module search paths

  ```python
  import sys
  print("Python version:", sys.version)
  print("Script arguments:", sys.argv)
  sys.path.append('/my/custom/path')
  ```

- **datetime**: Work with dates and times

  - `datetime.now()`: Current date and time
  - `datetime.strptime()`: Parse strings into datetime objects
  - `datetime.strftime()`: Format datetime objects as strings
  - `timedelta`: Represent time differences

  ```python
  from datetime import datetime, timedelta
  now = datetime.now()
  print("Now:", now)
  yesterday = now - timedelta(days=1)
  print("Yesterday:", yesterday)
  date_str = "2024-06-01"
  parsed = datetime.strptime(date_str, "%Y-%m-%d")
  print("Parsed date:", parsed)
  ```

- **math**: Mathematical functions

  - `math.sqrt(x)`: Square root
  - `math.pi`: Value of pi
  - `math.sin(x)`, `math.cos(x)`: Trigonometric functions
  - `math.factorial(x)`: Factorial

  ```python
  import math
  print("Square root of 16:", math.sqrt(16))
  print("Pi:", math.pi)
  print("Cosine of 0:", math.cos(0))
  print("5! =", math.factorial(5))
  ```

- **random**: Generate random numbers and selections

  - `random.randint(a, b)`: Random integer between a and b
  - `random.choice(seq)`: Random element from a sequence
  - `random.shuffle(seq)`: Shuffle a list in place
  - `random.random()`: Random float between 0 and 1

  ```python
  import random
  print("Random integer (1-10):", random.randint(1, 10))
  items = ['apple', 'banana', 'cherry']
  print("Random choice:", random.choice(items))
  random.shuffle(items)
  print("Shuffled list:", items)
  print("Random float:", random.random())
  ```

## Common Pitfalls

- Overlooking the standard library documentation can lead to unnecessary custom code for problems already solved by built-in modules.
- Some modules have platform-specific behavior (e.g., `os`), so always test on your target platform.
- Be mindful of deprecated APIs in newer Python versions.

**Next:** Dive deeper into the `os` and `sys` modules!

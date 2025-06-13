# os and sys Modules

The `os` and `sys` modules are part of Python's standard library and provide essential functions for interacting with the operating system and the Python interpreter. These modules allow you to perform tasks such as file and directory manipulation, environment variable access, process management, and handling command-line arguments.

---

## os Module

The `os` module provides a way of using operating system dependent functionality like reading or writing to the file system, managing directories, and interacting with environment variables.

### Commonly Used Functions

- **Get current working directory:**

  ```python
  import os
  print(os.getcwd())
  ```

- **Change current working directory:**

  ```python
  os.chdir('/path/to/directory')
  ```

- **List files and directories:**

  ```python
  print(os.listdir('.'))
  ```

- **Create and remove directories:**

  ```python
  os.mkdir('new_dir')
  os.makedirs('parent/child', exist_ok=True)  # Recursive
  os.rmdir('new_dir')
  os.removedirs('parent/child')  # Recursive
  ```

- **Rename and remove files:**

  ```python
  os.rename('old.txt', 'new.txt')
  os.remove('new.txt')
  ```

- **Get environment variables:**

  ```python
  print(os.environ.get('HOME'))
  os.environ['MY_VAR'] = 'value'
  ```

- **Execute a shell command:**

  ```python
  os.system('echo Hello, World!')
  ```

- **Path manipulations (with os.path):**
  ```python
  import os.path
  print(os.path.join('folder', 'file.txt'))
  print(os.path.exists('file.txt'))
  print(os.path.abspath('file.txt'))
  print(os.path.basename('/path/to/file.txt'))
  print(os.path.dirname('/path/to/file.txt'))
  ```

---

## sys Module

The `sys` module provides access to variables and functions that interact closely with the Python interpreter.

### Commonly Used Functions

- **Access command-line arguments:**

  ```python
  import sys
  print(sys.argv)  # List of command-line arguments
  ```

- **Exit the program:**

  ```python
  sys.exit(0)  # 0 for success, non-zero for errors
  ```

- **Get Python version:**

  ```python
  print(sys.version)
  print(sys.version_info)
  ```

- **Standard input/output/error:**

  ```python
  sys.stdout.write('Hello\n')
  sys.stderr.write('Error message\n')
  ```

- **Modify module search path:**

  ```python
  sys.path.append('/my/custom/path')
  ```

- **Get platform information:**

  ```python
  print(sys.platform)
  ```

- **Get reference to the current module:**
  ```python
  print(sys.modules[__name__])
  ```

---

## Common Pitfalls

- Not handling exceptions when working with files or directories (e.g., `FileNotFoundError`, `PermissionError`).
- Relying on platform-specific behavior (e.g., path separators, environment variable names).
- Modifying `sys.path` or `os.environ` can have side effects on other modules or subprocesses.
- Using `os.system` for shell commands is less secure than using the `subprocess` module.

---

**Next:** datetime and time modules!
These modules provide tools for interacting with the operating system and Python runtime.

## os Module

- Get current directory:
  ```python
  import os
  print(os.getcwd())
  ```
- List files in a directory:
  ```python
  print(os.listdir("."))
  ```
- Create/remove directories:
  ```python
  os.mkdir("test_dir")
  os.rmdir("test_dir")
  ```

## sys Module

- Access command-line arguments:
  ```python
  import sys
  print(sys.argv)
  ```
- Exit the program:
  ```python
  sys.exit()
  ```

## Common Pitfalls

- Not handling exceptions when working with files or directories.
- Relying on platform-specific behavior.

Next: datetime and time modules!

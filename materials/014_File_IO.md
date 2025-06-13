# File I/O

File I/O (Input/Output) in Python allows you to interact with files on your filesystem—reading data from files, writing data to files, and manipulating file contents. This is essential for tasks such as data processing, configuration management, and logging.

## Opening Files

To work with files, use the built-in `open()` function. It returns a file object, which you can use to read or write data.

**Syntax:**

```python
file_object = open(file_path, mode, encoding)
```

- `file_path`: Path to the file (relative or absolute).
- `mode`: Mode in which to open the file (see below).
- `encoding`: (Optional) Character encoding (e.g., `"utf-8"`).

**Example: Writing to a file**

```python
file = open("example.txt", "w", encoding="utf-8")
file.write("Hello, file!\n")
file.close()
```

**Example: Reading from a file**

```python
file = open("example.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()
```

## Reading Files

There are several ways to read file contents:

- **Read entire file:**

  ```python
  with open("example.txt", "r") as file:
          data = file.read()
  ```

- **Read line by line:**

  ```python
  with open("example.txt", "r") as file:
          for line in file:
                  print(line.strip())
  ```

- **Read lines into a list:**
  ```python
  with open("example.txt", "r") as file:
          lines = file.readlines()
  ```

## Writing Files

- **Overwrite file:**

  ```python
  with open("output.txt", "w") as file:
          file.write("First line\n")
          file.write("Second line\n")
  ```

- **Append to file:**

  ```python
  with open("output.txt", "a") as file:
          file.write("Appended line\n")
  ```

- **Write multiple lines:**
  ```python
  lines = ["Line 1\n", "Line 2\n"]
  with open("output.txt", "w") as file:
          file.writelines(lines)
  ```

## With Statement

The `with` statement is the recommended way to work with files. It ensures the file is properly closed, even if an error occurs.

```python
with open("example.txt", "r") as file:
        content = file.read()
        print(content)
# File is automatically closed here
```

## File Modes

| Mode | Description                |
| ---- | -------------------------- |
| `r`  | Read (default)             |
| `w`  | Write (overwrite)          |
| `a`  | Append                     |
| `b`  | Binary mode                |
| `x`  | Create, fail if exists     |
| `r+` | Read and write             |
| `w+` | Write and read (overwrite) |
| `a+` | Append and read            |

**Example: Open a binary file for reading**

```python
with open("image.png", "rb") as file:
        data = file.read()
```

## Other Useful File Methods

- `file.readline()`: Reads one line at a time.
- `file.seek(offset)`: Moves the file pointer to a specific position.
- `file.tell()`: Returns the current file pointer position.
- `file.truncate(size)`: Resizes the file to the given size.

**Example:**

```python
with open("example.txt", "r") as file:
        print(file.readline())  # Reads the first line
        file.seek(0)            # Go back to the start
        print(file.read())      # Reads the whole file
```

## Common Pitfalls

- Forgetting to close files (use `with` statement to avoid this).
- Overwriting files unintentionally with `w` mode.
- Not specifying encoding when working with non-ASCII text.
- Reading large files into memory at once (use line-by-line reading for large files).

## Resources

- [Python Official File I/O Documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

Next: Standard library overview!
